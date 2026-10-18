# -*- coding: utf-8 -*-
"""sympy checks of the step-author values for 22B-B (rubric/pitfalls/steps in tools/gen/gen_22B-B.py).
Run: PYTHONUTF8=1 py tools/verify/22B-B/verify_steps_22B-B.py
Every numeric step in tools/raw/22B-B.json must have an expected value computed here with sympy (coverage is asserted),
and the facts behind every choice distractor / findbug line are checked. Prints OK/MISMATCH lines (ASCII only)."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "22B-B.json").read_text(encoding="utf-8"))
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
    EXP[(num, part, idx)] = float(val) if isinstance(val, float) else sp.nsimplify(val)


x, a, b, c, d, l, k = sp.symbols("x a b c d l k")

# ---- Q1a  a+b = c+d => eigenvalues a+b, a-c
A2 = V([[a, b], [c, d]])
cp = A2.charpoly(l).as_expr()
sub = {d: a + b - c}
roots = sp.solve(cp.subs(sub), l)
chk("Q1a eigenvalues are a+b and a-c under a+b=c+d", set(sp.simplify(r) for r in roots) == {sp.simplify(a + b), sp.simplify(a - c)})
disc = sp.expand(((a - d) ** 2 + 4 * b * c).subs(sub))
chk("Q1a discriminant = (b+c)^2, not (b-c)^2", sp.expand(disc - (b + c) ** 2) == 0 and sp.expand(disc - (b - c) ** 2) != 0)
vals = {a: 3, b: 1, c: 2, d: 2}
exp(1, A_, 1, ((a - d) ** 2 + 4 * b * c).subs(vals))
exp(1, A_, 4, (a - c).subs(vals))
chk("Q1a numeric example eigenvalues {4,1}", sorted(A2.subs(vals).eigenvals()) == [1, 4])

# ---- Q1b
Bm = V([[2, 1], [1, 2]]); u = V([1, 1])
chk("Q1b Bu = 3u", Bm * u == 3 * u)
exp(1, B_, 3, float((Bm.inv() * u)[0]) if False else (Bm.inv() * u)[0])
chk("Q1b B^-1 u = u/3", Bm.inv() * u == u / 3)
chk("Q1b invertible matrix has no eigenvalue 0; an invertible matrix with a negative eigenvalue exists",
    all(v != 0 for v in Bm.eigenvals()) and any(v < 0 for v in V([[-1, 0], [0, 2]]).eigenvals()))

# ---- Q1c
exp(1, C_, 3, ((Bm - 1 * sp.eye(2)) * u)[0])
chk("Q1c (C-sI)u = (3-1)u", (Bm - sp.eye(2)) * u == 2 * u and (Bm - sp.eye(2)) * u != 3 * u)

# ---- Q1d
Dm = sp.diag(1, 2); Pm = V([[1, 1], [0, 1]])
Em = Pm * Dm * Pm.inv()
chk("Q1d PD = EP", Pm * Dm == Em * Pm)
exp(1, D_, 3, Em.trace())
chk("Q1d bug line: DP != PD so EP u = DP u fails", Dm * Pm != Pm * Dm)
chk("Q1d eigenvalues of D,E agree; eigenvector of E is Pu, not u", sorted(Em.eigenvals()) == sorted(Dm.eigenvals()) and Em * V([1, 0]) == V([1, 0]) and Em * (Pm * V([1, 0])) == Pm * V([1, 0]))

# ---- Q2
kk = k
M = V([[k, k**2, k], [1, k, -k], [1, 1, 1]]); rhs = V([1, 1, 1])
sol = sp.solve(list(M * V(sp.symbols("X Y Z")) - rhs), sp.symbols("X Y Z"), dict=True)[0]
X, Y, Z = sp.symbols("X Y Z")
chk("Q2a solution formulas", sp.simplify(sol[X] - (k + 3) / (k + 1)) == 0 and sp.simplify(sol[Y] + 1 / k) == 0 and sp.simplify(sol[Z] - (1 - k) / (k * (k + 1))) == 0)
exp(2, A_, 1, float(sol[X].subs(k, 2))); exp(2, A_, 2, float(sol[Y].subs(k, 2))); exp(2, A_, 3, float(sol[Z].subs(k, 2)))
rk = lambda kv: (M.subs(k, kv).rank(), M.subs(k, kv).row_join(rhs).rank())
chk("Q2a k=0 none, k=-1 none, k=1 infinite, k=2 unique", rk(0)[0] < rk(0)[1] and rk(-1)[0] < rk(-1)[1] and rk(1) == (2, 2) and rk(2) == (3, 3))
chk("Q2a choice distractors: k=1 and k=0 and k=-1 not unique", all(rk(v) != (3, 3) for v in (0, 1, -1)))
exp(2, B_, 0, rk(-1)[0]); exp(2, B_, 1, rk(-1)[1])
Mm1 = M.subs(k, -1)
exp(2, B_, 2, (rhs[0] + rhs[1]))
chk("Q2b k=-1: row1+row2 coefficients zero", (Mm1[0, :] + Mm1[1, :]) == sp.zeros(1, 3))
chk("Q2b choice: k=1 infinite (rank 2 = 2 < 3)", rk(1) == (2, 2))
chk("Q2b k=0 first row 0=1", M.subs(k, 0)[0, :] == sp.zeros(1, 3) and rhs[0] == 1)
M1 = M.subs(k, 1)
chk("Q2c k=1 reduces to z=0, x+y=1", M1.row_join(rhs).rref()[0][:2, :] == V([[1, 1, 0, 1], [0, 0, 1, 0]]))
exp(2, C_, 0, 0); exp(2, C_, 1, 1); exp(2, C_, 3, 3 - M1.rank())
chk("Q2c correct general solution", all(M1 * (V([1, 0, 0]) + t * V([-1, 1, 0])) == rhs for t in (0, 1, 5)))
chk("Q2c distractor (1,0,0)+y(1,1,0): homogeneous direction fails", M1 * V([1, 1, 0]) != sp.zeros(3, 1))
chk("Q2c distractor (1,0,1)+y(-1,1,0): not a solution", M1 * V([1, 0, 1]) != rhs)
chk("Q2c distractor origin+y(-1,1,0): origin not a solution", M1 * V([0, 0, 0]) != rhs)
zz = sp.symbols("zz")
ud = V([zz, -1, 2]); vd = V([zz, zz, 1])
dp = sp.expand(ud.dot(vd))
chk("Q2d u.v = z^2 - z + 2", dp == zz**2 - zz + 2)
exp(2, D_, 0, dp.subs(zz, 0))
exp(2, D_, 1, sp.discriminant(dp, zz))
rts = sp.solve(dp, zz)
exp(2, D_, 2, sp.re(rts[0])); exp(2, D_, 3, round(float(max(sp.im(r) for r in rts)), 3))
chk("Q2d roots 1/2 +- i sqrt7/2", set(rts) == {R(1, 2) + sp.I * sp.sqrt(7) / 2, R(1, 2) - sp.I * sp.sqrt(7) / 2})

# ---- Q3
A3 = V([[1, 4, 0], [0, 1, 2], [3, 12, 3]])
Ai = A3.inv()
exp(3, A_, 0, A3.det())
E1 = sp.eye(3); E1[2, :] = E1[2, :] - 3 * E1[0, :]
exp(3, A_, 1, (E1 * A3)[2, 2])
exp(3, A_, 2, Ai[0, 0]); exp(3, A_, 3, round(float(Ai[0, 2]), 3))
chk("Q3a A^-1 official", Ai == V([[-7, -4, R(8, 3)], [2, 1, R(-2, 3)], [-1, 0, R(1, 3)]]))
Ea = [V([[1, -4, 0], [0, 1, 0], [0, 0, 1]]), V([[1, 0, 0], [0, 1, -2], [0, 0, 1]]), V([[1, 0, 0], [0, 1, 0], [0, 0, R(1, 3)]]), V([[1, 0, 0], [0, 1, 0], [-3, 0, 1]])]
prod = Ea[0] * Ea[1] * Ea[2] * Ea[3]
chk("Q3b product = A^-1", prod == Ai)
chk("Q3b choice: reversed product differs", Ea[3] * Ea[2] * Ea[1] * Ea[0] != Ai)
exp(3, B_, 1, round(float(prod.det()), 3)); exp(3, B_, 2, prod[0, 0])
B3 = V([[5, 0, 1], [0, 4, 0], [1, 0, 5]])
exp(3, C_, 0, (0 * sp.eye(3) - B3).det())
exp(3, C_, 1, 3 - (4 * sp.eye(3) - B3).rank())
P3 = V([[-1, 0, 1], [0, 1, 0], [1, 0, 1]])
chk("Q3c BP = P diag(4,4,6)", B3 * P3 == P3 * sp.diag(4, 4, 6) and P3.det() != 0)
exp(3, C_, 3, (B3 * P3)[0, 2])
chk("Q3c eigenvalues 4,4,6 (not 3 distinct); det != 0; a nondiagonalizable matrix with real eigenvalues and det != 0 exists",
    sorted(B3.eigenvals(multiple=True)) == [4, 4, 6] and B3.det() != 0 and not V([[1, 1], [0, 1]]).is_diagonalizable())

# ---- Q4 (polynomials as coefficient lists)
p = a * x**3 + b * x**2 + c * x + d
cW1 = sp.Poly(sp.expand(p.subs(x, -1) - p.subs(x, 1)), a, b, c, d).as_expr()
chk("Q4a W1 constraint is a1+a3=0 (c + a = 0)", sp.expand(cW1 + 2 * (a + c)) == 0)
chk("Q4a x^3-x in W1; x^3, x, x^3+x not", all((q.subs(x, -1) == q.subs(x, 1)) == (q == x**3 - x) for q in (x**3 - x, x**3, x, x**3 + x)))
W1b = [sp.Integer(1), x**2, x**3 - x]
W2b = [-x**3 + 8, -x**3 + 4 * x, -x**3 + 2 * x**2]
cvec = lambda q: [sp.Poly(q, x).coeff_monomial(x**i) for i in range(4)]
Wm = V([cvec(q) for q in W1b + W2b]).T
exp(4, A_, 1, V([cvec(q) for q in W1b]).rank()); exp(4, A_, 2, V([cvec(q) for q in W2b]).rank())
chk("Q4a W1,W2 bases satisfy constraints", all(q.subs(x, -1) == q.subs(x, 1) for q in W1b) and all(q.subs(x, 2) == 0 for q in W2b))
a3 = sp.solve(8 * a + 4 * 0 + 2 * 0 + 8, a)[0]
exp(4, A_, 3, a3)
exp(4, B_, 0, V([cvec(q) for q in W1b]).rank() + V([cvec(q) for q in W2b]).rank())
rr, piv = Wm.rref()
exp(4, B_, 1, 6 - len(piv))
chk("Q4b pivots are the first four columns", piv == (0, 1, 2, 3), str(piv))
exp(4, B_, 2, Wm.rank())
inter = [-x**3 + x + 6, x**2 - 4]
chk("Q4c inter basis in W1 and W2", all(q.subs(x, -1) == q.subs(x, 1) and q.subs(x, 2) == 0 for q in inter))
chk("Q4c choice: x^2-4 in both; x^2-1, x^3-x, x^2+4 fail p(2)=0", (x**2 - 4).subs(x, 2) == 0 and all(q.subs(x, 2) != 0 for q in (x**2 - 1, x**3 - x, x**2 + 4)))
exp(4, C_, 1, V([cvec(q) for q in W1b]).rank() + V([cvec(q) for q in W2b]).rank() - Wm.rank())
exp(4, C_, 2, inter[0].subs(x, 2))
pp = -x**3 + 2 * x**2 + x - 2
chk("Q4d p = (-x^3+x+6) + 2(x^2-4)", sp.expand(pp - inter[0] - 2 * inter[1]) == 0)
chk("Q4d p in W1 and W2", pp.subs(x, -1) == pp.subs(x, 1) and pp.subs(x, 2) == 0)
exp(4, D_, 1, sp.Poly(sp.expand(pp - inter[0]), x).coeff_monomial(x**2))
exp(4, D_, 2, pp.subs(x, 2))

# ---- Q5
kT = sp.symbols("kT")
A5 = V([[1, 1, 1], [0, 1, 2], [0, 2, kT**2 + 3], [0, -1, -2]])
bvec = V([1, 1, 2, kT])
Aug5 = A5.row_join(bvec)
s5 = Aug5.copy(); s5[2, :] = s5[2, :] - 2 * s5[1, :]; s5[3, :] = s5[3, :] + s5[1, :]
exp(5, A_, 0, s5[2, 2].subs(kT, 2)); exp(5, A_, 1, s5[3, 3].subs(kT, 5))
chk("Q5a rows: (0 0 k^2-1 | 0), (0 0 0 | k+1)", sp.expand(s5[2, 2] - (kT**2 - 1)) == 0 and sp.expand(s5[3, 3] - (kT + 1)) == 0 and s5[3, 2] == 0)
inIm = lambda kv: A5.subs(kT, kv).rank() == A5.subs(kT, kv).row_join(bvec.subs(kT, kv)).rank()
chk("Q5a Im membership only for k=-1 (distractors 1, 0 fail)", inIm(-1) and not inIm(1) and not inIm(0) and not inIm(2))
rkT = lambda kv: A5.subs(kT, kv).rank()
chk("Q5b injective iff k != +-1", rkT(2) == 3 and rkT(0) == 3 and rkT(1) == 2 and rkT(-1) == 2)
exp(5, B_, 1, rkT(2)); exp(5, B_, 2, rkT(1)); exp(5, B_, 3, rkT(-1))
chk("Q5b never onto (rank <= 3 < 4)", all(rkT(v) <= 3 for v in (-1, 0, 1, 2, 5)))
K1 = A5.subs(kT, 1)
ker = K1.nullspace()
exp(5, C_, 0, len(ker))
kv = ker[0] / ker[0][2]
exp(5, C_, 1, kv[1])
chk("Q5c kernel vector (1,-2,1)", list(kv) == [1, -2, 1])
exp(5, C_, 2, (K1 * kv)[3])
chk("Q5c T(1-2x+x^2)=0", K1 * kv == sp.zeros(4, 1))
EB = V([[1, 3], [1, 4]])
exp(5, D_, 0, EB.det())
exp(5, D_, 1, EB.inv()[0, 0])
FEB = V([[2, 5], [2, 0]])
F = FEB * EB.inv()
chk("Q5d F(1,1)=(2,2), F(3,4)=(5,0), F = [[3,-1],[8,-6]]", F * V([1, 1]) == V([2, 2]) and F * V([3, 4]) == V([5, 0]) and F == V([[3, -1], [8, -6]]))
exp(5, D_, 2, F[0, 1]); exp(5, D_, 3, F[1, 0])
chk("Q5d wrong order [I][F] differs", EB * FEB != F)

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
# --- fix pass: bilinear vs Hermitian product for Q2d
_z = sp.Symbol("z"); _x, _y = sp.symbols("x y", real=True)
_zz = _x + sp.I * _y
chk("Q2d bilinear roots (1+-i sqrt7)/2", sorted(sp.solve(_z ** 2 - _z + 2, _z), key=lambda r: sp.im(r)) == [sp.Rational(1, 2) - sp.I * sp.sqrt(7) / 2, sp.Rational(1, 2) + sp.I * sp.sqrt(7) / 2])
_h = sp.expand(_zz * sp.conjugate(_zz) - sp.conjugate(_zz) + 2)
chk("Q2d Hermitian product has no solution", sp.solve([sp.re(_h), sp.im(_h)], [_x, _y], dict=True) == [])
extra = set(EXP) - {(num, part, i) for (num, part), qq in QS.items() for i, st in enumerate(qq.get("steps", [])) if st["type"] == "numeric"}
chk("no orphan expected values", not extra, str(sorted(extra)))
print("")
print("numeric steps checked:", n)
print("TOTAL MISMATCHES:", len(bad))
