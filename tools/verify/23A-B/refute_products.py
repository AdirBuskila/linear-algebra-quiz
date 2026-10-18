from sympy import *
# 23A-B 3b
E=lambda rows: Matrix(rows)
A=Matrix([[1,-2,-2],[0,-1,0],[-1,2,3]])
P=E([[1,2,0],[0,1,0],[0,0,1]])*E([[1,0,2],[0,1,0],[0,0,1]])*E([[1,0,0],[0,-1,0],[0,0,1]])*E([[1,0,0],[0,1,0],[1,0,1]])
print("23A-B 3b product==Ainv:",P==A.inv())
print("23A-B 3c BP=PD:", Matrix([[3,1,1],[1,3,1],[0,0,2]])*Matrix([[-1,-1,1],[1,0,1],[0,1,0]])==Matrix([[-1,-1,1],[1,0,1],[0,1,0]])*diag(2,2,4))
# 22B-B 3b
A=Matrix([[1,4,0],[0,1,2],[3,12,3]])
P=E([[1,-4,0],[0,1,0],[0,0,1]])*E([[1,0,0],[0,1,-2],[0,0,1]])*E([[1,0,0],[0,1,0],[0,0,Rational(1,3)]])*E([[1,0,0],[0,1,0],[-3,0,1]])
print("22B-B 3b:",P==A.inv())
B=Matrix([[5,0,1],[0,4,0],[1,0,5]]);Pm=Matrix([[-1,0,1],[0,1,0],[1,0,1]]);print("22B 3c",Pm.inv()*B*Pm)
# 21B-B 1a
A=Matrix([[0,1,7,8],[1,3,3,8],[-2,-5,1,-8]])
Em=Matrix([[0,1,0],[1,0,0],[0,0,1]]);F=Matrix([[1,0,0],[0,1,0],[-2,0,1]]);G=Matrix([[1,0,0],[0,1,0],[0,1,1]])
R=Matrix([[1,3,3,8],[0,1,7,8],[0,0,0,0]])
print("21B 1a EFGR==A:",Em*F*G*R==A)
# 21B 3d
B=Matrix([[-2,1,-1],[1,2,3],[1,-1,0]]);Pm=Matrix([[-1,-1,-3],[-1,-2,-1],[1,1,2]]);print("21B 3d",Pm.inv()*B*Pm)
# 21B 4b basis independence
V=Matrix([[-1,0,1,0],[0,-1,0,1],[1,0,1,0],[1,1,0,0]]);print("21B 4b basis rank",V.rank())
# 21B W2 + 5 cap check
print("21B cap in W1:", Matrix([5,5,4,6]), 5*Matrix([1,1,0,0])+2*Matrix([0,0,2,3]))
# 22B 4b
V=Matrix([[1,0,0,0],[0,0,1,0],[0,-1,0,1],[8,0,0,-1]]);print("22B 4b basis rank",V.rank())
# 21B 3a det claim
k=symbols('k');print(factor(Matrix([[1,1,1],[k,k**2,1],[k**2,2*k**2-1,1]]).det()))
# 23A-B 2d numeric angles
import cmath,math
z=(-2-1j)
th=cmath.phase(z)%(2*math.pi);print(math.degrees(th)/1, [(math.degrees(th)+360*j)/3 for j in range(3)])
print("21B 2d W2 angle 9pi/8 gives",cmath.rect(2**0.25,9*math.pi/8),"13pi/8 gives",cmath.rect(2**0.25,13*math.pi/8))
# 22B hermitian check
