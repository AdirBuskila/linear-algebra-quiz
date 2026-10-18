from sympy import *
# 1c/d: A real, AA^T=A^2=3/2 I => A symmetric; both signs of det attained by +-sqrt(3/2) I
s=sqrt(Rational(3,2)); 
for sg in (1,-1):
    A=sg*s*eye(3); assert A*A.T==A*A==Rational(3,2)*eye(3); print("det",simplify(A.det()),"det inv",simplify(A.inv().det()))
print(nsimplify(sqrt(Rational(27,8))), simplify(sqrt(Rational(8,27))), simplify(2*sqrt(6)/9-sqrt(Rational(8,27))))
# a symmetric non-scalar example with mixed signs: det positive/negative both fine
a=symbols('a'); x,y,z=symbols('x y z')
M=Matrix([[1,-1,-a,a],[a,1,-1,-a],[1,a,1,-1]]).subs(a,-1); print("2c rref",M.rref())
print(linsolve((M[:,:3],M[:,3]),x,y,z))
