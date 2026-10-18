/* basis_dim, level 8: coordinates and the transition matrix */
COURSE_LEVEL("basis_dim", {
  id: "C08", order: 8, icon: "🔄", title: "קואורדינטות ומטריצת מעבר",
  goal: "לחשב וקטור קואורדינטות, מטריצת מעבר בין בסיסים, ולהמיר קואורדינטות.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>אם $B=(b_1,\dots,b_n)$ הוא בסיס סדור ו-$v=c_1b_1+\dots+c_nb_n$, אז <b>וקטור הקואורדינטות</b> של $v$ הוא $[v]_B=(c_1,\dots,c_n)^T$. הסדר של הבסיס חשוב. בפולינומים ובמטריצות עובדים דרך הבסיס הסטנדרטי: הפולינום $a+bx$ נכתב $(a,b)$ לפי $(1,x)$.</p>
<p><b>מטריצת המעבר</b> $[I]_C^B$ מבסיס $B$ לבסיס $C$ היא המטריצה שעמודה $j$ שלה היא $[b_j]_C$, הקואורדינטות של $b_j$ לפי $C$. היא ממירה קואורדינטות:</p>
<div class="lesson-formula">$$[v]_C=[I]_C^B\,[v]_B,\qquad [I]_C^B=\big([I]_E^C\big)^{-1}[I]_E^B$$</div>
<p>כאן $E$ הבסיס הסטנדרטי, ו-$[I]_E^B$ היא המטריצה שעמודותיה הן הוקטורים של $B$ עצמם. דרך נוספת: מדרגים את המטריצה $(C\,|\,B)$ עד שמתקבל $(I\,|\,[I]_C^B)$.</div>
<div class="lesson-ex">דוגמה: $B=\big((1,2),(0,1)\big)$ ו-$C=\big((1,0),(1,1)\big)$. אז $[I]_E^B=\begin{pmatrix}1&0\\2&1\end{pmatrix}$ ו-$[I]_E^C=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, עם הופכית $\begin{pmatrix}1&-1\\0&1\end{pmatrix}$. לכן $[I]_C^B=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}1&0\\2&1\end{pmatrix}=\begin{pmatrix}-1&-1\\2&1\end{pmatrix}$. בדיקה: העמודה הראשונה $(-1,2)$ אומרת $(1,2)=-1\cdot(1,0)+2\cdot(1,1)$, וזה נכון.</div>
<div class="lesson-trap">⚠️ הסדר ב-$[I]_C^B$: המטריצה ממירה מ-$B$ אל $C$, וההופכית שלה $[I]_B^C$ ממירה בכיוון ההפוך. מחליפים את שני הכיוונים בטעות לעיתים קרובות, ולכן תמיד בודקים עמודה אחת ישירות.</div>
` },
  questions: [
    { id: "C08-Q1",
      step: { type: "numeric",
        prompt: String.raw`הבסיס הוא $B=\big((1,1),(1,-1)\big)$ ו-$v=(5,3)$. מהו הרכיב הראשון של $[v]_B$ ?`,
        answer: 4, tol: 0,
        explain: String.raw`פותרים $c_1(1,1)+c_2(1,-1)=(5,3)$, כלומר $c_1+c_2=5$ ו-$c_1-c_2=3$. לכן $c_1=4$ ו-$c_2=1$.` },
      recap: "קואורדינטות = מקדמי הצירוף." },
    { id: "C08-Q2",
      step: { type: "numeric",
        prompt: String.raw`הבסיס של $\mathbb{R}_2[x]$ הוא $B=\big(1,\ 1+x,\ 1+x+x^2\big)$ ו-$p=4+3x+2x^2$. כותבים $p=a\cdot1+b(1+x)+c(1+x+x^2)$. מהו $c$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`המקדם של $x^2$ בצירוף הוא $c$ בלבד, ולכן $c=2$. אחר כך מקדם $x$ נותן $b+c=3$, כלומר $b=1$, והמקדם החופשי נותן $a+b+c=4$, כלומר $a=1$.` },
      recap: "משווים מקדמים מהחזקה הגבוהה." },
    { id: "C08-Q3",
      question: String.raw`איזו נוסחה נותנת את מטריצת המעבר $[I]_C^B$ מבסיס $B$ לבסיס $C$ (כש-$E$ הבסיס הסטנדרטי)?`,
      options: [
        { id: "a", value: String.raw`$\big([I]_E^C\big)^{-1}[I]_E^B$` },
        { id: "b", value: String.raw`$[I]_E^B\big([I]_E^C\big)^{-1}$` },
        { id: "c", value: String.raw`$[I]_E^C[I]_E^B$` },
        { id: "d", value: String.raw`$\big([I]_E^B\big)^{-1}[I]_E^C$` },
      ],
      correctId: "a",
      explanation: String.raw`עוברים מ-$B$ אל הסטנדרטי ($[I]_E^B$) ומשם אל $C$ ($([I]_E^C)^{-1}$), והכפל כתוב מימין לשמאל. הבדיקה בדוגמה של הלימוד נותנת $\begin{pmatrix}-1&-1\\2&1\end{pmatrix}$ לנוסחה א', ואילו ב' נותנת $\begin{pmatrix}1&-1\\2&-1\end{pmatrix}$, ג' נותנת $\begin{pmatrix}3&1\\2&1\end{pmatrix}$, ו-ד' נותנת $\begin{pmatrix}1&1\\-2&-1\end{pmatrix}$. שלוש האחרונות שונות מהנכונה.`,
      recap: "[I]_C^B = ([I]_E^C)^(-1) [I]_E^B." },
    { id: "C08-Q4",
      step: { type: "numeric",
        prompt: String.raw`$B=\big((1,0),(1,1)\big)$ ו-$C=\big((2,1),(1,1)\big)$. מהי הכניסה בשורה $2$ ובעמודה $1$ של $[I]_C^B$ ?`,
        answer: -1, tol: 0,
        explain: String.raw`$[I]_E^C=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ עם הופכית $\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$, ו-$[I]_E^B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. המכפלה היא $\begin{pmatrix}1&0\\-1&1\end{pmatrix}$, והכניסה המבוקשת $-1$. בדיקה: $(1,0)=1\cdot(2,1)+(-1)\cdot(1,1)$.` },
      recap: "עמודה j = קואורדינטות של b_j לפי C." },
    { id: "C08-Q5",
      step: { type: "numeric",
        prompt: String.raw`מטריצת המעבר היא $[I]_C^B=\begin{pmatrix}1&0\\-1&1\end{pmatrix}$ ו-$[v]_B=\begin{pmatrix}3\\2\end{pmatrix}$. מהו הרכיב השני של $[v]_C$ ?`,
        answer: -1, tol: 0,
        explain: String.raw`$[v]_C=[I]_C^B[v]_B=\begin{pmatrix}1&0\\-1&1\end{pmatrix}\begin{pmatrix}3\\2\end{pmatrix}=\begin{pmatrix}3\\-3+2\end{pmatrix}=\begin{pmatrix}3\\-1\end{pmatrix}$. הרכיב השני $-1$.` },
      recap: "[v]_C = [I]_C^B [v]_B." },
    { id: "C08-Q6",
      question: String.raw`אם $[I]_C^B=\begin{pmatrix}1&0\\-1&1\end{pmatrix}$, מהי המטריצה $[I]_B^C$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&0\\1&1\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}1&-1\\0&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}-1&0\\1&-1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}1&0\\-1&1\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`$[I]_B^C$ ממירה בכיוון ההפוך, ולכן היא ההופכית של $[I]_C^B$. ההופכית של $\begin{pmatrix}1&0\\-1&1\end{pmatrix}$ היא $\begin{pmatrix}1&0\\1&1\end{pmatrix}$ (המכפלה היא $I$). אפשרות ב' היא ההעברה של המטריצה, ג' היא המטריצה כפול $-1$, ו-ד' היא המטריצה עצמה.`,
      recap: "[I]_B^C = ([I]_C^B)^(-1)." },
  ],
});
