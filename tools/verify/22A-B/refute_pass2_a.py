from sympy import *
a,b,z,k,t=symbols('a b z k t')
print("1c",Rational(81,32),"1d",Rational(32,81))
M=Matrix([[1,2,2,1],[1,a,3,3],[1,11,a,b]])
A=M[:,:3]; print("det sys",factor(A.det()))
for av,bv in [(2,1),(5,7),(5,0),(2,0),(5,7)]:
    Mm=M.subs({a:av,b:bv}); print(av,bv,Mm.rank(),Mm[:,:3].rank(), Mm.rref()[0].tolist())
# a=2: general bv
Mm=M.subs(a,2); print("a=2 rref",Mm.rref()[0].tolist(), Mm.rref())
print("a=2 elim",Mm.subs(b,symbols('b')).echelon_form())
print("a=5",M.subs(a,5).echelon_form())
print("2d",solve(Matrix([[1,2,-2],[0,z,1],[1,0,z]]).det(),z), factor(Matrix([[1,2,-2],[0,z,1],[1,0,z]]).det()))
A3=Matrix([[1,2,3],[4,5,6],[7,8,a]]); print("3a det",A3.det(), simplify(A3.inv()))
A9=A3.subs(a,9); print(A9.rank(), A9.rowspace(), A9.nullspace(), A9.T.nullspace())
# 4: U odd polys deg<=3: x, x^3
x=symbols('x')
# W: p'(1)=0: p=c0+c1x+c2x^2+c3x^3, c1+2c2+3c3=0
Wm=Matrix([[0,1,2,3]]); print("W null",Wm.nullspace())
Um=Matrix([[1,0,0,0],[0,0,1,0]]) # even coeffs zero
print("U null", Um.nullspace())
Uv=[Matrix([0,1,0,0]),Matrix([0,0,0,1])]
Wv=Wm.nullspace()
S=Matrix.hstack(*(Uv+Wv)); print("U+W rank",S.rank())
# intersection: p=c1 x+c3 x^3, c1+3c3=0 -> -3x+x^3 ; q(1)=1: q=c(x^3-3x), c(1-3)=1 c=-1/2
c=Rational(-1,2); q=c*(x**3-3*x); print(q, diff(q,x).subs(x,1), diff(q,x).subs(x,sqrt(2)))
T=Matrix([[1,1,-1,3],[1,2,0,4],[1,3,1,5]]); print("T rank",T.rank(),T.columnspace(),T.nullspace())
print(Matrix.hstack(T,Matrix([k,7,10])).rank())
print(solve(Matrix.hstack(T[:,:3], Matrix([k,7,10])).det(),k), Matrix.hstack(T,Matrix([k,7,10])).det() if False else '')
# k: need (k,7,10) in span of (1,1,1),(1,2,3): det
print(Matrix([[1,1,k],[1,2,7],[1,3,10]]).det())
Fm=Matrix([[1,1],[1,-1]]); P=Matrix([[5,2],[17,7]]); print(P.inv()*Fm*P, P.det())
