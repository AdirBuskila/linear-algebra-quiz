# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 23A-A (rubric/pitfalls/steps in tools/gen/gen_23A-A.py).
Run: PYTHONUTF8=1 py tools/verify/23A-A/verify_steps_23A-A.py
Every numeric step in tools/raw/23A-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / order / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "23A-A.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_ = "א", "ב", "ג", "ד"
R = sp.Rational
V = sp.Matrix
bad = []
EXP = {}


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def exp(num, part, idx, val):
    EXP[(num, part, idx)] = sp.nsimplify(val)


k = sp.symbols("k")
cc, dd = sp.symbols("cc dd")

# ---- Q1a: same eigenvalue
A = sp.diag(3, 3, 5)
v = V([1, 0, 0]); w = V([0, 1, 0])
lhs = A * (2 * v + 3 * w)
exp(1, A_, 2, lhs[1])
chk("Q1a A(cv+dw) = lambda (cv+dw) for lambda=3", lhs == 3 * (2 * v + 3 * w))
chk("Q1a order: c(Av)+d(Aw) = c lam v + d lam w = lam(cv+dw)", A * (cc * v + dd * w) == cc * (A * v) + dd * (A * w) and cc * 3 * v + dd * 3 * w == 3 * (cc * v + dd * w))
chk("Q1a bug line c lam v + d lam^2 w differs from d lam w", dd * 9 * w != dd * 3 * w)

# ---- Q1b: different eigenvalues
B = sp.diag(1, 2)
vb = V([1, 0]); wb = V([0, 1])
Bv = B * (vb + wb)
exp(1, B_, 1, Bv[1]); exp(1, B_, 2, sp.Matrix.hstack(vb + wb, Bv).det())
chk("Q1b v+w with B=diag(1,2) is not an eigenvector", sp.Matrix.hstack(vb + wb, Bv).rank() == 2)
B2 = 2 * sp.eye(2)
chk("Q1b distractor: with B=2I, v+w is an eigenvector but B(v+w) != v+w", B2 * (vb + wb) != vb + wb and B2 * (vb + wb) == 2 * (vb + wb))
chk("Q1b distractor B(v+w)=0 needs lambda=0 (B=diag(1,2) invertible, so it fails)", B * (vb + wb) != sp.zeros(2, 1))

# ---- Q1c: C^3, C^5
C3 = sp.Matrix([[5, -8], [-8, 13]]); C5 = sp.Matrix([[34, -55], [-55, 89]])
exp(1, C_, 0, C3.det())
chk("Q1c det C^5 = 1", C5.det() == 1)
Cm2 = C3 * C5.inv()
exp(1, C_, 2, Cm2[0, 0]); exp(1, C_, 3, Cm2[1, 1])
chk("Q1c C^-2 = [[5,3],[3,2]]", Cm2 == sp.Matrix([[5, 3], [3, 2]]))
chk("Q1c distractors C^5 C^-3 = C^2, C^5 C^3 = C^8 and (C^3)^-1 C^5 = C^2 are not C^-2",
    C5 * C3.inv() != Cm2 and C5 * C3 != Cm2 and C3.inv() * C5 != Cm2 and C5 * C3.inv() == (Cm2).inv())

# ---- Q1d: similar matrices
P = sp.Matrix([[1, 1], [0, 1]]); Bd = sp.diag(2, 3)
exp(1, D_, 1, (P.inv() * Bd * P).det())
X = sp.Matrix([[1, 2], [3, 4]]); Y = sp.Matrix([[0, 1], [1, 0]])
chk("Q1d distractors: det(X+Y)!=det X + det Y, det(2I2)=4!=2, det(X^T)=det X (not -det X)",
    (X + Y).det() != X.det() + Y.det() and (2 * sp.eye(2)).det() == 4 != 2 * sp.eye(2).det() / 2 and X.T.det() == X.det() != -X.det())
chk("Q1d multiplicativity det(P^-1 B P) = det P^-1 det B det P", (P.inv() * Bd * P).det() == P.inv().det() * Bd.det() * P.det())

# ---- Q2: system with k
S1 = sp.Matrix([[1, 2, k, 1], [1, 0, -3, -3], [2, k, -1, -2]])
S2 = S1.copy()
S2[1, :] = -(S2[1, :] - S2[0, :]); S2[2, :] = -(S2[2, :] - 2 * S2[0, :])
S2 = S2.applyfunc(sp.expand)
chk("Q2a S2 rows as printed", S2 == sp.Matrix([[1, 2, k, 1], [0, 2, k + 3, 4], [0, 4 - k, 2 * k + 1, 4]]))
S3 = S2.copy(); S3[2, :] = (2 * S3[2, :] - (4 - k) * S3[1, :]).applyfunc(sp.expand)
chk("Q2a S3 last row (0,0,k^2+3k-10 | 4k-8)", S3[2, :] == sp.Matrix([[0, 0, k**2 + 3 * k - 10, 4 * k - 8]]))
exp(2, A_, 0, S2[2, 1].subs(k, 1)); exp(2, A_, 1, S3[2, 2].subs(k, 1)); exp(2, A_, 2, S3[2, 3].subs(k, 1))
Ak = sp.Matrix([[2, k, -1], [1, 0, -3], [1, 2, k]]); Mk = Ak.row_join(sp.Matrix([-2, -3, 1]))
exp(2, B_, 0, S3[2, 3].subs(k, -5)); exp(2, B_, 1, Ak.subs(k, 2).rank())
cases = {}
for kv in (-5, 2, 0, 1, 3, -2):
    ra, rm = Ak.subs(k, kv).rank(), Mk.subs(k, kv).rank()
    cases[kv] = "none" if rm > ra else ("inf" if ra < 3 else "unique")
chk("Q2b mapping: -5 none, 2 infinite, others unique", cases == {-5: "none", 2: "inf", 0: "unique", 1: "unique", 3: "unique", -2: "unique"}, str(cases))
chk("Q2b distractors (swap, or both values none / both infinite) are false", cases[2] != "none" and cases[-5] != "inf")
x, y, z = sp.symbols("x y z")
s2 = sp.solve(list(Ak.subs(k, 2) * V([x, y, z]) - V([-2, -3, 1])), [x, y], dict=True)[0]
exp(2, C_, 0, s2[y].subs(z, 2)); exp(2, C_, 1, s2[x].subs(z, 2)); exp(2, C_, 2, 1)
chk("Q2c solution x=-3+3z, y=2-2.5z", sp.simplify(s2[x] - (-3 + 3 * z)) == 0 and sp.simplify(s2[y] - (2 - R(5, 2) * z)) == 0)
chk("Q2c exactly one free variable at k=2", 3 - Ak.subs(k, 2).rank() == 1)

# ---- Q2d: z^2 + (3i-4) z + 2i = 0
disc = sp.expand((3 * sp.I - 4)**2 - 8 * sp.I)
exp(2, D_, 0, sp.re(disc)); exp(2, D_, 1, sp.im(disc))
zz = sp.symbols("zz")
roots = sp.solve(zz**2 + (3 * sp.I - 4) * zz + 2 * sp.I, zz)
rv = sorted(roots, key=lambda r_: -sp.re(sp.N(r_)))
EXP[(2, D_, 2)] = sp.Float(sp.re(sp.N(rv[0], 12)))
chk("Q2d roots approx 4.23-3.295i and -0.23+0.295i", abs(sp.N(sp.re(rv[0])) - 4.23) < 0.01 and abs(sp.N(sp.im(rv[0])) + 3.295) < 0.01 and abs(sp.N(sp.re(rv[1])) + 0.23) < 0.01)
chk("Q2d sum of roots 4-3i (Vieta)", sp.simplify(sum(roots) - (4 - 3 * sp.I)) == 0)

# ---- Q3a: inverse
A3 = sp.Matrix([[1, 5, 1], [2, 11, 0], [0, 0, 1]]); Ai = A3.inv()
exp(3, A_, 0, A3.det()); exp(3, A_, 1, Ai[0, 0]); exp(3, A_, 2, Ai[0, 2]); exp(3, A_, 3, Ai[1, 0])
chk("Q3a A^-1 as printed", Ai == sp.Matrix([[11, -5, -11], [-2, 1, 2], [0, 0, 1]]))

# ---- Q3b: elementary matrices
E1 = sp.Matrix([[1, 0, 0], [-2, 1, 0], [0, 0, 1]]); E2 = sp.Matrix([[1, 0, 0], [0, 1, 2], [0, 0, 1]])
E3 = sp.Matrix([[1, 0, -1], [0, 1, 0], [0, 0, 1]]); E4 = sp.Matrix([[1, -5, 0], [0, 1, 0], [0, 0, 1]])
exp(3, B_, 0, 4); exp(3, B_, 1, E2[1, 2])
chk("Q3b A^-1 = E4 E3 E2 E1", E4 * E3 * E2 * E1 == Ai and E4 * E3 * E2 * E1 * A3 == sp.eye(3))
chk("Q3b distractors E1E2E3E4, E1E2E3E4*A, inverses in order are not the right answer",
    E1 * E2 * E3 * E4 != Ai and E1 * E2 * E3 * E4 * A3 != sp.eye(3) and E1.inv() * E2.inv() * E3.inv() * E4.inv() != Ai)

# ---- Q3c: diagonalization
Bm = sp.Matrix([[1, 0, 0], [-1, 6, 1], [-1, 5, 2]])
exp(3, C_, 0, Bm.trace()); exp(3, C_, 1, len((Bm - sp.eye(3)).nullspace())); exp(3, C_, 2, Bm.det())
chk("Q3c eigenvalues 1 (x2) and 7; diagonalizable; not symmetric", Bm.eigenvals() == {1: 2, 7: 1} and Bm.is_diagonalizable() and Bm != Bm.T)
chk("Q3c P, D with P^-1 B P = D", sp.Matrix([[5, 1, 0], [1, 0, 1], [0, 1, 1]]).inv() * Bm * sp.Matrix([[5, 1, 0], [1, 0, 1], [0, 1, 1]]) == sp.diag(1, 1, 7))
chk("Q3c distractor: not three distinct eigenvalues", len(Bm.eigenvals()) == 2)

# ---- Q4: subspaces of M2x2
M1 = sp.Matrix([[1, 2], [3, 4]]); M2 = sp.Matrix([[1, 1], [-1, 1]]); M3 = sp.Matrix([[1, 0], [-1, 3]])
Um = sp.Matrix.hstack(*[sp.Matrix(list(m)) for m in (M1, M2, M3)])
exp(4, A_, 0, M3[1, 1]); exp(4, A_, 1, Um.rank()); exp(4, A_, 2, Um.rank())
W_ = sp.Matrix([[1, 0], [0, -1]]); Wsy = sp.Matrix([[0, 1], [1, 0]])
exp(4, B_, 0, sp.Matrix.hstack(sp.Matrix(list(W_)), sp.Matrix(list(Wsy))).rank())
exp(4, B_, 1, -5)
chk("Q4b trace zero with a=5 gives d=-5", sp.solve(5 + sp.Symbol("d"), sp.Symbol("d")) == [-5])
chk("Q4b basis matrices symmetric with trace 0", W_ == W_.T and Wsy == Wsy.T and W_.trace() == 0 and Wsy.trace() == 0)
chk("Q4b distractors: I has trace 2; [[0,1],[-1,0]] not symmetric; single matrix does not span W",
    sp.eye(2).trace() != 0 and sp.Matrix([[0, 1], [-1, 0]]) != sp.Matrix([[0, 1], [-1, 0]]).T and sp.Matrix.hstack(sp.Matrix(list(W_)), sp.Matrix(list(Wsy))).rank() == 2)
vecs = [sp.Matrix(list(m)) for m in (W_, Wsy, M1, M2, M3)]
S5 = sp.Matrix.hstack(*vecs)
exp(4, C_, 0, S5.rank()); exp(4, C_, 1, 5 - S5.rank())
chk("Q4c U+W = M2x2 (rank 4)", S5.rank() == 4)
chk("Q4c distractor: W inside U would make dim(U+W)=3 although 3+2>4 (so 3+2>4 alone is not a reason)",
    sp.Matrix.hstack(*vecs[2:]).rank() == 3 and 3 + 2 > 4)
a, b, c, e, f = sp.symbols("a b c e f")
eqs = list(a * M1 + b * M2 + c * M3 - e * W_ - f * Wsy)
sol = sp.solve(eqs, [b, c, e, f], dict=True)[0]
exp(4, D_, 0, 3 + 2 - S5.rank())
mat2 = (2 * M1 + R(3, 1) * M2 - 4 * M3)
chk("Q4d a=2 gives b=3, c=-4", sp.simplify(sol[b].subs(a, 2)) == 3 and sp.simplify(sol[c].subs(a, 2)) == -4)
exp(4, D_, 1, mat2[0, 1]); exp(4, D_, 2, mat2[1, 1])
chk("Q4d result [[1,7],[7,-1]] is symmetric with trace 0", mat2 == sp.Matrix([[1, 7], [7, -1]]) and mat2 == mat2.T and mat2.trace() == 0)

# ---- Q5: linear map
Tm = sp.Matrix([[1, 1, 2, 2], [1, 2, 3, -2], [3, 4, 7, 2], [3, 5, 8, -2]])
exp(5, A_, 0, Tm.rank())
kn = Tm.nullspace()
exp(5, A_, 3, len(kn))
chk("Q5a kernel (-1,-1,1,0),(-6,4,0,1)", all(Tm * q == sp.zeros(4, 1) for q in (V([-1, -1, 1, 0]), V([-6, 4, 0, 1]))) and len(kn) == 2)
exp(5, A_, 2, (0 * V([-1, -1, 1, 0]) + 1 * V([-6, 4, 0, 1]))[1])
Im = sp.Matrix.hstack(Tm[:, 0], Tm[:, 1])
chk("Q5a columns 1,2 basis of column space", Im.rank() == 2 == Tm.rank())
chk("Q5a distractors: column 3 = column 1 + column 2; one column spans a line; echelon columns not in Im",
    Tm[:, 2] == Tm[:, 0] + Tm[:, 1] and Tm[:, 0].rank() == 1 and sp.Matrix.hstack(Im, V([1, 0, 0, 0])).rank() == 3 and sp.Matrix.hstack(Im, V([1, 1, 0, 0])).rank() == 3)
exp(5, B_, 0, Tm.rank())
chk("Q5b not injective and not onto", len(kn) == 2 and Tm.rank() < 4)
al, be, q_ = sp.symbols("al be q_")
sc = sp.solve([al + be - 11, al + 2 * be - 12], [al, be], dict=True)[0]
exp(5, C_, 0, sc[be]); exp(5, C_, 1, sc[al]); exp(5, C_, 2, 3 * sc[al] + 5 * sc[be])
chk("Q5c (11,12,34,35) in Im, (11,12,34,34) not", sp.Matrix.hstack(Im, V([11, 12, 34, 35])).rank() == 2 and sp.Matrix.hstack(Im, V([11, 12, 34, 34])).rank() == 3)
# T(b1)
def T(a_, b_, c_, d_):
    return V([a_ + b_ + 2 * c_ + 2 * d_, a_ + 2 * b_ + 3 * c_ - 2 * d_, 3 * a_ + 4 * b_ + 7 * c_ + 2 * d_, 3 * a_ + 5 * b_ + 8 * c_ - 2 * d_])
b1m = (0, 0, 2, 0); b2m = (2, 0, 0, 0); b3m = (0, 2, 0, 0); b4m = (0, 0, 0, 2)
Cmat = sp.Matrix.hstack(V([0, 0, -1, 0]), V([0, 0, 0, -1]), V([1, 0, 0, 0]), V([0, 1, 0, 0]))
cols = [Cmat.inv() * T(*bm) for bm in (b1m, b2m, b3m, b4m)]
Tcb = sp.Matrix.hstack(*cols)
exp(5, D_, 0, T(*b1m)[2]); exp(5, D_, 1, cols[0][0]); exp(5, D_, 2, Tcb[3, 3])
chk("Q5d [T]_C^B as printed", Tcb == sp.Matrix([[-14, -6, -8, -4], [-16, -6, -10, 4], [4, 2, 2, 4], [6, 2, 4, -4]]))

# ---- coverage
need = {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
n = 0
for key in sorted(need):
    n += 1
    num, part, i = key
    if key not in EXP:
        chk("Q%d%s step %d has an expected value" % (num, part, i), False)
        continue
    st = QS[(num, part)]["steps"][i]
    ok = abs(sp.Float(EXP[key]) - st["answer"]) <= st.get("tol", 0) + 1e-12
    chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, "abcd"["אבגד".index(part)], i, st["answer"], sp.N(EXP[key], 6)), ok)
chk("no orphan expected values", not (set(EXP) - need), str(sorted(set(EXP) - need)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
