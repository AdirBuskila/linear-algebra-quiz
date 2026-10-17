"use strict";
/* Answer normalisers for the step widgets (window.Normalize). Pure functions, no DOM, no state.
   text(s)       free text: trim, collapse whitespace, case-fold, drop a trailing period.
   complexity(s) asymptotic notation: spaces stripped, log/lg/log_2/log2 -> log, n² / n^{2} -> n^2,
                 Θ and O both accepted as written (Θ is folded onto O so either grades the same), case-insensitive.
   number(s)     decimal comma allowed, unicode minus, simple fractions "a/b"; NaN when it is not a number. */
(function (root) {
  const SUP = { "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9" };

  function text(s) {
    return String(s == null ? "" : s).normalize("NFKC").toLowerCase().replace(/\s+/g, " ").trim().replace(/[.。]+$/, "").trim();
  }

  function complexity(s) {
    let t = String(s == null ? "" : s).normalize("NFC");
    t = t.replace(/[Θθ]/g, "O").replace(/\\(?:Theta|theta|Omicron)/g, "O");
    t = t.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]+/g, m => "^" + [...m].map(c => SUP[c]).join(""));
    t = t.toLowerCase().replace(/\s+/g, "").replace(/\\/g, "");
    t = t.replace(/[·⋅*×]/g, "");                     // "n·log n" -> "nlog n"
    t = t.replace(/\^\{([^{}]*)\}/g, "^$1").replace(/_\{([^{}]*)\}/g, "_$1");
    t = t.replace(/log(?:_?2|₂)?(?![a-z])/g, "log");   // log, log2, log_2, log₂ -> log
    t = t.replace(/lg/g, "log");
    t = t.replace(/log(?:_?2|₂)/g, "log");
    return t;
  }

  function number(s) {
    let t = String(s == null ? "" : s).replace(/[−–—]/g, "-").replace(/\s+/g, "");
    if (!t) return NaN;
    const frac = /^(-?[0-9]+(?:[.,][0-9]+)?)\/([0-9]+(?:[.,][0-9]+)?)$/.exec(t);
    const val = x => Number(x.replace(",", "."));
    if (frac) { const d = val(frac[2]); return d === 0 ? NaN : val(frac[1]) / d; }
    if (!/^[+-]?(?:[0-9]+(?:[.,][0-9]*)?|[.,][0-9]+)$/.test(t)) return NaN;
    return val(t);
  }

  const api = { text, complexity, number };
  root.Normalize = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
})(typeof window !== "undefined" ? window : globalThis);
