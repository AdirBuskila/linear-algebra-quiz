/* diagonalization, level 3: eigenvectors and the eigenspace */
COURSE_LEVEL("diagonalization", {
  id: "C03", order: 3, icon: "🎯", title: "וקטורים עצמיים ומרחב עצמי",
  goal: "למצוא וקטור עצמי לכל ערך עצמי, ולקבוע את מימד המרחב העצמי.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>אחרי שמצאנו ערך עצמי $\lambda$, מחפשים את הוקטורים העצמיים שלו: כל הפתרונות של המערכת ההומוגנית $(\lambda I-A)\vec x=\vec 0$. קבוצת הפתרונות היא <b>המרחב העצמי</b> $\mathrm{Ker}(\lambda I-A)$ (ביחד עם וקטור האפס).</p>
<div class="lesson-rule">🔑 <b>מתכון:</b> (1) מציבים את $\lambda$ ב-$\lambda I-A$. (2) מדרגים. (3) כותבים את הפתרון עם משתנה חופשי ובוחרים ערך שונה מאפס. מימד המרחב העצמי הוא מספר המשתנים החופשיים.</div>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ ו-$\lambda=2$. אז $2I-A=\begin{pmatrix}-2&-1\\-2&-1\end{pmatrix}$, ושתי השורות זהות: $2x_1+x_2=0$. נבחר $x_1=1$ ונקבל $x_2=-2$, כלומר הוקטור $(1,-2)^T$.
בדיקה: $A(1,-2)^T=(2,-4)^T=2\,(1,-2)^T$.</div>
<ul>
<li>כשמציבים ערך עצמי, המטריצה $\lambda I-A$ <b>חייבת</b> להיות לא הפיכה, כלומר יש שורת אפסים אחרי דירוג. אם יוצאת מטריצה הפיכה, טעיתם בחישוב.</li>
<li>המרחב העצמי מכיל אינסוף וקטורים. מספיק לתת אחד כזה, כל כפולה שלו שונה מאפס גם נכונה.</li>
</ul>
<div class="lesson-trap">⚠️ וקטור האפס פותר את המערכת תמיד, אבל הוא לא וקטור עצמי. בוחרים פתרון שונה מאפס.</div>
` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ וערך עצמי $\lambda=4$. הוקטור העצמי הוא מהצורה $(1,t)^T$. מהו $t$ ?`,
        answer: 1, tol: 0,
        explain: String.raw`$4I-A=\begin{pmatrix}1&-1\\-2&2\end{pmatrix}$, והמשוואה היא $x_1-x_2=0$. לכן $x_2=x_1$, ו-$t=1$. בדיקה: $A(1,1)^T=(4,4)^T$.` },
      recap: "מציבים λ, פותרים (λI−A)x = 0." },
    { id: "C03-Q2",
      question: String.raw`$A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ וערך עצמי $\lambda=1$. איזה מהוקטורים הבאים הוא וקטור עצמי שלו?`,
      options: [
        { id: "a", value: String.raw`$(1,-2)^T$` },
        { id: "b", value: String.raw`$(2,-1)^T$` },
        { id: "c", value: String.raw`$(1,2)^T$` },
        { id: "d", value: String.raw`$(1,1)^T$` },
      ],
      correctId: "a",
      explanation: String.raw`$I-A=\begin{pmatrix}-2&-1\\-2&-1\end{pmatrix}$ נותן $2x_1+x_2=0$, ולכן $(1,-2)^T$. בדיקה: $A(1,-2)^T=(1,-2)^T$. אפשרות ב' הופכת בין הרכיבים ונותנת $A(2,-1)^T=(5,2)^T$. אפשרות ג' נותנת $(5,6)^T$. אפשרות ד' היא הוקטור העצמי של $\lambda=4$, לא של $\lambda=1$.`,
      recap: "בודקים בהצבה: Av = λv." },
    { id: "C03-Q3",
      question: String.raw`$A=\begin{pmatrix}3&0\\1&2\end{pmatrix}$ וערך עצמי $\lambda=3$. איזה מהבאים הוא וקטור עצמי של $A$ עבור $\lambda=3$ ?`,
      options: [
        { id: "a", value: String.raw`$(3,3)^T$` },
        { id: "b", value: String.raw`$(0,0)^T$` },
        { id: "c", value: String.raw`$(1,0)^T$` },
        { id: "d", value: String.raw`$(1,-1)^T$` },
      ],
      correctId: "a",
      explanation: String.raw`$3I-A=\begin{pmatrix}0&0\\-1&1\end{pmatrix}$ נותן $x_2=x_1$, ולכן כל $(s,s)^T$ עם $s\neq0$. הוקטור $(3,3)^T$ מתאים. וקטור האפס פותר את המערכת אך אינו וקטור עצמי. $A(1,0)^T=(3,1)^T$ ו-$A(1,-1)^T=(3,-1)^T$ אינם כפולות של הווקטור.`,
      recap: "כל כפולה שונה מאפס מתאימה; האפס לא." },
    { id: "C03-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהו מימד המרחב העצמי של $\lambda=2$ עבור $A=\begin{pmatrix}2&0\\0&2\end{pmatrix}$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`$2I-A=\begin{pmatrix}0&0\\0&0\end{pmatrix}$, ולכן אין משוואות, ושני המשתנים חופשיים. המרחב העצמי הוא כל $\mathbb{R}^2$, מימד $2$.` },
      recap: "מימד = מספר המשתנים החופשיים." },
    { id: "C03-Q5",
      step: { type: "numeric",
        prompt: String.raw`מהו מימד המרחב העצמי של $\lambda=2$ עבור $A=\begin{pmatrix}2&1\\0&2\end{pmatrix}$ ?`,
        answer: 1, tol: 0,
        explain: String.raw`$2I-A=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$. המשוואה היחידה היא $x_2=0$, ו-$x_1$ חופשי, ולכן מימד $1$. אותו ערך עצמי כמו בשאלה הקודמת, אבל מימד אחר.` },
      recap: "אותו ערך עצמי, מימד שונה." },
    { id: "C03-Q6",
      step: { type: "order",
        prompt: String.raw`סדרו את מציאת הוקטור העצמי של $\lambda=4$ עבור $A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$.`,
        lines: [
          String.raw`כותבים $4I-A=\begin{pmatrix}1&-1\\-2&2\end{pmatrix}$`,
          String.raw`מדרגים: $R_2\to R_2+2R_1$ נותן $\begin{pmatrix}1&-1\\0&0\end{pmatrix}$`,
          String.raw`המשוואה היחידה $x_1-x_2=0$, ולכן $x_2$ חופשי`,
          String.raw`בוחרים $x_2=1$ ומקבלים את הוקטור העצמי $(1,1)^T$`,
        ],
        explain: String.raw`קודם מציבים את הערך העצמי, אחר כך מדרגים. שורת האפסים מאשרת שזה באמת ערך עצמי, ואז בוחרים ערך שונה מאפס למשתנה החופשי.` },
      recap: "מציבים, מדרגים, משתנה חופשי, בוחרים." },
  ],
});
