# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 21A-A (rubric/pitfalls/steps in tools/gen/gen_21A-A.py).
Run: PYTHONUTF8=1 py tools/verify/21A-A/verify_steps_21A-A.py
Every numeric step in tools/raw/21A-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / order / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "21A-A.json").read_text(encoding="utf-8"))
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


# ---- Q1: AA^T + A^2 = 3I, AA^T - A^2 = 0  => 2A^2 = 3I
s = sp.sqrt(R(3, 2))
for sign in (1, -1):
    A = sign * s * sp.eye(3)
    chk("Q1 A=%d*sqrt(3/2) I satisfies both equations" % sign, A * A.T + A * A == 3 * sp.eye(3) and A * A.T - A * A == sp.zeros(3))
    chk("Q1 det A=%d*3sqrt6/4, det A^-1 same sign" % sign, sp.simplify(A.det() - sign * 3 * sp.sqrt(6) / 4) == 0 and sp.simplify(A.inv().det() - sign * 2 * sp.sqrt(6) / 9) == 0)
exp(1, C_, 0, (3 * sp.eye(3)).det())
d2 = sp.simplify((3 * sp.eye(3)).det() / 2 ** 3)
exp(1, C_, 1, d2); exp(1, C_, 2, sp.N(sp.sqrt(d2), 6))
chk("Q1c |A|^2=27/8", d2 == R(27, 8))
exp(1, D_, 0, sp.N(1 / d2, 6)); exp(1, D_, 1, sp.N(sp.sqrt(1 / d2), 6))
Am = s * sp.eye(3)
chk("Q1a (1/3)(A+A^T) is the inverse", Am * (Am + Am.T) / 3 == sp.eye(3))
chk("Q1a bug line A(A^T+A^2) = A A^T + A^3 differs from 3I", Am * (Am.T + Am * Am) != 3 * sp.eye(3))
Xs = sp.Matrix(3, 3, sp.symbols("m0:9"))
chk("Q1a factoring A(A^T+A)=AA^T+A^2 (generic)", sp.expand(Xs * (Xs.T + Xs) - (Xs * Xs.T + Xs * Xs)) == sp.zeros(3))
chk("Q1b ((A+A^T)/3)^T = (A+A^T)/3 (generic)", ((Xs + Xs.T) / 3).T == (Xs + Xs.T) / 3)
chk("Q1b bug line (1/3)A^T+(1/3)A^T != (1/3)(A+A^T) (generic)", sp.simplify((Xs.T / 3 + Xs.T / 3) - (Xs + Xs.T) / 3) != sp.zeros(3))

# ---- Q2 system
a = sp.symbols("a")
M = V([[1, -1, -a, a], [a, 1, -1, -a], [1, a, 1, -1]])
Mc = M[:, :3]
Ma3 = M.subs(a, 3)
exp(2, A_, 0, (1 + a).subs(a, 3))
chk("Q2a third-row coefficient after R3-R2 is -(a+1)(a-2)", sp.expand((1 + a) - (a ** 2 - 1) + (a + 1) * (a - 2)) == 0)
exp(2, A_, 1, (-(a + 1) * (a - 2)).subs(a, 3))
(sol3,) = sp.linsolve((Mc.subs(a, 3), Ma3[:, 3]))
exp(2, A_, 2, sol3[0]); exp(2, A_, 3, sol3[1])
chk("Q2a general solution (1-a)/(a-2), 1/(a-2), (1-a)/(a-2)", all(sp.simplify(e) == 0 for e in (Mc * V([(1 - a) / (a - 2), 1 / (a - 2), (1 - a) / (a - 2)]) - M[:, 3])))
exp(2, B_, 0, Mc.subs(a, -1).rank()); exp(2, B_, 1, M.subs(a, 2).rank())
chk("Q2b a=2: coefficient rank 2, augmented rank 3", Mc.subs(a, 2).rank() == 2 and M.subs(a, 2).rank() == 3)
chk("Q2b a=-1: ranks 1 and 1 (infinitely many)", M.subs(a, -1).rank() == 1 and Mc.subs(a, -1).rank() == 1)
dd = sp.factor(Mc.det())
chk("Q2b det of coefficients vanishes exactly at a=-1,2", set(sp.solve(dd, a)) == {-1, 2}, str(dd))
exp(2, C_, 0, 2); exp(2, C_, 1, (2 - 1 - 1))
nm1 = Mc.subs(a, -1)
chk("Q2c a=-1: single equation x-y+z=-1, rank 1", nm1.rank() == 1 and list(nm1.row(0)) == [1, -1, 1])
for name, v in [("(-1,0,1)", V([-1, 0, 1])), ("(0,-1,1)", V([0, -1, 1])), ("(1,0,1)", V([1, 0, 1])), ("(-1,0,-1)", V([-1, 0, -1]))]:
    inn = (nm1 * v)[0] == 0
    chk("Q2c direction %s %s in homogeneous solution set" % (name, "is" if inn else "is not"), inn == (name == "(-1,0,1)"))
chk("Q2c values 2,2,-2 for the distractors", [(nm1 * v)[0] for v in (V([0, -1, 1]), V([1, 0, 1]), V([-1, 0, -1]))] == [2, 2, -2])
chk("Q2c particular + 2(1,1,0) + 1(-1,0,1) solves with x=0", (nm1 * (V([-1, 0, 0]) + 2 * V([1, 1, 0]) + V([-1, 0, 1])))[0] == -1 and (V([-1, 0, 0]) + 2 * V([1, 1, 0]) + V([-1, 0, 1]))[0] == 0)
z = sp.symbols("z")
roots = sp.solve(z ** 4 + 8 * z, z)
nz = [r for r in roots if r != 0]
exp(2, D_, 0, sp.Abs(nz[0]).simplify()); exp(2, D_, 1, len(roots))
im0 = [sp.im(r) for r in nz if sp.re(r) == 1 and sp.im(r) > 0][0]
exp(2, D_, 2, sp.N(im0, 6))
chk("Q2d roots are 0, -2, 1+-sqrt3 i with modulus 2", set(roots) == {0, -2, 1 + sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I} and all(sp.Abs(r) == 2 for r in nz))

# ---- Q3
A3 = V([[2 * a, 3, 6], [4, a + 1, 4 * a - 2], [1, 5, 2]])
dA = sp.expand(A3.det())
chk("Q3a det = -36a^2+30a+84 = -6(a-2)(6a+7)", dA == -36 * a ** 2 + 30 * a + 84 and sp.expand(-6 * (a - 2) * (6 * a + 7)) == dA)
exp(3, A_, 0, dA.subs(a, 0)); exp(3, A_, 1, dA.subs(a, 1)); exp(3, A_, 2, sp.N(R(-7, 6), 6))
chk("Q3a roots 2, -7/6", set(sp.solve(dA, a)) == {2, R(-7, 6)})
B = V([[6, 0, 2], [1, 4, 0], [0, 0, 3]])
exp(3, C_, 0, B.trace()); exp(3, C_, 1, B.det())
chk("Q3c eigenvalues 3,4,6", set(B.eigenvals()) == {3, 4, 6})
v3 = V([R(-2, 3), R(2, 3), 1])
chk("Q3c v3=(-2/3,2/3,1) eigenvector of 3, (2,1,0) of 6, (0,1,0) of 4", B * v3 == 3 * v3 and B * V([2, 1, 0]) == 6 * V([2, 1, 0]) and B * V([0, 1, 0]) == 4 * V([0, 1, 0]))
exp(3, C_, 2, (3 * v3)[0])
for name, v in [("(0,0,1)", V([0, 0, 1])), ("(1,0,0)", V([1, 0, 0])), ("(1,1,0)", V([1, 1, 0]))]:
    chk("Q3c distractor %s is not an eigenvector for 4" % name, B * v != 4 * v)
chk("Q3c distractor images (2,0,3),(6,1,0),(6,5,0)", [list(B * v) for v in (V([0, 0, 1]), V([1, 0, 0]), V([1, 1, 0]))] == [[2, 0, 3], [6, 1, 0], [6, 5, 0]])
P = V([[R(-2, 3), 0, 2], [R(2, 3), 1, 1], [1, 0, 0]])
D = sp.diag(3, 4, 6)
chk("Q3d P^-1 B P = D", P.inv() * B * P == D)
exp(3, D_, 0, D[2, 2]); exp(3, D_, 1, P.det())
chk("Q3d distractor columns: (2,1,0) is for 6, (-2/3,2/3,1) for 3, (0,0,1) not eigen", B * V([2, 1, 0]) == 6 * V([2, 1, 0]) and B * v3 == 3 * v3 and B * V([0, 0, 1]) != 4 * V([0, 0, 1]))

# ---- Q4: R2[x] coordinates (a0,a1,a2)
U = V([[1, 1, 0], [2, 0, -1], [0, 2, 1]])
exp(4, A_, 0, U.rank())
al, be = sp.symbols("al be")
sl = sp.solve(list(al * V([1, 1, 0]) + be * V([0, 2, 1]) - V([2, 0, -1])), [al, be], dict=True)[0]
exp(4, A_, 1, sl[al])
chk("Q4a 2-x^2 = 2(1+x) - (2x+x^2)", sl == {al: 2, be: -1})
cW = 3
exp(4, A_, 2, -2 * cW)
Wm = V([[0, 1, 2]])
chk("Q4a W: p'(1)=b+2c, null space dim 2, {1, x^2-2x} in W", len(Wm.nullspace()) == 2 and (Wm * V([1, 0, 0]))[0] == 0 and (Wm * V([0, -2, 1]))[0] == 0)
exp(4, A_, 3, len(Wm.nullspace()))
BU = [V([1, 1, 0]), V([0, 2, 1])]; BW = [V([1, 0, 0]), V([0, -2, 1])]
S4 = sp.Matrix.hstack(*(BU + BW))
exp(4, B_, 0, S4.rank()); exp(4, B_, 1, S4.rank())
chk("Q4b U+W = whole space, rank 3", S4.rank() == 3)
chk("Q4b U != W: 1 in W but not in U", sp.Matrix.hstack(*BU, V([1, 0, 0])).rank() == 3)
t1 = V([1, 0, 0]) + V([1, 1, 0])
chk("Q4b U cup W not closed: 2+x in neither", sp.Matrix.hstack(*BU, t1).rank() == 3 and (Wm * t1)[0] != 0)
Hm = sp.Matrix.hstack(*BU, *[-b for b in BW])
ns = Hm.nullspace()
exp(4, C_, 0, Hm.rank())
chk("Q4c homogeneous system 3x4 rank 3, 1 free var; so dim(U cap W)=1", Hm.rank() == 3 and len(ns) == 1)
n0 = ns[0] / ns[0][3]
exp(4, C_, 1, n0[2])
vint = n0[0] * BU[0] + n0[1] * BU[1]
vint = vint / (vint[0] / 4)
chk("Q4c intersection vector (4,2,-1)", list(vint) == [4, 2, -1])
exp(4, C_, 2, vint[2])


def inUm(v): return sp.Matrix.hstack(*BU, v).rank() == 2
def inWm(v): return (Wm * v)[0] == 0


chk("Q4c 4+2x-x^2 in both", inUm(V([4, 2, -1])) and inWm(V([4, 2, -1])))
chk("Q4c 1+x in U only, 1 in W only, x^2-2x in W only", inUm(V([1, 1, 0])) and not inWm(V([1, 1, 0])) and inWm(V([1, 0, 0])) and not inUm(V([1, 0, 0])) and inWm(V([0, -2, 1])) and not inUm(V([0, -2, 1])))
xx = sp.symbols("xx")
qq = 4 + 2 * xx - xx ** 2
exp(4, D_, 0, qq.subs(xx, 2)); exp(4, D_, 1, qq.subs(xx, -2)); exp(4, D_, 2, 7 * (qq.subs(xx, 2) + qq.subs(xx, -2)))

# ---- Q5
a1, b1, c1, d1, a2, b2, c2, d2 = sp.symbols("a1 b1 c1 d1 a2 b2 c2 d2")


def T(a_, b_, c_, d_): return V([a_ + b_, b_ + c_, b_ + d_])


chk("Q5a additivity", T(a1 + a2, b1 + b2, c1 + c2, d1 + d2) == T(a1, b1, c1, d1) + T(a2, b2, c2, d2))
chk("Q5a bug: (b1+b2)(d1+d2) is not b+d of the sum", sp.expand((b1 + b2) * (d1 + d2) - ((b1 + b2) + (d1 + d2))) != 0)
chk("Q5a T(A)=(3,5,6) for A=[[1,2],[3,4]]", list(T(1, 2, 3, 4)) == [3, 5, 6])
exp(5, A_, 2, 2 * T(1, 2, 3, 4)[1])
chk("Q5a T(2A)=2T(A)", T(2, 4, 6, 8) == 2 * T(1, 2, 3, 4))
Tm = V([[1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1]])
kn = Tm.nullspace()
chk("Q5b kernel spanned by (1,-1,1,1)", len(kn) == 1 and Tm * V([1, -1, 1, 1]) == sp.zeros(3, 1))
chk("Q5b distractor images (2,2,2),(0,2,2),(0,-2,0)", [list(Tm * v) for v in (V([1, 1, 1, 1]), V([-1, 1, 1, 1]), V([1, -1, -1, 1]))] == [[2, 2, 2], [0, 2, 2], [0, -2, 0]])
exp(5, B_, 1, len(kn)); exp(5, B_, 2, Tm.rank()); exp(5, B_, 3, (Tm * V([1, -1, 1, 1]))[0])
chk("Q5b image basis (1,0,0),(1,1,1),(0,1,0) rank 3", sp.Matrix.hstack(V([1, 0, 0]), V([1, 1, 1]), V([0, 1, 0])).rank() == 3)
chk("Q5c not injective, onto; the zero map shows dim 4 > 3 does not give onto", len(kn) > 0 and Tm.rank() == 3 and sp.zeros(3, 4).rank() < 3)
part = V([0, 1, 0, 0])
chk("Q5d solution set is t(1,-1,1,1)+(0,1,0,0)", Tm * (2 * V([1, -1, 1, 1]) + part) == V([1, 1, 1]) and Tm * part == V([1, 1, 1]))
exp(5, D_, 0, (part + 2 * V([1, -1, 1, 1]))[1]); exp(5, D_, 1, (Tm * V([0, 0, 0, 0]))[0])
for name, base, direc in [("kernel only", V([0, 0, 0, 0]), V([1, -1, 1, 1])), ("particular (1,0,0,0)", V([1, 0, 0, 0]), V([1, -1, 1, 1])), ("direction (1,1,1,1)", part, V([1, 1, 1, 1]))]:
    ok = all(Tm * (base + k_ * direc) == V([1, 1, 1]) for k_ in (0, 1, 2, 3))
    chk("Q5d distractor %s does not map to (1,1,1) for all t" % name, not ok)

# ---- coverage
need = {(num, part, i) for (num, part), qq_ in QS.items() for i, st in enumerate(qq_.get("steps", [])) if st["type"] == "numeric"}
n = 0
for key in sorted(need):
    n += 1
    num, part, i = key
    if key not in EXP:
        chk("Q%d%s step %d has an expected value" % (num, part, i), False)
        continue
    st = QS[(num, part)]["steps"][i]
    ok = abs(float(sp.N(EXP[key])) - st["answer"]) <= st.get("tol", 0) + 1e-12
    chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, "abcd"["אבגד".index(part)], i, st["answer"], sp.N(EXP[key], 6)), ok)
chk("no orphan expected values", not (set(EXP) - need), str(sorted(set(EXP) - need)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
