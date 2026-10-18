from sympy import *
a,b,x,y,z=symbols('a b x y z')
C=Matrix([[1,0,0],[5,a,0],[2,a,1]]); print("1c det",C.det(), C.subs(a,0).columnspace(), C.subs(a,0).rank())
M=Matrix([[2,-1,1,3],[1,-1,1,2],[3,-1,-a,b]])
print("2a rref (generic)",M.rref())
print("2 det coeff", M[:,:3].det())
for av,bv in [(2,1),(-1,4)]:
    Mm=M.subs({a:av,b:bv}); print("2",av,bv,Mm.rref(), "rank coef",Mm[:,:3].rank(),"aug",Mm.rank())
    print(linsolve((Mm[:,:3],Mm[:,3]),x,y,z))
print("a=-1,b param:",[ (M.subs({a:-1,b:bv}).rank()) for bv in (4,0,1,5)])
print("a=-1: det", M[:,:3].subs(a,-1).det())
# 2e: 4z = conj(z)^2
r,t=symbols('r t',real=True)
sol=set()
zz=symbols('zz')
u,v=symbols('u v',real=True)
eqs=[re(expand(4*(u+I*v)-(u-I*v)**2)), im(expand(4*(u+I*v)-(u-I*v)**2))]
print("2e",solve(eqs,[u,v],dict=True))
A=Matrix([[1,2,1],[0,1,3],[3,8,8]]); print("3a det",A.det(),A.inv())
B=Matrix([[5,0,1],[0,4,0],[1,0,5]]); print("3b",B.eigenvects()); print(B.diagonalize())
V=Matrix([[0,1,1],[1,2,1+0],[1,3,2]]).T
vs=Matrix.hstack(Matrix([0,1,1]),Matrix([1,2,3]),Matrix([1,1,2]),Matrix([1,3,4]))
print("4a V rank",vs.rank(),vs.columnspace(), "rref",vs.rref())
Wm=Matrix([[1,-2,-1]]); Wb=Wm.nullspace(); print("W",Wb)
vc=vs.columnspace(); S=Matrix.hstack(*vc,*Wb); print("V+W rank",S.rank())
# V as plane: normal
n=vc[0].cross(vc[1]); print("V normal",n.T)
# intersection
c1,c2,d1,d2=symbols('c1 c2 d1 d2')
vec=c1*vc[0]+c2*vc[1]
print("cap:",solve(Wm*vec,[c1,c2],dict=True), vec.T)
w=Matrix([1,3,2]); print("4d in W:",(Wm*w)[0], "in V:", Matrix.hstack(*vc,w).rank())
# T
T=Matrix([[1,2,8,1],[-3,2,0,5],[1,1,5,0]]) # coeff rows: const,x,x^2 ; cols a,b,c,d
print("5 ker",T.nullspace(),"rank",T.rank(),"im",T.columnspace())
print("---- claim checks")
E1=Matrix([[1,0,0],[-3,1,0],[0,0,1]])  # placeholder
def E(i,j,c): 
    m=eye(3); m[i,j]=c; return m
Ls=[Matrix([[1,0,0],[0,1,0],[-3,0,1]]),Matrix([[1,0,0],[0,1,0],[0,-2,1]]),Matrix([[1,0,0],[0,1,0],[0,0,-1]]),Matrix([[1,0,0],[0,1,-3],[0,0,1]]),Matrix([[1,0,-1],[0,1,0],[0,0,1]]),Matrix([[1,-2,0],[0,1,0],[0,0,1]])]
prod=Ls[5]*Ls[4]*Ls[3]*Ls[2]*Ls[1]*Ls[0]
print("3a product == inv:",prod==A.inv())
P=Matrix([[0,-1,1],[1,0,0],[0,1,1]]); D=diag(4,4,6); print("3c",P.det(),P.inv()*B*P==D, B*P)
# 5b kernel check
K=[Matrix([[-2,-3],[1,0]]),Matrix([[1,-1],[0,1]])]
def Tf(M):
    a_,b_,c_,d_=M[0,0],M[0,1],M[1,0],M[1,1]; return (a_+2*b_+8*c_+d_,-3*a_+2*b_+5*d_ if False else -3*a_+2*b_+5*d_,a_+b_+5*c_)
print("5b",[Tf(m) for m in K])
print("5c imaging",Tf(Matrix([[1,0],[0,0]])),Tf(Matrix([[0,1],[0,0]])))
