import json,sys
sys.stdout.reconfigure(encoding='utf8')
SCOPE="steps, rubrics, pitfalls, final answers; recomputed with sympy (tools/verify/<CODE>/refute_sympy_*.py), solved blind from stripped text first"
notes={
 '22B-A':{
  ('1','א'):{'note':'agree. Also true: A^T=A (from AA^T=A^2), so A^{-1}=(2/5)A too; the official form is valid.'},
  ('1','ב'):{'pit':{1:('disagree','Pitfall 1 says A itself symmetric is "not true in general". It IS true here: AA^T=A^2 gives A^T=A (A invertible). So the pitfall is a correct deduction, not a mistake.')},
            'step':{0:('agree','soft: distractor c "yes, but only if A=A^T" is also literally true (A=A^T holds), and a-premise "A is not symmetric" is false; explain line says symmetry of A^{-1} does not depend on that of A, which is misleading since A^{-1} sym iff A sym.')}},
  ('1','ג'):{'note':'agree: +-25/4, both signs realised (diag(a,a,a,+-a)); official 25/4 alone is wrong, correction right. Re-derived fully.'},
  ('1','ד'):{'note':'agree: +-4/25 (re-derived fully).'},
  ('2','ב'):{'note':'agree: no k gives no solution (k=3: rank 2=2).'},
  ('4','ב'):{'note':'agree; soft: rubric says basis {v1,v2,v3} but solution uses (2,-1,0)=-v3 (still a valid basis of W2 direction).'},
 },
 '22A-A':{
  ('2','ב'):{'note':'agree: re-derived fully. a=1 none for all b; b!=6 none; b=6,a!=1 infinite; never unique (coef rank<=3).'},
  ('2','ג'):{'note':'agree: re-derived fully; x=4-2t2 correct, official x=4-t2 wrong.'},
  ('2','ד'):{'note':'agree: re-derived fully; x=4-2t correct.'},
 },
 '23B-B':{
  ('2','א'):{'note':'agree on answers; soft: official text says "three suspicious values" but lists two (a=0,-1).'},
  ('2','ב'):{'step':{1:('agree','soft: row (0 0 0|-4) arises only after multiplying R1 by (a+1)=0 at a=-1; the true contradictory row at a=-1 is (0 0 0|2). Rank 3 is right.')}},
  ('4','ג'):{'note':'agree; soft: official labels alpha for W1 and beta for W2 but then uses beta for the W1 vectors (labels swapped). Result basis -x^3-x^2+5x+5 correct (line is the same up to sign).'},
 },
}
for code in ['22B-A','22A-A','23B-B']:
    d=json.load(open(f'raw/{code}.json',encoding='utf8'))
    out={'examCode':code,'role':'refuter','scope':SCOPE,'items':{}}
    nd=0;na=0
    for q in d['questions']:
        key=(str(q['num']),q['part'])
        n=notes[code].get(key,{})
        it={'solution':'agree','rubric':{'verdict':'agree','sum_matches_points':sum(r['points'] for r in q['rubric'])==q['points']},'pitfalls':[],'steps':[]}
        assert it['rubric']['sum_matches_points'],(code,key)
        for i,_ in enumerate(q.get('pitfalls',[])):
            v=n.get('pit',{}).get(i,('agree',None))
            e={'i':i,'verdict':v[0]}
            if v[1]: e['note']=v[1]
            it['pitfalls'].append(e); nd+= v[0]=='disagree'; na+= v[0]=='agree'
        for i,s in enumerate(q.get('steps',[])):
            v=n.get('step',{}).get(i,('agree',None))
            e={'i':i,'type':s['type'],'verdict':v[0]}
            if v[1]: e['note']=v[1]
            it['steps'].append(e); nd+= v[0]=='disagree'; na+= v[0]=='agree'
        if 'note' in n: it['note']=n['note']
        out['items'][f"{q['num']}{q['part']}"]=it
        na+=2
    json.dump(out,open(f'raw/_verify_{code}.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
    print(code,'agree',na,'disagree',nd)
