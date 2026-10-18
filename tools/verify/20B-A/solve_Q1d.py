# -*- coding: utf-8 -*-
"""sympy solve + check of 20B-A Q1d (no official solution): z^3 + (3i-4) z = 0.
Run: PYTHONUTF8=1 py tools/verify/20B-A/solve_Q1d.py  (ASCII output)"""
import json, pathlib
import sympy as sp

z = sp.symbols("z")
eq = z ** 3 + (3 * sp.I - 4) * z
roots = sp.roots(sp.Poly(eq, z))
expected = {0, (3 - sp.I) / sp.sqrt(2), -(3 - sp.I) / sp.sqrt(2)}
got = {sp.simplify(r) for r in roots}
assert len(got) == 3 and all(sp.simplify(eq.subs(z, r)) == 0 for r in expected), roots
assert all(any(sp.simplify(e - g) == 0 for g in got) for e in expected), (got, expected)
print("OK roots:", sorted(map(str, got)))
a, b = sp.symbols("a b", real=True)
s = sp.solve([a ** 2 - b ** 2 - 4, 2 * a * b + 3], [a, b], dict=True)
assert len(s) == 2 and all(abs(sp.simplify(d[a] ** 2 - sp.Rational(9, 2))) == 0 and sp.simplify(d[b] ** 2 - sp.Rational(1, 2)) == 0 for d in s), s
print("OK a^2=9/2, b^2=1/2, ab=-3/2")
assert sp.Abs(4 - 3 * sp.I) == 5
assert abs(float(3 / sp.sqrt(2)) - 2.121) < 1e-3 and abs(float(-1 / sp.sqrt(2)) + 0.707) < 1e-3
# wrong-first-step distractors fail: dividing by z loses z=0 (which satisfies the equation)
assert eq.subs(z, 0) == 0
# step values in the generated raw json match
raw = json.loads((pathlib.Path(__file__).resolve().parents[3] / "tools" / "raw" / "20B-A.json").read_text(encoding="utf-8"))
q = [x for x in raw["questions"] if x["num"] == 1 and x.get("part") == "ד"][0]
assert q["solutionSource"] == "solved" and q["official"] is False and not q.get("hold")
assert q["stepsSource"] == "ai-draft" and q["rubricSource"] == "ai-draft"
assert [st["answer"] for st in q["steps"] if st["type"] == "numeric"] == [5, 2.121, -0.707]
print("OK raw Q1d: solved, official False, ai-draft, numeric steps match")
