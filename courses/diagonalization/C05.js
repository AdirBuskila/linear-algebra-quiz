/* diagonalization, level 5: algebraic and geometric multiplicity, the diagonalizability criterion */
COURSE_LEVEL("diagonalization", {
  id: "C05", order: 5, icon: "⚖️", title: "ריבוי אלגברי וגיאומטרי: מתי מלכסנים",
  goal: "לחשב ריבוי אלגברי וגיאומטרי ולקבוע אם מטריצה ניתנת לליכסון.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>מטריצה $A$ מסדר $n$ ניתנת לליכסון אם קיימת $P$ הפיכה ו-$D$ אלכסונית עם $AP=PD$. זה אפשרי רק כשיש $n$ וקטורים עצמיים בלתי תלויים, כי הם העמודות של $P$.</p>
<ul>
<li><b>ריבוי אלגברי</b> של $\lambda$: כמה פעמים $\lambda$ שורש של $p(\lambda)$.</li>
<li><b>ריבוי גיאומטרי</b> של $\lambda$: מימד המרחב העצמי, כלומר $n-\mathrm{rank}(\lambda I-A)$.</li>
<li>תמיד $1\le$ גיאומטרי $\le$ אלגברי.</li>
</ul>
<div class="lesson-rule">🔑 <b>קריטריון:</b> $A$ ניתנת לליכסון אם ורק אם לכל ערך עצמי הריבוי הגיאומטרי שווה לאלגברי. מקרה פרטי נוח: $n$ ערכים עצמיים שונים תמיד מבטיחים ליכסון.</div>
<div class="lesson-ex">דוגמה: $\begin{pmatrix}1&1\\0&1\end{pmatrix}$. הערך $1$ כפול (אלגברי 2), אבל $I-A=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$ מדרגה 1, ולכן הגיאומטרי הוא $2-1=1$. אין שני וקטורים עצמיים בלתי תלויים, ולכן <b>לא</b> ניתנת לליכסון.
לעומת זאת $\begin{pmatrix}2&0\\0&2\end{pmatrix}$: $2I-A=0$ מדרגה 0, הגיאומטרי $2$, ולכן אלכסונית כבר עכשיו.</div>
<div class="lesson-trap">⚠️ ערך עצמי כפול לא אומר שאי אפשר ללכסן, וגם לא שאפשר. חייבים לבדוק את המימד של המרחב העצמי.</div>
` },
  questions: [
    { id: "C05-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהו הריבוי האלגברי של הערך העצמי $3$ במטריצה $A=\begin{pmatrix}3&1&0\\0&3&0\\0&0&5\end{pmatrix}$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`המטריצה משולשית, ולכן $p(\lambda)=(\lambda-3)^2(\lambda-5)$. הערך $3$ שורש כפול, ולכן הריבוי האלגברי $2$.` },
      recap: "ריבוי אלגברי = ריבוי השורש ב-p." },
    { id: "C05-Q2",
      step: { type: "numeric",
        prompt: String.raw`מהו הריבוי הגיאומטרי של הערך העצמי $3$ במטריצה $A=\begin{pmatrix}3&1&0\\0&3&0\\0&0&5\end{pmatrix}$ ?`,
        answer: 1, tol: 0,
        explain: String.raw`$3I-A=\begin{pmatrix}0&-1&0\\0&0&0\\0&0&-2\end{pmatrix}$ מדרגה $2$, ולכן המימד הוא $3-2=1$.` },
      recap: "גיאומטרי = n − דרגה של λI−A." },
    { id: "C05-Q3",
      question: String.raw`האם $A=\begin{pmatrix}3&1&0\\0&3&0\\0&0&5\end{pmatrix}$ ניתנת לליכסון?`,
      options: [
        { id: "a", value: String.raw`לא, כי לערך $3$ הריבוי הגיאומטרי $1$ קטן מהאלגברי $2$` },
        { id: "b", value: String.raw`כן, כי יש לה ערך עצמי כפול` },
        { id: "c", value: String.raw`כן, כי היא משולשית` },
        { id: "d", value: String.raw`לא, כי יש לה ערך עצמי כפול` },
      ],
      correctId: "a",
      explanation: String.raw`לליכסון נדרש שבכל ערך עצמי הגיאומטרי יהיה שווה לאלגברי. כאן $1<2$ עבור $\lambda=3$, ולכן לא ניתנת. אפשרויות ב' ו-ד' קובעות לפי עצם הכפילות, וזה לא מספיק לאף כיוון. אפשרות ג': משולשית מגלה את הערכים העצמיים, לא את המימדים.`,
      recap: "בודקים גיאומטרי = אלגברי לכל ערך עצמי." },
    { id: "C05-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהו הריבוי הגיאומטרי של הערך העצמי $2$ במטריצה $A=\begin{pmatrix}2&0&0\\0&2&0\\1&0&5\end{pmatrix}$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`$2I-A=\begin{pmatrix}0&0&0\\0&0&0\\-1&0&-3\end{pmatrix}$ מדרגה $1$, ולכן הגיאומטרי $3-1=2$. זה שווה לריבוי האלגברי $2$.` },
      recap: "דרגה קטנה = מרחב עצמי גדול." },
    { id: "C05-Q5",
      question: String.raw`האם $A=\begin{pmatrix}2&0&0\\0&2&0\\1&0&5\end{pmatrix}$ ניתנת לליכסון?`,
      options: [
        { id: "a", value: String.raw`כן, כי לכל ערך עצמי הריבוי הגיאומטרי שווה לאלגברי` },
        { id: "b", value: String.raw`לא, כי היא אינה אלכסונית` },
        { id: "c", value: String.raw`לא, כי הערך $2$ כפול` },
        { id: "d", value: String.raw`כן, כי כל המטריצה מסדר 3 ניתנת לליכסון` },
      ],
      correctId: "a",
      explanation: String.raw`הערך $2$: אלגברי 2, גיאומטרי 2. הערך $5$: אלגברי 1, גיאומטרי 1. שניהם שווים, ולכן ניתנת לליכסון. אפשרות ב' מבלבלת בין "ניתנת לליכסון" ל"כבר אלכסונית". אפשרות ג' כבר ראינו שאינה מספיקה. אפשרות ד' שגויה: למשל $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ לא ניתנת.`,
      recap: "ערך כפול עם מרחב עצמי מלא לא מפריע." },
    { id: "C05-Q6",
      question: String.raw`איזו מהמטריצות הבאות אינה ניתנת לליכסון?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}5&1\\0&5\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}5&0\\0&5\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}5&1\\0&6\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}0&1\\1&0\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`באפשרות א' הערך $5$ כפול והמטריצה $5I-A=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$ מדרגה 1, ולכן גיאומטרי 1<2. ב' אלכסונית. ג' יש שני ערכים עצמיים שונים, $5$ ו-$6$. ד' הערכים העצמיים $1$ ו-$-1$ שונים.`,
      recap: "שני ערכים שונים (ב-2×2) מבטיחים ליכסון." },
  ],
});
