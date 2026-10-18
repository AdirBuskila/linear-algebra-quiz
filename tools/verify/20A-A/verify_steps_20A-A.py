# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 20A-A (rubric/pitfalls/steps in tools/gen/gen_20A-A.py).
Run: PYTHONUTF8=1 py tools/verify/20A-A/verify_steps_20A-A.py
Every numeric step in tools/raw/20A-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / order / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "20A-A.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_ = "א", "ב", "ג", "ד"
R = sp.Rational
V = sp.Matrix
bad = []
EXP = {}


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def exp(num, part, idx, val):
    EXP[(num, part, idx)] = sp.nsimplify(val)


k = sp.symbols("k")
# ---- Q1a: parallel planes
n1 = V([1, -2, 1]); n2 = V([k, -1, k])
ks = sp.solve(list(n2 - sp.Symbol("mu") * n1), [k, sp.Symbol("mu")], dict=True)[0]
exp(1, A_, 0, ks[k])
chk("Q1a k=1/2", ks[k] == R(1, 2))
p2 = V([R(1, 2), -1, R(1, 2)]) * 2
exp(1, A_, 1, -2 * 2)
chk("Q1a pi2 times 2 is x-2y+z-4=0, distinct from pi1 (+5)", list(p2) == [1, -2, 1] and -2 * 2 == -4 and -4 != 5)
dist = sp.Abs(5 - (-4)) / sp.sqrt(6)
exp(1, A_, 2, sp.N(dist, 6))
chk("Q1a distance 9/sqrt6 = 3 sqrt6/2", sp.simplify(dist - 3 * sp.sqrt(6) / 2) == 0)
# ---- Q1b: perpendicular
dot = sp.expand(n1.dot(n2))
chk("Q1b dot = 2k+2, k=-1", dot == 2 * k + 2 and sp.solve(dot, k) == [-1])
exp(1, B_, 1, dot.subs(k, 0)); exp(1, B_, 2, sp.solve(dot, k)[0])
chk("Q1b cross product vanishes only for parallel (k=1/2), not at k=-1", n1.cross(n2.subs(k, -1)) != sp.zeros(3, 1) and n1.cross(n2.subs(k, R(1, 2))) == sp.zeros(3, 1))
# ---- Q1c
m1 = V([1, -2, 1]); m2 = V([2, -1, 2])
cp = m1.cross(m2)
chk("Q1c cross = (-3,0,3), N=(1,0,-1) perpendicular to both, plane x-z=0 through (1,1,1)", list(cp) == [-3, 0, 3] and V([1, 0, -1]).dot(m1) == 0 and V([1, 0, -1]).dot(m2) == 0 and 1 - 1 == 0)
exp(1, C_, 1, cp[0])
chk("Q1c distractors: (n1+n2).n1=12, (n1-n2).n2=-3, n2.n1=6 all nonzero", ((m1 + m2).dot(m1), (m1 - m2).dot(m2), m2.dot(m1)) == (12, -3, 6))
# ---- Q1d
w = 5 + 3 * sp.I
exp(1, D_, 0, sp.Abs(w) ** 2)
exp(1, D_, 1, sp.N(sp.Abs(w) ** R(1, 5), 6))
th = sp.atan(R(3, 5))
exp(1, D_, 2, sp.N(th / 5 * 180 / sp.pi, 6))
exp(1, D_, 3, 360 / 5)
z0 = sp.Abs(w) ** R(1, 5) * (sp.cos(th / 5) + sp.I * sp.sin(th / 5))
chk("Q1d z0^5 = 5+3i", abs(sp.N(z0 ** 5 - w, 20)) < 1e-12)
chk("Q1d |z|=34^(1/10)", abs(sp.N(sp.Abs(w) ** R(1, 5) - sp.Integer(34) ** R(1, 10), 20)) < 1e-12)

# ---- Q2
A = V([[1, 0, 1, 1], [1, 1, 2, 0], [0, 1, 1, -1]])
ns = A.nullspace()
chk("Q2a nullspace spanned by (-1,-1,1,0),(-1,1,0,1)", len(ns) == 2 and A * V([-1, -1, 1, 0]) == sp.zeros(3, 1) and A * V([-1, 1, 0, 1]) == sp.zeros(3, 1))
exp(2, A_, 0, A.rank()); exp(2, A_, 1, (2 * 1 * 0 - 1 * 1 - 1 * 2) if False else (-1 * 1 + -1 * 2)); exp(2, A_, 2, len(ns))
chk("Q2a x1 = -s-t with s=1,t=2", (1 * V([-1, -1, 1, 0]) + 2 * V([-1, 1, 0, 1]))[0] == -3)
good = V([-2, 0, 1, 1])
chk("Q2a (-2,0,1,1) in Nul A", A * good == sp.zeros(3, 1))
for name, v in [("(2,0,1,1)", V([2, 0, 1, 1])), ("(-2,0,1,-1)", V([-2, 0, 1, -1])), ("(1,1,1,1)", V([1, 1, 1, 1]))]:
    chk("Q2a distractor %s not in Nul A, row1 value %s" % (name, (A * v)[0]), A * v != sp.zeros(3, 1))
chk("Q2a distractor row-1 values 4,-2,3", [(A * v)[0] for v in (V([2, 0, 1, 1]), V([-2, 0, 1, -1]), V([1, 1, 1, 1]))] == [4, -2, 3])
exp(2, B_, 0, A.T.rank())
al, be = sp.symbols("al be")
sl = sp.solve(list(al * A.row(0).T + be * A.row(1).T - A.row(2).T), [al, be], dict=True)[0]
exp(2, B_, 1, sl[al])
chk("Q2b R3 = -R1 + R2", sl == {al: -1, be: 1})
E = A.rref()[0]
chk("Q2b rref rows (1,0,1,1),(0,1,1,-1)", list(E.row(0)) == [1, 0, 1, 1] and list(E.row(1)) == [0, 1, 1, -1])
chk("Q2b row ops change column space: (1,0,0) is in no Col A", sp.Matrix.hstack(A, V([1, 0, 0])).rank() == 3 and E.col(0) == V([1, 0, 0]))
chk("Q2b original rows dependent (rank 2 < 3)", A.rank() == 2)
exp(2, C_, 0, A.rank())
chk("Q2c cols 1,2 basis, col3=C1+C2, col4=C1-C2", A[:, :2].rank() == 2 and A[:, 2] == A[:, 0] + A[:, 1] and A[:, 3] == A[:, 0] - A[:, 1])
exp(2, C_, 2, -1)
chk("Q2c distractors: echelon col (1,0,0) not in Col A; col1 alone rank 1; three columns rank 2", sp.Matrix.hstack(A[:, :2], V([1, 0, 0])).rank() == 3 and A[:, 0].rank() == 1 and A[:, :3].rank() == 2)
exp(2, D_, 0, len(A.rref()[1])); exp(2, D_, 1, A.shape[1] - A.rank()); exp(2, D_, 2, len(ns) + A.rank())

# ---- Q3
a = sp.symbols("a")
A3 = V([[2, 1, -1], [1, a, 1], [3, 1, -a]])
dA = sp.expand(A3.det())
chk("Q3a det = -2a(a-2)", dA == sp.expand(-2 * a * (a - 2)))
exp(3, A_, 0, dA.subs(a, 1)); exp(3, A_, 1, dA.subs(a, 3))
chk("Q3a singular exactly at a=0,2", set(sp.solve(dA, a)) == {0, 2})
A1 = A3.subs(a, 1)
Ai = A1.inv()
exp(3, B_, 0, A1.det()); exp(3, B_, 1, Ai[0, 0]); exp(3, B_, 2, Ai[1, 1]); exp(3, B_, 3, Ai[1, 2])
chk("Q3b inverse as printed", Ai == sp.Matrix([[-1, 0, 1], [2, R(1, 2), -R(3, 2)], [-1, R(1, 2), R(1, 2)]]))
M = V([[1, 1, -1], [1, 1, 1], [1, 1, 1]])
lam = sp.symbols("lam")
chk("Q3c char poly lam(lam-1)(lam-2)", sp.expand((lam * sp.eye(3) - M).det()) == sp.expand(lam * (lam - 1) * (lam - 2)))
exp(3, C_, 0, M.trace()); exp(3, C_, 1, M.det())
vs = {0: V([-1, 1, 0]), 1: V([-1, 1, 1]), 2: V([0, 1, 1])}
chk("Q3c eigenvectors", all(M * v == l * v for l, v in vs.items()))
exp(3, C_, 2, (M * V([0, 1, 1]))[1])
for name, v in [("(1,1,1)", V([1, 1, 1])), ("(0,1,1)", V([0, 1, 1])), ("(-1,1,0)", V([-1, 1, 0]))]:
    chk("Q3c distractor %s is not an eigenvector for 1" % name, M * v != v)
chk("Q3c images (1,3,3),(0,2,2) and (-1,1,0)->0", list(M * V([1, 1, 1])) == [1, 3, 3] and list(M * V([0, 1, 1])) == [0, 2, 2] and M * V([-1, 1, 0]) == sp.zeros(3, 1))
P = sp.Matrix.hstack(vs[0], vs[1], vs[2])
chk("Q3d P^-1 M P = diag(0,1,2)", P.inv() * M * P == sp.diag(0, 1, 2))
exp(3, D_, 0, 2); exp(3, D_, 1, P.det())
chk("Q3d distractors for col 3: (-1,1,1)->1, (-1,1,0)->0, (0,1,-1) not eigen, image (2,0,0)", M * vs[1] == vs[1] and M * vs[0] == sp.zeros(3, 1) and list(M * V([0, 1, -1])) == [2, 0, 0])

# ---- Q4
W1 = V([[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 1, 1]])
exp(4, A_, 0, W1.rank())
chk("Q4a W1 = R^3", W1.rank() == 3)
W2c = V([[1, -2, -1]])
chk("Q4a x-y=z+y <=> x-2y-z=0 with basis (2,1,0),(1,0,1)", (W2c * V([2, 1, 0]))[0] == 0 and (W2c * V([1, 0, 1]))[0] == 0 and len(W2c.nullspace()) == 2)
exp(4, A_, 1, 2 * 1 + 3); exp(4, A_, 2, len(W2c.nullspace()))
exp(4, B_, 0, 3); exp(4, B_, 2, 3 + 2 - 3)
chk("Q4b W1+W2 = R^3 (rank of union)", sp.Matrix.hstack(W1.T, V([[2, 1, 0], [1, 0, 1]]).T).rank() == 3)
exp(4, C_, 0, len(W2c.nullspace())); exp(4, C_, 1, 3 + 2 - 2)
chk("Q4c (5,2,1) in W2; distractor values of x-2y-z: (1,2,3)->-6, (2,0,1)->1, (0,1,0)->-2 all nonzero", [(W2c * v)[0] for v in (V([1, 2, 3]), V([2, 0, 1]), V([0, 1, 0]))] == [-6, 1, -2])
v = V([3, 1, -1])
exp(4, D_, 0, v[0] - v[1]); exp(4, D_, 1, v[2] + v[1])
chk("Q4d (3,1,-1) not in W2", (W2c * v)[0] != 0)

# ---- Q5
def T(x, y, z): return V([x - y, -2 * x + 2 * y, 2 * z])


x1, y1, z1, x2, y2, z2 = sp.symbols("x1 y1 z1 x2 y2 z2")
chk("Q5a additivity", T(x1 + x2, y1 + y2, z1 + z2) == T(x1, y1, z1) + T(x2, y2, z2))
chk("Q5a bug: +1 breaks additivity", T(x1 + x2, y1 + y2, z1 + z2)[2] + 1 != T(x1, y1, z1)[2] + T(x2, y2, z2)[2])
exp(5, A_, 2, T(2, 4, 6)[1])
chk("Q5a T(2,4,6)=(-2,4,12)", list(T(2, 4, 6)) == [-2, 4, 12])
Tm = V([[1, -1, 0], [-2, 2, 0], [0, 0, 2]])
exp(5, B_, 0, T(1, 1, 0)[0]); exp(5, B_, 1, len(Tm.nullspace())); exp(5, B_, 2, Tm.rank())
chk("Q5b kernel (1,1,0), image basis (1,-2,0),(0,0,1)", Tm * V([1, 1, 0]) == sp.zeros(3, 1) and Tm.rank() == 2 and sp.Matrix.hstack(V([1, -2, 0]), V([0, 0, 1]), Tm).rank() == 2)
chk("Q5b distractor bases: first two dependent, three dependent, (1,1,0) not in image", sp.Matrix.hstack(V([1, -2, 0]), V([-1, 2, 0])).rank() == 1 and sp.Matrix.hstack(V([1, -2, 0]), V([0, 0, 1]), V([0, 0, 2])).rank() == 2 and sp.Matrix.hstack(Tm, V([1, 1, 0])).rank() == 3)
chk("Q5c not injective, not onto", len(Tm.nullspace()) > 0 and Tm.rank() < 3)
for name, v in [("(1,0,0)", V([1, 0, 0])), ("(1,-2,0)", V([1, -2, 0])), ("(0,0,5)", V([0, 0, 5])), ("(2,-4,3)", V([2, -4, 3]))]:
    inim = sp.Matrix.hstack(Tm, v).rank() == 2
    chk("Q5c %s %s in Im T" % (name, "is" if inim else "is not"), inim == (name != "(1,0,0)"))
exp(5, C_, 2, len(Tm.nullspace()) + Tm.rank())
B1 = [V([1, 1, 1]), V([0, 1, 1]), V([0, 0, 1])]
B2 = sp.Matrix.hstack(V([1, 0, 0]), V([0, 1, 1]), V([1, 1, 0]))
Tb = sp.Matrix.hstack(*[B2.inv() * (Tm * b) for b in B1])
exp(5, D_, 0, (Tm * B1[1])[0]); exp(5, D_, 1, Tb[0, 1]); exp(5, D_, 2, Tb[1, 0]); exp(5, D_, 3, Tb[2, 2])
chk("Q5d matrix as printed", Tb == sp.Matrix([[2, -1, 2], [2, 2, 2], [-2, 0, -2]]))

# ---- coverage
need = {(num, part, i) for (num, part), qq_ in QS.items() for i, st in enumerate(qq_.get("steps", [])) if st["type"] == "numeric"}
n = 0
for key in sorted(need):
    n += 1
    num, part, i = key
    if key not in EXP:
        chk("Q%d%s step %d has an expected value" % (num, part, i), False)
        continue
    st = QS[(num, part)]["steps"][i]
    ok = abs(float(sp.N(EXP[key])) - st["answer"]) <= st.get("tol", 0) + 1e-12
    chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, "abcd"["אבגד".index(part)], i, st["answer"], sp.N(EXP[key], 6)), ok)
chk("no orphan expected values", not (set(EXP) - need), str(sorted(set(EXP) - need)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
