# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 22A-A (rubric/pitfalls/steps in tools/gen/gen_22A-A.py).
Run: PYTHONUTF8=1 py tools/verify/22A-A/verify_steps_22A-A.py
Every numeric step in tools/raw/22A-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "22A-A.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_, E_ = "א", "ב", "ג", "ד", "ה"
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


a, b, x, c_, d_ = sp.symbols("a b x c_ d_")

# ---- Q1a  det(C D^2) = det(D^3 C^-1)  =>  det D = (det C)^2
chk("Q1a (dc)^2 (dd)^2 = dd^3 with dd != 0 gives dd = dc^2", sp.solve(sp.Eq(c_**2 * d_**2, d_**3), d_) == [0, c_**2] or set(sp.solve(sp.Eq(c_**2 * d_**2, d_**3), d_)) == {0, c_**2})
chk("Q1a bug line: the '+' version gives dd = -dc^2 (negative), contradicting dd = dc^2", sp.solve(d_ + c_**2, d_) == [-c_**2] and sp.simplify(-c_**2 - c_**2) != 0)
Cm = sp.diag(3, 1); Dm = sp.diag(9, 1)
chk("Q1a model: C=diag(3,1), D=diag(9,1) satisfies C D^2 = D^3 C^-1 and det D = (det C)^2", Cm * Dm**2 == Dm**3 * Cm.inv() and Dm.det() == Cm.det() ** 2)
Cm2 = sp.diag(-3, 1); Dm2 = sp.diag(9, 1)
chk("Q1a model with det C = -3: C D^2 = D^3 C^-1 holds, det D = 9", Cm2 * Dm2**2 == Dm2**3 * Cm2.inv() and Dm2.det() == 9)
exp(1, A_, 1, Dm2.det())

# ---- Q1b
I2 = sp.eye(2)
Ap = sp.diag(1, 0)
chk("Q1b A^2=A, A != 0 but A-I singular", Ap**2 == Ap and Ap != sp.zeros(2) and (Ap - I2).det() == 0)
exp(1, B_, 1, (Ap - I2).det())
Ag = V([[1, 2], [3, 4]])
chk("Q1b (A-I)^2 = A^2 - 2A + I; with A^2=A it is -(A-I)", sp.expand((Ag - I2) ** 2) == Ag**2 - 2 * Ag + I2 and (Ap - I2) ** 2 == -(Ap - I2))
chk("Q1b bug line: A-2A+I = -(A-I) != A-I for A=0", (0 * I2 - 2 * 0 * I2 + I2) != (0 * I2 - I2) and -(Ap - I2) != (Ap - I2))
chk("Q1b invertible A-I and (A-I)^2 = -(A-I) forces A=0: A-I=-I", sp.zeros(2) - I2 == -I2)

# ---- Q1c
Cc = V([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]); Dd = V([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
chk("Q1c C, D antisymmetric", Cc.T == -Cc and Dd.T == -Dd)
CD = Cc * Dd
chk("Q1c CD = official", CD == V([[-3, -2, 1], [-3, -4, -1], [3, -2, -5]]))
exp(1, C_, 1, Cc.det()); exp(1, C_, 2, CD[0, 0]); exp(1, C_, 3, CD.det())
chk("Q1c choice: odd n -> det of antisymmetric = 0 (CD never invertible); even n: C=0 counterexample; claim false in general",
    all((V(m).det() == 0) for m in ([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]], [[0, 5, 1], [-5, 0, 2], [-1, -2, 0]])) and sp.zeros(2) * V([[0, 1], [-1, 0]]) == sp.zeros(2))

# ---- Q2 parameters a, b
M = V([[1, 0, 0, 2], [0, a**2 - a, a**2 - a, 0], [1, 0, a - 1, a + 1], [2, a**2 - a, a**2 + a - 2, 2 * a + 2]]); rhs = V([4, a, a + 3, 3 * a + b])
E = M.row_join(rhs)
E1 = E.copy(); E1[2, :] = (E1[2, :] - E1[0, :]).applyfunc(sp.expand); E1[3, :] = (E1[3, :] - 2 * E1[0, :]).applyfunc(sp.expand)
exp(2, A_, 0, E1[2, 2].subs(a, 3)); exp(2, A_, 1, E1[3, 4].subs({a: 2, b: 5}))
E2 = E1.copy(); E2[3, :] = (E2[3, :] - E2[1, :]).applyfunc(sp.expand)
exp(2, A_, 2, E2[3, 2].subs(a, 2))
E3 = E2.copy(); E3[3, :] = (E3[3, :] - 2 * E3[2, :]).applyfunc(sp.expand)
chk("Q2a final echelon row 4 = (0,0,0,0|b-6)", E3[3, :] == V([[0, 0, 0, 0, b - 6]]))
chk("Q2a final rows 2,3", E3[1, :] == V([[0, a**2 - a, a**2 - a, 0, a]]) and E3[2, :] == V([[0, 0, a - 1, a - 1, a - 1]]))
exp(2, A_, 3, E3[3, 4].subs(b, 10))
rk = lambda av, bv: (M.subs(a, av).rank(), M.subs(a, av).row_join(rhs.subs({a: av, b: bv})).rank())
chk("Q2b a=1,b=6 -> no solution", rk(1, 6)[0] < rk(1, 6)[1])
chk("Q2b b!=6 -> none; b=6,a!=1 -> infinite; never unique",
    all(rk(av, 7)[0] < rk(av, 7)[1] for av in (0, 1, 2, 5)) and all(rk(av, 6)[0] == rk(av, 6)[1] < 4 for av in (0, 2, 5, -3)))
exp(2, B_, 1, M.subs(a, 2).rank()); exp(2, B_, 2, M.subs(a, 0).rank())
# Q2c a=0,b=6
M0 = M.subs(a, 0); r0 = rhs.subs({a: 0, b: 6})
sol0 = V([4 - 2 * 1, 7, 1 - 1, 1])
chk("Q2c solution x=4-2t2, y=t1, z=1-t2, w=t2", all(M0 * V([4 - 2 * t2, t1, 1 - t2, t2]) == r0 for t1 in (0, 3) for t2 in (0, 1, 4)))
chk("Q2c official slip x=4-t2 fails", M0 * V([4 - 1, 0, 0, 1]) != r0)
exp(2, C_, 0, 4 - 2 * 1); exp(2, C_, 1, 1 - 1); exp(2, C_, 2, 4 - M0.rank())
# Q2d a=2,b=6
M2 = M.subs(a, 2); r2 = rhs.subs({a: 2, b: 6})
chk("Q2d solution (4-2t, t, 1-t, t)", all(M2 * V([4 - 2 * t, t, 1 - t, t]) == r2 for t in (0, 1, 3, -2)))
chk("Q2d official slip x=4-t fails", M2 * V([3, 1, 0, 1]) != r2)
exp(2, D_, 0, 4 - 2 * 1); exp(2, D_, 1, 1 - 3); exp(2, D_, 2, 4 - M2.rank())
# Q2e
z = [sp.cos(2 * sp.pi * kk / 3) + sp.I * sp.sin(2 * sp.pi * kk / 3) for kk in range(3)]
exp(2, E_, 0, round(float(sp.re(z[1])), 3))
chk("Q2e sum of roots = 0", sp.simplify(sum(z)) == 0)
chk("Q2e products z1*z0=z1, z1*z1=z2, z1*z2=z0 (and the bug z1*z2=z2 is false)", all(sp.simplify(z[1] * z[j] - z[(1 + j) % 3]) == 0 for j in range(3)) and sp.simplify(z[1] * z[2] - z[2]) != 0)
chk("Q2e z1 != 1", sp.simplify(z[1] - 1) != 0)

# ---- Q3
A3 = V([[1, 3, 0], [0, 3, 1], [1, 3, 1]])
Ai = A3.inv()
exp(3, A_, 0, A3.det())
E1m = sp.eye(3); E1m[2, :] = E1m[2, :] - E1m[0, :]
exp(3, A_, 1, (E1m * A3)[2, 2])
exp(3, A_, 2, round(float(Ai[1, 0]), 3)); exp(3, A_, 3, Ai[2, 0])
chk("Q3a A^-1 official", Ai == V([[0, -1, 1], [R(1, 3), R(1, 3), R(-1, 3)], [-1, 0, 1]]))
Ea = [V([[1, 0, 0], [0, 1, 0], [-1, 0, 1]]), V([[1, 0, 0], [0, 1, -1], [0, 0, 1]]), V([[1, -1, 0], [0, 1, 0], [0, 0, 1]]), V([[1, 0, 0], [0, R(1, 3), 0], [0, 0, 1]])]
prod = Ea[3] * Ea[2] * Ea[1] * Ea[0]
chk("Q3b E4 E3 E2 E1 A = I, product = A^-1", prod == Ai and prod * A3 == sp.eye(3))
chk("Q3b choice: reversed order differs", Ea[0] * Ea[1] * Ea[2] * Ea[3] != Ai)
exp(3, B_, 1, round(float(prod.det()), 3)); exp(3, B_, 2, prod[0, 1])
B3 = V([[1, 1, 0], [0, -2, 0], [-1, 0, 3]])
lam = sp.symbols("lam")
exp(3, C_, 0, (B3 - 0 * sp.eye(3)).det())
exp(3, C_, 1, len(B3.eigenvals()))
P3 = V([[2, 5, 0], [0, -15, 0], [1, 1, 1]])
chk("Q3c BP = P diag(1,-2,3)", B3 * P3 == P3 * sp.diag(1, -2, 3) and P3.det() != 0)
exp(3, C_, 3, (B3 * P3)[0, 1])
chk("Q3c choice: B has 3 distinct eigenvalues; not symmetric, not diagonal; det != 0 not sufficient",
    sorted(B3.eigenvals()) == [-2, 1, 3] and B3 != B3.T and not B3.is_diagonal() and B3.det() != 0 and not V([[1, 1], [0, 1]]).is_diagonalizable())

# ---- Q4
a_ = V([1, 2, -1]); b_ = V([2, 1, -1])
w1 = lambda v: v[0] + 2 * v[1] - v[2]
w2 = lambda v: 2 * v[0] + v[1] - v[2]
chk("Q4a (1,0,1) in W1; (1,1,0),(0,1,1),(1,2,1) not", w1(V([1, 0, 1])) == 0 and all(w1(V(v)) != 0 for v in ([1, 1, 0], [0, 1, 1], [1, 2, 1])))
exp(4, A_, 1, 3 - 1); exp(4, A_, 2, 3 - 1)
exp(4, A_, 3, 2 * 1 + 2)
chk("Q4a bases", all(w1(V(v)) == 0 for v in ([1, 0, 1], [0, 1, 2])) and all(w2(V(v)) == 0 for v in ([1, 0, 2], [0, 1, 1])))
vs = [V([1, 0, 1]), V([0, 1, 2]), V([1, 0, 2]), V([0, 1, 1])]
rk4 = V.hstack(*vs).rank()
exp(4, B_, 0, rk4); exp(4, B_, 1, 2 + 2); exp(4, B_, 2, rk4)
exp(4, C_, 0, 2 + 2 - rk4)
chk("Q4c (1,1,3) in W1 and W2", w1(V([1, 1, 3])) == 0 and w2(V([1, 1, 3])) == 0)
chk("Q4c distractors fail: (1,0,1) not in W2; (1,0,2) not in W1; (1,1,1) not in W1",
    w2(V([1, 0, 1])) != 0 and w1(V([1, 0, 2])) != 0 and w1(V([1, 1, 1])) != 0)
exp(4, C_, 2, w2(V([1, 1, 3])))
chk("Q4c dim(W1 cap W2) = 1", V.hstack(*vs[:2]).rank() + V.hstack(*vs[2:]).rank() - rk4 == 1)
q = V([2, 2, 6])
chk("Q4d (2,2,6) = 2(1,1,3), in W1 and W2", q == 2 * V([1, 1, 3]) and w1(q) == 0 and w2(q) == 0)
exp(4, D_, 1, 2); exp(4, D_, 2, w1(q))

# ---- Q5
A5 = V([[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]])
exp(5, A_, 0, A5.rank())
chk("Q5a pivots 1,2,3 (col4 = col3)", A5.rref()[1] == (0, 1, 2) and A5[:, 3] == A5[:, 2])
exp(5, A_, 2, len(A5.nullspace()))
nk = A5.nullspace()[0]; nk = nk / nk[3]
chk("Q5a kernel vector (0,0,-1,1)", list(nk) == [0, 0, -1, 1])
exp(5, A_, 3, nk[2])
exp(5, B_, 1, A5.rank()); exp(5, B_, 2, 3 - A5.rank())
chk("Q5b not injective, onto", len(A5.nullspace()) == 1 and A5.rank() == 3)
tt = sp.symbols("tt")
exp(5, C_, 0, sp.solve(2 + tt, tt)[0])
chk("Q5c k=0: (0,0,2,-2) = -2*(0,0,-1,1) in Nul A", A5 * V([0, 0, 2, -2]) == sp.zeros(3, 1) and V([0, 0, 2, -2]) == -2 * nk)
exp(5, C_, 1, 0); exp(5, C_, 2, len(A5.nullspace()))
Bm = V([[2, 3], [3, 5]])
exp(5, D_, 0, Bm.det()); exp(5, D_, 1, Bm.inv()[0, 0])
F = V([[7, 5], [3, 2]]) * Bm.inv()
chk("Q5d [F]_E^E official, F(2,3)=(7,3), F(3,5)=(5,2)", F == V([[20, -11], [9, -5]]) and F * V([2, 3]) == V([7, 3]) and F * V([3, 5]) == V([5, 2]))
exp(5, D_, 2, F[0, 0]); exp(5, D_, 3, F[0, 1])

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
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
