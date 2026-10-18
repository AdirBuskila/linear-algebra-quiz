from sympy import *
import random
# 6a: det H * d^2 = d^3 / det H => d = h^2 >0 ; check numerically with a constructed example
h,d=symbols('h d',nonzero=True)
print(solve(Eq(h*d**2,d**3/h),d))
# 6b: eigenvector check
A=Matrix([[2,1],[1,3]]); 
for val,m,vs in A.eigenvects(): 
    for v in vs: print(simplify(A.inv()*v-v/val))
# 6c counterexamples
B=eye(2); C=-eye(2); print((B+C).det(), (0*C).det(), (B*C).det())
