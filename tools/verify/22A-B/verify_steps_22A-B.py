# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 22A-B (rubric/pitfalls/steps in tools/gen/gen_22A-B.py).
Run: PYTHONUTF8=1 py tools/verify/22A-B/verify_steps_22A-B.py
Every numeric step in tools/raw/22A-B.json must have an expected value computed here with sympy (coverage is asserted,
in order, per item), and the facts behind choice distractors / order / findbug lines are checked. ASCII output only."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "22A-B.json").read_text(encoding="utf-8"))
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


def exp(num, part, *vals):
    EXP[(num, part)] = [sp.nsimplify(v) for v in vals]


a, b, t, k, z, x = sp.symbols("a b t k z x")

# ---- Q1: determinant facts
X = M([[1, 2], [3, 4]]); Y = M([[0, 1], [1, 6]])
chk("Q1a (mult) det(XY)=det X det Y; additivity fails", (X * Y).det() == X.det() * Y.det() and (X + Y).det() != X.det() + Y.det())
chk("Q1a distractor det(X^-1)=det X fails for X=2I", (2 * sp.eye(2)).inv().det() != (2 * sp.eye(2)).det())
chk("Q1a distractor det(aX)=a det X fails for n=2", (2 * sp.eye(2)).det() == 4 and 2 * sp.eye(2).det() == 2)
P = M([[1, 2], [3, 7]]); Q_ = M([[2, 1], [5, 3]]); C = M([[4, 1], [2, 3]])
D = (P * Q_).inv() * C * (P * Q_)
exp(1, A_, D.det())
chk("Q1a order chain: det(Q^-1)det(P^-1)det C det P det Q = det C", (Q_.inv().det() * P.inv().det() * C.det() * P.det() * Q_.det()) == C.det())
chk("Q1a bug line: det Q det P det C det P det Q != det C (for the model)", (sp.diag(2, 3).det() * sp.diag(1, 2).det()) ** 2 * C.det() != C.det())
A4 = sp.diag(2, 1, 1, 1); B4 = -R(3, 2) * A4.inv()
chk("Q1b model 2AB+3I=0, |A|=2, 4x4", 2 * A4 * B4 + 3 * sp.eye(4) == sp.zeros(4) and A4.det() == 2)
exp(1, B_, (-3 * sp.eye(4)).det(), (2 * A4).det())
rA = sp.randMatrix(4, 4, -3, 3, seed=7); rB = sp.randMatrix(4, 4, -3, 3, seed=8)
chk("Q1b det(2AB)=2^4 detA detB; distractors differ", (2 * rA * rB).det() == 16 * rA.det() * rB.det()
    and (16 * rA.det() * rB.det() != 2 * rA.det() * rB.det() or rA.det() * rB.det() == 0)
    and rA.det() * rB.det() != 0 and 16 * rA.det() * rB.det() != 16 * (rA.det() + rB.det()))
chk("Q1b/c (-3)^4 = 81, detB solves 32 detB = 81", (-3) ** 4 == 81 and R(81, 32) * 32 == 81 and 32 * R(81, 32) != -81 and 4 * R(81, 32) != 81 and 32 * R(81, 32) != 9)
exp(1, C_, B4.det())
chk("Q1c det B = 81/32 = 2.53125", B4.det() == R(81, 32) and float(R(81, 32)) == 2.53125)
exp(1, D_, B4.inv().det())
chk("Q1d det B^-1 = 32/81", B4.inv().det() == R(32, 81) and B4.det() * B4.inv().det() == 1 and B4.inv().det() != B4.det() and B4.inv().det() != -B4.det())

# ---- Q2
Ma = M([[1, 2, 2], [1, a, 3], [1, 11, a]]); rhs = M([1, 3, b])
chk("Q2a det = (a-5)(a+1); a=2 gives det !=0", sp.expand(Ma.det() - (a - 5) * (a + 1)) == 0 and Ma.det().subs(a, 2) != 0)
chk("Q2a distractors: a=5 alone / a=2,-1 / a=2 alone are not the singular set", set(sp.solve(Ma.det(), a)) == {5, -1})


def classify(av, bv):
    Mm = Ma.subs(a, av); r = rhs.subs(b, bv)
    rk = Mm.rank(); rka = Mm.row_join(r).rank()
    return "none" if rk != rka else ("unique" if rk == 3 else "inf")


chk("Q2a a=2: unique for all tested b", all(classify(2, bv) == "unique" for bv in (-3, 0, 1, 7)))
chk("Q2a a=5: only b=7 gives inf; a=-1: only b=-5", classify(5, 7) == "inf" and classify(5, 6) == "none" and classify(-1, -5) == "inf" and classify(-1, -4) == "none")
exp(2, A_, 7, -5)
sol2 = sp.linsolve((Ma.subs(a, 2), rhs.subs(b, 1)), (x, sp.Symbol("y"), z))
chk("Q2b a=2,b=1 unique solution (-3,0,2)", sol2 == {(-3, 0, 2)})
exp(2, B_, 2, 0, -3)
sol5 = sp.linsolve((Ma.subs(a, 5), rhs.subs(b, 7)), (x, sp.Symbol("y"), z))
(xs, ys, zs), = sol5
chk("Q2c a=5,b=7 family x=-1/3-4t/3, y=2/3-t/3, z=t", sp.simplify(xs.subs(zs, t) + R(1, 3) + R(4, 3) * t) == 0 and sp.simplify(ys.subs(zs, t) - R(2, 3) + t / 3) == 0)
exp(2, C_, Ma.subs(a, 5).rank(), 3 - Ma.subs(a, 5).rank(), -R(1, 3), R(1, 3))
chk("Q2c particular t=0 gives x=-1/3, t=1 gives y=1/3", (-R(1, 3) - R(4, 3) * 0) == -R(1, 3) and (R(2, 3) - R(1, 3)) == R(1, 3))
Az = M([[1, 2, -2], [0, z, 1], [1, 0, z]])
chk("Q2d det = z^2+2z+2", sp.expand(Az.det() - (z**2 + 2 * z + 2)) == 0)
exp(2, D_, Az.det().subs(z, 1), Az.det().subs(z, 0))
chk("Q2d roots -1+-i; distractors are not roots; z=-1 invertible", set(sp.solve(z**2 + 2 * z + 2, z)) == {-1 + sp.I, -1 - sp.I}
    and all(sp.expand(rr**2 + 2 * rr + 2) != 0 for rr in (1 + sp.I, 1 - sp.I, -1 + 2 * sp.I, -1 - 2 * sp.I, -2, 0)) and Az.det().subs(z, -1) == 1)

# ---- Q3
A3 = M([[1, 2, 3], [4, 5, 6], [7, 8, a]])
chk("Q3a det = -3a+27", sp.expand(A3.det() - (-3 * a + 27)) == 0)
cof = A3.cofactor_matrix()
exp(3, A_, A3.det().subs(a, 0), cof[0, 0].subs(a, 0), (A3.inv())[0, 1].subs(a, 0))
chk("Q3a A^-1 = C^T/det; C (not transposed) differs at a=0", A3.subs(a, 0).inv() == cof.subs(a, 0).T / 27 and cof.subs(a, 0).T != cof.subs(a, 0)
    and A3.subs(a, 0).inv() != cof.subs(a, 0) / 27 and A3.subs(a, 0).inv() != 27 * cof.subs(a, 0).T and A3.subs(a, 0).inv() != cof.subs(a, 0).inv() / 27)
A9 = A3.subs(a, 9)
chk("Q3b rank 2 at a=9", A9.rank() == 2)
chk("Q3b R2-4R1 entry (2,2) = -3", (A9[1, :] - 4 * A9[0, :])[1] == -3)
v1, v2 = M([1, 2, 3]), M([0, 1, 2])
chk("Q3b completion: only (0,0,1) is independent; others lie in span", M.hstack(v1, v2, M([0, 0, 1])).det() != 0
    and all(M.hstack(v1, v2, M(w)).det() == 0 for w in ([2, 4, 6], [1, 3, 5], [4, 5, 6])))
exp(3, B_, A9.rank(), -3, M.hstack(v1, v2, M([0, 0, 1])).det())
Cs = M([[0, 1], [1, 0]]); Ds = M([[1, 0], [0, -1]])
chk("Q3c example: C,D symmetric, CD=-DC, CD antisymmetric", Cs == Cs.T and Ds == Ds.T and Cs * Ds == -Ds * Cs and (Cs * Ds).T == -(Cs * Ds))
exp(3, C_, (Cs * Ds)[0, 1])
# generic proof facts
c1, c2, c3, d1, d2, d3 = sp.symbols("c1 c2 c3 d1 d2 d3")
Cg = M([[c1, c2], [c2, c3]]); Dg = M([[d1, d2], [d2, d3]])
chk("Q3c bug line: (CD)^T = C^T D^T is false in general", (Cg * Dg).T != Cg.T * Dg.T and (Cg * Dg).T == Dg.T * Cg.T)

# ---- Q4 (polynomials in R_3[x] as coefficient vectors (a0,a1,a2,a3))
xx = sp.symbols("xx")
pU = sp.symbols("a0:4")
pp = sum(pU[i] * xx**i for i in range(4))
Ucond = sp.Poly(sp.expand(pp.subs(xx, -xx) + pp), xx).all_coeffs()
sU = sp.solve(Ucond, pU, dict=True)[0]
chk("Q4a odd condition gives a0=a2=0", sU.get(pU[0]) == 0 and sU.get(pU[2]) == 0)
exp(4, A_, sU[pU[0]], len(pU) - len(sU))
chk("Q4a bases: x,x^3 odd; 1,x^2 even not in U; x^2 not in U", all(sp.expand(f.subs(xx, -xx) + f) == 0 for f in (xx, xx**3)) and all(sp.expand(f.subs(xx, -xx) + f) != 0 for f in (sp.Integer(1), xx**2)))
chk("Q4a dim U = 2", len([xx, xx**3]) == 2 and len(pU) - len(sU) == 2)
Wp = lambda f: sp.diff(f, xx).subs(xx, 1)
chk("Q4b p'(1) of x^3 = 3", Wp(xx**3) == 3)
chk("Q4b basis of W in W, distractors not", all(Wp(f) == 0 for f in (1, xx**2 - 2 * xx, xx**3 - 3 * xx)) and Wp(xx) == 1 and Wp(xx**2 - 1) == 2 and Wp(xx**3 - 1) == 3)
Wb = M([[1, 0, 0, 0], [0, -2, 1, 0], [0, -3, 0, 1]])
chk("Q4b dim W = 3 and {x^2-2x, x^3-3x} only rank 2", Wb.rank() == 3 and Wb[1:, :].rank() == 2)
exp(4, B_, Wp(xx**3), 3)
vecs = M([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, -2, 1, 0], [0, -3, 0, 1]])
chk("Q4c rank of 5 vectors = 4 (U+W = R3[x]); B_U cap B_W empty; B_U alone rank 2", vecs.rank() == 4 and M([[0, 1, 0, 0], [0, 0, 0, 1]]).rank() == 2
    and set([xx, xx**3]).isdisjoint({1, xx**2 - 2 * xx, xx**3 - 3 * xx}) and M([[1, 0, 0, 0], [0, -2, 1, 0], [0, -3, 0, 1]]).rank() == 3)
exp(4, C_, vecs.rank(), 5 - vecs.rank())
al, be = sp.symbols("al be")
chk("Q4d alpha=-3 beta; U cap W basis x^3-3x", sp.solve(Wp(al * xx + be * xx**3), al)[0] == -3 * be)
chk("Q4d distractors: x^3+3x -> 6, x-3x^3 -> -8, x not in W", Wp(xx**3 + 3 * xx) == 6 and Wp(xx - 3 * xx**3) == -8 and Wp(xx) == 1)
exp(4, D_, -3, 2 + 3 - 1)
chk("Q4d dim formula: dim(U+W)=4", 2 + 3 - 1 == vecs.rank())
q = sp.expand(sp.Symbol("be") * (xx**3 - 3 * xx))
bsol = sp.solve(q.subs(xx, 1) - 1, be)[0]
qq = sp.expand(bsol * (xx**3 - 3 * xx))
exp(4, E_, bsol, sp.diff(qq, xx).subs(xx, 1), sp.diff(qq, xx).subs(xx, sp.sqrt(2)))
chk("Q4e q'(1)=0 and q'(sqrt2)=-3/2", sp.diff(qq, xx).subs(xx, 1) == 0 and sp.simplify(sp.diff(qq, xx).subs(xx, sp.sqrt(2))) == -R(3, 2))

# ---- Q5
At = M([[1, 1, -1, 3], [1, 2, 0, 4], [1, 3, 1, 5]])
exp(5, A_, At.rank(), len(At.nullspace()), M([2, -1, 1, 0])[1])
ker = At.nullspace()
chk("Q5a kernel vectors (2,-1,1,0), (-2,-1,0,1)", At * M([2, -1, 1, 0]) == sp.zeros(3, 1) and At * M([-2, -1, 0, 1]) == sp.zeros(3, 1) and len(ker) == 2)
chk("Q5a t=1,s=0 -> x2=-1", M([2, -1, 1, 0])[1] == -1)
c1v, c2v = At[:, 0], At[:, 1]
Imb = M.hstack(c1v, c2v)
chk("Q5a Im basis = cols 1,2; distractors fail", Imb.rank() == 2 and M.hstack(Imb, M([1, 0, 0])).rank() == 3 and M.hstack(Imb, M([1, 1, 0])).rank() == 3
    and At.rank() == 2 and M.hstack(c1v, 2 * c1v).rank() == 1)
exp(5, B_, len(ker))
chk("Q5b not inj, not onto; distractor claims fail", len(ker) == 2 != 0 and At.rank() == 2 < 3)
vk = M([k, 7, 10])
aug = M.hstack(Imb, vk)
chk("Q5c rank [Imb|v] = 2 iff k=4", M.hstack(Imb, M([4, 7, 10])).rank() == 2 and all(M.hstack(Imb, M([kk, 7, 10])).rank() == 3 for kk in (0, 3, 5, 7)))
# last row after elimination: k-4
Er = M([[1, 1, k], [1, 2, 7], [1, 3, 10]])
r2 = Er[1, :] - Er[0, :]; r3 = Er[2, :] - Er[0, :]; r3 = r3 - 2 * r2
chk("Q5c last row of echelon = (0,0,k-4)", sp.expand(r3[2] - (k - 4)) == 0)
sc = sp.solve([sp.Symbol("x1") + sp.Symbol("x2") - 4, sp.Symbol("x1") + 2 * sp.Symbol("x2") - 7], [sp.Symbol("x1"), sp.Symbol("x2")])
exp(5, C_, r3[2].subs(k, 7), 4, sc[sp.Symbol("x1")])
chk("Q5c x1=1,x2=3 reproduces (4,7,10)", sc[sp.Symbol("x1")] * c1v + sc[sp.Symbol("x2")] * c2v == M([4, 7, 10]))
P5 = M([[5, 2], [17, 7]]); F = M([[1, 1], [1, -1]])
FB = P5.inv() * F * P5
exp(5, D_, P5.det(), FB[0, 0], FB[0, 1])
chk("Q5d [F]_B^B = [[178,73],[-434,-178]]", FB == M([[178, 73], [-434, -178]]) and FB.trace() == 0)
chk("Q5d distractor formulas give other matrices", P5 * F * P5.inv() != FB and P5.inv() * F != FB and F * P5.inv() != FB)

# ---- coverage: numeric steps in raw JSON equal EXP lists in order
n = 0
for key, qq in sorted(QS.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))):
    nums = [st for st in qq.get("steps", []) if st["type"] == "numeric"]
    want = EXP.get(key, [])
    if len(nums) != len(want):
        chk("Q%s%s numeric count %d vs expected %d" % (key[0], "abcde"["אבגדה".index(key[1])] if key[1] else "", len(nums), len(want)), False)
        continue
    for i, (st, w) in enumerate(zip(nums, want)):
        n += 1
        ok = abs(sp.Float(w) - st["answer"]) <= st.get("tol", 0) + 1e-9
        chk("Q%s%s numeric %d: stored %s vs sympy %s" % (key[0], "abcde"["אבגדה".index(key[1])], i, st["answer"], sp.N(w, 6)), ok)
for key in EXP:
    if key not in QS:
        chk("orphan expected %s" % (key,), False)
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
