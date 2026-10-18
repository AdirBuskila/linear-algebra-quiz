from sympy import *
x=symbols('x'); a=symbols('a0:4')
p=sum(a[i]*x**i for i in range(4))
odd=solve(Poly(expand(p.subs(x,-x)+p),x).all_coeffs(),a,dict=True); print("U",odd)
print("W: p'(1)=0 ->",solve(diff(p,x).subs(x,1),a[1]))
cap=p.subs({a[0]:0,a[2]:0}); s=solve(diff(cap,x).subs(x,1),a[1]); print("cap",s)
b=symbols('b'); q=b*(x**3-3*x); bb=solve(q.subs(x,1)-1,b)[0]; q=q.subs(b,bb); print(q,diff(q,x).subs(x,1),diff(q,x).subs(x,sqrt(2)))
U=Matrix([[0,1,0,0],[0,0,0,1]]); W=Matrix([[1,0,0,0],[0,-2,1,0],[0,-3,0,1]]); print("sum rank",Matrix.vstack(U,W).rank(),"W rank",W.rank())
