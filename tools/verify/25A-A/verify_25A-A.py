# -*- coding: utf-8 -*-
"""sympy checks of the official 25A-A answers. Run: PYTHONUTF8=1 py tools/verify/25A-A/verify_25A-A.py
Prints OK/MISMATCH lines (ASCII only)."""
import sympy as sp

bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)

# ---- Q1 : lines (a>0 intersect), plane S1 through both, plane S2 through l1 perpendicular to S1
a, s, t = sp.symbols("a s t", real=True)
l1 = sp.Matrix([0, a, -a]) + s * sp.Matrix([1, 0, 1])
l2 = sp.Matrix([5, -4, -1]) + t * sp.Matrix([a, -3, 0])
sol = sp.solve(list(l1 - l2), [s, t, a], dict=True)
print("  intersect solutions (s,t,a):", [(d[s], d[t], d[a]) for d in sol])
avals = sorted(d[a] for d in sol)
chk("Q1a a in {-9,2}", avals == [-9, 2])
L1 = sp.Matrix([1, 0, 1]); L2 = sp.Matrix([2, -3, 0]); p0 = sp.Matrix([0, 2, -2])
N1 = L1.cross(L2)
chk("Q1b N1=(3,2,-3)", list(N1) == [3, 2, -3])
chk("Q1b S1: 3x+2y-3z=10 (p0 on it)", (N1.T * p0)[0] == 10)
pt = (l2.subs({a: 2, t: -2}))
chk("Q1 intersection point (1,2,-1) on both", list(pt) == [1, 2, -1] and list(l1.subs({a: 2, s: 1})) == [1, 2, -1])
N2 = L1.cross(N1)
chk("Q1c N2 = 2(-1,3,1)", list(N2) == [-2, 6, 2])
chk("Q1c S2: -x+3y+z=4 (p0 on it)", ((-1) * 0 + 3 * 2 + (-2)) == 4)
chk("Q1c S2 normal perpendicular to N1 and L1", (N2.dot(N1) == 0) and (N2.dot(L1) == 0))

# ---- Q2 : homogeneous system with parameter
a = sp.symbols("a")
M = sp.Matrix([[a, a, -1], [a**2, a, a**2 - a], [a, a, 2*a + 1]])
R = M.copy()
R[1, :] = R[1, :] - a * R[0, :]
R[2, :] = R[2, :] - R[0, :]
chk("Q2a first step matrix", sp.simplify(R - sp.Matrix([[a, a, -1], [0, a - a**2, a**2], [0, 0, 2*a + 2]])) == sp.zeros(3, 3))
for av, rk in [(0, 1), (1, 2), (-1, 2), (2, 3), (5, 3), (sp.Rational(1, 2), 3)]:
    chk(f"Q2 rank at a={av} is {rk}", M.subs(a, av).rank() == rk)
chk("Q2 det = 2a^2(a-1)(a+1)? (zero set 0,1,-1)", sorted(sp.solve(sp.factor(M.det()), a)) == [-1, 0, 1], str(sp.factor(M.det())))
ns0 = M.subs(a, 0).nullspace(); ns1 = M.subs(a, 1).nullspace(); nsm = M.subs(a, -1).nullspace()
chk("Q2 a=0 nullspace = span{(1,0,0),(0,1,0)}", len(ns0) == 2 and all(v[2] == 0 for v in ns0))
chk("Q2 a=1 nullspace = span{(1,-1,0)}", len(ns1) == 1 and ns1[0].T.tolist()[0] in ([1, -1, 0], [-1, 1, 0]))
chk("Q2 a=-1 nullspace = span{(-3,1,2)}", len(nsm) == 1 and sp.Matrix([-3, 1, 2]).rank() == sp.Matrix.hstack(nsm[0], sp.Matrix([-3, 1, 2])).rank())

# ---- Q2d (this sitting numbering: Q2 has only four parts) -- no complex part in 25A-A

# ---- Q3a : inverse + elementary factorization
A = sp.Matrix([[1, 2, 1], [0, 1, 3], [3, 8, 8]])
Ai = A.inv()
chk("Q3a inverse", Ai == sp.Matrix([[16, 8, -5], [-9, -5, 3], [3, 2, -1]]))
E = [sp.Matrix([[1, -2, 0], [0, 1, 0], [0, 0, 1]]), sp.Matrix([[1, 0, -1], [0, 1, 0], [0, 0, 1]]),
     sp.Matrix([[1, 0, 0], [0, 1, -3], [0, 0, 1]]), sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]]),
     sp.Matrix([[1, 0, 0], [0, 1, 0], [0, -2, 1]]), sp.Matrix([[1, 0, 0], [0, 1, 0], [-3, 0, 1]])]
prod = sp.eye(3)
for e in E:
    prod = prod * e
chk("Q3a product of six elementary matrices = A^-1", prod == Ai)
chk("Q3a det A = -1", A.det() == -1)

# ---- Q3b : diagonalization
B = sp.Matrix([[9, 0, 1], [0, 8, 0], [1, 0, 9]])
chk("Q3b char poly (l-8)^2(l-10)", sp.factor(B.charpoly().as_expr()) == sp.factor((sp.Symbol('lambda') - 8)**2 * (sp.Symbol('lambda') - 10)) or
    sp.roots(B.charpoly()) == {8: 2, 10: 1})
P = sp.Matrix([[-1, 0, 1], [0, 1, 0], [1, 0, 1]]); D = sp.diag(8, 8, 10)
chk("Q3b BP = PD", B * P == P * D)
chk("Q3b P invertible, D = P^-1 B P", P.det() != 0 and P.inv() * B * P == D)

# ---- Q4 : polynomials in R3[x], coordinates (a,b,c,d) for ax^3+bx^2+cx+d
x = sp.symbols("x")
pa, pb, pc, pd = sp.symbols("pa pb pc pd")
p = pa * x**3 + pb * x**2 + pc * x + pd
sol1 = sp.solve([p.subs(x, 0) - sp.diff(p, x).subs(x, 0), sp.diff(p, x).subs(x, 0) - sp.diff(p, x, 2).subs(x, 0)], [pc, pd], dict=True)[0]
chk("Q4a W1: c=2b, d=2b", sol1[pc] == 2 * pb and sol1[pd] == 2 * pb)
w1 = [sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 2, 2])]
w2 = [sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 0, 0]), sp.Matrix([0, 0, 0, 1])]
chk("Q4a dim W1=2, dim W2=3", sp.Matrix.hstack(*w1).rank() == 2 and sp.Matrix.hstack(*w2).rank() == 3)
S = sp.Matrix.hstack(*(w1 + w2))
chk("Q4b dim(W1+W2)=4", S.rank() == 4)
chk("Q4c dim(W1 n W2) = 2+3-4 = 1", w1.__len__() + w2.__len__() - S.rank() == 1)
# explicit intersection: alpha*w1 comb = beta*w2 comb
al1, al2, be1, be2, be3 = sp.symbols("al1 al2 be1 be2 be3")
vec = al1 * w1[0] + al2 * w1[1] - (be1 * w2[0] + be2 * w2[1] + be3 * w2[2])
sol = sp.solve(list(vec), [al2, be2, be3, be1], dict=True)[0]
chk("Q4c intersection = span{x^3}", sol[al2] == 0 and sol[be2] == 0 and sol[be3] == 0 and sol[be1] == al1)
q = sp.Matrix([1, 2, 0, 3])
chk("Q4d Q=(1,2,0,3) in W1+W2 (full space)", sp.Matrix.hstack(S, q).rank() == S.rank() == 4)

# ---- Q5.1 : T : R3[x] -> M2x2
cols = [sp.Matrix([1, 1, 1, 1]), sp.Matrix([2, 0, 2, 5]), sp.Matrix([12, 10, 12, 15]), sp.Matrix([21, 1, 21, 51])]
T = sp.Matrix.hstack(*cols)
chk("Q5a matrix as printed", T == sp.Matrix([[1, 2, 12, 21], [1, 0, 10, 1], [1, 2, 12, 21], [1, 5, 15, 51]]))
chk("Q5a rank = 2, pivot cols 1,2", T.rank() == 2 and T.rref()[1] == (0, 1))
ker = T.nullspace()
kb = [sp.Matrix([-10, -1, 1, 0]), sp.Matrix([-1, -10, 0, 1])]
chk("Q5a Ker basis (-10,-1,1,0),(-1,-10,0,1)", all(T * k == sp.zeros(4, 1) for k in kb) and len(ker) == 2 and sp.Matrix.hstack(*kb).rank() == 2)
chk("Q5b not injective (ker dim 2), not onto M2x2 (rank 2 < 4)", len(ker) == 2 and T.rank() < 4)
aa, bb = sp.symbols("aa bb")
solc = sp.solve(list(T * sp.Matrix([22, 22, aa, bb])), [aa, bb], dict=True)
chk("Q5c a=b=-2", solc == [{aa: -2, bb: -2}])

# ---- Q5.2 : change of basis
EB = sp.Matrix([[2, 0], [2, 5]]); EC = sp.Matrix([[1, 2], [3, 7]])
chk("Q5d [I]_C^B = (E^C)^-1 E^B = [[10,-10],[-4,5]]", EC.inv() * EB == sp.Matrix([[10, -10], [-4, 5]]))

print("DONE, mismatches:", bad if bad else "none")
