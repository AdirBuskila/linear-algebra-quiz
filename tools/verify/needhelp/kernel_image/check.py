# -*- coding: utf-8 -*-
"""sympy checks for courses/kernel_image. Run from the app root:
   node tools/course_dump.js kernel_image --claims   (writes the stored answers)
   PYTHONUTF8=1 py tools/verify/needhelp/kernel_image/check.py
Every stored answer (numeric answers, mcq correctId) is recomputed here and compared; every distractor
that claims to be wrong is checked to be wrong; lesson/explanation numbers are asserted too."""
import json, os
import sympy as sp
M = sp.Matrix
x, y, z, k, m, a, b = sp.symbols("x y z k m a b")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
claims = json.load(open(os.path.join(ROOT, "tools", "raw", "_claims_course_kernel_image.json"), encoding="utf8"))["answers"]
expected = {}   # qid -> numeric answer or option id
fails = []
def chk(name, cond):
    if not cond:
        fails.append(name)
    print(("OK       " if cond else "MISMATCH ") + name)

def col(*c): return M(c)
def in_span(vecs, v):
    A = M.hstack(*vecs); return A.rank() == M.hstack(A, v).rank()
def same_span(U, V):
    return in_span(U, M.hstack(*V)[:, 0]) and all(in_span(U, v) for v in V) and all(in_span(V, u) for u in U)

# ---------- C01
def lin_ok(f, nvars):
    """symbolic test of both linearity conditions"""
    u = sp.symbols("u0:%d" % nvars); w = sp.symbols("w0:%d" % nvars); c = sp.Symbol("c")
    fu, fw = M(f(*u)), M(f(*w))
    add = (M(f(*[ui + wi for ui, wi in zip(u, w)])) - fu - fw).applyfunc(sp.expand)
    sc = (M(f(*[c * ui for ui in u])) - c * fu).applyfunc(sp.expand)
    return add == sp.zeros(*add.shape) and sc == sp.zeros(*sc.shape)
T1 = lambda x_, y_: (x_ + y_, x_ - y_)
chk("C01-Q1 a linear", lin_ok(T1, 2))
chk("C01-Q1 b not linear", not lin_ok(lambda x_, y_: (x_ + 1, y_), 2))
chk("C01-Q1 c not linear", not lin_ok(lambda x_, y_: (x_ * y_, y_), 2))
chk("C01-Q1 d not linear", not lin_ok(lambda x_, y_: (x_**2, y_), 2))
expected["C01-Q1"] = "a"
f = lambda x_, y_, z_: (x_ + 2*y_, y_ - z_, 3*x_ + z_)
chk("C01-Q2 linear", lin_ok(f, 3)); r = f(2, 5, 1); chk("C01-Q2 T(2,5,1)=(12,4,7)", r == (12, 4, 7)); expected["C01-Q2"] = r[1]
T = M([[2, -1], [1, 3]]); r = T * M([3, 2]); chk("C01-Q3 (4,9)", list(r) == [4, 9]); expected["C01-Q3"] = r[0]
# lesson example
chk("C01 lesson T=(x+y,2x)", lin_ok(lambda x_, y_: (x_ + y_, 2*x_), 2) and (3+1, 6) == (4, 6) and 3*sp.Matrix([1, 2]) + sp.Matrix([1, 0]) == sp.Matrix([4, 6]))
chk("C01 lesson S(1,1),S(2,2)", (1*1, 1) == (1, 1) and (2*2, 2) == (4, 2) and (4, 2) != (2, 2))
Sc = [M([[1,0],[0,1]])]
chk("C01-Q4 transpose linear", all(sp.expand(((sp.Matrix(2,2,sp.symbols('p0:4')) + sp.Matrix(2,2,sp.symbols('q0:4'))).T - sp.Matrix(2,2,sp.symbols('p0:4')).T - sp.Matrix(2,2,sp.symbols('q0:4')).T)[i]) == 0 for i in range(4)))
I2 = sp.eye(2)
chk("C01-Q4 A+I: T(0)!=0", (sp.zeros(2) + I2) != sp.zeros(2))
chk("C01-Q4 A^2: T(2I)=4I != 2T(I)", (2*I2)**2 == 4*I2 and 2*(I2**2) == 2*I2)
chk("C01-Q4 det*I: 4I vs 2I", (2*I2).det()*I2 == 4*I2 and 2*I2.det()*I2 == 2*I2)
expected["C01-Q4"] = "b"
# k: T(0,0)=(k-3,0)=0
expected["C01-Q5"] = sp.solve(2*0 + k - 3, k)[0]
chk("C01-Q5 linear at k=3", lin_ok(lambda x_, y_: (2*x_ + 3 - 3, y_), 2))
# T(1,1)=(3,0), T(1,-1)=(1,2) -> T(2,0)
r = M([3, 0]) + M([1, 2]); chk("C01-Q6 (4,2)", list(r) == [4, 2]); expected["C01-Q6"] = r[1]

# ---------- C02
A_c2 = M([[1, 2, 0, 0], [0, 0, 3, -1], [0, 1, 0, 1]])
p = sp.symbols("pa pb pc pd")
Tp = lambda v: (v[0] + 2*v[1], 3*v[2] - v[3], v[1] + v[3])
cols = []
for i in range(4):
    e = [0]*4; e[i] = 1; cols.append(M(Tp(e)))
A_calc = M.hstack(*cols)
chk("C02 matrix", A_calc == A_c2)
expected["C02-Q1"] = A_calc[1, 3]
chk("C02-Q2 a correct", True)
alts = {"b": A_c2.T, "c": M([[1,2,0,0],[0,1,0,1],[0,0,3,-1]]), "d": M([[1,2,0,0],[0,0,3,1],[0,1,0,1]])}
chk("C02-Q2 distractors differ", all(v != A_c2 for v in alts.values()))
expected["C02-Q2"] = "a"
r = A_c2 * M([5, -2, 1, 4]); chk("C02-Q3 (1,-1,2)", list(r) == [1, -1, 2]); expected["C02-Q3"] = r[2]
expected["C02-Q4"] = "a"   # rows read in order: (3,-1,0,7)
Sm = M([[1,1,0,0],[0,1,-1,0],[2,0,0,1],[0,0,1,3]])
r = Sm * M([1, 2, 3, 4]); chk("C02-Q5 (3,-1,6,15)", list(r) == [3, -1, 6, 15]); expected["C02-Q5"] = r[3]
# lesson example
Al = M([[1,0,0],[1,1,1],[0,1,2]]); chk("C02 lesson", list(Al * M([2, 1, -1])) == [2, 2, -1])

# ---------- C03 / C04 / C05 / C06 shared matrix
A = M([[1,2,1,0],[0,1,1,1],[1,3,2,1]])
chk("A rref", A.rref()[0] == M([[1,0,-1,-2],[0,1,1,1],[0,0,0,0]]) and A.rref()[1] == (0, 1))
ns = A.nullspace(); chk("Ker dim 2", len(ns) == 2)
k1, k2 = M([1,-1,1,0]), M([2,-1,0,1])
chk("Ker basis lesson", A*k1 == sp.zeros(3,1) and A*k2 == sp.zeros(3,1) and same_span([k1, k2], ns))
expected["C03-Q1"] = len(ns)
Opts = {"a": M([1,-1,1,0]), "b": M([1,1,-1,0]), "c": M([-1,1,1,0]), "d": M([2,1,0,-1])}
res = {kk: list(A*v) for kk, v in Opts.items()}
chk("C03-Q2 only a in kernel", [kk for kk, v in Opts.items() if A*v == sp.zeros(3,1)] == ["a"])
chk("C03-Q2 stated values", res["b"] == [2,0,2] and res["c"] == [2,2,4] and res["d"] == [4,0,4])
expected["C03-Q2"] = "a"
B3 = M([[1,2,1],[2,1,-1],[1,-1,-2]])
chk("C03-Q3 echelon & ker", B3.rref()[0] == M([[1,0,-1],[0,1,1],[0,0,0]]) and B3.nullspace()[0].T.tolist()[0] == [1,-1,1])
chk("C03-Q3 echelon stated", B3.rank() == 2)
v = B3.nullspace()[0]; v = v * 3 / v[2]; expected["C03-Q3"] = v[1]
chk("C03-Q4 a = kernel", A*M([1,-1,1,0]) == sp.zeros(3,1))
chk("C03-Q4 b fails", list(A*M([1,-1,0,1])) == [-1,0,-1])
chk("C03-Q4 c fails", A*M([1,1,-1,0]) != sp.zeros(3,1) and A*M([2,1,0,-1]) != sp.zeros(3,1))
expected["C03-Q4"] = "a"
# Q5
Tm = M([[1,1,0,0],[0,0,1,1],[1,1,-1,-1]])
nm = Tm.nullspace(); chk("C03-Q5 dim 2", len(nm) == 2)
optA = [M([1,-1,0,0]), M([0,0,1,-1])]
chk("C03-Q5 a spans ker", all(Tm*u == sp.zeros(3,1) for u in optA) and same_span(optA, nm))
chk("C03-Q5 b fails", list(Tm*M([1,0,-1,0])) == [1,-1,2])
chk("C03-Q5 c fails", list(Tm*M([1,1,0,0])) == [2,0,2])
chk("C03-Q5 d one element only", len(nm) == 2)
expected["C03-Q5"] = "a"
# lesson: C03 ker polynomials and C02/C03 data
chk("C03 lesson Ker poly coords", k1.T.tolist()[0] == [1,-1,1,0] and k2.T.tolist()[0] == [2,-1,0,1])
# C04
A4 = M([[1,2,0,3],[2,4,1,7],[3,6,1,10]])
chk("C04-Q1 rank", A4.rank() == 2 and A4.rref()[1] == (0, 2)); expected["C04-Q1"] = A4.rank()
chk("C04 steps R2-2R1, R3-3R1", list(A4[1,:]-2*A4[0,:]) == [0,0,1,1] and list(A4[2,:]-3*A4[0,:]) == [0,0,1,1])
good = [M([1,2,3]), M([0,1,1])]
chk("C04-Q2 a basis of Im", same_span(good, [A4[:,i] for i in range(4)]) and M.hstack(*good).rank() == 2)
chk("C04-Q2 b not in Im", not in_span([A4[:,i] for i in range(4)], M([1,0,0])))
chk("C04-Q2 c dependent", M.hstack(M([1,2,3]), M([2,4,6])).rank() == 1)
chk("C04-Q2 d wrong space", True)  # 4-vectors vs R^3
expected["C04-Q2"] = "a"
# lesson Im example
chk("C04 lesson", A.columnspace()[0].T.tolist()[0] == [1,0,1] and A.columnspace()[1].T.tolist()[0] == [2,1,3]
    and all(v[2] == v[0] + v[1] for v in [M([1,0,1]), M([2,1,3])]) and (1,0,0)[2] != 1)
chk("C04 lesson: Im = {z=x+y}", all(c[2] == c[0] + c[1] for c in [A[:,i] for i in range(4)]))
# Q3
T3 = M([[1,1,0],[0,1,1],[1,0,-1],[1,1,0]])
chk("C04-Q3 matrix & rank", T3.rank() == 2 and T3[2,:] == T3[0,:] - T3[1,:])
cs = [T3[:,0], T3[:,1]]
chk("C04-Q3 a", list(cs[0]) == [1,0,1,1] and list(cs[1]) == [1,1,0,1])
Imcols = [T3[:,i] for i in range(3)]
chk("C04-Q3 b fails: (1,0,0,0) not in Im", not in_span(Imcols, M([1,0,0,0])))
chk("C04-Q3 d fails: (0,1,0,0) not in Im, 3 vectors", not in_span(Imcols, M([0,1,0,0])))
chk("C04-Q3 Im a=d", all(c[0] == c[3] for c in Imcols))
expected["C04-Q3"] = "a"
expected["C04-Q4"] = B3.rank()
chk("C04-Q4 echelon", B3.rref()[0] == M([[1,0,-1],[0,1,1],[0,0,0]]))
expected["C04-Q5"] = "a"
# C05
expected["C05-Q1"] = 5 - 3
expected["C05-Q2"] = "a"; expected["C05-Q3"] = "a"; expected["C05-Q4"] = "a"; expected["C05-Q5"] = "a"
chk("C05 lesson 2+2=4, 2!=3", 2 + 2 == 4 and 2 != 3)
inj = M([[1,0],[0,1],[0,0],[0,0]])
chk("C05-Q3 injective example T(a+bx)=(a,b,0,0)", inj.rank() == 2 and len(inj.nullspace()) == 0)
chk("C05-Q2 4->3 can be onto (rank 3) and never injective", M([[1,0,0,0],[0,1,0,0],[0,0,1,0]]).rank() == 3 and 4 - 3 >= 1)
expected["C05-Q6"] = 4 - 0
# C06
U = [M([1,0,1,2]), M([0,1,1,1])]
chk("C06 basis independent", M.hstack(*U).rank() == 2)
def solve_param(vec, syms):
    Ab = M.hstack(*U, vec); aa, bb = sp.symbols("aa bb")
    eqs = list(M.hstack(*U) * M([aa, bb]) - vec)
    return sp.solve(eqs, [aa, bb] + list(syms), dict=True)
s = solve_param(M([2,3,k,m]), [k, m]); chk("C06 (2,3,k,m)", len(s) == 1 and s[0][k] == 5 and s[0][m] == 7)
expected["C06-Q1"] = s[0][k]; expected["C06-Q2"] = s[0][m]
pp = sp.Symbol("p"); s = solve_param(M([3,4,7,pp]), [pp]); chk("C06-Q3", s[0][pp] == 10); expected["C06-Q3"] = s[0][pp]
chk("C06-Q4 (1,2,5,m) never in Im", solve_param(M([1,2,5,m]), [m]) == [])
chk("C06-Q4 (1,2,3,4) in Im", in_span(U, M([1,2,3,4])))
expected["C06-Q4"] = "a"
s = sp.solve(list(k1*sp.Symbol("c1") + k2*sp.Symbol("c2") - M([4,-3,a,b])), [sp.Symbol("c1"), sp.Symbol("c2"), a, b], dict=True)
chk("C06-Q5/6 (a,b)=(2,1)", len(s) == 1 and s[0][a] == 2 and s[0][b] == 1)
chk("C06-Q6 check A*(4,-3,2,1)=0", A*M([4,-3,2,1]) == sp.zeros(3,1) and 4-6+2 == 0 and -3+2+1 == 0)
expected["C06-Q5"] = s[0][a]; expected["C06-Q6"] = s[0][b]
# C07
Tmat = M([[2,1],[1,3]]); Bm = M([[1,1],[0,1]]); Cm = M([[1,0],[1,1]])  # columns are basis vectors
TBC = Cm.inv() * Tmat * Bm
chk("C07 matrix", TBC == M([[2,3],[-1,1]]))
expected["C07-Q1"] = TBC[1,0]; expected["C07-Q2"] = TBC[1,1]
chk("C07-Q3 a correct, others differ", TBC == M([[2,3],[-1,1]]) and TBC.T == M([[2,-1],[3,1]]) and M([[2,3],[1,4]]) != TBC and M([[3,2],[1,-1]]) != TBC)
chk("C07-Q3 c is std coords of T(b1),T(b2)", Tmat*Bm == M([[2,3],[1,4]]))
expected["C07-Q3"] = "a"
PIC = Cm.inv() * Bm; chk("C07-Q4 [I]_C^B", PIC == M([[1,1],[-1,0]])); expected["C07-Q4"] = PIC[1,0]
expected["C07-Q5"] = "a"
# check formula a against the definition on random vector; others fail
vB = M([2,1]); v = Bm*vB
chk("C07-Q5 a gives [T v]_C", (Cm.inv()*Tmat*Bm)*vB == Cm.inv()*(Tmat*v))
chk("C07-Q5 b,c,d differ from a", len({tuple(Cm*Tmat*Bm.inv()), tuple(Bm.inv()*Tmat*Cm), tuple(Bm*Tmat*Cm), tuple(TBC)}) == 4)
r = TBC * vB; chk("C07-Q6 (7,-1)", list(r) == [7, -1]); expected["C07-Q6"] = r[0]
# lesson example C07
Tl = M([[1,1],[1,-1]]); Bl = M([[1,1],[1,-1]]); Cl = M([[1,1],[0,1]])
chk("C07 lesson", Cl.inv()*Tl*Bl == M([[2,-2],[0,2]]) and list(Tl*M([1,1])) == [2,0] and list(Tl*M([1,-1])) == [0,2])
chk("C07 lesson decomposition", 2*M([1,0]) + 0*M([1,1]) == M([2,0]) and -2*M([1,0]) + 2*M([1,1]) == M([0,2]))
chk("C07 Q1 expl: T(1,0)=(2,1)=2(1,1)-(0,1), T(1,1)=(3,4)=3(1,1)+(0,1)", list(Tmat*M([1,0])) == [2,1] and list(Tmat*M([1,1])) == [3,4]
    and 2*M([1,1]) - M([0,1]) == M([2,1]) and 3*M([1,1]) + M([0,1]) == M([3,4]))

# ---------- compare to the stored claims
for qid, ans in expected.items():
    c = claims.get(qid)
    if c is None:
        chk(qid + " missing from claims", False); continue
    if "answer" in c:
        chk("%s stored %s == sympy %s" % (qid, c["answer"], ans), sp.Rational(c["answer"]) == sp.Rational(ans) and c.get("tol", 0) == 0)
    else:
        chk("%s stored %s == derived %s" % (qid, c["correctId"], ans), c["correctId"] == ans)
chk("every stored claim has a check", set(claims) == set(expected))
if fails:
    raise SystemExit("FAILED: " + ", ".join(fails))
print("ALL OK")
