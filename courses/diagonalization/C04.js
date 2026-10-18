/* diagonalization, level 4: eigenvalues of 3x3 matrices */
COURSE_LEVEL("diagonalization", {
  id: "C04", order: 4, icon: "🧊", title: "ערכים עצמיים של מטריצה 3×3",
  goal: "למצוא ערכים עצמיים ב-$3\\times3$ בעזרת פיתוח לפי שורה או עמודה עם אפסים, ולבדוק עם עקבה ודטרמיננטה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>ב-$3\times3$ הפולינום האופייני ממעלה שלישית, ולכן הדטרמיננטה צריכה פיתוח. הטריק: מפתחים לפי שורה או עמודה שבה כמעט הכול אפס, וכך הפולינום כבר מגיע מפורק חלקית.</p>
<div class="lesson-rule">🔑 <b>משולשית</b> (מעל האלכסון או מתחתיו אפסים): הערכים העצמיים הם איברי האלכסון. <b>שורה או עמודה עם איבר אחד</b> שאינו אפס: מפתחים לפיה, ונשארת דטרמיננטה $2\times2$.</div>
<div class="lesson-ex">דוגמה: $B=\begin{pmatrix}3&1&0\\2&2&0\\5&7&6\end{pmatrix}$. בעמודה 3 רק האיבר $6$ שונה מאפס, ולכן $p(\lambda)=(\lambda-6)\cdot\det\begin{pmatrix}\lambda-3&-1\\-2&\lambda-2\end{pmatrix}=(\lambda-6)(\lambda^2-5\lambda+4)=(\lambda-6)(\lambda-1)(\lambda-4)$.
הערכים העצמיים: $6,1,4$. בדיקה: הסכום $11$ שווה לעקבה $3+2+6$, והמכפלה $24$ שווה ל-$\det B$.</div>
<ul>
<li>הסכום של הערכים העצמיים (עם ריבוי) הוא $\mathrm{Tr}B$, והמכפלה שלהם היא $\det B$.</li>
<li>שורש כפול נספר פעמיים. למשל $(\lambda-3)^2(\lambda-5)$ אומר שהערכים הם $3,3,5$.</li>
</ul>
<div class="lesson-trap">⚠️ אחרי פיתוח לפי איבר באמצע, זכרו את סימן המקום $(-1)^{i+j}$. כשהאיבר על האלכסון, הסימן הוא $+$.</div>
` },
  questions: [
    { id: "C04-Q1",
      question: String.raw`מהם הערכים העצמיים (עם ריבוי) של $\begin{pmatrix}2&5&7\\0&3&1\\0&0&3\end{pmatrix}$ ?`,
      options: [
        { id: "a", value: String.raw`$2,\ 3,\ 3$` },
        { id: "b", value: String.raw`$2,\ 5,\ 7$` },
        { id: "c", value: String.raw`$2,\ 3$ בלבד, כל אחד פעם אחת` },
        { id: "d", value: String.raw`$5,\ 1,\ 7$` },
      ],
      correctId: "a",
      explanation: String.raw`המטריצה משולשית עליונה, ולכן הערכים העצמיים הם איברי האלכסון $2,3,3$, והערך $3$ מופיע פעמיים. אפשרות $2,\ 5,\ 7$ לוקחת את השורה הראשונה, ואפשרות $5,\ 1,\ 7$ את האיברים שמעל האלכסון. אפשרות "$2,\ 3$ בלבד, כל אחד פעם אחת" שוכחת את הריבוי.`,
      recap: "משולשית: הערכים העצמיים הם האלכסון, עם ריבוי." },
    { id: "C04-Q2",
      step: { type: "numeric",
        prompt: String.raw`מהו הערך העצמי הגדול ביותר של $B=\begin{pmatrix}1&0&0\\4&5&2\\0&2&5\end{pmatrix}$ ? (רמז: פתחו לפי שורה 1.)`,
        answer: 7, tol: 0,
        explain: String.raw`$p(\lambda)=(\lambda-1)\det\begin{pmatrix}\lambda-5&-2\\-2&\lambda-5\end{pmatrix}=(\lambda-1)\left((\lambda-5)^2-4\right)=(\lambda-1)(\lambda-3)(\lambda-7)$. הערכים הם $1,3,7$, והגדול $7$.` },
      recap: "שורה עם איבר אחד: מפתחים לפיה." },
    { id: "C04-Q3",
      question: String.raw`מהו הפולינום האופייני של $B=\begin{pmatrix}6&0&2\\0&3&0\\2&0&6\end{pmatrix}$ ?`,
      options: [
        { id: "a", value: String.raw`$(\lambda-3)(\lambda-4)(\lambda-8)$` },
        { id: "b", value: String.raw`$(\lambda-3)(\lambda-6)^2$` },
        { id: "c", value: String.raw`$(\lambda-3)(\lambda-2)(\lambda-8)$` },
        { id: "d", value: String.raw`$(\lambda-3)(\lambda+4)(\lambda+8)$` },
      ],
      correctId: "a",
      explanation: String.raw`בשורה 2 רק האיבר $3$ שונה מאפס, ולכן $p=(\lambda-3)\left((\lambda-6)^2-4\right)=(\lambda-3)(\lambda-4)(\lambda-8)$. אפשרות $(\lambda-3)(\lambda-6)^2$ לוקחת את האלכסון כאילו המטריצה משולשית, אבל היא לא. אפשרות $(\lambda-3)(\lambda-2)(\lambda-8)$ טועה ב-$(\lambda-6)^2-4=\lambda^2-12\lambda+32$ שהשורשים שלו $4,8$ ולא $2,8$. באפשרות $(\lambda-3)(\lambda+4)(\lambda+8)$ הסימנים הפוכים.`,
      recap: "ממשיכים לפרק את ה-2×2 שנשאר." },
    { id: "C04-Q4",
      step: { type: "numeric",
        prompt: String.raw`לערכים העצמיים של $B=\begin{pmatrix}6&0&2\\0&3&0\\2&0&6\end{pmatrix}$ שניים הם $3$ ו-$4$. מהו השלישי? (רמז: העקבה.)`,
        answer: 8, tol: 0,
        explain: String.raw`העקבה היא $6+3+6=15$ ושווה לסכום הערכים העצמיים: $3+4+\mu=15$, ולכן $\mu=8$.` },
      recap: "סכום הערכים העצמיים = העקבה." },
    { id: "C04-Q5",
      step: { type: "numeric",
        prompt: String.raw`הערכים העצמיים של $B=\begin{pmatrix}6&0&2\\0&3&0\\2&0&6\end{pmatrix}$ הם $3,4,8$. מהי $\det B$ ?`,
        answer: 96, tol: 0,
        explain: String.raw`הדטרמיננטה היא מכפלת הערכים העצמיים: $3\cdot4\cdot8=96$. בדיקה ישירה: $3\cdot(36-4)=96$.` },
      recap: "דטרמיננטה = מכפלת הערכים העצמיים." },
    { id: "C04-Q6",
      step: { type: "findbug",
        prompt: String.raw`בפתרון הבא של הערכים העצמיים של $M=\begin{pmatrix}2&0&1\\0&5&0\\1&0&2\end{pmatrix}$ שורה אחת שגויה. סמנו אותה.`,
        lines: [
          String.raw`מפתחים לפי שורה 2: $p(\lambda)=(\lambda-5)\cdot\det\begin{pmatrix}\lambda-2&-1\\-1&\lambda-2\end{pmatrix}$`,
          String.raw`הדטרמיננטה הקטנה: $(\lambda-2)^2-1$`,
          String.raw`$(\lambda-2)^2-1=\lambda^2-4\lambda+5$`,
          String.raw`$\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$`,
          String.raw`הערכים העצמיים: $5,\ 1,\ 3$`,
        ],
        bugIndex: 2,
        explain: String.raw`$(\lambda-2)^2-1=\lambda^2-4\lambda+4-1=\lambda^2-4\lambda+3$, ולא $+5$. רק ל-$\lambda^2-4\lambda+3$ יש הפירוק בשורה הבאה.` },
      recap: "זהירות עם הריבוע: (λ−2)² = λ²−4λ+4." },
  ],
});
