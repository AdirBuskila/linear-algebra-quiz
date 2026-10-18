from sympy import *
k=symbols('k')
for v in [(-1,3,-2),(-1,1,-2),(1,-3,2)]:
    print(v, Matrix([v,[1,k,2],[2,1,1]]).det().expand(), solve(Matrix([v,[1,k,2],[2,1,1]]).det(),k), Matrix([v,[1,2,2],[2,1,1]]).det())
print(Matrix([[-1,3,-2],[1,-4,2],[2,1,1]]).det())
