from sympy import *
a,b,z=symbols('a b z')
M=Matrix([[2,-1,1,3],[1,-1,1,2],[3,-1,-a,b]])
print("det",factor(M[:,:3].det()))
print(M.echelon_form())
for av,bv in [(2,1),(-1,4),(-1,0),(-1,5),(0,3)]:
    Mm=M.subs({a:av,b:bv}); print(av,bv,Mm.rank(),Mm[:,:3].rank(),Mm.rref())
# critical a
print(solve(M[:,:3].det(),a))
print(solve(Eq(4*z,conjugate(z)**2),z) )
x,y=symbols('x y',real=True)
zz=x+I*y
print(solve([re(expand(4*zz-conjugate(zz)**2)),im(expand(4*zz-conjugate(zz)**2))],[x,y]))
A=Matrix([[1,2,1],[0,1,3],[3,8,8]]); print("detA",A.det(),A.inv())
B=Matrix([[5,0,1],[0,4,0],[1,0,5]]); print(B.eigenvects(), B.diagonalize())
V=Matrix([[0,1,1],[1,2,3],[1,1,2],[1,3,4]]).T; print(V.rank(),V.columnspace())
Wm=Matrix([[1,-2,-1]]); print(Wm.nullspace())
Vn=(Matrix([0,1,1]).cross(Matrix([1,1,2]))); print(Vn.T)
print(Matrix([[1,1,-1],[1,-2,-1]]).nullspace())
v=Matrix([1,3,2]); print((Vn.T*v), (Wm*v))
# T
a_,b_,c_,d_=symbols('a_ b_ c_ d_')
T=Matrix([[1,2,8,1],[-3,2,0,5],[1,1,5,0]]); print(T.rank(),T.columnspace(),T.nullspace(), T.rref())
