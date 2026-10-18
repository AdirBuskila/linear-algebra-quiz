import json, pathlib
RAW=pathlib.Path('tools/raw')
deriv={
'23A-B':"Own derivation (sympy, tools/verify/23A-B/refute_*.py): Q2 rank by a: unique iff a not in {0,1/3}; a=1/3 none (row 0 0 0|4/3); a=0 infinite (0,..): x free,y=-2,z=3; z=0 or z^3=-2-i (r=5^(1/6), args 68.86/188.86/308.86 deg). A^-1=[[3,-2,2],[0,-1,0],[1,0,1]], det -1, 4 elementary ops, product checked. B diagonalizable, eig 2,2,4, P cols (-1,1,0),(-1,0,1),(1,1,0). U=<x,1+x^2,2+x^3> dim3, W=<1,x^2> dim2, U+W=V dim4, U^W=<1+x^2> dim1. T: rank3, ker=<(-2,-1,1,0)>, not 1-1, not onto, p=10 q=0, [T]_C^B=[[4,8,10,5],[2,4,4,1],[3,6,5,1],[2,4,4,1]]. Proofs 1a-1d logically valid.",
'22B-B':"Own derivation: eigenvalues of [[a,b],[c,d]] with a+b=c+d are (a+b),(a-c) (charpoly factors). Q2 det=-k(k-1)(k+1): unique k not in {0,+-1}, (x,y,z)=((k+3)/(k+1),-1/k,(1-k)/(k(k+1))); k=0,-1 none; k=1 infinite (1-y,y,0). 2d bilinear z^2-z+2=0 -> (1+-i sqrt7)/2 (Hermitian product would give no solution). A^-1=[[-7,-4,8/3],[2,1,-2/3],[-1,0,1/3]], det 3; B diag(4,4,6) P cols (-1,0,1),(0,1,0),(1,0,1). W1=<1,x^2,x^3-x>, W2 dim3, sum dim4, cap=<x^3-x-6... i.e. -x^3+x+6, x^2-4> dim2, p in cap. T: (1,1,2,k) in Im iff k=-1; never onto; 1-1 iff k!=+-1; ker(k=1)=<1-2x+x^2>; [F]=[[3,-1],[8,-6]].",
'21B-B':"Own derivation: A=EFGR checked by multiplication (E swap, F=R3-2R1 inverse, G=R3+R2). B^-1=(B^2-5I)/4. X=D^-1+C^-1. Q2 det=k(k-3)(k+3): unique k not in {0,3,-3}; k=0,3 infinite; k=-3 none; k=0: (1-t,t,1/3). 2d roots (-i+-sqrt(-1-i))/2 = -0.2275+0.0493i, 0.2275-1.0493i (sqrt(-1-i) args 5pi/8 and 13pi/8). det A=-(k-1)^3(k+1). k=1 col(A)=<(1,1,1)>. B eig 0,1,-1 diagonalizable. W1 dim2, W2 dim3, sum=M2x2, cap=<[[5,5],[4,6]]>; U not subspace. T(a,b;c,d)=(a+b,d+c): ker dim2, Im=R^2, not invertible, [T]_{B2}^{B1}=[[1,2,3,4],[0,0,-1,-2]]."}
notes={
'23A-B':{'4ב':("agree","wording: solution says W is defined by 'one constraint' but p(x)=p(-x) gives two (a=c=0); dim 2 correct")},
'22B-B':{'2ד':("agree","convention note: answer uses bilinear u.v; under the standard Hermitian inner product there are NO solutions (|z|^2 - conj(z)+2=0 has no root). Official solution uses bilinear, so key matches official; context c2 (the linear system) is attached to this item though unrelated"),
         '5ג':("agree","minor: solution writes 1-2t+t^2 although the domain variable is x (steps use x)")},
'21B-B':{'2ג':("disagree","pitfall #1 is incoherent: 'dividing by 9 and erring: 9z=3 gives z=1/3' describes the correct result as the error. Solution/steps/rubric agree."),
         '2ד':("disagree","solution text: W2 = 2^(1/4)(cos 9pi/8 + i sin 9pi/8) is wrong; 9pi/8 gives -1.0987-0.455i. Correct is 13pi/8 (=5pi/8+pi) giving 0.455-1.0987i. Numeric W2, z1, z2 and all steps agree (error is inherited from the official solution, page 3)"),
         '3ג':("agree","weak: solution proves only the k!=+-1 direction, not that k=+-1 fails"),
         '3ד':("agree","naming: question/steps use B, solution/rubric use A"),
         '5ד':("agree","step0 explain 'the last choice' should refer to choice c (standard-basis coordinates); numbers correct"),
         '5א':("agree","solution rewritten for printed T=(a+b,d+c); official page 8 solved (a+d,b+c); confirmed the printed question is (a+b,d+c)")}}
for code in ['23A-B','22B-B','21B-B']:
    d=json.load(open(RAW/f'{code}.json',encoding='utf8'))
    items={}; ag=dis=0
    for q in d['questions']:
        k=f"{q['num']}{ {'א':'a','ב':'b','ג':'c','ד':'d'}[q['part']] }"
        v,n=notes.get(code,{}).get(f"{q['num']}{q['part']}",("agree",""))
        items[k]={"verdict":v,"rubric":"agree","pitfalls":"disagree" if (code=='21B-B' and k=='2c') else "agree",
                  "solution":"disagree" if (code=='21B-B' and k=='2d') else "agree",
                  "steps":["agree"]*len(q.get('steps',[])),"note":n}
        if v=="agree": ag+=1
        else: dis+=1
    out={"examCode":code,"role":"refuter","derivationBeforeClaims":deriv[code],"transcription":"checked against page PNGs (23A-B p1-2, 22B-B p1,3, 21B-B p2,3,7-9): no mismatches","summary":{"agree":ag,"disagree":dis,"unclear":0},"items":items}
    (RAW/f'_verify_{code}.json').write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding='utf8')
    print(code,ag,dis)
