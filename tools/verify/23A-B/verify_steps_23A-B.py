# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 23A-B (rubric/pitfalls/steps in tools/gen/gen_23A-B.py).
Run: PYTHONUTF8=1 py tools/verify/23A-B/verify_steps_23A-B.py
Every numeric step in tools/raw/23A-B.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "23A-B.json").read_text(encoding="utf-8"))
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
    EXP[(num, part, idx)] = sp.nsimplify(val) if not isinstance(val, float) else val


x, a, b, c, d, l = sp.symbols("x a b c d l")

# ---- Q1a  A^3 - A + I = 0  =>  A(I-A^2) = I ; the wrong line A^3 - A = I contradicts the hypothesis
chk("Q1a x*(1-x^2) = 1 mod x^3-x+1", sp.rem(sp.expand(x * (1 - x**2) - 1), x**3 - x + 1, x) == 0)
chk("Q1a bug line A^3-A=I is false (A^3-A = -I)", sp.rem(sp.expand((x**3 - x) - 1), x**3 - x + 1, x) != 0 and sp.rem(sp.expand((x**3 - x) + 1), x**3 - x + 1, x) == 0)
chk("Q1a wrong inverse A^2-I would give A(A^2-I) = -I", sp.rem(sp.expand(x * (x**2 - 1) + 1), x**3 - x + 1, x) == 0)

# ---- Q1b
B0 = V([[0, 1], [0, 0]]); C0 = V([[0, 0], [1, 0]])
chk("Q1b B^2=C^2=0, BC!=CB", B0**2 == sp.zeros(2) and C0**2 == sp.zeros(2) and B0 * C0 != C0 * B0)
exp(1, B_, 1, ((B0 * C0) ** 5)[0, 0])
chk("Q1b (BC)^5 != B^5C^5 without commutation", (B0 * C0) ** 5 != B0**5 * C0**5)
Bn = V([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
chk("Q1b bug line: B^2 != 0 fails for n<k only when k=3 (B^3=0, B^2!=0)", Bn**3 == sp.zeros(3) and Bn**2 != sp.zeros(3))
chk("Q1b distractor: nilpotent B is not invertible", Bn.det() == 0 and B0.det() == 0)

# ---- Q1c
D0 = V([[1, 0], [0, 0]]); E0 = V([[0, 0], [0, 1]])
chk("Q1c DE=0", D0 * E0 == sp.zeros(2))
exp(1, C_, 3, D0.det() + E0.det())
Dg = V([[1, 1], [0, 1]]); Eg = V([[1, 2], [3, 4]])
chk("Q1c bug line: right-multiplying by D^-1 does not isolate E (D E D^-1 != E)", Dg * Eg * Dg.inv() != Eg)

# ---- Q1d
F = V([[a, b], [c, d]])
chk("Q1d charpoly F = charpoly F^T", sp.expand(F.charpoly(l).as_expr() - F.T.charpoly(l).as_expr()) == 0)
F0 = V([[1, 2], [3, 4]])
exp(1, D_, 1, (F0.T - 0 * sp.eye(2)).det())
chk("Q1d det(F^T) = det(F) for the numeric example", F0.T.det() == F0.det() == -2)
Fa = V([[1, 1], [0, 2]])
ev1 = [v for (val, m, vs) in Fa.eigenvects() if val == 1 for v in vs][0]
ev1T = [v for (val, m, vs) in Fa.T.eigenvects() if val == 1 for v in vs][0]
chk("Q1d bug line: eigenvectors differ ((1,0) vs (1,-1))", list(ev1) == [1, 0] and sp.Matrix.hstack(ev1T, V([1, -1])).rank() == 1 and sp.Matrix.hstack(ev1, ev1T).rank() == 2)
chk("Q1d charpoly of that example equal", Fa.charpoly(l).as_expr() == Fa.T.charpoly(l).as_expr())

# ---- Q2 system with parameter
Ma = V([[a, 2 * a, 3 * a], [a, 2 * a + 1, 3 * a + 1], [a, 2 * a - 1, 0]]); rhs = V([4 * a, 4 * a + 1, 2 - a])
Aug = Ma.row_join(rhs)
s1 = Aug.copy(); s1[1, :] = (Aug[1, :] - Aug[0, :]).applyfunc(sp.expand); s1[2, :] = (Aug[2, :] - Aug[0, :]).applyfunc(sp.expand)
exp(2, A_, 0, s1[1, 3]); exp(2, A_, 1, s1[2, 1])
s2 = s1.copy(); s2[2, :] = (s1[2, :] + s1[1, :]).applyfunc(sp.expand)
exp(2, A_, 3, s2[2, 2].subs(a, 2))
# distractor operations: new coefficient of y in row 3 (row2 has 1)
r2y, r3y = s1[1, 1], s1[2, 1]
chk("Q2a choice: R3+R2 -> y coeff 0; R3-R2 -> -2; R3+2R2 -> 1; R3-R1 -> -1-2a+... != 0",
    sp.expand(r3y + r2y) == 0 and sp.expand(r3y - r2y) == -2 and sp.expand(r3y + 2 * r2y) == 1 and sp.expand(s1[2, 1] - Aug[0, 1]) != 0)
chk("Q2a final row3 = (0,0,1-3a,3-5a)", s2[2, :] == V([[0, 0, 1 - 3 * a, 3 - 5 * a]]))
exp(2, B_, 0, float(sp.solve(1 - 3 * a, a)[0]))
exp(2, B_, 1, float(s2[2, 3].subs(a, R(1, 3))))
exp(2, B_, 2, Ma.subs(a, 2).det())
chk("Q2b det(coeff) = a(1-3a)", sp.factor(Ma.det()) == a * (1 - 3 * a) or sp.expand(Ma.det() - a * (1 - 3 * a)) == 0, str(sp.factor(Ma.det())))
M0 = Ma.subs(a, 0); r0 = rhs.subs(a, 0)
chk("Q2b a=0 infinite (rank A = rank [A|b] = 2 < 3)", M0.rank() == 2 and M0.row_join(r0).rank() == 2)
chk("Q2b distractors: a=0 is not none/unique/exactly-two", M0.row_join(r0).rank() == M0.rank() and M0.rank() < 3)
chk("Q2b a=1/3 inconsistent", Ma.subs(a, R(1, 3)).rank() < Ma.subs(a, R(1, 3)).row_join(rhs.subs(a, R(1, 3))).rank())
sol = M0.gauss_jordan_solve(r0)
chk("Q2c a=0 general solution (t,-2,3)", sol[0].subs(sol[1][0], 7) == V([7, -2, 3]) if len(sol[1]) == 1 else False, str(sol[0].T))
exp(2, C_, 0, -2); exp(2, C_, 1, 3)
exp(2, C_, 2, 3 - M0.rank())
chk("Q2c particular check", M0 * V([5, -2, 3]) == r0)

# ---- Q2d  z^4 + (2+i) z = 0
w = -2 - sp.I
exp(2, D_, 0, sp.Abs(w) ** 2)
ang = float(sp.arg(w)) * 180 / float(sp.pi) % 360
exp(2, D_, 1, round(ang, 2))
exp(2, D_, 2, round(float(sp.root(5, 6)), 3))
ang4 = (ang + 720) / 3
exp(2, D_, 3, round(ang4, 2))
zz = sp.symbols("zz")
nroots = sp.Poly(zz**4 + (2 + sp.I) * zz, zz).nroots(n=20)
exp(2, D_, 4, len(set(round(complex(r).real, 8) + 1j * round(complex(r).imag, 8) for r in nroots)))
z4 = 5 ** (1 / 6) * complex(sp.cos(ang4 * sp.pi / 180), sp.sin(ang4 * sp.pi / 180))
chk("Q2d z4 = 5^(1/6) cis(308.86) is a root", abs(z4**4 + (2 + 1j) * z4) < 1e-9)
chk("Q2d distractor angle 26.57 gives z^3 = -2-i? no", abs(5 ** 0.5 * complex(sp.cos(26.565 * sp.pi / 180) + sp.I * sp.sin(26.565 * sp.pi / 180)) - complex(-2 - 1j)) > 1)

# ---- Q3 inverse
A3 = V([[1, -2, -2], [0, -1, 0], [-1, 2, 3]])
Ai = A3.inv()
exp(3, A_, 0, A3.det())
E1 = sp.eye(3); E1[2, :] = E1[2, :] + E1[0, :]
exp(3, A_, 1, (E1 * A3)[2, 2])
exp(3, A_, 2, Ai[0, 1]); exp(3, A_, 3, Ai[0, 2])
chk("Q3a A^-1 = [[3,-2,2],[0,-1,0],[1,0,1]]", Ai == V([[3, -2, 2], [0, -1, 0], [1, 0, 1]]))
Ea = [V([[1, 2, 0], [0, 1, 0], [0, 0, 1]]), V([[1, 0, 2], [0, 1, 0], [0, 0, 1]]), V([[1, 0, 0], [0, -1, 0], [0, 0, 1]]), V([[1, 0, 0], [0, 1, 0], [1, 0, 1]])]
prod = Ea[0] * Ea[1] * Ea[2] * Ea[3]
chk("Q3b product = A^-1", prod == Ai)
chk("Q3b choice: first op rightmost; reversed product differs", Ea[3] * Ea[2] * Ea[1] * Ea[0] != Ai)
exp(3, B_, 1, prod.det()); exp(3, B_, 2, prod[0, 0])
chk("Q3b first op E(R3+R1) applied to A then R2->-R2, R1+2R3, R1+2R2 gives I", Ea[0] * Ea[1] * Ea[2] * Ea[3] * A3 == sp.eye(3))

# ---- Q3c
B3 = V([[3, 1, 1], [1, 3, 1], [0, 0, 2]])
exp(3, C_, 0, (0 * sp.eye(3) - B3).det())
exp(3, C_, 1, 3 - (2 * sp.eye(3) - B3).rank())
P = V([[-1, -1, 1], [1, 0, 1], [0, 1, 0]]); Dg3 = sp.diag(2, 2, 4)
chk("Q3c BP = PD", B3 * P == P * Dg3 and P.det() != 0)
exp(3, C_, 3, (B3 * P)[0, 2])
chk("Q3c eigenvalues 2,2,4 (not three distinct), B not symmetric, det!=0 does not give diagonalizability",
    sorted(B3.eigenvals(multiple=True)) == [2, 2, 4] and B3 != B3.T and B3.det() != 0)
chk("Q3c a nondiagonalizable matrix with det != 0 exists", V([[1, 1], [0, 1]]).det() != 0 and not V([[1, 1], [0, 1]]).is_diagonalizable())

# ---- Q4  R3[x]
p = a * x**3 + b * x**2 + c * x + d
cond = sp.Eq(p.subs(x, 1), sp.diff(p, x).subs(x, 1))
chk("Q4a constraint is d = 2a+b", sp.solve(cond, d) == [2 * a + b])
exp(4, A_, 0, (2 * a + b).subs({a: 3, b: 1}))
q1 = x**3 + 2
exp(4, A_, 1, sp.diff(q1, x).subs(x, 1))
chk("Q4a p(1)=p'(1) for the three basis polynomials", all(q.subs(x, 1) == sp.diff(q, x).subs(x, 1) for q in [x**3 + 2, x**2 + 1, x]))
exp(4, A_, 2, 4 - 1)
Ucoef = V([[1, 0, 0, 2], [0, 1, 0, 1], [0, 0, 1, 0]])      # rows: coefficients of x^3,x^2,x,1
Wcoef = V([[0, 1, 0, 0], [0, 0, 0, 1]])
chk("Q4a dim U = 3 (basis independent and constraint rank 1)", Ucoef.rank() == 3)
chk("Q4b W basis x^2, 1 even; choice x^2+5 even, others not",
    sp.expand((x**2 + 5).subs(x, -x) - (x**2 + 5)) == 0 and all(sp.expand(q.subs(x, -x) - q) != 0 for q in [x**3 + x**2, x + 1, x**3]))
exp(4, B_, 1, 2)
exp(4, B_, 2, Wcoef.rank())
chk("Q4b even constraint forces a=c=0", sp.solve(sp.Poly(sp.expand(p.subs(x, -x) - p), x).coeffs(), [a, c], dict=True) == [{a: 0, c: 0}])
exp(4, C_, 0, sp.solve(sp.Poly(sp.expand(x**3 - (x**3 + 2) - c), x).coeffs()[-1], c)[0])
allp = V([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 2], [0, 1, 0, 1], [0, 0, 1, 0]])
exp(4, C_, 1, allp.rank())
exp(4, C_, 2, allp.rank())
# intersection
al, be, ga, de, ep = sp.symbols("al be ga de ep")
eqs = sp.Poly(sp.expand(al * (x**3 + 2) + be * (x**2 + 1) + ga * x - (de * x**2 + ep)), x).coeffs()
sol_i = sp.solve(eqs, [al, ga, de, ep], dict=True)[0]
chk("Q4d intersection: a=0, c=0, d=b", sol_i[al] == 0 and sol_i[ga] == 0 and sol_i[de] == be)
f = x**2 + 1
chk("Q4d x^2+1 in U (p(1)=2=p'(1)) and in W", f.subs(x, 1) == sp.diff(f, x).subs(x, 1) == 2 and f.subs(x, -x) == f)
chk("Q4d distractors: x^2 not in U, x^3+2 not even, x+1 not even",
    (x**2).subs(x, 1) != sp.diff(x**2, x).subs(x, 1) and (x**3 + 2).subs(x, -x) != x**3 + 2 and (x + 1).subs(x, -x) != x + 1)
exp(4, D_, 1, 1)
exp(4, D_, 2, 3 + 2 - 1)
chk("Q4d dim formula: rank(U basis + W basis) = 4 = 3 + 2 - 1", allp.rank() == 3 + 2 - 1 and Ucoef.rank() + Wcoef.rank() - 1 == 4)
chk("Q4d dim(U cap W) = dim U + dim W - dim(U+W) = 1", Ucoef.rank() + Wcoef.rank() - allp.rank() == 1)

# ---- Q5
Tm = V([[1, 1, 3, 1], [1, 1, 3, 1], [1, 2, 4, 1], [1, 3, 5, 5]])
exp(5, A_, 0, Tm.rank())
rr, piv = Tm.rref()
chk("Q5a pivot columns are 1,2,4", piv == (0, 1, 3), str(piv))
chk("Q5a col3 = 2*col1 + col2 (dependent)", Tm[:, 2] == 2 * Tm[:, 0] + Tm[:, 1])
exp(5, A_, 2, len(Tm.nullspace()))
ker = Tm.nullspace()[0]
chk("Q5a kernel vector (-2,-1,1,0)", list(ker / ker[2]) == [-2, -1, 1, 0])
exp(5, A_, 3, (ker / ker[2])[0])
chk("Q5b not injective and not onto", len(Tm.nullspace()) == 1 and Tm.rank() < 4)
exp(5, B_, 1, 4 - Tm.rank())
chk("Q5b distractors: ker nontrivial, rank<4", len(Tm.nullspace()) != 0 and Tm.rank() != 4)
kk = ker / ker[2]
tt = sp.symbols("tt")
sol_c = sp.solve([tt * kk[1] - 5, tt * kk[2] + 5], [tt], dict=True)[0]
exp(5, C_, 0, sol_c[tt]); exp(5, C_, 1, sol_c[tt] * kk[0]); exp(5, C_, 2, sol_c[tt] * kk[3])
chk("Q5c (10,5,-5,0) in Ker T", Tm * V([10, 5, -5, 0]) == sp.zeros(4, 1))
Bm = V([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]])      # columns are B vectors? build columns
Bcols = V([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]).T
Perm = V([[0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]])
TCB = Perm * Tm * Bcols
chk("Q5d [T]_C^B equals the official matrix", TCB == V([[4, 8, 10, 5], [2, 4, 4, 1], [3, 6, 5, 1], [2, 4, 4, 1]]))
exp(5, D_, 1, TCB[0, 0]); exp(5, D_, 2, TCB[0, 1]); exp(5, D_, 3, TCB[0, 3])
chk("Q5d choice: first coordinate of C=(x^3,1,x^2,x) is the x^3 coefficient (Perm row 1 picks row 4 of F-coordinates)", list(Perm[0, :]) == [0, 0, 0, 1])

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
        tol = st.get("tol", 0)
        ok = abs(float(EXP[key]) - st["answer"]) <= tol + 1e-12
        chk("Q%d%s step %d numeric answer %s == sympy %s" % (num, part, i, st["answer"], EXP[key]), ok)
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
