from sympy import *
a,x,y,z=symbols('a x y z')
M=Matrix([[a,2*a,3*a,4*a],[a,2*a+1,3*a+1,4*a+1],[a,2*a-1,0,2-a]])
print("Q2 aug",M)
for v in [0,1,Rational(1,1)*2,-1,Rational(1,2),3,5]:
    Mv=M.subs(a,v); print(v,"rank A",Mv[:,:3].rank(),"rank aug",Mv.rank(), Mv.rref()[0].tolist())
print("det coeff",factor(M[:,:3].det()))
print("rref generic", simplify(M.rref()[0]))
for v in [0,1,-1,2]:
    s=linsolve((M.subs(a,v)[:,:3],M.subs(a,v)[:,3]),x,y,z);print("sol",v,s)
print(linsolve((M[:,:3],M[:,3]),x,y,z))
# 2d
zz=symbols('zz')
print(solve(zz**3+2+I,zz))
print([N(r) for r in solve(zz**3+2+I,zz)])
r=-(2+I); print(abs(r), arg(r), N(abs(r)**Rational(1,3)), N(arg(r)))
A=Matrix([[1,-2,-2],[0,-1,0],[-1,2,3]]); print("A inv",A.inv(), A.det())
print(A.inv().rref())
B=Matrix([[3,1,1],[1,3,1],[0,0,2]]); print(B.eigenvects(), B.is_diagonalizable()); P,D=B.diagonalize();print(P,D)
# Q4
t=symbols('t'); c=symbols('c0:4')
p=sum(c[i]*t**i for i in range(4))
print("U:",solve(p.subs(t,1)-diff(p,t).subs(t,1),c))
print("W:",solve(expand(p-p.subs(t,-t)),c))
# U basis: c0 + c1+c2+c3 = c1+2c2+3c3 => c0 = c2+2c3
Ub=Matrix([[0,1,0,0],[1,0,1,0],[2,0,0,1]]) # 1:coeffs c0..c3 -> x ; 1+x^2 ; 2+x^3
Wb=Matrix([[1,0,0,0],[0,0,1,0]])
S=Ub.col_join(Wb); print("U+W dim",S.rank(), S.rref()[0])
print("dim cap",3+2-S.rank())
# cap: W even c1=c3=0, in U c0=c2+2c3 -> c0=c2 : 1+x^2
print("check 1+x^2 in U:", (1+t**2).subs(t,1)-diff(1+t**2,t).subs(t,1))
# Q5
T=Matrix([[1,1,3,1],[1,1,3,1],[1,2,4,1],[1,3,5,5]]) # rows 1,x,x^2,x^3 ; columns images
print("T rank",T.rank(), "null",T.nullspace(), "colspace",T.columnspace(), T.rref())
# p,q: kernel contains (p,5,-5,q)
pp,qq=symbols('pp qq'); print(solve(list(T*Matrix([pp,5,-5,qq])),[pp,qq]))
# [T]_C^B
Bm=Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]]) # columns b_j: (1,1,0,0),(0,1,1,0),(0,0,1,1),(0,0,0,1)
Bm=Matrix([[1,0,0,0],[1,1,0,0],[0,1,1,0],[0,0,1,1]])
TB=T*Bm
# C=(x^3,1,x^2,x): reorder rows (x^3,1,x^2,x)=(row3,row0,row2,row1)
TC=Matrix([TB.row(3),TB.row(0),TB.row(2),TB.row(1)]); print("[T]_C^B",TC)
print("a=1/3:", M.subs(a,Rational(1,3)).rref(), M.subs(a,Rational(1,3))[:,:3].rank())
print("eigen A? n/a; elementary decomposition: A inv factors")
Ai=A.inv()
# recompute elementary factorization steps by rref on [A|I] tracking
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
    prod=eye(n)
    for E in Es: prod=E*prod
    return Es,prod,cur
Es,prod,cur=elem(A); print(len(Es),prod==A.inv(),cur)
for E in Es: print(E.tolist())
