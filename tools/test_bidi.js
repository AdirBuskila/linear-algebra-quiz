// Plain-node unit tests for the render-time bidi fixes (window.Bidi in normalize.js):  node tools/test_bidi.js
const assert = require("assert");
const path = require("path");
global.window = {};
require(path.join(__dirname, "..", "normalize.js"));
const B = global.window.Bidi;
assert.ok(B && typeof B.render === "function", "Bidi API");

const label = l => `<bdi class="ltr nw opt-label" dir="ltr">${l}</bdi>`;
const ltr = t => `<bdi class="ltr nw" dir="ltr">${t}</bdi>`;

// option-label lines: the label (period included) is one LTR isolate at the line start
assert.strictEqual(B.render("a. סכום x ו-y"), `${label("a.")} סכום ${ltr("x")} ו-${ltr("y")}`);
assert.strictEqual(B.render("שאלה:<br>c. x עם סימן הפוך"), `שאלה:<br>${label("c.")} ${ltr("x")} עם סימן הפוך`);
assert.strictEqual(B.render("e. אף אחת מהתשובות לעיל לא נכונה"), `${label("e.")} אף אחת מהתשובות לעיל לא נכונה`);
assert.strictEqual(B.render("x<br>(b) שלום"), `${ltr("x")}<br>${label("(b)")} שלום`);
const many = B.render("שאלה<br>a. סכום x ו-y<br>b. מכפלת x ו-y<br>c. x עם סימן הפוך<br>e. אף אחת מהתשובות לעיל לא נכונה");
assert.strictEqual((many.match(/opt-label/g) || []).length, 4, "four labels");
assert.ok(!/(^|<br>)[a-e]\./.test(many), "no bare label left at a line start");

// idempotent
assert.strictEqual(B.render(B.render("a. סכום x ו-y")), B.render("a. סכום x ו-y"));

// a sentence ending with a formula keeps its period inside the formula's LTR isolate
const f = '<span class="math-inline"><math><mi>x</mi></math></span>';
assert.strictEqual(B.render(`הערך הוא ${f}.`), `הערך הוא <span class="math-run" dir="ltr">${f}.</span>`);
assert.strictEqual(B.render(`הערך הוא ${f}.<br>שורה`), `הערך הוא <span class="math-run" dir="ltr">${f}.</span><br>שורה`);
// formulas chained by punctuation form one run
assert.ok(B.render(`${f}, ${f}`).startsWith('<span class="math-run" dir="ltr">'));
// a period mid-sentence is left alone
assert.strictEqual(B.render(`${f}. אחר כך`), `${f}. אחר כך`);

// code blocks, inline code and math are untouched
const pre = '<pre class="code-block" dir="ltr"><code>a. x\nb. y</code></pre>';
assert.strictEqual(B.render(pre), pre);
assert.strictEqual(B.render(`שלום<br>${pre}`), `שלום<br>${pre}`);
const code = '<code class="tok" dir="ltr">a. x</code>';
assert.strictEqual(B.render(`<br>${code} ו`), `<br>${code} ו`);
const math = '<span class="math-block"><math><mi>a</mi><mo>.</mo></math></span>';
assert.strictEqual(B.render(math), math);

// plain Hebrew and a Latin-free line are unchanged
assert.strictEqual(B.render("שלום עולם."), "שלום עולם.");
assert.ok(!B.render("e.g. משהו").includes("opt-label"), "e.g. is not an option label");

console.log("test_bidi: ok");
