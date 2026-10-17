from sympy import *
a,s,t,x=symbols('a s t x')
# Q1
sol=solve([s-5-t*a, a-(-4-3*t), -a+s-(-1)],[s,t,a],dict=True); print('Q1',sol)
# Q2
M=Matrix([[a,a,-1],[a**2,a,a**2-a],[a,a,2*a+1]])
print('det',factor(M.det()))
for v in [0,1,-1,Rational(1,2),2,3,-2]:
    print(v,M.subs(a,v).rank(), M.subs(a,v).nullspace())
print(factor(M.det()))
# Q3
A=Matrix([[1,2,1],[0,1,3],[3,8,8]]);print(A.det(),A.inv())
B=Matrix([[9,0,1],[0,8,0],[1,0,9]]);print(B.eigenvects(),B.is_diagonalizable())
# Q4: basis 1,x,x^2,x^3 coords (c0..c3)
c=symbols('c0:4')
p=sum(c[i]*x**i for i in range(4))
print('W1', solve([p.subs(x,0)-diff(p,x).subs(x,0), diff(p,x).subs(x,0)-diff(p,x,2).subs(x,0)],c))
print('W2', solve([diff(p,x).subs(x,0)],c))
# W1: c0=c1=2c2 -> c0=c1=2c2: basis 2+2x+x^2, x^3 ; W2: c1=0 dim3
W1=Matrix([[2,2,1,0],[0,0,0,1]]);W2=Matrix([[1,0,0,0],[0,0,1,0],[0,0,0,1]])
S=Matrix.vstack(W1,W2);print('sum rank',S.rank())
print('Q4d',Matrix.vstack(S,Matrix([[3,0,2,1]])).rank())
# intersection: c1=0 and c0=c1=2c2 -> c0=0,c2=0 -> span x^3
# Q5
T=Matrix([[1,1,1,1],[2,0,2,5],[12,10,12,15],[21,1,21,51]]).T  # columns= images of 1,x,x2,x3 as (a,b,c,d)
print(T.rank(),T.nullspace(),T.columnspace())
img=lambda v: T*Matrix(v)
av,bv=symbols('a b')
print(solve(list(T*Matrix([22,22,av,bv])),[av,bv]))
Bm=Matrix([[2,0],[2,5]]);Cm=Matrix([[1,2],[3,7]]);print(Cm.inv()*Bm)
