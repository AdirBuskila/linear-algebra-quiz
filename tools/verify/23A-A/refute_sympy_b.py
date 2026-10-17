from sympy import *
A=Matrix([[1,5,1],[2,11,0],[0,0,1]])
E1=Matrix([[1,0,0],[-2,1,0],[0,0,1]]);E2=Matrix([[1,0,0],[0,1,2],[0,0,1]]);E3=Matrix([[1,0,-1],[0,1,0],[0,0,1]]);E4=Matrix([[1,-5,0],[0,1,0],[0,0,1]])
Ai=A.inv()
print(E4*E3*E2*E1==Ai,E1*E2*E3*E4==Ai,E1*E2*E3*E4*A==Ai,E1.inv()*E2.inv()*E3.inv()*E4.inv()==Ai,E1.inv()*E2.inv()*E3.inv()*E4.inv()==A)
w=sqrt(7-32*I);z1=((4-3*I)+w)/2;z2=((4-3*I)-w)/2
print(N(z1,6),N(z2,6),N(sqrt(7-32*I),6))
zz=symbols('zz');print([N(simplify(zz**2+(3*I-4)*zz+2*I).subs(zz,s)) for s in (z1,z2)])
C5=Matrix([[34,-55],[-55,89]]);print(C5.inv())
# 1c steps options
C3=Matrix([[5,-8],[-8,13]]);print('C^5 C^-3 = C^2?', C5*C3.inv(), C3.inv()*C5, C5*C3)
