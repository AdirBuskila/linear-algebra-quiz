# -*- coding: utf-8 -*-
"""sympy checks of the solver's 21A-B answers (no official key exists). Run: PYTHONUTF8=1 py tools/verify/21A-B/verify_21A-B.py
Every check is an assertion; ASCII output only."""
import sympy as sp

M, R, I = sp.Matrix, sp.Rational, sp.I
a, b, s, t, lam = sp.symbols("a b s t lam")
n = 0


def chk(name, cond):
    global n
    assert cond, name
    n += 1
    print("OK  " + name)


# Q1a/b: odd-order antisymmetric -> det 0; AB=B forces det B = 0
for size in (3, 5):
    Asym = sp.Matrix(size, size, lambda i, j: 0 if i == j else (sp.Symbol(f"m{min(i,j)}{max(i,j)}") * (1 if i < j else -1)))
    chk(f"Q1a antisymmetric {size}x{size} has det 0", sp.expand(Asym.det()) == 0)
A1 = M([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]])
chk("Q1b model: (A-I)B=0 with A-I invertible forces B=0, singular", A1.T == -A1 and (A1 - sp.eye(3)).det() != 0 and (A1 - sp.eye(3)).nullspace() == [])
C = M([[1, 0, 0], [5, a, 0], [2, a, 1]])
chk("Q1c det C = a", C.det() == a)
C0 = C.subs(a, 0)
chk("Q1c col space basis (1,5,2),(0,0,1), dim 2", C0.rank() == 2 and M.hstack(M([1, 5, 2]), M([0, 0, 1])).rank() == 2 and M.hstack(C0, M([1, 5, 2]), M([0, 0, 1])).rank() == 2)
chk("Q1d completed basis det -1", M.hstack(M([1, 5, 2]), M([0, 0, 1]), M([0, 1, 0])).det() == -1)

# Q2
Aug = M([[2, -1, 1, 3], [1, -1, 1, 2], [3, -1, -a, b]])
E = M([[1, -1, 1, 2], [0, 1, -1, -1], [0, 0, -a - 1, b - 4]])
chk("Q2a echelon is row-equivalent (same rref for a=2,b=1 and a=0,b=7)", all(Aug.subs({a: av, b: bv}).rref()[0] == E.subs({a: av, b: bv}).rref()[0] for av, bv in ((2, 1), (0, 7), (-1, 4), (-1, 0))))
S = Aug.copy(); S.row_swap(0, 1); S[1, :] -= 2 * S[0, :]; S[2, :] -= 3 * S[0, :]; S[2, :] -= 2 * S[1, :]
chk("Q2a exact row ops give E", sp.expand(S - E) == sp.zeros(3, 4))
def cls(av, bv):
    m = Aug.subs({a: av, b: bv}); r, ra = m[:, :3].rank(), m.rank()
    return "none" if r != ra else ("unique" if r == 3 else "inf")
chk("Q2b classification", all(cls(av, bv) == "unique" for av in (0, 2, 5, -2) for bv in (0, 4, 9)) and cls(-1, 4) == "inf" and all(cls(-1, bv) == "none" for bv in (0, 1, 5)))
chk("Q2c a=2,b=1 -> (1,0,1)", Aug.subs({a: 2, b: 1})[:, :3].LUsolve(Aug.subs({a: 2, b: 1})[:, 3]) == M([1, 0, 1]))
fam = M([1, t - 1, t])
chk("Q2d a=-1,b=4 family", sp.expand(Aug.subs({a: -1, b: 4})[:, :3] * fam - Aug.subs({a: -1, b: 4})[:, 3]) == sp.zeros(3, 1))
roots = [0, 4, -2 + 2 * sp.sqrt(3) * I, -2 - 2 * sp.sqrt(3) * I]
chk("Q2e four roots of 4z = conj(z)^2", all(sp.expand(4 * r - sp.conjugate(r) ** 2) == 0 for r in roots) and len(set(roots)) == 4)
xr, yr = sp.symbols("xr yr", real=True)
zz = xr + I * yr
eqs = sp.expand(4 * zz - sp.conjugate(zz) ** 2)
sols = sp.solve([sp.re(eqs), sp.im(eqs)], [xr, yr], dict=True)
chk("Q2e exactly four solutions", len(sols) == 4 and {sp.nsimplify(d[xr] + I * d[yr]) for d in sols} == set(roots))

# Q3a
A = M([[1, 2, 1], [0, 1, 3], [3, 8, 8]])
Ai = M([[16, 8, -5], [-9, -5, 3], [3, 2, -1]])
Es = [M([[1, -2, 0], [0, 1, 0], [0, 0, 1]]), M([[1, 0, -1], [0, 1, 0], [0, 0, 1]]), M([[1, 0, 0], [0, 1, -3], [0, 0, 1]]),
      M([[1, 0, 0], [0, 1, 0], [0, 0, -1]]), M([[1, 0, 0], [0, 1, 0], [0, -2, 1]]), M([[1, 0, 0], [0, 1, 0], [-3, 0, 1]])]
prod = sp.eye(3)
for e in Es:
    prod = prod * e
chk("Q3a A^-1 and product of six elementary matrices", A.inv() == Ai and prod == Ai)
# Q3b/c
B = M([[5, 0, 1], [0, 4, 0], [1, 0, 5]])
chk("Q3b char poly (l-4)^2(l-6)", sp.expand((lam * sp.eye(3) - B).det() - (lam - 4) ** 2 * (lam - 6)) == 0)
chk("Q3b eigvecs", B * M([0, 1, 0]) == 4 * M([0, 1, 0]) and B * M([-1, 0, 1]) == 4 * M([-1, 0, 1]) and B * M([1, 0, 1]) == 6 * M([1, 0, 1]) and (B - 4 * sp.eye(3)).rank() == 1 and (B - 6 * sp.eye(3)).rank() == 2)
P = M([[0, -1, 1], [1, 0, 0], [0, 1, 1]]); D = sp.diag(4, 4, 6)
chk("Q3c P^-1BP = D, |P|=2, BP shown", P.det() == 2 and P.inv() * B * P == D and B * P == M([[0, -4, 6], [4, 0, 0], [0, 4, 6]]))

# Q4
Vs = M([[0, 1, 1], [1, 2, 3], [1, 1, 2], [1, 3, 4]])
chk("Q4a dim V = 2, basis (1,1,2),(0,1,1)", Vs.rank() == 2 and M([[1, 1, 2], [0, 1, 1]]).col_join(Vs).rank() == 2)
chk("Q4a relations (1,2,3)=(1,1,2)+(0,1,1), (1,3,4)=(1,1,2)+2(0,1,1)", M([1, 2, 3]) == M([1, 1, 2]) + M([0, 1, 1]) and M([1, 3, 4]) == M([1, 1, 2]) + 2 * M([0, 1, 1]))
Wn = M([[1, -2, -1]])
chk("Q4a W basis (2,1,0),(1,0,1) in W, dim 2", Wn * M([2, 1, 0]) == M([0]) and Wn * M([1, 0, 1]) == M([0]) and len(Wn.nullspace()) == 2)
VW = M([[1, 1, 2], [0, 1, 1], [2, 1, 0], [1, 0, 1]])
chk("Q4b V+W = R^3", VW.rank() == 3)
chk("Q4c V cap W = span(1,0,1)", Wn * M([1, 0, 1]) == M([0]) and M([[1, 1, 2], [0, 1, 1], [1, 0, 1]]).rank() == 2 and 2 + 2 - 3 == 1)
chk("Q4d (1,3,2) not in W (so not in cap); decomposition 7/3(0,1,1)+(1,2/3,-1/3)", (Wn * M([1, 3, 2]))[0] != 0
    and R(7, 3) * M([0, 1, 1]) + M([1, R(2, 3), -R(1, 3)]) == M([1, 3, 2]) and (Wn * M([1, R(2, 3), -R(1, 3)]))[0] == 0)

# Q5
T5 = M([[1, 2, 8, 1], [-3, 2, 0, 5], [1, 1, 5, 0]])
chk("Q5b rref", T5.rref()[0] == M([[1, 0, 2, -1], [0, 1, 3, 1], [0, 0, 0, 0]]))
chk("Q5b kernel basis (-2,-3,1,0),(1,-1,0,1), dim 2", T5 * M([-2, -3, 1, 0]) == sp.zeros(3, 1) and T5 * M([1, -1, 0, 1]) == sp.zeros(3, 1) and len(T5.nullspace()) == 2)
chk("Q5c Im basis cols 1,2, dim 2", T5.rank() == 2 and T5[:, :2].rank() == 2 and T5[:, 0] == M([1, -3, 1]) and T5[:, 1] == M([2, 2, 1]) and T5[:, 2] == M([8, 0, 5]) and T5[:, 3] == M([1, 5, 0]))
chk("Q5d not invertible", T5.rank() < 4)

print(f"ALL {n} CHECKS OK")
