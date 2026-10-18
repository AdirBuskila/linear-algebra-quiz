/* diagonalization, level 7: short proofs about eigenvalues and eigenvectors */
COURSE_LEVEL("diagonalization", {
  id: "C07", order: 7, icon: "✍️", title: "הוכחות קצרות על ערכים ווקטורים עצמיים",
  goal: "לבנות הוכחות קצרות מההגדרה $A\\vec v=\\lambda\\vec v$: חזקות, צירופים והופכית.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כל ההוכחות בנושא מתחילות מאותה נקודה: ההגדרה $A\vec v=\lambda\vec v$, ופעולה שמבצעים על שני האגפים.</p>
<div class="lesson-rule">🔑 <b>מתכון:</b> (1) כותבים מה נתון, $A\vec v=\lambda\vec v$ עם $\vec v\neq\vec 0$. (2) מפעילים פעולה על שני האגפים (כפל במטריצה, בסקלר, חיבור). (3) מגיעים לצורה $M\vec x=\mu\vec x$ עבור מטריצה $M$ כלשהי. (4) מוודאים ש-$\vec x\neq\vec 0$.</div>
<div class="lesson-ex">דוגמה: אם $A\vec v=\lambda\vec v$ אז $A^2\vec v=A(\lambda\vec v)=\lambda A\vec v=\lambda^2\vec v$. לכן $\vec v$ וקטור עצמי של $A^2$ עם הערך $\lambda^2$.</div>
<ul>
<li><b>צירוף לאותו $\lambda$:</b> $A(c\vec v+d\vec w)=c\lambda\vec v+d\lambda\vec w=\lambda(c\vec v+d\vec w)$. כשהצירוף שונה מאפס, זהו וקטור עצמי.</li>
<li><b>ערכים שונים:</b> $\vec v,\vec w$ הם וקטורים עצמיים ל-$\lambda_1\neq\lambda_2$, ולכן הם בלתי תלויים. הצירוף $\vec v+\vec w$ נותן $\lambda_1\vec v+\lambda_2\vec w$, שאינו כפולה של $\vec v+\vec w$.</li>
<li><b>הופכית:</b> אם $B\vec x=\lambda\vec x$ ו-$B$ הפיכה אז $\lambda\neq0$, ו-$B^{-1}\vec x=\tfrac1\lambda\vec x$.</li>
<li><b>דמיון:</b> מ-$PA=BP$ ו-$A\vec x=\lambda\vec x$ מקבלים $B(P\vec x)=\lambda(P\vec x)$.</li>
</ul>
<div class="lesson-trap">⚠️ סיום ההוכחה דורש $\vec x\neq\vec 0$. מכפלה בהפיכה לא מאפסת וקטור שאינו אפס, אבל מכפלה בכל מטריצה שהיא עלולה.</div>
` },
  questions: [
    { id: "C07-Q1",
      step: { type: "order",
        prompt: String.raw`סדרו את שורות ההוכחה ש-$\vec v$ וקטור עצמי של $A^2$ אם $A\vec v=\lambda\vec v$.`,
        lines: [
          String.raw`$A\vec v=\lambda\vec v$`,
          String.raw`$A(A\vec v)=A(\lambda\vec v)$`,
          String.raw`$A^2\vec v=\lambda(A\vec v)$`,
          String.raw`$A^2\vec v=\lambda\cdot\lambda\vec v=\lambda^2\vec v$`,
        ],
        explain: String.raw`מפעילים $A$ על שני האגפים, מוציאים את הסקלר $\lambda$ החוצה, ואז מציבים שוב $A\vec v=\lambda\vec v$. כל שורה נובעת מהקודמת.` },
      recap: "מפעילים A על שני האגפים ומציבים שוב." },
    { id: "C07-Q2",
      question: String.raw`$\vec v,\vec w$ בלתי תלויים, ושניהם וקטורים עצמיים של $A$ עם אותו ערך עצמי $3$. מה נכון לגבי $2\vec v+5\vec w$ ?`,
      options: [
        { id: "a", value: String.raw`וקטור עצמי של $A$ עם ערך עצמי $3$` },
        { id: "b", value: String.raw`וקטור עצמי של $A$ עם ערך עצמי $2\cdot3+5\cdot3=21$` },
        { id: "c", value: String.raw`אינו וקטור עצמי של $A$` },
        { id: "d", value: String.raw`וקטור עצמי של $A$ עם ערך עצמי $7$` },
      ],
      correctId: "a",
      explanation: String.raw`$A(2\vec v+5\vec w)=2\cdot3\vec v+5\cdot3\vec w=3(2\vec v+5\vec w)$. הצירוף שונה מאפס כי $\vec v,\vec w$ בלתי תלויים, ולכן זה וקטור עצמי עם $\lambda=3$. הערך לא משתנה בצירוף: אפשרות "וקטור עצמי של $A$ עם ערך עצמי $2\cdot3+5\cdot3=21$" מכפילה את הערך במקדמים, ואפשרות "וקטור עצמי של $A$ עם ערך עצמי $7$" מחברת אותם.`,
      recap: "צירוף לאותו λ נשאר וקטור עצמי עם אותו λ." },
    { id: "C07-Q3",
      question: String.raw`$A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, $\vec v=(1,0)^T$ ($\lambda=1$) ו-$\vec w=(0,1)^T$ ($\lambda=2$). האם $\vec v+\vec w$ וקטור עצמי של $A$ ?`,
      options: [
        { id: "a", value: String.raw`לא, כי $A(\vec v+\vec w)=(1,2)^T$ אינו כפולה של $(1,1)^T$` },
        { id: "b", value: String.raw`כן, עם $\lambda=1$` },
        { id: "c", value: String.raw`כן, עם $\lambda=3$` },
        { id: "d", value: String.raw`כן, עם $\lambda=2$` },
      ],
      correctId: "a",
      explanation: String.raw`$A(\vec v+\vec w)=1\cdot\vec v+2\cdot\vec w=(1,2)^T$. בשביל להיות כפולה של $(1,1)^T$ היו צריכים שני הרכיבים להיות שווים, ולכן זה לא וקטור עצמי. ערכים עצמיים שונים לא מתערבבים.`,
      recap: "צירוף לערכים שונים אינו וקטור עצמי." },
    { id: "C07-Q4",
      step: { type: "numeric",
        prompt: String.raw`$B=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ הפיכה ו-$\vec x=(1,1)^T$ וקטור עצמי שלה עם $\lambda=4$. מהו הערך העצמי של $B^{-1}$ המתאים ל-$\vec x$ ?`,
        answer: 0.25, tol: 0,
        explain: String.raw`מ-$B\vec x=4\vec x$ מכפילים ב-$B^{-1}$ ומקבלים $\vec x=4B^{-1}\vec x$, כלומר $B^{-1}\vec x=\tfrac14\vec x$. הערך הוא $\tfrac14=0.25$.` },
      recap: "ערך עצמי של $B^{-1}$ הוא $1/\\lambda$." },
    { id: "C07-Q5",
      step: { type: "findbug",
        prompt: String.raw`בהוכחה ש-$\lambda$ ערך עצמי של $B$ כאשר $PA=BP$, $P$ הפיכה ו-$A\vec x=\lambda\vec x$ שורה אחת שגויה. סמנו אותה.`,
        lines: [
          String.raw`נתון $A\vec x=\lambda\vec x$ ו-$PA=BP$`,
          String.raw`$B(P\vec x)=(BP)\vec x$`,
          String.raw`$(BP)\vec x=(AP)\vec x$`,
          String.raw`$(PA)\vec x=P(A\vec x)=\lambda P\vec x$`,
          String.raw`$P\vec x\neq\vec 0$ כי $P$ הפיכה, ולכן $\lambda$ ערך עצמי של $B$`,
        ],
        bugIndex: 2,
        explain: String.raw`נתון $BP=PA$ ולא $BP=AP$. בדרך כלל $AP\neq PA$, כי כפל מטריצות אינו חילופי. השורה הנכונה היא $(BP)\vec x=(PA)\vec x$.` },
      recap: "לא להחליף סדר בכפל מטריצות." },
    { id: "C07-Q6",
      question: String.raw`בהוכחה הקודמת, מדוע $P\vec x\neq\vec 0$ ?`,
      options: [
        { id: "a", value: String.raw`כי $P$ הפיכה ו-$\vec x\neq\vec 0$, ולכן $P\vec x=\vec 0$ רק עבור $\vec x=\vec 0$` },
        { id: "b", value: String.raw`כי $P$ סימטרית` },
        { id: "c", value: String.raw`כי $\lambda\neq0$` },
        { id: "d", value: String.raw`כי $A$ הפיכה` },
      ],
      correctId: "a",
      explanation: String.raw`אם $P\vec x=\vec 0$ אז $\vec x=P^{-1}\vec 0=\vec 0$, בסתירה לכך ש-$\vec x$ וקטור עצמי. סימטריה, $\lambda\neq0$ והפיכות של $A$ אינן רלוונטיות: למשל $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ סימטרית ומאפסת את $(1,-1)^T$.`,
      recap: "הפיכה לא מאפסת וקטור שאינו אפס." },
  ],
});
