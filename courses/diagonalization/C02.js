/* diagonalization, level 2: the characteristic polynomial of a 2x2 matrix */
COURSE_LEVEL("diagonalization", {
  id: "C02", order: 2, icon: "🧮", title: "פולינום אופייני ל-2×2",
  goal: "למצוא ערכים עצמיים של מטריצה מסדר 2 מהפולינום האופייני.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>איך מוצאים את $\lambda$ בלי לנחש וקטור? $A\vec v=\lambda\vec v$ שקול ל-$(\lambda I-A)\vec v=\vec 0$. למערכת הומוגנית יש פתרון שונה מאפס בדיוק כאשר המטריצה לא הפיכה, כלומר הדטרמיננטה שלה אפס.</p>
<div class="lesson-rule">🔑 <b>פולינום אופייני:</b> $p(\lambda)=\det(\lambda I-A)$. הערכים העצמיים הם <b>השורשים</b> של $p$.</div>
<p>במטריצה $2\times2$ יש קיצור: $p(\lambda)=\lambda^2-(\mathrm{Tr}A)\,\lambda+\det A$, כאשר $\mathrm{Tr}A$ הוא סכום האלכסון. לכן סכום הערכים העצמיים הוא $\mathrm{Tr}A$ ומכפלתם $\det A$.</p>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$. העקבה $7$ והדטרמיננטה $12-2=10$, ולכן $p(\lambda)=\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)$.
הערכים העצמיים: $2$ ו-$5$. בדיקה: $2+5=7$ ו-$2\cdot5=10$.</div>
<div class="lesson-trap">⚠️ את הדטרמיננטה מחשבים כ-$ad-bc$ עם מינוס. טעות בסימן נותנת פולינום אחר לגמרי.</div>
` },
  questions: [
    { id: "C02-Q1",
      question: String.raw`מהו הפולינום האופייני של $A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ ?`,
      options: [
        { id: "a", value: String.raw`$\lambda^2-5\lambda+4$` },
        { id: "b", value: String.raw`$\lambda^2+5\lambda+4$` },
        { id: "c", value: String.raw`$\lambda^2-5\lambda+8$` },
        { id: "d", value: String.raw`$\lambda^2-4\lambda+5$` },
      ],
      correctId: "a",
      explanation: String.raw`העקבה $3+2=5$ והדטרמיננטה $3\cdot2-1\cdot2=4$, ולכן $\lambda^2-5\lambda+4$. אפשרות $\lambda^2+5\lambda+4$ הופכת את סימן העקבה. אפשרות $\lambda^2-5\lambda+8$ מחשבת $3\cdot2+1\cdot2=8$, כלומר מחברת במקום לחסר. אפשרות $\lambda^2-4\lambda+5$ מחליפה בין העקבה לדטרמיננטה.`,
      recap: "p(λ) = λ² − עקבה·λ + דטרמיננטה." },
    { id: "C02-Q2",
      question: String.raw`מהם הערכים העצמיים של $A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ ?`,
      options: [
        { id: "a", value: String.raw`$1$ ו-$4$` },
        { id: "b", value: String.raw`$-1$ ו-$-4$` },
        { id: "c", value: String.raw`$2$ ו-$3$` },
        { id: "d", value: String.raw`$1$ ו-$5$` },
      ],
      correctId: "a",
      explanation: String.raw`$\lambda^2-5\lambda+4=(\lambda-1)(\lambda-4)$, ולכן $\lambda=1,4$. בדיקה: הסכום $5$ הוא העקבה והמכפלה $4$ היא הדטרמיננטה. אפשרות "$-1$ ו-$-4$" היא הסימנים ההפוכים של השורשים. אפשרות "$2$ ו-$3$" לוקחת את איברי האלכסון, שאינם הערכים העצמיים כשהמטריצה אינה משולשית. באפשרות "$1$ ו-$5$" המכפלה היא $5$ ולא $4$.`,
      recap: "שורשי הפולינום האופייני הם הערכים העצמיים." },
    { id: "C02-Q3",
      step: { type: "numeric",
        prompt: String.raw`מהו הערך העצמי הגדול של $A=\begin{pmatrix}5&2\\2&5\end{pmatrix}$ ?`,
        answer: 7, tol: 0,
        explain: String.raw`העקבה $10$ והדטרמיננטה $25-4=21$. מחפשים שני מספרים עם סכום $10$ ומכפלה $21$: $\lambda^2-10\lambda+21=(\lambda-3)(\lambda-7)$. הגדול הוא $7$.` },
      recap: "סכום = עקבה, מכפלה = דטרמיננטה." },
    { id: "C02-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהי מכפלת שני הערכים העצמיים של $A=\begin{pmatrix}1&4\\2&3\end{pmatrix}$ ?`,
        answer: -5, tol: 0,
        explain: String.raw`המכפלה שווה ל-$\det A=1\cdot3-4\cdot2=-5$. אפשר לאמת: $\lambda^2-4\lambda-5=(\lambda-5)(\lambda+1)$, והמכפלה $5\cdot(-1)=-5$.` },
      recap: "מכפלת הערכים העצמיים = הדטרמיננטה." },
    { id: "C02-Q5",
      step: { type: "order",
        prompt: String.raw`סדרו את מציאת הערכים העצמיים של $A=\begin{pmatrix}1&2\\3&2\end{pmatrix}$.`,
        lines: [
          String.raw`כותבים $\lambda I-A=\begin{pmatrix}\lambda-1&-2\\-3&\lambda-2\end{pmatrix}$`,
          String.raw`מחשבים את הדטרמיננטה: $(\lambda-1)(\lambda-2)-6$`,
          String.raw`מפשטים: $\lambda^2-3\lambda-4$`,
          String.raw`מפרקים: $(\lambda-4)(\lambda+1)$, ולכן $\lambda=4$ או $\lambda=-1$`,
        ],
        explain: String.raw`קודם בונים את $\lambda I-A$, אחר כך לוקחים דטרמיננטה, מפשטים ורק בסוף מוצאים שורשים. הסכום $4+(-1)=3$ הוא העקבה, והמכפלה $-4$ היא הדטרמיננטה $2-6$.` },
      recap: "בונים λI−A, דטרמיננטה, מפשטים, מפרקים." },
    { id: "C02-Q6",
      step: { type: "findbug",
        prompt: String.raw`בפתרון הבא של הערכים העצמיים של $A=\begin{pmatrix}2&1\\4&5\end{pmatrix}$ שורה אחת שגויה. סמנו אותה.`,
        lines: [
          String.raw`$\lambda I-A=\begin{pmatrix}\lambda-2&-1\\-4&\lambda-5\end{pmatrix}$`,
          String.raw`$p(\lambda)=(\lambda-2)(\lambda-5)-4$`,
          String.raw`$p(\lambda)=\lambda^2-7\lambda+14$`,
          String.raw`$p(\lambda)=(\lambda-1)(\lambda-6)$`,
        ],
        bugIndex: 2,
        explain: String.raw`$(\lambda-2)(\lambda-5)=\lambda^2-7\lambda+10$, ואחרי החסרת $4$ מתקבל $\lambda^2-7\lambda+6$ ולא $+14$. רק הפולינום הנכון מתפרק ל-$(\lambda-1)(\lambda-6)$.` },
      recap: "שוכחים להחסיר: p = (λ−a)(λ−d) − bc." },
  ],
});
