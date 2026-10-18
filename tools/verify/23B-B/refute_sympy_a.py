from sympy import *
a,x,y,z,k,m=symbols('a x y z k m')
M=Matrix([[a,1,1],[1,1,2],[1,-1,a]]); b=Matrix([2,5,a+1])
print(factor(M.det()), [simplify(s) for s in M.LUsolve(b)])
for av in solve(M.det(),a):
    Ms=M.subs(a,av); bb=b.subs(a,av); print(av,Ms.rank(),Ms.row_join(bb).rank(), linsolve((Ms,bb),x,y,z))
print(solve(z**2-(2+I)*z+(-1+7*I),z))
A=Matrix([[1,6,0],[0,1,2],[5,30,3]]); print(A.det(),A.inv())
B=Matrix([[1,2,1],[-3,6,1],[0,0,4]]); print(B.eigenvects()); 
try: print(B.diagonalize())
except Exception as e: print('nodiag',e)
# poly space R3[x]; coords (1,x,x2,x3)
p=symbols('p0:4'); P=sum(p[i]*x**i for i in range(4))
c1=diff(P,x).subs(x,1); c2=P.subs(x,-1)
W1=Matrix([[Poly(c1,*p).coeff_monomial(q) for q in p],[Poly(c2,*p).coeff_monomial(q) for q in p]])
print(W1, W1.nullspace())
# W2: a-b-c+d=0 where a=x^3 coeff=p3,b=p2,c=p1,d=p0
W2=Matrix([[1,-1,-1,1]])  # on (p0,p1,p2,p3): d=p0,c=p1,b=p2,a=p3 -> p3-p2-p1+p0
print(W2.nullspace())
N1=W1.nullspace(); N2=W2.nullspace()
print('sum',Matrix.hstack(*N1,*N2).rank())
cap=W1.col_join(W2).nullspace(); print('cap',cap)
v=Matrix([-10,-10,2,2]); print(W1*v, W2*v)
T=Matrix([[1,1,11],[1,2,12],[1,1,11],[1,1,11]]); print(T.rank(),T.columnspace(),T.nullspace())
print(T*Matrix([m,2023,-2023]), )
print(Matrix.hstack(T,Matrix([101,102,101,k])).rank(), [ (kv,Matrix.hstack(T,Matrix([101,102,101,kv])).rank()) for kv in [100,101,102]])
Bm=Matrix([[1,1],[10,11]]); Cm=Matrix([[1,5],[4,19]])
print('C^-1 B',Cm.inv()*Bm,'B^-1 C',Bm.inv()*Cm)
