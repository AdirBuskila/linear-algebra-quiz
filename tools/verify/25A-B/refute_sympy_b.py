from sympy import *
A=Matrix([[1,1,1],[2,3,2],[3,8,2]])
I3=eye(3)
def E(i,j,c):
    M=eye(3);M[i,j]=c;return M
E1=E(1,0,-2);E2=E(2,0,-3);E3=E(0,1,-1);E4=E(2,1,-5);E5=diag(1,1,-1);E6=E(0,2,-1)
Ainv=A.inv()
print(E6*E5*E4*E3*E2*E1==Ainv)
# documented product
doc=E(0,2,-1)*diag(1,1,-1)*E(0,1,-1)*E(2,1,-5)*E(2,0,-3)*E(1,0,-2);print(doc==Ainv)
import itertools
for n,F in [('E1',E1),('E5',E5),('E4',E4),('E6',E6)]:
    others=[('E6',E6),('E5',E5),('E4',E4),('E3',E3),('E2',E2),('E1',E1)]
    seq=[F]+[M for nn,M in others if M is not F]
    P=eye(3)
    for M in seq:P=P*M
    print(n,'leftmost ->',P==Ainv)
a=symbols('a');M=Matrix([[a,a,-1],[a**2,a,a**2-a],[a,a,2*a+1]]);print((M.row_op if False else 0))
r2=M[1,:]-a*M[0,:];r3=M[2,:]-M[0,:];print(simplify(r2),simplify(r3))
print(expand(a**2-a-(-a)*a))
