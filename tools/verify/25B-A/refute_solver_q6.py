import sympy as sp, random, itertools
# 6a: det identity numerically
for _ in range(5):
    H=sp.randMatrix(3,3,-3,3); D=sp.randMatrix(3,3,-3,3)
    if H.det()==0 or D.det()==0: continue
    # (det H)^2 (det D)^2 == (det D)^3 iff det D == (det H)^2 ; derive from equation
    lhs=H.det()*D.det()**2; rhs=D.det()**3/H.det()
    print('eq holds' if lhs==rhs else 'eq fails (random pair does not satisfy relation)', 'detD==detH^2?',D.det()==H.det()**2)
h,dd=sp.symbols('h d',nonzero=True); print(sp.solve(sp.Eq(h*dd**2,dd**3/h),dd))
print((-3)**2)
# 6b
A=sp.diag(2,4); u=sp.Matrix([0,1]); print(A.inv()*u, sp.Rational(1,4))
# 6c
B=sp.eye(2);C=-sp.eye(2); print((B+C).det(), (0*C).det(), (B*C).det())
al=sp.symbols('al'); C2=sp.Matrix(2,2,sp.symbols('c0:4')); print(sp.factor((al*C2).det()), 2*-5)
print(sp.Matrix([[1,2],[3,4]]).inv()==sp.Matrix([[1,0],[0,1]]).inv()) 
Bm=sp.Matrix([[1,2],[0,1]]);Cm=sp.Matrix([[1,0],[3,1]]); print((Bm*Cm).inv()==Cm.inv()*Bm.inv(), (Bm*Cm).inv()==Bm.inv()*Cm.inv())
