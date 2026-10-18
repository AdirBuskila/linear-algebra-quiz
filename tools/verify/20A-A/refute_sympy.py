from sympy import *
k,a,x,y,z=symbols('k a x y z')
n1=Matrix([1,-2,1]); n2=Matrix([k,-1,k])
print("1a parallel k:",solve(n1.cross(n2),k), "perp k:",solve(n1.dot(n2),k))
# parallel: k=1/2? check
for kk in solve(n1.cross(n2),k):
    # planes x-2y+z+5=0 and kk x - y + kk z -2 =0 -> scale
    s=1/(-2/(-1)) if False else None
    m=Matrix([kk,-1,kk]); lam=-2/(-1) # n1 = lam*? 
    print("n2",m.T)
    # distance: point on pi2 -> pi1
    P=Matrix([0,2*(-1)*(-1)*0+(-2)/(1)*(-1)*0,0])
    # pi2: kk x - y + kk z = 2 -> y=-2 at x=z=0
    P=Matrix([0,-2,0]); print("dist", simplify(abs(n1.dot(P)+5)/n1.norm()))
n2b=Matrix([2,-1,2]); c=n1.cross(n2b); print("1c normal",c.T, "plane:",c.dot(Matrix([x,y,z])-Matrix([1,1,1])))
print("1d roots z^5=5+3i: r=",(34)**Rational(1,10), "arg", atan(Rational(3,5)))
A=Matrix([[1,0,1,1],[1,1,2,0],[0,1,1,-1]])
print("2a null",A.nullspace(),"2b rows",A.rref()[0],"2c cols pivots",A.rref()[1],[A[:,i].T for i in A.rref()[1]])
A3=Matrix([[2,1,-1],[1,a,1],[3,1,-a]]); print("3a det",factor(A3.det()),solve(A3.det(),a))
print("3b inv a=1", A3.subs(a,1).inv())
B=Matrix([[1,1,-1],[1,1,1],[1,1,1]]); print("3c",B.eigenvects()); print("3d",B.is_diagonalizable())
vs=[Matrix(v) for v in [(1,2,3),(2,3,1),(3,1,2),(1,1,1)]]
W1=Matrix.hstack(*vs); print("4a W1 rank",W1.rank(), W1.columnspace(), "W1 eq", )
# W2: x-y=z+y -> x-2y-z=0
W2m=Matrix([[1,-2,-1]]); print("W2 basis",W2m.nullspace())
W2b=W2m.nullspace()
S=Matrix.hstack(W1.columnspace()[0],W1.columnspace()[1],W1.columnspace()[2],*W2b); print("4b W1+W2 rank",S.rank())
# W1 is span of 3 indep? if rank 3 =R^3
print("W1 rank",W1.rank())
# intersection: W1 vs W2 
if W1.rank()==3:
    print("W1=R3, cap=W2")
print("4d (3,1,-1) in W2:", 3-2*1-(-1))
T=Matrix([[1,-1,0],[-2,2,0],[0,0,2]]); print("5b ker",T.nullspace(),"im",T.columnspace(),"rank",T.rank())
B1=Matrix([[1,0,0],[1,1,0],[1,1,1]]); B2=Matrix([[1,0,1],[0,1,1],[0,1,0]])
print("5d",B2.inv()*T*B1)
