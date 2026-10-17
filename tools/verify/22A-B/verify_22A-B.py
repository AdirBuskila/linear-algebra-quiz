# -*- coding: utf-8 -*-
"""sympy checks of the official 22A-B answers. Run: PYTHONUTF8=1 py tools/verify/22A-B/verify_22A-B.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
R = sp.Rational
a, b, z, k, l = sp.symbols("a b z k l")
# Q1a: det(C)=det(D) for D = (PQ)^-1 C PQ (random instance)
P = M([[1, 2], [3, 7]]); Q_ = M([[2, 1], [5, 3]]); C = M([[4, 1], [2, 3]])
chk("Q1a det C = det D", ((P * Q_).inv() * C * (P * Q_)).det() == C.det())
# Q1b-d: 2AB+3I=0, |A|=2, order 4. B = -3/2 A^-1  (so A invertible, B invertible)
A4 = sp.diag(2, 1, 1, 1); B4 = -R(3, 2) * A4.inv()
chk("Q1 model 2AB+3I=0", 2 * A4 * B4 + 3 * sp.eye(4) == sp.zeros(4) and A4.det() == 2)
chk("Q1c det B = 81/32", B4.det() == R(81, 32))
chk("Q1d det B^-1 = 32/81", B4.inv().det() == R(32, 81))
chk("Q1b (-3)^4 = 81 = 2^4*2*det B", 2**4 * 2 * R(81, 32) == 81)
# Q2
Ma = M([[1, 2, 2], [1, a, 3], [1, 11, a]]); rhs = M([1, 3, b])
chk("Q2 det = -(a-2)... zero at a=5,-1 or a=2? det", set(sp.solve(Ma.det(), a)) == {5, -1}, str(sp.factor(Ma.det())))
def classify(av, bv):
    Mm = Ma.subs(a, av); r = rhs.subs(b, bv)
    rk = Mm.rank(); rka = Mm.row_join(r).rank()
    return "none" if rk != rka else ("unique" if rk == 3 else "inf")
chk("Q2a unique for a=2 (any b), a=0, a=7", all(classify(av, bv) == "unique" for av in (2, 0, 7, 3) for bv in (1, 7, -5)))
chk("Q2a a=5: b=7 inf, b!=7 none", classify(5, 7) == "inf" and all(classify(5, bv) == "none" for bv in (0, 1, 8)))
chk("Q2a a=-1: b=-5 inf, b!=-5 none", classify(-1, -5) == "inf" and all(classify(-1, bv) == "none" for bv in (0, 1, 7)))
sol2 = Ma.subs(a, 2).LUsolve(rhs.subs(b, 1))
chk("Q2b a=2,b=1 -> (-3,0,2)", sol2 == M([-3, 0, 2]))
bb = sp.symbols("bb")
sol2g = Ma.subs(a, 2).LUsolve(rhs.subs(b, bb))
chk("Q2a a=2 general (-3-2(b-1)/9, (b-1)/9, 2)", sp.simplify(sol2g - M([-3 - 2 * (bb - 1) / 9, (bb - 1) / 9, 2])) == sp.zeros(3, 1))
t = sp.symbols("t")
M57 = Ma.subs(a, 5); r57 = rhs.subs(b, 7)
chk("Q2c a=5,b=7 family", sp.simplify(M57 * M([-R(1, 3) - R(4, 3) * t, R(2, 3) - t / 3, t]) - r57) == sp.zeros(3, 1))
chk("Q2 (a-2)(b-1)-18: a=5 -> b=7; a=-1 -> b=-5", sp.solve(3 * (b - 1) - 18, b) == [7] and sp.solve(-3 * (b - 1) - 18, b) == [-5])
Az = M([[1, 2, -2], [0, z, 1], [1, 0, z]])
chk("Q2d det = z^2+2z+2", sp.expand(Az.det() - (z**2 + 2 * z + 2)) == 0)
chk("Q2d roots -1+-i", set(sp.solve(z**2 + 2 * z + 2, z)) == {-1 + sp.I, -1 - sp.I})
# Q3
A3 = M([[1, 2, 3], [4, 5, 6], [7, 8, a]])
chk("Q3a det = -3a+27", sp.expand(A3.det() - (-3 * a + 27)) == 0)
CF = A3.cofactor_matrix()
chk("Q3a cofactor matrix as printed", sp.simplify(CF - M([[5 * a - 48, -4 * a + 42, -3], [-2 * a + 24, a - 21, 6], [-3, 6, -3]])) == sp.zeros(3))
chk("Q3a A^-1 = adj/det", sp.simplify(A3.inv() - CF.T / (-3 * a + 27)) == sp.zeros(3))
A9 = A3.subs(a, 9)
chk("Q3b a=9 rank 2", A9.rank() == 2)
bas = M([[1, 2, 3], [0, 1, 2], [0, 0, 1]])
chk("Q3b completed basis is a basis and first two rows lie in row space of A", bas.rank() == 3 and M.vstack(A9, bas[:2, :]).rank() == 2)
Cm = M([[0, 1], [1, 0]]); Dm = M([[1, 0], [0, -1]])
chk("Q3.2 model: C,D symmetric, CD=-DC => CD antisymmetric", Cm == Cm.T and Dm == Dm.T and Cm * Dm == -Dm * Cm and (Cm * Dm).T == -(Cm * Dm))
# Q5
T5 = M([[1, 1, -1, 3], [1, 2, 0, 4], [1, 3, 1, 5]])
chk("Q5a rank 2, pivots 1,2", T5.rank() == 2 and T5.rref()[1] == (0, 1))
chk("Q5a kernel (2,-1,1,0),(-2,-1,0,1)", T5 * M([2, -1, 1, 0]) == sp.zeros(3, 1) and T5 * M([-2, -1, 0, 1]) == sp.zeros(3, 1) and len(T5.nullspace()) == 2)
chk("Q5c k=4 only", [kk for kk in range(-20, 21) if M.hstack(T5[:, 0], T5[:, 1]).row_join(M([kk, 7, 10])).rank() == 2] == [4])
Fm = M([[1, 1], [1, -1]]); Bm = M([[5, 2], [17, 7]])
chk("Q5d [F]_B^B = [[178,73],[-434,-178]]", Bm.inv() * Fm * Bm == M([[178, 73], [-434, -178]]) and Bm.det() == 1)
# ---- Q4 (no official solution; solved by the solver). R3[x], coords (a0,a1,a2,a3) ----
x4 = sp.symbols("x4")
def co4(p):
    p = sp.Poly(sp.expand(p) + 0 * x4, x4)
    return M([[p.coeff_monomial(x4**k) for k in range(4)]])
a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3")
pg = a0 + a1 * x4 + a2 * x4**2 + a3 * x4**3
oddc = sp.Poly(sp.expand(pg.subs(x4, -x4) + pg), x4).coeffs()
chk("Q4a U: p(-x)=-p(x) iff a0=a2=0", sp.solve(oddc, [a0, a1, a2, a3], dict=True) == [{a0: 0, a2: 0}])
chk("Q4a U basis x, x^3 (dim 2)", all(sp.expand(p.subs(x4, -x4) + p) == 0 for p in (x4, x4**3)) and M.vstack(co4(x4), co4(x4**3)).rank() == 2)
Wb4 = [1 + 0 * x4, x4**2 - 2 * x4, x4**3 - 3 * x4]
chk("Q4b W basis 1, x^2-2x, x^3-3x satisfy p'(1)=0, dim 3", all(sp.diff(p, x4).subs(x4, 1) == 0 for p in Wb4) and M.vstack(*[co4(p) for p in Wb4]).rank() == 3
    and M([[0, 1, 2, 3]]).rank() == 1)
chk("Q4c U+W = R3[x]", M.vstack(co4(x4), co4(x4**3), *[co4(p) for p in Wb4]).rank() == 4)
chk("Q4d U cap W = span(x^3-3x)", sp.solve(sp.diff(a1 * x4 + a3 * x4**3, x4).subs(x4, 1), a1) == [-3 * a3] and 2 + 3 - 4 == 1)
q4 = -R(1, 2) * x4**3 + R(3, 2) * x4
chk("Q4e q(1)=1, q'(1)=0, q'(sqrt2)=-3/2", q4.subs(x4, 1) == 1 and sp.diff(q4, x4).subs(x4, 1) == 0 and sp.simplify(sp.diff(q4, x4).subs(x4, sp.sqrt(2)) + R(3, 2)) == 0)
print("ALL OK" if not bad else "MISMATCHES: " + ", ".join(bad))
assert not bad, bad
