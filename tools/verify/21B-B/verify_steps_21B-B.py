# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 21B-B (rubric/pitfalls/steps in tools/gen/gen_21B-B.py).
Run: PYTHONUTF8=1 py tools/verify/21B-B/verify_steps_21B-B.py
Every numeric step in tools/raw/21B-B.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug / order line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "21B-B.json").read_text(encoding="utf-8"))
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


t = sp.symbols("t")
# ---- Q1a: A = E F G R
A = M([[0, 1, 7, 8], [1, 3, 3, 8], [-2, -5, 1, -8]])
E1 = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, 0], [2, 0, 1]]); E3 = M([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
Rm = E3 * E2 * E1 * A
chk("Q1a R is the echelon form", Rm == M([[1, 3, 3, 8], [0, 1, 7, 8], [0, 0, 0, 0]]))
exp(1, A_, 0, Rm.rank())
Ee, Ff, Gg = E1.inv(), E2.inv(), E3.inv()
chk("Q1a A = E F G R", Ee * Ff * Gg * Rm == A)
chk("Q1a distractor A = E3 E2 E1 R is false", E3 * E2 * E1 * Rm != A)
chk("Q1a distractor A = E1 E2 E3 R is false", E1 * E2 * E3 * Rm != A)
chk("Q1a ops act on A: E3E2E1A=R", E3 * E2 * E1 * A == Rm)
exp(1, A_, 2, Ff[2, 0]); exp(1, A_, 3, Gg[2, 1])

# ---- Q1b: B^3-5B-4I=0
chk("Q1b a=-1 root", (-1) ** 3 - 5 * (-1) - 4 == 0)
chk("Q1b x(x^2-5)/4 = 1 mod x^3-5x-4", sp.rem(sp.expand(t * (t ** 2 - 5) / 4 - 1), t ** 3 - 5 * t - 4, t) == 0)
for nm, f in (("B^2-5", lambda a: a ** 2 - 5), ("-(B^2-5)/4", lambda a: -R(a ** 2 - 5, 4)), ("(B^2+5)/4", lambda a: R(a ** 2 + 5, 4))):
    chk("Q1b distractor %s != B^-1 at B=-1" % nm, f(-1) != -1)
chk("Q1b bug: at B=-1, B^3-5B = 4 not -4", (-1) ** 3 - 5 * (-1) == 4)
exp(1, B_, 3, R(1, 4) * ((-1) ** 2 - 5))

# ---- Q1c: CXD = C + D
Cm = M([[2, 1], [1, 1]]); Dm = M([[1, 3], [0, 2]])
X = Dm.inv() + Cm.inv()
chk("Q1c X = D^-1 + C^-1", Cm * X * Dm == Cm + Dm)
chk("Q1c XD = I + C^-1 D", X * Dm == sp.eye(2) + Cm.inv() * Dm)
chk("Q1c distractor: C X D C^-1 != X D (right multiplication does not cancel C)", Cm * X * Dm * Cm.inv() != X * Dm)
chk("Q1c matrices do not commute", Cm * Dm != Dm * Cm)
xs = sp.symbols("xs")
exp(1, C_, 2, sp.solve(sp.Eq(3 * xs * 6, 3 + 6), xs)[0])

# ---- Q2
k = sp.symbols("k")
Mk = M([[2, 2, 3 - k ** 2, 3 - k], [1, k + 1, k, 1 - k], [3, 3, -k ** 2, 3 - k]])
O = M([list(Mk.row(1)), list(Mk.row(2)), list(Mk.row(0))])
S1 = O.copy()
S1[1, :] = S1[1, :] - 3 * S1[0, :]
S1[2, :] = S1[2, :] - 2 * S1[0, :]
S1 = S1.applyfunc(sp.expand)
chk("Q2a after R2-3R1,R3-2R1 rows", S1[1, :] == M([[0, -3 * k, -k ** 2 - 3 * k, 2 * k]]) and S1[2, :] == M([[0, -2 * k, 3 - 2 * k - k ** 2, k + 1]]))
exp(2, A_, 1, S1[1, 1].subs(k, 1)); exp(2, A_, 2, S1[2, 2].subs(k, 3))
S2 = S1.copy(); S2[2, :] = 3 * S2[2, :] - 2 * S2[1, :]; S2 = S2.applyfunc(sp.expand)
chk("Q2a final row 3 = (0,0,9-k^2 | 3-k)", S2[2, :] == M([[0, 0, 9 - k ** 2, 3 - k]]))
exp(2, A_, 3, S2[2, 3].subs(k, 1))
A0 = Mk[:, :3]; b0 = Mk[:, 3]
xyz = sp.symbols("x y z")
sol_orig = sp.solve(list(A0.subs(k, 2) * M(xyz) - b0.subs(k, 2)), xyz, dict=True)
sol_sw = sp.solve(list(O[:, :3].subs(k, 2) * M(xyz) - O[:, 3].subs(k, 2)), xyz, dict=True)
chk("Q2a distractor: swapping rows keeps the solution set", sol_orig == sol_sw and len(sol_orig) == 1)


def rks(kv):
    return A0.subs(k, kv).rank(), Mk.subs(k, kv).rank()


exp(2, B_, 0, rks(3)[0]); exp(2, B_, 1, rks(-3)[1]); exp(2, B_, 2, rks(0)[0])
chk("Q2b k=3, k=0 infinite (ranks equal, <3)", rks(3)[0] == rks(3)[1] == 2 and rks(0)[0] == rks(0)[1] == 2)
chk("Q2b k=-3 no solution (rank A=2, aug=3)", rks(-3) == (2, 3))
chk("Q2b unique for k=1,2,5,-1 (rank 3)", all(rks(v) == (3, 3) for v in (1, 2, 5, -1)))
xx, yy, zz = xyz
s0 = sp.solve(list(A0.subs(k, 0) * M([xx, yy, zz]) - b0.subs(k, 0)), [xx, zz], dict=True)[0]
chk("Q2c k=0: z=1/3, x=1-y", s0[zz] == R(1, 3) and s0[xx] == 1 - yy)
exp(2, C_, 0, 3 - A0.subs(k, 0).rank()); exp(2, C_, 1, s0[zz]); exp(2, C_, 2, s0[xx].subs(yy, 3))
disc = sp.expand(sp.I ** 2 - 4 * R(1, 4) * sp.I)
chk("Q2d disc = -1-i", disc == -1 - sp.I)
exp(2, D_, 0, (sp.arg(disc) * 180 / sp.pi) % 360)
exp(2, D_, 1, sp.Float(sp.N(sp.Abs(sp.sqrt(disc)))))
w = sp.symbols("w")
rts = sp.solve(w ** 2 + sp.I * w + R(1, 4) * sp.I, w)
chk("Q2d roots are (-i +- sqrt(-1-i))/2", all(sp.simplify(r ** 2 + sp.I * r + R(1, 4) * sp.I) == 0 for r in rts))
exp(2, D_, 2, sp.Float(min(sp.N(sp.re(r)) for r in rts)))

# ---- Q3
Ak = M([[1, 1, 1], [k, k ** 2, 1], [k ** 2, 2 * k ** 2 - 1, 1]])
chk("Q3a det = -(k+1)(k-1)^3", sp.expand(Ak.det() + (k + 1) * (k - 1) ** 3) == 0)
exp(3, A_, 0, Ak.det().subs(k, 2)); exp(3, A_, 1, Ak.det().subs(k, 0))
chk("Q3a singular exactly at k=1,-1 (not 0)", set(sp.solve(Ak.det(), k)) == {1, -1} and Ak.det().subs(k, 0) != 0)
A1k = Ak.subs(k, 1)
exp(3, B_, 0, A1k.rank())
cs = A1k.columnspace()
chk("Q3b col space spanned by (1,1,1)", len(cs) == 1 and cs[0] == M([1, 1, 1]))
chk("Q3b distractors (1,0,0), (1,2,3) not in Col A; (1,1,1),(2,2,2) dependent",
    sp.Matrix.hstack(A1k, M([1, 0, 0])).rank() == 2 and sp.Matrix.hstack(A1k, M([1, 2, 3])).rank() == 2 and sp.Matrix.hstack(M([1, 1, 1]), M([2, 2, 2])).rank() == 1)
chk("Q3c rank 3 at k=2; rank < 3 at k=1", Ak.subs(k, 2).rank() == 3 and Ak.subs(k, 1).rank() < 3)
exp(3, C_, 1, Ak.subs(k, 2).rank())
B3 = M([[-2, 1, -1], [1, 2, 3], [1, -1, 0]])
exp(3, D_, 0, B3.trace()); exp(3, D_, 1, B3.det())
chk("Q3d eigenvalues 0,1,-1", B3.eigenvals() == {0: 1, 1: 1, -1: 1})
chk("Q3d B not symmetric", B3 != B3.T)
chk("Q3d det=0 / eigenvalue 0 do not imply diagonalizable: [[0,1],[0,0]]", not M([[0, 1], [0, 0]]).is_diagonalizable())
v3 = M([-1, -2, 1]); v2 = M([-3, -1, 2]); v1 = M([-1, -1, 1])
chk("Q3d eigenvectors v1(0), v2(-1), v3(1)", B3 * v1 == 0 * v1 and B3 * v2 == -v2 and B3 * v3 == v3)
P3 = M([[-1, -1, -3], [-1, -2, -1], [1, 1, 2]]); D3 = sp.diag(0, 1, -1)
chk("Q3d P^-1 B P = D", P3.inv() * B3 * P3 == D3)
exp(3, D_, 3, (B3 * v3)[0])

# ---- Q4
M1 = M([1, 1, 0, 0]); M2 = M([0, 0, 2, 3]); M3 = M([5, 5, 6, 9])
chk("Q4a M3 = 5 M1 + 3 M2", M3 == 5 * M1 + 3 * M2)
exp(4, A_, 0, 3)
exp(4, A_, 1, sp.Matrix.hstack(M1, M2, M3).rank())
c2 = M([[1, 1, -1, -1]])
exp(4, A_, 2, 4 - c2.rank())
for nm, mat, inw in (("(2 1;1 2)", [2, 1, 1, 2], True), ("(1 2;3 4)", [1, 2, 3, 4], False), ("(1 1;1 2)", [1, 1, 1, 2], False), ("(0 0;1 0)", [0, 0, 1, 0], False)):
    chk("Q4a membership %s in W2 is %s" % (nm, inw), ((c2 * M(mat))[0] == 0) == inw)
Wb1 = [M1, M2]; Wb2 = [M([-1, 1, 0, 0]), M([1, 0, 1, 0]), M([1, 0, 0, 1])]
chk("Q4a W2 basis in W2", all((c2 * v)[0] == 0 for v in Wb2))
allm = sp.Matrix.hstack(*(Wb1 + Wb2))
exp(4, B_, 0, allm.rank())
chk("Q4b distractors: dim sum 5 > 4; M1 not in W2; intersection nontrivial", allm.rank() == 4 and (c2 * M1)[0] != 0 and 2 + 3 - allm.rank() == 1)
ns = sp.Matrix.hstack(*Wb1).row_join(-sp.Matrix.hstack(*Wb2)).nullspace()
chk("Q4c intersection dim 1", len(ns) == 1)
iv = sp.Matrix.hstack(*Wb1) * M(list(ns[0][:2]))
iv = iv / iv[0] * 5
chk("Q4c intersection basis (5,5,4,6) in W2", iv == M([5, 5, 4, 6]) and (c2 * iv)[0] == 0)
chk("Q4c iv = 5 M1 + 2 M2", iv == 5 * M1 + 2 * M2)
exp(4, C_, 0, 2 + 3 - allm.rank()); exp(4, C_, 1, iv[2] + iv[3]); exp(4, C_, 2, (iv - 5 * M1)[2] / 2)


def f4(a, b, c, d):
    return (a + b) * (c + d)


kk = sp.Symbol("kk")
chk("Q4d U contains 0 and is closed under scalar mult (k^2 factor)",
    sp.simplify(f4(*[kk * v for v in (1, -1, 1, 1)]) - kk ** 2 * f4(1, -1, 1, 1)) == 0 and f4(0, 0, 0, 0) == 0)
exp(4, D_, 1, f4(2, 0, 2, 0)); exp(4, D_, 2, f4(1, -1, 1, 1))
chk("Q4d counterexample: both in U, sum not in U", f4(1, -1, 1, 1) == 0 and f4(1, 1, 1, -1) == 0 and f4(2, 0, 2, 0) != 0)

# ---- Q5 printed map T(a b; c d) = (a+b, d+c)
a1, b1, c1, d1, a2, b2, c2s, d2 = sp.symbols("a1 b1 c1 d1 a2 b2 c2 d2")


def T(a, b, c, d):
    return M([a + b, d + c])


chk("Q5a additivity", sp.simplify(T(a1 + a2, b1 + b2, c1 + c2s, d1 + d2) - T(a1, b1, c1, d1) - T(a2, b2, c2s, d2)) == sp.zeros(2, 1))
al = sp.symbols("al")
chk("Q5a homogeneity", sp.simplify(T(al * a1, al * b1, al * c1, al * d1) - al * T(a1, b1, c1, d1)) == sp.zeros(2, 1))
chk("Q5a T(0)=0 is insufficient: S(M)=(a^2,0) is nonlinear", (2 ** 2) != 2 * (1 ** 2))
chk("Q5a bug: (d1+d2)(c1+c2) != (d1+d2)+(c1+c2)", sp.expand((d1 + d2) * (c1 + c2s) - ((d1 + d2) + (c1 + c2s))) != 0)
Tm = M([[1, 1, 0, 0], [0, 0, 1, 1]])
kern = Tm.nullspace()
exp(5, B_, 1, len(kern)); exp(5, B_, 2, Tm.rank())
for nm, v, inK in (("(1 -1;0 0)", [1, -1, 0, 0], True), ("(1 1;0 0)", [1, 1, 0, 0], False), ("(1 0;0 -1)", [1, 0, 0, -1], False), ("(0 0;1 1)", [0, 0, 1, 1], False)):
    chk("Q5b %s in ker T is %s" % (nm, inK), (Tm * M(v) == sp.zeros(2, 1)) == inK)
exp(5, C_, 1, len(kern))
chk("Q5c T is onto (rank 2) but not injective", Tm.rank() == 2 and len(kern) == 2)
Bm = [M([[1, 0], [0, 0]]), M([[1, 1], [0, 0]]), M([[1, 1], [1, 0]]), M([[1, 1], [1, 1]])]
B2 = M([[1, 1], [0, -1]])
cols = [B2.inv() * T(m[0, 0], m[0, 1], m[1, 0], m[1, 1]) for m in Bm]
chk("Q5d matrix", sp.Matrix.hstack(*cols) == M([[1, 2, 3, 4], [0, 0, -1, -2]]))
exp(5, D_, 1, cols[2][0]); exp(5, D_, 2, cols[2][1]); exp(5, D_, 3, cols[3][1])
stdcols = sp.Matrix.hstack(*[T(m[0, 0], m[0, 1], m[1, 0], m[1, 1]) for m in Bm])
chk("Q5d distractor: T(B1) in the standard basis is (1 2 2 2; 0 0 1 2), not the answer", stdcols == M([[1, 2, 2, 2], [0, 0, 1, 2]]) and stdcols != sp.Matrix.hstack(*cols))
chk("Q5d shape 2x4", sp.Matrix.hstack(*cols).shape == (2, 4))

# ---- coverage
n = 0
for (num, part), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] != "numeric":
            continue
        n += 1
        key = (num, part, i)
        if key not in EXP:
            chk("Q%d%s step %d has an expected value" % (num, part, i), False)
            continue
        ok = abs(sp.N(EXP[key]) - st["answer"]) <= st.get("tol", 0) + 1e-12
        chk("Q%d%s step %d numeric answer %s == sympy %s (tol %s)" % (num, part, i, st["answer"], sp.N(EXP[key], 6), st.get("tol", 0)), ok)
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
for (num, part), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] == "choice":
            ids = [o["id"] for o in st["options"]]
            vals = [o["value"] for o in st["options"]]
            chk("Q%d%s step %d choice has distinct options and valid key" % (num, part, i), st["correctId"] in ids and len(set(vals)) == len(vals))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
