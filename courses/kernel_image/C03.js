/* kernel_image, level 3: the kernel */
COURSE_LEVEL("kernel_image", {
  id: "C03", order: 3, icon: "🕳️", title: "הגרעין",
  goal: "למצוא בסיס ומימד לגרעין של העתקה, ולתרגם את הבסיס בחזרה לפולינומים או למטריצות.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>ה<b>גרעין</b> של $T:V\to W$ הוא כל הווקטורים ש-$T$ שולחת לאפס:
$$\mathrm{Ker}\,T=\{v\in V:\ T(v)=\vec 0\}$$
זהו תת-מרחב של $V$. אם $A$ היא המטריצה הסטנדרטית, אז $v\in\mathrm{Ker}\,T$ בדיוק כאשר $A\,[v]=\vec 0$, ולכן מוצאים את הגרעין על ידי פתרון המערכת ההומוגנית.</p>
<div class="lesson-rule">🔑 המתכון: (1) כותבים את $A$. (2) מדרגים ופותרים $A\vec x=\vec 0$. (3) כל משתנה חופשי נותן וקטור בסיס, ו-$\dim\mathrm{Ker}\,T$ הוא מספר המשתנים החופשיים. (4) <b>מתרגמים חזרה</b> מקואורדינטות לאיברי $V$.</div>
<div class="lesson-ex">דוגמה: $T:\mathbb{R}_3[x]\to\mathbb{R}^3$ עם המטריצה
$$A=\begin{pmatrix}1&2&1&0\\0&1&1&1\\1&3&2&1\end{pmatrix}\ \to\ \begin{pmatrix}1&2&1&0\\0&1&1&1\\0&0&0&0\end{pmatrix}\ \to\ \begin{pmatrix}1&0&-1&-2\\0&1&1&1\\0&0&0&0\end{pmatrix}$$
המשתנים החופשיים הם $x_3=s$ ו-$x_4=t$, ו-$x_1=s+2t$, $x_2=-s-t$. לכן
$$\vec x=s\begin{pmatrix}1\\-1\\1\\0\end{pmatrix}+t\begin{pmatrix}2\\-1\\0\\1\end{pmatrix}$$
שני משתנים חופשיים: $\dim\mathrm{Ker}\,T=2$. בתרגום חזרה לפולינומים, בסיס הגרעין הוא $\left(1-x+x^2,\ \ 2-x+x^3\right)$. בדיקה: $A(1,-1,1,0)^T=\vec 0$ ו-$A(2,-1,0,1)^T=\vec 0$.</div>
<div class="lesson-trap">⚠️ בסיס הגרעין שמוצאים מהפתרון הוא וקטורי קואורדינטות. אם התחום הוא פולינומים או מטריצות, חייבים לכתוב את התשובה כפולינומים או כמטריצות.</div>
` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: String.raw`המטריצה הסטנדרטית של $T:\mathbb{R}_3[x]\to\mathbb{R}^3$ היא $A=\begin{pmatrix}1&2&1&0\\0&1&1&1\\1&3&2&1\end{pmatrix}$. מהו $\dim\mathrm{Ker}\,T$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`אחרי דירוג יש שני צירים (עמודות 1 ו-2) ושני משתנים חופשיים ($x_3,x_4$). לכן $\dim\mathrm{Ker}\,T=2$. השורה השלישית שווה לסכום שתי הראשונות ולכן מתאפסת.` },
      recap: "מימד הגרעין = מספר המשתנים החופשיים." },
    { id: "C03-Q2",
      question: String.raw`אחד הווקטורים הבאים שייך לגרעין של ההעתקה שמטריצתה $A=\begin{pmatrix}1&2&1&0\\0&1&1&1\\1&3&2&1\end{pmatrix}$. איזה?`,
      options: [
        { id: "a", value: String.raw`$(1,\ -1,\ 1,\ 0)$` },
        { id: "b", value: String.raw`$(1,\ 1,\ -1,\ 0)$` },
        { id: "c", value: String.raw`$(-1,\ 1,\ 1,\ 0)$` },
        { id: "d", value: String.raw`$(2,\ 1,\ 0,\ -1)$` },
      ],
      correctId: "a",
      explanation: String.raw`מציבים: $A(1,-1,1,0)^T=(1-2+1,\ -1+1,\ 1-3+2)=(0,0,0)$. עבור $(1,1,-1,0)$ מתקבל $(2,0,2)$ (בשורה הראשונה $1+2-1=2$). עבור $(-1,1,1,0)$ מתקבל $(2,2,4)$. עבור $(2,1,0,-1)$ מתקבל $(4,0,4)$. אף אחד מהם אינו אפס.`,
      recap: "וקטור בגרעין אם $A\\vec x=\\vec 0$: מציבים ובודקים." },
    { id: "C03-Q3",
      step: { type: "numeric",
        prompt: String.raw`$T(x,y,z)=(x+2y+z,\ 2x+y-z,\ x-y-2z)$. הגרעין הוא קו ישר. לווקטור בגרעין שבו $z=3$ יש $y$ השווה ל:`,
        answer: -3, tol: 0,
        explain: String.raw`המטריצה $\begin{pmatrix}1&2&1\\2&1&-1\\1&-1&-2\end{pmatrix}$ מתדרגת ל-$\begin{pmatrix}1&2&1\\0&-3&-3\\0&0&0\end{pmatrix}$. מהשורה השנייה $y=-z$, ומהראשונה $x=-2y-z=z$. הגרעין נפרש על ידי $(1,-1,1)$, ועבור $z=3$ מתקבל $(3,-3,3)$, כלומר $y=-3$.` },
      recap: "פותרים מלמטה למעלה, משתנה חופשי אחד נותן קו." },
    { id: "C03-Q4",
      question: String.raw`$T:\mathbb{R}_3[x]\to\mathbb{R}^3$ עם מטריצה סטנדרטית $A=\begin{pmatrix}1&2&1&0\\0&1&1&1\\1&3&2&1\end{pmatrix}$. מהו בסיס של $\mathrm{Ker}\,T$ ?`,
      options: [
        { id: "a", value: String.raw`$\left(1-x+x^2,\ \ 2-x+x^3\right)$` },
        { id: "b", value: String.raw`$\left(1-x+x^3,\ \ 2-x+x^2\right)$` },
        { id: "c", value: String.raw`$\left(1+x-x^2,\ \ 2+x-x^3\right)$` },
        { id: "d", value: String.raw`$\left((1,-1,1,0),\ (2,-1,0,1)\right)$` },
      ],
      correctId: "a",
      explanation: String.raw`הקואורדינטות $(1,-1,1,0)$ ו-$(2,-1,0,1)$ מתורגמות ל-$1-x+x^2$ ו-$2-x+x^3$. באפשרות ב' שני הווקטורים הוחלפו בקואורדינטות האחרונות ($A(1,-1,0,1)^T=(-1,0,-1)\neq\vec 0$). באפשרות ג' הסימנים של $x$ ו-$x^2$ הפוכים ($A(1,1,-1,0)^T\neq\vec 0$). אפשרות ד' מכילה את הווקטורים הנכונים אבל בלי תרגום לפולינומים, והגרעין הוא תת-מרחב של $\mathbb{R}_3[x]$.`,
      recap: "בסיס הגרעין נכתב באיברי התחום." },
    { id: "C03-Q5",
      question: String.raw`$T:M_{2\times2}(\mathbb{R})\to\mathbb{R}^3$, $T\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a+b,\ c+d,\ a+b-c-d)$. מהו בסיס של $\mathrm{Ker}\,T$ ?`,
      options: [
        { id: "a", value: String.raw`$\left(\begin{pmatrix}1&-1\\0&0\end{pmatrix},\ \begin{pmatrix}0&0\\1&-1\end{pmatrix}\right)$` },
        { id: "b", value: String.raw`$\left(\begin{pmatrix}1&0\\-1&0\end{pmatrix},\ \begin{pmatrix}0&1\\0&-1\end{pmatrix}\right)$` },
        { id: "c", value: String.raw`$\left(\begin{pmatrix}1&1\\0&0\end{pmatrix},\ \begin{pmatrix}0&0\\1&1\end{pmatrix}\right)$` },
        { id: "d", value: String.raw`$\left(\begin{pmatrix}1&-1\\1&-1\end{pmatrix}\right)$` },
      ],
      correctId: "a",
      explanation: String.raw`הרכיב השלישי הוא הפרש של שני הראשונים, ולכן מספיק $a+b=0$ ו-$c+d=0$. שני משתנים חופשיים ($b$ ו-$d$) נותנים את הבסיס $\begin{pmatrix}-1&1\\0&0\end{pmatrix},\begin{pmatrix}0&0\\-1&1\end{pmatrix}$, שפורש אותו מרחב כמו האפשרות הראשונה. באפשרות ב' $T$ נותנת $(1,\,-1,\,2)$ על המטריצה הראשונה. באפשרות ג' $T$ נותנת $(2,0,2)$. באפשרות ד' איבר אחד בלבד ו-$\dim\mathrm{Ker}\,T=2$.`,
      recap: "משתנים חופשיים נותנים את הבסיס; מתרגמים חזרה למטריצות." },
  ],
});
