# -*- coding: utf-8 -*-
"""sympy checks of the official 25B-A answers. Run: PYTHONUTF8=1 py tools/verify/25B-A/verify_25B-A.py
Prints OK/MISMATCH lines (ASCII only). Q6 has no official solution (held), so it is not checked here."""
import sympy as sp

bad = []


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational
t, s, a = sp.symbols("t s a")
V = sp.Matrix

# ---- Q1 : planes S1,S2,S3 and lines
N1 = V([1, 1, 1])
pl1 = lambda p: p[0] + p[1] + p[2]
pl2 = lambda p: 2 * p[0] - p[1] + 2 * p[2] - 1
pl3 = lambda p: p[0] - p[1] + 2 * p[2] + 1
l1 = V([R(1, 3), R(-1, 3), 0]) + t * V([-1, 0, 1])
chk("Q1a l1 lies in S1 and S2", sp.simplify(pl1(l1)) == 0 and sp.simplify(pl2(l1)) == 0)
chk("Q1a l1 direction = N1 x N2", N1.cross(V([2, -1, 2])).T.rank() == 1 and sp.Matrix.hstack(N1.cross(V([2, -1, 2])), V([-1, 0, 1])).rank() == 1)
l2 = V([R(-1, 2), R(1, 2), 0]) + s * V([-3, 1, 2])
chk("Q1a l2 lies in S1 and S3 (direction (-3,1,2))", sp.simplify(pl1(l2)) == 0 and sp.simplify(pl3(l2)) == 0)
chk("Q1a l2 direction = N1 x N3", sp.Matrix.hstack(N1.cross(V([1, -1, 2])), V([-3, 1, 2])).rank() == 1)
chk("Q1a rref S1,S2 gives x=1/3-z, y=-1/3", sp.Matrix([[1, 1, 1, 0], [2, -1, 2, 1]]).rref()[0] == sp.Matrix([[1, 0, 1, R(1, 3)], [0, 1, 0, R(-1, 3)]]))
chk("Q1a rref S1,S3 gives x=-1/2-3/2 z, y=1/2+1/2 z", sp.Matrix([[1, 1, 1, 0], [1, -1, 2, -1]]).rref()[0] == sp.Matrix([[1, 0, R(3, 2), R(-1, 2)], [0, 1, R(-1, 2), R(1, 2)]]))
L1 = V([-1, 0, 1]); L2 = V([-3, 1, 2])
N4 = N1.cross(L1); N5 = N1.cross(L2)
chk("Q1b N4=(1,-2,1), N5=(1,-5,4)", list(N4) == [1, -2, 1] and list(N5) == [1, -5, 4])
p1 = V([R(1, 3), R(-1, 3), 0]); p2 = V([R(-1, 2), R(1, 2), 0])
chk("Q1b S4: x-2y+z=1 contains p1, N4.N1=0 and contains l1", N4.dot(p1) == 1 and N4.dot(N1) == 0 and N4.dot(L1) == 0)
chk("Q1b S5: x-5y+4z=-3 contains p2, N5.N1=0 and contains l2", N5.dot(p2) == -3 and N5.dot(N1) == 0 and N5.dot(L2) == 0)
sol = sp.solve(list(l1 - V([R(-1, 2), R(1, 2), 0]) - s * L2), [t, s], dict=True)
chk("Q1c l1 and l2 meet: s=-5/6, t=-5/3", sol and sol[0][s] == R(-5, 6) and sol[0][t] == R(-5, 3), str(sol))
p0 = l1.subs(t, R(-5, 3))
chk("Q1c p0 = (2,-1/3,-5/3)", list(p0) == [2, R(-1, 3), R(-5, 3)])
chk("Q1c p0 on l2 with s=-5/6", list(V([R(-1, 2), R(1, 2), 0]) + R(-5, 6) * L2) == list(p0))
chk("Q1c p0 satisfies S1,S2,S3", pl1(p0) == 0 and pl2(p0) == 0 and pl3(p0) == 0)
chk("Q1c (II) -1/3 = 1/2 + s gives s=-5/6", sp.solve(R(-1, 3) - R(1, 2) - s, s) == [R(-5, 6)])
chk("Q1c p0 on S4 and S5", N4.dot(p0) == 1 and N5.dot(p0) == -3)
chk("Q1c l3 direction N4 x N5 parallel to N1", sp.Matrix.hstack(N4.cross(N5), N1).rank() == 1)
chk("Q1c l3 = p0 + t(1,1,1) in S4 and S5", sp.simplify(N4.dot(p0 + t * N1) - 1) == 0 and sp.simplify(N5.dot(p0 + t * N1) + 3) == 0)

# ---- Q2 : system with parameter a and complex equation
M = sp.Matrix([[1, -1, 2, 0], [-1, a, a - 3, a], [0, a - 1, 2 * a, 2 * a + 1], [1, a - 2, 2 * a + 2, 2 * a + 1]])
E = M.copy()
E[1, :] = E[1, :] + E[0, :]
E[3, :] = E[3, :] - E[0, :]
chk("Q2a step R2+R1, R4-R1", E == sp.Matrix([[1, -1, 2, 0], [0, a - 1, a - 1, a], [0, a - 1, 2 * a, 2 * a + 1], [0, a - 1, 2 * a, 2 * a + 1]]))
E[3, :] = E[3, :] - E[2, :]
E[2, :] = E[2, :] - E[1, :]
chk("Q2a final echelon", sp.simplify(E - sp.Matrix([[1, -1, 2, 0], [0, a - 1, a - 1, a], [0, 0, a + 1, a + 1], [0, 0, 0, 0]])) == sp.zeros(4, 4))
A = M[:, :3]
for av, ra, rm in [(1, 2, 3), (-1, 2, 2), (2, 3, 3), (0, 3, 3), (5, 3, 3)]:
    chk("Q2b a=%s rank A=%s rank [A|b]=%s" % (av, ra, rm), A.subs(a, av).rank() == ra and M.subs(a, av).rank() == rm)
chk("Q2b a=1 no solution, a=-1 infinitely many, else unique", True if (M.subs(a, 1).rank() > A.subs(a, 1).rank()) and (M.subs(a, -1).rank() == A.subs(a, -1).rank() == 2) else False)
x, y, z = sp.symbols("x y z")
solm = sp.solve(list(A.subs(a, -1) * V([x, y, z]) - M.subs(a, -1)[:, 3]), [x, y], dict=True)[0]
chk("Q2c a=-1: y=1/2-z, x=1/2-3z", sp.simplify(solm[x] - (R(1, 2) - 3 * z)) == 0 and sp.simplify(solm[y] - (R(1, 2) - z)) == 0, str(solm))
chk("Q2c a=-1 particular and direction", A.subs(a, -1) * V([R(1, 2), R(1, 2), 0]) == M.subs(a, -1)[:, 3] and A.subs(a, -1) * V([-3, -1, 1]) == sp.zeros(4, 1))
chk("Q2c a=-1 equivalent system x-y+2z=0, -2y-2z=-1", True if sp.Matrix([[1, -1, 2, 0], [0, -2, -2, -1]]).rref()[0].rank() == 2 else False)
zz = sp.symbols("zz")
w = sp.symbols("w")
roots = sp.solve(w**3 - 8 * sp.I, w)
chk("Q2d w^3 = 8i roots sqrt3+i, -sqrt3+i, -2i", set(map(sp.simplify, roots)) == {sp.sqrt(3) + sp.I, -sp.sqrt(3) + sp.I, -2 * sp.I})
chk("Q2d (7-i)/(3+i) = 2-i", sp.simplify((7 - sp.I) / (3 + sp.I) - (2 - sp.I)) == 0)
zs = [sp.conjugate(r) - 2 - sp.I for r in [sp.sqrt(3) + sp.I, -sp.sqrt(3) + sp.I, -2 * sp.I]]
chk("Q2d z0=-2+sqrt3-2i, z1=-2-sqrt3-2i, z2=-2+i", [sp.simplify(q) for q in zs] == [-2 + sp.sqrt(3) - 2 * sp.I, -2 - sp.sqrt(3) - 2 * sp.I, -2 + sp.I])
for q in zs:
    chk("Q2d solution %s satisfies the equation" % q, sp.simplify(sp.expand((sp.conjugate(q) + (7 - sp.I) / (3 + sp.I))**3 - 8 * sp.I)) == 0)
chk("Q2d exactly 3 solutions (cubic in z-bar)", len(roots) == 3)

# ---- Q3.1 inverse
A3 = sp.Matrix([[1, -1, 0], [0, 1, 1], [5, -5, 9]])
Ai = sp.Matrix([[R(14, 9), 1, R(-1, 9)], [R(5, 9), 1, R(-1, 9)], [R(-5, 9), 0, R(1, 9)]])
chk("Q3a A^-1 as printed", A3.inv() == Ai and A3 * Ai == sp.eye(3))
M0 = A3.row_join(sp.eye(3))
c1 = M0.copy(); c1[2, :] -= 5 * c1[0, :]
chk("Q3a R3-5R1", c1[2, :] == sp.Matrix([[0, 0, 9, -5, 0, 1]]))
c2 = c1.copy(); c2[2, :] = c2[2, :] / 9
chk("Q3a R3/9", c2[2, :] == sp.Matrix([[0, 0, 1, R(-5, 9), 0, R(1, 9)]]))
c3 = c2.copy(); c3[1, :] -= c3[2, :]
chk("Q3a R2-R3", c3[1, :] == sp.Matrix([[0, 1, 0, R(5, 9), 1, R(-1, 9)]]))
c4 = c3.copy(); c4[0, :] += c4[1, :]
chk("Q3a R1+R2 -> [I|A^-1]", c4 == sp.eye(3).row_join(Ai))
G1 = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
G2 = sp.Matrix([[1, 0, 0], [0, 1, -1], [0, 0, 1]])
G3 = sp.diag(1, 1, R(1, 9))
G4 = sp.Matrix([[1, 0, 0], [0, 1, 0], [-5, 0, 1]])
chk("Q3a A^-1 = G1 G2 G3 G4 (as printed, four factors)", G1 * G2 * G3 * G4 == Ai)
chk("Q3a factors are elementary (R1+R2, R2-R3, R3/9, R3-5R1)",
    G1 == sp.eye(3).elementary_row_op("n->n+km", row=0, k=1, row2=1) and G2 == sp.eye(3).elementary_row_op("n->n+km", row=1, k=-1, row2=2)
    and G4 == sp.eye(3).elementary_row_op("n->n+km", row=2, k=-5, row2=0))

# ---- Q3.2 diagonalization
B = sp.Matrix([[7, 0, 1], [0, 6, 0], [1, 0, 7]])
lam = sp.symbols("lam")
chk("Q3b char poly (l-6)^2 (l-8)", sp.expand((lam * sp.eye(3) - B).det() - (lam - 6)**2 * (lam - 8)) == 0)
chk("Q3b eigenvalues 6,6,8", B.eigenvals() == {6: 2, 8: 1})
chk("Q3b (l-6)(l^2-14l+48)", sp.expand((lam - 6) * (lam**2 - 14 * lam + 48) - (lam - 6)**2 * (lam - 8)) == 0)
P = sp.Matrix([[-1, 0, 1], [0, 1, 0], [1, 0, 1]])
D = sp.diag(6, 6, 8)
chk("Q3b PD = BP", P * D == B * P)
chk("Q3b P invertible", P.det() != 0, "det=%s" % P.det())
chk("Q3b PD as printed", P * D == sp.Matrix([[-6, 0, 8], [0, 6, 0], [6, 0, 8]]))
chk("Q3b BP as printed", B * P == sp.Matrix([[-6, 0, 8], [0, 6, 0], [6, 0, 8]]))
chk("Q3b rref(B-6I) = [1 0 1;0 0 0;0 0 0]", (B - 6 * sp.eye(3)).rref()[0] == sp.Matrix([[1, 0, 1], [0, 0, 0], [0, 0, 0]]))
chk("Q3b rref(B-8I) = [1 0 -1;0 1 0;0 0 0]", (B - 8 * sp.eye(3)).rref()[0] == sp.Matrix([[1, 0, -1], [0, 1, 0], [0, 0, 0]]))

# ---- Q4 symmetric matrices, U, W in M2x2 (coordinates a,b,c,d)
e11 = V([1, 0, 0, 0]); sy = V([0, 1, 1, 0]); e22 = V([0, 0, 0, 1])
u1 = V([1, 2, -1, 3]); u2 = V([2, 0, -3, 2])
Wb = sp.Matrix.hstack(e11, sy, e22)
chk("Q4b W basis independent, dim 3", Wb.rank() == 3)
chk("Q4b W = {b=c} has dim 3 (nullspace of [0 1 -1 0])", len(sp.Matrix([[0, 1, -1, 0]]).nullspace()) == 3)
chk("Q4b chain: -R2+R3, swap R3,R4 gives [I;0]", sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]]).rref()[0] == sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]))
Sm = sp.Matrix.hstack(e11, sy, e22, u1, u2)
chk("Q4c printed echelon is row-equivalent to the 4x5 matrix", Sm.rref()[0] == sp.Matrix([[1, 0, 0, 1, 2], [0, 1, 0, 2, 0], [0, 0, 1, 3, 2], [0, 0, 0, 1, 1]]).rref()[0])
chk("Q4c dim(U+W)=4, U independent", Sm.rank() == 4 and sp.Matrix.hstack(u1, u2).rank() == 2)
chk("Q4c basis E11, E12+E21, E22, u1 spans U+W", sp.Matrix.hstack(e11, sy, e22, u1).rank() == 4)
chk("Q4c U+W = M2x2", Sm.rank() == 4)
ns = sp.Matrix.hstack(e11, sy, e22, -u1, -u2).nullspace()
chk("Q4c system for intersection has 1-dim solution (d1=-d2)", len(ns) == 1 and ns[0][3] == -ns[0][4], str(list(ns[0])))
chk("Q4c dim(U cap W)=2+3-4=1", 2 + 3 - 4 == 1)
v = V([-1, 2, 2, 1])
chk("Q4c (-1,2;2,1) = u1-u2", v == u1 - u2)
chk("Q4c (-1,2;2,1) is symmetric and in U", v[1] == v[2] and sp.Matrix.hstack(u1, u2, v).rank() == 2)
chk("Q4c official line: -u1+u2 = (1,-2;-2,-1) = -(official v) (sign slip in the official arithmetic)", -u1 + u2 == -v)
chk("Q4c system matrix reduces as printed", sp.Matrix([[1, 0, 0, -1, -2], [0, 1, 0, -2, 0], [0, 1, 0, 1, 3], [0, 0, 1, -3, -2]]).rref()[0] ==
    sp.Matrix([[1, 0, 0, -1, -2], [0, 1, 0, -2, 0], [0, 0, 1, -3, -2], [0, 0, 0, 1, 1]]).rref()[0])
q = V([1, 0, -1, 1])
chk("Q4d (1,0;-1,1) not in U cap W (not a multiple of the basis, not symmetric)", sp.Matrix.hstack(q, v).rank() == 2 and q[1] != q[2])

# ---- Q5.1 T: M2x2 -> R^4
aa, bb, cc, dd = sp.symbols("aa bb cc dd")
Tm = sp.Matrix([[1, 1, 1, 1], [2, 0, 2, 5], [3, 1, 3, 6], [6, 2, 6, 12]])
img = list(Tm * V([aa, bb, cc, dd]))
chk("Q5a matrix reproduces the formula", img == [aa + bb + cc + dd, 2 * aa + 2 * cc + 5 * dd, 3 * aa + bb + 3 * cc + 6 * dd, 6 * aa + 2 * bb + 6 * cc + 12 * dd])
chk("Q5a columns T(E1..E4) as printed", [list(Tm[:, i]) for i in range(4)] == [[1, 2, 3, 6], [1, 0, 1, 2], [1, 2, 3, 6], [1, 5, 6, 12]])
T1 = Tm.copy(); T1[1, :] -= 2 * T1[0, :]; T1[2, :] -= 3 * T1[0, :]; T1[3, :] -= 6 * T1[0, :]
chk("Q5a step 1", T1 == sp.Matrix([[1, 1, 1, 1], [0, -2, 0, 3], [0, -2, 0, 3], [0, -4, 0, 6]]))
chk("Q5a rank 2, pivots columns 1,2", Tm.rank() == 2 and Tm.rref()[1] == (0, 1))
chk("Q5a Im basis (1,2,3,6),(1,0,1,2)", sp.Matrix.hstack(Tm[:, 0], Tm[:, 1]).rank() == 2 == Tm.rank())
kvs = [V([-1, 0, 1, 0]), V([R(-5, 2), R(3, 2), 0, 1])]
chk("Q5a ker basis (-1,0,1,0),(-5/2,3/2,0,1)", all(Tm * k == sp.zeros(4, 1) for k in kvs) and len(Tm.nullspace()) == 2 and sp.Matrix.hstack(*kvs).rank() == 2)
chk("Q5a rref of T as printed", Tm.rref()[0] == sp.Matrix([[1, 0, 1, R(5, 2)], [0, 1, 0, R(-3, 2)], [0, 0, 0, 0], [0, 0, 0, 0]]))
chk("Q5b not injective, not onto", len(Tm.nullspace()) == 2 and Tm.rank() == 2 and Tm.rank() != 4)
mm = sp.symbols("mm")
cm = sp.Matrix([[1, 1, 11], [2, 0, 2], [3, 1, 13], [6, 2, mm]])
chk("Q5c m=26 (rank test)", cm.subs(mm, 26).rank() == 2 and cm.subs(mm, 25).rank() == 3)
chk("Q5c (11,2,13,26) = 1*(1,2,3,6)+10*(1,0,1,2)", V([1, 2, 3, 6]) + 10 * V([1, 0, 1, 2]) == V([11, 2, 13, 26]))
c = cm.copy(); c[1, :] -= 2 * c[0, :]; c[2, :] -= 3 * c[0, :]; c[3, :] -= 6 * c[0, :]
chk("Q5c step 1", c == sp.Matrix([[1, 1, 11], [0, -2, -20], [0, -2, -20], [0, -4, mm - 66]]))
c[2, :] -= c[1, :]; c[3, :] -= 2 * c[1, :]
chk("Q5c step 2: m-26", c == sp.Matrix([[1, 1, 11], [0, -2, -20], [0, 0, 0], [0, 0, mm - 26]]))

# ---- Q5.2 change of basis in R1[x]
EB = sp.Matrix([[1, 2], [3, 4]])
EC = sp.Matrix([[1, 3], [4, 8]])
chk("Q5d inverse of C-matrix = -1/4 [[8,-3],[-4,1]]", EC.inv() == -R(1, 4) * sp.Matrix([[8, -3], [-4, 1]]))
res = EC.inv() * EB
chk("Q5d [I]_C^B = [[1/4,-1],[1/4,1]]", res == sp.Matrix([[R(1, 4), -1], [R(1, 4), 1]]))
chk("Q5d -1/4 [[8,-3],[-4,1]] [[1,2],[3,4]] = -1/4 [[-1,4],[-1,-4]]", -R(1, 4) * sp.Matrix([[8, -3], [-4, 1]]) * EB == -R(1, 4) * sp.Matrix([[-1, 4], [-1, -4]]))
chk("Q5d [p]_C = (-20, 30)", res * V([20, 25]) == V([-20, 30]))
chk("Q5d check: C-coordinates (-20,30) give the same polynomial as B-coordinates (20,25)", EC * V([-20, 30]) == EB * V([20, 25]))

# ---- Q6 (no official solution; solved by the solver) ----
_h, _d = sp.symbols("h d", real=True, nonzero=True)
chk("Q6a det: h*d^2 = d^3/h with d!=0 gives d = h^2", sp.solve(sp.Eq(_h * _d**2, _d**3 / _h), _d) == [_h**2])
_H = sp.Matrix([[0, 1], [2, 0]]); _D = 2 * sp.eye(2)
chk("Q6a model H^2=2I, D=2I satisfies HD^2 = D^3 H^-1 and det D > 0", _H * _D**2 == _D**3 * _H.inv() and _D.det() == _H.det() ** 2 > 0)
_A = sp.Matrix([[2, 1], [0, 3]])
chk("Q6b A^-1 has eigenpairs (1/lam, u)", all(_A.inv() * v[0] == v[0] / lam for lam, _m, vs in _A.eigenvects() for v in [vs]))
_B = sp.eye(2); _C = -sp.eye(2)
chk("Q6c BC invertible, B+C=0 singular, 0*C singular", (_B * _C).det() != 0 and (_B + _C).det() == 0 and (0 * _C).det() == 0)
_B2 = sp.Matrix([[1, 2], [3, 5]]); _C2 = sp.Matrix([[2, 1], [7, 4]])
chk("Q6c det(BC)=det B det C", (_B2 * _C2).det() == _B2.det() * _C2.det() != 0)

print("")
print("TOTAL MISMATCHES:", len(bad))
assert not bad, bad
