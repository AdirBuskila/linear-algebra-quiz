/* kernel_image, level 5: dimension theorem, injective and onto */
COURSE_LEVEL("kernel_image", {
  id: "C05", order: 5, icon: "⚖️", title: "משפט המימדים, חח״ע ועל",
  goal: "להשתמש במשפט המימדים, ולהכריע ולנמק אם העתקה חח״ע ואם היא על.",
  source: "ai-verified",
  lesson: { html: String.raw`
<div class="lesson-rule">🔑 <b>משפט המימדים</b>: $\dim\mathrm{Ker}\,T+\dim\mathrm{Im}\,T=\dim V$, כאשר $V$ הוא התחום.</div>
<ul>
<li>$T$ <b>חח״ע</b> אם ורק אם $\mathrm{Ker}\,T=\{\vec 0\}$, כלומר $\dim\mathrm{Ker}\,T=0$.</li>
<li>$T$ <b>על</b> אם ורק אם $\mathrm{Im}\,T=W$, כלומר $\dim\mathrm{Im}\,T=\dim W$ (מימד הטווח).</li>
</ul>
<p>מהמשפט נובע: כשמימדי התחום והטווח שווים, $T$ חח״ע אם ורק אם היא על. אם $\dim V>\dim W$ אז $T$ לא חח״ע (הגרעין לפחות $\dim V-\dim W>0$). אם $\dim V<\dim W$ אז $T$ לא על ($\dim\mathrm{Im}\le\dim V<\dim W$).</p>
<div class="lesson-ex">דוגמה: $T:\mathbb{R}_3[x]\to\mathbb{R}^3$ עם $\dim\mathrm{Ker}\,T=2$ ו-$\dim\mathrm{Im}\,T=2$ (בדיקה: $2+2=4=\dim\mathbb{R}_3[x]$). $T$ לא חח״ע כי $\dim\mathrm{Ker}\,T=2\neq0$, ולא על כי $\dim\mathrm{Im}\,T=2\neq3=\dim\mathbb{R}^3$.</div>
<div class="lesson-trap">⚠️ כותבים את ההשוואה במפורש, והשוואה נכונה: חח״ע נקבע מהגרעין ($\neq0$), על נקבע מהתמונה מול מימד <b>הטווח</b>. לא כותבים "לא חח״ע כי לא על".</div>
` },
  questions: [
    { id: "C05-Q1",
      step: { type: "numeric",
        prompt: String.raw`$T:\mathbb{R}^5\to\mathbb{R}^3$ לינארית ו-$\dim\mathrm{Im}\,T=3$. מהו $\dim\mathrm{Ker}\,T$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`לפי משפט המימדים $\dim\mathrm{Ker}\,T=5-3=2$.` },
      recap: "Ker + Im = מימד התחום." },
    { id: "C05-Q2",
      question: String.raw`$T:\mathbb{R}^4\to\mathbb{R}^3$ לינארית. איזו טענה נכונה בהכרח?`,
      options: [
        { id: "a", value: String.raw`$T$ לא חח״ע` },
        { id: "b", value: String.raw`$T$ לא על` },
        { id: "c", value: String.raw`$T$ חח״ע` },
        { id: "d", value: String.raw`$\mathrm{Ker}\,T=\{\vec 0\}$` },
      ],
      correctId: "a",
      explanation: String.raw`$\dim\mathrm{Im}\,T\le3$, ולכן $\dim\mathrm{Ker}\,T=4-\dim\mathrm{Im}\,T\ge1$, כלומר $T$ לא חח״ע. היא יכולה להיות על ($\dim\mathrm{Im}=3$), ולכן ב' לא בהכרח. ג' ו-ד' סותרות את $\dim\mathrm{Ker}\ge1$.`,
      recap: "תחום גדול מהטווח: לא חח״ע." },
    { id: "C05-Q3",
      question: String.raw`$T:\mathbb{R}_1[x]\to\mathbb{R}^4$ לינארית. איזו טענה נכונה בהכרח?`,
      options: [
        { id: "a", value: String.raw`$T$ לא על` },
        { id: "b", value: String.raw`$T$ לא חח״ע` },
        { id: "c", value: String.raw`$T$ על` },
        { id: "d", value: String.raw`$\dim\mathrm{Ker}\,T=2$` },
      ],
      correctId: "a",
      explanation: String.raw`$\dim\mathbb{R}_1[x]=2$, ולכן $\dim\mathrm{Im}\,T\le2<4=\dim\mathbb{R}^4$ ו-$T$ לא על. היא יכולה להיות חח״ע (למשל $T(a+bx)=(a,b,0,0)$), ולכן ב' לא בהכרח. ג' שגויה, ו-ד' לא נובעת מהנתונים (עבור הדוגמה החח״עית $\dim\mathrm{Ker}\,T=0$).`,
      recap: "תחום קטן מהטווח: לא על." },
    { id: "C05-Q4",
      question: String.raw`$T:\mathbb{R}_3[x]\to\mathbb{R}^3$ עם $\dim\mathrm{Ker}\,T=2$ ו-$\dim\mathrm{Im}\,T=2$. מה נכון?`,
      options: [
        { id: "a", value: String.raw`$T$ לא חח״ע ולא על` },
        { id: "b", value: String.raw`$T$ חח״ע ולא על` },
        { id: "c", value: String.raw`$T$ לא חח״ע אבל על` },
        { id: "d", value: String.raw`$T$ חח״ע ועל` },
      ],
      correctId: "a",
      explanation: String.raw`$\dim\mathrm{Ker}\,T=2\neq0$, ולכן לא חח״ע. $\dim\mathrm{Im}\,T=2\neq3=\dim\mathbb{R}^3$, ולכן לא על. כל אחת מהאפשרויות האחרות סותרת לפחות אחת משתי ההשוואות.`,
      recap: "חח״ע: Ker. על: Im מול מימד הטווח." },
    { id: "C05-Q5",
      question: String.raw`$\dim\mathrm{Im}\,T=2$ ו-$\dim W=3$. איזה נימוק מוכיח ש-$T$ לא על?`,
      options: [
        { id: "a", value: String.raw`$\dim\mathrm{Im}\,T=2<3=\dim W$` },
        { id: "b", value: String.raw`$\dim\mathrm{Ker}\,T\neq0$` },
        { id: "c", value: String.raw`$\dim\mathrm{Im}\,T\neq\dim V$` },
        { id: "d", value: String.raw`$T$ לא חח״ע` },
      ],
      correctId: "a",
      explanation: String.raw`״על״ נקבע מהשוואת התמונה למימד הטווח. ב' ו-ד' מנמקות אי-חח״עיות, שלא גוררת אי-על כשמימדי התחום והטווח שונים. ג' משווה את התמונה לתחום, וזו לא ההשוואה הנכונה.`,
      recap: "על: משווים ל-$\\dim W$." },
    { id: "C05-Q6",
      step: { type: "numeric",
        prompt: String.raw`$T:M_{2\times2}(\mathbb{R})\to\mathbb{R}_3[x]$ לינארית וחח״ע. מהו $\dim\mathrm{Im}\,T$ ?`,
        answer: 4, tol: 0,
        explain: String.raw`חח״ע: $\dim\mathrm{Ker}\,T=0$, ולכן $\dim\mathrm{Im}\,T=\dim M_{2\times2}(\mathbb{R})-0=4$. מכיוון ש-$\dim\mathbb{R}_3[x]=4$ ההעתקה גם על.` },
      recap: "חח״ע: התמונה במימד התחום." },
    { bankId: "24A-A-Q5b", recap: "חח״ע לפי הגרעין, על לפי התמונה מול הטווח, עם ההשוואה במפורש." },
  ],
});
