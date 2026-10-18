from sympy import *
C=Matrix([[0,1,2],[-1,0,3],[-2,-3,0]]); D=Matrix([[0,1,1],[-1,0,1],[-1,-1,0]])
print(C*D, (C*D).det(), C.det(), D.det(), C.T==-C, D.T==-D)
E1=Matrix([[1,0,0],[0,1,0],[-1,0,1]]);E2=Matrix([[1,0,0],[0,1,-1],[0,0,1]]);E3=Matrix([[1,-1,0],[0,1,0],[0,0,1]]);E4=diag(1,Rational(1,3),1)
A=Matrix([[1,3,0],[0,3,1],[1,3,1]]); print(E4*E3*E2*E1==A.inv(), E4*E3*E2*E1*A)
# wrong-order check
print(E1*E2*E3*E4==A.inv())
# 22A-A 4: pitfall/ steps
# 2e findbug
w=exp(2*pi*I/3); print(simplify(w*w**2), N(w))
# 4a sanity of options
for v in [(1,1,0),(0,1,1),(1,2,1),(1,0,1)]: print(v, v[0]+2*v[1]-v[2])
for v in [(1,1,3),(1,0,1),(1,0,2),(1,1,1)]: print(v, v[0]+2*v[1]-v[2], 2*v[0]+v[1]-v[2])
B=Matrix([[1,1,0],[0,-2,0],[-1,0,3]]); P=Matrix([[2,5,0],[0,-15,0],[1,1,1]]); print(P.inv()*B*P, (B*P)[0,1])
