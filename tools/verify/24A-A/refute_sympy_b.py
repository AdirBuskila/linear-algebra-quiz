from sympy import *
k,x,y,z=symbols('k x y z')
M=Matrix([[1,0,-3,-3],[2,k,-1,-2],[1,2,k,1]])
for kv in [-5,2]:
    Mv=M.subs(k,kv);print(kv,Mv[:,:3].rank(),Mv.rank(),linsolve((Mv[:,:3],Mv[:,3]),x,y,z), Mv[:,:3].nullspace())
