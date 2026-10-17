# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 24A-A (rubric/pitfalls/steps in tools/gen/gen_24A-A.py).
Run: PYTHONUTF8=1 py tools/verify/24A-A/verify_steps_24A-A.py
Every numeric step in tools/raw/24A-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / order / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "24A-A.json").read_text(encoding="utf-8"))
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
I2 = sp.eye(2)

# ---- Q1 (matrix with A^2 + A + I = 0): example A used in the numeric steps
A = sp.Matrix([[0, -1], [1, -1]])
chk("Q1 example satisfies A^2+A+I=0", A**2 + A + I2 == sp.zeros(2, 2))
chk("Q1a A^-1 = -A-I = A^2", A.inv() == -A - I2 and A.inv() == A**2)
exp(1, A_, 1, A.inv()[0, 0])
chk("Q1a order lines: A(A+I) = -I and A(-A-I) = I; the bug line A(A+I)=I is false", A * (A + I2) == -I2 and A * (-A - I2) == I2 and A * (A + I2) != I2)
chk("Q1b A^2-A+I = -2A (the three distractors differ)", A**2 - A + I2 == -2 * A and (A**2 - A + I2) != -2 * A - 2 * I2 and (A**2 - A + I2) != sp.zeros(2, 2) and (A**2 - A + I2) != -2 * I2)
exp(1, B_, 1, (A**2 - A + I2).det())
chk("Q1b inverse -1/2 A^-1", (A**2 - A + I2).inv() == -R(1, 2) * A.inv())
E11 = sp.Matrix([[1, 0], [0, 0]]); E22 = sp.Matrix([[0, 0], [0, 1]])
exp(1, C_, 1, E11.trace() * E22.trace()); exp(1, C_, 2, (E11 * E22).trace())
chk("Q1c counterexample is symmetric and diagonal", E11 == E11.T and E22 == E22.T and E11.is_diagonal() and E22.is_diagonal())

# ---- Q2: system with parameter k
M = sp.Matrix([[1, 0, -3, -3], [2, k, -1, -2], [1, 2, k, 1]])
Ak = M[:, :3]
det = sp.factor(Ak.det())
chk("Q2a det = (k-2)(k+5)", sp.expand(det - (k - 2) * (k + 5)) == 0, str(det))
exp(2, A_, 0, det.subs(k, 1))
x, y, z = sp.symbols("x y z")
sol = sp.solve(list(Ak * V([x, y, z]) - M[:, 3]), [x, y, z], dict=True)[0]
chk("Q2a official unique solution formula", sp.simplify(sol[x] - (-3 * (k + 1) / (k + 5))) == 0 and sp.simplify(sol[y] - 4 / (k + 5)) == 0 and sp.simplify(sol[z] - 4 / (k + 5)) == 0)
exp(2, A_, 1, sol[x].subs(k, 1)); exp(2, A_, 2, 3 * sol[y].subs(k, 1))
EXP[(2, B_, 0)] = sp.nsimplify((4 * (k - 2)).subs(k, -5))
exp(2, B_, 1, Ak.subs(k, -5).rank()); exp(2, B_, 2, M.subs(k, -5).rank())
chk("Q2b only k=-5 has no solution", M.subs(k, -5).rank() > Ak.subs(k, -5).rank() and M.subs(k, 2).rank() == Ak.subs(k, 2).rank() == 2 and M.subs(k, 0).rank() == Ak.subs(k, 0).rank() == 3)
M2 = M.subs(k, 2)
s2 = sp.solve(list(Ak.subs(k, 2) * V([x, y, z]) - M2[:, 3]), [x, y], dict=True)[0]
exp(2, C_, 0, s2[x].subs(z, 0)); exp(2, C_, 1, s2[y].subs(z, 0))
exp(2, C_, 2, sp.diff(s2[x], z)); exp(2, C_, 3, sp.diff(s2[y], z))
p = V([-3, 2, 0]); d = V([6, -5, 2])
A2 = Ak.subs(k, 2)
chk("Q2c/d p particular, d homogeneous", A2 * p == M2[:, 3] and A2 * d == sp.zeros(3, 1))
exp(2, D_, 0, (A2 * d)[1]); exp(2, D_, 1, (A2 * p)[2])
chk("Q2d distractors: p is not a homogeneous solution; t d is not a solution of the original", A2 * p != sp.zeros(3, 1) and A2 * d != M2[:, 3])

# ---- Q3a: inverse
A3 = sp.Matrix([[1, -1, 1], [0, 1, 1], [-1, 1, 1]])
Ai = A3.inv()
exp(3, A_, 0, A3.det()); exp(3, A_, 1, Ai[0, 1]); exp(3, A_, 2, 2 * Ai[1, 0]); exp(3, A_, 3, 2 * Ai[2, 2])
chk("Q3a A^-1 as printed", Ai == sp.Matrix([[0, 1, -1], [R(-1, 2), 1, R(-1, 2)], [R(1, 2), 0, R(1, 2)]]))

# ---- Q3b: elementary matrices
E1 = sp.Matrix([[1, 0, 0], [0, 1, 0], [1, 0, 1]]); E2 = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]]); E3 = sp.diag(1, 1, R(1, 2))
E4 = sp.Matrix([[1, 0, 0], [0, 1, -1], [0, 0, 1]]); E5 = sp.Matrix([[1, 0, -2], [0, 1, 0], [0, 0, 1]])
exp(3, B_, 0, 5); exp(3, B_, 1, E1[2, 0])
chk("Q3b E5 E4 E3 E2 E1 A = I and A^-1 = E5E4E3E2E1", E5 * E4 * E3 * E2 * E1 * A3 == sp.eye(3) and E5 * E4 * E3 * E2 * E1 == Ai)
chk("Q3b distractor E1..E5 (first op leftmost) is not A^-1", E1 * E2 * E3 * E4 * E5 != Ai)
chk("Q3b distractor E1..E5 * A is not the identity", E1 * E2 * E3 * E4 * E5 * A3 != sp.eye(3))
chk("Q3b distractor inverses in order is not A^-1", E1.inv() * E2.inv() * E3.inv() * E4.inv() * E5.inv() != Ai)

# ---- Q3c: diagonalization
B = sp.Matrix([[1, 1, 0], [0, -2, 0], [-1, 0, 3]])
exp(3, C_, 0, B.trace()); exp(3, C_, 1, B.det())
chk("Q3c three distinct eigenvalues 1,-2,3", set(B.eigenvals()) == {1, -2, 3})
chk("Q3c distractors: B not symmetric, not diagonal; invertible does not imply diagonalizable", B != B.T and not B.is_diagonal() and sp.Matrix([[1, 1], [0, 1]]).det() != 0 and not sp.Matrix([[1, 1], [0, 1]]).is_diagonalizable())
exp(3, C_, 3, (B * V([2, 0, 1]))[0])
chk("Q3c P, D with PD=BP", sp.Matrix([[2, 5, 0], [0, -15, 0], [1, 1, 1]]) * sp.diag(1, -2, 3) == B * sp.Matrix([[2, 5, 0], [0, -15, 0], [1, 1, 1]]))

# ---- Q4: subspaces of R^3
b1 = V([1, 0, 1]); b2 = V([0, 1, 0]); c1 = V([1, 1, 0]); c2 = V([0, 0, 1])
exp(4, A_, 0, len(sp.Matrix([[1, 0, -1]]).nullspace())); exp(4, A_, 1, len(sp.Matrix([[1, -1, 0]]).nullspace()))
chk("Q4a basis (1,0,1),(0,1,0) lies in W1 (z=x) and spans it", all(v[2] == v[0] for v in (b1, b2)) and sp.Matrix.hstack(b1, b2).rank() == 2)
chk("Q4a distractors: single vector spans only a line; (1,1,0) not in W1; (1,0,1),(2,0,2) dependent",
    sp.Matrix.hstack(b1).rank() < 2 and c1[2] != c1[0] and sp.Matrix.hstack(b1, 2 * b1).rank() == 1)
S4 = sp.Matrix.hstack(b1, b2, c1, c2)
exp(4, B_, 0, S4.rank()); exp(4, B_, 1, 4 - S4.rank()); exp(4, B_, 2, S4.rank())
al = sp.symbols("a1 a2 b1 b2")
H = sp.Matrix([[1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
exp(4, C_, 1, H.rank()); exp(4, C_, 2, 4 - H.rank())
nsH = H.nullspace()[0]
w = nsH[0] * b1 + nsH[1] * b2
chk("Q4c intersection is spanned by (1,1,1)", sp.Matrix.hstack(w, V([1, 1, 1])).rank() == 1)
exp(4, C_, 3, (5 * V([1, 1, 1]))[0])
chk("Q4c distractors: (1,0,1) has z=x but is not in W2; (0,1,1) has z=y but not in W1; (1,1,1) violates x+y+z=0",
    b1[1] != b1[0] and V([0, 1, 1])[2] != V([0, 1, 1])[0] and sum([1, 1, 1]) != 0)
exp(4, D_, 0, 1)
chk("Q4d (1,1,1) in W1 (z=x) and W2 (y=x); sum of coordinates 3; a single vector is no basis of R^3",
    V([1, 1, 1])[2] == V([1, 1, 1])[0] and V([1, 1, 1])[1] == V([1, 1, 1])[0] and sum([1, 1, 1]) == 3 and sp.Matrix.hstack(V([1, 1, 1])).rank() < 3)

# ---- Q5: linear map R3[x] -> R^4
Tm = sp.Matrix([[1, 1, 2, 2], [2, 3, 2, 3], [3, 4, 4, 5], [4, 5, 6, 7]])
exp(5, A_, 0, Tm.rank())
kn = Tm.nullspace()
chk("Q5a kernel (-4,2,1,0),(-3,1,0,1)", all(Tm * v == sp.zeros(4, 1) for v in (V([-4, 2, 1, 0]), V([-3, 1, 0, 1]))) and len(kn) == 2)
exp(5, A_, 2, (1 * V([-4, 2, 1, 0]) + 0 * V([-3, 1, 0, 1]))[1]); exp(5, A_, 3, len(kn))
Im = sp.Matrix.hstack(Tm[:, 0], Tm[:, 1])
chk("Q5a columns 1,2 form a basis of the column space", Im.rank() == 2 == Tm.rank())
chk("Q5a distractor: three columns dependent; one column spans only a line", Tm[:, :3].rank() == 2 < 3 and Tm[:, 0].rank() == 1)
chk("Q5a distractor: echelon columns (1,0,0,0),(1,1,0,0) not in Im", sp.Matrix.hstack(Im, V([1, 0, 0, 0])).rank() == 3 and sp.Matrix.hstack(Im, V([1, 1, 0, 0])).rank() == 3)
exp(5, B_, 0, len(kn))
chk("Q5b not injective and not onto", len(kn) == 2 and Tm.rank() < 4)
kk, mm = sp.symbols("kk mm")
s1, s2_ = sp.symbols("s1 s2_")
sc = sp.solve(list(s1 * V([-4, 2, 1, 0]) + s2_ * V([-3, 1, 0, 1]) - V([-7, 3, kk, mm])), [s1, s2_, kk, mm], dict=True)[0]
exp(5, C_, 1, sc[kk]); exp(5, C_, 2, sc[mm])
chk("Q5c polynomial -7+3x+x^2+x^3 is in the kernel", Tm * V([-7, 3, 1, 1]) == sp.zeros(4, 1))
chk("Q5c distractor: kernel vector (-4,2,1,0) is not in Im", sp.Matrix.hstack(Im, V([-4, 2, 1, 0])).rank() == 3)
EB = sp.Matrix([[3, 7], [2, 5]]); EC = sp.Matrix([[5, 3], [3, 2]])
res = EC.inv() * EB
exp(5, D_, 1, EC.det()); exp(5, D_, 2, (EC.inv() * V([3, 2]))[0]); exp(5, D_, 3, res[1, 1])
chk("Q5d correct matrix", res == sp.Matrix([[0, -1], [1, 4]]))
for nm, mtx in (("EB*EC^-1", EB * EC.inv()), ("EC*EB", EC * EB), ("EB^-1*EC", EB.inv() * EC)):
    chk("Q5d distractor %s differs from the correct matrix" % nm, mtx != res)

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
    chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, "abcd"["אבגד".index(part)], i, st["answer"], EXP[key]), ok)
chk("no orphan expected values", not (set(EXP) - need), str(sorted(set(EXP) - need)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
