/* kernel_image, level 7: matrix of T in other bases */
COURSE_LEVEL("kernel_image", {
  id: "C07", order: 7, icon: "🔄", title: "מטריצה מייצגת בבסיסים אחרים",
  goal: "לחשב את המטריצה המייצגת של העתקה לפי בסיסים נתונים, ומטריצת מעבר בין בסיסים.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>בבסיס שאינו הסטנדרטי כותבים את אותו וקטור בקואורדינטות אחרות. אם $B=(b_1,\dots,b_n)$ בסיס של התחום ו-$C$ בסיס של הטווח, <b>המטריצה המייצגת</b> $[T]_C^B$ בנויה כך: העמודה ה-$j$ היא $[T(b_j)]_C$, כלומר הקואורדינטות של $T(b_j)$ לפי $C$. אז $[T(v)]_C=[T]_C^B\,[v]_B$.</p>
<div class="lesson-ex">דוגמה: $T(x,y)=(x+y,\ x-y)$, $B=\big((1,1),(1,-1)\big)$, $C=\big((1,0),(1,1)\big)$. אז $T(b_1)=(2,0)=2(1,0)+0(1,1)$ ו-$T(b_2)=(0,2)=-2(1,0)+2(1,1)$. לכן
$$[T]_C^B=\begin{pmatrix}2&-2\\0&2\end{pmatrix}$$</div>
<p><b>מטריצת מעבר</b> $[I]_C^B$ היא המטריצה המייצגת של העתקת הזהות: העמודה ה-$j$ היא $[b_j]_C$. בעזרת הבסיס הסטנדרטי $E$:
$$[T]_C^B=[I]_C^E\,[T]_E^E\,[I]_E^B,\qquad [I]_C^E=\big([I]_E^C\big)^{-1}$$
כאשר $[I]_E^B$ פשוט מורכבת מווקטורי $B$ כעמודות.</p>
<div class="lesson-rule">🔑 מחשבים כל $T(b_j)$ ומפרקים לפי $C$: מערכת לכל עמודה (או דירוג משותף של $[\,C\mid T(b_1)\ \cdots\ T(b_n)\,]$).</div>
<div class="lesson-trap">⚠️ מפרקים לפי הבסיס $C$ של הטווח ולא לפי $B$, וכל וקטור נכנס כעמודה לפי הסדר של $B$.</div>
` },
  questions: [
    { id: "C07-Q1",
      step: { type: "numeric",
        prompt: String.raw`$T(x,y)=(2x+y,\ x+3y)$, $B=\big((1,0),(1,1)\big)$, $C=\big((1,1),(0,1)\big)$. מהו האיבר בשורה $2$ ועמודה $1$ של $[T]_C^B$ ?`,
        answer: -1, tol: 0,
        explain: String.raw`$T(b_1)=T(1,0)=(2,1)=2(1,1)+(-1)(0,1)$, ולכן העמודה הראשונה היא $(2,-1)$. האיבר בשורה $2$ הוא $-1$.` },
      recap: "מפרקים $T(b_1)$ לפי $C$." },
    { id: "C07-Q2",
      step: { type: "numeric",
        prompt: String.raw`באותה העתקה ובאותם בסיסים, מהו האיבר בשורה $2$ ועמודה $2$ של $[T]_C^B$ ?`,
        answer: 1, tol: 0,
        explain: String.raw`$T(b_2)=T(1,1)=(3,4)=3(1,1)+1\cdot(0,1)$, ולכן העמודה השנייה היא $(3,1)$. האיבר בשורה $2$ הוא $1$. המטריצה המלאה היא $\begin{pmatrix}2&3\\-1&1\end{pmatrix}$.` },
      recap: "עמודה לכל איבר של $B$." },
    { id: "C07-Q3",
      question: String.raw`באותה העתקה ובאותם בסיסים, מהי $[T]_C^B$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}2&3\\-1&1\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}2&-1\\3&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}2&3\\1&4\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}3&2\\1&-1\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`העמודות הן $(2,-1)$ ו-$(3,1)$. אפשרות $\begin{pmatrix}2&-1\\3&1\end{pmatrix}$ היא המשוחלפת (שורות במקום עמודות). אפשרות $\begin{pmatrix}2&3\\1&4\end{pmatrix}$ היא $T(1,0)$ ו-$T(1,1)$ בקואורדינטות סטנדרטיות, בלי פירוק לפי $C$. אפשרות $\begin{pmatrix}3&2\\1&-1\end{pmatrix}$ מחליפה את סדר שתי העמודות.`,
      recap: "העמודה ה-$j$ היא $[T(b_j)]_C$." },
    { id: "C07-Q4",
      step: { type: "numeric",
        prompt: String.raw`$B=\big((1,0),(1,1)\big)$, $C=\big((1,1),(0,1)\big)$. מהו האיבר בשורה $2$ ועמודה $1$ של מטריצת המעבר $[I]_C^B$ ?`,
        answer: -1, tol: 0,
        explain: String.raw`$b_1=(1,0)=1\cdot(1,1)+(-1)(0,1)$, ולכן העמודה הראשונה היא $(1,-1)$. מכאן האיבר הוא $-1$. (העמודה השנייה: $b_2=(1,1)$ נותן $(1,0)$.)` },
      recap: "מעבר: מפרקים את וקטורי $B$ לפי $C$." },
    { id: "C07-Q5",
      question: String.raw`בהינתן הבסיסים $B$ ו-$C$ ב-$\mathbb{R}^2$ והמטריצה הסטנדרטית $A=[T]_E^E$, מהי הנוסחה הנכונה ל-$[T]_C^B$ ?`,
      options: [
        { id: "a", value: String.raw`$\big([I]_E^C\big)^{-1}\,A\,[I]_E^B$` },
        { id: "b", value: String.raw`$[I]_E^C\,A\,\big([I]_E^B\big)^{-1}$` },
        { id: "c", value: String.raw`$\big([I]_E^B\big)^{-1}\,A\,[I]_E^C$` },
        { id: "d", value: String.raw`$[I]_E^B\,A\,[I]_E^C$` },
      ],
      correctId: "a",
      explanation: String.raw`קלט בקואורדינטות $B$: קודם $[I]_E^B$ הופכת אותן לסטנדרטיות, אחר כך $A$ מפעילה את $T$, ולבסוף $\big([I]_E^C\big)^{-1}$ הופכת את התוצאה לקואורדינטות $C$. האפשרויות האחרות מחליפות את התפקידים של $B$ ו-$C$ או לא הופכות נכון.`,
      recap: "$[T]_C^B=([I]_E^C)^{-1}A[I]_E^B$." },
    { id: "C07-Q6",
      step: { type: "numeric",
        prompt: String.raw`עם $[T]_C^B=\begin{pmatrix}2&3\\-1&1\end{pmatrix}$ ווקטור $v$ שקואורדינטותיו לפי $B$ הן $(2,1)$. מהו הרכיב הראשון של $[T(v)]_C$ ?`,
        answer: 7, tol: 0,
        explain: String.raw`$[T(v)]_C=[T]_C^B[v]_B=\begin{pmatrix}2&3\\-1&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=\begin{pmatrix}7\\-1\end{pmatrix}$. הרכיב הראשון הוא $7$.` },
      recap: "$[T(v)]_C=[T]_C^B[v]_B$." },
    { bankId: "23B-B-Q5e", recap: "מטריצת מעבר: $([I]_E^C)^{-1}[I]_E^B$ או דירוג של $[C\\mid B]$." },
  ],
});
