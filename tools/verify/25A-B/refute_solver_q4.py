import sympy as sp
a,b,c,d,x=sp.symbols('a b c d x')
p=a+b*x+c*x**2+d*x**3   # own coords (const,x,x^2,x^3)
f=lambda q:(q.subs(x,0),sp.diff(q,x).subs(x,0),sp.diff(q,x,2).subs(x,0))
# W1: p(0)=p'(0)=p''(0)
w1=sp.solve([f(p)[0]-f(p)[1],f(p)[1]-f(p)[2]],[a,b],dict=True)[0]; print('W1',sp.expand(p.subs(w1)))
W1=[sp.Poly(x**3,x),sp.Poly(x**2+2*x+2,x)]
for q in (x**3,x**2+2*x+2): assert f(q)[0]==f(q)[1]==f(q)[2]
# claimed alt wrong conditions
assert not (f(x**2+2*x+2)[0]==f(x**2+2*x+2)[1]==1)
M=lambda L:sp.Matrix([[sp.Poly(q,x).coeff_monomial(x**k) for k in range(3,-1,-1)] for q in L])  # (a,b,c,d) of claim
print('dimW1',M([x**3,x**2+2*x+2]).rank(),'dimW2',M([x**3,x**2,1]).rank())
for q in (x**3,x**2,1): assert sp.diff(q,x).subs(x,0)==0
print('sum rank',M([x**3,x**2+2*x+2,x**2,1]).rank())
print('claim matrix', M([x**3,x**2+2*x+2,x**2,1]).tolist())
R=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,1,2,2],[0,0,0,1]]); R[2,:]=R[2,:]-R[1,:]; R[2,:]=R[2,:]-2*R[3,:]; print(R)
# intersection: p in W1, p'(0)=0
print('int',sp.solve(sp.Eq(sp.diff(p.subs(w1),x).subs(x,0),0),b))
print('2+3-1=',2+3-1)
Q=x**3+2*x**2+3; print('Q\'(0)',sp.diff(Q,x).subs(x,0), 'dQ',sp.diff(Q,x), 'Q W1?',f(Q))
