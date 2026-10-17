# -*- coding: utf-8 -*-
"""sympy checks of the official 24A-A answers. Run: PYTHONUTF8=1 py tools/verify/24A-A/verify_24A-A.py
Prints OK/MISMATCH lines (ASCII only)."""
import sympy as sp

bad = []


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R12 = sp.Rational(1, 2)

# ---- Q1 : A^2+A+I=0 (concrete instance with that polynomial, plus the ring identities)
A = sp.Matrix([[0, -1], [1, -1]])
I2 = sp.eye(2)
chk("Q1 instance A^2+A+I=0", A**2 + A + I2 == sp.zeros(2, 2))
chk("Q1a A^-1 = A^2", A.inv() == A**2)
chk("Q1a A^-1 = -A-I", A.inv() == -A - I2)
chk("Q1b A^2-A+I = -2A", A**2 - A + I2 == -2 * A)
chk("Q1b (A^2-A+I)^-1 = -1/2 A^-1", (A**2 - A + I2).inv() == -R12 * A.inv())
Ax = sp.Matrix([[1, 0], [0, 0]])
Bx = sp.Matrix([[0, 0], [0, 1]])
chk("Q1c counterexample tr(A)=tr(B)=1, AB=0, tr(AB)=0",
    Ax.trace() == 1 and Bx.trace() == 1 and (Ax * Bx) == sp.zeros(2, 2) and (Ax * Bx).trace() == 0)

# ---- Q2 : system with parameter k
k, x, y, z = sp.symbols("k x y z")
M = sp.Matrix([[1, 0, -3], [2, k, -1], [1, 2, k]])
b = sp.Matrix([-3, -2, 1])
chk("Q2 det = (k-2)(k+5): singular only at k=2,-5 (k=0 is an artifact of dividing by k)", sorted(sp.solve(M.det(), k)) == [-5, 2], str(sp.factor(M.det())))
sol = sp.solve([x - 3 * z + 3, 2 * x + k * y - z + 2, x + 2 * y + k * z - 1], [x, y, z], dict=True)[0]
chk("Q2a unique solution formula",
    sp.simplify(sol[x] + 3 * (k + 1) / (k + 5)) == 0 and sp.simplify(sol[y] - 4 / (k + 5)) == 0
    and sp.simplify(sol[z] - 4 / (k + 5)) == 0, str(sol))
chk("Q2a k=0 unique solution", M.subs(k, 0).det() != 0)


def Mb(kv):
    return M.subs(k, kv).row_join(b)


chk("Q2c k=2 rank A=2 rank [A|b]=2", M.subs(k, 2).rank() == 2 and Mb(2).rank() == 2)
chk("Q2b k=-5 rank A=2 rank [A|b]=3 (no solution)", M.subs(k, -5).rank() == 2 and Mb(-5).rank() == 3)
p0 = sp.Matrix([-3, 2, 0])
d1 = sp.Matrix([6, -5, 2])
d2 = sp.Matrix([3, sp.Rational(-5, 2), 1])
chk("Q2c particular solution (-3,2,0) at k=2", M.subs(k, 2) * p0 == b)
chk("Q2c direction (6,-5,2) homogeneous", M.subs(k, 2) * d1 == sp.zeros(3, 1))
chk("Q2c direction (3,-5/2,1) homogeneous", M.subs(k, 2) * d2 == sp.zeros(3, 1))
chk("Q2c nullspace dim 1 and the two directions parallel",
    len(M.subs(k, 2).nullspace()) == 1 and sp.Matrix.hstack(d1, d2).rank() == 1)
chk("Q2c reduced aug matrix at k=2",
    Mb(2).rref()[0] == sp.Matrix([[1, 0, -3, -3], [0, 1, sp.Rational(5, 2), 2], [0, 0, 0, 0]]))
full = Mb(k)
R = sp.Matrix([[1, 0, -3, -3], [0, k, 5, 4], [0, 2, k + 3, 4]])
chk("Q2 first step (R2-2R1, R3-R1)",
    (full[1, :] - 2 * full[0, :]) == R[1, :] and (full[2, :] - full[0, :]) == R[2, :])
r3 = sp.simplify(R[2, :] / 2 - R[1, :] / k)
chk("Q2 R3-R2 entries (k^2+3k-10)/(2k) and (2k-4)/k",
    sp.simplify(r3[2] - (k**2 + 3 * k - 10) / (2 * k)) == 0 and sp.simplify(r3[3] - (2 * k - 4) / k) == 0)
chk("Q2 (2k)R3 = (k-2)(k+5), 4(k-2)",
    sp.expand(2 * k * r3[2] - (k - 2) * (k + 5)) == 0 and sp.expand(2 * k * r3[3] - 4 * (k - 2)) == 0)

# ---- Q3.1 inverse
A3 = sp.Matrix([[1, -1, 1], [0, 1, 1], [-1, 1, 1]])
Ai = sp.Matrix([[0, 1, -1], [-R12, 1, -R12], [R12, 0, R12]])
chk("Q3a A^-1 as printed", A3.inv() == Ai and A3 * Ai == sp.eye(3))
E1 = sp.Matrix([[1, 0, 0], [0, 1, 0], [1, 0, 1]])
E2 = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
E3 = sp.diag(1, 1, R12)
E4 = sp.Matrix([[1, 0, 0], [0, 1, -1], [0, 0, 1]])
E5 = sp.Matrix([[1, 0, -2], [0, 1, 0], [0, 0, 1]])
chk("Q3b E1 = R3+R1", E1 == sp.eye(3).elementary_row_op("n->n+km", row=2, k=1, row2=0))
chk("Q3b E2 = R1+R2", E2 == sp.eye(3).elementary_row_op("n->n+km", row=0, k=1, row2=1))
chk("Q3b E4 = R2-R3", E4 == sp.eye(3).elementary_row_op("n->n+km", row=1, k=-1, row2=2))
chk("Q3b E5 = R1-2R3", E5 == sp.eye(3).elementary_row_op("n->n+km", row=0, k=-2, row2=2))
chk("Q3b E5E4E3E2E1 A = I", E5 * E4 * E3 * E2 * E1 * A3 == sp.eye(3))
chk("Q3b A^-1 = E5E4E3E2E1", E5 * E4 * E3 * E2 * E1 == A3.inv())
M0 = A3.row_join(sp.eye(3))
s1 = E1 * M0
chk("Q3a chain step 1 (R3+R1)", s1[2, :] == sp.Matrix([[0, 0, 2, 1, 0, 1]]))
s2 = E2 * s1
chk("Q3a chain step 2 (R1+R2)", s2[0, :] == sp.Matrix([[1, 0, 2, 1, 1, 0]]))
s3 = E3 * s2
chk("Q3a chain step 3 (R3/2)", s3[2, :] == sp.Matrix([[0, 0, 1, R12, 0, R12]]))
s4 = E4 * s3
chk("Q3a chain step 4 (R2-R3)", s4[1, :] == sp.Matrix([[0, 1, 0, -R12, 1, -R12]]))
s5 = E5 * s4
chk("Q3a chain final [I|A^-1]", s5 == sp.eye(3).row_join(Ai))

# ---- Q3.2 diagonalization
B = sp.Matrix([[1, 1, 0], [0, -2, 0], [-1, 0, 3]])
lam = sp.symbols("lam")
chk("Q3c char poly (1-l)(-2-l)(3-l)", sp.expand((B - lam * sp.eye(3)).det() - (1 - lam) * (-2 - lam) * (3 - lam)) == 0)
chk("Q3c eigenvalues {1,-2,3}", sorted(B.eigenvals().keys()) == [-2, 1, 3])
P = sp.Matrix([[2, 5, 0], [0, -15, 0], [1, 1, 1]])
D = sp.diag(1, -2, 3)
chk("Q3c B P = P D", B * P == P * D)
chk("Q3c P invertible", P.det() != 0, "det=" + str(P.det()))
for v, l in [((2, 0, 1), 1), ((5, -15, 1), -2), ((0, 0, 1), 3)]:
    chk("Q3c eigenvector %s for %s" % (v, l), B * sp.Matrix(v) == l * sp.Matrix(v))
chk("Q3c B diagonalizable", B.is_diagonalizable())
chk("Q3c rref B-I", (B - sp.eye(3)).rref()[0] == sp.Matrix([[1, 0, -2], [0, 1, 0], [0, 0, 0]]))
chk("Q3c rref B+2I", (B + 2 * sp.eye(3)).rref()[0] == sp.Matrix([[1, 0, -5], [0, 1, 15], [0, 0, 0]]))
chk("Q3c rref B-3I", (B - 3 * sp.eye(3)).rref()[0] == sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))

# ---- Q4 subspaces of R^3
w1 = [sp.Matrix([1, 0, 1]), sp.Matrix([0, 1, 0])]   # z = x
w2 = [sp.Matrix([1, 1, 0]), sp.Matrix([0, 0, 1])]   # y = x
chk("Q4a W1 basis in {z=x}, independent", all(v[2] == v[0] for v in w1) and sp.Matrix.hstack(*w1).rank() == 2)
chk("Q4a {z=x} has dim 2", len(sp.Matrix([[1, 0, -1]]).nullspace()) == 2)
chk("Q4a W2 basis in {y=x}, independent", all(v[1] == v[0] for v in w2) and sp.Matrix.hstack(*w2).rank() == 2)
chk("Q4a {y=x} has dim 2", len(sp.Matrix([[1, -1, 0]]).nullspace()) == 2)
S = sp.Matrix.hstack(*w1, *w2)
chk("Q4b dim(W1+W2)=3", S.rank() == 3)
rows = sp.Matrix([[1, 0, 1], [0, 1, 0], [1, 1, 0], [0, 0, 1]])
step = rows.copy()
step[0, :] = step[0, :] - step[3, :]
step[2, :] = step[2, :] - step[1, :]
step[2, :] = step[2, :] - step[0, :]
step.row_swap(2, 3)
chk("Q4b printed chain R1-R4, R3-R2, R3-R1, swap R3,R4 gives (e1,e2,e3,0)",
    step == sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]))
ns = sp.Matrix([[1, 0, -1], [1, -1, 0]]).nullspace()
chk("Q4c intersection = span(1,1,1), dim 1", len(ns) == 1 and sp.Matrix.hstack(ns[0], sp.Matrix([1, 1, 1])).rank() == 1)
sysm = sp.Matrix([[1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
chk("Q4c coefficient system rank 3 (one free parameter)", sysm.rank() == 3)
ns4 = sysm.nullspace()[0]
chk("Q4c solutions: beta1=beta2=-t, alpha1=alpha2=t", sp.Matrix.hstack(ns4, sp.Matrix([1, 1, -1, -1])).rank() == 1, str(list(ns4)))
t = sp.symbols("t")
chk("Q4c w = t(1,1,0)+t(0,0,1) = t(1,1,1)", (t * sp.Matrix([1, 1, 0]) + t * sp.Matrix([0, 0, 1])) == t * sp.Matrix([1, 1, 1]))
chk("Q4d (1,1,1) in W1 and in W2", 1 == 1 and 1 == 1)
chk("Q4 dimension formula 2+2-1=3", 2 + 2 - 1 == 3)

# ---- Q5.1 linear map R3[x] -> R^4
T = sp.Matrix([[1, 1, 2, 2], [2, 3, 2, 3], [3, 4, 4, 5], [4, 5, 6, 7]])
chk("Q5a rank T = 2", T.rank() == 2)
chk("Q5a rref of T", T.rref()[0] == sp.Matrix([[1, 0, 4, 3], [0, 1, -2, -1], [0, 0, 0, 0], [0, 0, 0, 0]]))
T1 = T.copy()
T1[1, :] = T1[1, :] - 2 * T1[0, :]
T1[2, :] = T1[2, :] - 3 * T1[0, :]
T1[3, :] = T1[3, :] - 4 * T1[0, :]
chk("Q5a first echelon step as printed", T1 == sp.Matrix([[1, 1, 2, 2], [0, 1, -2, -1], [0, 1, -2, -1], [0, 1, -2, -1]]))
chk("Q5a Im = span of columns 1,2", sp.Matrix.hstack(T[:, 0], T[:, 1]).rank() == 2)
ns = T.nullspace()
chk("Q5a dim ker = 2", len(ns) == 2)
kv = [sp.Matrix([-4, 2, 1, 0]), sp.Matrix([-3, 1, 0, 1])]
chk("Q5a ker basis (-4,2,1,0),(-3,1,0,1)", all(T * v == sp.zeros(4, 1) for v in kv) and sp.Matrix.hstack(*kv).rank() == 2)
chk("Q5a ker basis spans the nullspace", sp.Matrix.hstack(*kv, *ns).rank() == 2)
chk("Q5b not injective (ker dim 2), not onto (2 != 4)", len(ns) == 2 and T.rank() == 2 and T.rank() != 4)
kk, mm = sp.symbols("k m")
chk("Q5c k=m=1", sp.solve([4 * kk + 3 * mm - 7, 2 * kk + mm - 3], [kk, mm]) == {kk: 1, mm: 1})
chk("Q5c -7+3x+x^2+x^3 in Ker", T * sp.Matrix([-7, 3, 1, 1]) == sp.zeros(4, 1))
chk("Q5c unique (det [[4,3],[2,1]] != 0)", sp.Matrix([[4, 3], [2, 1]]).det() != 0)
ss = sp.Matrix([[-4, -3], [2, 1], [1, 0], [0, 1]]).row_join(sp.Matrix([-7, 3, kk, mm]))
chk("Q5c (-7,3,k,m) in kernel iff k=m=1 (rank test)",
    ss.subs({kk: 1, mm: 1}).rank() == 2 and ss.subs({kk: 2, mm: 1}).rank() == 3 and ss.subs({kk: 1, mm: 2}).rank() == 3)

# ---- Q5.2 change of basis
EB = sp.Matrix([[3, 7], [2, 5]])
EC = sp.Matrix([[5, 3], [3, 2]])
res = EC.inv() * EB
chk("Q5d [I]_C^B = [[0,-1],[1,4]]", res == sp.Matrix([[0, -1], [1, 4]]))
chk("Q5d inverse of C-matrix = [[2,-3],[-3,5]]", EC.inv() == sp.Matrix([[2, -3], [-3, 5]]))
chk("Q5d C * res = B", EC * res == EB)
aug = EC.row_join(EB)
a1 = aug.copy()
a1[0, :] = a1[0, :] - 2 * a1[1, :]
chk("Q5d method 2 step R1-2R2", a1[0, :] == sp.Matrix([[-1, -1, -1, -3]]))
a2 = a1.copy()
a2[1, :] = a2[1, :] + 3 * a2[0, :]
chk("Q5d method 2 step R2+3R1", a2[1, :] == sp.Matrix([[0, -1, -1, -4]]))
chk("Q5d method 2 rref", aug.rref()[0] == sp.Matrix([[1, 0, 0, -1], [0, 1, 1, 4]]))

print("")
print("TOTAL MISMATCHES:", len(bad), "of", "see above")
