from sympy import *
z=symbols('z')
print(solve(z**3+(3*I-4)*z,z), [simplify(s**3+(3*I-4)*s) for s in solve(z**3+(3*I-4)*z,z)])
print(N(3/sqrt(2),6),N(-1/sqrt(2),6),abs(4-3*I), sqrtdenest(sqrt(4-3*I)))
print(simplify(((3-I)/sqrt(2))**2))
