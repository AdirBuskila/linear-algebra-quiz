// Tests for aiprompt.js:  node tools/test_aiprompt.js   (build the demo first: see verify_dom.js header)
const fs = require("fs"), path = require("path"), assert = require("assert");
const { JSDOM, VirtualConsole } = require("jsdom");
const ROOT = path.join(__dirname, "..");
const read = f => fs.readFileSync(path.join(ROOT, f), "utf8");
let fail = 0;
function t(name, fn) { try { fn(); console.log("  ok  " + name); } catch (e) { fail++; console.log("FAIL  " + name + "\n      " + e.message); } }

function boot(full) {
  const errors = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => errors.push(e.message || String(e)));
  const dom = new JSDOM(read("index.html"), { pretendToBeVisual: true, runScripts: "outside-only", url: "http://localhost/index.html", virtualConsole: vc });
  const w = dom.window;
  w.scrollTo = () => {}; w.HTMLElement.prototype.scrollIntoView = () => {}; w.confirm = () => true;
  w.matchMedia = w.matchMedia || (q => ({ matches: false, media: q, addEventListener() {}, removeEventListener() {} }));
  w.opened = []; w.open = (...a) => { w.opened.push(a); return null; };
  const files = full
    ? [...w.document.querySelectorAll("script[src]")].map(s => s.getAttribute("src").split("?")[0]).filter(s => !/^(https?:)?\/\//.test(s))
    : ["aiprompt.js"];
  for (const f of files) { if (f === "learn.js" && !fs.existsSync(path.join(ROOT, f))) continue;   // optional: only built when briefs exist (same as verify_dom)
    try { w.eval(read(f)); } catch (e) { errors.push(f + ": " + e.message); } }
  return { w, errors };
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
const noClipboard = w => Object.defineProperty(w.navigator, "clipboard", { value: undefined, configurable: true });
const bank = boot(true).w.OPEN_BANK;
const byKind = k => bank.questions.find(q => q.kind === k);
const AP = boot(false).w.AiPrompt;

t("API present", () => { assert.ok(AP && typeof AP.build === "function" && typeof AP.open === "function"); });

const proof = byKind("proof"), comp = byKind("computation"), code = byKind("code");
const P = AP.build(proof, { answerText: "הוכחה שלי כאן", photo: false });
t("prompt has question, solution, every rubric line + points", () => {
  assert.ok(P.includes(proof.question));
  assert.ok(P.includes(proof.solution));
  for (const r of proof.rubric) { assert.ok(P.includes(r.text), r.text); assert.ok(P.includes(r.points + " נק"), "pts " + r.points); }
});
t("solution is labelled by source: official only when q.official", () => {
  assert.strictEqual(proof.official, true);
  assert.ok(P.includes("הפתרון הרשמי:\n" + proof.solution));
  const U = AP.build(Object.assign({}, proof, { official: false }), { answerText: "x", photo: false });
  assert.ok(U.includes("פתרון לדוגמה (לא רשמי):\n" + proof.solution), "unofficial label");
  assert.ok(!U.includes("הפתרון הרשמי"), "an unofficial solution is never called official");
});
t("student answer included, no photo line", () => {
  assert.ok(P.includes("הוכחה שלי כאן"));
  assert.ok(!P.includes("מצורפת תמונה"));
});
t("proof / computation / code instructions are kind-specific", () => {
  const C = AP.build(comp, { answerText: "x", photo: false });
  assert.ok(P.includes("תקפות לוגית") && !C.includes("תקפות לוגית"));
  assert.ok(C.includes("השורה השגויה הראשונה") && C.includes("הערך הסופי") && !P.includes("הערך הסופי"));
  assert.ok(AP.build(code, { answerText: "x", photo: false }).includes("מקרי קצה"));
});
t("common rules: grade vs rubric, quote first wrong line, not restate solution", () => {
  assert.ok(P.includes("לפי המחוון") && P.includes("צטט") && P.includes("אל תסתפק"));
});
t("photo:true has photo line and no empty answer block", () => {
  const X = AP.build(proof, { answerText: "", photo: true });
  assert.ok(X.includes("מצורפת תמונה של הפתרון שלי בכתב יד"));
  assert.ok(!X.includes("התשובה שלי:"));
  assert.ok(!AP.build(proof, { answerText: "   ", photo: false }).includes("התשובה שלי:"), "blank text, no photo -> no empty block");
});
t("output format section", () => {
  assert.ok(P.includes("ציון לכל שורת מחוון") && P.includes("טיפ אחד"));
});
t("no HTML tags in any question's prompt; TeX kept raw", () => {
  for (const q of bank.questions) {
    const s = AP.build(q, { answerText: "ans", photo: false });
    assert.ok(!/<\/?[a-zA-Z][^>]*>/.test(s), q.id + " has a tag");
  }
  assert.ok(/\$[^$]+\$/.test(comp.question) ? AP.build(comp, { answerText: "", photo: true }).includes(comp.question) : true);
});

(async () => {
  const A = boot(true).w;
  noClipboard(A);
  A.AiPrompt.open("claude", "PROMPT TEXT");
  t("no clipboard -> modal read-only textarea with prompt", () => {
    const ta = A.document.querySelector(".aip-modal textarea");
    assert.ok(ta && ta.value === "PROMPT TEXT" && ta.readOnly);
  });
  t("opens target in new tab", () => { assert.strictEqual(A.opened[0][0], "https://claude.ai/new"); assert.strictEqual(A.opened[0][1], "_blank"); });
  t("modal closes", () => { A.document.querySelector(".aip-modal .aip-close").click(); assert.ok(!A.document.querySelector(".aip-modal")); });
  t("target urls", () => {
    A.AiPrompt.open("chatgpt", "x"); A.AiPrompt.open("gemini", "x");
    assert.strictEqual(A.opened[1][0], "https://chatgpt.com/"); assert.strictEqual(A.opened[2][0], "https://gemini.google.com/app");
  });

  const B = boot(true).w;
  Object.defineProperty(B.navigator, "clipboard", { value: { writeText: () => Promise.reject(new Error("no")) }, configurable: true });
  B.AiPrompt.open("gemini", "REJ"); await sleep(10);
  t("clipboard rejection -> modal", () => { assert.strictEqual(B.document.querySelector(".aip-modal textarea").value, "REJ"); });
  let copied = null;
  const C = boot(true).w;
  Object.defineProperty(C.navigator, "clipboard", { value: { writeText: s => { copied = s; return Promise.resolve(); } }, configurable: true });
  C.AiPrompt.open("chatgpt", "OK"); await sleep(10);
  t("clipboard ok -> copied, no modal", () => { assert.strictEqual(copied, "OK"); assert.ok(!C.document.querySelector(".aip-modal")); });

  const O = boot(true).w, order = [];
  Object.defineProperty(O.navigator, "clipboard", { value: { writeText: () => { order.push("write"); return Promise.resolve(); } }, configurable: true });
  O.open = () => { order.push("open"); return null; };
  O.AiPrompt.open("claude", "X");
  t("writeText is called before window.open", () => { assert.deepStrictEqual(order, ["write", "open"]); });

  // in-app: slot UI + photo toggle + click builds the prompt from the attempt textarea
  const D = boot(true), d = D.w, doc = d.document;
  noClipboard(d);
  const click = el => el.dispatchEvent(new d.MouseEvent("click", { bubbles: true, cancelable: true }));
  const r = doc.querySelector('input[name=mode][value="exam"]'); r.checked = true; r.dispatchEvent(new d.Event("change", { bubbles: true }));
  doc.querySelector("#examPick").value = "DEMO-A"; doc.querySelector("#examPick").dispatchEvent(new d.Event("change", { bubbles: true }));
  click(doc.querySelector("#startBtn"));
  for (let i = 0; i < 10 && !doc.querySelector(".ai-grade-slot"); i++) click(doc.querySelector("#nextBtn"));
  const slot = doc.querySelector(".ai-grade-slot");
  t("slot UI: photo toggle + 3 buttons", () => {
    assert.ok(slot.querySelector("input[type=checkbox]"));
    assert.strictEqual(slot.querySelectorAll("button[data-target]").length, 3);
  });
  const ta0 = doc.querySelector("#attempt"); ta0.value = "הניסיון שלי 123"; ta0.dispatchEvent(new d.Event("input", { bubbles: true }));
  click(slot.querySelector('button[data-target="gemini"]'));
  t("click -> modal prompt built from the attempt, gemini tab", () => {
    const m = doc.querySelector(".aip-modal textarea");
    assert.ok(m && m.value.includes("הניסיון שלי 123"));
    assert.strictEqual(d.opened.pop()[0], "https://gemini.google.com/app");
  });
  doc.querySelector(".aip-modal .aip-close").click();
  slot.querySelector("input[type=checkbox]").checked = true;
  click(slot.querySelector('button[data-target="chatgpt"]'));
  t("photo toggle -> photo line, attempt omitted", () => {
    const v = doc.querySelector(".aip-modal textarea").value;
    assert.ok(v.includes("מצורפת תמונה של הפתרון שלי בכתב יד") && !v.includes("הניסיון שלי 123"));
  });
  t("no page errors", () => { assert.deepStrictEqual(D.errors, []); });
  console.log(fail ? `\n${fail} FAILED` : "\nall ok");
  process.exit(fail ? 1 : 0);
})();
