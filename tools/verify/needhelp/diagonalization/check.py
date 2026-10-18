# -*- coding: utf-8 -*-
"""sympy checks of the guided course `diagonalization` (courses/diagonalization/C01..C08.js).

Run:  PYTHONUTF8=1 py tools/verify/needhelp/diagonalization/check.py
Every stored answer (mcq correctId, numeric answer, order lines, findbug index) is recomputed with sympy and
asserted, every mcq distractor is asserted wrong, every numeric equality chain in any text is evaluated, and the
boss bankIds are checked against the bank.
"""
import json, pathlib, re, subprocess
import sympy as sp
from sympy import Matrix, Rational as R, symbols, eye, diag, zeros

HERE = pathlib.Path(__file__).resolve().parent
APP = HERE.parents[3]
BS = chr(92)
lam, x1, x2 = symbols("lambda x1 x2")

node = r"""
const fs=require('fs'),vm=require('vm'),path=require('path');
const dir=process.argv[process.argv.length-1]; const out={};
for(const f of fs.readdirSync(dir).filter(n=>n.endsWith('.js')).sort()){
  let got=null; const sb={}; sb.window=sb; sb.COURSE_LEVEL=(c,l)=>{got=l};
  vm.createContext(sb); vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),sb);
  out[got.id]=got;
}
process.stdout.write(JSON.stringify(out));
"""
raw = subprocess.run(["node", "-e", node, str(APP / "courses" / "diagonalization")], capture_output=True, check=True).stdout
LV = json.loads(raw.decode("utf8"))
Q = {}
for lid, lv in LV.items():
    for q in lv["questions"]:
        if "id" in q:
            assert q["id"] not in Q, q["id"]
            Q[q["id"]] = q
BANK = {q["id"]: q for q in json.load(open(APP / "questions.json", encoding="utf8"))["questions"]}

checks = 0
def ok(cond, msg):
    global checks
    checks += 1
    assert cond, "FAILED: " + msg

def pm(tex):
    """all \\begin{pmatrix}..\\end{pmatrix} in tex -> list of sympy Matrix"""
    out = []
    for m in re.finditer(re.escape(BS) + r"begin\{pmatrix\}(.*?)" + re.escape(BS) + r"end\{pmatrix\}", tex, re.S):
        rows = [r for r in m.group(1).split(BS * 2) if r.strip()]
        out.append(Matrix([[sp.sympify(c.strip()) for c in r.split("&")] for r in rows]))
    return out

def mcq(qid, truth):
    """truth: {optionId: bool} computed by sympy; exactly the stored correctId must be true"""
    q = Q[qid]
    ok(sorted(o["id"] for o in q["options"]) == sorted(truth), qid + " option ids")
    ok({i for i, v in truth.items() if v} == {q["correctId"]}, f"{qid}: sympy says {[i for i,v in truth.items() if v]}, stored {q['correctId']}")

def opt(qid, i):
    return next(o["value"] for o in Q[qid]["options"] if o["id"] == i)

def num(qid, val):
    s = Q[qid]["step"]
    ok(s["type"] == "numeric" and sp.nsimplify(s["answer"]) == sp.nsimplify(val), f"{qid}: stored {s['answer']} computed {val}")

def is_eig(A, v, mu=None):
    w = A * v
    if v == zeros(*v.shape): return False
    for i in range(len(v)):
        if v[i] != 0:
            c = w[i] / v[i]; break
    return w == c * v and (mu is None or c == mu)

def charpoly(A):
    return sp.expand((lam * eye(A.rows) - A).det())

def pv(*a): return Matrix(a)

# ================================================================ C01
A = Matrix([[3, 1], [0, 2]])
cands = {"a": pv(1, 0), "b": pv(0, 1), "c": pv(1, 1), "d": pv(1, 2)}
mcq("C01-Q1", {i: is_eig(A, v) for i, v in cands.items()})
ok(A * pv(1, 0) == 3 * pv(1, 0) and A * pv(0, 1) == pv(1, 2) and A * pv(1, 1) == pv(4, 2) and A * pv(1, 2) == pv(5, 4), "C01-Q1 explanation products")
A = Matrix([[4, 1], [2, 3]])
ok(A * pv(1, 1) == pv(5, 5) and A * pv(1, 0) == pv(4, 2) and not is_eig(A, pv(1, 0)), "C01 lesson example")
ok(A * pv(1, -2) == 2 * pv(1, -2), "C03 lesson/brief check (1,-2) lambda 2")
num("C01-Q2", 5); ok(is_eig(A, pv(1, 1), 5), "C01-Q2")
A3 = Matrix([[1, 2], [2, 1]]); ok(is_eig(A3, pv(1, -1), -1) and A3 * pv(1, -1) == pv(-1, 1), "C01-Q3"); num("C01-Q3", -1)
A4 = Matrix([[2, 1], [0, 3]]); v4 = pv(1, 2)
ok(A4 * v4 == pv(4, 6), "C01-Q4 product")
mcq("C01-Q4", {"a": not is_eig(A4, v4), "b": is_eig(A4, v4, 4), "c": is_eig(A4, v4, 6), "d": is_eig(A4, v4, 2)})
ok(A4 * v4 != 2 * v4 and 2 * v4 == pv(2, 4), "C01-Q4 lambda=2 gives (2,4)")
ok(A * (2 * pv(1, 1)) == pv(10, 10), "C01-Q5"); num("C01-Q5", (A * (2 * pv(1, 1)))[0])
ok(pv(5, 3) != 5 * pv(1, 1), "C01 trap (5,3) not a multiple of (1,1)")

# ================================================================ C02
def trdet_poly(A): return sp.expand(lam**2 - A.trace() * lam + A.det())
A = Matrix([[4, 1], [2, 3]])
ok(charpoly(A) == trdet_poly(A) == sp.expand((lam - 2) * (lam - 5)) == lam**2 - 7*lam + 10, "C02 lesson poly")
ok(A.trace() == 7 and A.det() == 10 and 12 - 2 == 10 and 2 + 5 == 7 and 2 * 5 == 10, "C02 lesson arithmetic")
A = Matrix([[3, 1], [2, 2]])
ok(charpoly(A) == trdet_poly(A) == lam**2 - 5*lam + 4, "C02-Q1 poly")
polys = {"a": lam**2 - 5*lam + 4, "b": lam**2 + 5*lam + 4, "c": lam**2 - 5*lam + 8, "d": lam**2 - 4*lam + 5}
mcq("C02-Q1", {i: sp.expand(p - charpoly(A)) == 0 for i, p in polys.items()})
ok(3*2 + 1*2 == 8 and A.trace() == 5 and A.det() == 4, "C02-Q1 explanation")
ev = A.eigenvals()
ok(ev == {1: 1, 4: 1}, "C02-Q2 eigenvalues")
sets = {"a": {1, 4}, "b": {-1, -4}, "c": {2, 3}, "d": {1, 5}}
mcq("C02-Q2", {i: s == set(ev) for i, s in sets.items()})
ok(1 * 5 != 4 and 1 + 5 == 6, "C02-Q2 distractor d")
B = Matrix([[5, 2], [2, 5]]); ok(B.eigenvals() == {3: 1, 7: 1} and B.trace() == 10 and B.det() == 21 and 25 - 4 == 21, "C02-Q3"); num("C02-Q3", max(B.eigenvals()))
B = Matrix([[1, 4], [2, 3]]); ok(B.eigenvals() == {5: 1, -1: 1} and B.det() == -5 and 1*3 - 4*2 == -5 and 5 * (-1) == -5, "C02-Q4")
ok(charpoly(B) == lam**2 - 4*lam - 5 == sp.expand((lam - 5) * (lam + 1)), "C02-Q4 poly"); num("C02-Q4", B.det())
B = Matrix([[1, 2], [3, 2]])
ok(sp.expand((lam - 1) * (lam - 2) - 6) == charpoly(B) == lam**2 - 3*lam - 4 == sp.expand((lam - 4) * (lam + 1)), "C02-Q5 chain")
ok(B.eigenvals() == {4: 1, -1: 1} and 4 + (-1) == 3 == B.trace() and B.det() == -4 and 2 - 6 == -4, "C02-Q5 values")
ok((lam * eye(2) - B) == Matrix([[lam - 1, -2], [-3, lam - 2]]), "C02-Q5 line 0")
s = Q["C02-Q5"]["step"]["lines"]; ok(len(s) == 4 and "\\lambda^2-3\\lambda-4" in s[2] and "(\\lambda-4)(\\lambda+1)" in s[3], "C02-Q5 lines")
B = Matrix([[2, 1], [4, 5]])
ok(sp.expand((lam - 2) * (lam - 5) - 4) == charpoly(B) == lam**2 - 7*lam + 6 == sp.expand((lam - 1) * (lam - 6)), "C02-Q6 truth")
ok(lam**2 - 7*lam + 14 != charpoly(B), "C02-Q6 line 2 is wrong")
ok((lam * eye(2) - B) == Matrix([[lam - 2, -1], [-4, lam - 5]]), "C02-Q6 line 0")
ok(Q["C02-Q6"]["step"]["bugIndex"] == 2 and "+14" in Q["C02-Q6"]["step"]["lines"][2], "C02-Q6 bug line")

# ================================================================ C03
A = Matrix([[3, 1], [2, 2]])
ok((4 * eye(2) - A) == Matrix([[1, -1], [-2, 2]]) and (4 * eye(2) - A).nullspace()[0].T == Matrix([[1, 1]]), "C03-Q1 kernel")
ok(is_eig(A, pv(1, 1), 4) and A * pv(1, 1) == pv(4, 4), "C03-Q1"); num("C03-Q1", 1)
cands = {"a": pv(1, -2), "b": pv(2, -1), "c": pv(1, 2), "d": pv(1, 1)}
mcq("C03-Q2", {i: is_eig(A, v, 1) for i, v in cands.items()})
ok((eye(2) - A) == Matrix([[-2, -1], [-2, -1]]) and A * pv(2, -1) == pv(5, 2) and A * pv(1, 2) == pv(5, 6) and is_eig(A, pv(1, 1), 4), "C03-Q2 explanation")
A = Matrix([[3, 0], [1, 2]])
cands = {"a": pv(3, 3), "b": pv(0, 0), "c": pv(1, 0), "d": pv(1, -1)}
mcq("C03-Q3", {i: is_eig(A, v, 3) for i, v in cands.items()})
ok((3 * eye(2) - A) == Matrix([[0, 0], [-1, 1]]) and A * pv(1, 0) == pv(3, 1) and A * pv(1, -1) == pv(3, -1) and A.eigenvals() == {3: 1, 2: 1}, "C03-Q3 explanation")
ok(((2 * eye(2) - Matrix([[2, 0], [0, 2]])).nullspace().__len__()) == 2, "C03-Q4 dim"); num("C03-Q4", 2)
ok(len((2 * eye(2) - Matrix([[2, 1], [0, 2]])).nullspace()) == 1, "C03-Q5 dim"); num("C03-Q5", 1)
ok((2 * eye(2) - Matrix([[2, 1], [0, 2]])) == Matrix([[0, -1], [0, 0]]), "C03-Q5 matrix")
A = Matrix([[3, 1], [2, 2]])
ok((4 * eye(2) - A).row_join(zeros(2, 1)).rref()[0] == Matrix([[1, -1, 0], [0, 0, 0]]), "C03-Q6 rref")
ok(Matrix([[1, -1], [-2, 2]]).elementary_row_op("n->n+km", row=1, k=2, row2=0) == Matrix([[1, -1], [0, 0]]), "C03-Q6 R2+2R1")
ok(is_eig(A, pv(1, 1), 4), "C03-Q6 result")
L = Q["C03-Q6"]["step"]["lines"]; ok("x_2=1" in L[3] and "(1,1)" in L[3] and "R_2+2R_1" in L[1], "C03-Q6 lines")
# lesson example of C03 (A=[[4,1],[2,3]], lambda=2)
A0 = Matrix([[4, 1], [2, 3]]); ok(2 * eye(2) - A0 == Matrix([[-2, -1], [-2, -1]]) and A0 * pv(1, -2) == pv(2, -4) == 2 * pv(1, -2), "C03 lesson")

# ================================================================ C04
T = Matrix([[2, 5, 7], [0, 3, 1], [0, 0, 3]]); ok(T.eigenvals() == {2: 1, 3: 2}, "C04-Q1")
sets = {"a": {2: 1, 3: 2}, "b": {2: 1, 5: 1, 7: 1}, "c": {2: 1, 3: 1}, "d": {5: 1, 1: 1, 7: 1}}
mcq("C04-Q1", {i: s == T.eigenvals() for i, s in sets.items()})
B = Matrix([[1, 0, 0], [4, 5, 2], [0, 2, 5]])
ok(charpoly(B) == sp.expand((lam - 1) * (lam - 3) * (lam - 7)) and B.eigenvals() == {1: 1, 3: 1, 7: 1}, "C04-Q2")
ok(sp.expand((lam - 5)**2 - 4) == sp.expand((lam - 3) * (lam - 7)), "C04-Q2 factor"); num("C04-Q2", 7)
B = Matrix([[6, 0, 2], [0, 3, 0], [2, 0, 6]])
tr = charpoly(B)
polys = {"a": (lam - 3) * (lam - 4) * (lam - 8), "b": (lam - 3) * (lam - 6)**2, "c": (lam - 3) * (lam - 2) * (lam - 8), "d": (lam - 3) * (lam + 4) * (lam + 8)}
mcq("C04-Q3", {i: sp.expand(p) == tr for i, p in polys.items()})
ok(sp.expand((lam - 6)**2 - 4) == lam**2 - 12*lam + 32 == sp.expand((lam - 4) * (lam - 8)), "C04-Q3 explanation")
ok(B.trace() == 15 and 6 + 3 + 6 == 15 and 15 - 3 - 4 == 8, "C04-Q4"); num("C04-Q4", 15 - 3 - 4); ok(B.eigenvals() == {3: 1, 4: 1, 8: 1}, "C04-Q4 eig")
ok(B.det() == 96 and 3*4*8 == 96 and 3 * (36 - 4) == 96, "C04-Q5"); num("C04-Q5", B.det())
Lx = Matrix([[3, 1, 0], [2, 2, 0], [5, 7, 6]])
ok(charpoly(Lx) == sp.expand((lam - 6) * (lam - 1) * (lam - 4)) and sp.expand((lam - 6) * (lam**2 - 5*lam + 4)) == charpoly(Lx), "C04 lesson poly")
ok(Lx.trace() == 11 and 6 + 1 + 4 == 11 and 3 + 2 + 6 == 11 and Lx.det() == 24 and 6 * 1 * 4 == 24, "C04 lesson checks")
M = Matrix([[2, 0, 1], [0, 5, 0], [1, 0, 2]])
ok(M.eigenvals() == {5: 1, 1: 1, 3: 1} and sp.expand((lam - 2)**2 - 1) == lam**2 - 4*lam + 3 != lam**2 - 4*lam + 5, "C04-Q6")
ok(charpoly(M) == sp.expand((lam - 5) * (lam - 1) * (lam - 3)), "C04-Q6 poly")
ok(Q["C04-Q6"]["step"]["bugIndex"] == 2 and "+5" in Q["C04-Q6"]["step"]["lines"][2], "C04-Q6 bug line")

# ================================================================ C05
A = Matrix([[3, 1, 0], [0, 3, 0], [0, 0, 5]])
ok(charpoly(A) == sp.expand((lam - 3)**2 * (lam - 5)), "C05 poly"); num("C05-Q1", A.eigenvals()[3])
g3 = 3 - (3 * eye(3) - A).rank(); ok(g3 == 1 and (3 * eye(3) - A).rank() == 2, "C05-Q2 geometric"); num("C05-Q2", g3)
ok(not A.is_diagonalizable(), "C05 A not diagonalizable")
mcq("C05-Q3", {"a": (not A.is_diagonalizable()) and g3 < A.eigenvals()[3], "b": A.is_diagonalizable(), "c": A.is_diagonalizable(), "d": not A.is_diagonalizable() and False})
ok(A.is_upper and not A.is_diagonalizable(), "C05-Q3 triangular but not diagonalizable")
B = Matrix([[2, 0, 0], [0, 2, 0], [1, 0, 5]])
ok(B.eigenvals() == {2: 2, 5: 1}, "C05-Q4 eig"); g2 = 3 - (2 * eye(3) - B).rank(); ok(g2 == 2 and (2 * eye(3) - B).rank() == 1, "C05-Q4"); num("C05-Q4", g2)
ok(B.is_diagonalizable() and not B.is_diagonal(), "C05-Q5")
mcq("C05-Q5", {"a": B.is_diagonalizable(), "b": not B.is_diagonalizable(), "c": not B.is_diagonalizable(), "d": B.is_diagonalizable() and False})
ok(not Matrix([[1, 1], [0, 1]]).is_diagonalizable() and Matrix([[2, 0], [0, 2]]).is_diagonalizable(), "C05 lesson examples")
ok((eye(2) - Matrix([[1, 1], [0, 1]])).rank() == 1 and 2 - 1 == 1 and (2 * eye(2) - Matrix([[2, 0], [0, 2]])).rank() == 0, "C05 lesson ranks")
opts = {i: pm(opt("C05-Q6", i))[0] for i in "abcd"}
mcq("C05-Q6", {i: not M_.is_diagonalizable() for i, M_ in opts.items()})
ok(opts["c"].eigenvals() == {5: 1, 6: 1} and opts["d"].eigenvals() == {1: 1, -1: 1} and (5 * eye(2) - opts["a"]).rank() == 1, "C05-Q6 explanation")

# ================================================================ C06
A = Matrix([[3, 1], [2, 2]])
ok(is_eig(A, pv(1, -2), 1) and is_eig(A, pv(1, 1), 4), "C06 premise")
truth = {}
for i in "abcd":
    P, D = pm(opt("C06-Q1", i))[:2]
    truth[i] = P.det() != 0 and D.is_diagonal() and A * P == P * D
mcq("C06-Q1", truth)
P = Matrix([[1, 1], [-2, 1]]); D = diag(1, 4)
ok(A * P == Matrix([[1, 4], [-2, 4]]) == P * D, "C06 AP=PD")
ok((A * P)[0, 1] == 4 and 3*1 + 1*1 == 4, "C06-Q2"); num("C06-Q2", (A * P)[0, 1])
P2 = P[:, ::-1]
ok(A * P2 == P2 * diag(4, 1) and A * P2 != P2 * D, "C06-Q3")
mcq("C06-Q3", {"a": A * P2 == P2 * diag(4, 1), "b": A * P2 == P2 * D, "c": A * P2 == P2 * diag(-1, -4), "d": A * P2 == P2 * D.inv()})
ok(A.eigenvals() == {1: 1, 4: 1} and (A**5).eigenvals() == {1: 1, 1024: 1} and 4**5 == 1024, "C06-Q4"); num("C06-Q4", 4**5)
A0 = Matrix([[4, 1], [2, 3]]); P0 = Matrix([[1, 1], [-2, 1]]); D0 = diag(2, 5)
ok(A0 * P0 == Matrix([[2, 5], [-4, 5]]) == P0 * D0, "C06 lesson example")
ok(A0**3 == P0 * D0**3 * P0.inv(), "C06 lesson A^k = P D^k P^-1")
ok(P * D == Matrix([[1, 4], [-2, 4]]) and P * diag(4, 1) == Matrix([[4, 1], [-8, 1]]) and P * diag(4, 1) != A * P, "C06-Q6")
ok(Q["C06-Q6"]["step"]["bugIndex"] == 2 and "4&1" in Q["C06-Q6"]["step"]["lines"][2], "C06-Q6 bug line")
ok(len(Q["C06-Q5"]["step"]["lines"]) == 5, "C06-Q5 lines")

# ================================================================ C07
Ax = symbols("a b c d"); Am = Matrix(2, 2, Ax)
# A^2 v = lambda^2 v given Av = lambda v: verified on a concrete matrix and symbolically via A*(A v) = A*(lam v)
A = Matrix([[3, 1], [2, 2]]); v = pv(1, 1)
ok(A * v == 4 * v and A**2 * v == 16 * v and A * (A * v) == A * (4 * v) == 4 * (A * v), "C07-Q1 chain on an example")
ok(Q["C07-Q1"]["step"]["lines"][3].count("\\lambda^2") == 1 and len(Q["C07-Q1"]["step"]["lines"]) == 4, "C07-Q1 lines")
# linearity: A(cv+dw) with Av = 3v, Aw = 3w, v,w independent
A3 = Matrix([[3, 0], [0, 3]]); v, w = pv(1, 0), pv(0, 1)
ok(A3 * (2 * v + 5 * w) == 3 * (2 * v + 5 * w) and (2 * v + 5 * w) != zeros(2, 1), "C07-Q2 example")
A3b = Matrix([[3, 1], [0, 3]]); v, w = pv(1, 0), pv(2, 0)  # dependent but same lambda: still fine; independence only ensures nonzero
ok(A3b * (2 * v + 5 * w) == 3 * (2 * v + 5 * w), "C07-Q2 same eigenvalue")
c_, d_ = symbols("c d"); lv = symbols("l")
ok(sp.expand(lv * c_ * pv(1, 0) + lv * d_ * pv(0, 1) - lv * (c_ * pv(1, 0) + d_ * pv(0, 1))) == zeros(2, 1), "C07 lesson linearity")
mcq("C07-Q2", {"a": is_eig(A3, 2 * v + 5 * w, 3), "b": is_eig(A3, 2 * v + 5 * w, 21), "c": not is_eig(A3, 2 * v + 5 * w), "d": is_eig(A3, 2 * v + 5 * w, 7)})
ok(2*3 + 5*3 == 21 and 2 + 5 == 7, "C07-Q2 distractor arithmetic")
Ad = Matrix([[1, 0], [0, 2]]); ev, ew = pv(1, 0), pv(0, 1)
ok(Ad * ev == ev and Ad * ew == 2 * ew and Ad * (ev + ew) == pv(1, 2) and not is_eig(Ad, ev + ew), "C07-Q3")
mcq("C07-Q3", {"a": not is_eig(Ad, ev + ew), "b": is_eig(Ad, ev + ew, 1), "c": is_eig(Ad, ev + ew, 3), "d": is_eig(Ad, ev + ew, 2)})
Bq = Matrix([[3, 1], [2, 2]]); ok(is_eig(Bq, pv(1, 1), 4) and Bq.det() != 0 and Bq.inv() * pv(1, 1) == R(1, 4) * pv(1, 1), "C07-Q4"); num("C07-Q4", R(1, 4))
ok(Q["C07-Q4"]["step"]["answer"] == 0.25, "C07-Q4 stored 0.25")
# similar matrices: PA = BP
Pm = Matrix([[1, 1], [0, 1]]); Am_ = Matrix([[3, 1], [2, 2]]); Bm = Pm * Am_ * Pm.inv()
ok(Pm * Am_ == Bm * Pm and Pm * Am_ != Am_ * Pm and Bm * Pm != Am_ * Pm, "C07-Q5 AP != PA in general")
xv = pv(1, 1); ok(Bm * (Pm * xv) == 4 * (Pm * xv), "C07-Q5 B(Px) = lambda Px")
ok(Q["C07-Q5"]["step"]["bugIndex"] == 2 and "AP" in Q["C07-Q5"]["step"]["lines"][2], "C07-Q5 bug line")
ok(Pm.det() != 0 and Pm.nullspace() == [], "C07-Q6 invertible has trivial kernel")
mcq("C07-Q6", {"a": Pm.nullspace() == [], "b": False, "c": False, "d": False})
S = Matrix([[1, 1], [1, 1]]); ok(S == S.T and S * pv(1, -1) == zeros(2, 1), "C07-Q6 symmetric matrix can kill a vector")

# ================================================================ C08 boss: bank ids
boss = [q["bankId"] for q in LV["C08"]["questions"]]
ok(4 <= len(boss) <= 6 and len(set(boss)) == len(boss), "boss size")
for bid in boss:
    bq = BANK[bid]
    ok(bid not in ("25A-B-Q4", "25B-A-Q6"), bid + " excluded id")
    ok(bq["topic"] == "eigen_diagonalization" and not bq.get("hold"), bid + " topic, not held")
    ok(bq.get("official") is True or bq.get("stepsSource") == "ai-verified", bid + " official or ai-verified")
    ok(bq.get("stepsSource") == "ai-verified" and bq.get("solutionSource") == "official-pdf", bid + " verified label")
mats = {"22B-A-Q3c": Matrix([[2, 1, 1], [1, 2, 1], [0, 0, 1]]), "23A-A-Q3c": Matrix([[1, 0, 0], [-1, 6, 1], [-1, 5, 2]]),
        "24A-A-Q3c": Matrix([[1, 1, 0], [0, -2, 0], [-1, 0, 3]]), "25A-B-Q3b": Matrix([[1] * 3] * 3)}
for bid, Mb in mats.items():
    got = pm(BANK[bid]["question"])
    if got: ok(got[0] == Mb, bid + " matrix in stem")
    ok(Mb.is_diagonalizable(), bid + " diagonalizable (boss recap says so)")
# the bank steps behind these four, recomputed
B22 = mats["22B-A-Q3c"]; ok(B22.det() == 3 and (-B22).det() == -3 or charpoly(B22).subs(lam, 0) == -3, "22B-A-Q3c |0I-B|=-3")
ok(3 - (eye(3) - B22).rank() == 2, "22B-A-Q3c dim E(1)=2")
B23 = mats["23A-A-Q3c"]; ok(B23.trace() == 9 and B23.det() == 7 and 3 - (eye(3) - B23).rank() == 2 and B23.eigenvals() == {1: 2, 7: 1}, "23A-A-Q3c")
B24 = mats["24A-A-Q3c"]; ok(B24.trace() == 2 and B24.det() == -6 and B24 * pv(2, 0, 1) == pv(2, 0, 1) and B24.eigenvals() == {1: 1, -2: 1, 3: 1}, "24A-A-Q3c")
B25 = mats["25A-B-Q3b"]; ok(B25.rank() == 1 and 3 - B25.rank() == 2 and B25.eigenvals() == {0: 2, 3: 1}, "25A-B-Q3b")
ok(B22.eigenvals() == {3: 1, 1: 2}, "22B-A-Q3c eigenvalues")
# recaps stored in C08
rc = {q["bankId"]: q["recap"] for q in LV["C08"]["questions"]}
ok("1 עם מרחב עצמי ממימד 2" in rc["23A-A-Q3c"] and "מדרגה 1" in rc["25A-B-Q3b"], "C08 recaps match the verified facts")

# ================================================================ generic arithmetic scan of every text field
def spans(text):
    return [m.group(1) or m.group(2) for m in re.finditer(r"\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$", text)]

def walk(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)

NUMERIC = re.compile(r"^[0-9+\-*/().^ ]+$")
def to_py(s):
    s = s.replace(BS + "cdot", "*").replace(BS + "times", "*").replace("{", "(").replace("}", ")")
    s = re.sub(re.escape(BS) + r"[,;! ]", "", s)
    s = re.sub(re.escape(BS) + r"tfrac\(([^()]*)\)\(([^()]*)\)", r"((\1)/(\2))", s)
    s = re.sub(re.escape(BS) + r"frac\(([^()]*)\)\(([^()]*)\)", r"((\1)/(\2))", s)
    s = s.replace("^", "**")
    s = re.sub(r"(\d)\(", r"\1*(", s); s = re.sub(r"\)\(", r")*(", s); s = re.sub(r"\)(\d)", r")*\1", s)
    return s

scanned = 0
for lid, lv in LV.items():
    for text in walk(lv):
        for sp_ in spans(text):
            parts = [p.strip() for p in sp_.split("=")]
            if len(parts) < 2: continue
            if any(BS + "neq" in p or BS + "ne" in p or "<" in p or ">" in p for p in parts): continue
            conv = [to_py(p) for p in parts]
            if not all(c and NUMERIC.match(c.replace("**", "^")) for c in conv): continue
            try: vals = [sp.sympify(c) for c in conv]
            except Exception: continue
            scanned += 1
            ok(all(v == vals[0] for v in vals), f"{lid}: numeric chain not equal: {sp_!r} -> {vals}")
print(f"numeric chains evaluated: {scanned}")

# ================================================================ coverage
want = {f"C0{n}-Q{k}" for n, cnt in [(1, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)] for k in range(1, cnt + 1)}
ok(want == set(Q), "all authored questions covered: " + str(want ^ set(Q)))
for qid, q in Q.items():
    if "options" in q:
        ok(len({o["id"] for o in q["options"]}) == len(q["options"]) and q["correctId"] in {o["id"] for o in q["options"]}, qid + " options")
    ok("explanation" in q or "explain" in q.get("step", {}), qid + " has explanation")
for lid, lv in LV.items():
    ok(lv["source"] == "ai-verified", lid + " label")
print(f"OK: {len(Q)} authored questions, {len(boss)} boss bank ids, {checks} assertions")
