from sympy import *
a=symbols('a')
# Q1
print('1a dist', Rational(9)/sqrt(6), nsimplify(9/sqrt(6)), N(9/sqrt(6)))
print('1c', Matrix([1,-2,1]).cross(Matrix([2,-1,2])))
print('1d', N(34**Rational(1,10)), N(atan(Rational(3,5))), N(atan(Rational(3,5))/5), N(atan(Rational(3,5))*180/pi))
# Q2
A=Matrix([[1,0,1,1],[1,1,2,0],[0,1,1,-1]])
print('2 rref',A.rref(), 'rank',A.rank())
print('null',A.nullspace()); print('col',A.columnspace()); print('row',A.T.columnspace(), A.rref()[0])
# Q3
A3=Matrix([[2,1,-1],[1,a,1],[3,1,-a]])
print('3a',factor(A3.det()), solve(A3.det(),a), expand(A3.det()))
A31=A3.subs(a,1); print('3b det',A31.det(), A31.inv() if A31.det()!=0 else None)
B=Matrix([[1,1,-1],[1,1,1],[1,1,1]])
print('3c',B.eigenvects(), B.charpoly().as_expr().factor(), B.is_diagonalizable())
P,D=B.diagonalize(); print(P,D)
# Q4
W1=Matrix.hstack(Matrix([1,2,3]),Matrix([2,3,1]),Matrix([3,1,2]),Matrix([1,1,1]))
print('W1 rank',W1.rank(), W1.rref())
Wn=Matrix([[1,-2,-1]]).nullspace(); print('W2 basis',Wn)  # x-y-z-y = x-2y-z=0
W2=Matrix.hstack(*Wn); print('W1+W2 rank',Matrix.hstack(W1,W2).rank())
v=Matrix([3,1,-1]); print('v in W2?', (Matrix([[1,-2,-1]])*v), 'in W1?', W1.rank()==Matrix.hstack(W1,v).rank())
# W1 = R^3 if rank 3
# Q5
T=Matrix([[1,-1,0],[-2,2,0],[0,0,2]])
print('ker',T.nullspace(),'im',T.columnspace(), T.rank())
B1=Matrix.hstack(Matrix([1,1,1]),Matrix([0,1,1]),Matrix([0,0,1]))
B2=Matrix.hstack(Matrix([1,0,0]),Matrix([0,1,1]),Matrix([1,1,0]))
print('5d',B2.inv()*T*B1)
print('T on B1 cols',[list(T*B1[:,i]) for i in range(3)])
print('B2inv', B2.inv())
