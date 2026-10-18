# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 21A-B (rubric/pitfalls/steps in tools/gen/gen_21A-B.py).
Run: PYTHONUTF8=1 py tools/verify/21A-B/verify_steps_21A-B.py
Every numeric step in tools/raw/21A-B.json must have an expected value computed here with sympy (coverage is asserted,
in order, per item), and the facts behind choice distractors / order / findbug lines are checked. ASCII output only."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "21A-B.json").read_text(encoding="utf-8"))
QS = {(q["num"], q.get("part")): q for q in raw["questions"] if not q.get("hold")}
A_, B_, C_, D_, E_ = "א", "ב", "ג", "ד", "ה"
LET = "אבגדה"
R = sp.Rational
M = sp.Matrix
bad = []
EXP = {}


def chk(name, cond, info=""):
    print(("OK       " if cond else "MISMATCH ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def exp(num, part, *vals):
    EXP[(num, part)] = [sp.nsimplify(v) for v in vals]


a, b, t, z, al, be = sp.symbols("a b t z al be")

# ---- Q1a: antisymmetric of odd order
A3 = M([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]])
chk("Q1a example antisymmetric 3x3 has det 0", A3.T == -A3 and A3.det() == 0)
A5 = sp.diag(5, 1, 1)
chk("Q1a det(-A) = (-1)^3 det A = -5 (n=3, det A=5)", (-A5).det() == -5 == (-1) ** 3 * A5.det())
chk("Q1a bug line -n det A differs from (-1)^n det A (n=3: -3*5 vs -5)", -3 * A5.det() != (-A5).det())
exp(1, A_, (-A5).det(), A3.det())
# ---- Q1b: AB=B with A antisymmetric forces B=0 (so B singular)
p, q, r = sp.symbols("p q r")
Aa = M([[0, p, q], [-p, 0, r], [-q, -r, 0]])
chk("Q1b (I-A) is invertible for every real antisymmetric 3x3 (det = 1+p^2+q^2+r^2), so AB=B forces B=0",
    sp.expand((sp.eye(3) - Aa).det() - (1 + p**2 + q**2 + r**2)) == 0)
exp(1, B_, 0)
chk("Q1b det A det B = det B with det A=0 gives det B=0", sp.solve(sp.Symbol("d") * 0 - sp.Symbol("d"), sp.Symbol("d")) == [0])
# ---- Q1c, Q1d
Cm = M([[1, 0, 0], [5, a, 0], [2, a, 1]])
chk("Q1c det C = a", Cm.det() == a)
C0 = Cm.subs(a, 0)
exp(1, C_, Cm.det().subs(a, 4), C0.rank())
cols = M.hstack(M([1, 5, 2]), M([0, 0, 1]))
chk("Q1c basis (1,5,2),(0,0,1) spans Col C(a=0); distractors fail", cols.rank() == 2 == C0.rank() and M.hstack(cols, C0[:, 0]).rank() == 2 and M.hstack(cols, C0[:, 2]).rank() == 2
    and M.hstack(M([1, 5, 2]), M([0, 0, 0]), M([0, 0, 1])).rank() < 3 and M.hstack(M([1, 5, 2]), M([2, 10, 4])).rank() == 1 and M([1, 5, 2]).rank() < C0.rank())
Dm = M.hstack(M([1, 5, 2]), M([0, 0, 1]), M([0, 1, 0]))
exp(1, D_, 3 - C0.rank(), Dm.det())
chk("Q1d completion by (0,1,0) works; distractors dependent", Dm.det() == -1 and M.hstack(M([1, 5, 2]), M([0, 0, 1]), M([1, 5, 3])).det() == 0
    and M.hstack(M([1, 5, 2]), M([0, 0, 1]), M([0, 0, 2])).det() == 0 and M.hstack(M([1, 5, 2]), M([0, 0, 1]), M([2, 10, 4])).det() == 0)

# ---- Q2
Sys = M([[2, -1, 1, 3], [1, -1, 1, 2], [3, -1, -a, b]])
S1 = Sys.copy(); S1.row_swap(0, 1)
S2 = S1.copy(); S2[1, :] = S2[1, :] - 2 * S2[0, :]; S2[2, :] = S2[2, :] - 3 * S2[0, :]
S2 = S2.applyfunc(sp.expand)
S3 = S2.copy(); S3[2, :] = (S3[2, :] - 2 * S3[1, :]).applyfunc(sp.expand)
chk("Q2a rows as printed", S2[2, :] == M([[0, 2, -a - 3, b - 6]]) and S3[2, :] == M([[0, 0, -a - 1, b - 4]]) and S3[1, :] == M([[0, 1, -1, -1]]))
exp(2, A_, S2[2, 1], S2[2, 2].subs(a, 0), S3[2, 2].subs(a, 0), S3[2, 3].subs(b, 0))
Coef = Sys[:, :3]


def classify(av, bv):
    Mm = Coef.subs(a, av); rr = Sys[:, 3].subs(b, bv)
    rk = Mm.rank(); rka = Mm.row_join(rr).rank()
    return "none" if rk != rka else ("unique" if rk == 3 else "inf")


chk("Q2b classification: a!=-1 unique; a=-1: b=4 inf, else none", all(classify(av, bv) == "unique" for av in (0, 2, 5) for bv in (0, 4)) and classify(-1, 4) == "inf" and classify(-1, 3) == "none")
exp(2, B_, Coef.subs(a, -1).rank(), 4)
sol = sp.linsolve((Coef.subs(a, 2), Sys[:, 3].subs(b, 1)), (sp.Symbol("x"), sp.Symbol("y"), z))
chk("Q2c a=2,b=1 unique solution (1,0,1), 3x-y-az=1", sol == {(1, 0, 1)} and 3 * 1 - 0 - 2 * 1 == 1)
exp(2, C_, 1, 0, 1, 1)
solD = sp.linsolve((Coef.subs(a, -1), Sys[:, 3].subs(b, 4)), (sp.Symbol("x"), sp.Symbol("y"), z))
(xs, ys, zs), = solD
chk("Q2d a=-1,b=4: x=1, y=t-1, z=t", xs == 1 and sp.simplify(ys.subs(zs, t) - (t - 1)) == 0)
exp(2, D_, 3 - Coef.subs(a, -1).rank(), xs, (t - 1).subs(t, 3))
# Q2e
zz = sp.symbols("zz", complex=True)
sols = [0, 4, -2 + 2 * sp.sqrt(3) * sp.I, -2 - 2 * sp.sqrt(3) * sp.I]
chk("Q2e four solutions satisfy 4z = conj(z)^2", all(sp.simplify(4 * s - sp.conjugate(s) ** 2) == 0 for s in sols))
th = lambda k: 2 * sp.pi * k / 3
bads = {"pi k": [sp.pi, 2 * sp.pi], "pi k /3": [sp.pi / 3], "2 pi k": []}
chk("Q2e distractor angles fail: theta=pi (z=-4), theta=pi/3", all(sp.simplify(4 * (4 * sp.exp(sp.I * ang)) - sp.conjugate(4 * sp.exp(sp.I * ang)) ** 2) != 0 for ang in (sp.pi, sp.pi / 3)))
chk("Q2e theta=2 pi k gives only z=4; the set 2pi k/3 gives 3 distinct", len({sp.simplify(4 * sp.exp(sp.I * th(k))) for k in range(3)}) == 3)
exp(2, E_, 4, sp.re(sols[2]), sp.im(sols[2]))

# ---- Q3
A = M([[1, 2, 1], [0, 1, 3], [3, 8, 8]])
exp(3, A_, A.det(), A.inv()[0, 0], A.inv()[2, 2])
chk("Q3a A^-1 as printed", A.inv() == M([[16, 8, -5], [-9, -5, 3], [3, 2, -1]]))


def E(i, j, c):  # R_i -> R_i + c R_j
    m = sp.eye(3); m[i, j] = c; return m


Es = [E(2, 0, -3), E(2, 1, -2), sp.diag(1, 1, -1), E(1, 2, -3), E(0, 2, -1), E(0, 1, -2)]
chk("Q3a E6...E1 A = I; E1...E6 differs", Es[5] * Es[4] * Es[3] * Es[2] * Es[1] * Es[0] * A == sp.eye(3) and Es[0] * Es[1] * Es[2] * Es[3] * Es[4] * Es[5] != A.inv())
B = M([[5, 0, 1], [0, 4, 0], [1, 0, 5]])
lam = sp.symbols("lam")
chk("Q3b char poly (l-4)^2 (l-6); 5 is not an eigenvalue; det B=96", sp.expand((lam * sp.eye(3) - B).det() - (lam - 4) ** 2 * (lam - 6)) == 0
    and (B - 5 * sp.eye(3)).det() != 0 and B.det() == 96 and B.eigenvals() == {4: 2, 6: 1})
exp(3, B_, B.det(), len((B - 4 * sp.eye(3)).nullspace()))
chk("Q3b eigenvectors of 6: (1,0,1) yes; (1,0,-1), (0,1,0) are 4-eigenvectors; (1,1,1) is not an eigenvector",
    B * M([1, 0, 1]) == 6 * M([1, 0, 1]) and B * M([1, 0, -1]) == 4 * M([1, 0, -1]) and B * M([0, 1, 0]) == 4 * M([0, 1, 0])
    and M.hstack(M([1, 1, 1]), B * M([1, 1, 1])).rank() == 2)
P = M([[0, -1, 1], [1, 0, 0], [0, 1, 1]])
D = P.inv() * B * P
exp(3, C_, P.det(), D[2, 2])
chk("Q3c P^-1 B P = diag(4,4,6); permuted diagonals differ", D == sp.diag(4, 4, 6) and D != sp.diag(4, 6, 4) and D != sp.diag(6, 4, 4) and D != sp.diag(6, 6, 4))
Jb = M([[1, 1], [0, 1]])
chk("Q3c distractors: [[1,1],[0,1]] has real eigenvalues but is not diagonalizable; det B != 0 does not imply diagonalizable",
    Jb.eigenvals() == {1: 2} and not Jb.is_diagonalizable() and Jb.det() != 0)

# ---- Q4
Vg = M([[1, 1, 2], [0, 1, 1], [1, 2, 3], [1, 3, 4]])
chk("Q4a rank V = 2; distractor sets", Vg.rank() == 2 and M([[1, 1, 2], [0, 1, 1], [1, 2, 3]]).rank() == 2 and M.hstack(M([1, 1, 2]), M([0, 1, 1]), M([2, 1, 0])).det() != 0)
chk("Q4a (2,1,0) not in V but in W", M.vstack(Vg, M([[2, 1, 0]])).rank() == 3 and 2 - 0 == 2 * 1)
exp(4, A_, Vg.rank(), 3 - 1)
Wb = M([[2, 1, 0], [1, 0, 1]])
chk("Q4a W basis satisfies x-z=2y", all(v[0] - v[2] == 2 * v[1] for v in (Wb[0, :], Wb[1, :])) and Wb.rank() == 2)
All = M.vstack(M([[1, 1, 2], [0, 1, 1]]), Wb)
exp(4, B_, All.rank(), M([[1, 1, 2], [0, 1, 1], [2, 1, 0]]).det())
chk("Q4b V+W = R^3 (rank 3); B_V and B_W alone rank 2; four vectors dependent", All.rank() == 3 and M([[1, 1, 2], [0, 1, 1]]).rank() == 2 and Wb.rank() == 2 and All.shape[0] == 4)
vec = al * M([1, 1, 2]) + be * M([0, 1, 1])
cond = sp.expand(vec[0] - vec[2] - 2 * vec[1])
chk("Q4c x-z-2y = -3al-3be; beta=-al", sp.expand(cond + 3 * al + 3 * be) == 0 and sp.solve(cond, be) == [-al])
exp(4, C_, cond.subs({al: 1, be: 2}), sp.solve(cond.subs(al, 1), be)[0], 1)
chk("Q4c basis (1,0,1) in V cap W; distractors fail", (1 - 1 == 2 * 0) and M.vstack(Vg, M([[1, 0, 1]])).rank() == 2
    and all(not (v[0] - v[2] == 2 * v[1]) for v in ([1, 1, 2], [0, 1, 1])) and M.vstack(Vg, M([[2, 1, 0]])).rank() == 3)
chk("Q4c dimension formula 2+2-1=3", 2 + 2 - 1 == All.rank())
w = M([1, 3, 2])
exp(4, D_, w[0] - w[2] - 2 * w[1])
chk("Q4d (1,3,2) not in W (so not in V cap W), but in V+W=R^3", w[0] - w[2] != 2 * w[1] and All.rank() == 3)

# ---- Q5
def T(a_, b_, c_, d_):
    return M([a_ + 2 * b_ + 8 * c_ + d_, -3 * a_ + 2 * b_ + 5 * d_, a_ + b_ + 5 * c_])


a1, b1, c1, d1, a2, b2, c2, d2, s = sp.symbols("a1 b1 c1 d1 a2 b2 c2 d2 s")
chk("Q5a additivity and homogeneity of T symbolically", sp.expand(T(a1 + a2, b1 + b2, c1 + c2, d1 + d2) - T(a1, b1, c1, d1) - T(a2, b2, c2, d2)) == sp.zeros(3, 1)
    and sp.expand(T(s * a1, s * b1, s * c1, s * d1) - s * T(a1, b1, c1, d1)) == sp.zeros(3, 1))
exp(5, A_, T(1, 1, 1, 1)[0], T(2, 0, 0, 2)[1])
Tm = M([[1, 2, 8, 1], [-3, 2, 0, 5], [1, 1, 5, 0]])
ker = Tm.nullspace()
chk("Q5b kernel basis (-2,-3,1,0), (1,-1,0,1); dim 2", Tm.rank() == 2 and len(ker) == 2 and Tm * M([-2, -3, 1, 0]) == sp.zeros(3, 1) and Tm * M([1, -1, 0, 1]) == sp.zeros(3, 1))
exp(5, B_, Tm.rank(), (-2 * 1 + 0), (-3 * 0 - 1))
chk("Q5b a=-2s+t, b=-3s-t reproduce the kernel", all(Tm * M([-2 * ss + tt, -3 * ss - tt, ss, tt]) == sp.zeros(3, 1) for ss, tt in ((1, 0), (0, 1), (2, 5))))
chk("Q5b distractors: (2,3,1,0) not in kernel, E11 and E12 not in kernel, single vector dim 1 < 2",
    Tm * M([2, 3, 1, 0]) != sp.zeros(3, 1) and Tm * M([1, 0, 0, 0]) != sp.zeros(3, 1) and Tm * M([0, 1, 0, 0]) != sp.zeros(3, 1))
c1v, c2v, c3v = Tm[:, 0], Tm[:, 1], Tm[:, 2]
cc = sp.symbols("cc1 cc2")
solc = sp.solve(list(cc[0] * c1v + cc[1] * c2v - c3v), cc, dict=True)[0]
exp(5, C_, 4 - len(ker), solc[cc[1]])
Imb = M.hstack(c1v, c2v)
chk("Q5c Im basis cols 1,2 (rank 2); col3 = 2col1+3col2; 1 not in Im; {1, 2+x} (echelon cols) not in Im; three vectors dependent",
    Imb.rank() == 2 and solc[cc[0]] == 2 and solc[cc[1]] == 3 and M.hstack(Imb, M([1, 0, 0])).rank() == 3 and M.hstack(Imb, M([2, 1, 0])).rank() == 3
    and M.hstack(Imb, c3v).rank() == 2)
exp(5, D_, 4, 3)
chk("Q5d dim M2 = 4 != 3 = dim R2[x]; Im has dim 2", 4 != 3 and Imb.rank() == 2)

# ---- coverage: numeric steps in raw JSON equal EXP lists in order
n = 0
for key, qq in sorted(QS.items(), key=lambda kv: (kv[0][0], LET.index(kv[0][1]))):
    nums = [st for st in qq.get("steps", []) if st["type"] == "numeric"]
    want = EXP.get(key, [])
    tag = "Q%d%s" % (key[0], "abcde"[LET.index(key[1])])
    if len(nums) != len(want):
        chk("%s numeric count %d vs expected %d" % (tag, len(nums), len(want)), False)
        continue
    for i, (st, wv) in enumerate(zip(nums, want)):
        n += 1
        ok = abs(float(sp.N(wv)) - st["answer"]) <= st.get("tol", 0) + 1e-9
        chk("%s numeric %d: stored %s vs sympy %s" % (tag, i, st["answer"], sp.N(wv, 6)), ok)
for key in EXP:
    if key not in QS:
        chk("orphan expected %s" % (key,), False)
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
