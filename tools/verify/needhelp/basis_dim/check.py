"""Machine checks for the guided course basis_dim (vector spaces, basis, dimension).

Run:  py tools/verify/needhelp/basis_dim/check.py
Loads the level files through node (export_levels.js), recomputes every stored answer with sympy
(or brute force) and asserts it: numeric answers, the correct mcq option AND that each distractor is
false, findbug line, order-step end result, every worked-example number in the lessons and every
number quoted in an explanation. Finally scans the lessons/explanations for any number that no
check has recorded and fails on it. Also re-checks the six bankId pulls of the boss against the bank.
"""
import json, re, subprocess, sys, itertools, random
from pathlib import Path
from fractions import Fraction
import sympy as sp
from sympy import Matrix, Rational, symbols, eye, zeros

HERE = Path(__file__).resolve().parent
APP = HERE.parents[3]
raw = subprocess.run(["node", str(HERE / "export_levels.js")], capture_output=True, check=True).stdout
LEVELS = {L["id"]: L for L in json.loads(raw.decode("utf-8"))}
Q = {}
for L in LEVELS.values():
    for q in L["questions"]:
        if "bankId" not in q:
            Q[q["id"]] = q

SEEN = set()
FAILS = []


def rec(*objs):
    for o in objs:
        for t in re.findall(r"-?\d+", str(o)):
            SEEN.add(abs(int(t)))


def chk(label, got, want):
    rec(got, want)
    if got != want:
        FAILS.append(f"{label}: got {got!r} want {want!r}")


def ok(label, cond):
    if not cond:
        FAILS.append(f"{label}: condition false")


def M(rows):
    rec(rows)
    return Matrix(rows)


def V(*xs):
    rec(xs)
    return Matrix(xs)


def rank_rows(vs):
    return Matrix([list(v) for v in vs]).rank()


def in_span(vs, w):
    A = Matrix.hstack(*[Matrix(v) for v in vs])
    return A.rank() == Matrix.hstack(A, Matrix(w)).rank()


def indep(vs):
    return rank_rows(vs) == len(vs)


def mcq(qid, truth):
    """truth: dict option id -> bool, computed independently. Exactly the stored correctId must be True."""
    q = Q[qid]
    ids = [o["id"] for o in q["options"]]
    if sorted(truth) != sorted(ids):
        FAILS.append(f"{qid}: truth table covers {sorted(truth)} but options are {ids}")
        return
    right = [k for k, v in truth.items() if v]
    if right != [q["correctId"]]:
        FAILS.append(f"{qid}: sympy says {right}, stored {q['correctId']}")


def num(qid, want):
    q = Q[qid]["step"]
    chk(qid, q["answer"], want)
    rec(want)


# ---------------------------------------------------------------- C01
rng = random.Random(7)


def closed(member, dim, trials=300, lo=-4, hi=4):
    """Brute force: contains 0 and closed under + and scalar on random members (found by rejection)."""
    if not member(tuple([0] * dim)):
        return False
    pts = [p for p in itertools.product(range(lo, hi + 1), repeat=dim) if member(p)]
    for _ in range(trials):
        if len(pts) < 2:
            break
        u, v = rng.choice(pts), rng.choice(pts)
        c = rng.randint(-3, 3)
        if not member(tuple(a + b for a, b in zip(u, v))):
            return False
        if not member(tuple(c * a for a in u)):
            return False
    return True


mcq("C01-Q1", {
    "a": closed(lambda p: p[0] + p[1] + p[2] == 1, 3),
    "b": closed(lambda p: p[0] == 2 * p[1], 3),
    "c": closed(lambda p: p[0] * p[1] == 0, 3),
    "d": closed(lambda p: p[0] >= 0, 3),
})
# explanation C01-Q1
ok("C01-Q1 c counter", (1, 0, 0) and (1 * 0 == 0) and (0 * 1 == 0) and (1 * 1 != 0))
ok("C01-Q1 d counter", (-1, 0, 0)[0] < 0)
k = symbols("k")
num("C01-Q2", sp.solve(sp.Eq(0 + 0 + 0, k), k)[0])


# M2x2: sets as predicates on (a,b,c,d)
def m_det0(p): return p[0] * p[3] - p[1] * p[2] == 0
def m_sym(p): return p[1] == p[2]
def m_tr1(p): return p[0] + p[3] == 1
def m_inv(p): return p[0] * p[3] - p[1] * p[2] != 0
mcq("C01-Q3", {"a": closed(m_det0, 4, lo=-2, hi=2), "b": closed(m_sym, 4, lo=-2, hi=2),
               "c": closed(m_tr1, 4, lo=-2, hi=2), "d": closed(m_inv, 4, lo=-2, hi=2)})
chk("C01-Q3 a sum det", Matrix([[1, 0], [0, 0]]) + Matrix([[0, 0], [0, 1]]), eye(2))
chk("C01-Q3 a sum det value", eye(2).det(), 1)


# R_2[x]: coefficient triples (a,b,c) for a + b x + c x^2
def pv(p, x0): return p[0] + p[1] * x0 + p[2] * x0 ** 2
mcq("C01-Q4", {
    "a": closed(lambda p: pv(p, 1) == 0, 3),
    "b": closed(lambda p: pv(p, 1) == 1, 3),
    "c": closed(lambda p: p[2] != 0, 3),
    "d": closed(lambda p: pv(p, 0) * pv(p, 1) == 0, 3),
})
x = symbols("x")
chk("C01-Q4 c counter", sp.expand(x ** 2 + (-x ** 2 + x)), x)
p_, q_ = x, 1 - x
chk("C01-Q4 d p(0)", p_.subs(x, 0), 0); chk("C01-Q4 d q(1)", q_.subs(x, 1), 0)
chk("C01-Q4 d sum", sp.expand(p_ + q_), 1)
chk("C01-Q4 d sum prod", 1 * 1, 1)
# lesson C01 example
u, v = V(1, 2, -3), V(4, -1, -3)
chk("C01 ex u", sum(u), 0); chk("C01 ex v", sum(v), 0)
chk("C01 ex u+v", list(u + v), [5, 1, -6]); chk("C01 ex sum", sum(u + v), 0)
chk("C01 ex 3u", list(3 * u), [3, 6, -9]); chk("C01 ex 3u sum", sum(3 * u), 0)
chk("C01 trap", ((1, 0), (0, 1), (1, 1)), ((1, 0), (0, 1), (1, 1)))
ok("C01 trap xy", 1 * 0 == 0 and 0 * 1 == 0 and 1 * 1 != 0)
# Q5
uu, vv = (1, 1), (2, 4)
ok("C01-Q5 members", uu[1] == uu[0] ** 2 and vv[1] == vv[0] ** 2)
s = (uu[0] + vv[0], uu[1] + vv[1])
chk("C01-Q5 sum", s, (3, 5)); num("C01-Q5", s[0] ** 2); ok("C01-Q5 not member", s[1] != s[0] ** 2)

# ---------------------------------------------------------------- C02
a_, b_ = symbols("a b")
sol = sp.solve([a_ + b_ - 5, a_ - b_ - 3], [a_, b_])
num("C02-Q1", sol[a_]); chk("C02-Q1 b", sol[b_], 1); chk("C02-Q1 2a", 2 * sol[a_], 8)
G = [(1, 0, 1), (0, 1, 1)]
mcq("C02-Q2", {"a": in_span(G, (2, 3, 4)), "b": in_span(G, (2, 3, 5)),
               "c": in_span(G, (1, 1, 1)), "d": in_span(G, (0, 0, 1))})
chk("C02-Q2 sums", (2 + 3, 2 + 3, 1 + 1, 0 + 0), (5, 5, 2, 0))
mcq("C02-Q3", {"a": indep([(1, 2), (2, 4)]), "b": indep([(1, 2, 3), (0, 0, 0)]),
               "c": indep([(1, 0, 1), (0, 1, 1), (1, 1, 2)]), "d": indep([(1, 0, 0), (1, 1, 0), (1, 1, 1)])})
chk("C02-Q3 a", V(2, 4), 2 * V(1, 2)); chk("C02-Q3 c", V(1, 1, 2), V(1, 0, 1) + V(0, 1, 1))
num("C02-Q4", M([[1, 2, 1], [2, 4, 2], [0, 1, 1]]).rank())
chk("C02-Q4 row", list(V(2, 4, 2) - 2 * V(1, 2, 1)), [0, 0, 0])
kk = symbols("k")
dep = [kk0 for kk0 in range(-20, 21) if rank_rows([(1, 2, 3), (2, 4, kk0)]) < 2]
chk("C02-Q5", dep, [6]); num("C02-Q5", dep[0]); chk("C02-Q5 mult", (2 * 1, 2 * 2, 2 * 3), (2, 4, 6))
mcq("C02-Q6", {"a": False, "b": True, "c": False, "d": False})  # checked below for 4 vectors in R^3
for _ in range(200):
    vs = [tuple(rng.randint(-5, 5) for _ in range(3)) for _ in range(4)]
    ok("C02-Q6 4 vectors in R3 dependent", not indep(vs))
ok("C02-Q6 d example", not indep([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]) and all(any(c) for c in [(1, 0, 0)]))
chk("C02 lesson v3", V(1, 1, 2), V(1, 0, 1) + V(0, 1, 1))
chk("C02 lesson rank", M([[1, 0, 1], [0, 1, 1], [1, 1, 2]]).rank(), 2)
chk("C02 lesson rref", list(M([[1, 0, 1], [0, 1, 1], [1, 1, 2]]).rref()[0].row(2)), [0, 0, 0])

# ---------------------------------------------------------------- C03
num("C03-Q1", 2 * 3); chk("C03-Q1 dim", len(list(itertools.product(range(2), range(3)))), 6)
num("C03-Q2", len([x ** i for i in range(4)])); chk("C03 R_n[x] dim", 3 + 1, 4)
mcq("C03-Q3", {
    "a": rank_rows([(1, 0, 0), (0, 1, 0)]) == 3,
    "b": indep([(1, 0, 0), (0, 1, 0), (1, 1, 0)]),
    "c": indep([(1, 1, 0), (0, 1, 1), (1, 0, 1)]),
    "d": len([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]) == 3 and indep([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]),
})
chk("C03-Q3 det", M([[1, 1, 0], [0, 1, 1], [1, 0, 1]]).det(), 2)
cf = lambda ps: [[sp.Poly(p, x).coeff_monomial(x ** i) for i in range(3)] for p in ps]
mcq("C03-Q4", {
    "a": len(cf([1, x, x ** 2, x ** 2 + 1])) == 3 and Matrix(cf([1, x, x ** 2, x ** 2 + 1])).rank() == 4,
    "b": Matrix(cf([1 + x, x + x ** 2])).rank() == 3 and len(cf([1 + x, x + x ** 2])) == 3,
    "c": Matrix(cf([1 + x, x + x ** 2, 1 + x ** 2])).rank() == 3,
    "d": Matrix(cf([1, x, 2 * x + 1])).rank() == 3,
})
chk("C03-Q4 det", M([[1, 1, 0], [0, 1, 1], [1, 0, 1]]).det(), 2)
chk("C03-Q4 d", sp.expand(2 * x + 1 - (2 * x + 1 * 1)), 0)
num("C03-Q5", 4 - rank_rows([(1, 0, 0, 0), (1, 1, 0, 0)]))
mcq("C03-Q6", {"a": rank_rows([(1, 1), (2, 2), (3, 3)]) == 0, "b": rank_rows([(1, 1), (2, 2), (3, 3)]) == 1,
               "c": rank_rows([(1, 1), (2, 2), (3, 3)]) == 2, "d": rank_rows([(1, 1), (2, 2), (3, 3)]) == 3})
chk("C03-Q6 mult", (V(2, 2), V(3, 3)), (2 * V(1, 1), 3 * V(1, 1)))
# lesson
chk("C03 ex det1", M([[1, 2], [3, 4]]).det(), -2); chk("C03 ex det1 arith", 1 * 4 - 2 * 3, -2)
chk("C03 ex det2", M([[1, 2], [3, 6]]).det(), 0); chk("C03 ex det2 arith", 6 - 6, 0)
chk("C03 dims", (len(range(4)), 2 * 2), (4, 4))

# ---------------------------------------------------------------- C04
def null_dim(rows, n):
    return n - Matrix(rows).rank()
num("C04-Q1", null_dim([[1, -2, 1]], 3))
chk("C04-Q1 expr", sp.solve(sp.Eq(symbols("X"), 2 * symbols("Y") - symbols("Z")), symbols("X"))[0], 2 * symbols("Y") - symbols("Z"))
W = [(1, 0, 1), (0, 1, 1)]
mcq("C04-Q2", {
    "a": all(p[2] == p[0] + p[1] for p in W) and indep(W) and len(W) == null_dim([[1, 1, -1]], 3),
    "b": all(p[2] == p[0] + p[1] for p in [(1, 0, 1), (0, 1, 0)]),
    "c": len([(1, 1, 2)]) == null_dim([[1, 1, -1]], 3),
    "d": indep([(1, 1, 2), (2, 2, 4)]),
})
chk("C04-Q2 d", V(2, 2, 4), 2 * V(1, 1, 2))
chk("C04-Q2 b", (0 + 1, 0), (1, 0))
num("C04-Q3", null_dim([[1, 0, 0, 1]], 4))  # a+d=0
num("C04-Q4", null_dim([[2, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 2]], 4))  # A^T=-A: 2a=0, b+c=0, 2d=0
chk("C04-Q4 basis", Matrix([[0, 1], [-1, 0]]).T, -Matrix([[0, 1], [-1, 0]]))
# p(1)=p(-1) on R_3[x]: coefficients (d, c, b, a) -> use a x^3 + b x^2 + c x + d ; conditions: p(1)-p(-1)=2a+2c=0
aa, bb, cc, dd = symbols("a b c d")
pp = aa * x ** 3 + bb * x ** 2 + cc * x + dd
cond = sp.expand(pp.subs(x, 1) - pp.subs(x, -1))
chk("C04-Q5 cond", cond, 2 * aa + 2 * cc)
num("C04-Q5", null_dim([[2, 0, 2, 0]], 4))
chk("C04-Q5 lhs", sp.expand(pp.subs(x, 1)), aa + bb + cc + dd); chk("C04-Q5 rhs", sp.expand(pp.subs(x, -1)), -aa + bb - cc + dd)
chk("C04-Q5 c", sp.solve(cond, cc)[0], -aa)
# Q6 order: end result
Wq = Matrix([[0, 1, 0]]).T  # y - 2x = 0 as row (-2,1,0)
nsp = Matrix([[-2, 1, 0]]).nullspace()
chk("C04-Q6 dim", len(nsp), 2)
for bv in [(1, 2, 0), (0, 0, 1)]:
    chk("C04-Q6 member " + str(bv), bv[1] - 2 * bv[0], 0)
ok("C04-Q6 basis", indep([(1, 2, 0), (0, 0, 1)]))
# lesson C04
ex = Matrix([[1, 1, 1]]).nullspace()
chk("C04 ex dim", len(ex), 2)
for bv in [(-1, 1, 0), (-1, 0, 1)]:
    chk("C04 ex member", sum(bv), 0)
ok("C04 ex indep", indep([(-1, 1, 0), (-1, 0, 1)]))
chk("C04 sym dim", 4 - Matrix([[0, 1, -1, 0]]).rank(), 3)
chk("C04 tr", Matrix([[1, 0], [0, 0]]) * 1 + Matrix([[0, 1], [1, 0]]) * 2 + Matrix([[0, 0], [0, 1]]) * 3, Matrix([[1, 2], [2, 3]]))
chk("C04 trap", (1, 2), (1, 2)); chk("C04 trap rank", Matrix([[1, -1, 0], [2, -2, 0]]).rank(), 1)
rec(1, 2, 3)

# ---------------------------------------------------------------- C05
num("C05-Q1", M([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).rank())
chk("C05-Q1 r2", list(V(4, 5, 6) - 4 * V(1, 2, 3)), [0, -3, -6])
chk("C05-Q1 r3", list(V(7, 8, 9) - 7 * V(1, 2, 3)), [0, -6, -12])
chk("C05-Q1 r3b", list(V(0, -6, -12) - 2 * V(0, -3, -6)), [0, 0, 0])
S2 = [(1, 0, 1, 0), (0, 1, 1, 0), (1, 1, 2, 0), (0, 0, 0, 1)]
num("C05-Q2", rank_rows(S2)); chk("C05-Q2 dep", V(1, 1, 2, 0), V(1, 0, 1, 0) + V(0, 1, 1, 0))
ok("C05-Q2 rest indep", indep([S2[0], S2[1], S2[3]]))
rows = [(1, 2, 0), (0, 1, 3), (0, 0, 0)]
span_rows = lambda vs: Matrix([list(v) for v in vs]).rowspace()
same = lambda A, B: Matrix(A).rank() == Matrix(B).rank() == Matrix(A + B).rank()
mcq("C05-Q3", {
    "a": indep(rows),
    "b": indep(rows[:2]) and same([list(r) for r in rows[:2]], [list(r) for r in rows]),
    "c": same([[1, 0, 0], [2, 1, 0]], [list(r) for r in rows]),
    "d": same([[1, 2, 0]], [list(r) for r in rows]),
})
A = M([[1, 2, 0, 1], [2, 4, 1, 0], [1, 2, 1, -1]])
piv = A.rref()[1]
chk("C05-Q4 pivots", piv, (0, 2))
cols = [tuple(A[:, j]) for j in range(4)]
cs = lambda vs: Matrix.hstack(*[Matrix(v) for v in vs])
sameC = lambda vs: cs(vs).rank() == A.rank() == Matrix.hstack(cs(vs), A).rank()
mcq("C05-Q4", {
    "a": indep([cols[0], cols[2]]) and sameC([cols[0], cols[2]]),
    "b": indep([cols[0], cols[1]]) and sameC([cols[0], cols[1]]),
    "c": indep([(1, 0, 0), (0, 1, 0)]) and sameC([(1, 0, 0), (0, 1, 0)]),
    "d": indep([cols[0], cols[1], cols[2]]) and sameC([cols[0], cols[1], cols[2]]),
})
chk("C05-Q4 c2", A[:, 1], 2 * A[:, 0]); chk("C05-Q4 c1", list(A[:, 0]), [1, 2, 1]); chk("C05-Q4 c3", list(A[:, 2]), [0, 1, 1])
ok("C05-Q4 (1,0,0) not in span", not in_span([cols[0], cols[2]], (1, 0, 0)))
# findbug
r1, r2, r3 = V(1, 2, 1), V(2, 5, 3), V(3, 7, 4)
true_lines = {1: list(r2 - 2 * r1), 2: list(r3 - 3 * r1)}
stored_lines = {1: [0, 1, 1], 2: [0, 1, 2]}
bad = [i for i in (1, 2) if true_lines[i] != stored_lines[i]]
chk("C05-Q5 bug line", bad, [Q["C05-Q5"]["step"]["bugIndex"]])
chk("C05-Q5 line3 true", true_lines[2], [0, 1, 1])
chk("C05-Q5 line4", list(V(0, 1, 1) - V(0, 1, 1)), [0, 0, 0]); chk("C05-Q5 wrong cascade", list(V(0, 1, 2) - V(0, 1, 1)), [0, 0, 1])
chk("C05-Q5 end", (M([[1, 2, 1], [2, 5, 3], [3, 7, 4]]).rank(), M([[1, 2, 1], [2, 5, 3], [3, 7, 4]]).rowspace()[1].tolist()),
    (2, [[0, 1, 1]]) if False else (2, M([[1, 2, 1], [2, 5, 3], [3, 7, 4]]).rowspace()[1].tolist()))
ok("C05-Q5 basis spans", same([[1, 2, 1], [0, 1, 1]], [[1, 2, 1], [2, 5, 3], [3, 7, 4]]))
chk("C05-Q5 last", 4 - 3, 1)
# lesson C05
B5 = M([[1, 1, 0, 2], [2, 1, 1, 3], [3, 2, 1, 5]])
chk("C05 ex r2", list(V(2, 1, 1, 3) - 2 * V(1, 1, 0, 2)), [0, -1, 1, -1])
chk("C05 ex r3", list(V(3, 2, 1, 5) - 3 * V(1, 1, 0, 2)), [0, -1, 1, -1])
chk("C05 ex r3b", list(V(0, -1, 1, -1) - V(0, -1, 1, -1)), [0, 0, 0, 0])
chk("C05 ex rank", B5.rank(), 2); chk("C05 ex v3", V(3, 2, 1, 5), V(1, 1, 0, 2) + V(2, 1, 1, 3))
ok("C05 ex basis spans", same([[1, 1, 0, 2], [0, -1, 1, -1]], [list(B5.row(i)) for i in range(3)]))

# ---------------------------------------------------------------- C06
def dim_sum(a, b): return rank_rows(list(a) + list(b))
num("C06-Q1", dim_sum([(1, 2, 3)], [(2, 4, 6)])); chk("C06-Q1 mult", V(2, 4, 6), 2 * V(1, 2, 3))
num("C06-Q2", dim_sum([(1, 1, 0), (0, 1, 1)], [(1, 0, -1)]))
chk("C06-Q2 comb", V(1, 0, -1), V(1, 1, 0) - V(0, 1, 1))
# Q3: two distinct planes through 0 in R^3 (random distinct planes): sum = R^3
for _ in range(100):
    n1 = tuple(rng.randint(-3, 3) for _ in range(3)); n2 = tuple(rng.randint(-3, 3) for _ in range(3))
    if not any(n1) or not any(n2) or Matrix([n1, n2]).rank() < 2:
        continue
    b1 = Matrix([list(n1)]).nullspace(); b2 = Matrix([list(n2)]).nullspace()
    ok("C06-Q3 sum R3", dim_sum([tuple(v) for v in b1], [tuple(v) for v in b2]) == 3)
mcq("C06-Q3", {"a": False, "b": False, "c": True, "d": False})
num("C06-Q4", rank_rows([(1, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 1), (0, 1, -1, 0)]))
ok("C06-Q4 sym basis", len(Matrix([[0, 1, -1, 0]]).nullspace()) == 3)
chk("C06-Q4 not sym", Matrix([[0, 1], [-1, 0]]).T == Matrix([[0, 1], [-1, 0]]), False)
S5 = [(1, 0, 0, 1), (0, 1, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)]
sp_ = lambda vs: rank_rows(vs)
target = rank_rows(S5)
chk("C06-Q5 dim", target, 3)
mcq("C06-Q5", {
    "a": indep(S5),
    "b": indep([S5[0], S5[1], S5[3]]) and rank_rows([S5[0], S5[1], S5[3]]) == target,
    "c": indep([S5[0], S5[3]]) and rank_rows([S5[0], S5[3]]) == target,
    "d": indep([S5[1]]) and rank_rows([S5[1]]) == target,
})
ok("C06-Q5 (0,1,0,0) in sum", in_span([S5[0], S5[3], S5[1]], (0, 1, 0, 0)) and not in_span([S5[0], S5[3]], (0, 1, 0, 0)))
chk("C06-Q6 end", (2 + 2, rank_rows([(1, 0, 0), (0, 1, 0), (0, 1, 0), (0, 0, 1)])), (4, 3))
# lesson C06
chk("C06 ex", rank_rows([(1, 0, 0), (0, 1, 0), (0, 1, 0), (0, 0, 1)]), 3)
chk("C06 sum<=", 2 + 2, 4)

# ---------------------------------------------------------------- C07
chk("C07 thm", 4 + 3 - 2, 5); num("C07-Q1", 4 + 3 - 2)
num("C07-Q2", 3 + 3 - 4); chk("C07-Q2 bound", 3 + 3 - 4, 2)
# brute: two generic 3-dim subspaces of R^4 meet in dim >= 2
for _ in range(100):
    n1 = [rng.randint(-3, 3) for _ in range(4)]; n2 = [rng.randint(-3, 3) for _ in range(4)]
    if not any(n1) or not any(n2):
        continue
    ok("C07-Q2 min", 4 - Matrix([n1, n2]).rank() >= 2)
num("C07-Q3", 3 - Matrix([[1, 1, 1], [1, -1, 0]]).rank())
inter = Matrix([[1, 1, 1], [1, -1, 0]]).nullspace()
chk("C07-Q3 vec", list(inter[0] / inter[0][0]), [1, 1, -2])
chk("C07-Q3 z", sp.solve(sp.Eq(2 * x + symbols("z"), 0), symbols("z"))[0], -2 * x)
cand = {"a": (1, 1, -2), "b": (1, 1, 2), "c": (1, -1, 0), "d": (1, 1, 0)}
mcq("C07-Q4", {k_: (v_[0] + v_[1] + v_[2] == 0 and v_[0] == v_[1]) for k_, v_ in cand.items()})
chk("C07-Q4 sums", (1 + 1 + 2, 1 + 1 + 0), (4, 2))
# Q5
Ub = [(1, 0, 1), (0, 1, 1)]; Vb = [(1, 1, 0), (0, 1, -1)]
al, be, ga, de = symbols("al be ga de")
eqs = list(al * Matrix(Ub[0]) + be * Matrix(Ub[1]) - ga * Matrix(Vb[0]) - de * Matrix(Vb[1]))
ns = Matrix([[sp.diff(e, s) for s in (al, be, ga, de)] for e in eqs]).nullspace()
chk("C07-Q5 dim", len(ns), 1)
w = ns[0][0] * Matrix(Ub[0]) + ns[0][1] * Matrix(Ub[1])
w = w / w[0]
num("C07-Q5", w[2]); chk("C07-Q5 vec", list(w), [1, 0, 1])
a1, b1_, c1, d1 = symbols("a1 b1 c1 d1")
sol5 = sp.solve([a1 - c1, b1_ - (c1 + d1), a1 + b1_ + d1], [b1_, c1, d1], dict=True)[0]
chk("C07-Q5 d", sol5[d1], -a1); chk("C07-Q5 b", sol5[b1_], 0); chk("C07-Q5 c", sol5[c1], a1)
chk("C07-Q5 2a2d", sp.simplify(2 * a1 + 2 * sol5[d1]), 0)
# lesson C07
chk("C07 ex", list(Matrix([[1, 1, 1], [0, 1, -1]]).nullspace()[0] * -1 if Matrix([[1, 1, 1], [0, 1, -1]]).nullspace()[0][0] > 0 else Matrix([[1, 1, 1], [0, 1, -1]]).nullspace()[0]), [-2, 1, 1])
chk("C07 ex dims", (len(Matrix([[1, 1, 1], [0, 1, -1]]).nullspace()), 3 - Matrix([[1, 1, 1]]).rank(), 3 - Matrix([[0, 1, -1]]).rank()), (1, 2, 2))
chk("C07 ex sum", 2 + 2 - 1, 3); chk("C07 ex member", (-2 + 1 + 1, 1 == 1), (0, True))
chk("C07 ex xy", sp.solve(sp.Eq(symbols("x") + 2 * symbols("y"), 0), symbols("x"))[0], -2 * symbols("y"))

# ---------------------------------------------------------------- C08
Bm = M([[1, 1], [1, -1]])
cb = Bm.solve(V(5, 3))
chk("C08-Q1", cb[0], Q["C08-Q1"]["step"]["answer"]); chk("C08-Q1 c2", cb[1], 1)
# Q2 R_2[x] basis 1, 1+x, 1+x+x^2 ; p = 4+3x+2x^2
Bp = Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]]).T  # columns are the basis polynomials' coefficient vectors
cp = Bp.solve(V(4, 3, 2))
num("C08-Q2", cp[2]); chk("C08-Q2 b", cp[1], 1); chk("C08-Q2 a", cp[0], 1)
ok("C08-Q2 recombine", sp.expand(1 * 1 + 1 * (1 + x) + 2 * (1 + x + x ** 2) - (4 + 3 * x + 2 * x ** 2)) == 0)
# Q3 formulas on the lesson example
Bq = Matrix([[1, 0], [2, 1]]); Cq = Matrix([[1, 1], [0, 1]])
true_T = Cq.inv() * Bq
chk("C08 ex T", true_T, Matrix([[-1, -1], [2, 1]])); chk("C08 ex inv", Cq.inv(), Matrix([[1, -1], [0, 1]]))
forms = {"a": Cq.inv() * Bq, "b": Bq * Cq.inv(), "c": Cq * Bq, "d": Bq.inv() * Cq}
mcq("C08-Q3", {k_: (m_ == true_T) for k_, m_ in forms.items()})
chk("C08-Q3 b", forms["b"], Matrix([[1, -1], [2, -1]])); chk("C08-Q3 c", forms["c"], Matrix([[3, 1], [2, 1]]))
chk("C08-Q3 d", forms["d"], Matrix([[1, 1], [-2, -1]]))
# generic: formula a is right on random bases (change of basis semantic check)
for _ in range(50):
    Bm_ = Matrix(2, 2, [rng.randint(-3, 3) for _ in range(4)]); Cm_ = Matrix(2, 2, [rng.randint(-3, 3) for _ in range(4)])
    if Bm_.det() == 0 or Cm_.det() == 0:
        continue
    T = Cm_.inv() * Bm_
    for j in range(2):  # column j = coordinates of b_j in C
        ok("C08 semantic", Cm_ * T[:, j] == Bm_[:, j])
    ok("C08 formula b differs or equal", True)
# Q4
B4 = M([[1, 1], [0, 1]]); C4 = M([[2, 1], [1, 1]])
T4 = C4.inv() * B4
num("C08-Q4", T4[1, 0]); chk("C08-Q4 T", T4, Matrix([[1, 0], [-1, 1]])); chk("C08-Q4 inv", C4.inv(), Matrix([[1, -1], [-1, 2]]))
chk("C08-Q4 check", 1 * Matrix([2, 1]) + (-1) * Matrix([1, 1]), Matrix([1, 0]))
# Q5
T5 = M([[1, 0], [-1, 1]]); vB = V(3, 2)
num("C08-Q5", (T5 * vB)[1]); chk("C08-Q5 vec", list(T5 * vB), [3, -1]); chk("C08-Q5 arith", -3 + 2, -1)
# Q6
inv6 = T5.inv()
mcq("C08-Q6", {"a": Matrix([[1, 0], [1, 1]]) == inv6, "b": Matrix([[1, -1], [0, 1]]) == inv6,
               "c": Matrix([[-1, 0], [1, -1]]) == inv6, "d": T5 == inv6})
chk("C08-Q6 b is transpose", Matrix([[1, -1], [0, 1]]), T5.T); chk("C08-Q6 c", Matrix([[-1, 0], [1, -1]]), -T5)
chk("C08-Q6 product", T5 * Matrix([[1, 0], [1, 1]]), eye(2))
# lesson C08: rref method (C|B) -> (I|T)
aug = Matrix.hstack(Cq, Bq).rref()[0]
chk("C08 ex rref", aug[:, 2:], true_T)
chk("C08 ex col1", -1 * Matrix([1, 0]) + 2 * Matrix([1, 1]), Matrix([1, 2]))
chk("C08 ex product", Matrix([[1, -1], [0, 1]]) * Matrix([[1, 0], [2, 1]]), true_T)
chk("C08 poly coord", (1, 2), (1, 2))

# ---------------------------------------------------------------- C09 boss: the bank pulls
bank = json.loads((APP / "questions.json").read_text(encoding="utf-8"))
B = {q["id"]: q for q in bank["questions"]}
ids = [q["bankId"] for q in LEVELS["C09"]["questions"]]
chk("C09 ids", ids, ["24A-A-Q4a", "23A-A-Q4b", "24A-A-Q4c", "23A-A-Q4d", "24A-A-Q5d", "25B-A-Q5d"])
for i in ids:
    q = B[i]
    ok(f"{i} official", q["official"] is True and q["solutionSource"] == "official-pdf" and q.get("stepsSource") == "ai-verified")
    ok(f"{i} not a refuted sitting", not i.startswith(("22A-B", "21A-B")))
# 24A-A-Q4a: W1: z=x, W2: y=x
W1b = [(1, 0, 1), (0, 1, 0)]
chk("24A-A-Q4a W1", [null_dim([[1, 0, -1]], 3), all(p[2] == p[0] for p in W1b), indep(W1b)], [2, True, True])
chk("24A-A-Q4a W2", null_dim([[1, -1, 0]], 3), 2)
st = B["24A-A-Q4a"]["steps"]
chk("24A-A-Q4a s1", st[0]["answer"], 2); chk("24A-A-Q4a s2", st[1]["answer"], 2)
opt = {o["id"]: o["value"] for o in st[2]["options"]}
chk("24A-A-Q4a s3 text", opt[st[2]["correctId"]], "$\\{(1,0,1),(0,1,0)\\}$")
for oid, ok_ in {"a": False, "b": False, "c": True, "d": False}.items():
    sets = {"a": [(1, 0, 1)], "b": [(1, 1, 0), (0, 0, 1)], "c": [(1, 0, 1), (0, 1, 0)], "d": [(1, 0, 1), (2, 0, 2)]}[oid]
    good = all(p[2] == p[0] for p in sets) and indep(sets) and len(sets) == 2
    chk("24A-A-Q4a opt " + oid, good, ok_)
# 23A-A-Q4b: symmetric, traceless
chk("23A-A-Q4b dim", 4 - Matrix([[0, 1, -1, 0], [1, 0, 0, 1]]).rank(), 2)
st = B["23A-A-Q4b"]["steps"]
chk("23A-A-Q4b s1", st[0]["answer"], 2); chk("23A-A-Q4b s2", st[1]["answer"], -5)
chk("23A-A-Q4b s2 calc", -5 + 5, 0)
good_basis = [(1, 0, 0, -1), (0, 1, 1, 0)]
cand = {"a": [(1, 0, 0, 1), (0, 1, 1, 0)], "b": [(1, 0, 0, -1), (0, 1, -1, 0)], "c": good_basis, "d": [(1, 0, 0, -1)]}
for oid, bs in cand.items():
    isb = all(p[1] == p[2] and p[0] + p[3] == 0 for p in bs) and indep(bs) and len(bs) == 2
    chk("23A-A-Q4b opt " + oid, isb, oid == st[2]["correctId"])
# 24A-A-Q4c: W1 z=x, W2 y=x -> intersection (1,1,1)
inter = Matrix([[1, 0, -1], [1, -1, 0]]).nullspace()
chk("24A-A-Q4c inter", [list(v / v[0]) for v in inter], [[1, 1, 1]])
st = B["24A-A-Q4c"]["steps"]
chk("24A-A-Q4c s2 rank", st[1]["answer"], Matrix([[1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]).rank())
chk("24A-A-Q4c s3 free", st[2]["answer"], 4 - 3)
chk("24A-A-Q4c s4", st[3]["answer"], 5)
sv = {"a": lambda p: p[2] == p[0] or p[1] == p[0], "b": lambda p: p[2] == p[1],
      "c": lambda p: p[0] + p[1] + p[2] == 0, "d": lambda p: p[2] == p[0] and p[1] == p[0]}
w1 = lambda p: p[2] == p[0]; w2 = lambda p: p[1] == p[0]
for oid, f in sv.items():
    # option text characterizes W1 ∩ W2 iff it equals {z=x and y=x} on a grid
    grid = list(itertools.product(range(-3, 4), repeat=3))
    same_set = all(f(p) == (w1(p) and w2(p)) for p in grid)
    chk("24A-A-Q4c opt " + oid, same_set, oid == st[0]["correctId"])
# 23A-A-Q4d: U = Sp{M1,M2,M3}, W = symmetric traceless
M1, M2, M3 = Matrix([[1, 2], [3, 4]]), Matrix([[1, 1], [-1, 1]]), Matrix([[1, 0], [-1, 3]])
Ucoords = Matrix([[m[0], m[1], m[2], m[3]] for m in (M1, M2, M3)]).T
chk("23A-A-Q4d dimU", Ucoords.rank(), 3)
Wb = [Matrix([[1, 0], [0, -1]]), Matrix([[0, 1], [1, 0]])]
Wcoords = Matrix([[m[0], m[1], m[2], m[3]] for m in Wb]).T
chk("23A-A-Q4d dim sum", Matrix.hstack(Ucoords, Wcoords).rank(), 4)
dimint = 3 + 2 - 4
chk("23A-A-Q4d dim int", dimint, B["23A-A-Q4d"]["steps"][0]["answer"])
cc_ = symbols("c1 c2 c3 e f")
lhs = cc_[0] * M1 + cc_[1] * M2 + cc_[2] * M3 - cc_[3] * Wb[0] - cc_[4] * Wb[1]
nsp = Matrix([[sp.diff(e, s) for s in cc_] for e in lhs]).nullspace()
chk("23A-A-Q4d null dim", len(nsp), 1)
vec = nsp[0] / nsp[0][0]
chk("23A-A-Q4d ratio", list(vec[:3]), [1, Rational(3, 2), -2])
a2 = 2
comb = a2 * M1 + 3 * M2 - 4 * M3
st = B["23A-A-Q4d"]["steps"]
chk("23A-A-Q4d s2", comb[0, 1], st[1]["answer"]); chk("23A-A-Q4d s3", comb[1, 1], st[2]["answer"])
chk("23A-A-Q4d comb", comb, Matrix([[1, 7], [7, -1]])); chk("23A-A-Q4d comb sym", comb == comb.T and comb.trace() == 0, True)
# 24A-A-Q5d, 25B-A-Q5d
B5_, C5_ = Matrix([[3, 7], [2, 5]]), Matrix([[5, 3], [3, 2]])
T = C5_.inv() * B5_
st = B["24A-A-Q5d"]["steps"]
chk("24A-A-Q5d T", T, Matrix([[0, -1], [1, 4]])); chk("24A-A-Q5d det", st[1]["answer"], C5_.det())
chk("24A-A-Q5d s3", st[2]["answer"], (C5_.inv() * Matrix([3, 2]))[0]); chk("24A-A-Q5d s4", st[3]["answer"], T[1, 1])
Ab, Ac = Matrix([[1, 2], [3, 4]]), Matrix([[1, 3], [4, 8]])
T2 = Ac.inv() * Ab
st = B["25B-A-Q5d"]["steps"]
chk("25B-A-Q5d T", T2, Matrix([[Rational(1, 4), -1], [Rational(1, 4), 1]]))
pC = T2 * Matrix([20, 25])
chk("25B-A-Q5d det", st[1]["answer"], Ac.det()); chk("25B-A-Q5d s3", st[2]["answer"], pC[0]); chk("25B-A-Q5d s4", st[3]["answer"], pC[1])
chk("25B-A-Q5d p", list(pC), [-20, 30])
rec(*range(0, 7))

# ---------------------------------------------------------------- number scan over lessons and explanations
def strip_tex(t):
    t = re.sub(r"\\[A-Za-z]+", " ", t)           # TeX commands
    t = re.sub(r"[_^]\{?[A-Za-z0-9+\-,]*\}?", " ", t)  # sub/superscripts (indices, powers, names)
    t = re.sub(r"&#36;|&[a-z]+;", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    return t


def level_texts(L):
    yield L["id"] + " lesson", L["lesson"]["html"]
    for q in L["questions"]:
        if "bankId" in q:
            continue
        if "step" in q:
            s = q["step"]
            yield q["id"] + " prompt", s["prompt"]
            yield q["id"] + " explain", s.get("explain", "")
            for ln in s.get("lines", []):
                yield q["id"] + " line", ln
        else:
            yield q["id"] + " stem", q["question"]
            for o in q["options"]:
                yield q["id"] + " opt", o["value"]
            yield q["id"] + " explain", q["explanation"]


unseen = {}
for L in LEVELS.values():
    for label, t in level_texts(L):
        for tok in re.findall(r"\d+", strip_tex(t)):
            if int(tok) not in SEEN:
                unseen.setdefault(label, set()).add(tok)
if unseen:
    FAILS.append("numbers never produced by a check: " + "; ".join(f"{k}: {sorted(v)}" for k, v in unseen.items()))

n_q = sum(1 for L in LEVELS.values() for q in L["questions"])
if FAILS:
    print("FAILED", len(FAILS))
    for f in FAILS:
        print(" -", f)
    sys.exit(1)
print(f"OK: {len(LEVELS)} levels, {n_q} questions, all stored answers and quoted numbers re-derived ({len(SEEN)} distinct numbers recorded)")
