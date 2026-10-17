# -*- coding: utf-8 -*-
"""sympy checks of the official 23A-B answers. Run: PYTHONUTF8=1 py tools/verify/23A-B/verify_23A-B.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
R = sp.Rational
# Q1a: A^3-A+I=0 => A^-1 = I-A^2 (polynomial identity mod x^3-x+1)
x = sp.symbols("x")
chk("Q1a x*(1-x^2) = 1 mod x^3-x+1", sp.rem(sp.expand(x * (1 - x**2) - 1), x**3 - x + 1, x) == 0)
# Q1d: charpoly of F and F^T agree
a, b, c, d, l = sp.symbols("a b c d l")
F = M([[a, b], [c, d]])
chk("Q1d charpoly F = charpoly F^T", sp.expand(F.charpoly(l).as_expr() - F.T.charpoly(l).as_expr()) == 0)
# Q2
Ma = M([[a, 2 * a, 3 * a], [a, 2 * a + 1, 3 * a + 1], [a, 2 * a - 1, 0]]); rhs = M([4 * a, 4 * a + 1, 2 - a])
Aug = Ma.row_join(rhs)
step1 = Aug.copy(); step1[1, :] = Aug[1, :] - Aug[0, :]; step1[2, :] = Aug[2, :] - Aug[0, :]
chk("Q2a step1 rows", step1[1, :].applyfunc(sp.expand) == M([[0, 1, 1, 1]]) and step1[2, :].applyfunc(sp.expand) == M([[0, -1, -3 * a, 2 - 5 * a]]))
step2 = step1.copy(); step2[2, :] = (step1[2, :] + step1[1, :]).applyfunc(sp.expand)
chk("Q2a step2 row3 = (0,0,1-3a,3-5a)", step2[2, :] == M([[0, 0, 1 - 3 * a, 3 - 5 * a]]))
chk("Q2b det = a(1-3a)*a-ish: zero only at a=0,1/3", set(sp.solve(Ma.det(), a)) == {0, R(1, 3)}, str(sp.factor(Ma.det())))
M13 = Ma.subs(a, R(1, 3)); r13 = rhs.subs(a, R(1, 3))
chk("Q2b a=1/3 inconsistent", M13.rank() != M13.row_join(r13).rank())
chk("Q2b a=1/3 contradiction value 4/3", step2.subs(a, R(1, 3))[2, 3] == R(4, 3))
M0 = Ma.subs(a, 0); r0 = rhs.subs(a, 0)
chk("Q2b a=0 rank 2 consistent", M0.rank() == 2 and M0.row_join(r0).rank() == 2)
t = sp.symbols("t")
chk("Q2c a=0 solution (t,-2,3)", sp.simplify(M0 * M([t, -2, 3]) - r0) == sp.zeros(3, 1))
chk("Q2b unique for a=2", Ma.subs(a, 2).rank() == 3)
# Q2d roots
z = sp.symbols("z")
roots = sp.Poly(z**4 + (2 + sp.I) * z, z).nroots(n=15)
def polar(r):
    ang = float(sp.arg(r)) * 180 / 3.141592653589793
    return round(float(abs(r)), 5), round(ang % 360, 2)
got = sorted(polar(r) for r in roots)
r6 = round(float(5 ** (1 / 6)), 5)
print("  roots polar:", got)
chk("Q2d z1=0", any(abs(r) < 1e-9 for r in roots))
chk("Q2d angles 68.86, 188.86, 308.86 (not 300.86)", sorted(p[1] for p in got if p[0] > 0.1) == [68.86, 188.86, 308.86])
chk("Q2d modulus 5^(1/6)", all(abs(p[0] - r6) < 1e-4 for p in got if p[0] > 0.1))
chk("Q2d printed 300.86 is NOT a root", abs(complex(5 ** (1 / 6)) * complex(__import__('math').cos(__import__('math').radians(300.86)), __import__('math').sin(__import__('math').radians(300.86))) ** 4 + (2 + 1j) * complex(5 ** (1 / 6)) * complex(__import__('math').cos(__import__('math').radians(300.86)), __import__('math').sin(__import__('math').radians(300.86)))) > 0.01)
# Q3.1
A3 = M([[1, -2, -2], [0, -1, 0], [-1, 2, 3]])
Ai = M([[3, -2, 2], [0, -1, 0], [1, 0, 1]])
chk("Q3.1a inverse", A3.inv() == Ai)
E1 = M([[1, 2, 0], [0, 1, 0], [0, 0, 1]]); E2 = M([[1, 0, 2], [0, 1, 0], [0, 0, 1]])
E3 = M([[1, 0, 0], [0, -1, 0], [0, 0, 1]]); E4 = M([[1, 0, 0], [0, 1, 0], [1, 0, 1]])
chk("Q3.1b E1E2E3E4 = A^-1", E1 * E2 * E3 * E4 == Ai)
# Q3.2
B3 = M([[3, 1, 1], [1, 3, 1], [0, 0, 2]])
lam = sp.symbols("lam")
chk("Q3.2 charpoly (l-2)^2(l-4)", sp.expand(B3.charpoly(lam).as_expr() - (lam - 2)**2 * (lam - 4)) == 0)
P = M([[-1, -1, 1], [1, 0, 1], [0, 1, 0]]); D = sp.diag(2, 2, 4)
chk("Q3.2 BP=PD, P invertible", B3 * P == P * D and P.det() != 0)
# Q4
p = sp.symbols("p0:4")
px = p[0] * x**3 + p[1] * x**2 + p[2] * x + p[3]
cU = sp.expand(px.subs(x, 1) - sp.diff(px, x).subs(x, 1))
chk("Q4a U: d=2a+b", sp.solve(cU, p[3]) == [2 * p[0] + p[1]])
chk("Q4a U basis in U", all(sp.expand(q.subs(x, 1) - sp.diff(q, x).subs(x, 1)) == 0 for q in [x**3 + 2, x**2 + 1, x]))
cW = sp.expand(px - px.subs(x, -x))
chk("Q4b W: even, a=c=0", set(sp.solve(sp.Poly(cW, x).coeffs(), [p[0], p[2]], dict=True)[0].values()) == {0})
cs = lambda q: [sp.Poly(q, x).coeff_monomial(x**k) for k in (3, 2, 1, 0)]
Ub = M([cs(q) for q in [x**3 + 2, x**2 + 1, x]]); Wb = M([cs(q) for q in [x**2, sp.Integer(1)]])
chk("Q4a/b dims 3,2", Ub.rank() == 3 and Wb.rank() == 2)
chk("Q4c dim(U+W)=4", Ub.col_join(Wb).rank() == 4)
# U cap W: dimension and member x^2+1
chk("Q4d x^2+1 in U and W", sp.expand((x**2 + 1).subs(x, 1) - sp.diff(x**2 + 1, x).subs(x, 1)) == 0)
nul = M.vstack(Ub, -Wb).T.nullspace() if False else None
inter = M.hstack(Ub.T, -Wb.T).nullspace()
chk("Q4d dim(U cap W)=1", len(inter) == 1 and 4 == 3 + 2 - 1)
v = inter[0]
vec = (M.hstack(Ub.T) * v[:3, :]).T
chk("Q4d U cap W = span(x^2+1)", vec.rank() == 1 and M([[0, 1, 0, 1]]).col_join(vec).rank() == 1)
# Q5
A = M([[1, 1, 3, 1], [1, 1, 3, 1], [1, 2, 4, 1], [1, 3, 5, 5]])
chk("Q5a rank 3, pivots 1,2,4", A.rank() == 3 and A.rref()[1] == (0, 1, 3))
ker = A.nullspace()
chk("Q5a Ker basis (-2,-1,1,0)", len(ker) == 1 and ker[0] == M([-2, -1, 1, 0]))
chk("Q5c p=10 q=0", A * M([10, 5, -5, 0]) == sp.zeros(4, 1))
Bm = M([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]])  # columns = basis B vectors
Ic = M([[0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]])  # F coords (1,x,x2,x3) -> C coords (x3,1,x2,x)
TCB = Ic * A * Bm
chk("Q5d [T]_C^B method 1", TCB == M([[4, 8, 10, 5], [2, 4, 4, 1], [3, 6, 5, 1], [2, 4, 4, 1]]))
cols = [A * Bm[:, j] for j in range(4)]
print("  T(B_j) in F coords:", [list(c) for c in cols])
chk("Q5d method 2 intermediates",
    [list(Ic * c) for c in cols] == [[4, 2, 3, 2], [8, 4, 6, 4], [10, 4, 5, 4], [5, 1, 1, 1]])
print("ALL OK" if not bad else "MISMATCHES: " + ", ".join(bad))
