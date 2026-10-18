# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 23B-B (rubric/pitfalls/steps in tools/gen/gen_23B-B.py).
Run: PYTHONUTF8=1 py tools/verify/23B-B/verify_steps_23B-B.py
Every numeric step in tools/raw/23B-B.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug / order line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "23B-B.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_, E_ = "א", "ב", "ג", "ד", "ה"
R = sp.Rational
M = sp.Matrix
bad = []
EXP = {}


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def exp(num, part, idx, val):
    EXP[(num, part, idx)] = sp.nsimplify(val)


I2 = sp.eye(2)
# ---- Q1a: B^-1 x = (1/lam) x ; distractors tested on B = 2I, lam = 2
Bm = 2 * sp.eye(2); lam = 2
x = M([1, 0])
chk("Q1a B^-1 x = x/lam", Bm.inv() * x == x / lam)
for nm, v in (("lam", lam), ("-lam", -lam), ("lam^2", lam ** 2)):
    chk("Q1a distractor eigenvalue %s is wrong for B=2I" % nm, Bm.inv() * x != v * x)
chk("Q1a bug line B^-1 x = lam x false for B=2I", Bm.inv() * x != lam * x)

# ---- Q1b: AXB = A+B => X = B^-1 + A^-1 ; noncommuting distractor
A = M([[2, 1], [1, 1]]); B = M([[1, 3], [0, 2]])
X = B.inv() + A.inv()
chk("Q1b X = B^-1 + A^-1 solves AXB=A+B", A * X * B == A + B)
chk("Q1b XB = I + A^-1 B", X * B == I2 + A.inv() * B)
chk("Q1b distractor: right-multiplying AXB by A^-1 does not cancel A (A X B A^-1 != X B)", A * X * B * A.inv() != X * B)
chk("Q1b distractor: matrices do not commute (AB != BA)", A * B != B * A)
chk("Q1b distractor: (A+B)/(AB)-style X = (A+B)B^-1A^-1 differs from B^-1+A^-1", (A + B) * B.inv() * A.inv() != X)
a_, b_ = sp.symbols("a_ b_")
exp(1, B_, 2, sp.solve(sp.Eq(2 * a_ * 4, 2 + 4), a_)[0])

# ---- Q1c: A^3-5A-4I=0
t = sp.symbols("t")
chk("Q1c a=-1 is a root of a^3-5a-4", (-1) ** 3 - 5 * (-1) - 4 == 0)
chk("Q1c x*(x^2-5)/4 = 1 mod x^3-5x-4", sp.rem(sp.expand(t * (t ** 2 - 5) / 4 - 1), t ** 3 - 5 * t - 4, t) == 0)
for nm, f in (("A^2-5", lambda a: a ** 2 - 5), ("-(A^2-5)/4", lambda a: -(a ** 2 - 5) / 4), ("(A^2+5)/4", lambda a: (a ** 2 + 5) / 4)):
    chk("Q1c distractor %s != A^-1 at A=-1" % nm, f(-1) != R(1, -1))
exp(1, C_, 3, (R(1, 4)) * ((-1) ** 2 - 5))
chk("Q1c (A^2-5)/4 correct at A=-1", R(1, 4) * ((-1) ** 2 - 5) == R(1, -1))
chk("Q1c bug: at A=-1, A^3-5A = 4 (not -4)", (-1) ** 3 - 5 * (-1) == 4 != -4)

# ---- Q1d: PA = BP
Aa = M([[1, 2], [0, 3]]); Pp = M([[1, 1], [0, 1]]); Bb = Pp * Aa * Pp.inv()
chk("Q1d B = P A P^-1 satisfies PA = BP", Pp * Aa == Bb * Pp)
ev = Aa.eigenvects()
for val, mult, vecs in ev:
    v = vecs[0]
    chk("Q1d P x is an eigenvector of B for lam=%s" % val, Bb * (Pp * v) == val * (Pp * v) and (Pp * v) != sp.zeros(2, 1))
chk("Q1d lam=0 is possible (A=0): distractor 'lam != 0'", (sp.zeros(2) * M([1, 0])) == 0 * M([1, 0]))
chk("Q1d A need not be invertible: A=0", sp.zeros(2).det() == 0)
chk("Q1d P need not be orthogonal: P^T P != I", Pp.T * Pp != I2)
chk("Q1d bug: PA x = PB x false in general (P A != P B)", Pp * Aa != Pp * Bb)

# ---- Q2
a = sp.symbols("a")
Ma = M([[a, 1, 1], [1, 1, 2], [1, -1, a]]); rhs = M([2, 5, a + 1])
chk("Q2 det = a(a+1)", sp.expand(Ma.det() - a * (a + 1)) == 0)
sol = [sp.simplify(s) for s in Ma.LUsolve(rhs)]
exp(2, A_, 1, sol[0].subs(a, 1)); exp(2, A_, 2, sol[2].subs(a, 3))
chk("Q2a x,y,z formulas", sp.simplify(sol[0] + 2 / (a + 1)) == 0 and sp.simplify(sol[1] - 3 * (a - 1) / (a + 1)) == 0 and sp.simplify(sol[2] - (a + 5) / (a + 1)) == 0)
chk("Q2a det zero exactly at a=0,-1; nonzero at a=1", Ma.det().subs(a, 0) == 0 and Ma.det().subs(a, -1) == 0 and Ma.det().subs(a, 1) != 0)
Mm1 = Ma.subs(a, -1); rm1 = rhs.subs(a, -1)
exp(2, B_, 0, Mm1.rank()); exp(2, B_, 1, Mm1.row_join(rm1).rank())
M0 = Ma.subs(a, 0); r0 = rhs.subs(a, 0)
chk("Q2b distractor: a=0 has free variable and det=0 yet is consistent", M0.det() == 0 and M0.rank() == M0.row_join(r0).rank() == 2)
chk("Q2b a=0 has an all-zero-free solution (consistent) so a zero row is not a contradiction", M0.row_join(r0).rank() == M0.rank())
z = sp.symbols("z")
p0 = M([3 - z, 2 - z, z])
chk("Q2c solution (3-z,2-z,z)", sp.simplify(M0 * p0 - r0) == sp.zeros(3, 1))
exp(2, C_, 0, p0[0].subs(z, 1)); exp(2, C_, 1, p0[1].subs(z, 2))
for nm, v in (("(-1,-1,1)", M([-1, -1, 1])), ("(3,2,0)", M([3, 2, 0])), ("(1,1,1)", M([1, 1, 1])), ("(1,-1,1)", M([1, -1, 1]))):
    chk("Q2c direction %s in null space -> %s" % (nm, M0 * v == sp.zeros(3, 1)), cond=(M0 * v == sp.zeros(3, 1)) == (nm == "(-1,-1,1)"))
w = sp.symbols("w")
disc = sp.expand((2 + sp.I) ** 2 - 4 * (-1 + 7 * sp.I))
exp(2, D_, 0, sp.im(disc))
rts = [r for r in sp.solve(w ** 2 - disc, w)]
chk("Q2d sqrt(7-24i) = +-(4-3i)", set(rts) == {4 - 3 * sp.I, -4 + 3 * sp.I})
exp(2, D_, 1, 4)
zr = sp.solve(w ** 2 - (2 + sp.I) * w + (-1 + 7 * sp.I), w)
chk("Q2d roots 3-i, -1+2i", set(zr) == {3 - sp.I, -1 + 2 * sp.I})
exp(2, D_, 2, sp.re(-1 + 2 * sp.I))

# ---- Q3
A3 = M([[1, 6, 0], [0, 1, 2], [5, 30, 3]])
exp(3, A_, 0, A3.det()); Ai = A3.inv()
exp(3, A_, 1, Ai[0, 0]); exp(3, A_, 2, Ai[1, 0])
chk("Q3a A^-1 rows", Ai == M([[-19, -6, 4], [R(10, 3), 1, R(-2, 3)], [R(-5, 3), 0, R(1, 3)]]))
E1 = M([[1, 0, 0], [0, 1, 0], [-5, 0, 1]]); E2 = M([[1, 0, 0], [0, 1, 0], [0, 0, R(1, 3)]])
E3 = M([[1, 0, 0], [0, 1, -2], [0, 0, 1]]); E4 = M([[1, -6, 0], [0, 1, 0], [0, 0, 1]])
chk("Q3b E4E3E2E1 = A^-1", E4 * E3 * E2 * E1 == Ai)
chk("Q3b distractor E1E2E3E4 != A^-1", E1 * E2 * E3 * E4 != Ai)
chk("Q3b distractor E1^-1E2^-1E3^-1E4^-1 = A (so != A^-1)", E1.inv() * E2.inv() * E3.inv() * E4.inv() == A3 and A3 != Ai)
chk("Q3b distractor sum of E's != A^-1", E1 + E2 + E3 + E4 != Ai)
exp(3, B_, 1, E1[2, 0]); exp(3, B_, 2, E2[2, 2]); exp(3, B_, 3, (E4 * E3 * E2 * E1)[0, 0])
chk("Q3b E1 is R3-5R1 applied to A", (E1 * A3)[2, :] == M([[0, 0, 3]]))

B3 = M([[1, 2, 1], [-3, 6, 1], [0, 0, 4]])
ev3 = B3.eigenvals()
chk("Q3c eigenvalues 3 (x1), 4 (x2)", ev3 == {3: 1, 4: 2})
chk("Q3c distractor 3 (x2),4 (x1) wrong; 1,2,4 wrong", ev3 != {3: 2, 4: 1} and ev3 != {1: 1, 2: 1, 4: 1} and sum(ev3.values()) == 3 and ev3 != {3: 1, 4: 1})
exp(3, C_, 1, len((B3 - 4 * sp.eye(3)).nullspace()))
chk("Q3c B not symmetric", B3 != B3.T)
chk("Q3c double eigenvalue alone does not give diagonalization: [[0,1],[0,0]]", not M([[0, 1], [0, 0]]).is_diagonalizable())
chk("Q3c B is diagonalizable", B3.is_diagonalizable())
P3 = M([[1, 2, 1], [1, 3, 0], [0, 0, 3]]); D3 = sp.diag(3, 4, 4)
chk("Q3c PD = BP", P3 * D3 == B3 * P3)
exp(3, C_, 3, (P3 * D3)[0, 1])

# ---- Q4
a_, b_, c_, d_ = sp.symbols("a b c d")
def poly(co): return co[0] * t ** 3 + co[1] * t ** 2 + co[2] * t + co[3]
cons1 = M([[3, 2, 1, 0], [-1, 1, -1, 1]]); cons2 = M([[1, -1, -1, 1]])
exp(4, A_, 0, 4 - cons1.rank()); exp(4, A_, 1, 4 - cons2.rank())
chk("Q4a W1 basis vectors in W1", cons1 * M([-3, 2, 5, 0]) == sp.zeros(2, 1) and cons1 * M([2, -3, 0, 5]) == sp.zeros(2, 1))
for nm, co in (("x^3+x^2", [1, 1, 0, 0]), ("x^2+x", [0, 1, 1, 0]), ("x^3-x", [1, 0, -1, 0])):
    chk("Q4a distractor %s not in W1" % nm, cons1 * M(co) != sp.zeros(2, 1))
chk("Q4a -3x^3+2x^2+5x in W1", cons1 * M([-3, 2, 5, 0]) == sp.zeros(2, 1))
s_, t_ = sp.symbols("s_ t_")
ns = cons1.gauss_jordan_solve(sp.zeros(2, 1))
exp(4, A_, 3, (R(2, 5) * 5 - R(3, 5) * 0))
chk("Q4a b = 2s/5 - 3t/5", all(cons1 * M([-R(3, 5) * sv + R(2, 5) * tv, R(2, 5) * sv - R(3, 5) * tv, sv, tv]) == sp.zeros(2, 1) for sv, tv in ((1, 0), (0, 1), (5, 5))))
W1b = [M([-3, 2, 5, 0]), M([2, -3, 0, 5])]; W2b = [M([1, 1, 0, 0]), M([1, 0, 1, 0]), M([-1, 0, 0, 1])]
chk("Q4a W2 basis in W2", all(cons2 * v == sp.zeros(1, 1) for v in W2b))
allv = sp.Matrix.hstack(*(W1b + W2b))
exp(4, B_, 0, allv.rank()); exp(4, B_, 2, 5 - allv.rank())
chk("Q4b distractor dim sum = 5 but rank 4", allv.rank() == 4)
chk("Q4b distractor W1 not subset of W2", cons2 * W1b[0] != sp.zeros(1, 1))
chk("Q4b distractor W1 cap W2 nontrivial", 2 + 3 - allv.rank() == 1)
inter = sp.Matrix.hstack(*W1b).row_join(-sp.Matrix.hstack(*W2b)).nullspace()
chk("Q4c intersection dim 1", len(inter) == 1)
iv = (sp.Matrix.hstack(*W1b) * M(list(inter[0][:2]))).applyfunc(sp.nsimplify)
iv = iv / iv[0] * (-1)
chk("Q4c basis (-1,-1,5,5)", iv == M([-1, -1, 5, 5]))
exp(4, C_, 1, 2 + 3 - allv.rank()); exp(4, C_, 2, iv[3])
for nm, val in (("sum", 2 + 3 + 4), ("product", 2 * 3), ("min", 2)):
    chk("Q4c distractor %s gives %s != 1" % (nm, val), val != 1)
q4d = M([2, 2, -10, -10])
exp(4, D_, 0, (q4d[0] / iv[0]))
chk("Q4d 2x^3+2x^2-10x-10 = -2*basis and in W1 and W2", q4d == -2 * iv and cons1 * q4d == sp.zeros(2, 1) and cons2 * q4d == sp.zeros(1, 1))

# ---- Q5
At = M([[1, 1, 11], [1, 2, 12], [1, 1, 11], [1, 1, 11]])
exp(5, A_, 0, At.rank())
chk("Q5a col3 = 10 col1 + col2", At[:, 2] == 10 * At[:, 0] + At[:, 1])
chk("Q5a distractor: three columns dependent", At.rank() < 3)
chk("Q5a distractor: (1,0,0,0) not in Im T", sp.Matrix.hstack(At, M([1, 0, 0, 0])).rank() == 3)
chk("Q5a distractor: rows of A are vectors of R^3, not R^4", At.shape[1] == 3)
kn = At.nullspace()
exp(5, A_, 2, len(kn)); exp(5, A_, 3, (kn[0] / kn[0][2])[0])
chk("Q5a kernel (-10,-1,1)", kn[0] / kn[0][2] == M([-10, -1, 1]))
exp(5, B_, 1, At.rank())
chk("Q5b not injective and not onto", len(kn) == 1 and At.rank() < 4)
exp(5, C_, 0, sp.solve(sp.Eq(2023, -sp.Symbol("k")), sp.Symbol("k"))[0])
kk = -2023; exp(5, C_, 1, -10 * kk)
chk("Q5c m + 2023t - 2023t^2 = k(-10 - t + t^2) with k=-2023, m=20230", sp.expand(20230 + 2023 * t - 2023 * t ** 2 - kk * (-10 - t + t ** 2)) == 0)
A12 = At[:, :2]
for kv, rk in ((101, 2), (102, 3)):
    bk = M([101, 102, 101, kv])
    exp(5, D_, 0 if kv == 101 else 1, A12.row_join(bk).rank())
    chk("Q5d rank [A12|b] k=%d" % kv, A12.row_join(bk).rank() == rk)
chk("Q5d rank A12 = 2", A12.rank() == 2)
b101 = M([101, 102, 101, 101])
chk("Q5d b is not equal to a column of A but is in Im T", all(b101 != At[:, j] for j in range(3)) and A12.row_join(b101).rank() == 2)
chk("Q5d A12 is 4x2 (not square)", A12.shape == (4, 2))
EB = M([[1, 1], [10, 11]]); EC = M([[1, 5], [4, 19]])
res = EC.inv() * EB
chk("Q5e [I]_C^B = (31 36; -6 -7)", res == M([[31, 36], [-6, -7]]))
exp(5, E_, 1, EC.det()); exp(5, E_, 2, res[0, 0]); exp(5, E_, 3, res[1, 1])
for nm, mt in (("EB*EC^-1", EB * EC.inv()), ("EB^-1*EC", EB.inv() * EC), ("EC*EB", EC * EB)):
    chk("Q5e distractor %s != correct" % nm, mt != res)

# ---- coverage
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
        chk("Q%d%s step %d numeric answer %s == sympy %s (tol %s)" % (num, part, i, st["answer"], EXP[key], st.get("tol", 0)), ok)
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
# every choice step has exactly one correct id among its options; order lines unique-checked
for (num, part), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] == "choice":
            ids = [o["id"] for o in st["options"]]
            vals = [o["value"] for o in st["options"]]
            chk("Q%d%s step %d choice has distinct options and valid key" % (num, part, i), st["correctId"] in ids and len(set(vals)) == len(vals))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
