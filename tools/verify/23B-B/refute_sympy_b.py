from sympy import *
A=Matrix([[1,6,0],[0,1,2],[5,30,3]])
E1=Matrix([[1,0,0],[0,1,0],[-5,0,1]]);E2=diag(1,1,Rational(1,3));E3=Matrix([[1,0,0],[0,1,-2],[0,0,1]]);E4=Matrix([[1,-6,0],[0,1,0],[0,0,1]])
print(E4*E3*E2*E1==A.inv())
B=Matrix([[1,2,1],[-3,6,1],[0,0,4]]);P=Matrix([[1,2,1],[1,3,0],[0,0,3]]);D=diag(3,4,4);print(P*D==B*P, P*D)
# 4b rref check
M=Matrix([[1,1,-1,-3,2],[1,0,0,2,-3],[0,1,0,5,0],[0,0,1,0,5]]);print(M.rref())
# 4a options
x=symbols('x')
for p in [x**3+x**2,x**2+x,-3*x**3+2*x**2+5*x,x**3-x,2*x**3-3*x**2+5]: print(p, diff(p,x).subs(x,1), p.subs(x,-1))
# 1c scalar
print([(a**3-5*a-4) for a in [-1]], [(1/4)*((-1)**2-5)])
# 1b scalar
print(Rational(6,8))
# 5d
print(Matrix([[1,1],[10,11]]), Matrix([[1,5],[4,19]]).inv(), Matrix([[1,5],[4,19]]).det())
T=Matrix([[1,1,11],[1,2,12],[1,1,11],[1,1,11]]);print(T*Matrix([-10,-1,1]))
# 1d wrong alternative: A=B=0 P=I ; options order
print(Matrix([[3,2,1,0],[-1,1,-1,1]]).rref())
