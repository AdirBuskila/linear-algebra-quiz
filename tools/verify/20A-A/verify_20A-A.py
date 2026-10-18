# -*- coding: utf-8 -*-
"""sympy checks of the solver's 20A-A answers (no official key exists). Run: PYTHONUTF8=1 py tools/verify/20A-A/verify_20A-A.py
Every check is an assertion; ASCII output only."""
import sympy as sp

M, R, I = sp.Matrix, sp.Rational, sp.I
a, k, lam, s, t = sp.symbols("a k lam s t")
n = 0


def chk(name, cond):
    global n
    assert cond, name
    n += 1
    print("OK  " + name)


# Q1
n1 = M([1, -2, 1]); n2 = M([k, -1, k])
chk("Q1a parallel iff k=1/2", sp.solve(list(n1.cross(n2)), k) == {k: R(1, 2)} or sp.solve(list(n1.cross(n2)), k) == [R(1, 2)])
P1 = M([-5, 0, 0])
chk("Q1a (-5,0,0) on pi1; distance to x-2y+z-4=0 is 9/sqrt6 = 3sqrt6/2", (n1.T * P1)[0] + 5 == 0 and sp.simplify(abs((n1.T * P1)[0] - 4) / n1.norm() - 3 * sp.sqrt(6) / 2) == 0)
chk("Q1a pi2 at k=1/2 times 2 = x-2y+z-4", 2 * (n2.subs(k, R(1, 2))) == n1)
chk("Q1b perpendicular iff k=-1", sp.solve(n1.dot(n2), k) == [-1])
N = n1.cross(n2.subs(k, 2))
chk("Q1c n1 x n2 = (-3,0,3); plane x-z=0 through (1,1,1)", N == M([-3, 0, 3]) and M([1, 0, -1]).dot(n1) == 0 and M([1, 0, -1]).dot(n2.subs(k, 2)) == 0 and 1 - 1 == 0)
th = sp.atan(R(3, 5))
roots = [34 ** R(1, 10) * sp.exp(I * (th + 2 * sp.pi * j) / 5) for j in range(5)]
chk("Q1d five roots of z^5 = 5+3i", all(abs(sp.N(r**5 - (5 + 3 * I))) < 1e-9 for r in roots) and len({sp.N(r, 8) for r in roots}) == 5)
chk("Q1d |5+3i| = sqrt34, angles ~6.19 deg + 72k", sp.Abs(5 + 3 * I) == sp.sqrt(34) and [round(float((th + 2 * sp.pi * j) / 5 * 180 / sp.pi), 2) for j in range(5)] == [6.19, 78.19, 150.19, 222.19, 294.19]
    and round(float(34 ** R(1, 10)), 3) == 1.423)

# Q2
A = M([[1, 0, 1, 1], [1, 1, 2, 0], [0, 1, 1, -1]])
chk("Q2a rref", A.rref()[0] == M([[1, 0, 1, 1], [0, 1, 1, -1], [0, 0, 0, 0]]))
chk("Q2a null basis", A * M([-1, -1, 1, 0]) == sp.zeros(3, 1) and A * M([-1, 1, 0, 1]) == sp.zeros(3, 1) and len(A.nullspace()) == 2)
chk("Q2b row basis spans row space, dim 2", M([[1, 0, 1, 1], [0, 1, 1, -1]]).col_join(A).rank() == 2 and A.rank() == 2 and A[2, :] == A[1, :] - A[0, :])
chk("Q2c col basis cols 1,2; col3=c1+c2, col4=c1-c2", A[:, 2] == A[:, 0] + A[:, 1] and A[:, 3] == A[:, 0] - A[:, 1] and A[:, :2].rank() == 2)
chk("Q2d 2+2=4", len(A.nullspace()) + A.rank() == A.cols)

# Q3
A3 = M([[2, 1, -1], [1, a, 1], [3, 1, -a]])
chk("Q3a det = -2a(a-2)", sp.expand(A3.det() + 2 * a * (a - 2)) == 0 and sp.expand(2 * (-a**2 - 1) - (-a - 3) - (1 - 3 * a) - A3.det()) == 0)
A31 = A3.subs(a, 1)
chk("Q3b det 2, adj and inverse", A31.det() == 2 and A31.adjugate() == M([[-2, 0, 2], [4, 1, -3], [-2, 1, 1]]) and A31.inv() == M([[-1, 0, 1], [2, R(1, 2), -R(3, 2)], [-1, R(1, 2), R(1, 2)]]))
B = M([[1, 1, -1], [1, 1, 1], [1, 1, 1]])
chk("Q3c char poly lam(lam-1)(lam-2)", sp.expand((lam * sp.eye(3) - B).det() - lam * (lam - 1) * (lam - 2)) == 0)
inner = M([[lam - 1, -1, 1], [0, 1, -1], [-1, -1, lam - 1]])
chk("Q3c row trick: R2-R3 gives lam*(inner), inner=(lam-1)(lam-2)", sp.expand(inner.det() - (lam - 1) * (lam - 2)) == 0 and M([[-1, 1], [1, -1]]).det() == 0)
for lv, v in ((0, [-1, 1, 0]), (1, [-1, 1, 1]), (2, [0, 1, 1])):
    chk(f"Q3c eigvec {lv}", B * M(v) == lv * M(v))
P = M([[-1, -1, 0], [1, 1, 1], [0, 1, 1]]); D = sp.diag(0, 1, 2)
chk("Q3d |P|=1, P^-1AP=D, AP shown", P.det() == 1 and P.inv() * B * P == D and B * P == M([[0, -1, 0], [0, 1, 2], [0, 1, 2]]))

# Q4
W1 = M([[1, 1, 1], [1, 2, 3], [2, 3, 1], [3, 1, 2]])
chk("Q4a W1 = R^3", W1.rank() == 3)
E = W1.copy(); E[1, :] -= E[0, :]; E[2, :] -= 2 * E[0, :]; E[3, :] -= 3 * E[0, :]
ok = E[1:, :] == M([[0, 1, 2], [0, 1, -1], [0, -2, -1]]); E[2, :] -= E[1, :]; E[3, :] += 2 * E[1, :]
ok = ok and E[2, :] == M([[0, 0, -3]]) and E[3, :] == M([[0, 0, 3]])
chk("Q4a printed reduction", ok)
w2 = M([[1, -2, -1]])
chk("Q4a W2 basis (2,1,0),(1,0,1), dim 2", w2 * M([2, 1, 0]) == M([0]) and w2 * M([1, 0, 1]) == M([0]) and len(w2.nullspace()) == 2)
chk("Q4b/c sum R^3, cap W2 dim 2", W1.col_join(M([[2, 1, 0], [1, 0, 1]])).rank() == 3 and 3 + 2 - 3 == 2)
chk("Q4d (3,1,-1) not in W2", (w2 * M([3, 1, -1]))[0] != 0 and 3 - 1 == 2 and -1 + 1 == 0)

# Q5
T = M([[1, -1, 0], [-2, 2, 0], [0, 0, 2]])
chk("Q5b ker (1,1,0) dim 1, Im (1,-2,0),(0,0,1) dim 2", T * M([1, 1, 0]) == sp.zeros(3, 1) and len(T.nullspace()) == 1 and T.rank() == 2
    and T.row_join(M([1, -2, 0])).rank() == 2 and T.row_join(M([0, 0, 1])).rank() == 2)
chk("Q5c (1,0,0) not in Im", T.row_join(M([1, 0, 0])).rank() == 3)
B1 = M([[1, 0, 0], [1, 1, 0], [1, 1, 1]]); B2 = M([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
Tm = M([[2, -1, 2], [2, 2, 2], [-2, 0, -2]])
chk("Q5d [T]_{B2}^{B1}", B2.inv() * T * B1 == Tm and B2 * Tm == T * B1)
chk("Q5d coordinate formula", all(B2 * M([p - q + r, r, q - r]) == M([p, q, r]) for p, q, r in ((0, 0, 2), (-1, 2, 2), (3, -1, 5))))

print(f"ALL {n} CHECKS OK")
