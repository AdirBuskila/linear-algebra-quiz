from sympy import *
k,x,y,z,q=symbols('k x y z q')
C5=Matrix([[34,-55],[-55,89]]);C3=Matrix([[5,-8],[-8,13]])
print('detC5',C5.det(),'detC3',C3.det(),'C^2',C3.inv()*C5,'C^-2',C5.inv()*C3, (C3.inv()*C5).inv())
# ensure consistency: exists C with those? C^2 = F ; C = C^3 * C^-2 ... C = C3*(C2)^-1
C2=C3.inv()*C5;C=C3*C2.inv();print('C',C,C**5==C5,C**3==C3)
M=Matrix([[2,k,-1,-2],[1,0,-3,-3],[1,2,k,1]])
print(factor(M[:,:3].det()))
for kv in [2,-5,0,1,3,-3,Rational(1,2)]:
    Mv=M.subs(k,kv);print(kv,Mv[:,:3].rank(),Mv.rank())
for kv in [2,-5]: print(kv,linsolve((M.subs(k,kv)[:,:3],M.subs(k,kv)[:,3]),x,y,z))
print(M.rref())
# 2d
zz=symbols('zz');print(solve(zz**2+(3*I-4)*zz+2*I,zz))
# 3
A=Matrix([[1,5,1],[2,11,0],[0,0,1]]);print(A.det(),A.inv())
B=Matrix([[1,0,0],[-1,6,1],[-1,5,2]]);print(B.eigenvects(),B.is_diagonalizable())
P,D=B.diagonalize();print(P,D,D==P.inv()*B*P)
# 4
Um=[Matrix([1,2,3,4]),Matrix([1,1,-1,1]),Matrix([1,0,-1,3])];US=Matrix.hstack(*Um);print('dimU',US.rank(),US.columnspace(),US.nullspace())
# W: symmetric trace 0: [[a,b],[b,-a]] coords (a,b,b,-a): basis (1,0,0,-1),(0,1,1,0)
Wm=[Matrix([1,0,0,-1]),Matrix([0,1,1,0])];WS=Matrix.hstack(*Wm)
S=Matrix.hstack(US,WS);print('dim sum',S.rank(),'cap',US.rank()+2-S.rank())
print(S.columnspace(), S.nullspace())
# cap
a,b=symbols('a b')
c1,c2=symbols('c1 c2')
# element of U = c1 u1 + c2 u2 ; in W if v[1]==v[2] and v[0]==-v[3]
cc=symbols('cc1:4')
v=sum((cc[i]*Um[i] for i in range(3)),zeros(4,1))
print(solve([v[1]-v[2],v[0]+v[3]],cc,dict=True), )
sol=solve([v[1]-v[2],v[0]+v[3]],cc,dict=True)[0];print(v.subs(sol).T)
# 5
T=Matrix([[1,1,2,2],[1,2,3,-2],[3,4,7,2],[3,5,8,-2]]);print(T.rank(),T.rref(),T.nullspace(),T.columnspace())
for qv in range(-200,200):
    if T.row_join(Matrix([11,12,34,qv])).rank()==T.rank(): print('q',qv)
print(T.row_join(Matrix([11,12,34,q])).rref())
# 5d
Bb=[Matrix([[0,0],[2,0]]),Matrix([[2,0],[0,0]]),Matrix([[0,2],[0,0]]),Matrix([[0,0],[0,2]])]
Cb=Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
cols=[]
for Mx in Bb:
    vec=Matrix([Mx[0,0],Mx[0,1],Mx[1,0],Mx[1,1]]);img=T*vec;cols.append(Cb.inv()*img)
R=Matrix.hstack(*cols);print(R, Cb)
for i,Mx in enumerate(Bb):
    vec=Matrix([Mx[0,0],Mx[0,1],Mx[1,0],Mx[1,1]]);print('T(B%d)'%(i+1),(T*vec).T)
