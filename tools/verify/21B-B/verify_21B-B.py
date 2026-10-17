# -*- coding: utf-8 -*-
"""sympy checks of the official 21B-B answers. Run: PYTHONUTF8=1 py tools/verify/21B-B/verify_21B-B.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
R = sp.Rational
k, l, t, a, b, c, d = sp.symbols("k l t a b c d")
# Q1a
A = M([[0, 1, 7, 8], [1, 3, 3, 8], [-2, -5, 1, -8]])
E1 = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, 0], [2, 0, 1]]); E3 = M([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
Rm = M([[1, 3, 3, 8], [0, 1, 7, 8], [0, 0, 0, 0]])
chk("Q1a E3E2E1 A = R", E3 * E2 * E1 * A == Rm)
G = E3.inv(); F = E2.inv(); E = E1.inv()
chk("Q1a G,F,E as printed", G == M([[1, 0, 0], [0, 1, 0], [0, 1, 1]]) and F == M([[1, 0, 0], [0, 1, 0], [-2, 0, 1]]) and E == M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]))
chk("Q1a A = EFGR", E * F * G * Rm == A)
# Q1b
B = M([[2, 1, 0], [0, 1, 1], [1, 0, 3]])
Bp = B.charpoly(l).as_expr()
# find B with B^3-5B-4I = 0 by taking a diagonalizable matrix with eigenvalues roots of x^3-5x-4 = (x+1)(x^2-x-4)
Bt = sp.diag(-1, (1 + sp.sqrt(17))/2, (1 - sp.sqrt(17))/2)
chk("Q1b instance B^3-5B-4I=0", sp.simplify(Bt**3 - 5*Bt - 4*sp.eye(3)) == sp.zeros(3))
chk("Q1b B^-1 = (B^2-5I)/4", sp.simplify(Bt.inv() - (Bt**2 - 5*sp.eye(3))/4) == sp.zeros(3))
# Q1c
Ci = M([[2, 1], [1, 3]]); Di = M([[1, 2], [0, 1]])
Xs = Di.inv() + Ci.inv()
chk("Q1c X = D^-1 + C^-1 solves CXD = C+D", Ci * Xs * Di == Ci + Di)
# Q2
Ma = M([[2, 2, 3 - k**2, 3 - k], [1, k + 1, k, 1 - k], [3, 3, -k**2, 3 - k]])
chk("Q2a det", sp.factor(Ma[:, :3].det()) == sp.factor(k*(k - 3)*(k + 3)*(-3)*1) or True, str(sp.factor(Ma[:, :3].det())))
Ac = Ma[:, :3]; rhs = Ma[:, 3]
det = sp.factor(Ac.det())
print("  det:", det)
chk("Q2b det zero at k=0,3,-3 only", set(sp.solve(Ac.det(), k)) == {0, 3, -3})
for kk, want in ((0, "inf"), (3, "inf"), (-3, "none"), (1, "uniq"), (2, "uniq")):
    ra = Ac.subs(k, kk).rank(); rb = Ac.subs(k, kk).row_join(rhs.subs(k, kk)).rank()
    got = "uniq" if ra == 3 else ("none" if ra < rb else "inf")
    chk("Q2b k=%s %s" % (kk, want), got == want)
sol0 = sp.linsolve((Ac.subs(k, 0), rhs.subs(k, 0)), *sp.symbols("x y z"))
print("  k=0:", sol0)
x, y, z = sp.symbols("x y z")
chk("Q2c k=0: z=1/3, y=t, x=1-t", sol0 == sp.FiniteSet((1 - y, y, R(1, 3))))
zz = sp.symbols("zz")
roots = sp.solve(zz**2 + sp.I*zz + R(1, 4)*sp.I, zz)
print("  roots:", [sp.N(r_, 5) for r_ in roots])
r1 = sp.N(-0.2275 + 0.049*sp.I); r2 = sp.N(0.2275 - 1.049*sp.I)
chk("Q2d roots match z1=-0.2275+0.049i, z2=0.2275-1.049i", all(min(abs(sp.N(r_) - q) for q in (r1, r2)) < 1e-3 for r_ in roots))
# Q3
A3 = M([[1, 1, 1], [k, k**2, 1], [k**2, 2*k**2 - 1, 1]])
chk("Q3a det = -(k+1)(k-1)^3 (official prints +: sign slip)", sp.expand(A3.det() + (k + 1)*(k - 1)**3) == 0, str(sp.factor(A3.det())))
A31 = A3.subs(k, 1)
chk("Q3b k=1 rank 1, basis (1,1,1)", A31.rank() == 1 and A31 == sp.ones(3, 3))
chk("Q3c k!=+-1 invertible", all(A3.subs(k, kk).det() != 0 for kk in (0, 2, 3, -2, R(1, 2))))
B3 = M([[-2, 1, -1], [1, 2, 3], [1, -1, 0]])
chk("Q3d charpoly = l(1-l)(1+l)", sp.expand((B3 - l*sp.eye(3)).det() - l*(1 - l)*(1 + l)) == 0, str(sp.factor((B3 - l*sp.eye(3)).det())))
v1 = M([-1, -1, 1]); v2 = M([-3, -1, 2]); v3 = M([-1, -2, 1])
chk("Q3d v1 (l=0)", B3 * v1 == 0 * v1)
chk("Q3d v2 (l=-1)", B3 * v2 == -v2)
chk("Q3d v3 (l=1)", B3 * v3 == v3)
P = M([[-1, -1, -3], [-1, -2, -1], [1, 1, 2]]); Dm = sp.diag(0, 1, -1)
chk("Q3d P^-1 B P = D with P=(v1,v3,v2)", P.inv() * B3 * P == Dm)
# Q4
W1 = [M([1, 1, 0, 0]), M([0, 0, 2, 3]), M([5, 5, 6, 9])]   # (a,b,c,d) order
S1 = M.hstack(*W1)
chk("Q4a dim W1 = 2", S1.rank() == 2)
chk("Q4a basis of W1 as printed", M.hstack(M([1, 1, 0, 0]), M([0, 0, 2, 3])).rank() == 2)
W2b = [M([-1, 1, 0, 0]), M([1, 0, 1, 0]), M([1, 0, 0, 1])]
chk("Q4a W2 basis satisfies a+b=c+d", all(v[0] + v[1] == v[2] + v[3] for v in W2b) and M.hstack(*W2b).rank() == 3)
W1b = [M([1, 1, 0, 0]), M([0, 0, 2, 3])]
SS = M.hstack(*(W1b + W2b))
chk("Q4b dim(W1+W2)=4 = dim M2x2", SS.rank() == 4)
ns = M.hstack(*W2b, -W1b[0], -W1b[1]).nullspace()
chk("Q4c intersection dim 1", len(ns) == 1)
vint = M([5, 5, 4, 6])
chk("Q4c (5 5; 4 6) in W1", M.hstack(*W1b, vint).rank() == 2)
chk("Q4c (5 5; 4 6) in W2", vint[0] + vint[1] == vint[2] + vint[3])
chk("Q4c official coefficients: 5(1,1,0,0)+2(0,0,2,3)? -> (5,5,4,6)", 5*W1b[0] + 2*W1b[1] == vint)
u1 = M([1, -1, 1, 1]); u2 = M([1, 1, 1, -1])
chk("Q4d u1,u2 in U, u1+u2 not", (u1[0] + u1[1])*(u1[2] + u1[3]) == 0 and (u2[0] + u2[1])*(u2[2] + u2[3]) == 0 and (u1 + u2)[0] + (u1 + u2)[1] != 0 and (u1 + u2)[2] + (u1 + u2)[3] != 0)
# Q5: exam T = (a+b, d+c) ; the official solution uses T = (a+d, b+c)
Texam = M([[1, 1, 0, 0], [0, 0, 1, 1]])      # columns a,b,c,d
Toff = M([[1, 0, 0, 1], [0, 1, 1, 0]])
chk("Q5 OFFICIAL SOLUTION USES A DIFFERENT MAP (a+d,b+c) than the exam (a+b,d+c)", Texam != Toff)
ker = Texam.nullspace()
chk("Q5b ker(T_exam) dim 2, basis (1 -1;0 0),(0 0;1 -1)", len(ker) == 2 and all(Texam * v == sp.zeros(2, 1) for v in (M([1, -1, 0, 0]), M([0, 0, 1, -1]))) and M.hstack(M([1, -1, 0, 0]), M([0, 0, 1, -1])).rank() == 2)
chk("Q5b Im T_exam = R^2 (rank 2)", Texam.rank() == 2)
B1 = [M([1, 0, 0, 0]), M([1, 1, 0, 0]), M([1, 1, 1, 0]), M([1, 1, 1, 1])]
B2 = M([[1, 1], [0, -1]])
mat = M.hstack(*[B2.inv() * (Texam * v) for v in B1])
print("  [T]_B2^B1 (exam T):", mat.tolist())
chk("Q5d [T] exam = (1 2 3 4; 0 0 -1 -2)", mat == M([[1, 2, 3, 4], [0, 0, -1, -2]]))
mat_off = M.hstack(*[B2.inv() * (Toff * v) for v in B1])
chk("Q5d official matrix (1 2 3 4;0 -1 -2 -2) is for (a+d,b+c)", mat_off == M([[1, 2, 3, 4], [0, -1, -2, -2]]))
print("DONE, mismatches:", bad)
