# -*- coding: utf-8 -*-
"""sympy checks of the official 22B-A answers. Run: PYTHONUTF8=1 py tools/verify/22B-A/verify_22B-A.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
R = sp.Rational
k, t, x, z, l = sp.symbols("k t x z l")
# Q1: models. A symmetric with A^2 = (5/2) I, 4x4.
a = sp.sqrt(R(5, 2))
for label, A in [("det+", sp.diag(a, a, a, a)), ("det-", sp.diag(a, a, a, -a))]:
    I4 = sp.eye(4)
    chk("Q1 model %s satisfies AA^T+A^2=5I, AA^T-A^2=0" % label, sp.simplify(A * A.T + A**2 - 5 * I4) == sp.zeros(4) and sp.simplify(A * A.T - A**2) == sp.zeros(4))
    chk("Q1a model %s A^-1=(A^T+A)/5" % label, sp.simplify(A.inv() - (A.T + A) / 5) == sp.zeros(4))
    chk("Q1b model %s A^-1 symmetric" % label, A.inv() == A.inv().T)
dp = sp.simplify(sp.diag(a, a, a, a).det()); dm = sp.simplify(sp.diag(a, a, a, -a).det())
chk("Q1c det = 25/4 for one model", dp == R(25, 4))
chk("Q1c det = -25/4 for the other (official 25/4 not forced)", dm == -R(25, 4))
chk("Q1d det(A^-1) = +-4/25", sp.simplify(sp.diag(a, a, a, a).inv().det()) == R(4, 25) and sp.simplify(sp.diag(a, a, a, -a).inv().det()) == -R(4, 25))
chk("Q1 det^2 = (5/2)^4", dp**2 == R(5, 2)**4 and dm**2 == R(5, 2)**4)
# Q2
Ma = M([[1, 1, k], [3, 4, 2], [2, 3, -1]]); rhs = M([2, k, 1])
Aug = Ma.row_join(rhs)
s1 = Aug.copy(); s1[1, :] = 3 * Aug[0, :] - Aug[1, :]; s1[2, :] = 2 * Aug[0, :] - Aug[2, :]
chk("Q2 step1", s1[1, :].applyfunc(sp.expand) == M([[0, -1, 3 * k - 2, 6 - k]]) and s1[2, :].applyfunc(sp.expand) == M([[0, -1, 2 * k + 1, 3]]))
s2 = s1.copy(); s2[0, :] = s1[0, :] + s1[1, :]; s2[1, :] = -s1[1, :]
chk("Q2 step2", s2[0, :].applyfunc(sp.expand) == M([[1, 0, 4 * k - 2, 8 - k]]) and s2[1, :].applyfunc(sp.expand) == M([[0, 1, 2 - 3 * k, k - 6]]))
s3 = s2.copy(); s3[2, :] = s2[2, :] + s2[1, :]
chk("Q2 step3 row3 (0 0 3-k | k-3)", s3[2, :].applyfunc(sp.expand) == M([[0, 0, 3 - k, k - 3]]))
chk("Q2 det zero only at k=3", sp.solve(Ma.det(), k) == [3], str(sp.factor(Ma.det())))
sol = [sp.simplify(q) for q in Ma.LUsolve(rhs)]
chk("Q2a unique solution (3(k+2), -2(k+2), -1)", sp.simplify(sol[0] - 3 * (k + 2)) == 0 and sp.simplify(sol[1] + 2 * (k + 2)) == 0 and sp.simplify(sol[2] + 1) == 0)
M3 = Ma.subs(k, 3); r3 = rhs.subs(k, 3)
chk("Q2b no inconsistent k (k=3 consistent)", M3.rank() == M3.row_join(r3).rank() == 2)
chk("Q2c k=3 family (5,-3,0)+z(-10,7,1)", sp.simplify(M3 * M([5 - 10 * z, -3 + 7 * z, z]) - r3) == sp.zeros(3, 1))
# Q2d
zz = sp.symbols("zz")
Amat = M([[1 - sp.I, sp.I * zz], [zz**2, 1 + sp.I]])
chk("Q2d det = 2 - i z^3", sp.expand(Amat.det() - (2 - sp.I * zz**3)) == 0)
roots = sp.solve(2 - sp.I * zz**3, zz)
c2 = sp.cbrt(2)
exp = {c2 * sp.I, -c2 * (sp.sqrt(3) / 2 + sp.I / 2), c2 * (sp.sqrt(3) / 2 - sp.I / 2)}
chk("Q2d roots i*2^(1/3), -2^(1/3)(cos30+i sin30), 2^(1/3)(cos30-i sin30)", all(sp.simplify(sp.expand(e**3 + 2 * sp.I)) == 0 for e in exp) and len(exp) == 3 == len(roots))
# Q3
A3 = M([[1, 2, 0], [0, 1, 1], [2, 4, 2]])
Ai = M([[-1, -2, 1], [1, 1, -R(1, 2)], [-1, 0, R(1, 2)]])
chk("Q3.1a inverse", A3.inv() == Ai)
E1 = M([[1, -2, 0], [0, 1, 0], [0, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, -1], [0, 0, 1]])
E3 = sp.diag(1, 1, R(1, 2)); E4 = M([[1, 0, 0], [0, 1, 0], [-2, 0, 1]])
chk("Q3.1b E1E2E3E4 = A^-1", E1 * E2 * E3 * E4 == Ai)
B3 = M([[2, 1, 1], [1, 2, 1], [0, 0, 1]])
chk("Q3.2 charpoly (l-1)^2(l-3)", sp.expand(B3.charpoly(l).as_expr() - (l - 1)**2 * (l - 3)) == 0)
P = M([[-1, -1, 1], [1, 0, 1], [0, 1, 0]]); D = sp.diag(1, 1, 3)
chk("Q3.2 D=P^-1BP", P.inv() * B3 * P == D)
# Q4
A4 = M([[1, 2, -4], [-2, 3, -13], [-1, -1, 1]])
v1 = M([1, -2, -1]); v2 = M([2, 3, -1]); v3 = M([-2, 1, 0]); v4 = M([3, 0, 1])
chk("Q4a rref pivots 1,2 and rank 2", A4.rref()[1] == (0, 1) and A4.rank() == 2)
chk("Q4a col3 = 2 v1 - 3 v2", A4[:, 2] == 2 * v1 - 3 * v2)
chk("Q4a v3,v4 in W2 and independent", all((v[0] + 2 * v[1] - 3 * v[2]) == 0 for v in (v3, v4)) and M.hstack(v3, v4).rank() == 2)
chk("Q4a official slip s(-2,0,1) is NOT in W2", (-2 + 0 - 3) != 0)
W = M.hstack(v1, v2, -v3, -v4)
chk("Q4b matrix columns as printed", W == M([[1, 2, 2, -3], [-2, 3, -1, 0], [-1, -1, 0, -1]]))
chk("Q4b dim(W1+W2)=3, pivots 1,2,3", W.rank() == 3 and W.rref()[1] == (0, 1, 2))
ns = W.nullspace()
chk("Q4c nullspace 1-dim, beta1=2 beta2", len(ns) == 1 and ns[0][2] * 1 == 2 * ns[0][3])
vint = M([-1, 2, 1])
chk("Q4c (-1,2,1) in W1 and W2", M.hstack(v1, v2, vint).rank() == 2 and (vint[0] + 2 * vint[1] - 3 * vint[2]) == 0)
chk("Q4c dim cap = 2+2-3 = 1", 2 + 2 - 3 == 1)
chk("Q4c 2t v3 + t v4 = t(-1,2,1)", 2 * v3 + v4 == vint)
chk("Q4d (5,-10,-5) = -5 (-1,2,1)", M([5, -10, -5]) == -5 * vint)
# Q5
A5 = M([[1, 1, 1, 1], [1, 1, 3, 3], [-1, -1, 1, 1]])
a_, b_, c_, d_ = sp.symbols("a b c d")
xs = sp.symbols("xs")
Tv = (a_ + b_ + c_ + d_) + (a_ + b_ + 3 * c_ + 3 * d_) * xs + (-a_ - b_ + c_ + d_) * xs**2
cols = [Tv.subs({a_: int(i == 0), b_: int(i == 1), c_: int(i == 2), d_: int(i == 3)}) for i in range(4)]
chk("Q5a matrix from T", M([[sp.Poly(cc, xs).coeff_monomial(xs**j) for cc in cols] for j in range(3)]) == A5)
chk("Q5a rank 2, pivots 1,3", A5.rank() == 2 and A5.rref()[1] == (0, 2))
ns5 = A5.nullspace()
chk("Q5a kernel basis (-1,1,0,0),(0,0,-1,1)", len(ns5) == 2 and all(A5 * v == sp.zeros(3, 1) for v in (M([-1, 1, 0, 0]), M([0, 0, -1, 1]))) and M.hstack(M([-1, 1, 0, 0]), M([0, 0, -1, 1])).rank() == 2)
chk("Q5b not onto, not 1-1", A5.rank() < 3 and A5.rank() < 4)
chk("Q5c k=5 only", [kk for kk in range(-20, 21) if M.hstack(A5[:, 0], A5[:, 2]).row_join(M([kk, 11, 1])).rank() == 2] == [5])
Fm = M([[1, -2], [-2, 4]])  # F(a+bx) in basis (1,x): columns F(1), F(x)
Bm = M([[1, 1], [-1, 1]])
chk("Q5d F(1-x)=3-6x, F(1+x)=-1+2x", Fm * M([1, -1]) == M([3, -6]) and Fm * M([1, 1]) == M([-1, 2]))
chk("Q5d [F]_B^B = [[9/2,-3/2],[-3/2,1/2]]", Bm.inv() * Fm * Bm == M([[R(9, 2), -R(3, 2)], [-R(3, 2), R(1, 2)]]))
print("ALL OK" if not bad else "MISMATCHES: " + ", ".join(bad))
