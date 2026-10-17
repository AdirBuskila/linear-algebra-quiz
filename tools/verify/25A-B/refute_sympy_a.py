from sympy import *
x,y,z,a,k,s,t=symbols('x y z a k s t',real=True)
n1=Matrix([-k**2,-1,k+1]);n2=Matrix([1,k,2*k-3])
print('dot',factor(n1.dot(n2)),solve(n1.dot(n2),k))
kk=-3 if solve(n1.dot(n2),k) else 0
print(solve(n1.dot(n2),k))
for kv in solve(n1.dot(n2),k):
    N1=n1.subs(k,kv);N2=n2.subs(k,kv);print(kv,N1.T,N2.T,N1.cross(N2).T)
    d=N1.cross(N2)
    sol=solve([N1[0]*x+N1[1]*y+N1[2]*z-2,N2[0]*x+N2[1]*y+N2[2]*z-1],[x,y],dict=True);print(sol)
    p0=Matrix([12,-14,5]);print('p0 on S1,S2',N1.dot(p0),N2.dot(p0))
    print('S3 normal planes: direction span N1,N2; S3 eq via d', d.dot(p0))
# Q2
M=Matrix([[a,a,-1],[a**2,a,a**2-a],[a,a,2*a+1]])
print(factor(M.det()))
for av in [0,1,2,-1,Rational(1,2),-Rational(1,2),3]:
    Mv=M.subs(a,av);print(av,Mv.rank(),Mv.nullspace())
# echelon
R=M.row_join(zeros(3,1));print(R.rref(simplify=True))
# 2d: plane: rank 1? 
# Q3
A=Matrix([[1,1,1],[2,3,2],[3,8,2]]);print(A.det(),A.inv())
B=ones(3,3);P,D=B.diagonalize();print(P,D,B*P==P*D,B.eigenvals())
# Q4 R3[x] coords (c0,c1,c2,c3)
W1=Matrix([[1,-1,0,0],[0,0,0,0]]) 
c0,c1,c2,c3=symbols('c0 c1 c2 c3')
print('W1',solve([c0-c1,c1-2*c2],[c0,c1],dict=True))
# W1: c0=c1=2c2 -> p = 2c2(1+x)+c2 x^2 + c3 x^3 : basis (2+2x+x^2), x^3 ; dim 2
w1=[Matrix([2,2,1,0]),Matrix([0,0,0,1])]
w2=[Matrix([1,0,0,0]),Matrix([0,0,1,0]),Matrix([0,0,0,1])]
S=Matrix.hstack(*w1,*w2);print('dim sum',S.rank(), S.columnspace())
print('cap dim',2+3-S.rank())
# intersection: W1 elements with c1=0: c0=c1=0=2c2 -> c2=0 -> c3 x^3
q=Matrix([3,0,2,1]);print('Q in sum?',S.row_join(q).rank())
# Q5
T=Matrix([[1,1,1,1],[1,1,2,2],[2,2,3,3],[3,3,5,5]]);print(T.rref(),T.rank(),T.nullspace(),T.columnspace())
for kv in range(-20,20):
  for mv in range(-30,40):
    if T.row_join(Matrix([4,6,kv,mv])).rank()==2: print('k,m',kv,mv)
kk,mm=symbols('kk mm');print(T.row_join(Matrix([4,6,kk,mm])).rref())
# 5d
Bm=Matrix([[20,25],[20,24]]);Cm=Matrix([[1,3],[3,10]]);print(Cm.inv()*Bm, Bm.inv()*Cm, Cm*Bm.inv(), Bm*Cm.inv())
