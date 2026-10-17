# -*- coding: utf-8 -*-
"""sympy checks of the official 25A-B answers. Run: PYTHONUTF8=1 py tools/verify/25A-B/verify_25A-B.py
Prints OK/MISMATCH lines (ASCII only). Q4 has no official solution; the solver's answers are checked at the end."""
import sympy as sp

bad = []


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational
k, a, s, t, x, y, z = sp.symbols("k a s t x y z")

# ---- Q1 : two planes
N1 = sp.Matrix([-k**2, -1, k + 1])
N2 = sp.Matrix([1, k, 2 * k - 3])
chk("Q1a N1.N2 = k^2-2k-3", sp.expand(N1.dot(N2) - (k**2 - 2 * k - 3)) == 0)
chk("Q1a roots {-1,3}", sorted(sp.solve(N1.dot(N2), k)) == [-1, 3])
S1 = lambda X, Y, Z: -k**2 * X - Y + (k + 1) * Z - 2
S2 = lambda X, Y, Z: X + k * Y + (2 * k - 3) * Z - 1
chk("Q1b S1 at k=-1: -x-y=2", sp.expand(S1(x, y, z).subs(k, -1) - (-x - y - 2)) == 0)
chk("Q1b S2 at k=-1: x-y-5z=1", sp.expand(S2(x, y, z).subs(k, -1) - (x - y - 5 * z - 1)) == 0)
Aug = sp.Matrix([[-1, -1, 0, 2], [1, -1, -5, 1]])
step = Aug.copy()
step[1, :] = step[1, :] + step[0, :]
chk("Q1b R2+R1 -> (0,-2,-5|3)", step[1, :] == sp.Matrix([[0, -2, -5, 3]]))
step[0, :] = 2 * Aug[0, :] - step[1, :]
chk("Q1b 2R1-R2 -> (-2,0,5|1)", step[0, :] == sp.Matrix([[-2, 0, 5, 1]]))
chk("Q1b rref", Aug.rref()[0] == sp.Matrix([[1, 0, R(-5, 2), R(-1, 2)], [0, 1, R(5, 2), R(-3, 2)]]))
line = sp.Matrix([R(-1, 2), R(-3, 2), 0]) + t * sp.Matrix([R(5, 2), R(-5, 2), 1])
chk("Q1b line lies in both planes", sp.simplify(S1(*line).subs(k, -1)) == 0 and sp.simplify(S2(*line).subs(k, -1)) == 0)
chk("Q1b p0=(12,-14,5) on both planes", S1(12, -14, 5).subs(k, -1) == 0 and S2(12, -14, 5).subs(k, -1) == 0)
chk("Q1b p0 at t=5", list(line.subs(t, 5)) == [12, -14, 5])
n1 = sp.Matrix([-1, -1, 0]); n2 = sp.Matrix([1, -1, -5])
chk("Q1c normals at k=-1", list(N1.subs(k, -1)) == list(n1) and list(N2.subs(k, -1)) == list(n2))
chk("Q1c planes perpendicular (n1.n2=0)", n1.dot(n2) == 0)
chk("Q1c normals independent (valid direction vectors of S3)", sp.Matrix.hstack(n1, n2).rank() == 2)
dirL = n1.cross(n2)
chk("Q1c S3 normal = n1 x n2 is perpendicular to n1 and n2 (so S3 contains directions n1, n2)", dirL.dot(n1) == 0 and dirL.dot(n2) == 0)
chk("Q1c S3 direction of S1 normal is parallel to S2 (n1.n2=0)", n1.dot(n2) == 0)

# ---- Q2 : homogeneous system
M = sp.Matrix([[a, a, -1], [a**2, a, a**2 - a], [a, a, 2 * a + 1]])
E = M.copy()
E[1, :] = E[1, :] - a * E[0, :]
E[2, :] = E[2, :] - E[0, :]
chk("Q2a first step", sp.simplify(E - sp.Matrix([[a, a, -1], [0, a - a**2, a**2], [0, 0, 2 * a + 2]])) == sp.zeros(3, 3))
E2 = sp.Matrix([[a, a, -1], [0, 1, a / (1 - a)], [0, 0, 1]])
step2 = sp.Matrix([[a, a, -1], [0, (a - a**2) / (a * (1 - a)), a**2 / (a * (1 - a))], [0, 0, (2 * a + 2) / (2 * (a + 1))]])
chk("Q2a normalised echelon form", sp.simplify(step2 - E2) == sp.zeros(3, 3))
for av, rk in [(0, 1), (1, 2), (-1, 2), (2, 3), (5, 3), (R(1, 2), 3)]:
    chk("Q2 rank at a=%s is %s" % (av, rk), M.subs(a, av).rank() == rk)
chk("Q2b trivial only iff a not in {0,1,-1}", sorted(sp.solve(M.det(), a)) == [-1, 0, 1], str(sp.factor(M.det())))
M0 = sp.Matrix([[0, 0, -1], [0, 0, 0], [0, 0, 2]])
chk("Q2 a=0 reduced (R3+2R1) = (0 0 -1; 0 0 0; 0 0 0)", sp.Matrix([[0, 0, -1], [0, 0, 0], [0, 0, 2 + 2 * (-1)]]) == sp.Matrix([[0, 0, -1], [0, 0, 0], [0, 0, 0]]))
chk("Q2 a=0 nullspace = {(x,y,0)}", len(M.subs(a, 0).nullspace()) == 2 and all(v[2] == 0 for v in M.subs(a, 0).nullspace()))
ns = M.subs(a, -1).nullspace()
chk("Q2 a=-1 nullspace span (-3,1,2)", len(ns) == 1 and sp.Matrix.hstack(ns[0], sp.Matrix([-3, 1, 2])).rank() == 1)
chk("Q2 a=-1 echelon (-1 -1 -1; 0 -2 1; 0 0 0)", E.subs(a, -1) == sp.Matrix([[-1, -1, -1], [0, -2, 1], [0, 0, 0]]))
ns = M.subs(a, 1).nullspace()
chk("Q2 a=1 nullspace span (1,-1,0)", len(ns) == 1 and sp.Matrix.hstack(ns[0], sp.Matrix([1, -1, 0])).rank() == 1)
chk("Q2 a=1 echelon (1 1 -1; 0 0 1; 0 0 4) -> R3-4R2", E.subs(a, 1) == sp.Matrix([[1, 1, -1], [0, 0, 1], [0, 0, 4]]))

# ---- Q3.1 inverse as product of elementaries
A = sp.Matrix([[1, 1, 1], [2, 3, 2], [3, 8, 2]])
Ai = sp.Matrix([[10, -6, 1], [-2, 1, 0], [-7, 5, -1]])
chk("Q3a A^-1 as printed", A.inv() == Ai and A * Ai == sp.eye(3))
M0 = A.row_join(sp.eye(3))
c1 = M0.copy(); c1[1, :] -= 2 * c1[0, :]; c1[2, :] -= 3 * c1[0, :]
chk("Q3a step R2-2R1,R3-3R1", c1 == sp.Matrix([[1, 1, 1, 1, 0, 0], [0, 1, 0, -2, 1, 0], [0, 5, -1, -3, 0, 1]]))
c2 = c1.copy(); c2[0, :] -= c2[1, :]; c2[2, :] -= 5 * c2[1, :]
chk("Q3a step R1-R2,R3-5R2", c2 == sp.Matrix([[1, 0, 1, 3, -1, 0], [0, 1, 0, -2, 1, 0], [0, 0, -1, 7, -5, 1]]))
c3 = c2.copy(); c3[2, :] = -c3[2, :]
chk("Q3a step -R3", c3 == sp.Matrix([[1, 0, 1, 3, -1, 0], [0, 1, 0, -2, 1, 0], [0, 0, 1, -7, 5, -1]]))
c4 = c3.copy(); c4[0, :] -= c4[2, :]
chk("Q3a step R1-R3 -> [I|A^-1]", c4 == sp.eye(3).row_join(Ai))
F1 = sp.Matrix([[1, 0, -1], [0, 1, 0], [0, 0, 1]])
F2 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
F3 = sp.Matrix([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
F4 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, -5, 1]])
F5 = sp.Matrix([[1, 0, 0], [0, 1, 0], [-3, 0, 1]])
F6 = sp.Matrix([[1, 0, 0], [-2, 1, 0], [0, 0, 1]])
chk("Q3a A^-1 = F1 F2 F3 F4 F5 F6 (as printed, six factors)", F1 * F2 * F3 * F4 * F5 * F6 == Ai)
chk("Q3a F6 A... product times A = I", F1 * F2 * F3 * F4 * F5 * F6 * A == sp.eye(3))
chk("Q3a each factor is elementary (det +-1)", all(abs(F.det()) == 1 for F in (F1, F2, F3, F4, F5, F6)))

# ---- Q3.2 diagonalization of all-ones matrix
B = sp.ones(3, 3)
lam = sp.symbols("lam")
chk("Q3b char poly = 3 lam^2 - lam^3", sp.expand((B - lam * sp.eye(3)).det() - (3 * lam**2 - lam**3)) == 0)
chk("Q3b eigenvalues 0 (x2), 3", B.eigenvals() == {0: 2, 3: 1})
P = sp.Matrix([[1, -1, -1], [1, 1, 0], [1, 0, 1]])
D = sp.diag(3, 0, 0)
chk("Q3b B P = P D", B * P == P * D)
chk("Q3b B P as printed (3 0 0 rows)", B * P == sp.Matrix([[3, 0, 0], [3, 0, 0], [3, 0, 0]]))
chk("Q3b P invertible", P.det() != 0, "det=%s" % P.det())
for v, l in [((-1, 1, 0), 0), ((-1, 0, 1), 0), ((1, 1, 1), 3)]:
    chk("Q3b eigenvector %s for %s" % (v, l), B * sp.Matrix(v) == l * sp.Matrix(v))
chk("Q3b eigenspace of 0 is x+y+z=0 (dim 2)", len((B).nullspace()) == 2)
chk("Q3b rref of B-3I has pivots 2, nullity 1", (B - 3 * sp.eye(3)).rank() == 2)
chk("Q3b B diagonalizable", B.is_diagonalizable())

# ---- Q5.1 T: M2x2 -> R3[x]
Tm = sp.Matrix([[1, 1, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 5, 5]])
aa, bb, cc, dd = sp.symbols("aa bb cc dd")
img = Tm * sp.Matrix([aa, bb, cc, dd])
chk("Q5a matrix reproduces the formula", list(img) == [aa + bb + cc + dd, aa + bb + 2 * cc + 2 * dd, 2 * aa + 2 * bb + 3 * cc + 3 * dd, 3 * aa + 3 * bb + 5 * cc + 5 * dd])
T1 = Tm.copy(); T1[1, :] -= T1[0, :]; T1[2, :] -= 2 * T1[0, :]; T1[3, :] -= 3 * T1[0, :]
chk("Q5a step 1", T1 == sp.Matrix([[1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 2, 2]]))
chk("Q5a echelon form", Tm.rref()[0] == sp.Matrix([[1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]))
chk("Q5a rank 2 pivots in columns 1,3", Tm.rank() == 2 and Tm.rref()[1] == (0, 2))
chk("Q5a Im basis 1+x+2x^2+3x^3, 1+2x+3x^2+5x^3", list(Tm[:, 0]) == [1, 1, 2, 3] and list(Tm[:, 2]) == [1, 2, 3, 5])
kv = [sp.Matrix([-1, 1, 0, 0]), sp.Matrix([0, 0, -1, 1])]
chk("Q5a ker basis in M2x2", all(Tm * v == sp.zeros(4, 1) for v in kv) and len(Tm.nullspace()) == 2)
chk("Q5b not injective, not onto", len(Tm.nullspace()) == 2 and Tm.rank() == 2 and Tm.rank() != 4)
Cm = sp.Matrix([[1, 1], [1, 2], [2, 3], [3, 5]])
kk, mm = sp.symbols("kk mm")
cm = Cm.row_join(sp.Matrix([4, 6, kk, mm]))
chk("Q5c rank test: k=10,m=16 in Im", cm.subs({kk: 10, mm: 16}).rank() == 2 and cm.subs({kk: 9, mm: 16}).rank() == 3 and cm.subs({kk: 10, mm: 15}).rank() == 3)
chk("Q5c 2*col1+2*col2 = (4,6,10,16)", 2 * Cm[:, 0] + 2 * Cm[:, 1] == sp.Matrix([4, 6, 10, 16]))
c = cm.copy(); c[1, :] -= c[0, :]; c[2, :] -= 2 * c[0, :]; c[3, :] -= 3 * c[0, :]
chk("Q5c step 1", c == sp.Matrix([[1, 1, 4], [0, 1, 2], [0, 1, kk - 8], [0, 2, mm - 12]]))
c[2, :] -= c[1, :]; c[3, :] -= 2 * c[1, :]
chk("Q5c step 2: k-10, m-16", c == sp.Matrix([[1, 1, 4], [0, 1, 2], [0, 0, kk - 10], [0, 0, mm - 16]]))

# ---- Q5.2 change of basis in R1[x]
EB = sp.Matrix([[20, 25], [20, 24]])
EC = sp.Matrix([[1, 3], [3, 10]])
chk("Q5d inverse of C-matrix [[10,-3],[-3,1]]", EC.inv() == sp.Matrix([[10, -3], [-3, 1]]))
chk("Q5d [I]_C^B = [[140,178],[-40,-51]]", EC.inv() * EB == sp.Matrix([[140, 178], [-40, -51]]))
chk("Q5d C*res = B", EC * sp.Matrix([[140, 178], [-40, -51]]) == EB)
aug = EC.row_join(EB)
r1 = aug.copy(); r1[1, :] -= 3 * r1[0, :]
chk("Q5d method 2 step R2-3R1", r1 == sp.Matrix([[1, 3, 20, 25], [0, 1, -40, -51]]))
r1[0, :] -= 3 * r1[1, :]
chk("Q5d method 2 step R1-3R2", r1 == sp.Matrix([[1, 0, 140, 178], [0, 1, -40, -51]]))

# ---- Q4 (no official solution; solved by the solver). coords (a,b,c,d) of ax^3+bx^2+cx+d ----
_x = sp.symbols("x")
def _co(p):
    p = sp.Poly(p, _x)
    return sp.Matrix([[p.coeff_monomial(_x**k) for k in (3, 2, 1, 0)]])
def _inW1(p):
    return sp.simplify(p.subs(_x, 0) - sp.diff(p, _x).subs(_x, 0)) == 0 and sp.simplify(sp.diff(p, _x).subs(_x, 0) - sp.diff(p, _x, 2).subs(_x, 0)) == 0
def _inW2(p):
    return sp.diff(p, _x).subs(_x, 0) == 0
_aa, _bb, _cc, _dd = sp.symbols("aa bb cc dd")
_gen = _aa * _x**3 + _bb * _x**2 + _cc * _x + _dd
_cond1 = [_gen.subs(_x, 0) - sp.diff(_gen, _x).subs(_x, 0), sp.diff(_gen, _x).subs(_x, 0) - sp.diff(_gen, _x, 2).subs(_x, 0)]
chk("Q4a W1 basis x^3, x^2+2x+2 in W1; dim W1 = 4-2 = 2", _inW1(_x**3) and _inW1(_x**2 + 2 * _x + 2) and sp.Matrix([[sp.diff(e, v) for v in (_aa, _bb, _cc, _dd)] for e in _cond1]).rank() == 2)
chk("Q4a W2 basis x^3, x^2, 1; dim 3", all(_inW2(p) for p in (_x**3, _x**2, sp.Integer(1) + 0 * _x)))
_S = sp.Matrix.vstack(_co(_x**3), _co(_x**2 + 2 * _x + 2), _co(_x**2), _co(1 + 0 * _x**3))
chk("Q4b W1+W2 = R3[x] (rank 4)", _S.rank() == 4)
chk("Q4c W1 cap W2 = span x^3: general W1 elt in W2 iff b=0", sp.solve(sp.diff(_aa * _x**3 + _bb * (_x**2 + 2 * _x + 2), _x).subs(_x, 0), _bb) == [0] and 2 + 3 - 4 == 1)
_Q = _x**3 + 2 * _x**2 + 3
chk("Q4d Q in W1+W2, coords (1,2,0,3), Q in W2 itself", _co(_Q) == sp.Matrix([[1, 2, 0, 3]]) and _inW2(_Q))
chk("Q4b row ops", sp.Matrix([[0, 1, 2, 2]]) - sp.Matrix([[0, 1, 0, 0]]) - 2 * sp.Matrix([[0, 0, 0, 1]]) == sp.Matrix([[0, 0, 2, 0]]))

print("")
print("TOTAL MISMATCHES:", len(bad))
assert not bad, bad
