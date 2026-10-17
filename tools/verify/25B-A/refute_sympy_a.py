from sympy import *
x,y,z,a,m=symbols('x y z a m')
# Q1
n1=Matrix([1,1,1]);n2=Matrix([2,-1,2]);n3=Matrix([1,-1,2])
for n,c in((n2,1),(n3,-1)):
    s=solve([x+y+z,n[0]*x+n[1]*y+n[2]*z-c],[x,y],dict=True);print('line',s, 'dir',n1.cross(n))
# S4 contains l1 perp S1: normal = d1 x n1
d1=n1.cross(n2);d2=n1.cross(n3);N4=d1.cross(n1);N5=d2.cross(n1);print('N4',N4.T,'N5',N5.T)
# point on l1: z=0 -> x+y=0,2x-y=1 -> x=1/3,y=-1/3
p1=Matrix([Rational(1,3),Rational(-1,3),0]);print('S4 rhs',N4.dot(p1))
# l2: z=0: x+y=0, x-y=-1 -> x=-1/2,y=1/2
p2=Matrix([Rational(-1,2),Rational(1,2),0]);print('S5 rhs',N5.dot(p2))
print('l1 cap l2',solve([x+y+z,2*x-y+2*z-1,x-y+2*z+1],[x,y,z]))
print('S4 cap S5',solve([N4.dot(Matrix([x,y,z]))-N4.dot(p1),N5.dot(Matrix([x,y,z]))-N5.dot(p2)],[x,y],dict=True),N4.cross(N5).T)
# Q2
M=Matrix([[1,-1,2,0],[-1,a,a-3,a],[0,a-1,2*a,2*a+1],[1,a-2,2*a+2,2*a+1]])
print(M.rref(simplify=True)); 
A=M[:,:3]
print('det-ish minors', factor(A[:3,:].det()), factor(A[1:,:].det()),factor(M[:3,[0,1,3]].det()))
for av in [1,0,-1,2,3,Rational(1,2),-2]:
    Mv=M.subs(a,av);print(av,'rankA',Mv[:,:3].rank(),'rankM',Mv.rank())
print(solve(list(M.subs(a,-1)*Matrix([x,y,z,-1])),[x,y,z]) if False else linsolve((M.subs(a,-1)[:,:3],M.subs(a,-1)[:,3]),x,y,z))
# 2d
zz=symbols('zz')
w=symbols('w')
sol=solve((w+(7-I)/(3+I))**3-8*I,w);print('w',sol,'z',[conjugate(s) for s in sol],simplify((7-I)/(3+I)))
# Q3
A3=Matrix([[1,-1,0],[0,1,1],[5,-5,9]]);print(A3.det(),A3.inv())
B=Matrix([[7,0,1],[0,6,0],[1,0,7]]);P,D=B.diagonalize();print(P,D, P*D==B*P)
# Q4
sym=Matrix([[1,0,0,0]]);
# W basis E11, E12+E21, E22
U=Matrix([[1,2,-1,3],[2,0,-3,2]]).T
Wb=Matrix([[1,0,0,0],[0,1,1,0],[0,0,0,1]]).T
print('dim U',U.rank(),'dim U+W',U.row_join(Wb).rank(),'dim cap',2+3-U.row_join(Wb).rank())
s,t=symbols('s t')
v=s*U[:,0]+t*U[:,1];print(solve(v[1]-v[2],[s,t],dict=True), v.T)
sol=solve(v[1]-v[2],[s,t],dict=True)[0] if True else 0
print('cap',(v.subs(sol)).T)
vec=Matrix([1,0,-1,1]);print('in U?',U.row_join(vec).rank(),U.rank())
# Q5
T=Matrix([[1,1,1,1],[2,0,2,5],[3,1,3,6],[6,2,6,12]]);print(T.rank(),T.nullspace(),T.columnspace())
print(Matrix.hstack(T,Matrix([11,2,13,m])).rank(), )
Tm=T.row_join(Matrix([11,2,13,m]));print(Tm.rref(), solve(Tm.det() if False else 0,m) if False else '')
cs=T.columnspace(); 
for mv in range(-30,60):
    if T.row_join(Matrix([11,2,13,mv])).rank()==T.rank(): print('m=',mv)
# 5d
Bb=Matrix([[1,2],[3,4]]);Cb=Matrix([[1,3],[4,8]]);print((Cb.inv()*Bb*Matrix([20,25])).T)
