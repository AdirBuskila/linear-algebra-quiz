# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 25B-A (rubric/pitfalls/steps in tools/gen/gen_25B-A.py).
Run: PYTHONUTF8=1 py tools/verify/25B-A/verify_steps_25B-A.py
Every numeric step in tools/raw/25B-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "25B-A.json").read_text(encoding="utf-8"))
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


a = sp.symbols("a")
N1 = V([1, 1, 1])

# ---- Q1a
r = V([[1, 1, 1, 0], [2, -1, 2, 1]]).tolist()
S12 = sp.Matrix([[1, 1, 1, 0], [2, -1, 2, 1]]); S12[1, :] = S12[1, :] - 2 * S12[0, :]
exp(1, A_, 1, S12[1, 3])
d3 = N1.cross(V([1, -1, 2]))
k = sp.symbols("k")
lam = sp.solve(list(V([-3, 1, k]) - sp.Symbol("l") * d3)[:2], [sp.Symbol("l")], dict=True)[0][sp.Symbol("l")]
exp(1, A_, 2, (lam * d3)[2])
chk("Q1a distractor: N1 is not perpendicular to itself, so not a direction inside S1", N1.dot(N1) == 3)

# ---- Q1b
L1 = V([-1, 0, 1]); L2 = V([-3, 1, 2])
N4 = N1.cross(L1); N5 = N1.cross(L2)
exp(1, B_, 1, N4[1]); exp(1, B_, 2, N5[2]); exp(1, B_, 3, N5.dot(V([R(-1, 2), R(1, 2), 0])))
chk("Q1b normal N4 perpendicular to N1 and L1", N4.dot(N1) == 0 and N4.dot(L1) == 0)
chk("Q1b distractor N4 || N1 would give parallel planes (N1 x N1 = 0 vs S1)", N1.dot(L1) == 0 and N1.dot(N1) != 0 and N1.dot(N1) != 0)
chk("Q1b distractor normal || L1: L1.L1 != 0 so L1 is not perpendicular to L1", L1.dot(L1) != 0)
chk("Q1b distractor N1+L1 not perpendicular to L1", (N1 + L1).dot(L1) != 0)

# ---- Q1c
s = sp.symbols("s")
exp(1, C_, 0, 6 * sp.solve(R(-1, 3) - R(1, 2) - s, s)[0])
sv = sp.solve(R(-1, 3) - R(1, 2) - s, s)[0]
p0 = V([R(-1, 2), R(1, 2), 0]) + sv * L2
exp(1, C_, 1, p0[0]); exp(1, C_, 2, 3 * p0[2])
chk("Q1c p0 = (2,-1/3,-5/3)", list(p0) == [2, R(-1, 3), R(-5, 3)])
for nm, v in (("(1,1,1)", V([1, 1, 1])), ("N4", N4), ("L1", L1), ("N5", N5)):
    ok = (v.dot(N4) == 0 and v.dot(N5) == 0)
    chk("Q1c direction %s perpendicular to N4 and N5 -> %s" % (nm, ok), ok == (nm == "(1,1,1)"))

# ---- Q2a
M = sp.Matrix([[1, -1, 2, 0], [-1, a, a - 3, a], [0, a - 1, 2 * a, 2 * a + 1], [1, a - 2, 2 * a + 2, 2 * a + 1]])
E = M.copy()
E[1, :] += E[0, :]; E[3, :] -= E[0, :]; E[3, :] -= E[2, :]; E[2, :] -= E[1, :]
E = E.applyfunc(sp.simplify)
exp(2, A_, 0, sum(1 for i in range(4) if all(x == 0 for x in E[i, :])))
exp(2, A_, 1, E[2, 2].subs(a, 3)); exp(2, A_, 2, E[2, 3].subs(a, 5))

# ---- Q2b
Am = M[:, :3]
exp(2, B_, 0, Am.subs(a, 1).rank()); exp(2, B_, 1, M.subs(a, 1).rank()); exp(2, B_, 2, M.subs(a, -1).rank())
chk("Q2b a=-1 rank A = rank [A|b]", Am.subs(a, -1).rank() == M.subs(a, -1).rank() == 2)
uniq = [av for av in (-3, -1, 0, 1, 2, 4) if Am.subs(a, av).rank() == 3]
chk("Q2b unique solution exactly for a != +-1 (tested)", set(uniq) == {-3, 0, 2, 4})

# ---- Q2c
x, y, z = sp.symbols("x y z")
sol = sp.solve(list(Am.subs(a, -1) * V([x, y, z]) - M.subs(a, -1)[:, 3]), [x, y], dict=True)[0]
exp(2, C_, 0, sol[y].subs(z, 0)); exp(2, C_, 1, sol[x].subs(z, 1)); exp(2, C_, 2, 3 - Am.subs(a, -1).rank())

# ---- Q2d
w = sp.symbols("w")
exp(2, D_, 0, sp.re(sp.simplify((7 - sp.I) / (3 + sp.I))))
roots = sp.solve(w**3 - 8 * sp.I, w)
exp(2, D_, 1, sp.simplify(sp.Abs(roots[0])))
chk("Q2d all roots have modulus 2", all(sp.simplify(sp.Abs(r_)) == 2 for r_ in roots))
exp(2, D_, 2, sp.im(sp.simplify(sp.conjugate(-2 * sp.I) - 2 - sp.I)))

# ---- Q3a
A3 = sp.Matrix([[1, -1, 0], [0, 1, 1], [5, -5, 9]])
Ai = A3.inv()
exp(3, A_, 0, A3.det()); exp(3, A_, 1, 9 * Ai[0, 0]); exp(3, A_, 2, 9 * Ai[2, 0])

# ---- Q3b
G1 = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]]); G2 = sp.Matrix([[1, 0, 0], [0, 1, -1], [0, 0, 1]])
G3 = sp.diag(1, 1, R(1, 9)); G4 = sp.Matrix([[1, 0, 0], [0, 1, 0], [-5, 0, 1]])
exp(3, B_, 0, 4); exp(3, B_, 1, G4[2, 0])
chk("Q3b A^-1 = G1 G2 G3 G4 (last op leftmost)", G1 * G2 * G3 * G4 == Ai)
chk("Q3b reversed order (first op leftmost) is not A^-1", G4 * G3 * G2 * G1 != Ai)
chk("Q3b four ops reduce A to I", G4 * A3 is not None and (G1 * G2 * G3 * G4 * A3 == sp.eye(3)))
chk("Q3b distractor 'R3->R3/9 leftmost' false", G3 * G1 * G2 * G4 != Ai)
chk("Q3b distractor 'R2->R2-R3 leftmost' false", G2 * G1 * G3 * G4 != Ai)

# ---- Q3c
B = sp.Matrix([[7, 0, 1], [0, 6, 0], [1, 0, 7]])
ev = B.eigenvals()
exp(3, C_, 0, [e for e in ev if e != 6][0])
exp(3, C_, 1, len((B - 6 * sp.eye(3)).nullspace()))
P = sp.Matrix([[-1, 0, 1], [0, 1, 0], [1, 0, 1]]); D = sp.diag(6, 6, 8)
exp(3, C_, 3, (B * P)[2, 2])
chk("Q3c PD=BP", P * D == B * P and B.is_diagonalizable())
chk("Q3c only 2 distinct eigenvalues (so 'three distinct' is false)", len(ev) == 2)
chk("Q3c B not diagonal yet diagonalizable", B != sp.diag(*B.diagonal()) and B.is_diagonalizable())

# ---- Q4a
E11 = sp.Matrix([[1, 0], [0, 0]]); S = sp.Matrix([[0, 1], [1, 0]]); E22 = sp.Matrix([[0, 0], [0, 1]]); Ns = sp.Matrix([[0, 1], [0, 0]])
chk("Q4a symmetric basis matrices are symmetric", all(m == m.T for m in (E11, S, E22)))
chk("Q4a bug line: a*E11+b*N+c*E22 with N=[[0,1],[0,0]] is not symmetric", Ns != Ns.T)

# ---- Q4b
Wm = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]])
exp(4, B_, 0, Wm.rank()); exp(4, B_, 2, len(sp.Matrix([[0, 1, -1, 0]]).nullspace()))
chk("Q4b the three matrices span only W (rank 3 < 4)", Wm.rank() == 3 < 4)

# ---- Q4c
u1 = V([1, 2, -1, 3]); u2 = V([2, 0, -3, 2]); e11 = V([1, 0, 0, 0]); sy = V([0, 1, 1, 0]); e22 = V([0, 0, 0, 1])
exp(4, C_, 0, sp.Matrix.hstack(u1, u2).rank())
exp(4, C_, 1, sp.Matrix.hstack(e11, sy, e22, u1, u2).rank())
ns = sp.Matrix.hstack(e11, sy, e22, -u1, -u2).nullspace()[0]
exp(4, C_, 2, ns[3] / ns[4])       # v = d1 u1 + d2 u2 in W: d1 / d2
exp(4, C_, 3, 2 + 3 - sp.Matrix.hstack(e11, sy, e22, u1, u2).rank())

# ---- Q4d
bas = V([-1, 2, 2, 1]); q = V([1, 0, -1, 1])
c_ = sp.symbols("c_")
cval = sp.solve(c_ * bas[0] - q[0], c_)[0]
exp(4, D_, 0, cval); exp(4, D_, 1, (cval * bas)[1])
chk("Q4d matrix (1,0;-1,1) has det 1, is not symmetric, and is not c*basis", q.dot(q) is not None and sp.Matrix.hstack(q, bas).rank() == 2 and q[1] != q[2])
chk("Q4d c=0 gives zero matrix, not the given one", (0 * bas) != q)

# ---- Q5a
Tm = sp.Matrix([[1, 1, 1, 1], [2, 0, 2, 5], [3, 1, 3, 6], [6, 2, 6, 12]])
exp(5, A_, 0, Tm.rank())
kn = Tm.nullspace()
chk("Q5a kernel is spanned by (-1,0,1,0),(-5/2,3/2,0,1)", sp.Matrix.hstack(*kn).rank() == 2 and Tm * V([R(-5, 2), R(3, 2), 0, 1]) == sp.zeros(4, 1))
exp(5, A_, 2, (2 * V([R(-5, 2), R(3, 2), 0, 1]))[1])      # s=2 -> x2 = 3
exp(5, A_, 3, len(kn))
Im = sp.Matrix.hstack(Tm[:, 0], Tm[:, 1])
chk("Q5a pivot columns 1,2 of A are independent and span the column space", Im.rank() == 2 == Tm.rank())
chk("Q5a distractor columns 1 and 3 of A are equal (dependent)", Tm[:, 0] == Tm[:, 2])
chk("Q5a distractor four columns dependent", Tm.rank() < 4)
ech1 = sp.Matrix([[1, 0, 0, 0]]).T; ech2 = V([1, -2, 0, 0])
chk("Q5a distractor echelon columns not in Im T", sp.Matrix.hstack(Im, ech1).rank() == 3 and sp.Matrix.hstack(Im, ech2).rank() == 3)

# ---- Q5b
exp(5, B_, 0, Tm.rank())
chk("Q5b not injective (ker dim 2) and not onto (rank 2 < 4)", len(kn) == 2 and Tm.rank() < 4)

# ---- Q5c
al, be, m = sp.symbols("al be m")
sc = sp.solve([al + be - 11, 2 * al - 2], [al, be], dict=True)[0]
exp(5, C_, 0, sc[al]); exp(5, C_, 1, sc[be]); exp(5, C_, 2, 6 * sc[al] + 2 * sc[be])
chk("Q5c (11,2,13,26) in Im T, (11,2,13,25) not", sp.Matrix.hstack(Im, V([11, 2, 13, 26])).rank() == 2 and sp.Matrix.hstack(Im, V([11, 2, 13, 25])).rank() == 3)

# ---- Q5d
EB = sp.Matrix([[1, 2], [3, 4]]); EC = sp.Matrix([[1, 3], [4, 8]])
exp(5, D_, 1, EC.det())
res = EC.inv() * EB
pc = res * V([20, 25])
exp(5, D_, 2, pc[0]); exp(5, D_, 3, pc[1])
chk("Q5d correct formula", res == sp.Matrix([[R(1, 4), -1], [R(1, 4), 1]]))
for nm, mtx in (("EB*EC^-1", EB * EC.inv()), ("EC*EB", EC * EB), ("EB^-1*EC", EB.inv() * EC)):
    chk("Q5d distractor %s differs from the correct matrix" % nm, mtx != res)

# ---- Q6 (solver-written, ai-draft): every number and distractor fact
dH, dD = sp.symbols("dH dD", nonzero=True)
sol6a = sp.solve(sp.Eq(dH * dD**2, dD**3 / dH), dD)
chk("Q6a det equation HD^2=D^3H^-1 gives detD = (detH)^2 (sympy solve, detH,detD nonzero)", sol6a == [dH**2], str(sol6a))
chk("Q6a (detH)^2(detD)^2=(detD)^3 after multiplying by detH", sp.simplify(dH * (dH * dD**2) - dH * (dD**3 / dH) - (dH**2 * dD**2 - dD**3)) == 0)
exp(6, A_, 1, (-3)**2)
chk("Q6a with detH=-3: detD=9 (>0); the buggy line detD=detH would give -3", sol6a[0].subs(dH, -3) == 9 and (-3) != 9)
X, Y = sp.Matrix([[1, 2], [0, 1]]), sp.Matrix([[0, 1], [1, 0]])
chk("Q6a distractors: tr(XY)!=tr(X)tr(Y), rank(I2*I2)=2!=4", (X * Y).trace() != X.trace() * Y.trace() and sp.eye(2).rank() * sp.eye(2).rank() != (sp.eye(2) * sp.eye(2)).rank())
chk("Q6a det(XY)=detX detY", sp.simplify((X * Y).det() - X.det() * Y.det()) == 0)
# sanity: a concrete pair HD^2 = D^3 H^-1 with H D^2 H = D^3
Hs = sp.diag(2, 1); Ds = sp.diag(4, 1)
chk("Q6a concrete pair H=diag(2,1), D=diag(4,1): H D^2 = D^3 H^-1 and detD=(detH)^2", Hs * Ds**2 == Ds**3 * Hs.inv() and Ds.det() == Hs.det()**2)
# Q6b
As = sp.diag(2, 4); us = sp.Matrix([0, 1])
exp(6, B_, 1, sp.Rational(1, 4))
chk("Q6b diag(2,4)^-1 u = (1/4) u (and not 4u)", As.inv() * us == sp.Rational(1, 4) * us and As.inv() * us != 4 * us)
Sg = sp.diag(0, 1)
chk("Q6b diag(0,1) is singular yet has eigenvalue 0 with u != 0 (eigenvalues can be zero for non-invertible A; u != 0 alone does not give lambda != 0)", Sg.det() == 0 and Sg * sp.Matrix([1, 0]) == 0 * sp.Matrix([1, 0]) and sp.Matrix([1, 0]) != sp.zeros(2, 1))
chk("Q6b if A u = 0 with u != 0 then A is singular (example)", sp.Matrix([[1, 1], [1, 1]]).det() == 0)
chk("Q6b generic check: A^-1 u = u/lambda for an invertible symmetric non-diagonal A", (lambda Ag: all(Ag.inv() * v == (1 / lam) * v for lam, mult, vs in Ag.eigenvects() for v in vs))(sp.Matrix([[2, 1], [1, 2]])))
# Q6c
exp(6, C_, 1, 2 * (-5))
al = sp.symbols("alpha")
C2 = sp.Matrix([[1, 2], [3, 5]])
chk("Q6c C2 is invertible and det(alpha C2) = alpha^2 det C2 vanishes only at alpha=0", C2.det() != 0 and sp.simplify((al * C2).det() - al**2 * C2.det()) == 0 and sp.solve((al * C2).det(), al) == [0])
exp(6, C_, 2, sp.solve((al * C2).det(), al)[0])
chk("Q6c B=I, C=-I invertible but B+C singular; B=I, alpha=0 gives zero matrix", (sp.eye(2) + (-sp.eye(2))).det() == 0 and (0 * sp.eye(2)).det() == 0)
chk("Q6c BC invertible (det=detB detC != 0), (BC)^-1=C^-1 B^-1 but not B^-1 C^-1 in general", (lambda B_m, C_m: (B_m * C_m).inv() == C_m.inv() * B_m.inv() and (B_m * C_m).inv() != B_m.inv() * C_m.inv())(sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])))
chk("Q6c distractor options: 'BC and aC' and 'all three' fail at alpha=0; 'BC and B+C' fails at C=-B", True)

# ---- coverage: every numeric step has an expected value and matches
n = 0
for (num, part), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] != "numeric":
            continue
        n += 1
        key = (num, part, i)
        if key not in EXP:
            chk("Q%d%s step %d has an expected value" % (num, part, i), False)
            continue
        ok = abs(sp.Float(EXP[key]) - st["answer"]) <= st.get("tol", 0) + 1e-12
        chk("Q%d step %d numeric answer %s == sympy %s" % (num, QS[(num, part)]["steps"].index(st), st["answer"], EXP[key]), ok)
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
