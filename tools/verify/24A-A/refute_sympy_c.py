from sympy import *
A=Matrix([[1,-1,1],[0,1,1],[-1,1,1]])
E1=Matrix([[1,0,0],[0,1,0],[1,0,1]]);E2=Matrix([[1,1,0],[0,1,0],[0,0,1]]);E3=diag(1,1,Rational(1,2));E4=Matrix([[1,0,0],[0,1,-1],[0,0,1]]);E5=Matrix([[1,0,-2],[0,1,0],[0,0,1]])
Ai=A.inv()
print(E5*E4*E3*E2*E1==Ai, E1*E2*E3*E4*E5==Ai, E1*E2*E3*E4*E5*A==Ai, E1.inv()*E2.inv()*E3.inv()*E4.inv()*E5.inv()==Ai, E1.inv()*E2.inv()*E3.inv()*E4.inv()*E5.inv()==A)
print(E1*A,E2*E1*A,E3*E2*E1*A,E4*E3*E2*E1*A,E5*E4*E3*E2*E1*A)
a=Matrix([[0,-1],[1,-1]]);print(a**2+a+eye(2),(a**2).T, (a**2-a+eye(2))==-2*a,(a**2-a+eye(2)).det())
B=Matrix([[1,1,0],[0,-2,0],[-1,0,3]]);print(B*Matrix([2,0,1]),B.det(),B.trace())
