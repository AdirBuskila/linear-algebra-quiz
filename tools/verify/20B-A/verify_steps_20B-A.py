# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 20B-A (rubric/pitfalls/steps in tools/gen/gen_20B-A.py).
Run: PYTHONUTF8=1 py tools/verify/20B-A/verify_steps_20B-A.py
Every numeric step in tools/raw/20B-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug / order line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "20B-A.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_ = "א", "ב", "ג", "ד"
R = sp.Rational
M = sp.Matrix
bad = []
EXP = {}


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def exp(num, part, idx, val):
    EXP[(num, part, idx)] = val if isinstance(val, sp.Float) else sp.nsimplify(val)


k = sp.symbols("k")
# ---- Q1a
M1 = M([1, 2, 0]); M2 = M([0, 3, -2]); a1 = M([1, k, 2]); a2 = M([2, 1, 1])
d12 = M2 - M1
exp(1, A_, 1, d12[1])
det = sp.Matrix.hstack(d12, a1, a2).T.det()
chk("Q1a determinant = 3k+3", sp.expand(M([[*d12], [*a1], [*a2]]).det() - (3 * k + 3)) == 0)
exp(1, A_, 2, (3 * k + 3).subs(k, 0)); exp(1, A_, 3, sp.solve(3 * k + 3, k)[0])
chk("Q1a at k=0 the determinant equals 3", M([[*d12], [*a1.subs(k, 0)], [*a2]]).det() == 3)
# real intersection check at k=-1: solve l1 = l2
s, u = sp.symbols("s u")
l1 = M1 + s * a1.subs(k, -1); l2 = M2 + u * a2
sol = sp.solve(list(l1 - l2), [s, u], dict=True)
chk("Q1a lines intersect at k=-1", len(sol) == 1)
a1m = a1.subs(k, -1)
chk("Q1a distractors at k=-1: dot != 0, cross != 0, det == 0", a1m.dot(a2) == 3 and a1m.cross(a2) != sp.zeros(3, 1) and M([[*d12], [*a1m], [*a2]]).det() == 0)
chk("Q1a lines at k=-4 do not intersect", len(sp.solve(list(M1 + s * a1.subs(k, -4) - l2), [s, u], dict=True)) == 0)

# ---- Q1b (k=2)
a12 = a1.subs(k, 2)
cr = a12.cross(a2)
exp(1, B_, 1, cr[1])
tp = cr.dot(d12)
exp(1, B_, 2, tp)
dist = sp.Abs(tp) / cr.norm()
exp(1, B_, 3, sp.Float(sp.N(dist)))
chk("Q1b d = 3*sqrt(2)/2", sp.simplify(dist - 3 * sp.sqrt(2) / 2) == 0)
chk("Q1b distractors: |M1M2|=sqrt6, |a1.a2|/|axb|, |axb|/|M1M2| are not d",
    all(sp.N(v) != sp.N(dist) for v in (d12.norm(), sp.Abs(a12.dot(a2)) / cr.norm(), cr.norm() / d12.norm())))
# distance by minimisation
dd = (M1 + s * a12 - M2 - u * a2)
mm = sp.solve([sp.diff(dd.dot(dd), s), sp.diff(dd.dot(dd), u)], [s, u], dict=True)[0]
chk("Q1b min distance by calculus", sp.simplify(sp.sqrt(dd.dot(dd).subs(mm)) - dist) == 0)

# ---- Q1c
va = M([1, 0, 0]); vb = M([1, 1, 0]); vc = M([0, 1, 0])
chk("Q1c counterexample a x b = a x c != 0, b != c", va.cross(vb) == va.cross(vc) != sp.zeros(3, 1) and vb != vc)
exp(1, C_, 1, va.cross(vb)[2]); exp(1, C_, 2, (vb - vc)[0])
chk("Q1c distractors: b-c = a (parallel, nonzero, not perpendicular), a nonzero", (vb - vc) == va and va.dot(vb - vc) != 0)

# ---- Q2
A2 = M([[1, -1, 1], [k - 1, k + 1, k + 1], [k, -2 - k, -k]]); b2 = M([1, k + 1, 1])
S = A2.row_join(b2)
S[1, :] = S[1, :] - (k - 1) * S[0, :]; S[2, :] = S[2, :] - k * S[0, :]
S1 = S.applyfunc(sp.expand)
chk("Q2a S1 rows", S1[1, :] == M([[0, 2 * k, 2, 2]]) and S1[2, :] == M([[0, -2, -2 * k, 1 - k]]))
exp(2, A_, 1, S1[1, 1].subs(k, 3)); exp(2, A_, 2, S1[2, 3].subs(k, 3))
S2 = S1.copy(); S2.row_swap(1, 2); S2[1, :] = -S2[1, :]
chk("Q2a swap with sign gives (0,2,2k|k-1),(0,2k,2|2)", S2[1, :] == M([[0, 2, 2 * k, k - 1]]) and S2[2, :] == M([[0, 2 * k, 2, 2]]))
S3 = S2.copy(); S3[2, :] = (S3[2, :] - k * S3[1, :]).applyfunc(sp.expand)
chk("Q2a final row 3 = (0,0,2-2k^2 | 2+k-k^2)", S3[2, :] == M([[0, 0, 2 - 2 * k ** 2, 2 + k - k ** 2]]))
exp(2, A_, 3, S3[2, 2].subs(k, 2))
for nm, c in (("R3-kR2", k), ("R3+kR2", -k), ("R3-R2", 1), ("R3-2kR2", 2 * k)):
    zeroed = sp.expand(S2[2, 1] - c * S2[1, 1]) == 0
    chk("Q2a operation %s zeroes (3,2) generically -> %s" % (nm, zeroed), zeroed == (nm == "R3-kR2"))


def rk(kv):
    return A2.subs(k, kv).rank(), S.subs(k, kv).rank() if False else A2.row_join(b2).subs(k, kv).rank()


exp(2, B_, 0, rk(1)[0]); exp(2, B_, 1, rk(1)[1]); exp(2, B_, 2, rk(-1)[1])
chk("Q2b k=1 no solution (2,3); k=-1 infinite (2,2); others unique (3,3)", rk(1) == (2, 3) and rk(-1) == (2, 2) and all(rk(v) == (3, 3) for v in (0, 2, 3, -3)))
Am1 = A2.subs(k, -1); bm1 = b2.subs(k, -1)
x, y, z = sp.symbols("x y z")
sl = sp.solve(list(Am1 * M([x, y, z]) - bm1), [x, y], dict=True)[0]
chk("Q2c k=-1 solution x=0, y=z-1", sl[x] == 0 and sp.simplify(sl[y] - (z - 1)) == 0)
exp(2, C_, 0, sl[x]); exp(2, C_, 1, sl[y].subs(z, 3))
for nm, v, ok in (("(0,1,1)", M([0, 1, 1]), True), ("(-2,-1,1)", M([-2, -1, 1]), False), ("(1,1,1)", M([1, 1, 1]), False), ("(0,-1,0)", M([0, -1, 0]), False)):
    chk("Q2c direction %s in null space is %s" % (nm, ok), (Am1 * v == sp.zeros(3, 1)) == ok)

# ---- Q3
A3 = M([[1, 0, 1, 1], [1, 1, 2, 0], [0, 1, 1, -1]])
exp(3, A_, 0, A3.rank())
ns = A3.nullspace()
chk("Q3a null space dim 2, spanned by (-1,-1,1,0),(-1,1,0,1)", len(ns) == 2 and A3 * M([-1, -1, 1, 0]) == sp.zeros(3, 1) and A3 * M([-1, 1, 0, 1]) == sp.zeros(3, 1))
exp(3, A_, 2, (2 * M([-1, -1, 1, 0]) + M([-1, 1, 0, 1]))[1])
for nm, v, ok in (("(-1,1,0,1)", [-1, 1, 0, 1], True), ("(1,-1,1,0)", [1, -1, 1, 0], False), ("(1,1,1,1)", [1, 1, 1, 1], False), ("(0,0,1,1)", [0, 0, 1, 1], False)):
    chk("Q3a vector %s in null space is %s" % (nm, ok), (A3 * M(v) == sp.zeros(3, 1)) == ok)
exp(3, B_, 0, A3.rank())
r1, r2, r3 = A3.row(0), A3.row(1), A3.row(2)
chk("Q3b R3 = R2 - R1 (c=1, d=-1) and the 3 rows are dependent", r3 == r2 - r1 and M([r1, r2, r3]).rank() == 2)
exp(3, B_, 1, -1)
exp(3, C_, 0, A3.rank())
c1, c2, c4 = A3.col(0), A3.col(1), A3.col(3)
chk("Q3c col4 = col1 - col2; four columns dependent; (1,0,0) not in Col A",
    c4 == c1 - c2 and A3.rank() < 4 and sp.Matrix.hstack(A3, M([1, 0, 0])).rank() == 3)
exp(3, C_, 2, -1)
exp(3, D_, 0, A3.shape[1])
chk("Q3d rank-nullity: nullity+rank=4 columns, not 3 rows", len(ns) + A3.rank() == 4 and 4 != A3.shape[0])
chk("Q3d distractors: nullity != rank is a coincidence here; product 4 = 4 coincides", len(ns) == A3.rank() and len(ns) * A3.rank() == 4)

# ---- Q4
a = sp.symbols("a")
A4 = M([[2 * a, 4, 4 + 2 * a], [a, 3, 5], [1, 1, a]])
chk("Q4a det = 4(a-1)(a-2)", sp.expand(A4.det() - 4 * (a - 1) * (a - 2)) == 0)
exp(4, A_, 0, A4.det().subs(a, 4)); exp(4, A_, 1, A4.det().subs(a, 0))
chk("Q4a singular exactly at a=1,2", set(sp.solve(A4.det(), a)) == {1, 2} and A4.det().subs(a, -1) != 0 and A4.det().subs(a, -2) != 0)
A40 = A4.subs(a, 0)
exp(4, B_, 0, A40.det()); exp(4, B_, 1, sp.Float(sp.N(A40.inv()[0, 0]))); exp(4, B_, 2, A40.inv()[2, 1])
chk("Q4b inverse", A40.inv() == M([[R(-5, 8), R(1, 2), 1], [R(5, 8), R(-1, 2), 0], [R(-3, 8), R(1, 2), 0]]))
B4 = M([[3, 1, 0], [0, 2, 0], [1, 1, 4]])
exp(4, C_, 0, B4.trace()); exp(4, C_, 1, B4.det())
chk("Q4c eigenvalues 2,3,4", B4.eigenvals() == {2: 1, 3: 1, 4: 1})
for nm, v, ok in (("(-1,1,0)", [-1, 1, 0], True), ("(1,1,0)", [1, 1, 0], False), ("(-1,0,1)", [-1, 0, 1], False), ("(0,0,1)", [0, 0, 1], False)):
    chk("Q4c %s eigenvector for 2 is %s" % (nm, ok), (B4 * M(v) == 2 * M(v)) == ok)
chk("Q4c other eigenvectors: (-1,0,1) for 3, (0,0,1) for 4", B4 * M([-1, 0, 1]) == 3 * M([-1, 0, 1]) and B4 * M([0, 0, 1]) == 4 * M([0, 0, 1]))
P4 = M([[-1, -1, 0], [1, 0, 0], [0, 1, 1]]); D4 = sp.diag(2, 3, 4)
chk("Q4d P^-1 B P = D", P4.inv() * B4 * P4 == D4)
exp(4, D_, 0, P4.det()); exp(4, D_, 1, (P4 * D4)[0, 1])
for lamv, ok in ((3, True), (2, False), (4, False), (0, False)):
    chk("Q4d column 2 of P eigen for %s is %s" % (lamv, ok), (B4 * P4[:, 1] == lamv * P4[:, 1]) == ok)

# ---- Q5
al, c_, aa = sp.symbols("alpha c_ aa")
def Wm(a, c): return M([[a, 2 * a], [-a, c]])
chk("Q5a closure under addition and scalar multiple", sp.simplify(Wm(1, 2) + Wm(2, 5) - Wm(3, 7)) == sp.zeros(2, 2) and sp.simplify(al * Wm(aa, c_) - Wm(al * aa, al * c_)) == sp.zeros(2, 2))
exp(5, A_, 2, (Wm(1, 0) + Wm(2, 0))[0, 1])
bug = M([[al * aa, 2 * aa], [-al * aa, al * c_]])
chk("Q5a bug matrix is not in W for alpha != 1", sp.simplify(bug[0, 1] - 2 * bug[0, 0]) != 0)
Wa = M([[1, 2], [-1, 0]])
chk("Q5a W not closed under matrix multiplication: (1 2;-1 0)^2 not in W", (Wa * Wa)[0, 1] != 2 * (Wa * Wa)[0, 0])
chk("Q5a {e1,e2} contains a basis yet is not a subspace (e1+e2 not in the set)", True and (M([1, 1]) != M([1, 0]) and M([1, 1]) != M([0, 1])))
exp(5, B_, 0, 2)
bW = [Wa, M([[0, 0], [0, 1]])]
chk("Q5b basis in W, independent", all(m[0, 1] == 2 * m[0, 0] and m[1, 0] == -m[0, 0] for m in bW) and sp.Matrix.hstack(*[M(list(m)) for m in bW]).rank() == 2)
chk("Q5b distractors: dependent / not spanning / (0 1;0 0) not in W",
    sp.Matrix.hstack(M(list(Wa)), M(list(2 * Wa))).rank() == 1 and 2 > 1 and M([[0, 1], [0, 0]])[0, 1] != 2 * M([[0, 1], [0, 0]])[0, 0])
exp(5, B_, 2, 5)
chk("Q5b coordinates of (2 4;-2 5): a=2, c=5", Wm(2, 5) == 2 * Wa + 5 * M([[0, 0], [0, 1]]))
w1 = M([1, 2, -1, 0]); w2 = M([0, 0, 0, 1]); u1 = M([-1, 2, 1, -3]); u2 = M([1, 0, -1, 2])
big = sp.Matrix.hstack(w1, w2, u1, u2)
exp(5, C_, 0, big.rank())
inter = sp.Matrix.hstack(w1, w2).row_join(-sp.Matrix.hstack(u1, u2)).nullspace()
chk("Q5c intersection dimension 1", len(inter) == 1)
iv = sp.Matrix.hstack(w1, w2) * M(list(inter[0][:2]))
iv = iv / iv[0]
chk("Q5c intersection basis (1,2,-1,1)", iv == M([1, 2, -1, 1]))
exp(5, C_, 2, iv[2])
chk("Q5c distractor formulas give 7, 4, 4 != 1", 2 + 2 + big.rank() == 7 and 2 * 2 == 4 and 2 + 2 == 4 and 2 + 2 - big.rank() == 1)
exp(5, D_, 1, (M([[1, 1], [1, 1]]))[0, 0] + M([[1, 1], [1, 1]])[0, 1])
Cm = M([[1, 1], [1, 1]])
chk("Q5d (1 1;1 1) not in W; other options in W", Cm[0, 1] != 2 * Cm[0, 0] and all(m[0, 1] == 2 * m[0, 0] and m[1, 0] == -m[0, 0] for m in (M([[1, 2], [-1, 5]]), M([[0, 0], [0, 3]]), M([[2, 4], [-2, 0]]))))

# ---- Q6
a_, b_, c6, d_ = sp.symbols("a b c d")
Tm = M([[1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1]])
exp(6, A_, 0, Tm.rank())
kn = Tm.nullspace()
exp(6, A_, 1, len(kn))
chk("Q6a kernel (1,-1,1,1)", kn[0] / kn[0][0] == M([1, -1, 1, 1]))
for nm, v, ok in (("(1,-1,1,1)", [1, -1, 1, 1], True), ("(1,1,1,1)", [1, 1, 1, 1], False), ("(1,0,0,1)", [1, 0, 0, 1], False), ("(1,-1,1,-1)", [1, -1, 1, -1], False)):
    chk("Q6a matrix %s in ker is %s" % (nm, ok), (Tm * M(v) == sp.zeros(3, 1)) == ok)
exp(6, A_, 3, (2 * kn[0] / kn[0][0])[1])
exp(6, B_, 0, Tm.rank())
exp(6, B_, 2, (Tm * M([0, 1, 0, 0]))[1])
chk("Q6b Im T = R^3 (rank 3); ker not trivial so T not injective", Tm.rank() == 3 and len(kn) == 1)
exp(6, C_, 1, len(kn))
part = M([0, 1, 0, 0]); tgt = M([1, 1, 1])
sol6 = sp.symbols("d6")
gen = M([sol6, 1 - sol6, sol6, sol6])
chk("Q6d preimage of (1,1,1) is (d,1-d,d,d)", sp.simplify(Tm * gen - tgt) == sp.zeros(3, 1))
exp(6, D_, 0, gen[1].subs(sol6, 2)); exp(6, D_, 1, gen[2].subs(sol6, 2))
chk("Q6d zero matrix not in preimage; kernel elements map to 0 not (1,1,1); set nonempty", Tm * M([0, 0, 0, 0]) != tgt and Tm * kn[0] != tgt and Tm * gen.subs(sol6, 0) == tgt)

# ---- coverage
n = 0
for (num, part_), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] != "numeric":
            continue
        n += 1
        key = (num, part_, i)
        if key not in EXP:
            chk("Q%d%s step %d has an expected value" % (num, part_, i), False)
            continue
        ok = abs(sp.N(EXP[key]) - st["answer"]) <= st.get("tol", 0) + 1e-12
        chk("Q%d%s step %d numeric answer %s == sympy %s (tol %s)" % (num, part_, i, st["answer"], sp.N(EXP[key], 6), st.get("tol", 0)), ok)
extra = set(EXP) - {(num, part_, i) for (num, part_), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
for (num, part_), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] == "choice":
            ids = [o["id"] for o in st["options"]]
            vals = [o["value"] for o in st["options"]]
            chk("Q%d%s step %d choice has distinct options and valid key" % (num, part_, i), st["correctId"] in ids and len(set(vals)) == len(vals))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
