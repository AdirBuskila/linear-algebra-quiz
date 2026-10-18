from sympy import *
k,x,y,z=symbols('k x y z')
M=Matrix([[1,1,k],[3,4,2],[2,3,-1]]); b=Matrix([2,k,1])
print('Q2 det',factor(M.det()))
print('uniq sol',simplify(M.inv()*b) if False else [simplify(s) for s in M.LUsolve(b)])
for kv in [k0 for k0 in solve(M.det(),k)]:
    aug=M.subs(k,kv).row_join(b.subs(k,kv)); print('k=',kv,M.subs(k,kv).rank(),aug.rank()); 
    if M.subs(k,kv).rank()==aug.rank(): print(linsolve((M.subs(k,kv),b.subs(k,kv)),x,y,z))
print('2d', solve(2-I*z**3,z), [ (N(r)) for r in solve(z**3+2*I,z)])
print('Q3a',Matrix([[1,2,0],[0,1,1],[2,4,2]]).inv(), Matrix([[1,2,0],[0,1,1],[2,4,2]]).det())
B=Matrix([[2,1,1],[1,2,1],[0,0,1]]); print(B.eigenvects()); print(B.diagonalize())
A=Matrix([[1,2,-4],[-2,3,-13],[-1,-1,1]]); print('W1 rank',A.rank(),A.columnspace(), A.det())
n2=Matrix([[1,2,-3]]).nullspace(); print('W2',n2)
W1=A.columnspace()
S=Matrix.hstack(*W1,*n2); print('sum rank',S.rank())
# intersection: W1 vectors satisfying x+2y-3z=0
cs=symbols('c0:%d'%len(W1)); v=sum((c*w for c,w in zip(cs,W1)),zeros(3,1)); print('cap',solve(v[0]+2*v[1]-3*v[2],cs), v.T)
print('4d', 5-20+15, (Matrix([5,-10,-5])), 'inW2:',5+2*(-10)-3*(-5))
print('inW1?', Matrix.hstack(A,Matrix([5,-10,-5])).rank(), A.rank())
T=Matrix([[1,1,1,1],[1,1,3,3],[-1,-1,1,1]]); print('T',T.rank(),T.columnspace(),T.nullspace())
# 5c: k+11t+t^2 -> (k,11,1)
print('5c',Matrix.hstack(T,Matrix([k,11,1])).rank(), solve(Matrix.hstack(T,Matrix([k,11,1])).extract([0,1,2],[0,1,2,3,4]).det() if False else 0,k))
for kv in range(-3,4): print(kv,Matrix.hstack(T,Matrix([kv,11,1])).rank())
a,b2=symbols('a b')
print(linsolve((T.col_join(zeros(0,4)).extract([0,1,2],[2,3]) if False else Matrix([[1,1],[3,3],[1,1]]),Matrix([k,11,1])),a,b2))
# 5d
Bm=Matrix([[1,1],[-1,1]])  # columns 1-x, 1+x as (const,x)
F=Matrix([[1,-2],[-2,4]])
print('5d',Bm.inv()*F*Bm)
