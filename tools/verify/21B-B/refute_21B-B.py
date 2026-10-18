from sympy import *
k,x,y,z,t=symbols('k x y z t')
A=Matrix([[0,1,7,8],[1,3,3,8],[-2,-5,1,-8]])
print("rref",A.rref())
# 1b  B^3-5B-4I=0 -> B(B^2-5I)=4I -> B^-1=(B^2-5I)/4
b=symbols('b'); print(factor(b**3-5*b-4))
M=Matrix([[2,2,3-k**2,3-k],[1,k+1,k,1-k],[3,3,-k**2,3-k]])
print("det",factor(M[:,:3].det()))
print("gen",simplify(Matrix(linsolve((M[:,:3],M[:,3]),x,y,z).args[0])))
for v in [0,1,-1,2,3,-3]:
    Mv=M.subs(k,v); print(v,Mv[:,:3].rank(),Mv.rank(),linsolve((Mv[:,:3],Mv[:,3]),x,y,z), Mv.rref()[0].tolist())
zz=symbols('zz'); print(solve(zz**2+I*zz+Rational(1,4)*I,zz), [N(s) for s in solve(zz**2+I*zz+Rational(1,4)*I,zz)])
A3=Matrix([[1,1,1],[k,k**2,1],[k**2,2*k**2-1,1]]); print("detA3",factor(A3.det()))
print("k=1 colspace",A3.subs(k,1).columnspace(), A3.subs(k,1).rank())
B=Matrix([[-2,1,-1],[1,2,3],[1,-1,0]]); print(B.eigenvects(), B.is_diagonalizable(), B.charpoly().as_expr().factor())
# Q4
W1=[Matrix([[1,1],[0,0]]),Matrix([[0,0],[2,3]]),Matrix([[5,5],[6,9]])]
V=Matrix([[m[0],m[1],m[2],m[3]] for m in W1]); print("W1 rank",V.rank(), V.rref())
# W2: a+b=c+d dim3 ; basis
a,b_,c,d=symbols('a b c d')
W2=Matrix([[1,-1,0,0],[0,1,1,0],[0,0,1,-1]])  # rows (a,b,c,d) ; check a+b-c-d
print([r[0]+r[1]-r[2]-r[3] for r in W2.tolist()])
W2=Matrix([[1,0,1,0],[0,1,1,0],[0,0,1,1]])  # a+b=c+d: (1,0,1,0):1=1 ok;(0,1,1,0) ok;(0,0,1,1)? 0=2 no
print("W2 check")
W2b=[ (1,0,1,0),(0,1,1,0),(0,0,1,1) ]
print([r[0]+r[1]-r[2]-r[3] for r in W2b])
W2b=[(1,0,1,0),(0,1,1,0),(1,0,0,1)]; print([r[0]+r[1]-r[2]-r[3] for r in W2b])
W1m=V.rref()[0][:2,:]
S=W1m.col_join(Matrix([[1,0,1,0],[0,1,1,0],[1,0,0,1]])); print("sum rank",S.rank())
# intersection: W1 = {m: a=b, with ... } W1 rows basis: (1,1,0,0),(0,0,2,3),(5,5,6,9) -> third = 5*(1,1,0,0)+3*(0,0,2,3)?? 
print(Matrix([[1,1,0,0],[0,0,2,3],[5,5,6,9]]).rank())
s,u=symbols('s u'); m=s*Matrix([1,1,0,0])+u*Matrix([0,0,2,3])
print("cap:",solve(m[0]+m[1]-m[2]-m[3],[s,u],dict=True))
# 4d  (a+b)(c+d)=0: E11 + ... counterexample
M1=Matrix([[1,0],[0,0]]); M2=Matrix([[0,0],[1,0]]); Ssum=M1+M2
print("U closed? ",(Ssum[0,0]+Ssum[0,1])*(Ssum[1,0]+Ssum[1,1]))
# 5
Tm=Matrix([[1,1,0,0],[0,0,1,1]]); print("T",Tm.rank(),Tm.nullspace())
B1=[Matrix([[1,0],[0,0]]),Matrix([[1,1],[0,0]]),Matrix([[1,1],[1,0]]),Matrix([[1,1],[1,1]])]
Bb=Matrix([[1,1],[0,-1]])
cols=[]
for m in B1:
    img=Matrix([m[0,0]+m[0,1],m[1,0]+m[1,1]]); cols.append(Bb.inv()*img)
print("[T]",Matrix.hstack(*cols))
# also alt reading with B only in domain? print raw images
print([ (m[0,0]+m[0,1],m[1,0]+m[1,1]) for m in B1])
# 1c
C,D=symbols('C D',commutative=False)
