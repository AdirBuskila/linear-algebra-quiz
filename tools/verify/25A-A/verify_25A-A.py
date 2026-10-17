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

# ======================================================================================
# STEPS: every expected value stored in tools/raw/25A-A.json steps is recomputed with sympy and compared.
import json, pathlib
RAW = json.loads((pathlib.Path(__file__).resolve().parents[2] / "raw" / "25A-A.json").read_text(encoding="utf-8"))
QS = {"25A-A-Q%d%s" % (q["num"], {"א": "a", "ב": "b", "ג": "c", "ד": "d"}[q["part"]]): q for q in RAW["questions"]}


def step_num(qid, idx, expected):
    st = QS[qid]["steps"][idx]
    chk("STEP %s[%d] numeric" % (qid, idx), st["type"] == "numeric" and sp.nsimplify(st["answer"]) == sp.nsimplify(expected),
        "json=%s sympy=%s" % (st.get("answer"), expected))


def step_choice(qid, idx, expected_value):
    st = QS[qid]["steps"][idx]
    val = [o["value"] for o in st["options"] if o["id"] == st["correctId"]][0]
    chk("STEP %s[%d] choice" % (qid, idx), st["type"] == "choice" and val == expected_value, val)


a, s, t = sp.symbols("a s t")
# Q1a : c in a^2+7a-c, positive root
resid = sp.expand(3 * ((s_ := a - 1) - 5 - a * (-(a + 4) / 3)))   # (I) with s from (III), t from (II)
chk("S Q1a quadratic is a^2+7a-18", sp.expand(resid - (a**2 + 7*a - 18)) == 0, str(resid))
step_num("25A-A-Q1a", 1, -resid.subs(a, 0))
step_num("25A-A-Q1a", 2, [r for r in sp.solve(resid, a) if r > 0][0])
# Q1b / Q1c
L1 = sp.Matrix([1, 0, 1]); L2 = sp.Matrix([2, -3, 0]); P0 = sp.Matrix([0, 2, -2])
N1 = L1.cross(L2); N2 = L1.cross(N1)
step_num("25A-A-Q1b", 1, N1[1]); step_num("25A-A-Q1b", 2, (N1.T * P0)[0])
step_num("25A-A-Q1c", 1, N2[2]); step_num("25A-A-Q1c", 2, ((sp.Matrix([-1, 3, 1])).T * P0)[0])
# Q2
a = sp.symbols("a")
M = sp.Matrix([[a, a, -1], [a**2, a, a**2 - a], [a, a, 2*a + 1]])
R = M.copy(); R[1, :] = R[1, :] - a * R[0, :]; R[2, :] = R[2, :] - R[0, :]
step_num("25A-A-Q2a", 0, R[2, 2].subs(a, 3)); step_num("25A-A-Q2a", 1, R[1, 1].subs(a, 3))
bad_a = sorted(set(sp.solve(a * (1 - a), a)) | set(sp.solve(2 * (a + 1), a)))
chk("S Q2a forbidden division set {-1,0,1}", bad_a == [-1, 0, 1])
step_choice("25A-A-Q2a", 2, r"$a\in\{0,1,-1\}$")
step_num("25A-A-Q2b", 1, M.subs(a, 2).rank())
dets = sorted(sp.solve(M.det(), a)); step_num("25A-A-Q2b", 2, len(dets))
chk("S Q2b det zeros {-1,0,1}", dets == [-1, 0, 1]); step_choice("25A-A-Q2b", 3, r"$a\neq0,\ 1,\ -1$")
step_num("25A-A-Q2c", 0, M.subs(a, -1).rank())
v = M.subs(a, -1).nullspace()[0]; v = v / v[1]
step_num("25A-A-Q2c", 1, v[0]); chk("S Q2c z=2y at a=-1", v[2] == 2)
step_num("25A-A-Q2c", 2, M.subs(a, 1).rank())
line_a = [av for av in (0, 1, -1, 2) if 3 - M.subs(a, av).rank() == 1]
chk("S Q2c line values {-1,1}", line_a == [1, -1] or sorted(line_a) == [-1, 1]); step_choice("25A-A-Q2c", 3, r"$a=1$ ו-$a=-1$")
step_num("25A-A-Q2d", 0, M.subs(a, 0).rank()); step_num("25A-A-Q2d", 1, 3 - M.subs(a, 0).rank())
# Q3a : replay the six row operations on (A|I)
A = sp.Matrix([[1, 2, 1], [0, 1, 3], [3, 8, 8]])
step_num("25A-A-Q3a", 0, A.det()); step_num("25A-A-Q3a", 1, A.inv()[0, 0])
G = A.row_join(sp.eye(3))
ops = [("add", 2, 0, -3), ("add", 2, 1, -2), ("mul", 2, None, -1), ("add", 1, 2, -3), ("add", 0, 2, -1), ("add", 0, 1, -2)]
for kind, i, j, c in ops:
    if kind == "add":
        G[i, :] = G[i, :] + c * G[j, :]
    else:
        G[i, :] = c * G[i, :]
chk("S Q3a six row ops turn (A|I) into (I|A^-1)", G[:, :3] == sp.eye(3) and G[:, 3:] == A.inv())
step_num("25A-A-Q3a", 2, len(ops))
# Q3b
B = sp.Matrix([[9, 0, 1], [0, 8, 0], [1, 0, 9]])
ev = B.eigenvals()
step_num("25A-A-Q3b", 0, [e for e in ev if e != 8][0])
dim8 = 3 - (8 * sp.eye(3) - B).rank(); step_num("25A-A-Q3b", 1, dim8)
dim_total = sum(len((B - e * sp.eye(3)).nullspace()) for e in ev)
chk("S Q3b diagonalizable (sum of eigenspace dims = 3, 8 has multiplicity 2)", dim_total == 3 and ev[8] == 2 and B.is_diagonalizable())
step_choice("25A-A-Q3b", 2, r"כן, כי לכל ערך עצמי המימד של המרחב העצמי שווה לריבוי האלגברי")
# Q4
x, pa, pb, pc, pd = sp.symbols("x pa pb pc pd")
pp = pa * x**3 + pb * x**2 + pc * x + pd
step_num("25A-A-Q4a", 0, sp.diff(pp, x, 2).subs(x, 0).coeff(pb))
w1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 2, 2]]); w2 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
step_num("25A-A-Q4a", 1, w1.rank()); step_num("25A-A-Q4a", 2, w2.rank())
four = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 2, 2], [0, 0, 0, 1]])
step_num("25A-A-Q4b", 1, four.rank()); step_num("25A-A-Q4b", 2, sp.Matrix.vstack(w1, w2).rank())
C45 = sp.Matrix.hstack(*(list(w1.T.columnspace() and [w1[0, :].T, w1[1, :].T]) + [-w2[0, :].T, -w2[1, :].T, -w2[2, :].T]))
step_num("25A-A-Q4c", 0, C45.rank()); step_num("25A-A-Q4c", 1, C45.shape[1] - C45.rank())
step_num("25A-A-Q4c", 2, len(C45.nullspace()))
Qc = sp.Matrix([1, 2, 0, 3])
step_num("25A-A-Q4d", 1, Qc[2]); step_num("25A-A-Q4d", 2, Qc[3])
# Q5
T = sp.Matrix([[1, 2, 12, 21], [1, 0, 10, 1], [1, 2, 12, 21], [1, 5, 15, 51]])
step_num("25A-A-Q5a", 0, T.rank()); step_num("25A-A-Q5a", 1, 4 - T.rank())
chk("S Q5a pivots are columns 1,2 of the original A", T.rref()[1] == (0, 1)); step_choice("25A-A-Q5a", 2, r"מהעמודות המקוריות של $A$ שבמקומן יש איברים מובילים אחרי הדירוג")
kk = T.nullspace(); kb1 = sp.Matrix([-10, -1, 1, 0])
chk("S Q5a (c,-1,1,0) with c=-10 in Ker", T * kb1 == sp.zeros(4, 1) and len(kk) == 2); step_num("25A-A-Q5a", 3, kb1[0])
step_num("25A-A-Q5b", 0, 4)
chk("S Q5b dim Ker 2 != 0 and rank 2 < 4", len(kk) == 2 and T.rank() < 4)
step_choice("25A-A-Q5b", 1, r"לא, כי הגרעין אינו טריוויאלי ($\dim\mathrm{Ker}\,T=2$)")
step_choice("25A-A-Q5b", 2, r"לא, כי $\dim\mathrm{Im}\,T=2<4=\dim M_{2\times2}(\mathbb{R})$")
s1, s2 = sp.symbols("s1 s2")
sc = sp.solve([-10*s1 - s2 - 22, -s1 - 10*s2 - 22], [s1, s2], dict=True)[0]
step_num("25A-A-Q5c", 0, sc[s2]); step_num("25A-A-Q5c", 1, sc[s1]); step_num("25A-A-Q5c", 2, sc[s2])
chk("S Q5c polynomial 22+22x+ax^2+bx^3 (a=b=-2) in Ker T", T * sp.Matrix([22, 22, -2, -2]) == sp.zeros(4, 1))
EB = sp.Matrix([[2, 0], [2, 5]]); EC = sp.Matrix([[1, 2], [3, 7]])
step_num("25A-A-Q5d", 1, EC.det()); step_num("25A-A-Q5d", 2, EC.inv()[0, 0]); step_num("25A-A-Q5d", 3, (EC.inv() * EB)[1, 0])
chk("S every item has rubric (points sum), pitfalls, steps", all(q.get("rubric") and q.get("pitfalls") and q.get("steps") and
    sum(r["points"] for r in q["rubric"]) == q["points"] for q in QS.values()) and len(QS) == 17)

print("DONE, mismatches:", bad if bad else "none")
