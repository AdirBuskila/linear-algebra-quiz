from sympy import *
x=symbols('x'); a,b,c,d=symbols('a b c d'); p=a*x**3+b*x**2+c*x+d
print("W1",solve([p.subs(x,0)-diff(p,x).subs(x,0),diff(p,x).subs(x,0)-diff(p,x,2).subs(x,0)],[c,d],dict=True))
w1=[Matrix([1,0,0,0]),Matrix([0,1,2,2])]; w2=[Matrix([1,0,0,0]),Matrix([0,1,0,0]),Matrix([0,0,0,1])]
print("sum rank",Matrix.hstack(*w1,*w2).rank())
# intersection: s*w1a + t*w1b with c=0 -> t*2=0
s,t=symbols('s t'); print(solve((s*w1[0]+t*w1[1])[2],t))
Q=Matrix([1,2,0,3]); print("Q in W2:",Q[2]==0, "rank with Q",Matrix.hstack(*w1,*w2,Q).rank())
