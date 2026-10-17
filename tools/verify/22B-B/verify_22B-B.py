# -*- coding: utf-8 -*-
"""sympy checks of the official 22B-B answers. Run: PYTHONUTF8=1 py tools/verify/22B-B/verify_22B-B.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
R = sp.Rational
a, b, c, d, k, t, x, z, l = sp.symbols("a b c d k t x z l")
# Q1a: a+b=c+d => eigenvalues a+b and a-c
A = M([[a, b], [c, d]])
A_sub = A.subs(d, a + b - c)
ev = sp.solve(A_sub.charpoly(l).as_expr(), l)
chk("Q1a eigenvalues a+b, a-c", set(sp.simplify(e) for e in ev) == {a + b, a - c})
# Q1b,c,d with a random instance
B = M([[2, 1], [1, 1]]); u = B.eigenvects()[0][2][0]; lam = B.eigenvects()[0][0]
chk("Q1b B^-1 u = u/lam", sp.simplify(B.inv() * u - u / lam) == sp.zeros(2, 1))
s = sp.symbols("s")
chk("Q1c (B-sI)u = (lam-s)u", sp.simplify((B - s * sp.eye(2)) * u - (lam - s) * u) == sp.zeros(2, 1))
Pm = M([[1, 2], [0, 1]]); D_ = M([[3, 1], [0, 2]]); E_ = Pm * D_ * Pm.inv()
chk("Q1d PD=EP => same charpoly", sp.expand(E_.charpoly(l).as_expr() - D_.charpoly(l).as_expr()) == 0)
# Q2
Ma = M([[k, k**2, k], [1, k, -k], [1, 1, 1]]); rhs = M([1, 1, 1])
chk("Q2 det zero only at k=-1,0,1", set(sp.solve(Ma.det(), k)) == {-1, 0, 1}, str(sp.factor(Ma.det())))
sol = Ma.LUsolve(rhs)
sol = [sp.simplify(q) for q in sol]
print("  sol:", sol)
chk("Q2a x=(k+3)/(k+1)", sp.simplify(sol[0] - (k + 3) / (k + 1)) == 0)
chk("Q2a y=-1/k", sp.simplify(sol[1] + 1 / k) == 0)
chk("Q2a z=(1-k)/(k(k+1))", sp.simplify(sol[2] - (1 - k) / (k * (k + 1))) == 0)
M0 = Ma.subs(k, 0)
chk("Q2b k=0 first row 0=1", M0[0, :] == sp.zeros(1, 3))
Mm1 = Ma.subs(k, -1)
chk("Q2b k=-1 inconsistent, row1+row2=(0,0,0|2)", Mm1.rank() != Mm1.row_join(rhs).rank() and Mm1[0, :] + Mm1[1, :] == sp.zeros(1, 3))
M1 = Ma.subs(k, 1)
chk("Q2c k=1 rank 2 consistent", M1.rank() == 2 and M1.row_join(rhs).rank() == 2)
y = sp.symbols("y")
chk("Q2c general (1-y,y,0)", sp.simplify(M1 * M([1 - y, y, 0]) - rhs) == sp.zeros(3, 1))
chk("Q2c homogeneous (-t,t,0)", M1 * M([-t, t, 0]) == sp.zeros(3, 1))
# row-reduction intermediates
ech = M([[1, k, 1, 1 / k], [1, k, -k, 1], [1, 1, 1, 1]])
r2 = sp.simplify(ech[0, :] - ech[1, :]); r3 = sp.simplify(ech[0, :] - ech[2, :])
chk("Q2 step R1-R2, R1-R3", sp.simplify(r2 - M([[0, 0, 1 + k, 1 / k - 1]])) == sp.zeros(1, 4) and sp.simplify(r3 - M([[0, k - 1, 0, 1 / k - 1]])) == sp.zeros(1, 4))
r1new = sp.simplify(ech[0, :] - M([[0, 0, 1, (1 - k) / (k * (1 + k))]]))
chk("Q2 step R1-R2 -> (1,k,0,2/(k+1))", sp.simplify(r1new[3] - 2 / (k + 1)) == 0)
zz = sp.symbols("zz")
roots = sp.solve(M([zz, -1, 2]).dot(M([zz, zz, 1])), zz)
chk("Q2d roots (1+-i sqrt7)/2", set(map(sp.simplify, roots)) == {(1 + sp.I * sp.sqrt(7)) / 2, (1 - sp.I * sp.sqrt(7)) / 2})
# Q3
A3 = M([[1, 4, 0], [0, 1, 2], [3, 12, 3]])
Ai = M([[-7, -4, R(8, 3)], [2, 1, -R(2, 3)], [-1, 0, R(1, 3)]])
chk("Q3.1a inverse", A3.inv() == Ai)
E1 = M([[1, -4, 0], [0, 1, 0], [0, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, -2], [0, 0, 1]])
E3 = sp.diag(1, 1, R(1, 3)); E4 = M([[1, 0, 0], [0, 1, 0], [-3, 0, 1]])
chk("Q3.1b E1E2E3E4 = A^-1", E1 * E2 * E3 * E4 == Ai)
B3 = M([[5, 0, 1], [0, 4, 0], [1, 0, 5]])
chk("Q3.2 charpoly (l-4)^2(l-6)", sp.expand(B3.charpoly(l).as_expr() - (l - 4)**2 * (l - 6)) == 0)
P = M([[-1, 0, 1], [0, 1, 0], [1, 0, 1]]); D = sp.diag(4, 4, 6)
chk("Q3.2 D=P^-1 B P", P.inv() * B3 * P == D)
# Q4
xs = sp.symbols("x")
cs = lambda q: [sp.Poly(q, xs).coeff_monomial(xs**j) for j in range(4)]  # coords wrt 1,x,x2,x3
W1b = [sp.Integer(1), xs**2, xs**3 - xs]
W2b = [-xs**3 + 8, -xs**3 + 4 * xs, -xs**3 + 2 * xs**2]
inW1 = lambda q: sp.expand(q.subs(xs, -1) - q.subs(xs, 1)) == 0
inW2 = lambda q: sp.expand(q.subs(xs, 2)) == 0
chk("Q4a W1 basis in W1", all(inW1(q) for q in W1b))
chk("Q4a W2 basis in W2", all(inW2(q) for q in W2b))
W1m = M([cs(q) for q in W1b]); W2m = M([cs(q) for q in W2b])
chk("Q4a dims 3,3", W1m.rank() == 3 and W2m.rank() == 3)
# dim W1 = dim of solution set: constraint a1+a3=0 (1 equation) ; W2: one equation => 3 each
chk("Q4a W1 constraint a1+a3=0 matches", all(cs(q)[1] + cs(q)[3] == 0 for q in W1b))
chk("Q4b dim(W1+W2)=4", W1m.col_join(W2m).rank() == 4)
chk("Q4b first four of the union form a basis", M([cs(q) for q in W1b + [W2b[0]]]).rank() == 4)
inter_basis = [-xs**3 + xs + 6, xs**2 - 4]
chk("Q4c intersection basis in W1 and W2", all(inW1(q) and inW2(q) for q in inter_basis))
chk("Q4c dim(W1 cap W2)=3+3-4=2", 3 + 3 - 4 == 2 and M([cs(q) for q in inter_basis]).rank() == 2)
beta = sp.symbols("b1 b2 b3")
pv = sum(bb * q for bb, q in zip(beta, W2b))
chk("Q4c beta1=3b2-b3 in W1", inW1(sp.expand(pv.subs(beta[0], 3 * beta[1] - beta[2]))))
t1, t2 = sp.symbols("t1 t2")
chk("Q4c (3t1-t2)(-x^3+8)+t1(..)+t2(..) simplifies", sp.expand((3 * t1 - t2) * W2b[0] + t1 * W2b[1] + t2 * W2b[2] - (4 * t1 * inter_basis[0] + 2 * t2 * inter_basis[1])) == 0)
chk("Q4d p = (-x^3+x+6) + 2(x^2-4)", sp.expand(-xs**3 + 2 * xs**2 + xs - 2 - (inter_basis[0] + 2 * inter_basis[1])) == 0 and inW1(-xs**3 + 2 * xs**2 + xs - 2) and inW2(-xs**3 + 2 * xs**2 + xs - 2))
# Q5
Tm = M([[1, 1, 1], [0, 1, 2], [0, 2, k**2 + 3], [0, -1, -2]])
aug = Tm.row_join(M([1, 1, 2, k]))
rr = aug.copy(); rr[2, :] = rr[2, :] - 2 * rr[1, :]; rr[3, :] = rr[3, :] + rr[1, :]
chk("Q5a reduced (0 0 k^2-1 | 0),(0 0 0 | k+1)", rr[2, :].applyfunc(sp.expand) == M([[0, 0, k**2 - 1, 0]]) and rr[3, :].applyfunc(sp.expand) == M([[0, 0, 0, k + 1]]))
chk("Q5a only k=-1", sp.solve(rr[3, 3], k) == [-1])
chk("Q5b never onto (3 columns < 4)", all(Tm.subs(k, v).rank() <= 3 for v in range(-3, 4)))
chk("Q5b injective iff k != +-1", all((Tm.subs(k, v).rank() == 3) == (v not in (1, -1)) for v in range(-3, 4)))
T1 = Tm.subs(k, 1)
chk("Q5c k=1 kernel (1,-2,1)", len(T1.nullspace()) == 1 and T1 * M([1, -2, 1]) == sp.zeros(4, 1))
Bm = M([[1, 3], [1, 4]]); FB = M([[2, 5], [2, 0]])
FE = FB * Bm.inv()
chk("Q5d [F]_E^E = [[3,-1],[8,-6]]", FE == M([[3, -1], [8, -6]]))
chk("Q5d check F(1,1)=(2,2), F(3,4)=(5,0)", FE * M([1, 1]) == M([2, 2]) and FE * M([3, 4]) == M([5, 0]))
print("ALL OK" if not bad else "MISMATCHES: " + ", ".join(bad))
