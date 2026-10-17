# -*- coding: utf-8 -*-
"""sympy checks of the official 23B-B answers. Run: PYTHONUTF8=1 py tools/verify/23B-B/verify_23B-B.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
# Q1b: AXB=A+B  => X = B^-1 + A^-1 (random invertible)
A = M([[2, 1], [1, 1]]); B = M([[1, 3], [0, 2]])
X = B.inv() + A.inv()
chk("Q1b X=B^-1+A^-1", A * X * B == A + B)
# Q1g: A^3-5A-4I=0 => A^-1=(A^2-5I)/4, symbolic via polynomial identity
x = sp.symbols("x")
chk("Q1g x*(x^2-5)/4 = 1 mod x^3-5x-4", sp.rem(sp.expand(x * (x**2 - 5) / 4 - 1), x**3 - 5 * x - 4, x) == 0)
# Q2
a = sp.symbols("a")
Ma = M([[a, 1, 1], [1, 1, 2], [1, -1, a]]); rhs = M([2, 5, a + 1])
print("  det:", sp.factor(Ma.det()))
chk("Q2 det = a(a+1)", sp.expand(Ma.det() - a * (a + 1)) == 0)
sol = Ma.LUsolve(rhs)
sol = [sp.simplify(s) for s in sol]
print("  sol:", sol)
chk("Q2a x=-2/(a+1)", sp.simplify(sol[0] + 2 / (a + 1)) == 0)
chk("Q2a y=3(a-1)/(a+1)", sp.simplify(sol[1] - 3 * (a - 1) / (a + 1)) == 0)
chk("Q2a z=(a+5)/(a+1)", sp.simplify(sol[2] - (a + 5) / (a + 1)) == 0)
Mm1 = Ma.subs(a, -1)
chk("Q2b a=-1 inconsistent", Mm1.rank() != Mm1.row_join(rhs.subs(a, -1)).rank())
M0 = Ma.subs(a, 0); r0 = rhs.subs(a, 0)
chk("Q2c a=0 rank 2 consistent", M0.rank() == 2 and M0.row_join(r0).rank() == 2)
p0 = M([3, 2, 0]); d0 = M([-1, -1, 1])
z = sp.symbols("z")
chk("Q2c a=0 param solution", sp.simplify(M0 * (p0 + z * d0) - r0) == sp.zeros(3, 1))
zz = sp.symbols("zz")
roots = sp.solve(zz**2 - (2 + sp.I) * zz + (-1 + 7 * sp.I), zz)
chk("Q2d roots 3-i, -1+2i", set(map(sp.simplify, roots)) == {3 - sp.I, -1 + 2 * sp.I})
# Q3.1
A3 = M([[1, 6, 0], [0, 1, 2], [5, 30, 3]])
Ai = M([[-19, -6, 4], [sp.Rational(10, 3), 1, -sp.Rational(2, 3)], [-sp.Rational(5, 3), 0, sp.Rational(1, 3)]])
chk("Q3.1a inverse", A3.inv() == Ai)
E1 = M([[1, -6, 0], [0, 1, 0], [0, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, -2], [0, 0, 1]])
E3 = M([[1, 0, 0], [0, 1, 0], [0, 0, sp.Rational(1, 3)]]); E4 = M([[1, 0, 0], [0, 1, 0], [-5, 0, 1]])
chk("Q3.1b E1E2E3E4 = A^-1", E1 * E2 * E3 * E4 == Ai)
# Q3.2
B3 = M([[1, 2, 1], [-3, 6, 1], [0, 0, 4]])
lam = sp.symbols("lam")
chk("Q3.2 charpoly (l-3)(l-4)^2", sp.expand(B3.charpoly(lam).as_expr() - (lam - 3) * (lam - 4)**2) == 0)
P = M([[1, 2, 1], [1, 3, 0], [0, 0, 3]]); D = sp.diag(3, 4, 4)
chk("Q3.2 PD=BP", P * D == B3 * P and P.det() != 0)
chk("Q3.2 PD matrix", P * D == M([[3, 8, 4], [3, 12, 0], [0, 0, 12]]))
chk("Q3.2 diagonalizable", B3.is_diagonalizable())
# Q4
p = sp.symbols("p0:4")  # a b c d  -> ax^3+bx^2+cx+d
xs = sp.symbols("xs")
pol = lambda v: v[0] * xs**3 + v[1] * xs**2 + v[2] * xs + v[3]
cond1 = [sp.diff(pol(p), xs).subs(xs, 1), pol(p).subs(xs, -1)]
C1 = sp.Matrix([[sp.diff(c, v) for v in p] for c in cond1])
chk("Q4 W1 conditions matrix", C1 == M([[3, 2, 1, 0], [-1, 1, -1, 1]]))
ns1 = C1.nullspace(); chk("Q4a dim W1=2", len(ns1) == 2)
b1 = [M([-3, 2, 5, 0]), M([2, -3, 0, 5])]
chk("Q4a W1 basis vectors in W1, independent", all(C1 * v == sp.zeros(2, 1) for v in b1) and M.hstack(*b1).rank() == 2)
C2 = M([[1, -1, -1, 1]]); b2 = [M([1, 1, 0, 0]), M([1, 0, 1, 0]), M([-1, 0, 0, 1])]
chk("Q4a W2 basis in W2, dim 3", all(C2 * v == sp.zeros(1, 1) for v in b2) and M.hstack(*b2).rank() == 3)
chk("Q4b dim(W1+W2)=4", M.hstack(*b1, *b2).rank() == 4)
inter = C1.col_join(C2).nullspace()
chk("Q4c dim intersection 1", len(inter) == 1)
v = inter[0]; v = v / v[3] * 5
print("  intersection vector:", list(v))
chk("Q4c basis (-1,-1,5,5)", list(v) == [-1, -1, 5, 5])
chk("Q4d 2x^3+2x^2-10x-10 = -2*basis", M([2, 2, -10, -10]) == -2 * M([-1, -1, 5, 5]))
# Q5
T = M([[1, 1, 11], [1, 2, 12], [1, 1, 11], [1, 1, 11]])
chk("Q5a rank 2", T.rank() == 2)
chk("Q5a kernel (-10,-1,1)", T * M([-10, -1, 1]) == sp.zeros(4, 1) and len(T.nullspace()) == 1)
chk("Q5a image basis cols 1,2 independent", M.hstack(T[:, 0], T[:, 1]).rank() == 2)
k, m = sp.symbols("k m")
chk("Q5g m=20230, k=-2023", sp.expand(k * (-10 - xs + xs**2) - (m + 2023 * xs - 2023 * xs**2)).subs({k: -2023, m: 20230}) == 0)
Tk = T.row_join(M([101, 102, 101, k]))
chk("Q5d k=101", Tk.subs(k, 101).rank() == 2 and Tk.subs(k, 100).rank() == 3)
Bb = M([[1, 1], [10, 11]]); Cc = M([[1, 5], [4, 19]])
chk("Q5.2 [I]_C^B", Cc.inv() * Bb == M([[31, 36], [-6, -7]]))
print("MISMATCHES:", bad if bad else "none")
# extra: Q4 displayed reductions
chk("Q4a rref of W1 system", M([[3, 2, 1, 0], [-1, 1, -1, 1]]).rref()[0] == M([[1, 0, sp.Rational(3, 5), -sp.Rational(2, 5)], [0, 1, -sp.Rational(2, 5), sp.Rational(3, 5)]]))
chk("Q4b rref of basis matrix", M([[1, 1, -1, -3, 2], [1, 0, 0, 2, -3], [0, 1, 0, 5, 0], [0, 0, 1, 0, 5]]).rref()[0] == M([[1, 0, 0, 0, -1], [0, 1, 0, 0, 5], [0, 0, 1, 0, 5], [0, 0, 0, 1, -1]]))
print("MISMATCHES:", bad if bad else "none")
