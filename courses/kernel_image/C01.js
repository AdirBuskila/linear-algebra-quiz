/* kernel_image, level 1: what a linear map is, and how to test it */
COURSE_LEVEL("kernel_image", {
  id: "C01", order: 1, icon: "🔀", title: "מהי העתקה לינארית",
  goal: "להכריע אם פונקציה היא העתקה לינארית, ולחשב את ערכה על וקטור נתון.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p><b>העתקה</b> $T:V\to W$ מקבלת וקטור מ-$V$ (התחום) ומחזירה וקטור ב-$W$ (הטווח). היא <b>לינארית</b> אם שני התנאים מתקיימים לכל $u,v\in V$ ולכל מספר $c$:</p>
<ul>
<li>$T(u+v)=T(u)+T(v)$ (שומרת על חיבור).</li>
<li>$T(cu)=c\,T(u)$ (שומרת על כפל בסקלר).</li>
</ul>
<p>שני התנאים יחד אומרים ש-$T(au+bv)=a\,T(u)+b\,T(v)$: כדי לדעת את $T$ על כל וקטור מספיק לדעת אותה על וקטורים שמהם הוא נבנה כצירוף לינארי.</p>
<div class="lesson-ex">דוגמה: $T(x,y)=(x+y,\ 2x)$. אז $T(3,1)=(4,6)$ ו-$T(1,0)=(1,2)$, $T(0,1)=(1,0)$. אכן $3\,T(1,0)+1\cdot T(0,1)=(3,6)+(1,0)=(4,6)$.</div>
<div class="lesson-rule">🔑 עבור כל העתקה לינארית $T(\vec 0)=\vec 0$. לכן אם $T(\vec 0)\neq\vec 0$, ההעתקה בוודאי לא לינארית. אבל $T(\vec 0)=\vec 0$ לא מספיק: נוסחה עם מכפלה בין משתנים ($xy$), חזקה ($x^2$) או קבוע נוסף נכשלת בדרך כלל באחד משני התנאים. מפריכים בעזרת דוגמה נגדית אחת.</div>
<div class="lesson-ex">דוגמה נגדית: $S(x,y)=(xy,\ y)$. מתקיים $S(1,1)=(1,1)$ אבל $S(2,2)=(4,2)\neq 2\,S(1,1)=(2,2)$, ולכן $S$ לא לינארית.</div>
<div class="lesson-trap">⚠️ העתקה לינארית היא נוסחה שבה כל רכיב של התוצאה הוא צירוף לינארי של המשתנים בלבד, בלי איבר חופשי: $(2x-y,\ x+3y)$ כן, $(2x-y+1,\ x)$ לא.</div>
` },
  questions: [
    { id: "C01-Q1",
      question: String.raw`איזו מהפונקציות הבאות היא העתקה לינארית $T:\mathbb{R}^2\to\mathbb{R}^2$ ?`,
      options: [
        { id: "a", value: String.raw`$T(x,y)=(x+y,\ x-y)$` },
        { id: "b", value: String.raw`$T(x,y)=(x+1,\ y)$` },
        { id: "c", value: String.raw`$T(x,y)=(xy,\ y)$` },
        { id: "d", value: String.raw`$T(x,y)=(x^2,\ y)$` },
      ],
      correctId: "a",
      explanation: String.raw`בפונקציה הראשונה כל רכיב הוא צירוף לינארי של $x,y$, ולכן היא לינארית. בשנייה $T(0,0)=(1,0)\neq(0,0)$. בשלישית $T(1,1)=(1,1)$ אבל $T(2,2)=(4,2)\neq2\,T(1,1)$. ברביעית $T(1,0)=(1,0)$ אבל $T(2,0)=(4,0)\neq2\,T(1,0)$.`,
      recap: "אם יש איבר חופשי, מכפלת משתנים או חזקה, ההעתקה לא לינארית." },
    { id: "C01-Q2",
      step: { type: "numeric",
        prompt: String.raw`ההעתקה $T(x,y,z)=(x+2y,\ y-z,\ 3x+z)$ לינארית. מהו הרכיב השני של $T(2,5,1)$ ?`,
        answer: 4, tol: 0,
        explain: String.raw`הרכיב השני הוא $y-z=5-1=4$. (התוצאה המלאה היא $T(2,5,1)=(12,4,7)$.)` },
      recap: "מציבים את הקואורדינטות בנוסחה." },
    { id: "C01-Q3",
      step: { type: "numeric",
        prompt: String.raw`$T:\mathbb{R}^2\to\mathbb{R}^2$ לינארית, $T(1,0)=(2,1)$ ו-$T(0,1)=(-1,3)$. מהו הרכיב הראשון של $T(3,2)$ ?`,
        answer: 4, tol: 0,
        explain: String.raw`$(3,2)=3(1,0)+2(0,1)$, ולכן $T(3,2)=3(2,1)+2(-1,3)=(4,9)$. הרכיב הראשון הוא $6-2=4$.` },
      recap: "מפרקים לצירוף של וקטורים שהערך עליהם ידוע: $T(au+bv)=aT(u)+bT(v)$." },
    { id: "C01-Q4",
      question: String.raw`איזו מהפונקציות הבאות היא העתקה לינארית $T:M_{2\times2}(\mathbb{R})\to M_{2\times2}(\mathbb{R})$ ?`,
      options: [
        { id: "a", value: String.raw`$T(A)=A+I$` },
        { id: "b", value: String.raw`$T(A)=A^T$` },
        { id: "c", value: String.raw`$T(A)=A^2$` },
        { id: "d", value: String.raw`$T(A)=(\det A)\cdot I$` },
      ],
      correctId: "b",
      explanation: String.raw`שחלוף שומר על חיבור ועל כפל בסקלר: $(A+B)^T=A^T+B^T$ ו-$(cA)^T=cA^T$. בראשונה $T(0)=I\neq0$. בשלישית $T(2I)=4I\neq2\,T(I)=2I$. ברביעית $T(2I)=\det(2I)\,I=4I\neq 2\,T(I)=2I$.`,
      recap: "שחלוף לינארי; הוספת קבוע, ריבוע ודטרמיננטה לא." },
    { id: "C01-Q5",
      step: { type: "numeric",
        prompt: String.raw`עבור איזה ערך של $k$ ההעתקה $T(x,y)=(2x+k-3,\ y)$ היא לינארית?`,
        answer: 3, tol: 0,
        explain: String.raw`חייב להתקיים $T(0,0)=(0,0)$, כלומר $k-3=0$ ואז $k=3$. עבור $k=3$ ההעתקה $(2x,\ y)$ לינארית.` },
      recap: "$T(\\vec 0)=\\vec 0$ היא תנאי הכרחי." },
    { id: "C01-Q6",
      step: { type: "numeric",
        prompt: String.raw`$T:\mathbb{R}^2\to\mathbb{R}^2$ לינארית, $T(1,1)=(3,0)$ ו-$T(1,-1)=(1,2)$. מהו הרכיב השני של $T(2,0)$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`$(2,0)=(1,1)+(1,-1)$, ולכן $T(2,0)=(3,0)+(1,2)=(4,2)$. הרכיב השני הוא $2$.` },
      recap: "כותבים את הוקטור כצירוף של וקטורים שהערך עליהם ידוע." },
  ],
});
