from sympy import *
a,x,y,z=symbols('a x y z')
# Q2
M=Matrix([[1,-1,-a,a],[a,1,-1,-a],[1,a,1,-1]])
print('2a rref generic', simplify(M.rref()[0]))
A=M[:,:3]; print('det',factor(A.det()))
for v in [0,1,-1]:
    Mv=M.subs(a,v); print('a=',v,Mv.rref()[0], A.subs(a,v).rank(), Mv.rank())
print('sol generic', solve(list(M*Matrix([x,y,z,1])),[x,y,z]))
print('2c a=-1', M.subs(a,-1).rref())
print('2d', solve(z**4+8*z, z), [simplify(r) for r in roots(Poly(z**4+8*z,z))])
# Q3
A3=Matrix([[2*a,3,6],[4,a+1,4*a-2],[1,5,2]])
print('3a det',factor(A3.det()), solve(A3.det(),a))
print('3b a=2 det',A3.subs(a,2).det())
B=Matrix([[6,0,2],[1,4,0],[0,0,3]])
print('3c', B.eigenvects()); P,D=B.diagonalize(); print(P,D, P.inv()*B*P==D)
# Q4: R2[x] as (a0,a1,a2)
def vec(c0,c1,c2): return Matrix([c0,c1,c2])
Ub=Matrix.hstack(vec(1,1,0),vec(2,0,-1),vec(0,2,1))
print('U rank',Ub.rank(), Ub.columnspace(), 'det',Ub.det())
# W: a1+2a2=0
Wc=Matrix([[0,1,2]]).nullspace(); print('W basis',Wc)
print('U nullspace relation', Ub.nullspace())
Sum=Matrix.hstack(Ub,*Wc); print('U+W rank',Sum.rank())
# U cap W: coefficients c: p=Ub*c ; a1+2a2=0
cond=(Matrix([[0,1,2]])*Ub); print('cond',cond, cond.nullspace())
for n in cond.nullspace(): print('cap vec',Ub*n)
p=symbols('c0 c1 c2')
