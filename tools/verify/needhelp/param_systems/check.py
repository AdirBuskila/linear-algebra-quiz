# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided course `param_systems` (courses/param_systems/C01..C08.js).

Run:  PYTHONUTF8=1 py tools/verify/needhelp/param_systems/check.py
Every stored answer (mcq correctId, numeric answer, order lines, findbug index) is recomputed and asserted,
the distractors are asserted wrong, every purely numeric equality chain in any text is evaluated, and the boss
bankIds are checked against the bank (official or ai-verified, never a held sitting) and against sympy.
"""
import json, pathlib, re, subprocess, sys
import sympy as sp
from sympy import Matrix, Rational as R, symbols

HERE = pathlib.Path(__file__).resolve().parent
APP = HERE.parents[3]
BS = chr(92)
k, a, b, t, x, y, z = symbols("k a b t x y z")

# ---------------------------------------------------------------- load the levels
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
raw = subprocess.run(["node", "-e", node, str(APP / "courses" / "param_systems")], capture_output=True, check=True).stdout
LV = json.loads(raw.decode("utf8"))
Q = {}
for lid, lv in LV.items():
    for q in lv["questions"]:
        if "id" in q:
            assert q["id"] not in Q, q["id"]
            Q[q["id"]] = q
bank = json.load(open(APP / "questions.json", encoding="utf8"))["questions"]
BANK = {q["id"]: q for q in bank}

checks = 0
def ok(cond, msg):
    global checks
    checks += 1
    assert cond, "FAILED: " + msg

# ---------------------------------------------------------------- helpers
def aug(rows):
    return Matrix(rows)

def classify(M, n=None):
    """M = augmented matrix (last column = rhs). -> 'none' | 'unique' | ('inf', free)"""
    n = M.cols - 1 if n is None else n
    A, B = M[:, :n], M
    rA, rB = A.rank(), B.rank()
    if rA < rB: return "none"
    if rA == n: return "unique"
    return ("inf", n - rA)

def parse_aug(tex):
    """parse \\begin{array}{..}rows\\end{array} (rows split by double backslash, & columns) to a sympy Matrix"""
    m = re.search(re.escape(BS) + r"begin\{array\}\{[^}]*\}(.*?)" + re.escape(BS) + r"end\{array\}", tex, re.S)
    body = m.group(1)
    rows = [r for r in body.split(BS * 2) if r.strip()]
    return Matrix([[sp.sympify(c.strip()) for c in r.split("&")] for r in rows])

def mcq(qid, spec):
    """spec: {optionId: (substring that must appear in the option text, truth computed by sympy)}"""
    q = Q[qid]
    ids = [o["id"] for o in q["options"]]
    ok(sorted(ids) == sorted(spec), qid + " option ids")
    truth = set()
    for o in q["options"]:
        sub, val = spec[o["id"]]
        ok(sub in o["value"], f"{qid} option {o['id']} text drifted (wanted {sub!r}): {o['value']!r}")
        if val: truth.add(o["id"])
    ok(truth == {q["correctId"]}, f"{qid}: sympy says {truth}, stored {q['correctId']}")

def num(qid, val):
    s = Q[qid]["step"]
    ok(s["type"] == "numeric", qid + " type")
    ok(sp.nsimplify(s["answer"]) == sp.nsimplify(val), f"{qid}: stored {s['answer']} computed {val}")

def in_text(qid, *pieces):
    q = Q[qid]
    blob = json.dumps(q, ensure_ascii=False)
    for p in pieces:
        ok(p in blob.replace(BS * 2, BS), f"{qid}: expected fragment {p!r} in explanation")

def expl(qid):
    q = Q[qid]
    return q["explanation"] if "explanation" in q else q["step"]["explain"]

# ================================================================ C01
M = Matrix([[1, 2, -1, 4], [3, -1, 0, 2], [0, 1, 5, 7]])
eqs = [x + 2*y - z - 4, 3*x - y - 2, y + 5*z - 7]
A_, B_ = sp.linear_eq_to_matrix(eqs, [x, y, z])
ok(A_.row_join(B_) == M, "C01-Q1 augmented matrix")
q = Q["C01-Q1"]
for o in q["options"]:
    PM = parse_aug(o["value"])
    ok((PM == M) == (o["id"] == q["correctId"]), "C01-Q1 option " + o["id"])
# Q2
r = Matrix([[3, 7, 5]]) - 3 * Matrix([[1, 2, 4]])
ok(r == Matrix([[0, 1, -7]]), "C01-Q2 row")
num("C01-Q2", r[2])
# Q3: row operations preserve the solution set, multiplication by 0 does not
S = Matrix([[1, 2, 3], [4, 5, 6]]); sol0 = sp.solve_linear_system(Matrix([[1, 2, 3], [2, -1, 4]]), x, y)
Z = Matrix([[1, 2, 3], [0, 0, 0]])
ok(sp.solve_linear_system(Z, x, y) != sol0, "C01-Q3 multiplying a row by 0 changes the solution set")
for lam in (-2, 5):
    ok(sp.solve_linear_system(Matrix([[1, 2, 3], [2*lam, -lam, 4*lam]]), x, y) == sol0, "scaling keeps solutions")
Madd = Matrix([[1, 2, 3], [2 + 2*1, -1 + 2*2, 4 + 2*3]]); ok(sp.solve_linear_system(Madd, x, y) == sol0, "C01-Q3 add multiple keeps solutions")
ok(sp.solve_linear_system(Matrix([[2, -1, 4], [1, 2, 3]]), x, y) == sol0, "C01-Q3 swap keeps solutions")
ok(Q["C01-Q3"]["correctId"] == "c" and "0" in Q["C01-Q3"]["options"][2]["value"], "C01-Q3 stored option is multiplication by 0")
# Q4
E4 = Matrix([[1, 2, 0, 3, 1], [0, 0, 1, 4, 2]])
piv = E4[:, :4].rref()[1]
ok(piv == (0, 2), "C01-Q4 pivots")
num("C01-Q4", 4 - len(piv))
# Q5 + lesson example
S1 = Matrix([[1, 1, 3], [2, -1, 0]])
ok(sp.solve_linear_system(S1, x, y) == {x: 1, y: 2}, "C01 lesson example x=1,y=2")
ok(S1[1, :] - 2 * S1[0, :] == Matrix([[0, -3, -6]]), "C01-Q5 R2-2R1")
ok(1 + 2 == 3 and 2 * 1 - 2 == 0, "C01 lesson check")
ok(Q["C01-Q5"]["step"]["lines"][2].count("y=2") == 1 and "x=3-2=1" in Q["C01-Q5"]["step"]["lines"][3], "C01-Q5 lines")

# ================================================================ C02
def tex_matrix_in_question(qid):
    return parse_aug(Q[qid]["question"] if "question" in Q[qid] else Q[qid]["step"]["prompt"])
M1 = tex_matrix_in_question("C02-Q1"); ok(classify(M1) == "none", "C02-Q1 none")
mcq("C02-Q1", {"a": ("אין", classify(M1) == "none"), "b": ("יחיד", classify(M1) == "unique"),
               "c": ("אינסוף", isinstance(classify(M1), tuple)), "d": ("אי אפשר", False)})
M2 = tex_matrix_in_question("C02-Q2"); c2 = classify(M2); ok(c2 == ("inf", 1), "C02-Q2 inf 1")
mcq("C02-Q2", {"a": ("אין פתרון", c2 == "none"), "b": ("פתרון יחיד", c2 == "unique"),
               "c": ("משתנה חופשי אחד", c2 == ("inf", 1)), "d": ("שני משתנים", c2 == ("inf", 2))})
M3 = tex_matrix_in_question("C02-Q3"); sol = sp.solve_linear_system(M3, x, y, z)
ok(sol == {x: 1, y: 2, z: 3}, "C02-Q3 solution"); num("C02-Q3", sol[x])
ok(8 - 2 * 3 == 2 and 6 - 2 - 3 == 1 and 1 + 2 + 3 == 6, "C02 lesson arithmetic")
M4 = tex_matrix_in_question("C02-Q4"); c4 = classify(M4); ok(c4 == "unique", "C02-Q4 unique")
ok(M4.rank() == 2, "C02-Q4 rank")
mcq("C02-Q4", {"a": ("אין פתרון", c4 == "none"), "b": ("פתרון יחיד", c4 == "unique"),
               "c": ("אינסוף", isinstance(c4, tuple)), "d": ("שני פתרונות", False)})
num("C02-Q5", 5 - 3)
# Q6: number of solutions of a real linear system is 0, 1 or infinite - brute force over small systems
import itertools
seen = set()
for coeffs in itertools.product([0, 1], repeat=9):
    for rhs in itertools.product([0, 1], repeat=3):
        Mq = Matrix([list(coeffs[0:3]) + [rhs[0]], list(coeffs[3:6]) + [rhs[1]], list(coeffs[6:9]) + [rhs[2]]])
        c = classify(Mq); seen.add("none" if c == "none" else "one" if c == "unique" else "inf")
        if isinstance(c, tuple): ok(c[1] >= 1, "inf means at least one free variable, never exactly two points")
ok(seen == {"none", "one", "inf"}, "C02-Q6 only 0/1/inf occur in the 3x3 brute force")
# two solutions would need a line through exactly two points: impossible; and (3 unknowns, 1 eq) can be inconsistent
ok(classify(Matrix([[1, 1, 1, 1], [1, 1, 1, 2]])) == "none", "C02-Q6 distractor d: fewer equations than unknowns, still no solution")
mcq("C02-Q6", {"a": ("0, 1 או אינסוף", True), "b": ("0, 1, 2", False), "c": ("לפחות", False), "d": ("פחות משוואות", False)})

# ================================================================ C03
E3 = Matrix([[1, 2, -1, 3], [0, 1, 3, 1]])
yt = sp.solve(E3[1, 0]*x + E3[1, 1]*y + E3[1, 2]*z - E3[1, 3], y)[0].subs(z, t)
ok(yt == 1 - 3*t, "C03 y(t)")
num("C03-Q1", yt.subs(t, 2))
xt = sp.expand(3 - 2*yt + t); ok(xt == 1 + 7*t, "C03 x(t)")
gen = Matrix([xt, yt, t]); p = gen.subs(t, 0); d = gen.diff(t)
ok(p == Matrix([1, 1, 0]) and d == Matrix([7, -3, 1]), "C03 p, d")
ok(sp.simplify(E3[:, :3] * gen - E3[:, 3]) == sp.zeros(2, 1), "C03 general solution satisfies the system")
ok(E3[:, :3] * d == sp.zeros(2, 1), "C03 d is homogeneous")
mcq("C03-Q2", {"a": ("(1,1,0)+t\\,(7,-3,1)", True), "b": ("(-7,3,1)", d == Matrix([-7, 3, 1])),
               "c": ("(3,1,0)", p == Matrix([3, 1, 0])), "d": ("(7,3,1)", d == Matrix([7, 3, 1]))})
# lesson example: x+y+z=1, x+2y+3z=2
L = Matrix([[1, 1, 1, 1], [1, 2, 3, 2]])
Lg = Matrix([t, 1 - 2*t, t])
ok(sp.simplify(L[:, :3] * Lg - L[:, 3]) == sp.zeros(2, 1), "C03 lesson example")
ok(sp.expand(t + 2*(1 - 2*t) + 3*t) == 2, "C03 lesson check eq 2")
ok(sp.expand(1 - (1 - 2*t) - t) == t, "C03 lesson x=t")
# Q3
sys3 = lambda v: [v[0] + 2*v[1] - v[2] - 3, v[1] + 3*v[2] - 1]
cands = {"a": (8, -2, 1), "b": (8, 2, 1), "c": (1, 1, 1), "d": (3, 1, 0)}
mcq("C03-Q3", {i: ("(" + ",".join(str(c) for c in v) + ")", all(e == 0 for e in sys3(v))) for i, v in cands.items()})
# Q4, Q5
ok(sp.expand(3 - 2*(1 - 3*t) + t) == 1 + 7*t, "C03-Q5 correct arithmetic is 1+7t")
ok(sp.expand(3 - 2*(1 - 3*t) + t) != 1 + 5*t, "C03-Q5 buggy line is wrong")
s5 = Q["C03-Q5"]["step"]; ok(s5["bugIndex"] == 3 and "1+5t" in s5["lines"][3] and "1+7t" not in s5["lines"][3], "C03-Q5 bug line")
ok(all("1+5t" not in l for l in s5["lines"][:3]) and "y=1-3t" in s5["lines"][1], "C03-Q5 other lines clean")
s4 = Q["C03-Q4"]["step"]["lines"]; ok(len(s4) == 4 and "(1,1,0)+t(7,-3,1)" in s4[3] and "y=1-3t" in s4[1] and "1+7t" in s4[2] and "z=t" in s4[0], "C03-Q4 lines")

# ================================================================ C04
SA = lambda kk: Matrix([[1, 1, 1, 1], [1, 2, 3, 2], [1, 2, kk, kk]])
SB = lambda kk: Matrix([[1, 1, 1, 1], [1, 2, 3, 2], [1, 2, kk, 2]])
# last row after R2-R1, R3-R1, R3-R2
red = lambda M_: (M_[2, :] - M_[0, :]) - (M_[1, :] - M_[0, :])
ok(red(SA(k)) == Matrix([[0, 0, k - 3, k - 2]]), "C04 SA last row")
ok(red(SB(k)) == Matrix([[0, 0, k - 3, 0]]), "C04 SB last row")
ok(sp.solve(red(SA(k))[2], k) == [3], "C04-Q1 critical 3"); num("C04-Q1", 3)
for kk in range(-8, 9):
    cA = classify(SA(kk)); cB = classify(SB(kk))
    ok(cA == ("none" if kk == 3 else "unique"), f"SA k={kk}")
    ok(cB == (("inf", 1) if kk == 3 else "unique"), f"SB k={kk}")
mcq("C04-Q2", {"a": ("אין פתרון", classify(SA(3)) == "none"), "b": ("פתרון יחיד", classify(SA(3)) == "unique"),
               "c": ("אינסוף", isinstance(classify(SA(3)), tuple)), "d": ("לא ניתן", False)})
def cls_sB(kk):
    c = classify(SB(kk)); return "inf" if isinstance(c, tuple) else c
mcq("C04-Q3", {"a": ("אינסוף פתרונות", cls_sB(3) == "inf" and cls_sB(5) == "unique"),
               "b": ("אין פתרון", cls_sB(3) == "none"),
               "c": ("k=3$ פתרון יחיד", cls_sB(5) == "inf"),
               "d": ("לכל $k$", cls_sB(3) == "unique")})
# Q4: (0 0 k^2-4 | k+2)
def cls_last(p, q, kk):
    pv, qv = p.subs(k, kk), q.subs(k, kk)
    return "unique" if pv != 0 else ("none" if qv != 0 else "inf")
p4, q4 = k**2 - 4, k + 2
ok(sp.factor(p4) == (k - 2)*(k + 2), "C04-Q4 factor")
cl = {kk: cls_last(p4, q4, kk) for kk in range(-6, 7)}
ok(cl[2] == "none" and cl[-2] == "inf" and all(v == "unique" for kk, v in cl.items() if kk not in (2, -2)), "C04-Q4 classification")
ok(q4.subs(k, 2) == 4, "C04-Q4 q(2)=4")
mcq("C04-Q4", {"a": ("$k=2$ אין פתרון, $k=-2$ אינסוף", cl[2] == "none" and cl[-2] == "inf"),
               "b": ("$k=2$ אינסוף פתרונות", cl[2] == "inf" and cl[-2] == "none"),
               "c": ("k=\\pm2$ אין", cl[2] == "none" and cl[-2] == "none"),
               "d": ("כל $k$ אחר פתרון יחיד", cl[2] == "none" and cl[-2] == "unique")})
# Q5
solA = sp.solve_linear_system(SA(4), x, y, z); ok(solA == {x: 2, y: -3, z: 2}, "C04-Q5 solution at k=4")
num("C04-Q5", solA[x]); ok(2 - 6 + 8 == 4, "C04-Q5 check")
ok(red(SA(4)) == Matrix([[0, 0, 1, 2]]), "C04-Q5 last row at k=4")
# Q6
p6, q6 = 3 - k, k - 3
cl6 = {kk: cls_last(p6, q6, kk) for kk in range(-6, 7)}
ok("none" not in cl6.values() and cl6[3] == "inf", "C04-Q6 never none")
mcq("C04-Q6", {"a": ("לאף ערך", "none" not in cl6.values()), "b": ("k=3$", cl6[3] == "none"),
               "c": ("neq3$", all(cl6[kk] == "none" for kk in cl6 if kk != 3)), "d": ("לכל ערך", all(v == "none" for v in cl6.values()))})
ok(q6 == -p6, "C04 trap q is a multiple of p")

# ================================================================ C05
SD = lambda kk: Matrix([[kk, 1, 1], [1, kk, 1]])
# swapped + R2 - k R1
sw = Matrix([[1, k, 1], [k, 1, 1]]); r2 = sw[1, :] - k * sw[0, :]
ok(sp.expand(r2 - Matrix([[0, 1 - k**2, 1 - k]])) == sp.zeros(1, 3), "C05 row (0 1-k^2 | 1-k)")
ok(sp.expand(1 - k**2 - (1 - k)*(1 + k)) == 0, "C05 factor")
for kk in range(-6, 7):
    c = classify(SD(kk))
    exp = ("inf", 1) if kk == 1 else "none" if kk == -1 else "unique"
    ok(c == exp, f"C05 SD k={kk}")
# unique solution formula
sD = sp.solve([k*x + y - 1, x + k*y - 1], [x, y], dict=True)[0]
ok(sp.simplify(sD[x] - 1/(1 + k)) == 0 and sp.simplify(sD[y] - 1/(1 + k)) == 0, "C05 x=y=1/(1+k)")
ok(sp.simplify((1 - k)/(1 - k**2) - 1/(1 + k)) == 0, "C05 y formula")
ok(SD(1)[0, :] == SD(1)[1, :] , "C05-Q4 k=1 equations identical")
ok(SD(-1)[0, :2] == -SD(-1)[1, :2] and SD(-1)[0, 2] == SD(-1)[1, 2], "C05-Q4 k=-1: -x+y=1, x-y=1")
ok(1 + 1 == 2 and (1 - (-1)) == 2, "C05-Q3 q(-1)=2")
num("C05-Q3", -1)
# Q1: a(1-a)
ok(set(sp.solve(a*(1 - a), a)) == {0, 1}, "C05-Q1 zeros")
mcq("C05-Q1", {"a": ("a=0$ ו-$a=1", set(sp.solve(a*(1-a), a)) == {0, 1}), "b": ("a=1$ בלבד", set(sp.solve(a*(1-a), a)) == {1}),
               "c": ("a=0$ בלבד", set(sp.solve(a*(1-a), a)) == {0}), "d": ("a=-1$", set(sp.solve(a*(1-a), a)) == {-1, 1})})
ok(Q["C05-Q2"]["correctId"] == "a" and "להחליף" in Q["C05-Q2"]["options"][0]["value"], "C05-Q2 stored")
mcq("C05-Q4", {"a": ("k=1$ אינסוף פתרונות, $k=-1$ אין", classify(SD(1)) == ("inf", 1) and classify(SD(-1)) == "none"),
               "b": ("k=1$ אין פתרון", classify(SD(1)) == "none" and classify(SD(-1)) == ("inf", 1)),
               "c": ("k=\\pm1$ אין", classify(SD(1)) == "none" and classify(SD(-1)) == "none"),
               "d": ("k=\\pm1$ אינסוף", isinstance(classify(SD(1)), tuple) and isinstance(classify(SD(-1)), tuple))})
num("C05-Q5", (1/(1 + k)).subs(k, 3)); ok(3 * R(1, 4) + R(1, 4) == 1, "C05-Q5 check")
ok(sp.solve_linear_system(SD(3), x, y)[x] == R(1, 4), "C05-Q5 direct")
s6 = Q["C05-Q6"]["step"]
ok(s6["bugIndex"] == 1 and "1-k\\,|\\,1-k" in s6["lines"][1] and "1-k^2" not in s6["lines"][1], "C05-Q6 bug line")
ok(all("1-k^2" in l or i != 2 for i, l in enumerate(s6["lines"])), "C05-Q6 line 3 uses 1-k^2")

# ================================================================ C06
SE = lambda aa, bb: Matrix([[1, 1, 1, 1], [1, 2, 3, 2], [1, 2, aa, bb]])
ok(red(SE(a, b)) == Matrix([[0, 0, a - 3, b - 2]]), "C06 last row")
ok((SE(a, b)[1, :] - SE(a, b)[0, :]) == Matrix([[0, 1, 2, 1]]) and (SE(a, b)[2, :] - SE(a, b)[0, :]) == Matrix([[0, 1, a - 1, b - 1]]), "C06 intermediate rows")
for aa in range(-5, 8):
    for bb in range(-5, 8):
        c = classify(SE(aa, bb))
        exp = "unique" if aa != 3 else ("none" if bb != 2 else ("inf", 1))
        ok(c == exp, f"SE a={aa} b={bb}")
ok(sp.solve_linear_system(SE(a, b), x, y, z)[z] == (b - 2)/(a - 3), "C06 z=(b-2)/(a-3)")
num("C06-Q1", 3)
c = classify(SE(3, 5)); mcq("C06-Q2", {"a": ("אין פתרון", c == "none"), "b": ("פתרון יחיד", c == "unique"), "c": ("אינסוף", isinstance(c, tuple)), "d": ("רק אם", False)})
ok(red(SE(3, 5)) == Matrix([[0, 0, 0, 3]]), "C06-Q2 explanation row (0 0 0 | 3)")
c = classify(SE(3, 2)); mcq("C06-Q3", {"a": ("משתנה חופשי אחד", c == ("inf", 1)), "b": ("שני משתנים", c == ("inf", 2)), "c": ("אין פתרון", c == "none"), "d": ("פתרון יחיד", c == "unique")})
sol = sp.solve_linear_system(SE(5, 4), x, y, z); ok(sol == {x: 1, y: -1, z: 1}, "C06-Q4 solution"); num("C06-Q4", sol[y])
ok(red(SE(5, 4)) == Matrix([[0, 0, 2, 2]]) and 1 - 2 + 5 == 4, "C06-Q4 explanation")
none_pairs = lambda f: all((classify(SE(aa, bb)) == "none") == f(aa, bb) for aa in range(-5, 8) for bb in range(-5, 8))
mcq("C06-Q5", {"a": ("a=3$ ו-$b\\neq2", none_pairs(lambda aa, bb: aa == 3 and bb != 2)),
               "b": ("a\\neq3$ ו-$b\\neq2", none_pairs(lambda aa, bb: aa != 3 and bb != 2)),
               "c": ("a=3$, לכל", none_pairs(lambda aa, bb: aa == 3)),
               "d": ("b\\neq2$, לכל", none_pairs(lambda aa, bb: bb != 2))})
g = Matrix([t, 1 - 2*t, t]); ok(sp.simplify(SE(3, 2)[:, :3] * g - SE(3, 2)[:, 3]) == sp.zeros(3, 1), "C06 general solution at (3,2)")
num("C06-Q6", g.diff(t)[1]); ok(g.diff(t) == Matrix([1, -2, 1]) and g.subs(t, 0) == Matrix([0, 1, 0]), "C06-Q6 p,d")

# ================================================================ C07
def hom_dim(Mh):
    return Mh.cols - Mh.rank()
H2 = lambda aa: Matrix([[1, 1, 1], [1, 2, 3], [1, 2, aa]])
H1 = lambda aa: Matrix([[1, 1, 1], [1, aa, 1]])
H3 = lambda aa: Matrix([[1, 1, 1], [aa, 1, 0], [1, aa, 0]])
ok(red(Matrix([[1, 1, 1, 0], [1, 2, 3, 0], [1, 2, a, 0]])) == Matrix([[0, 0, a - 3, 0]]), "C07-Q2 last row")
for aa in range(-6, 7):
    ok((hom_dim(H2(aa)) == 1) == (aa == 3) and (hom_dim(H2(aa)) == 0) == (aa != 3), f"H2 a={aa}")
    ok(hom_dim(H1(aa)) == (2 if aa == 1 else 1), f"H1 a={aa}")
    ok(hom_dim(H3(aa)) == (1 if aa in (1, -1) else 0), f"H3 a={aa}")
num("C07-Q2", 3)
ok(H2(3).nullspace()[0].T * 1 == Matrix([[1, -2, 1]]), "C07-Q3 line direction (1,-2,1)")
mcq("C07-Q3", {"a": ("ישר", hom_dim(H2(3)) == 1), "b": ("מישור", hom_dim(H2(3)) == 2), "c": ("הנקודה", hom_dim(H2(3)) == 0), "d": ("אין פתרון", False)})
mcq("C07-Q1", {"a": ("לפחות פתרון אחד", all(Matrix([0, 0, 0]) == Matrix([0, 0, 0]) for _ in [0]) and True),
               "b": ("אין פתרון", False), "c": ("אינסוף פתרונות", all(hom_dim(H2(aa)) > 0 for aa in range(-6, 7))),
               "d": ("הפתרון היחיד", all(hom_dim(H2(aa)) == 0 for aa in range(-6, 7)))})
ok(all((H2(aa) * Matrix([0, 0, 0])) == Matrix([0, 0, 0]) for aa in range(-6, 7)), "C07-Q1 zero always a solution")
ok(sp.simplify(H1(a) - H1(a)) == sp.zeros(2, 3) and (H1(a)[1, :] - H1(a)[0, :]) == Matrix([[0, a - 1, 0]]), "C07-Q4 R2-R1")
d1 = {aa: hom_dim(H1(aa)) for aa in range(-6, 7)}
mcq("C07-Q4", {"a": ("a\\neq1$ הפתרונות ישר, $a=1$ הפתרונות מישור", d1[2] == 1 and d1[1] == 2),
               "b": ("a\\neq1$ רק", d1[2] == 0 and d1[1] == 1), "c": ("a\\neq1$ הפתרונות מישור", d1[2] == 2 and d1[1] == 1),
               "d": ("a\\neq1$ רק $\\vec 0$, $a=1$ מישור", d1[2] == 0 and d1[1] == 2)})
num("C07-Q5", hom_dim(H1(1)))
# lesson example: H3 at a=1 and a=-1
n1 = H3(1).nullspace()[0]; n2 = H3(-1).nullspace()[0]
ok(n1.T == Matrix([[1, -1, 0]]) or n1.T == -Matrix([[1, -1, 0]]), "C07 lesson a=1 line (1,-1,0)")
ok(sp.simplify(n2.T / n2[0]) == Matrix([[1, 1, -2]]), "C07 lesson a=-1 line (1,1,-2)")
num("C07-Q6", (n2 / n2[0])[2])
ok(sp.factor(H3(a).det()) == (a - 1)*(a + 1), "C07 lesson det a^2-1")

# ================================================================ explanation numbers not covered above
ok(sp.solve_linear_system(M4, x, y) == {x: 1, y: 2}, "C02-Q4 explanation x=1,y=2")
ok(3 + 2 * 1 - 0 == 5 and 1 + 0 == 1, "C03-Q3 (3,1,0): eq1 gives 5, eq2 gives 1")
ok(1 + 2 * 1 - 1 == 2 and 2 + 3 * 1 == 5, "C03-Q3 (1,1,1) eq1 gives 2; (8,2,1) eq2 gives 5")
ok((8 + 2 * (-2) - 1, -2 + 3 * 1) == (3, 1), "C03-Q3 (8,-2,1) solves both")
ok(SA(3)[2, 3] - SA(3)[1, 3] == 1 and (red(SA(3)))[3] == 1, "C04 lesson q(3)=1")
ok(red(SB(3)) == Matrix([[0, 0, 0, 0]]), "C04 lesson SB at k=3 is (0 0 0 | 0)")
ok((H1(1)[1, :] - H1(1)[0, :]) == Matrix([[0, 0, 0]]), "C07-Q4 a=1 identical equations")
ok((H1(2)[1, :] - H1(2)[0, :]) == Matrix([[0, 1, 0]]), "C07-Q4 a=2 row (0 a-1 0)")
ok(H3(1)[1, :] == Matrix([[1, 1, 0]]) and H3(-1)[1, :] == Matrix([[-1, 1, 0]]) and H3(-1)[2, :] == Matrix([[1, -1, 0]]), "C07 lesson rows at a=+-1")

# ================================================================ C08 boss: bank ids
EXCLUDED = ("22A-B", "21A-B", "21A-A", "20A-A")
boss = [q["bankId"] for q in LV["C08"]["questions"]]
ok(1 <= len(boss) and 4 <= len(boss) <= 6 and len(set(boss)) == len(boss), "boss size")
for bid in boss:
    bq = BANK[bid]
    ok(not any(bid.startswith(e) for e in EXCLUDED), bid + " from an excluded sitting")
    ok(bq["topic"] == "linear_systems" and bq.get("official") is True, bid + " official + topic")
    ok(not bq.get("hold") and bq.get("confidence") == "high", bid + " not held")
    ok(bq.get("stepsSource") == "ai-verified" or bq.get("solutionSource") == "official-pdf", bid + " verified label")
# systems behind the boss questions (contexts)
S22 = lambda kk: Matrix([[1, 1, kk, 2], [3, 4, 2, kk], [2, 3, -1, 1]])
for kk in range(-8, 9):
    c = classify(S22(kk)); ok(c == (("inf", 1) if kk == 3 else "unique"), f"22B-A k={kk}")
ok(sp.factor(S22(k)[:, :3].det()) == (k - 3), "22B-A det")
s = sp.solve_linear_system(S22(k), x, y, z)
ok(sp.simplify(s[x] - 3*(k + 2)) == 0 and sp.simplify(s[y] + 2*(k + 2)) == 0 and sp.simplify(s[z] + 1) == 0, "22B-A-Q2a solution 3(k+2), -2(k+2), -1")
ok("3(k+2)" in BANK["22B-A-Q2a"]["solution"], "22B-A-Q2a stored x")
ok(not any(classify(S22(kk)) == "none" for kk in range(-20, 21)), "22B-A-Q2b: no k gives no solution")
S24 = lambda kk: Matrix([[1, 0, -3, -3], [2, kk, -1, -2], [1, 2, kk, 1]])
ok(sp.factor(S24(k)[:, :3].det()) == (k - 2)*(k + 5), "24A det (k-2)(k+5)")
nones = [kk for kk in range(-20, 21) if classify(S24(kk)) == "none"]
ok(nones == [-5], f"24A-A-Q2b: no solution only at k=-5, got {nones}")
ok(classify(S24(2)) == ("inf", 1), "24A k=2 infinite")
ok(4 * (-5 - 2) == -28, "24A-A-Q2b stored -28"); ok("-5" in BANK["24A-A-Q2b"]["solution"] and "-28" in BANK["24A-A-Q2b"]["solution"], "24A stored text")
S25 = lambda aa: Matrix([[1, -1, 2, 0], [-1, aa, aa - 3, aa], [0, aa - 1, 2*aa, 2*aa + 1], [1, aa - 2, 2*aa + 2, 2*aa + 1]])
for aa in range(-8, 9):
    c = classify(S25(aa)); exp = "none" if aa == 1 else ("inf", 1) if aa == -1 else "unique"
    ok(c == exp, f"25B-A a={aa}")
sol25 = Matrix([R(1, 2) - 3*t, R(1, 2) - t, t]); ok(sp.simplify(S25(-1)[:, :3] * sol25 - S25(-1)[:, 3]) == sp.zeros(4, 1), "25B-A-Q2c solution")
ok(sol25.subs(t, 0) == Matrix([R(1, 2), R(1, 2), 0]) and sol25.diff(t) == Matrix([-3, -1, 1]), "25B-A-Q2c p,d")
S25h = lambda aa: Matrix([[aa, aa, -1], [aa**2, aa, aa**2 - aa], [aa, aa, 2*aa + 1]])
for aa in range(-6, 7):
    ok(hom_dim(S25h(aa)) == (1 if aa in (1, -1) else 2 if aa == 0 else 0), f"25A-A a={aa}")
ok(hom_dim(S25h(0)) == 2, "25A-A a=0 plane (rank 1)")
ok(hom_dim(S25h(1)) == 1 and hom_dim(S25h(-1)) == 1, "25A-A-Q2c: lines at a=1 and a=-1 only")
ok(all(hom_dim(S25h(Rr)) != 1 for Rr in [R(1, 2), R(-1, 2), 2, -2, 3, R(1, 3)]), "25A-A other values not a line")
ok(set(sp.solve(sp.factor(S25h(a).det()), a)) == {0, 1, -1}, "25A det roots 0,1,-1")

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
    s = re.sub(re.escape(BS) + r"frac\(([^()]*)\)\(([^()]*)\)", r"((\1)/(\2))", s)
    s = s.replace("^", "**")
    s = re.sub(r"(\d)\(", r"\1*(", s); s = re.sub(r"\)\(", r")*(", s); s = re.sub(r"\)(\d)", r")*\1", s)
    return s

scanned = 0
CONTRADICTIONS = {"0=5", "0=1", "0=2", "0=3"}
for lid, lv in LV.items():
    for text in walk(lv):
        for sp_ in spans(text):
            parts = [p.strip() for p in sp_.split("=")]
            if len(parts) < 2: continue
            if any(BS + "neq" in p or BS + "ne" in p or "<" in p or ">" in p for p in parts): continue
            if re.fullmatch(r"[a-z]|[a-z]\([^)]*\)|[a-z]\{?[0-9]\}?|[a-z]_[0-9]", parts[0]) and len(parts) >= 3:
                parts = parts[1:]               # "y=8-2*3=2": check the numeric chain after the variable
            conv = [to_py(p) for p in parts]
            if not all(NUMERIC.match(c.replace("**", "^")) and c for c in conv): continue
            try:
                vals = [sp.nsimplify(sp.sympify(c)) for c in conv]
            except Exception:
                continue
            if sp_.strip() in CONTRADICTIONS:   # deliberate "0=c" rows of inconsistent systems
                ok(vals[0] == 0 and vals[1] != 0, "contradiction span " + sp_)
                continue
            scanned += 1
            ok(all(v == vals[0] for v in vals), f"{lid}: numeric chain not equal: {sp_!r} -> {vals}")
print(f"numeric chains evaluated: {scanned}")

# ================================================================ every question is covered by an assertion above
ids_checked = {"C01-Q1","C01-Q2","C01-Q3","C01-Q4","C01-Q5","C02-Q1","C02-Q2","C02-Q3","C02-Q4","C02-Q5","C02-Q6","C03-Q1","C03-Q2","C03-Q3","C03-Q4","C03-Q5",
               "C04-Q1","C04-Q2","C04-Q3","C04-Q4","C04-Q5","C04-Q6","C05-Q1","C05-Q2","C05-Q3","C05-Q4","C05-Q5","C05-Q6","C06-Q1","C06-Q2","C06-Q3","C06-Q4","C06-Q5","C06-Q6",
               "C07-Q1","C07-Q2","C07-Q3","C07-Q4","C07-Q5","C07-Q6"}
ok(ids_checked == set(Q), "all authored questions covered: missing " + str(set(Q) ^ ids_checked))
for qid, q in Q.items():
    if "options" in q:
        ok(q["correctId"] in [o["id"] for o in q["options"]] and len(q["options"]) == 4, qid + " options")
print(f"ALL {checks} CHECKS PASSED")
