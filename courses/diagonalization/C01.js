/* diagonalization, level 1: eigenvector and eigenvalue */
COURSE_LEVEL("diagonalization", {
  id: "C01", order: 1, icon: "🧭", title: "וקטור עצמי וערך עצמי",
  goal: "לבדוק אם וקטור הוא וקטור עצמי של מטריצה, ולמצוא את הערך העצמי שלו.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>מטריצה $A$ מזיזה וקטורים. רוב הוקטורים משנים כיוון, אבל לפעמים וקטור $\vec v$ רק נמתח או מתכווץ: $A\vec v$ הוא כפולה של $\vec v$.</p>
<div class="lesson-rule">🔑 <b>הגדרה:</b> $\vec v\neq\vec 0$ הוא <b>וקטור עצמי</b> של $A$ עם <b>ערך עצמי</b> $\lambda$ אם $A\vec v=\lambda\vec v$.</div>
<p>הבדיקה היא חישוב אחד: מכפילים $A\vec v$ ובודקים אם התוצאה היא כפולה של $\vec v$. אם כן, הכפולה היא $\lambda$.</p>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ ו-$\vec v=(1,1)^T$. מתקבל $A\vec v=(5,5)^T=5\vec v$, ולכן $\vec v$ וקטור עצמי עם $\lambda=5$.
לעומת זאת $\vec u=(1,0)^T$ נותן $A\vec u=(4,2)^T$, וזו אינה כפולה של $\vec u$, ולכן $\vec u$ אינו וקטור עצמי.</div>
<ul>
<li>וקטור האפס <b>אינו</b> וקטור עצמי, גם אם $A\vec 0=\lambda\vec 0$ לכל $\lambda$.</li>
<li>כל כפולה שונה מאפס של וקטור עצמי היא גם וקטור עצמי, עם אותו $\lambda$.</li>
<li>ערך עצמי יכול להיות גם $0$ או שלילי.</li>
</ul>
<div class="lesson-trap">⚠️ כפולה צריכה להיות <b>אותו</b> מספר בכל הרכיבים. התוצאה $(5,3)^T$ מ-$(1,1)^T$ אינה כפולה שלו.</div>
` },
  questions: [
    { id: "C01-Q1",
      question: String.raw`נתונה $A=\begin{pmatrix}3&1\\0&2\end{pmatrix}$. איזה מהוקטורים הבאים הוא וקטור עצמי של $A$?`,
      options: [
        { id: "a", value: String.raw`$(1,0)^T$` },
        { id: "b", value: String.raw`$(0,1)^T$` },
        { id: "c", value: String.raw`$(1,1)^T$` },
        { id: "d", value: String.raw`$(1,2)^T$` },
      ],
      correctId: "a",
      explanation: String.raw`$A(1,0)^T=(3,0)^T=3\,(1,0)^T$, ולכן אפשרות א' נכונה עם $\lambda=3$. בשאר: $A(0,1)^T=(1,2)^T$, $A(1,1)^T=(4,2)^T$ ו-$A(1,2)^T=(5,4)^T$, ואף אחד מהם אינו כפולה של הווקטור המקורי.`,
      recap: "מחשבים Av ובודקים אם זו כפולה של v." },
    { id: "C01-Q2",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ ו-$\vec v=(1,1)^T$ הוא וקטור עצמי של $A$. מהו הערך העצמי שלו?`,
        answer: 5, tol: 0,
        explain: String.raw`$A\vec v=(4+1,\ 2+3)^T=(5,5)^T=5\vec v$, ולכן $\lambda=5$.` },
      recap: "הערך העצמי הוא הכפולה: Av = λv." },
    { id: "C01-Q3",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ ו-$\vec v=(1,-1)^T$ הוא וקטור עצמי של $A$. מהו הערך העצמי שלו?`,
        answer: -1, tol: 0,
        explain: String.raw`$A\vec v=(1-2,\ 2-1)^T=(-1,1)^T=-1\cdot\vec v$, ולכן $\lambda=-1$. ערך עצמי יכול להיות שלילי.` },
      recap: "ערך עצמי יכול להיות שלילי." },
    { id: "C01-Q4",
      question: String.raw`נתונה $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ והוקטור $\vec v=(1,2)^T$. איזו טענה נכונה?`,
      options: [
        { id: "a", value: String.raw`$\vec v$ אינו וקטור עצמי, כי $A\vec v=(4,6)^T$ אינו כפולה של $\vec v$` },
        { id: "b", value: String.raw`$\vec v$ וקטור עצמי עם $\lambda=4$` },
        { id: "c", value: String.raw`$\vec v$ וקטור עצמי עם $\lambda=6$` },
        { id: "d", value: String.raw`$\vec v$ וקטור עצמי עם $\lambda=2$` },
      ],
      correctId: "a",
      explanation: String.raw`$A\vec v=(2+2,\ 0+6)^T=(4,6)^T$. הרכיב הראשון מרמז על כפולה $4$, והשני על כפולה $3$, ולכן אין כפולה אחת. הערכים $4$ ו-$6$ נראים כמו $\lambda$ אבל כל אחד מתאים לרכיב אחד בלבד, ו-$\lambda=2$ נותן $(2,4)^T$.`,
      recap: "כפולה אחת לכל הרכיבים, אחרת זה לא וקטור עצמי." },
    { id: "C01-Q5",
      step: { type: "numeric",
        prompt: String.raw`$\vec v=(1,1)^T$ וקטור עצמי של $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ עם $\lambda=5$. מהו הרכיב הראשון של $A\,(2\vec v)$?`,
        answer: 10, tol: 0,
        explain: String.raw`$2\vec v=(2,2)^T$ גם הוא וקטור עצמי עם $\lambda=5$, ולכן $A(2\vec v)=5\cdot(2,2)^T=(10,10)^T$. הרכיב הראשון הוא $10$.` },
      recap: "כפולה שונה מאפס של וקטור עצמי היא וקטור עצמי." },
  ],
});
