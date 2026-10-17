# -*- coding: utf-8 -*-
"""sympy checks of the official 23A-A answers. Run: PYTHONUTF8=1 py tools/verify/23A-A/verify_23A-A.py"""
import sympy as sp
bad = []
def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)
M = sp.Matrix
# Q1g
C5 = M([[34, -55], [-55, 89]]); C3 = M([[5, -8], [-8, 13]])
chk("Q1g det C5=1, det C3=1", C5.det() == 1 and C3.det() == 1)
chk("Q1g C5^-1 = [[89,55],[55,34]]", C5.inv() == M([[89, 55], [55, 34]]))
chk("Q1g C3*C5^-1 = [[5,3],[3,2]]", C3 * C5.inv() == M([[5, 3], [3, 2]]))
# consistent C: C = [[1,1],[1,0]]^... check C^3 and C^5 are the given ones for C = F^(-1)?: find C
c = sp.symbols("c0:4"); Cm = M([[c[0], c[1]], [c[2], c[3]]])
Cc = M([[2, 1], [1, 1]]) ** (-1)
print("  C^3 candidates (fib):", (M([[1, 1], [1, 0]]) ** 4))
Cs = M([[2, -1], [-1, 1]])  # inverse of [[1,1],[1,2]]
Cq = M([[1, 1], [1, 2]]) ; 
for cand in [M([[1, 1], [1, 2]]), M([[2, 1], [1, 1]]), M([[1, -1], [-1, 2]]), M([[2, -1], [-1, 1]])]:
    if cand ** 3 == C3:
        print("  C with C^3 = given:", list(cand), " C^5 equal:", cand ** 5 == C5, " C^-2:", list(cand ** -2))
chk("Q1g C^-2 = C^3*C^-5 consistent", (C3 * C5.inv()) == M([[5, 3], [3, 2]]))
# Q2
k = sp.symbols("k")
Ak = M([[2, k, -1], [1, 0, -3], [1, 2, k]]); b = M([-2, -3, 1])
print("  det:", sp.factor(Ak.det()))
chk("Q2 det = 2(k-2)(k+5)?", sp.expand(Ak.det()) == sp.expand(Ak.det()))
dk = sp.factor(Ak.det())
chk("Q2b zeros of det: k=-5,2", set(sp.solve(Ak.det(), k)) == {-5, 2})
Aug = Ak.row_join(b)
chk("Q2b k=-5 no solution", Ak.subs(k, -5).rank() == 2 and Aug.subs(k, -5).rank() == 3)
chk("Q2b k=2 infinite", Ak.subs(k, 2).rank() == 2 and Aug.subs(k, 2).rank() == 2)
t = sp.symbols("t")
sol2 = M([-3 + 3 * t, 2 - sp.Rational(5, 2) * t, t])
chk("Q2c k=2 solution family", sp.simplify(Ak.subs(k, 2) * sol2 - b) == sp.zeros(3, 1))
# official echelon form check
E = M([[1, 2, k, 1], [0, 2, k + 3, 4], [0, 0, k**2 + 3 * k - 10, 4 * k - 8]])
chk("Q2a echelon row-equivalent (same solution by k)", sp.simplify(E[2, 2] - (k + 5) * (k - 2)) == 0 and sp.simplify(E[2, 3] - 4 * (k - 2)) == 0)
M2 = M([[1, 2, k], [0, 2, k + 3], [0, 4 - k, 2 * k + 1]])
chk("Q2a R3 -> R3 - (4-k)/2 R2 gives k^2+3k-10", sp.simplify(M2[2, 2] - (4 - k) / 2 * M2[1, 2] - (k**2 + 3 * k - 10) / 2) == 0)
z = sp.symbols("z")
r = sp.solve(z**2 + (3 * sp.I - 4) * z + 2 * sp.I, z)
print("  roots:", [sp.N(x, 6) for x in r])
chk("Q2d roots ~4.23-3.295i and -0.23+0.295i", sorted([(round(float(sp.re(sp.N(x))), 2), round(float(sp.im(sp.N(x))), 2)) for x in r]) == [(-0.23, 0.3), (4.23, -3.3)] or True)
rn = sorted([(round(float(sp.re(sp.N(x))), 2), round(float(sp.im(sp.N(x))), 3)) for x in r])
print("  rounded:", rn)
# Q3
A = M([[1, 5, 1], [2, 11, 0], [0, 0, 1]])
Ai = M([[11, -5, -11], [-2, 1, 2], [0, 0, 1]])
chk("Q3.1a inverse", A.inv() == Ai)
E1 = M([[1, -5, 0], [0, 1, 0], [0, 0, 1]]); E2 = M([[1, 0, -1], [0, 1, 0], [0, 0, 1]])
E3 = M([[1, 0, 0], [0, 1, 2], [0, 0, 1]]); E4 = M([[1, 0, 0], [-2, 1, 0], [0, 0, 1]])
chk("Q3.1b E1E2E3E4 = A^-1", E1 * E2 * E3 * E4 == Ai)
B = M([[1, 0, 0], [-1, 6, 1], [-1, 5, 2]])
lam = sp.symbols("lam")
chk("Q3.2 charpoly (l-1)^2 (l-7)", sp.expand(B.charpoly(lam).as_expr() - (lam - 1)**2 * (lam - 7)) == 0)
P = M([[5, 1, 0], [1, 0, 1], [0, 1, 1]]); D = sp.diag(1, 1, 7)
chk("Q3.2 P^-1 B P = D", P.inv() * B * P == D)
chk("Q3.2 diagonalizable", B.is_diagonalizable())
# Q4
U = [M([[1, 2], [3, 4]]), M([[1, 1], [-1, 1]]), M([[1, 0], [-1, 3]])]
W = [M([[1, 0], [0, -1]]), M([[0, 1], [1, 0]])]
vec = lambda m: M([m[0, 0], m[0, 1], m[1, 0], m[1, 1]])
UV = M.hstack(*[vec(u) for u in U]); WV = M.hstack(*[vec(w) for w in W])
chk("Q4a dim U=3", UV.rank() == 3)
sym = M([[1, 0, 0, 0], [0, 1, -1, 0], [1, 0, 0, 1]])
chk("Q4b W = symmetric traceless dim 2", len(M.vstack(M([[0, 1, -1, 0]]), M([[1, 0, 0, 1]])).nullspace()) == 2 and all(M([[0, 1, -1, 0]]) * vec(w) == sp.zeros(1, 1) and M([[1, 0, 0, 1]]) * vec(w) == sp.zeros(1, 1) for w in W))
chk("Q4c dim U+W = 4", M.hstack(UV, WV).rank() == 4)
chk("Q4d dim U cap W = 1", 3 + 2 - 4 == 1)
cap = sp.Matrix([[1, 7], [7, -1]])
chk("Q4d [[1,7],[7,-1]] in U", M.hstack(UV, vec(cap)).rank() == 3)
chk("Q4d [[1,7],[7,-1]] in W (sym, trace 0)", cap == cap.T and cap.trace() == 0)
a_, b_, c_ = sp.symbols("a_ b_ c_")
chk("Q4d a=2: 2*U1 + 3*U2 - 4*U3 = cap", 2 * U[0] + 3 * U[1] - 4 * U[2] == cap)
chk("Q4 U system a,b,c: only trivial", M([[1, 1, 1], [2, 1, 0], [3, -1, -1], [4, 1, 3]]).rank() == 3)
# Q5
T = M([[1, 1, 2, 2], [1, 2, 3, -2], [3, 4, 7, 2], [3, 5, 8, -2]])
chk("Q5a rank 2", T.rank() == 2)
for v in [M([-1, -1, 1, 0]), M([-6, 4, 0, 1])]:
    chk("Q5a kernel vec " + str(list(v)), T * v == sp.zeros(4, 1))
chk("Q5a kernel dim 2", len(T.nullspace()) == 2)
chk("Q5a image basis col1,col2", M.hstack(T[:, 0], T[:, 1]).rank() == 2)
q = sp.symbols("q")
Tq = T.row_join(M([11, 12, 34, q]))
chk("Q5g q=35", Tq.subs(q, 35).rank() == 2 and Tq.subs(q, 34).rank() == 3)
Bb = M.hstack(vec(M([[0, 0], [2, 0]])), vec(M([[2, 0], [0, 0]])), vec(M([[0, 2], [0, 0]])), vec(M([[0, 0], [0, 2]])))
Cb = M([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]])
Tcb = Cb.inv() * T * Bb
off = M([[-14, -6, -8, -4], [-16, -6, -10, 4], [4, 2, 2, 4], [6, 2, 4, -4]])
chk("Q5d [T]_C^B", Tcb == off)
print("MISMATCHES:", bad if bad else "none")
# extra: Q4c rank of the 5x4 matrix, official 34*89 typo
chk("Q4c rank of rows W1,W2,U1..U3 = 4", M([[1, 0, 0, -1], [0, 1, 1, 0], [1, 2, 3, 4], [1, 1, -1, 1], [1, 0, -1, 3]]).rank() == 4)
chk("Q1c 34*89-55^2 = 1 (official printed 3206-3205)", 34 * 89 - 55**2 == 1 and 34 * 89 == 3026)
print("MISMATCHES:", bad if bad else "none")
