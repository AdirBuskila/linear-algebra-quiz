# -*- coding: utf-8 -*-
"""sympy checks of the solver's 21A-A answers (no official key exists). Run: PYTHONUTF8=1 py tools/verify/21A-A/verify_21A-A.py
Every check is an assertion; ASCII output only. Q3b is held (A singular at a=2) and is checked as such."""
import sympy as sp

M, R, I = sp.Matrix, sp.Rational, sp.I
a, x, s, t, b, lam = sp.symbols("a x s t b lam")
n = 0


def chk(name, cond):
    global n
    assert cond, name
    n += 1
    print("OK  " + name)


# Q1: AA^T + A^2 = 3I, AA^T - A^2 = 0 -> A^-1 = 2/3 A = 2/3 A^T, |A| = +-3sqrt6/4
c = sp.sqrt(R(3, 2))
for sign in (1, -1):
    A = sign * c * sp.eye(3)
    chk(f"Q1 model sign={sign} satisfies both equations", sp.simplify(A * A.T + A * A - 3 * sp.eye(3)) == sp.zeros(3) and sp.simplify(A * A.T - A * A) == sp.zeros(3))
    chk(f"Q1a A^-1 = 2/3 A (sign={sign})", sp.simplify(A.inv() - R(2, 3) * A) == sp.zeros(3))
    chk(f"Q1c |A| = {sign}*3sqrt6/4", sp.simplify(A.det() - sign * 3 * sp.sqrt(6) / 4) == 0)
    chk(f"Q1d |A^-1| = {sign}*2sqrt6/9", sp.simplify(A.inv().det() - sign * 2 * sp.sqrt(6) / 9) == 0)
# a non-scalar model too (diag with mixed signs) -> still |A|^2 = 27/8
A = c * sp.diag(1, -1, 1)
chk("Q1 mixed-sign model satisfies equations, |A|^2=27/8", sp.simplify(A * A.T + A * A - 3 * sp.eye(3)) == sp.zeros(3) and sp.simplify(A.det() ** 2) == R(27, 8))
chk("Q1b A^-1 symmetric", sp.simplify(A.inv() - A.inv().T) == sp.zeros(3))
chk("Q1c sqrt(27/8) = 3sqrt6/4", sp.simplify(sp.sqrt(R(27, 8)) - 3 * sp.sqrt(6) / 4) == 0)

# Q2
Aug = M([[1, -1, -a, a], [a, 1, -1, -a], [1, a, 1, -1]])
chk("Q2 det = -(a-2)(a+1)^2", sp.expand(Aug[:, :3].det() + (a - 2) * (a + 1) ** 2) == 0)
S1 = Aug.copy(); S1[1, :] = S1[1, :] - a * S1[0, :]; S1[2, :] = S1[2, :] - S1[0, :]
chk("Q2a after R2-aR1, R3-R1", sp.expand(S1 - M([[1, -1, -a, a], [0, a + 1, a**2 - 1, -a**2 - a], [0, a + 1, a + 1, -a - 1]])) == sp.zeros(3, 4))
S2 = M([[1, -1, -a, a], [0, 1, a - 1, -a], [0, 0, 2 - a, a - 1]])
chk("Q2a S2 rows are (R2/(a+1)) and (R3-R2)/(a+1)", sp.simplify(S2[1, :] - S1[1, :] / (a + 1)) == sp.zeros(1, 4) and sp.simplify(S2[2, :] - (S1[2, :] - S1[1, :]) / (a + 1)) == sp.zeros(1, 4))
sol = Aug[:, :3].LUsolve(Aug[:, 3])
chk("Q2a/b unique solution formula", sp.simplify(sol - M([(1 - a) / (a - 2), 1 / (a - 2), (1 - a) / (a - 2)])) == sp.zeros(3, 1))
chk("Q2a a=2 rref", Aug.subs(a, 2).rref()[0] == M([[1, 0, -1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]))
chk("Q2a a=2 echelon (before rref)", S2.subs(a, 2) == M([[1, -1, -2, 2], [0, 1, 1, -2], [0, 0, 0, 1]]))
chk("Q2a a=-1 rref", Aug.subs(a, -1).rref()[0] == M([[1, -1, 1, -1], [0, 0, 0, 0], [0, 0, 0, 0]]))
chk("Q2b a=2 none, a=-1 infinite", Aug.subs(a, 2)[:, :3].rank() == 2 and Aug.subs(a, 2).rank() == 3 and Aug.subs(a, -1).rank() == Aug.subs(a, -1)[:, :3].rank() == 1)
v = M([-1 + s - t, s, t])
chk("Q2c a=-1 family solves", sp.expand(Aug.subs(a, -1)[:, :3] * v - Aug.subs(a, -1)[:, 3]) == sp.zeros(3, 1))
z = sp.symbols("z")
roots = [0, -2, 1 + sp.sqrt(3) * I, 1 - sp.sqrt(3) * I]
chk("Q2d roots of z^4+8z", all(sp.expand(r**4 + 8 * r) == 0 for r in roots) and len(set(roots)) == 4 and sp.degree(z**4 + 8 * z, z) == 4)

# Q3
A3 = M([[2 * a, 3, 6], [4, a + 1, 4 * a - 2], [1, 5, 2]])
chk("Q3a det = -36a^2+30a+84 = -6(a-2)(6a+7)", sp.expand(A3.det() - (-36 * a**2 + 30 * a + 84)) == 0 and sp.expand(-6 * (a - 2) * (6 * a + 7) - (-36 * a**2 + 30 * a + 84)) == 0)
chk("Q3b HOLD: A singular at a=2 (rows 1,2 equal)", A3.subs(a, 2).det() == 0 and A3.subs(a, 2)[0, :] == A3.subs(a, 2)[1, :])
B = M([[6, 0, 2], [1, 4, 0], [0, 0, 3]])
chk("Q3c char poly (l-3)(l-4)(l-6)", sp.expand((lam * sp.eye(3) - B).det() - (lam - 3) * (lam - 4) * (lam - 6)) == 0)
for lv, vec in ((3, [-2, 2, 3]), (4, [0, 1, 0]), (6, [2, 1, 0])):
    chk(f"Q3c eigvec for {lv}", B * M(vec) == lv * M(vec) and (B - lv * sp.eye(3)).rank() == 2)
P = M([[-2, 0, 2], [2, 1, 1], [3, 0, 0]]); D = sp.diag(3, 4, 6)
chk("Q3d P^-1BP = D, |P|=-6, BP shown", P.det() == -6 and P.inv() * B * P == D and B * P == M([[-6, 0, 12], [6, 4, 6], [9, 0, 0]]))

# Q4 (coords a0,a1,a2)
U = M([[1, 1, 0], [2, 0, -1], [0, 2, 1]])
chk("Q4a U rank 2, 2x+x^2 = 2(1+x)-(2-x^2)", U.rank() == 2 and U[2, :] == 2 * U[0, :] - U[1, :])
Wb = M([[1, 0, 0], [0, -2, 1]])
chk("Q4a W basis satisfies a1+2a2=0, dim 2", all(r[1] + 2 * r[2] == 0 for r in Wb.tolist()) and Wb.rank() == 2 and 3 - M([[0, 1, 2]]).rank() == 2)
chk("Q4b U+W = R2[x]", U[:2, :].col_join(Wb).rank() == 3)
q = M([4, 2, -1])
chk("Q4c 4+2x-x^2 in U and W", U[:2, :].T.row_join(q).rank() == 2 and q[1] + 2 * q[2] == 0)
chk("Q4c dim U cap W = 1", 2 + 2 - U[:2, :].col_join(Wb).rank() == 1)
qp = 4 + 2 * x - x**2
chk("Q4d q(2)+q(-2)=0", qp.subs(x, 2) + qp.subs(x, -2) == 0 and qp.subs(x, 2) == 4)

# Q5: T(a b; c d) = (a+b, b+c, b+d)
T5 = M([[1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1]])
chk("Q5b kernel = span(-1,1,-1,-1), dim 1", T5 * M([-1, 1, -1, -1]) == sp.zeros(3, 1) and len(T5.nullspace()) == 1)
chk("Q5b rank 3 = onto; T(E11),T(E21),T(E22) standard", T5.rank() == 3 and T5[:, 0] == M([1, 0, 0]) and T5[:, 2] == M([0, 1, 0]) and T5[:, 3] == M([0, 0, 1]))
fam = M([1 - t, t, 1 - t, 1 - t])
chk("Q5d family maps to (1,1,1) and is all solutions", sp.expand(T5 * fam) == M([1, 1, 1]) and len(T5.nullspace()) == 1)
chk("Q5d zero matrix not in family", sp.solve([1 - t, t], t) == [])

print(f"ALL {n} CHECKS OK")
