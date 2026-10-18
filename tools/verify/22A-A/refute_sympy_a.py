from sympy import *
a,b,x,y,z,w=symbols('a b x y z w')
M=Matrix([[1,0,0,2,4],[0,a**2-a,a**2-a,0,a],[1,0,a-1,a+1,a+3],[2,a**2-a,a**2+a-2,2*a+2,3*a+b]])
print(M.rref(simplify=True) if False else '')
# row reduce symbolically by hand: R3-=R1, R4-=2R1, R4-=R2
M2=M.copy(); M2[2,:]=M[2,:]-M[0,:]; M2[3,:]=M[3,:]-2*M[0,:]-M[1,:]; M2=M2.applyfunc(factor); pprint(M2)
for av,bv in [(0,6),(2,6)]:
    Ms=M.subs({a:av,b:bv}); print(av,bv,Ms[:,:4].rank(),Ms.rank(), linsolve((Ms[:,:4],Ms[:,4]),x,y,z,w))
# classify
for av in [0,1,2,3,-2,Rational(1,2)]:
  for bv in [6,0,1,-3]:
    Ms=M.subs({a:av,b:bv}); print(av,bv,Ms[:,:4].rank(),Ms.rank())
# a=0, b arbitrary; a=1
for av in [0,1]:
  print('a',av,[ (bv,M.subs({a:av,b:bv})[:,:4].rank(),M.subs({a:av,b:bv}).rank()) for bv in range(-3,8)])
print('a=2 any b', [(bv,M.subs({a:2,b:bv})[:,:4].rank(),M.subs({a:2,b:bv}).rank()) for bv in range(-3,8)])
A=Matrix([[1,3,0],[0,3,1],[1,3,1]]); print(A.det(),A.inv())
B=Matrix([[1,1,0],[0,-2,0],[-1,0,3]]); print(B.eigenvects(), B.diagonalize())
W1=Matrix([[1,2,-1]]).nullspace(); W2=Matrix([[2,1,-1]]).nullspace(); print(W1,W2)
print('sum',Matrix.hstack(*W1,*W2).rank())
N=Matrix([[1,2,-1],[2,1,-1]]).nullspace(); print('cap',N)
v=Matrix([2,2,6]); print((Matrix([[1,2,-1],[2,1,-1]])*v).T)
T=Matrix([[1,1,1,1],[1,2,2,2],[1,2,3,3]]); print(T.rank(),T.columnspace(),T.nullspace())
k=symbols('k'); print(T*Matrix([k,0,2,-2]), solve((T*Matrix([k,0,2,-2])),k))
# 5d
P=Matrix([[2,3],[3,5]]); Q=Matrix([[7,5],[3,2]]); print(Q*P.inv())
print(solve(z**3-1,z), sum(solve(z**3-1,z)))
