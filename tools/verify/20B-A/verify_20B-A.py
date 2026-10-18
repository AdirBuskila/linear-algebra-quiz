# -*- coding: utf-8 -*-
"""sympy checks of the official 20B-A answers. Run: PYTHONUTF8=1 py tools/verify/20B-A/verify_20B-A.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix; R = sp.Rational
a, k, t, s, u, v = sp.symbols("a k t s u v")
# Q1 a: l1 (x-1)/1=(y-2)/k=z/2 ; l2 x/2=(y-3)/1=(z+2)/1
M1 = M([1, 2, 0]); M2 = M([0, 3, -2]); a1 = M([1, k, 2]); a2 = M([2, 1, 1])
d12 = M2 - M1
chk("Q1a M1M2 = (-1,1,-2) (official prints (-1,3,-2))", d12 == M([-1, 1, -2]))
V = sp.Matrix.hstack(d12, a1, a2).det()
chk("Q1a coplanarity det = 3k+3, k=-1", sp.expand(V - (3 * k + 3)) == 0 and sp.solve(V, k) == [-1])
off = M([-1, 3, -2]); Vo = sp.Matrix.hstack(off, a1, a2).det()
chk("Q1a the official own vector (-1,3,-2) gives 3k+9, not its printed 3k+12 (a second slip; k=-4 is wrong either way)", sp.expand(Vo - (3 * k + 9)) == 0 and sp.solve(Vo, k) == [-3])
sol = sp.solve([M1[i] + u * a1[i].subs(k, -1) - M2[i] - v * a2[i] for i in range(3)], [u, v], dict=True)
chk("Q1a k=-1 the lines really meet", len(sol) == 1, str(sol))
sol4 = sp.solve([M1[i] + u * a1[i].subs(k, -4) - M2[i] - v * a2[i] for i in range(3)], [u, v], dict=True)
chk("Q1a k=-4 the lines do NOT meet (official value wrong)", len(sol4) == 0)
chk("Q1a never parallel", sp.solve([a1[0] * 2 - a2[0], a1[1] * 2 - a2[1] , a1[2] * 2 - a2[2]], k) == [])
# Q1 a2: k=2
a1k = a1.subs(k, 2); cr = a1k.cross(a2)
chk("Q1a2 a1 x a2 = (0,3,-3), norm 3 sqrt 2", cr == M([0, 3, -3]) and sp.simplify(cr.norm() - 3 * sp.sqrt(2)) == 0)
dist = sp.Abs(d12.dot(cr)) / cr.norm()
chk("Q1a2 d = 9/(3 sqrt 2) = 3 sqrt2 / 2", sp.simplify(dist - 3 * sp.sqrt(2) / 2) == 0 and d12.dot(cr) == 9, str(sp.nsimplify(dist)))
# brute check of the distance by minimisation
f = (M1 + u * a1k - M2 - v * a2).dot(M1 + u * a1k - M2 - v * a2)
crit = sp.solve([sp.diff(f, u), sp.diff(f, v)], [u, v], dict=True)[0]
chk("Q1a2 minimisation gives the same distance", sp.simplify(sp.sqrt(f.subs(crit)) - 3 * sp.sqrt(2) / 2) == 0)
chk("Q1a2 official value 3 sqrt2 and 18 are wrong", sp.simplify(dist - 3 * sp.sqrt(2)) != 0)
# Q1 b
A_, B_, C_ = M([1, 0, 0]), M([1, 1, 0]), M([0, 1, 0])
chk("Q1b counterexample", A_.cross(B_) == A_.cross(C_) and A_.cross(B_) != sp.zeros(3, 1) and B_ != C_)
# Q2
Ab = M([[1, -1, 1, 1], [k - 1, k + 1, k + 1, k + 1], [k, -2 - k, -k, 1]])
E = Ab.copy()
E[1, :] = E[1, :] - (k - 1) * E[0, :]; E[2, :] = E[2, :] - k * E[0, :]
chk("Q2a step 1 rows (0 2k 2|2), (0 -2 -2k|1-k) (so the op is R3-kR1)", sp.simplify(E - M([[1, -1, 1, 1], [0, 2 * k, 2, 2], [0, -2, -2 * k, 1 - k]])) == sp.zeros(3, 4))
E2 = M([[1, -1, 1, 1], [0, 2, 2 * k, k - 1], [0, 2 * k, 2, 2]])
chk("Q2a after R2<->-R3", sp.simplify(E2[1, :] + E[2, :]) == sp.zeros(1, 4) and E2[2, :] == E[1, :])
E3 = E2.copy(); E3[2, :] = E3[2, :] - k * E3[1, :]
chk("Q2a final row (0 0 2-2k^2 | 2+k-k^2)", sp.simplify(E3[2, :] - M([[0, 0, 2 - 2 * k**2, 2 + k - k**2]])) == sp.zeros(1, 4))
A2 = Ab[:, :3]; b2 = Ab[:, 3]
def cls(kv):
    Mm = A2.subs(k, kv); r = b2.subs(k, kv)
    rk = Mm.rank(); rka = Mm.row_join(r).rank()
    return "none" if rk != rka else ("unique" if rk == 3 else "inf")
chk("Q2b k=1 none, k=-1 inf, others unique", cls(1) == "none" and cls(-1) == "inf" and all(cls(x) == "unique" for x in (0, 2, 3, -3, R(1, 2))))
ls = sp.linsolve((A2.subs(k, -1), b2.subs(k, -1)))
print("   k=-1 solution set:", ls)
chk("Q2c k=-1 true solution (0, t-1, t)", ls == sp.FiniteSet((0, sp.Symbol('tau0') - 1, sp.Symbol('tau0'))) or all(sp.simplify(A2.subs(k, -1) * M([0, t - 1, t]) - b2.subs(k, -1)) == sp.zeros(3, 1) for _ in [0]))
chk("Q2c official x=-2z, y=-1-z is NOT a solution", sp.simplify(A2.subs(k, -1) * M([-2 * t, -1 - t, t]) - b2.subs(k, -1)) != sp.zeros(3, 1))
# Q3
A3 = M([[1, 0, 1, 1], [1, 1, 2, 0], [0, 1, 1, -1]])
chk("Q3a rref [1 0 1 1;0 1 1 -1;0 0 0 0]", A3.rref()[0] == M([[1, 0, 1, 1], [0, 1, 1, -1], [0, 0, 0, 0]]))
ns = A3.nullspace()
chk("Q3a null basis (-1,-1,1,0),(-1,1,0,1), dim 2", len(ns) == 2 and A3 * M([-1, -1, 1, 0]) == sp.zeros(3, 1) and A3 * M([-1, 1, 0, 1]) == sp.zeros(3, 1))
chk("Q3b row space = sp{(1,0,1,1),(0,1,1,-1)} = sp{(1,0,1,1),(1,1,2,0)}, dim 2", sp.Matrix([[1, 0, 1, 1], [0, 1, 1, -1], [1, 1, 2, 0]]).rank() == 2 and A3.rank() == 2)
chk("Q3c col basis (1,1,0),(0,1,1), dim 2", sp.Matrix.hstack(M([1, 1, 0]), M([0, 1, 1])).rank() == 2 and sp.Matrix.hstack(A3, M([1, 1, 0]), M([0, 1, 1])).rank() == 2)
chk("Q3d 2+2=4", len(ns) + A3.rank() == 4)
# Q4
A4 = M([[2 * a, 4, 4 + 2 * a], [a, 3, 5], [1, 1, a]])
chk("Q4a1 det = 4(a-2)(a-1)", sp.expand(A4.det() - 4 * (a - 2) * (a - 1)) == 0)
A40 = A4.subs(a, 0)
chk("Q4a2 inverse at a=0", A40.inv() == M([[R(-5, 8), R(1, 2), 1], [R(5, 8), R(-1, 2), 0], [R(-3, 8), R(1, 2), 0]]))
B4 = M([[3, 1, 0], [0, 2, 0], [1, 1, 4]])
chk("Q4b1 eigenvalues 2,3,4", B4.eigenvals() == {2: 1, 3: 1, 4: 1})
P = M([[-1, -1, 0], [1, 0, 0], [0, 1, 1]]); D = sp.diag(2, 3, 4)
chk("Q4b1 eigenvectors (-1,1,0),(-1,0,1),(0,0,1)", all(B4 * P[:, i] == D[i, i] * P[:, i] for i in range(3)))
chk("Q4b2 P^-1 B P = D", P.inv() * B4 * P == D)
# Q5
Wb = [M([[1, 2], [-1, 0]]), M([[0, 0], [0, 1]])]
chk("Q5b W basis elements satisfy a+b=0 and top-right = 2a", all(m[1, 0] + m[0, 0] == 0 and m[0, 1] == 2 * m[0, 0] for m in Wb))
U1 = M([[-1, 2], [1, -3]]); U2 = M([[1, 0], [-1, 2]])
w = sp.Matrix([list(x) for x in Wb] + [list(U1), list(U2)])
bs, bt = sp.symbols("bs bt")
X = bs * U1 + bt * U2
cond = sp.solve([X[0, 1] - 2 * X[0, 0], X[1, 0] + X[0, 0]], [bs, bt], dict=True)
print("   intersection condition:", cond)
chk("Q5c intersection spanned by (1 2;-1 1) = U1+2 U2", sp.simplify((U1 + 2 * U2) - M([[1, 2], [-1, 1]])) == sp.zeros(2, 2) and all(sp.simplify(X.subs(c) - bt.subs(c) * (U1 / 2 + U2)) == sp.zeros(2, 2) for c in cond))
chk("Q5c dim(W cap U) = dim W + dim U - dim(W+U) = 2+2-3 = 1", sp.Matrix([list(x) for x in Wb + [U1, U2]]).rank() == 3)
chk("Q5d (1 1;1 1) not in W", 1 + 1 != 0)
# Q6
Tm = M([[1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1]])
chk("Q6a ker basis (1 -1;1 1), dim 1", len(Tm.nullspace()) == 1 and Tm * M([1, -1, 1, 1]) == sp.zeros(3, 1))
chk("Q6b rank 3, Im = R^3", Tm.rank() == 3)
chk("Q6c not injective, onto", len(Tm.nullspace()) > 0 and Tm.rank() == 3)
dd = sp.symbols("dd")
chk("Q6d preimage of (1,1,1) is (d 1-d; d d)", sp.simplify(Tm * M([dd, 1 - dd, dd, dd]) - M([1, 1, 1])) == sp.zeros(3, 1))
chk("Q6d zero matrix not in preimage so not a subspace", Tm * M([0, 0, 0, 0]) != M([1, 1, 1]))
# --- fix pass: pitfalls with the wrong vector (-1,3,-2)
_ws = M([-1, 3, -2]); _a1 = M([1, k, 2]); _a2 = M([2, 1, 1])
chk("Q1a wrong vector: det = 3k+9 -> k=-3", sp.solve(sp.Matrix.hstack(_ws, _a1, _a2).det(), k) == [-3])
_c = M([1, 2, 2]).cross(_a2)
chk("Q1b wrong vector: mixed product 15 -> 5 sqrt2 / 2", _c.dot(_ws) == 15 and sp.simplify(15 / _c.norm() - 5 * sp.sqrt(2) / 2) == 0)
print("MISMATCHES:", bad)
