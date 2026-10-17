# -*- coding: utf-8 -*-
"""sympy checks of the official 22A-A answers. Run: PYTHONUTF8=1 py tools/verify/22A-A/verify_22A-A.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
R = sp.Rational
a, b, x, y, z, w, t, t1, t2, l = sp.symbols("a b x y z w t t1 t2 l")
# Q1c counterexample
C = M([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]); D = M([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
chk("Q1c C,D antisymmetric", C.T == -C and D.T == -D)
chk("Q1c CD as printed", C * D == M([[-3, -2, 1], [-3, -4, -1], [3, -2, -5]]))
chk("Q1c det CD = 0", (C * D).det() == 0)
# Q1a identity sanity on a commuting instance: det D = det(C)^2 when C D^2 = D^3 C^-1
Cn = M([[2, 0], [0, 3]]); Dn = M([[4, 0], [0, 9]])
chk("Q1a instance C D^2 = D^3 C^-1 => det D = det(C)^2", Cn * Dn**2 == Dn**3 * Cn.inv() and Dn.det() == Cn.det()**2)
# Q2
A = M([[1, 0, 0, 2, 4], [0, a**2 - a, a**2 - a, 0, a], [1, 0, a - 1, a + 1, a + 3], [2, a**2 - a, a**2 + a - 2, 2*a + 2, 3*a + b]])
# check against the printed system
X = M([x, y, z, w])
eqs = [x + 2*w - 4, (a**2 - a)*y + (a**2 - a)*z - a, x + (a - 1)*z + (a + 1)*w - (a + 3), 2*x + (a**2 - a)*y + (a**2 + a - 2)*z + (2*a + 2)*w - (3*a + b)]
Ac = M([[sp.diff(e, v) for v in (x, y, z, w)] for e in eqs])
chk("Q2a augmented matrix", Ac.row_join(M([-e.subs({x: 0, y: 0, z: 0, w: 0}) for e in eqs])) == A)
E = A.copy()
E[2, :] = E[2, :] - E[0, :]; E[3, :] = E[3, :] - 2*E[0, :]
E[3, :] = E[3, :] - E[1, :]
E[3, :] = E[3, :] - 2*E[2, :]
E = E.applyfunc(sp.expand)
print("  final row4:", list(E[3, :]), " row3:", list(E[2, :]))
chk("Q2a final echelon row 4 (0 0 0 0 | b-6)", list(E[3, :]) == [0, 0, 0, 0, b - 6])
chk("Q2a final row 3 (0 0 a-1 a-1 | a-1)", list(E[2, :]) == [0, 0, a - 1, a - 1, a - 1])
for aa in (0, 1, 2, 5):
    for bb in (6, 7):
        Ma = Ac.subs(a, aa); ra = Ma.rank(); rb = Ma.row_join(M([4, aa, aa + 3, 3*aa + bb])).rank()
        print("  a=%s b=%s rank %s/%s" % (aa, bb, ra, rb))
chk("Q2b b!=6 inconsistent for all a", all(Ac.subs(a, aa).rank() < Ac.subs(a, aa).row_join(M([4, aa, aa + 3, 3*aa + 7])).rank() for aa in (0, 1, 2, 5, -3, R(1, 2))))
chk("Q2b b=6, a!=1: consistent and rank<4 (infinitely many)", all(Ac.subs(a, aa).rank() == Ac.subs(a, aa).row_join(M([4, aa, aa + 3, 3*aa + 6])).rank() < 4 for aa in (0, 2, 5, -3, R(1, 2))))
chk("Q2b OFFICIAL SLIP: a=1,b=6 has NO solution (row 2 is 0=a=1)", Ac.subs(a, 1).rank() < Ac.subs(a, 1).row_join(M([4, 1, 4, 9])).rank())
chk("Q2b never a unique solution (rank<=3 for symbolic a)", all(Ac.subs(a, aa).rank() <= 3 for aa in range(-4, 6)) and sp.simplify(Ac.det()) == 0)
sol0 = sp.linsolve((Ac.subs(a, 0), M([4, 0, 3, 6])), x, y, z, w)
print("  a=0,b=6:", sol0)
chk("Q2c a=0 solution is (4-2t2,t1,1-t2,t2)", sol0 == sp.FiniteSet((4 - 2*w, y, 1 - w, w)), str(sol0))
chk("Q2c OFFICIAL SLIP: (4-t2,t1,1-t2,t2) fails x+2w=4", Ac.subs(a, 0) * M([4 - t2, t1, 1 - t2, t2]) != M([4, 0, 3, 6]))
sol2 = sp.linsolve((Ac.subs(a, 2), M([4, 2, 5, 12])), x, y, z, w)
print("  a=2,b=6:", sol2)
chk("Q2d a=2 solution is (4-2t, t, 1-t, t)", sol2 == sp.FiniteSet((4 - 2*w, 1 - z, 1 - w, w)) or sol2 == sp.FiniteSet((4 - 2*w, w, 1 - w, w)))
chk("Q2d official (4-t,t,1-t,t) is WRONG", Ac.subs(a, 2) * M([4 - t, t, 1 - t, t]) != M([4, 2, 5, 12]))
chk("Q2d corrected (4-2t,t,1-t,t)", Ac.subs(a, 2) * M([4 - 2*t, t, 1 - t, t]) == M([4, 2, 5, 12]))
# Q2e
zs = [sp.exp(2*sp.pi*sp.I*k/3) for k in range(3)]
chk("Q2e z0+z1+z2 = 0", sp.simplify(sp.expand_complex(sum(zs))) == 0)
# Q3
A3 = M([[1, 3, 0], [0, 3, 1], [1, 3, 1]])
Ai = A3.inv()
chk("Q3a A^-1", Ai == M([[0, -1, 1], [R(1, 3), R(1, 3), -R(1, 3)], [-1, 0, 1]]))
E1 = M([[1, 0, 0], [0, 1, 0], [-1, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, -1], [0, 0, 1]])
E3 = M([[1, -1, 0], [0, 1, 0], [0, 0, 1]]); E4 = M([[1, 0, 0], [0, R(1, 3), 0], [0, 0, 1]])
chk("Q3b E4E3E2E1 A = I", E4 * E3 * E2 * E1 * A3 == sp.eye(3))
chk("Q3b A^-1 = E4E3E2E1", E4 * E3 * E2 * E1 == Ai)
B = M([[1, 1, 0], [0, -2, 0], [-1, 0, 3]])
chk("Q3c charpoly (1-l)(-2-l)(3-l)", sp.expand(B.charpoly(l).as_expr() - sp.expand(-(1 - l)*(-2 - l)*(3 - l)*(-1)**0)) in (0,) or sp.expand((B - l*sp.eye(3)).det() - (1 - l)*(-2 - l)*(3 - l)) == 0)
P = M([[2, 5, 0], [0, -15, 0], [1, 1, 1]]); Dd = sp.diag(1, -2, 3)
chk("Q3c P^-1 B P = D", P.inv() * B * P == Dd)
# Q4
W1 = M([[1, 0, 1], [0, 1, 2]]).T; W2 = M([[1, 0, 2], [0, 1, 1]]).T
a1 = M([1, 2, -1]); b1 = M([2, 1, -1])
chk("Q4a bases in kernels", all((a1.T * W1[:, i])[0] == 0 for i in range(2)) and all((b1.T * W2[:, i])[0] == 0 for i in range(2)))
S = W1.row_join(W2)
chk("Q4b dim(W1+W2)=3", S.rank() == 3)
ns = S.nullspace()
chk("Q4c intersection dim 1", len(ns) == 1)
v = M([1, 1, 3])
chk("Q4c (1,1,3) in both", (a1.T * v)[0] == 0 and (b1.T * v)[0] == 0)
chk("Q4d (2,2,6) = 2(1,1,3) in W1 cap W2", (a1.T * M([2, 2, 6]))[0] == 0 and (b1.T * M([2, 2, 6]))[0] == 0)
# Q5
a_, b_, c_, d_ = sp.symbols("a_ b_ c_ d_")
Tm = M([[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]])
chk("Q5a1 rank 3, ker dim 1", Tm.rank() == 3 and len(Tm.nullspace()) == 1)
chk("Q5a1 kernel vector (0,0,-1,1)", Tm * M([0, 0, -1, 1]) == sp.zeros(3, 1))
chk("Q5a1 columns 1,2,3 pivot", Tm[:, :3].rank() == 3)
chk("Q5a3 k=0", sp.solve([k_ for k_ in [sp.Symbol('k') + 0 + 2 - 2, sp.Symbol('k') + 0 + 2*2 - 2*2, sp.Symbol('k') + 0 + 3*2 - 3*2]], sp.Symbol('k')) == {sp.Symbol('k'): 0})
Bm = M([[2, 3], [3, 5]])
Fm = M([[7, 5], [3, 2]]) * Bm.inv() if False else None
FB = M([[7, 5], [3, 2]])
F = FB * Bm.inv()
chk("Q5b [F]_E^E = (20 -11; 9 -5)", F == M([[20, -11], [9, -5]]))
chk("Q5b F(2,3)=(7,3), F(3,5)=(5,2)", F * M([2, 3]) == M([7, 3]) and F * M([3, 5]) == M([5, 2]))
print("DONE, mismatches:", bad)
