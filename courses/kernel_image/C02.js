/* kernel_image, level 2: coordinates and the standard matrix */
COURSE_LEVEL("kernel_image", {
  id: "C02", order: 2, icon: "🧮", title: "קואורדינטות ומטריצה סטנדרטית",
  goal: "לכתוב את המטריצה הסטנדרטית של העתקה ולחשב בעזרתה את ערך ההעתקה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כדי לחשב עם העתקה בין מרחבים כמו פולינומים או מטריצות, הופכים כל איבר לעמודת מספרים: <b>וקטור הקואורדינטות</b> שלו לפי הבסיס הסטנדרטי.</p>
<ul>
<li>ב-$\mathbb{R}_3[x]$ הבסיס הוא $(1,\ x,\ x^2,\ x^3)$, והפולינום $a+bx+cx^2+dx^3$ הופך לעמודה $(a,b,c,d)$.</li>
<li>ב-$M_{2\times2}(\mathbb{R})$ הבסיס הוא $E_1,E_2,E_3,E_4$ (היחידה במקום $(1,1)$, $(1,2)$, $(2,1)$, $(2,2)$ לפי הסדר), והמטריצה $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ הופכת לעמודה $(a,b,c,d)$: קוראים שורה אחרי שורה.</li>
</ul>
<p><b>המטריצה הסטנדרטית</b> $A$ של $T$: העמודה ה-$j$ היא וקטור הקואורדינטות של $T$ על איבר הבסיס ה-$j$ של התחום. אז לכל איבר $v$ מתקיים $[T(v)]=A\,[v]$.</p>
<div class="lesson-ex">דוגמה: $T:\mathbb{R}_2[x]\to\mathbb{R}^3$, $T(a+bx+cx^2)=(a,\ a+b+c,\ b+2c)$. אז $T(1)=(1,1,0)$, $T(x)=(0,1,1)$, $T(x^2)=(0,1,2)$ ו-
$$A=\begin{pmatrix}1&0&0\\1&1&1\\0&1&2\end{pmatrix}$$
עבור $p=2+x-x^2$ מתקבל $A\,(2,1,-1)^T=(2,\ 2,\ -1)^T$.</div>
<div class="lesson-rule">🔑 מספר העמודות של $A$ הוא $\dim V$ (התחום) ומספר השורות הוא $\dim W$ (הטווח). את $T$ על איבר הבסיס ה-$j$ כותבים כעמודה, לא כשורה.</div>
<div class="lesson-trap">⚠️ סדר הקואורדינטות חשוב: במטריצה קוראים $(a,b,c,d)$ שורה אחרי שורה, לא עמודה אחרי עמודה.</div>
` },
  questions: [
    { id: "C02-Q1",
      step: { type: "numeric",
        prompt: String.raw`$T:\mathbb{R}_3[x]\to\mathbb{R}^3$ מוגדרת על ידי $T(a+bx+cx^2+dx^3)=(a+2b,\ 3c-d,\ b+d)$. מהו האיבר בשורה $2$ ובעמודה $4$ של המטריצה הסטנדרטית?`,
        answer: -1, tol: 0,
        explain: String.raw`העמודה הרביעית היא $T(x^3)$, כלומר $a=b=c=0$ ו-$d=1$: $T(x^3)=(0,\ -1,\ 1)$. האיבר בשורה $2$ הוא $-1$.` },
      recap: "העמודה ה-$j$ היא $T$ של איבר הבסיס ה-$j$." },
    { id: "C02-Q2",
      question: String.raw`מהי המטריצה הסטנדרטית של $T:\mathbb{R}_3[x]\to\mathbb{R}^3$, $T(a+bx+cx^2+dx^3)=(a+2b,\ 3c-d,\ b+d)$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&2&0&0\\0&0&3&-1\\0&1&0&1\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}1&0&0\\2&0&1\\0&3&0\\0&-1&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}1&2&0&0\\0&1&0&1\\0&0&3&-1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}1&2&0&0\\0&0&3&1\\0&1&0&1\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`העמודות הן $T(1)=(1,0,0)$, $T(x)=(2,0,1)$, $T(x^2)=(0,3,0)$, $T(x^3)=(0,-1,1)$, וזה נותן את המטריצה הראשונה (שלוש שורות, ארבע עמודות). השנייה היא המטריצה המשוחלפת (שורות במקום עמודות). בשלישית שורות 2 ו-3 מוחלפות. ברביעית יש סימן שגוי: האיבר בשורה 2 ובעמודה 4 הוא $-1$ ולא $1$.`,
      recap: "שורות = ממד הטווח, עמודות = ממד התחום." },
    { id: "C02-Q3",
      step: { type: "numeric",
        prompt: String.raw`עבור ההעתקה $T(a+bx+cx^2+dx^3)=(a+2b,\ 3c-d,\ b+d)$, מהו הרכיב השלישי של $T(5-2x+x^2+4x^3)$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`הקואורדינטות הן $(5,-2,1,4)$. הרכיב השלישי הוא $b+d=-2+4=2$. (התוצאה המלאה: $(1,\ -1,\ 2)$.)` },
      recap: "$[T(v)]=A[v]$." },
    { id: "C02-Q4",
      question: String.raw`מהו וקטור הקואורדינטות של $\begin{pmatrix}3&-1\\0&7\end{pmatrix}$ בבסיס הסטנדרטי של $M_{2\times2}(\mathbb{R})$ ?`,
      options: [
        { id: "a", value: String.raw`$(3,\ -1,\ 0,\ 7)$` },
        { id: "b", value: String.raw`$(3,\ 0,\ -1,\ 7)$` },
        { id: "c", value: String.raw`$(3,\ 7,\ -1,\ 0)$` },
        { id: "d", value: String.raw`$(7,\ 0,\ -1,\ 3)$` },
      ],
      correctId: "a",
      explanation: String.raw`קוראים שורה אחרי שורה: $3,-1$ ואחר כך $0,7$. האפשרות השנייה קוראת עמודה אחרי עמודה, השלישית קוראת את האלכסון קודם, והרביעית קוראת מהסוף להתחלה.`,
      recap: "מטריצה $2\\times2$: $(a,b,c,d)$ שורה אחרי שורה." },
    { id: "C02-Q5",
      step: { type: "numeric",
        prompt: String.raw`$S:M_{2\times2}(\mathbb{R})\to\mathbb{R}^4$ מוגדרת על ידי $S\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a+b,\ b-c,\ 2a+d,\ c+3d)$. מהו הרכיב הרביעי של $S\begin{pmatrix}1&2\\3&4\end{pmatrix}$ ?`,
        answer: 15, tol: 0,
        explain: String.raw`$a=1,b=2,c=3,d=4$. הרכיב הרביעי הוא $c+3d=3+12=15$. (התוצאה המלאה: $(3,\ -1,\ 6,\ 15)$.)` },
      recap: "מציבים את ארבע הקואורדינטות בסדר $(a,b,c,d)$." },
  ],
});
