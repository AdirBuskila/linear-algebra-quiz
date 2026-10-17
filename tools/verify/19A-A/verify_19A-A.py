# -*- coding: utf-8 -*-
"""sympy checks of the official 19A-A answers. Run: PYTHONUTF8=1 py tools/verify/19A-A/verify_19A-A.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix; R = sp.Rational
a, k, s, t = sp.symbols("a k s t")
# Q1
P1 = M([2, 1, 1]); P2 = M([1, 2, 2]); m1 = M([2, -a, -5]); m2 = M([a, -2, -1])
cr = m1.cross(m2)
chk("Q1a m1xm2", sp.simplify(cr - M([a - 10, 2 - 5 * a, a**2 - 4])) == sp.zeros(3, 1))
V = (P2 - P1).dot(cr)
chk("Q1a V=(a-2)(a-4)", sp.expand(V - (a - 2) * (a - 4)) == 0)
chk("Q1a lines never parallel (m1 x m2 = 0 has no solution)", sp.solve(list(cr), a) == [])
n = cr.subs(a, 2)
chk("Q1b normal (-8,-8,0)", n == M([-8, -8, 0]))
chk("Q1b D=24 and l2 point on plane", -8 * 2 - 8 * 1 + 24 == 0 and (-8) * 1 + (-8) * 2 + 24 == 0 and 24 > 0)
d0 = sp.Abs(V.subs(a, 0)) / cr.subs(a, 0).norm()
chk("Q1c d = 8/sqrt(120)", sp.simplify(d0 - 8 / sp.sqrt(120)) == 0, str(sp.nsimplify(d0)))
# Q2
Ab = M([[1, -1, 1, -2], [1, k, 1, k + 1], [k, k, 1, 2]])
E = Ab.copy()
E[1, :] = E[1, :] - E[0, :]; E[2, :] = E[2, :] - k * E[0, :]
chk("Q2a step1", sp.simplify(E - M([[1, -1, 1, -2], [0, k + 1, 0, k + 3], [0, 2 * k, 1 - k, 2 + 2 * k]])) == sp.zeros(3, 4))
E[1, :] = 2 * E[1, :] - E[2, :]
chk("Q2a step2", sp.simplify(E[1, :] - M([[0, 2, k - 1, 4]])) == sp.zeros(1, 4))
E[2, :] = E[2, :] - k * E[1, :]
chk("Q2a final row3", sp.simplify(E[2, :] - M([[0, 0, 1 - k**2, 2 - 2 * k]])) == sp.zeros(1, 4))
A2 = Ab[:, :3]; b2 = Ab[:, 3]
def cls(kv):
    Mm = A2.subs(k, kv); r = b2.subs(k, kv)
    rk = Mm.rank(); rka = Mm.row_join(r).rank()
    return "none" if rk != rka else ("unique" if rk == 3 else "inf")
chk("Q2b classification", cls(1) == "inf" and cls(-1) == "none" and all(cls(v) == "unique" for v in (0, 2, 3, -2, 5)))
sol1 = sp.linsolve((A2.subs(k, 1), b2.subs(k, 1)))
chk("Q2c k=1 solution (-t,2,t)", sol1 == sp.FiniteSet((-t, 2, t)) or sp.simplify(list(sol1)[0][0] + list(sol1)[0][2]) == 0 and list(sol1)[0][1] == 2, str(sol1))
sol_i = A2.subs(k, sp.I).LUsolve(b2.subs(k, sp.I))
chk("Q2d k=i solution (-1,2-i,1-i)", sp.simplify(sol_i - M([-1, 2 - sp.I, 1 - sp.I])) == sp.zeros(3, 1))
# Q3
B = M([[0, 1, 7, 8], [1, 3, 3, 8], [-2, -5, 1, -8]])
Rr = M([[1, 3, 3, 8], [0, 1, 7, 8], [0, 0, 0, 0]])
Gm = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); Fm = M([[1, 0, 0], [0, 1, 0], [2, 0, 1]]); Em = M([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
chk("Q3a official E F G R != B as printed (official final-answer slip, confirmed)", Em * Fm * Gm * Rr != B)
chk("Q3a official E F G B equals R (the reduction)", Em * Fm * Gm * B == Rr)
Eok = Gm; Fok = M([[1, 0, 0], [0, 1, 0], [-2, 0, 1]]); Gok = M([[1, 0, 0], [0, 1, 0], [0, 1, 1]])
chk("Q3a corrected E=swap, F=R3-2R1 inverse, G=R3+R2 gives B=EFGR", Eok * Fok * Gok * Rr == B)
chk("Q3a E,F,G,R are elementary / rref-like", all(x.det() != 0 for x in (Eok, Fok, Gok)))
# Q4
Wb = [M([[1, 0], [0, 1]]), M([[0, 1], [1, 1]])]
def v4(Mx): return list(Mx)
chk("Q4 W basis lies in W (b=c, a+b-d=0)", all(m[0, 1] == m[1, 0] and m[0, 0] + m[0, 1] - m[1, 1] == 0 for m in Wb))
off = M([[0, 1], [1, 0]])
chk("Q4b official basis element (0 1;1 0) is NOT in W", not (off[0, 1] == off[1, 0] and off[0, 0] + off[0, 1] - off[1, 1] == 0), "(expected: not in W, a+b-d=1+0... -> 0+1-0=1)")
Us = [M([[1, 0], [1, 1]]), M([[0, 1], [-1, -2]]), M([[0, 0], [0, 1]])]
UW = sp.Matrix([list(x) for x in Us + Wb])
chk("Q4g rank(U)=3, rank(W)=2, dim(U+W)=4", sp.Matrix([list(x) for x in Us]).rank() == 3 and sp.Matrix([list(x) for x in Wb]).rank() == 2 and UW.rank() == 4)
chk("Q4g B2 = U1,U2,U3,I is a basis", sp.Matrix([list(x) for x in Us + [Wb[0]]]).rank() == 4)
official_rowsW = sp.Matrix([list(x) for x in Us + [Wb[0], off]])
chk("Q4g with the printed (0 1;1 0) the rank is also 4 (conclusion unchanged)", official_rowsW.rank() == 4)
c1, c2, c3, d1, d2 = sp.symbols("c1 c2 c3 d1 d2")
sol = sp.solve(list(c1 * Us[0] + c2 * Us[1] + c3 * Us[2] - d1 * Wb[0] - d2 * Wb[1]), [c1, c2, c3, d1], dict=True)[0]
vv = sol[d1] * Wb[0] + d2 * Wb[1]
chk("Q4d intersection = d2*(2 1;1 3)", sp.simplify(vv - d2 * M([[2, 1], [1, 3]])) == sp.zeros(2, 2), str(vv.subs(d2, 1).tolist()))
chk("Q4d (2 1;1 3) in W and in U", M([[2, 1], [1, 3]])[0, 1] == M([[2, 1], [1, 3]])[1, 0] and 2 + 1 - 3 == 0 and sp.Matrix([list(x) for x in Us + [M([[2, 1], [1, 3]])]]).rank() == 3)
# Q5
A5 = M([[1, 2 * a - 1, 2], [1, 3, a], [1, 3 * a - 1, 5]])
chk("Q5a det = -(a^2+4a-12)", sp.expand(A5.det() + (a**2 + 4 * a - 12)) == 0)
chk("Q5a singular exactly at a=2,-6", set(sp.solve(A5.det(), a)) == {2, -6})
A1 = A5.subs(a, 1)
chk("Q5a A1 = [1 1 2;1 3 1;1 2 5], det 7", A1 == M([[1, 1, 2], [1, 3, 1], [1, 2, 5]]) and A1.det() == 7)
chk("Q5a inverse", A1.inv() == R(1, 7) * M([[13, -1, -5], [-4, 3, 1], [-1, -1, 2]]))
B2 = M([[-1, 0], [0, 1]])
chk("Q5b B^2=I, B != +-I", B2 * B2 == sp.eye(2) and B2 != sp.eye(2) and B2 != -sp.eye(2))
chk("Q5b det = -30375", 3**5 * (-5) * (-5) * 2 * R(1, 2) * (-5) == -30375)
Bq = sp.MatrixSymbol('Bq', 5, 5)
Bn = sp.diag(-5, 1, 1, 1, 1); Cn = sp.diag(2, 1, 1, 1, 1)
chk("Q5b det(3B^2 C^T C^-1 B^T) numeric model", (3 * Bn**2 * Cn.T * Cn.inv() * Bn.T).det() == -30375)
# Q6
x = sp.symbols("x"); aa, bb, cc, dd = sp.symbols("aa bb cc dd")
def T(p):
    p = sp.Poly(p, x); co = [p.coeff_monomial(x**i) for i in range(4)]
    a_, b_, c_, d_ = co
    return sp.expand((a_ - 2 * c_ + d_) + (b_ + 2 * c_ - a_ - d_) * x**2 + b_ * x**3)
p1 = aa + bb * x + cc * x**2 + dd * x**3; p2 = 3 + 5 * x - x**2 + 2 * x**3
chk("Q6a linear", sp.expand(T(p1 + p2) - T(p1) - T(p2)) == 0 and sp.expand(T(7 * p1) - 7 * T(p1)) == 0)
chk("Q6b ker basis 2+x^2, -1+x^3", T(2 + x**2) == 0 and T(-1 + x**3) == 0)
Tm = M([[1, 0, -2, 1], [0, 0, 0, 0], [-1, 1, 2, -1], [0, 1, 0, 0]])
chk("Q6b dim ker = 2, Im = sp{1-x^2, x^2+x^3}, rank 2", len(Tm.nullspace()) == 2 and Tm.rank() == 2 and sp.Matrix([[1, 0, -1, 0], [0, 0, 1, 1]]).row_join(sp.zeros(2, 0)).rank() == 2)
chk("Q6c image basis in coordinates", all(sp.Matrix(Tm.columnspace()[i:i + 1][0]).shape == (4, 1) for i in range(2)) and sp.Matrix.hstack(*Tm.columnspace(), M([1, 0, -1, 0]), M([0, 0, 1, 1])).rank() == 2)
chk("Q6d T not injective (dim ker 2 > 0)", len(Tm.nullspace()) == 2)
print("MISMATCHES:", bad)
