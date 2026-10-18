from sympy import *
A=Matrix([[1,2,0],[0,1,1],[2,4,2]])
M1=Matrix([[1,-2,0],[0,1,0],[0,0,1]]);M2=Matrix([[1,0,0],[0,1,-1],[0,0,1]]);M3=diag(1,1,Rational(1,2));M4=Matrix([[1,0,0],[0,1,0],[-2,0,1]])
print(M1*M2*M3*M4==A.inv(), (M1*M2*M3*M4).det(), (M1*M2*M3*M4)[0,0])
B=Matrix([[2,1,1],[1,2,1],[0,0,1]]);P=Matrix([[-1,-1,1],[1,0,1],[0,1,0]]);print(P.inv()*B*P,(B*P)[0,2])
# Q1: all A symmetric with AA^T=A^2=5/2 I
a=sqrt(Rational(5,2)); print(diag(a,a,a,-a)*diag(a,a,a,-a).T, diag(a,a,a,-a).det(), diag(a,a,a,a).det())
print(N(1/a), N(Rational(1,5)*2*a), N(2**Rational(1,3)*sqrt(3)/2), N(2**Rational(1,3)))
# 2c sol check
M=Matrix([[1,1,3],[3,4,2],[2,3,-1]]); b=Matrix([2,3,1]); print(M*Matrix([5,-3,0])-b, M*Matrix([-10,7,1]))
# 4 steps: (2,-1,0) in W2
print(2+2*(-1)-0)
Wm=Matrix([[1,2,-1],[2,1,-1]]) # none
# 4c internal: 2t v3 + t v4
print(2*Matrix([-2,1,0])+Matrix([3,0,1]))
# 3 options 4a 
for v in [(1,1,0),(3,0,1),(2,1,0),(0,1,1)]: print(v,v[0]+2*v[1]-3*v[2])
