# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 19A-A (rubric/pitfalls/steps in tools/gen/gen_19A-A.py).
Run: PYTHONUTF8=1 py tools/verify/19A-A/verify_steps_19A-A.py
Every numeric step in tools/raw/19A-A.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug / order line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "19A-A.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_ = "א", "ב", "ג", "ד"
R = sp.Rational
M = sp.Matrix
bad = []
EXP = {}


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def exp(num, part, idx, val):
    EXP[(num, part, idx)] = val if isinstance(val, sp.Float) else sp.nsimplify(val)


a = sp.symbols("a")
# ---- Q1
m1 = M([2, -a, -5]); m2 = M([a, -2, -1]); P12 = M([1, 2, 2]) - M([2, 1, 1])
cr = m1.cross(m2)
chk("Q1 cross product", sp.expand(cr - M([a - 10, 2 - 5 * a, a ** 2 - 4])) == sp.zeros(3, 1))
V = sp.expand(P12.dot(cr))
chk("Q1 V = (a-2)(a-4)", sp.expand(V - (a - 2) * (a - 4)) == 0)
exp(1, A_, 1, V.subs(a, 0)); exp(1, A_, 2, V.subs(a, 3)); exp(1, A_, 3, cr[0].subs(a, 0))
chk("Q1a at a=2: V=0, m1.m2=13, cross != 0; V != 0 elsewhere", V.subs(a, 2) == 0 and m1.dot(m2).subs(a, 2) == 13 and cr.subs(a, 2) != sp.zeros(3, 1) and V.subs(a, 0) != 0)
s, t = sp.symbols("s t")
l1 = lambda av: M([2, 1, 1]) + s * M([2, -av, -5]); l2 = lambda av: M([1, 2, 2]) + t * M([av, -2, -1])
chk("Q1a lines intersect at a=2 and a=4, not at a=3", all(len(sp.solve(list(l1(av) - l2(av)), [s, t], dict=True)) == 1 for av in (2, 4)) and len(sp.solve(list(l1(3) - l2(3)), [s, t], dict=True)) == 0)
n2 = cr.subs(a, 2)
chk("Q1b normal (-8,-8,0)", n2 == M([-8, -8, 0]))
exp(1, B_, 1, n2[0]); exp(1, B_, 2, -(n2.dot(M([2, 1, 1]))))
chk("Q1b plane contains the point of l2 (1,2,2)", n2.dot(M([1, 2, 2])) + 24 == 0)
mm1 = m1.subs(a, 2)
for nm, v in (("m1", mm1), ("P1P2", P12), ("m1+m2", mm1 + m2.subs(a, 2))):
    chk("Q1b distractor %s is not perpendicular to m1" % nm, v.dot(mm1) != 0)
chk("Q1b cross is perpendicular to both directions", n2.dot(mm1) == 0 and n2.dot(m2.subs(a, 2)) == 0)
V0 = V.subs(a, 0); c0 = cr.subs(a, 0)
exp(1, C_, 1, V0)
exp(1, C_, 2, sp.Float(sp.N(c0.norm())))
exp(1, C_, 3, sp.Float(sp.N(sp.Abs(V0) / c0.norm())))
chk("Q1c cross (-10,2,-4), d = 8/sqrt(120)", c0 == M([-10, 2, -4]) and sp.simplify(sp.Abs(V0) / c0.norm() - 8 / sp.sqrt(120)) == 0)
chk("Q1c skew: V != 0 and not parallel; a.b != 0 also at intersecting a=2", V0 != 0 and c0 != sp.zeros(3, 1) and m1.dot(m2).subs(a, 2) != 0)

# ---- Q2
k = sp.symbols("k")
A2 = M([[1, -1, 1], [1, k, 1], [k, k, 1]]); b2 = M([-2, k + 1, 2])
S = A2.row_join(b2)
S1 = S.copy(); S1[1, :] = S1[1, :] - S1[0, :]; S1[2, :] = S1[2, :] - k * S1[0, :]; S1 = S1.applyfunc(sp.expand)
chk("Q2a R1 rows", S1[1, :] == M([[0, k + 1, 0, k + 3]]) and S1[2, :] == M([[0, 2 * k, 1 - k, 2 + 2 * k]]))
exp(2, A_, 0, S1[1, 1].subs(k, 1))
S2 = S1.copy(); S2[1, :] = 2 * S2[1, :] - S2[2, :]; S2 = S2.applyfunc(sp.expand)
chk("Q2a R2 row 2 = (0,2,k-1|4)", S2[1, :] == M([[0, 2, k - 1, 4]]))
exp(2, A_, 1, S2[1, 2].subs(k, 5))
S3 = S2.copy(); S3[2, :] = S3[2, :] - k * S3[1, :]; S3 = S3.applyfunc(sp.expand)
chk("Q2a final row 3 = (0,0,1-k^2 | 2-2k)", S3[2, :] == M([[0, 0, 1 - k ** 2, 2 - 2 * k]]))
exp(2, A_, 2, S3[2, 2].subs(k, 3))


def rk(kv):
    return A2.subs(k, kv).rank(), S.subs(k, kv).rank()


exp(2, B_, 0, rk(1)[0]); exp(2, B_, 1, rk(-1)[1]); exp(2, B_, 2, rk(-1)[0])
chk("Q2b k=1 infinite (2,2); k=-1 none (2,3); k=0 unique (3,3)", rk(1) == (2, 2) and rk(-1) == (2, 3) and rk(0) == (3, 3))
x, y, z = sp.symbols("x y z")
s1 = sp.solve(list(A2.subs(k, 1) * M([x, y, z]) - b2.subs(k, 1)), [x, y], dict=True)[0]
chk("Q2c k=1: y=2, x=-z", s1[y] == 2 and s1[x] == -z)
exp(2, C_, 0, s1[y]); exp(2, C_, 1, s1[x].subs(z, 3))
H = A2.subs(k, 1)
for nm, v, ok in (("(-1,0,1)", [-1, 0, 1], True), ("(1,0,1)", [1, 0, 1], False), ("(0,2,0)", [0, 2, 0], False), ("(-1,2,1)", [-1, 2, 1], False)):
    chk("Q2c direction %s in null space is %s" % (nm, ok), (H * M(v) == sp.zeros(3, 1)) == ok)
sI = sp.solve(list(A2.subs(k, sp.I) * M([x, y, z]) - b2.subs(k, sp.I)), [x, y, z], dict=True)[0]
chk("Q2d solution (-1, 2-i, 1-i)", sp.simplify(sI[x] + 1) == 0 and sp.simplify(sI[y] - (2 - sp.I)) == 0 and sp.simplify(sI[z] - (1 - sp.I)) == 0)
exp(2, D_, 0, sp.re(sI[z])); exp(2, D_, 1, sp.im(sI[z])); exp(2, D_, 2, sp.re(sI[y]))
chk("Q2d (i-1)(1-i) = 2i", sp.expand((sp.I - 1) * (1 - sp.I)) == 2 * sp.I)

# ---- Q3
B = M([[0, 1, 7, 8], [1, 3, 3, 8], [-2, -5, 1, -8]])
e1 = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); e2 = M([[1, 0, 0], [0, 1, 0], [2, 0, 1]]); e3 = M([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
Rm = e3 * e2 * e1 * B
chk("Q3a R", Rm == M([[1, 3, 3, 8], [0, 1, 7, 8], [0, 0, 0, 0]]))
exp(3, A_, 0, Rm.rank())
Ee, Ff, Gg = e1.inv(), e2.inv(), e3.inv()
chk("Q3a B = E F G R with the inverses", Ee * Ff * Gg * Rm == B)
chk("Q3a distractor E=e3,F=e2,G=e1 gives e3 e2 e1 R != B", e3 * e2 * e1 * Rm != B)
chk("Q3a distractor E=e1,F=e2,G=e3 gives e1 e2 e3 R != B", e1 * e2 * e3 * Rm != B)
chk("Q3a distractor E=e3^-1,F=e2^-1,G=e1^-1 gives e3^-1 e2^-1 e1^-1 R != B", e3.inv() * e2.inv() * e1.inv() * Rm != B)
exp(3, A_, 2, Ff[2, 0]); exp(3, A_, 3, Gg[2, 1])
lam, c, d_ = sp.symbols("lam c d")
Aeg = M([[2, 1], [0, 3]]); ve = M([1, 0])
chk("Q3b A(c v) = lam (c v) for c=0 trivially, c v = 0 not an eigenvector", Aeg * (0 * ve) == 2 * (0 * ve) and (0 * ve) == sp.zeros(2, 1))
chk("Q3c w=2v dependent still works", Aeg * (3 * ve + 5 * (2 * ve)) == 2 * (3 * ve + 5 * (2 * ve)))
chk("Q3c A=0 (not invertible) still works", sp.zeros(2) * M([1, 2]) == 0 * M([1, 2]))
chk("Q3c non-symmetric A works", Aeg != Aeg.T and Aeg * ve == 2 * ve)
Ad = sp.diag(1, 2)
vv = M([1, 0]); ww = M([0, 1])
chk("Q3d A(v+w) = (1,2) not an eigenvector", (Ad * (vv + ww))[1] == 2 and not any(Ad * (vv + ww) == l_ * (vv + ww) for l_ in (1, 2)))
exp(3, D_, 1, (Ad * (vv + ww))[1])
chk("Q3d equal eigenvalues: I(e1+e2) = 1*(e1+e2), nonzero, v != w", sp.eye(2) * (vv + ww) == 1 * (vv + ww) and (vv + ww) != sp.zeros(2, 1) and vv != ww)

# ---- Q4
a_, b_ = sp.symbols("a_ b_")
def inW(m): return m[0, 1] == m[1, 0] and m[0, 0] + m[0, 1] - m[1, 1] == 0
exp(4, A_, 1, 2 + 3)
chk("Q4a general form in W", inW(M([[a_, b_], [b_, a_ + b_]])))
for nm, m in (("a-b", M([[1, 1], [1, 0]])), ("-b", M([[1, 1], [-1, 2]])), ("b-a", M([[1, 1], [1, 0]]))):
    chk("Q4a distractor form %s fails at a=b=1" % nm, not inW(m))
kk = sp.Symbol("kk")
chk("Q4a bug (2,2) entry ka+b != k(a+b)", sp.expand(kk * a_ + b_ - kk * (a_ + b_)) != 0)
Wb = [M([[1, 0], [0, 1]]), M([[0, 1], [1, 1]])]
chk("Q4b basis in W and independent", all(inW(m) for m in Wb) and sp.Matrix.hstack(*[M(list(m)) for m in Wb]).rank() == 2)
exp(4, B_, 0, 2)
chk("Q4b distractors: (0 1;1 0) not in W; {I} too small; third set dependent",
    not inW(M([[0, 1], [1, 0]])) and 1 < 2 and inW(M([[1, 1], [1, 2]])) and sp.Matrix.hstack(*[M(list(m)) for m in Wb], M([1, 1, 1, 2])).rank() == 2)
exp(4, B_, 2, M([[3, 2], [2, 5]])[0, 1])
chk("Q4b (3 2;2 5) = 3 I + 2 (0 1;1 1)", M([[3, 2], [2, 5]]) == 3 * Wb[0] + 2 * Wb[1])
Ub = [M([[1, 0], [1, 1]]), M([[0, 1], [-1, -2]]), M([[0, 0], [0, 1]])]
allm = sp.Matrix.hstack(*[M(list(m)) for m in Ub + Wb])
exp(4, C_, 0, allm.rank())
exp(4, C_, 1, sp.Matrix.hstack(*[M(list(m)) for m in Ub]).rank())
chk("Q4c dim(U+W)=4, dim U=3, dim W=2 (so U+W != U, W)", allm.rank() == 4 and 3 < 4 and 2 < 4)
exp(4, D_, 0, 3 + 2 - allm.rank())
Uv = sp.Matrix.hstack(*[M(list(m)) for m in Ub]); Wv = sp.Matrix.hstack(*[M(list(m)) for m in Wb])
ns = Uv.row_join(-Wv).nullspace()
chk("Q4d intersection dim 1", len(ns) == 1)
sol = ns[0] / ns[0][4]
iv = Wv * M(list(sol[3:5]))
chk("Q4d intersection basis (2 1;1 3) with d1=2*d2", iv == M([2, 1, 1, 3]) and sol[3] == 2)
exp(4, D_, 1, sol[3] / sol[4]); exp(4, D_, 2, sol[2])
chk("Q4d (2 1;1 3) in W", inW(M([[2, 1], [1, 3]])))

# ---- Q5
A5 = M([[1, 2 * a - 1, 2], [1, 3, a], [1, 3 * a - 1, 5]])
chk("Q5a det = -(a+6)(a-2)", sp.expand(A5.det() + (a + 6) * (a - 2)) == 0)
exp(5, A_, 0, A5.det().subs(a, 0)); exp(5, A_, 1, A5.det().subs(a, 1))
chk("Q5a singular at -6, 2 (not 6, -2)", set(sp.solve(A5.det(), a)) == {-6, 2} and A5.det().subs(a, 6) != 0 and A5.det().subs(a, -2) != 0)
A51 = A5.subs(a, 1)
exp(5, B_, 0, A51.det())
cof = A51.cofactor_matrix()
exp(5, B_, 1, cof[0, 0]); exp(5, B_, 2, cof[0, 1])
chk("Q5b A^-1 = C^T/7", A51.inv() == cof.T / 7 and A51.inv() == M([[13, -1, -5], [-4, 3, 1], [-1, -1, 2]]) / 7)
minors = sp.Matrix(3, 3, lambda i, j: A51.minor(i, j))
chk("Q5b distractors: C/det, det*C^T, minors^T/det differ from A^-1", cof / 7 != A51.inv() and 7 * cof.T != A51.inv() and minors.T / 7 != A51.inv())
chk("Q5b (A^-1)_{21} = C_12 / det", A51.inv()[1, 0] == cof[0, 1] / 7)
for nm, m in (("(-1 0;0 1)", M([[-1, 0], [0, 1]])), ("(1 1;0 1)", M([[1, 1], [0, 1]])), ("(0 1;-1 0)", M([[0, 1], [-1, 0]])), ("(2 0;0 1/2)", M([[2, 0], [0, R(1, 2)]]))):
    chk("Q5c %s squares to I -> %s" % (nm, m * m == sp.eye(2)), (m * m == sp.eye(2)) == (nm == "(-1 0;0 1)"))
exp(5, C_, 1, M([[1, 0], [0, -1]]).det())
chk("Q5c det(B)^2 = det(B^2) = 1 for B=diag(1,-1)", M([[1, 0], [0, -1]]).det() ** 2 == 1 and M([[1, 0], [0, -1]]) ** 2 == sp.eye(2))
# 5d with random 5x5 and given dets
import random
random.seed(1)
Mx = M(5, 5, lambda i, j: random.randint(-3, 3))
while Mx.det() == 0:
    Mx = M(5, 5, lambda i, j: random.randint(-3, 3))
chk("Q5d det(3M) = 3^5 det M, not 3, 5 or 15 times", Mx.det() != 0 and (3 * Mx).det() == 3 ** 5 * Mx.det() and (3 * Mx).det() not in (3 * Mx.det(), 5 * Mx.det(), 15 * Mx.det()))
exp(5, D_, 1, 3 ** 5 * (-5) ** 2)
exp(5, D_, 2, 2 * R(1, 2))
exp(5, D_, 3, 3 ** 5 * (-5) ** 2 * 1 * (-5))

# ---- Q6
a6, b6, c6, d6, x_ = sp.symbols("a6 b6 c6 d6 x_")
def Tp(a, b, c, d): return M([a - 2 * c + d, 0, b + 2 * c - a - d, b])
chk("Q6a additivity/homogeneity", all(sp.simplify(Tp(*[u + v for u, v in zip(p, q)]) - Tp(*p) - Tp(*q)) == sp.zeros(4, 1) for p, q in (((a6, b6, c6, d6), (1, 2, 3, 4)),)) and sp.simplify(Tp(*[kk * v for v in (a6, b6, c6, d6)]) - kk * Tp(a6, b6, c6, d6)) == sp.zeros(4, 1))
chk("Q6a T(0)=0 is insufficient: a^2 is nonlinear", (2) ** 2 != 2 * 1 ** 2)
exp(6, A_, 1, Tp(1, 0, 1, 0)[2]); exp(6, A_, 2, Tp(1, 0, 0, 0)[2] + Tp(0, 0, 1, 0)[2])
chk("Q6a T(1+x^2) = T(1)+T(x^2)", Tp(1, 0, 1, 0) == Tp(1, 0, 0, 0) + Tp(0, 0, 1, 0))
Tmat = M([[1, 0, -2, 1], [0, 0, 0, 0], [-1, 1, 2, -1], [0, 1, 0, 0]])
chk("Q6 matrix of T agrees with the formula", all(Tmat * M(list(p)) == Tp(*p) for p in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))))
kn = Tmat.nullspace()
chk("Q6b kernel dim 2", len(kn) == 2)
exp(6, B_, 1, len(kn))
for nm, v, ok in (("2+x^2", [2, 0, 1, 0], True), ("1+x^2", [1, 0, 1, 0], False), ("x^3", [0, 0, 0, 1], False), ("x+x^2", [0, 1, 1, 0], False)):
    chk("Q6b %s in ker T is %s" % (nm, ok), (Tmat * M(v) == sp.zeros(4, 1)) == ok)
chk("Q6b -1+x^3 in ker T", Tmat * M([-1, 0, 0, 1]) == sp.zeros(4, 1))
exp(6, B_, 2, 2 * 3 - 1)
exp(6, C_, 0, Tmat.rank())
Im = [M([1, 0, -1, 0]), M([0, 0, 1, 1])]
cs = Tmat.columnspace()
chk("Q6c Im T = span{1-x^2, x^2+x^3}", sp.Matrix.hstack(*cs, *Im).rank() == 2 and sp.Matrix.hstack(*Im).rank() == 2)
chk("Q6c distractors: dependent; x^3 not in Im; 1, x^3 not in Im",
    sp.Matrix.hstack(Im[0], M([-2, 0, 2, 0])).rank() == 1 and sp.Matrix.hstack(*Im, M([0, 0, 0, 1])).rank() == 3
    and sp.Matrix.hstack(*Im, M([1, 0, 0, 0])).rank() == 3)
exp(6, C_, 2, Tp(0, 1, 0, 0)[3])
exp(6, D_, 1, len(kn))
chk("Q6d kernel nontrivial so T not injective", len(kn) > 0)

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
        ok = abs(sp.N(EXP[key]) - st["answer"]) <= st.get("tol", 0) + 1e-12
        chk("Q%d%s step %d numeric answer %s == sympy %s (tol %s)" % (num, part, i, st["answer"], sp.N(EXP[key], 6), st.get("tol", 0)), ok)
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
for (num, part), qq in QS.items():
    for i, st in enumerate(qq.get("steps", [])):
        if st["type"] == "choice":
            ids = [o["id"] for o in st["options"]]
            vals = [o["value"] for o in st["options"]]
            chk("Q%d%s step %d choice has distinct options and valid key" % (num, part, i), st["correctId"] in ids and len(set(vals)) == len(vals))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
