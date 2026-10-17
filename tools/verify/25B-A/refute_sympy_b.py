from sympy import *
A=Matrix([[1,-1,0],[0,1,1],[5,-5,9]])
E1=Matrix([[1,0,0],[0,1,0],[-5,0,1]]);E2=diag(1,1,Rational(1,9));E3=Matrix([[1,0,0],[0,1,-1],[0,0,1]]);E4=Matrix([[1,1,0],[0,1,0],[0,0,1]])
print(E4*E3*E2*E1==A.inv(), E1*E2*E3*E4==A.inv())
for n,M in [('E3',E3),('E2',E2)]: print(n,M==A.inv())
Ab=Matrix([[1,2],[3,4]]);Ac=Matrix([[1,3],[4,8]])
print(Ac.inv()*Ab, Ab*Ac.inv(), Ac*Ab, Ab.inv()*Ac)
# check rref steps 3a
print((E1*A), (E2*E1*A), (E3*E2*E1*A), E4*E3*E2*E1*A)
B=Matrix([[7,0,1],[0,6,0],[1,0,7]]);print((B-6*eye(3)).rank())
# distractor 4a, W symmetric: findbug fine
# 5a distractors
T=Matrix([[1,1,1,1],[2,0,2,5],[3,1,3,6],[6,2,6,12]]);print(T.rref())
print(T.row_join(Matrix([1,0,0,0])).rank(),T.row_join(Matrix([1,-2,0,0])).rank())
