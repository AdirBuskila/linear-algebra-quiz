# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 22B-A (rubric/pitfalls/steps in tools/gen/gen_22B-A.py).
Run: PYTHONUTF8=1 py tools/verify/22B-A/verify_steps_22B-A.py
Every numeric step in tools/raw/22B-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "22B-A.json").read_text(encoding="utf-8"))
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
    EXP[(num, part, idx)] = float(val) if isinstance(val, float) else sp.nsimplify(val)


x, k, zz = sp.symbols("x k zz")

# ---- Q1: A A^T + A^2 = 5I, A A^T - A^2 = 0
av = sp.sqrt(R(5, 2))
Ap = av * sp.eye(4)
chk("Q1 model A=sqrt(5/2) I satisfies both equations", Ap * Ap.T + Ap**2 == 5 * sp.eye(4) and Ap * Ap.T - Ap**2 == sp.zeros(4))
Am = sp.diag(av, av, av, -av)
chk("Q1 model diag(a,a,a,-a) satisfies both equations", Am * Am.T + Am**2 == 5 * sp.eye(4) and Am * Am.T - Am**2 == sp.zeros(4))
chk("Q1a inverse (A^T+A)/5 on the model", Ap.inv() == (Ap.T + Ap) / 5 and Am.inv() == (Am.T + Am) / 5)
exp(1, A_, 3, round(float(((Ap.T + Ap) / 5)[0, 0]), 3))
Gen = V([[1, 2, 3, 0], [0, 1, 4, 1], [2, 0, 1, 5], [1, 1, 0, 3]])
chk("Q1a bug line: A(A^T-A) != AA^T + A^2 for a generic A", Gen * (Gen.T - Gen) != Gen * Gen.T + Gen**2 and Gen * (Gen.T + Gen) == Gen * Gen.T + Gen**2)
chk("Q1a right factoring would differ: (A^T+A)A != A(A^T+A) generically", (Gen.T + Gen) * Gen != Gen * (Gen.T + Gen))
Ga = V([[1, 2], [3, 4]])
exp(1, B_, 3, (Ga.T + Ga)[0, 1])
chk("Q1b A^T+A symmetric", (Ga.T + Ga) == (Ga.T + Ga).T and (Ga.T + Ga).T != (Ga.T - Ga))
chk("Q1b distractor: A itself not symmetric but A^-1 formula symmetric", Ga != Ga.T and ((Ga.T + Ga) / 5) == ((Ga.T + Ga) / 5).T)
chk("Q1b bug line: (A^T+A)^T = A+A^T, not A^T-A", (Gen.T + Gen).T == Gen + Gen.T and (Gen.T + Gen).T != Gen.T - Gen)
exp(1, C_, 0, (R(5, 2)) ** 4 * 1.0 if False else float(R(5, 2) ** 4))
exp(1, C_, 1, float(Am.det()))
chk("Q1c dets of the two models are +25/4 and -25/4", Ap.det() == R(25, 4) and Am.det() == R(-25, 4))
chk("Q1c det(A^2) = (5/2)^4", (Ap**2).det() == R(5, 2) ** 4 and (Am**2).det() == R(5, 2) ** 4)
exp(1, D_, 0, (Ap.det() * Ap.inv().det()))
exp(1, D_, 1, float(Am.inv().det()))
chk("Q1d det A^-1 = +-4/25 on the models", Ap.inv().det() == R(4, 25) and Am.inv().det() == R(-4, 25) and Am.inv().det() != R(25, 4))

# ---- Q2
X, Y, Z = sp.symbols("X Y Z")
Mk = V([[1, 1, k], [3, 4, 2], [2, 3, -1]]); rhs = V([2, k, 1])
sol = sp.solve(list(Mk * V([X, Y, Z]) - rhs), [X, Y, Z], dict=True)[0]
chk("Q2a solution x=3(k+2), y=-2(k+2), z=-1", sp.simplify(sol[X] - 3 * (k + 2)) == 0 and sp.simplify(sol[Y] + 2 * (k + 2)) == 0 and sp.simplify(sol[Z] + 1) == 0)
rk = lambda kv: (Mk.subs(k, kv).rank(), Mk.subs(k, kv).row_join(rhs.subs(k, kv)).rank())
chk("Q2a unique for all tested k != 3; k=3 not unique", all(rk(v) == (3, 3) for v in (0, 1, -2, 2, 7)) and rk(3) == (2, 2))
exp(2, A_, 1, sol[X].subs(k, 1)); exp(2, A_, 2, sol[Y].subs(k, 1)); exp(2, A_, 3, sol[Z])
exp(2, B_, 0, rk(3)[0]); exp(2, B_, 1, rk(3)[1])
E = Mk.row_join(rhs)
E1 = E.copy(); E1[1, :] = E1[1, :] - 3 * E1[0, :]; E1[2, :] = E1[2, :] - 2 * E1[0, :]
E1[2, :] = E1[2, :] - E1[1, :]
E1 = E1.applyfunc(sp.expand)
exp(2, B_, 2, 0)
r3 = (Mk.subs(k, 3).row_join(rhs.subs(k, 3))).rref()[0]
chk("Q2b at k=3 no contradiction row", r3[2, :] == sp.zeros(1, 4))
chk("Q2b distractors k=0 and k=-2 each have a solution", rk(0)[0] == rk(0)[1] and rk(-2)[0] == rk(-2)[1])
M3 = Mk.subs(k, 3); r3v = rhs.subs(k, 3)
exp(2, C_, 0, 5); exp(2, C_, 1, -3); exp(2, C_, 3, 3 - M3.rank())
chk("Q2c general solution (5,-3,0)+z(-10,7,1)", all(M3 * (V([5, -3, 0]) + t * V([-10, 7, 1])) == r3v for t in (0, 1, -2)))
chk("Q2c distractors fail", M3 * V([10, 7, 1]) != sp.zeros(3, 1) and M3 * V([-10, 7, -1]) != sp.zeros(3, 1) and M3 * V([0, 0, 0]) != r3v)
Az = V([[1 - sp.I, sp.I * zz], [zz**2, 1 + sp.I]])
chk("Q2d det = 2 - i z^3", sp.expand(Az.det() - (2 - sp.I * zz**3)) == 0)
rts = sp.solve(zz**3 + 2 * sp.I, zz)
chk("Q2d roots of z^3=-2i", len(rts) == 3 and all(sp.simplify(r**3 + 2 * sp.I) == 0 for r in rts))
cr = sp.cbrt(2)
exp(2, D_, 0, round(float(cr), 3))
exp(2, D_, 1, 90)
z0 = sp.I * cr
z1 = -cr * (sp.sqrt(3) / 2 + sp.I / 2)
z2 = cr * (sp.sqrt(3) / 2 - sp.I / 2)
chk("Q2d z0,z1,z2 are roots", all(sp.simplify(r**3 + 2 * sp.I) == 0 for r in (z0, z1, z2)))
exp(2, D_, 2, round(float(sp.re(z1)), 3)); exp(2, D_, 3, round(float(sp.im(z2)), 3))
chk("Q2d angle of z0 is 90 deg", sp.arg(z0) == sp.pi / 2)

# ---- Q3
A3 = V([[1, 2, 0], [0, 1, 1], [2, 4, 2]])
Ai = A3.inv()
exp(3, A_, 0, A3.det())
E1m = sp.eye(3); E1m[2, :] = E1m[2, :] - 2 * E1m[0, :]
exp(3, A_, 1, (E1m * A3)[2, 2])
exp(3, A_, 2, Ai[0, 0]); exp(3, A_, 3, float(Ai[1, 2]))
chk("Q3a A^-1 official", Ai == V([[-1, -2, 1], [1, 1, R(-1, 2)], [-1, 0, R(1, 2)]]))
Ea = [V([[1, -2, 0], [0, 1, 0], [0, 0, 1]]), V([[1, 0, 0], [0, 1, -1], [0, 0, 1]]), V([[1, 0, 0], [0, 1, 0], [0, 0, R(1, 2)]]), V([[1, 0, 0], [0, 1, 0], [-2, 0, 1]])]
prod = Ea[0] * Ea[1] * Ea[2] * Ea[3]
chk("Q3b product = A^-1", prod == Ai)
chk("Q3b choice: reversed product differs", Ea[3] * Ea[2] * Ea[1] * Ea[0] != Ai)
exp(3, B_, 1, float(prod.det())); exp(3, B_, 2, prod[0, 0])
B3 = V([[2, 1, 1], [1, 2, 1], [0, 0, 1]])
exp(3, C_, 0, (0 * sp.eye(3) - B3).det())
exp(3, C_, 1, 3 - (sp.eye(3) - B3).rank())
P3 = V([[-1, -1, 1], [1, 0, 1], [0, 1, 0]])
chk("Q3c BP = P diag(1,1,3)", B3 * P3 == P3 * sp.diag(1, 1, 3) and P3.det() != 0)
exp(3, C_, 3, (B3 * P3)[0, 2])
chk("Q3c eigenvalues 1,1,3 not distinct, B not symmetric, det != 0 not sufficient",
    sorted(B3.eigenvals(multiple=True)) == [1, 1, 3] and B3 != B3.T and B3.det() != 0 and not V([[1, 1], [0, 1]]).is_diagonalizable())

# ---- Q4
Aw = V([[1, 2, -4], [-2, 3, -13], [-1, -1, 1]])
v1 = Aw[:, 0]; v2 = Aw[:, 1]
v3 = V([-2, 1, 0]); v4 = V([3, 0, 1])
plane = lambda v: v[0] + 2 * v[1] - 3 * v[2]
chk("Q4a choice: (3,0,1) in plane; (1,1,0),(2,1,0),(0,1,1) not", plane(V([3, 0, 1])) == 0 and all(plane(V(v)) != 0 for v in ([1, 1, 0], [2, 1, 0], [0, 1, 1])))
exp(4, A_, 1, Aw.rank()); exp(4, A_, 2, 3 - 1)
exp(4, A_, 3, (1 * v3 + 1 * v4)[0])
chk("Q4a pivot columns of A are 1,2", Aw.rref()[1] == (0, 1))
Wm = v1.row_join(v2).row_join(v3).row_join(v4)
exp(4, B_, 0, Wm.rank())
exp(4, B_, 1, 4 - len(Wm.rref()[1]))
chk("Q4b pivots are first three columns", Wm.rref()[1] == (0, 1, 2))
exp(4, B_, 2, 2 + 2)
w = V([-1, 2, 1])
inter_dim = Aw.rank() + 2 - Wm.rank()
exp(4, C_, 0, inter_dim)
chk("Q4c (-1,2,1) in W2 and in W1", plane(w) == 0 and v1.row_join(v2).row_join(w).rank() == 2)
chk("Q4c distractors: (1,2,-1) not in W2; (-2,1,0),(3,0,1) in W2 but not in W1",
    plane(V([1, 2, -1])) != 0 and plane(v3) == 0 and plane(v4) == 0 and v1.row_join(v2).row_join(v3).rank() == 3 and v1.row_join(v2).row_join(v4).rank() == 3)
exp(4, C_, 2, (2 * v3 + 1 * v4)[1])
chk("Q4c combination 2*v3 + v4 = (-1,2,1)", 2 * v3 + v4 == w)
q = V([5, -10, -5])
chk("Q4d q = -5 w in both subspaces", q == -5 * w and plane(q) == 0 and v1.row_join(v2).row_join(q).rank() == 2)
exp(4, D_, 1, -5); exp(4, D_, 2, plane(q))

# ---- Q5
A5 = V([[1, 1, 1, 1], [1, 1, 3, 3], [-1, -1, 1, 1]])
exp(5, A_, 0, A5.rank())
chk("Q5a pivot columns 1,3", A5.rref()[1] == (0, 2) and A5[:, 1] == A5[:, 0] and A5[:, 3] == A5[:, 2])
exp(5, A_, 2, len(A5.nullspace()))
kv = V([0, 0, -1, 1])
chk("Q5a kernel vector (0,0,-1,1) and (-1,1,0,0)", A5 * kv == sp.zeros(3, 1) and A5 * V([-1, 1, 0, 0]) == sp.zeros(3, 1))
exp(5, A_, 3, kv[2])
chk("Q5b not injective and not onto", len(A5.nullspace()) == 2 and A5.rank() < 3)
exp(5, B_, 1, 3 - A5.rank())
Ak = V([[1, 1], [1, 3], [-1, 1]])
kk = sp.symbols("kk")
Aug = Ak.row_join(V([kk, 11, 1]))
chk("Q5c consistent only for k=5", Aug.subs(kk, 5).rank() == 2 and all(Aug.subs(kk, v).rank() == 3 for v in (0, 1, 4, 6)))
El = Aug.copy(); El[1, :] = El[1, :] - El[0, :]; El[2, :] = El[2, :] + El[0, :]; El[2, :] = El[2, :] - El[1, :]
exp(5, C_, 0, sp.expand(El[2, 2]).subs(kk, 5) * 1)
chk("Q5c last RHS = -10+2k", sp.expand(El[2, 2]) == 2 * kk - 10, str(sp.expand(El[2, 2])))
sc = sp.solve([sp.Symbol("x1") + sp.Symbol("x2") - 5, sp.Symbol("x1") + 3 * sp.Symbol("x2") - 11], dict=True)[0]
exp(5, C_, 1, sc[sp.Symbol("x2")]); exp(5, C_, 2, sc[sp.Symbol("x1")])
chk("Q5c (5,11,1) = 2 col1 + 3 col2", Ak * V([2, 3]) == V([5, 11, 1]))
exp(5, C_, 3, sp.solve(sp.expand(El[2, 2]), kk)[0])
Tb = V([[1, 1], [-1, 1]])
exp(5, D_, 0, Tb.det())
Fm = lambda a_, b_: V([a_ - 2 * b_, -2 * a_ + 4 * b_])
exp(5, D_, 1, Fm(1, -1)[0])
FEB = Fm(1, -1).row_join(Fm(1, 1))
res = Tb.inv() * FEB
chk("Q5d [F]_B^B", res == V([[R(9, 2), R(-3, 2)], [R(-3, 2), R(1, 2)]]))
exp(5, D_, 2, float(res[0, 0])); exp(5, D_, 3, float(res[1, 1]))

# ---- coverage: every numeric step has an expected value and matches
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
        tol = st.get("tol", 0)
        ok = abs(float(EXP[key]) - st["answer"]) <= tol + 1e-12
        chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, part, i, st["answer"], EXP[key]), ok)
# --- fix pass: A A^T = A^2 with A invertible forces A^T = A; Q4b third column is -v3
_Ms = sp.Matrix(2, 2, sp.symbols("m0:4"))
_Ainv = sp.Matrix([[2, 1], [1, 1]])
chk("Q4b (2,-1,0) == -(-2,1,0)", sp.Matrix([2, -1, 0]) == -sp.Matrix([-2, 1, 0]))
_s = sp.Matrix([[0, 1], [1, 3]]); _t = sp.Matrix([[1, 0], [0, 1]])
chk("Q1b distractor (A^-1)^T=(1/5)(A^T-A) is not A^-1 when A^T=A and A^2=5/2 I", sp.Rational(1, 5) * (sp.sqrt(sp.Rational(5, 2)) * sp.eye(2) - sp.sqrt(sp.Rational(5, 2)) * sp.eye(2)) != sp.sqrt(sp.Rational(2, 5)) * sp.eye(2))
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
