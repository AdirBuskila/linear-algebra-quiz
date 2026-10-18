from sympy import *
a,b,k=symbols('a b k')
M=Matrix([[1,2,2,1],[1,a,3,3],[1,11,a,b]])
print(M.subs(a,-1).echelon_form(), M.subs(a,-1).subs(b,symbols('b')).rref())
for bv in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
    Mm=M.subs({a:-1,b:bv}); print(bv,Mm.rank(),Mm[:,:3].rank())
print(Matrix([[1,1,k],[1,2,7],[1,3,10]]).det())
Fm=Matrix([[1,1],[1,-1]]); P=Matrix([[5,2],[17,7]]); print(P.inv()*Fm*P, P.det())
A3=Matrix([[1,2,3],[4,5,6],[7,8,a]]); print(simplify(A3.inv()*A3))
