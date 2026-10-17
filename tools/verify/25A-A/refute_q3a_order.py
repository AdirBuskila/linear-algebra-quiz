from sympy import *
from itertools import permutations, product
A=Matrix([[1,2,1],[0,1,3],[3,8,8]])
def op(M,o):
    M=M.copy();k=o[0]
    if k=='add': _,i,j,c=o; M[i,:]=M[i,:]+c*M[j,:]
    elif k=='sc': _,i,c=o; M[i,:]=c*M[i,:]
    return M
ops=[('add',2,0,-3),('add',2,1,-2),('sc',2,-1),('add',1,2,-3),('add',0,2,-1),('add',0,1,-2)]
ok=[]
for p in permutations(range(6)):
    M=A
    for i in p: M=op(M,ops[i])
    if M==eye(3): ok.append(p)
print(len(ok),ok)
