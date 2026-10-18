import json
RAW='tools/raw/'
def build(code, overrides, itemnotes, derivation):
    d=json.load(open(RAW+code+'.json',encoding='utf8'))
    items=[]
    for q in d['questions']:
        key=f"{q['num']}{q['part']}"
        if 'hold' in q:
            items.append({"num":q['num'],"part":q['part'],"verdict":"skipped","note":"held item ("+str(q['hold'])+"), out of scope"}); continue
        o=overrides.get(key,{})
        steps=[]
        for j,s in enumerate(q['steps']):
            st=o.get('steps',{}).get(j)
            steps.append({"step":j,"type":s['type'],"verdict":st[0] if st else "agree","note":st[1] if st else ""})
        it={"num":q['num'],"part":q['part'],
            "solution":o.get('solution','agree'),
            "rubric":o.get('rubric','agree (points sum to item total, content matches own derivation)'),
            "pitfalls":o.get('pitfalls','agree'),
            "steps":steps}
        if key in itemnotes: it['note']=itemnotes[key]
        bad=[it['solution'],it['rubric'],it['pitfalls']]+[s['verdict'] for s in steps]
        it['verdict']='disagree' if any(str(b).startswith('disagree') for b in bad) else 'agree'
        items.append(it)
    out={"examCode":code,"verifier":"refuter","derivation":derivation,"items":items}
    json.dump(out,open(RAW+f'_verify_{code}.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
    from collections import Counter
    print(code,Counter(i['verdict'] for i in items))

build('20B-A',{
 '1א':{'pitfalls':'disagree: pitfall 1 says the wrong vector (-1,3,-2) gives k=-4. Correct arithmetic with that vector gives det=3k+9 so k=-3; the official k=-4 comes from a second slip (-3*(1-4) written as 12 instead of 9). Solution key k=-1 agrees.'},
 '1ב':{'pitfalls':'disagree: pitfall 1 says the wrong vector yields 3*sqrt2. With (-1,3,-2) the mixed product is 15 (official wrote 18, an arithmetic slip), giving 15/(3*sqrt2)=5*sqrt2/2. Final d=3*sqrt2/2 agrees.'},
},{
 '1ג':'counterexample verified: a x b = a x c = (0,0,1), b != c',
 '5ג':'own computation: intersection = span{[[1,2],[-1,1]]}, dim 1, rank of 4x4 = 3, dim(W+U)=3',
},"Own sympy derivations in tools/verify/20B-A/refute_20B-A.py: 1a k=-1; 1b d=3*sqrt2/2; 1c false (b-c parallel to a); 2 rref last row (0 0 2-2k^2 | 2+k-k^2), k=1 none, k=-1 infinite x=0,y=z-1, else unique; 3 null{(-1,-1,1,0),(-1,1,0,1)}, row{(1,0,1,1),(0,1,1,-1)}, col{(1,1,0),(0,1,1)}, rank 2; 4a det=4(a-1)(a-2); 4b inverse [[-5/8,1/2,1],[5/8,-1/2,0],[-3/8,1/2,0]]; 4c eigen 2,3,4 with (-1,1,0),(-1,0,1),(0,0,1); 5b basis {[[1,2],[-1,0]],[[0,0],[0,1]]}; 5c W∩U=span{[[1,2],[-1,1]]}; 6 ker=span{[[1,-1],[1,1]]}, Im=R^3, not injective, onto, preimage of (1,1,1) = [[d,1-d],[d,d]] affine, not subspace. Transcription checked against pages 1-5,7.")

build('19A-A',{
 '1ב':{'steps':{0:('disagree',"key (b) agrees. Explanation numbers wrong: for a=2 m1.m1=33 (claimed 18), P1P2.m1=-9 (ok), (m1+m2).m1=46 (claimed 42)")}},
 '2ד':{'pitfalls':'disagree: pitfall 1 lists (i-1)(1-i)=2i as an arithmetic error, but 2i is the correct value (and what the solution uses); misleading'},
},{
 '3ג':'caveat: statement fails if cv+dw=0 (e.g. w=-v, c=d); solution and rubric never require cv+dw != 0 (official solution has the same gap)',
 '3ד':'caveat: solution asserts "!= lambda(cv+dw)" without the independence argument (distinct-eigenvalue eigenvectors are independent, so c(l1-l)v+d(l2-l)w=0 forces l=l1=l2); rubric accepts the assertion',
},"Own sympy derivations in tools/verify/19A-A/refute_19A-A.py and _b.py: 1a a=2,4 (V=(a-2)(a-4)); 1b plane -8x-8y+24=0 (x+y=3); 1c d=8/sqrt120=2*sqrt30/15≈0.7303; 2 rref last row (0 0 (1-k)(1+k) | 2(1-k)), k=1 infinite (x=-t,y=2,z=t), k=-1 none, else unique, k=i -> (-1,2-i,1-i); 3a EFGR==B verified numerically with E=P12,F=[[1,0,0],[0,1,0],[-2,0,1]],G=[[1,0,0],[0,1,0],[0,1,1]], only option b of the step choice reproduces B; 4 W basis {I,[[0,1],[1,1]]}, dim(U+W)=4, U∩W=span{[[2,1],[1,3]]}; 5a det=-(a-2)(a+6); 5b inverse (1/7)[[13,-1,-5],[-4,3,1],[-1,-1,2]]; 5d -30375; 6 ker=span{2+x^2,-1+x^3}, Im=span{1-x^2,x^2+x^3}, not injective. Transcription checked against pages 1-3,7 (T formula, B, lines, system).")
