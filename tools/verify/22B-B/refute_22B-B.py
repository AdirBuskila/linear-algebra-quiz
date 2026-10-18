from sympy import *
k,x,y,z,t=symbols('k x y z t')
M=Matrix([[k,k**2,k,1],[1,k,-k,1],[1,1,1,1]])
print("det",factor(M[:,:3].det()))
print("generic sol",simplify(Matrix(linsolve((M[:,:3],M[:,3]),x,y,z).args[0])))
for v in [0,1,-1,2,3]:
    Mv=M.subs(k,v); print(v,Mv[:,:3].rank(),Mv.rank(),linsolve((Mv[:,:3],Mv[:,3]),x,y,z))
# 1a: char poly of general
a,b,c,d,l=symbols('a b c d l')
Am=Matrix([[a,b],[c,d]]); cp=(Am-l*eye(2)).det()
print("cp subs d=a+b-c:",factor(expand(cp.subs(d,a+b-c))))
# 2d
zr,zi=symbols('zr zi',real=True); zc=zr+I*zi
dot=zc*1+(-1)*zc.conjugate()*0
# orthogonal: standard complex inner product u.conj(v)? try both
u=Matrix([zc,-1,2]); v=Matrix([zc,zc,1])
bil=expand(sum(u[i]*v[i] for i in range(3)))   # bilinear
herm=expand(sum(u[i]*conjugate(v[i]) for i in range(3)))
zz=symbols('zz')
print("bilinear z^2 - z + 2 :", solve(zz*zz-zz+2,zz))
print("herm: ", solve([re(herm),im(herm)],[zr,zi],dict=True))
A=Matrix([[1,4,0],[0,1,2],[3,12,3]]); print("A",A.det(),A.inv())
def elem(A):
    n=A.shape[0]; cur=A.copy(); Es=[]
    for c in range(n):
        piv=None
        for r in range(c,n):
            if cur[r,c]!=0: piv=r;break
        if piv!=c:
            E=eye(n); E.row_swap(c,piv); cur=E*cur; Es.append(E)
        if cur[c,c]!=1:
            E=eye(n); E[c,c]=1/cur[c,c]; cur=E*cur; Es.append(E)
        for r in range(n):
            if r!=c and cur[r,c]!=0:
                E=eye(n); E[r,c]=-cur[r,c]; cur=E*cur; Es.append(E)
    return Es,cur
Es,cur=elem(A); print(len(Es),cur)
for E in Es: print(E.tolist())
B=Matrix([[5,0,1],[0,4,0],[1,0,5]]); print(B.eigenvects(), B.diagonalize())
# Q4
c0,c1,c2,c3=symbols('c0:4'); p=c0+c1*t+c2*t**2+c3*t**3
print("W1",solve(p.subs(t,-1)-p.subs(t,1),[c0,c1,c2,c3]),"W2",solve(p.subs(t,2),c0))
# W1: c1+c3=0 -> basis 1,x^2,x-x^3 dim3 ; W2: dim3 basis x-2, x^2-4, x^3-8
W1=Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,-1]])
W2=Matrix([[-2,1,0,0],[-4,0,1,0],[-8,0,0,1]])
S=W1.col_join(W2); print("sum rank",S.rank())
# intersection: p(-1)=p(1), p(2)=0 -> c1=-c3, c0+2c1+4c2+8c3=0 ; dim 2
eqs=[c1+c3, c0+2*c1+4*c2+8*c3]
print(solve(eqs,[c0,c1],dict=True))
q=-t**3+2*t**2+t-2; print("q(-1),q(1),q(2)",q.subs(t,-1),q.subs(t,1),q.subs(t,2))
# 5
T=Matrix([[1,1,1],[0,1,2],[0,2,k**2+3],[0,-1,-2]])
print("T rank gen",T.rank(), "minors")
print(factor(Matrix([[1,1,1],[0,1,2],[0,2,k**2+3]]).det()))
aug=Matrix([[1,1,1,1],[0,1,2,1],[0,2,k**2+3,2],[0,-1,-2,k]])
for kv in [-1,0,1,2,-2,3]: print(kv,T.subs(k,kv).rank(),aug.subs(k,kv).rank())
print("ker k=1",T.subs(k,1).nullspace())
# aug in Im(T): solve for k: (1,1,2,k)
# F
P=Matrix([[1,3],[1,4]]); Q=Matrix([[2,5],[2,0]]); print("F",Q*P.inv())
