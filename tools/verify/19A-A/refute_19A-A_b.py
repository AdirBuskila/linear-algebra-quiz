from sympy import *
m1=Matrix([2,-2,-5]);m2=Matrix([2,-2,-1]);P=Matrix([-1,1,1])
print("1b dots with m1:",m1.dot(m1),P.dot(m1),(m1+m2).dot(m1)," with m2:",m1.dot(m2),P.dot(m2),(m1+m2).dot(m2), "m1.n",m1.dot(Matrix([-8,-8,0])))
B=Matrix([[0,1,7,8],[1,3,3,8],[-2,-5,1,-8]])
E=Matrix([[0,1,0],[1,0,0],[0,0,1]]);F=Matrix([[1,0,0],[0,1,0],[-2,0,1]]);G=Matrix([[1,0,0],[0,1,0],[0,1,1]])
R=Matrix([[1,3,3,8],[0,1,7,8],[0,0,0,0]])
print("EFGR==B",E*F*G*R==B)
e1=E;e2=Matrix([[1,0,0],[0,1,0],[2,0,1]]);e3=Matrix([[1,0,0],[0,1,0],[0,-1,1]])
print(e3*e2*e1*B==R)
ops={'a':(e3,e2,e1),'b':(e1.inv(),e2.inv(),e3.inv()),'c':(e1,e2,e3),'d':(e3.inv(),e2.inv(),e1.inv())}
for k,(x,y,z) in ops.items(): print(k,x*y*z*R==B)
