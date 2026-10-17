from sympy import *
k,x,y,z=symbols('k x y z')
M=Matrix([[1,0,-3,-3],[2,k,-1,-2],[1,2,k,1]])
print(factor(M[:,:3].det()))
print(solve(list(M[:,:3]*Matrix([x,y,z])-M[:,3]),[x,y,z],dict=True))
for kv in [-2,Rational(3,1),0,1,5,Rational(-1,2),2,4,-3,6, -1]:
    Mv=M.subs(k,kv);print(kv,Mv[:,:3].rank(),Mv.rank())
print(M.rref())
for kv in [-2,3]:
    print(kv,linsolve((M.subs(k,kv)[:,:3],M.subs(k,kv)[:,3]),x,y,z))
# elimination form
R=M.copy();R[1,:]=R[1,:]-2*R[0,:];R[2,:]=R[2,:]-R[0,:];print(R)
# 3
A=Matrix([[1,-1,1],[0,1,1],[-1,1,1]]);print(A.det(),A.inv())
B=Matrix([[1,1,0],[0,-2,0],[-1,0,3]]);print(B.eigenvals(),B.is_diagonalizable())
P,D=B.diagonalize();print(P,D,P*D==B*P)
print(B.eigenvects())
# 4
W1=[Matrix([1,0,1]),Matrix([0,1,0])];W2=[Matrix([1,1,0]),Matrix([0,0,1])]
S=Matrix.hstack(*W1,*W2);print(S.rank(),S.columnspace())
# cap: z=x,y=x -> (1,1,1)
print('cap vec',Matrix([1,1,1]))
# 5
T=Matrix([[1,1,2,2],[2,3,2,3],[3,4,4,5],[4,5,6,7]]);print(T.rank(),T.rref(),T.nullspace(),T.columnspace())
kk,mm=symbols('kk mm')
print(solve(list(T*Matrix([-7,3,kk,mm])),[kk,mm]))
Bm=Matrix([[3,7],[2,5]]);Cm=Matrix([[5,3],[3,2]]);print(Cm.inv()*Bm,Cm.inv(),Bm.inv()*Cm,Bm*Cm.inv(),Cm*Bm)
