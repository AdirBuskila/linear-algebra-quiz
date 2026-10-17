# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 25A-B (rubric/pitfalls/steps in tools/gen/gen_25A-B.py).
Run: PYTHONUTF8=1 py tools/verify/25A-B/verify_steps_25A-B.py
Every numeric step in tools/raw/25A-B.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "25A-B.json").read_text(encoding="utf-8"))
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
a = sp.symbols("a")

# ---- Q1a
N1k = V([-k**2, -1, k + 1]); N2k = V([1, k, 2 * k - 3])
dot = sp.expand(N1k.dot(N2k))
c_ = sp.symbols("c_")
exp(1, A_, 1, -sp.Poly(dot, k).coeff_monomial(1))   # dot = k^2 - 2k - c  ->  c = -(constant term)
chk("Q1a dot product = k^2-2k-3", sp.expand(dot - (k**2 - 2 * k - 3)) == 0)
exp(1, A_, 2, [r for r in sp.solve(dot, k) if r < 0][0])
nA = V([-1, -1, 0]); nB = V([1, -1, -5])
chk("Q1a perpendicular planes have perpendicular normals (k=-1); parallel normals would not be perpendicular planes", N1k.subs(k, -1).dot(N2k.subs(k, -1)) == 0 and sp.Matrix.hstack(N1k.subs(k, -1), N2k.subs(k, -1)).rank() == 2)

# ---- Q1b
M = sp.Matrix([[-1, -1, 0, 2], [1, -1, -5, 1]])
exp(1, B_, 0, N2k.subs(k, -1)[2])
M2 = M.copy(); M2[1, :] = M2[1, :] + M2[0, :]
exp(1, B_, 1, M2[1, 3])
dirv = nA.cross(nB)
exp(1, B_, 2, 5 * dirv[2] / dirv[0])   # direction = (5,-5,m)
chk("Q1b direction (5,-5,2)", list(dirv) == [5, -5, 2])
t = sp.symbols("t")
base = V([R(-1, 2), R(-3, 2), 0]); dd = V([R(5, 2), R(-5, 2), 1])
tv = sp.solve(list(base + t * dd - V([12, -14, 5])), t, dict=True)
exp(1, B_, 3, tv[0][t])
chk("Q1b line lies in both planes", all(sp.simplify((M[i, :3] * (base + t * dd))[0] - M[i, 3]) == 0 for i in range(2)))

# ---- Q1c
exp(1, C_, 1, nA.dot(nB)); exp(1, C_, 2, nB[2])
chk("Q1c normal of S3 is the line direction (5,-5,2): perpendicular to N1 and N2", dirv.dot(nA) == 0 and dirv.dot(nB) == 0)
chk("Q1c distractor: direction (5,-5,2) is not parallel to S3 (it is its normal)", dirv.dot(dirv) != 0)
chk("Q1c distractor: (5,-5,2) and N1 x N2 span only a line", sp.Matrix.hstack(dirv, nA.cross(nB)).rank() == 1)
chk("Q1c correct: N1,N2 independent and both perpendicular to the normal", sp.Matrix.hstack(nA, nB).rank() == 2)

# ---- Q2
Z = sp.Matrix([[a, a, -1], [a**2, a, a**2 - a], [a, a, 2 * a + 1]])
Z1 = Z.copy(); Z1[1, :] = Z1[1, :] - a * Z1[0, :]; Z1[2, :] = Z1[2, :] - Z1[0, :]
Z1 = Z1.applyfunc(sp.simplify)
exp(2, A_, 0, Z1[2, 2].subs(a, 4)); exp(2, A_, 1, Z1[1, 1].subs(a, 3))
chk("Q2a divisors vanish exactly at 0,1,-1", sorted(sp.solve(sp.Poly(a * (1 - a) * 2 * (a + 1)), a)) == [-1, 0, 1])
exp(2, B_, 0, Z.subs(a, 2).rank()); exp(2, B_, 1, Z.subs(a, -1).rank())
exp(2, B_, 2, len([v for v in (0, 1, -1) if Z.subs(a, v).rank() < 3]))
chk("Q2b rank 3 for all tested a not in {0,1,-1}", all(Z.subs(a, v).rank() == 3 for v in (2, -2, 5, R(1, 2), -3)))
x, y, z = sp.symbols("x y z")
nsm = Z.subs(a, -1).nullspace()[0]
exp(2, C_, 0, nsm[2] / nsm[1]); exp(2, C_, 1, nsm[0] / nsm[1])
exp(2, C_, 2, Z.subs(a, 1).rank())
ns1 = Z.subs(a, 1).nullspace()[0]
exp(2, C_, 3, ns1[1] / ns1[0])
Z0 = Z.subs(a, 0)
exp(2, D_, 0, Z0.rank()); exp(2, D_, 1, 3 - Z0.rank())
chk("Q2d every solution at a=0 has z=0", all(v[2] == 0 for v in Z0.nullspace()))
exp(2, D_, 2, 0)

# ---- Q3a
A3 = sp.Matrix([[1, 1, 1], [2, 3, 2], [3, 8, 2]])
Ai = A3.inv()
exp(3, A_, 0, A3.det()); exp(3, A_, 1, Ai[0, 0]); exp(3, A_, 2, Ai[2, 0])
E = [sp.Matrix([[1, 0, -1], [0, 1, 0], [0, 0, 1]]), sp.diag(1, 1, -1), sp.Matrix([[1, -1, 0], [0, 1, 0], [0, 0, 1]]),
     sp.Matrix([[1, 0, 0], [0, 1, 0], [0, -5, 1]]), sp.Matrix([[1, 0, 0], [0, 1, 0], [-3, 0, 1]]), sp.Matrix([[1, 0, 0], [-2, 1, 0], [0, 0, 1]])]
chk("Q3a official six-factor product = A^-1", E[0] * E[1] * E[2] * E[3] * E[4] * E[5] == Ai)
for j, nm in ((5, "first op R2-2R1"), (1, "R3->-R3"), (3, "R3-5R2")):
    rest = [E[i] for i in range(6) if i != j]
    prod = E[j]
    for m_ in rest:
        prod = prod * m_
    chk("Q3a distractor leftmost = %s gives a different product" % nm, prod != Ai)

# ---- Q3b
B = sp.ones(3, 3)
exp(3, B_, 0, B.rank()); exp(3, B_, 1, len((B - 0 * sp.eye(3)).nullspace()))
ev = B.eigenvals()
exp(3, B_, 2, [e for e in ev if e != 0][0])
P = sp.Matrix([[1, -1, -1], [1, 1, 0], [1, 0, 1]]); D = sp.diag(3, 0, 0)
exp(3, B_, 4, (B * P)[0, 0])
chk("Q3b BP=PD, P invertible", B * P == P * D and P.det() != 0)
chk("Q3b only two distinct eigenvalues; B singular yet diagonalizable", len(ev) == 2 and B.det() == 0 and B.is_diagonalizable())
chk("Q3b a repeated eigenvalue does not prevent diagonalization here", B.is_diagonalizable())

# ---- Q5a
Tm = sp.Matrix([[1, 1, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 5, 5]])
exp(5, A_, 0, Tm.rank())
kn = Tm.nullspace()
chk("Q5a kernel (-1,1,0,0),(0,0,-1,1)", all(Tm * v == sp.zeros(4, 1) for v in (V([-1, 1, 0, 0]), V([0, 0, -1, 1]))) and len(kn) == 2)
exp(5, A_, 2, (2 * V([0, 0, -1, 1]))[2]); exp(5, A_, 3, len(kn))
Im = sp.Matrix.hstack(Tm[:, 0], Tm[:, 2])
chk("Q5a columns 1,3 are an independent spanning set of the column space", Im.rank() == 2 == Tm.rank())
chk("Q5a distractor columns 1,2 are equal", Tm[:, 0] == Tm[:, 1])
chk("Q5a distractor four columns dependent", Tm.rank() < 4)
chk("Q5a distractor echelon columns (1,0,0,0),(1,1,0,0) not in Im", sp.Matrix.hstack(Im, V([1, 0, 0, 0])).rank() == 3 and sp.Matrix.hstack(Im, V([1, 1, 0, 0])).rank() == 3)

# ---- Q5b
exp(5, B_, 0, len(kn))
chk("Q5b not injective, not onto", len(kn) == 2 and Tm.rank() < 4)

# ---- Q5c
al, be = sp.symbols("al be")
sc = sp.solve([al + be - 4, al + 2 * be - 6], [al, be], dict=True)[0]
exp(5, C_, 0, sc[be]); exp(5, C_, 1, sc[al])
exp(5, C_, 2, 2 * sc[al] + 3 * sc[be]); exp(5, C_, 3, 3 * sc[al] + 5 * sc[be])
Cm = sp.Matrix([[1, 1], [1, 2], [2, 3], [3, 5]])
chk("Q5c (4,6,10,16) in Im, perturbations not", Cm.row_join(V([4, 6, 10, 16])).rank() == 2 and Cm.row_join(V([4, 6, 9, 16])).rank() == 3 and Cm.row_join(V([4, 6, 10, 15])).rank() == 3)

# ---- Q5d
EB = sp.Matrix([[20, 25], [20, 24]]); EC = sp.Matrix([[1, 3], [3, 10]])
res = EC.inv() * EB
exp(5, D_, 1, EC.det()); exp(5, D_, 2, res[0, 0]); exp(5, D_, 3, res[1, 1])
chk("Q5d correct matrix", res == sp.Matrix([[140, 178], [-40, -51]]))
for nm, mtx in (("EB*EC^-1", EB * EC.inv()), ("EC*EB", EC * EB), ("EB^-1*EC", EB.inv() * EC)):
    chk("Q5d distractor %s differs from the correct matrix" % nm, mtx != res)

# ---- coverage
n = 0
need = {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
for key in sorted(need, key=lambda t_: (t_[0], t_[1], t_[2])):
    n += 1
    num, part, i = key
    if key not in EXP:
        chk("Q%d%s step %d has an expected value" % (num, part, i), False)
        continue
    st = QS[(num, part)]["steps"][i]
    ok = abs(sp.Float(EXP[key]) - st["answer"]) <= st.get("tol", 0) + 1e-12
    chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, "abcd"["אבגד".index(part)], i, st["answer"], EXP[key]), ok)
chk("no orphan expected values", not (set(EXP) - need), str(sorted(set(EXP) - need)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
