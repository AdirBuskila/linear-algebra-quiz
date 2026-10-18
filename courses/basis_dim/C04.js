/* basis_dim, level 4: a subspace given by conditions -> general vector -> basis */
COURSE_LEVEL("basis_dim", {
  id: "C04", order: 4, icon: "🧮", title: "בסיס לתת-מרחב שמוגדר בתנאים",
  goal: "לקחת תת-מרחב שנתון בתנאים, לכתוב וקטור כללי, ולפרק אותו לבסיס.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כשתת-מרחב נתון בתנאים (למשל $x+y+z=0$) מוצאים לו בסיס במתכון של ארבעה צעדים:</p>
<ul>
<li>כותבים וקטור כללי של המרחב.</li>
<li>מציבים את התנאים, כלומר פותרים את המשוואות ומבטאים משתנים בעזרת <b>משתנים חופשיים</b>.</li>
<li>פורקים את הוקטור לצירוף: כל משתנה חופשי מוכפל בוקטור קבוע.</li>
<li>הוקטורים הקבועים הם הבסיס, ו<b>המימד = מספר המשתנים החופשיים</b>.</li>
</ul>
<div class="lesson-ex">דוגמה: $W=\{(x,y,z)\,:\,x+y+z=0\}$. מבטאים $x=-y-z$, ולכן הוקטור הכללי הוא $(-y-z,\,y,\,z)=y(-1,1,0)+z(-1,0,1)$. הבסיס הוא $\{(-1,1,0),(-1,0,1)\}$ והמימד $2$ (שני משתנים חופשיים, $y$ ו-$z$).</div>
<p>במרחבים אחרים עוברים לוקטור הקואורדינטות לפי הבסיס הסטנדרטי ועובדים כרגיל. מטריצה $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ נכתבת $(a,b,c,d)$, ופולינום $ax^3+bx^2+cx+d$ נכתב $(a,b,c,d)$. למשל המטריצות הסימטריות הן $\begin{pmatrix}a&b\\b&c\end{pmatrix}=a\begin{pmatrix}1&0\\0&0\end{pmatrix}+b\begin{pmatrix}0&1\\1&0\end{pmatrix}+c\begin{pmatrix}0&0\\0&1\end{pmatrix}$, כלומר בסיס בן שלוש מטריצות ומימד $3$.</p>
<div class="lesson-rule">🔑 בתשובה כותבים את <b>הוקטורים</b> (המטריצות, הפולינומים) ולא את המקדמים. מספר הוקטורים בבסיס הוא מימד המרחב: מספר הנעלמים פחות מספר האילוצים הבלתי תלויים.</div>
<div class="lesson-trap">⚠️ אילוצים תלויים לא מורידים את המימד פעמיים. שני התנאים $x=y$ ו-$2x=2y$ הם אילוץ אחד.</div>
` },
  questions: [
    { id: "C04-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהו המימד של $\{(x,y,z)\,:\,x-2y+z=0\}$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`שלושה נעלמים ואילוץ אחד: מבטאים $x=2y-z$ ונשארים שני משתנים חופשיים, $y$ ו-$z$. המימד $3-1=2$.` },
      recap: "מימד = נעלמים פחות אילוצים בלתי תלויים." },
    { id: "C04-Q2",
      question: String.raw`איזו קבוצה היא בסיס של $\{(x,y,z)\,:\,z=x+y\}$ ?`,
      options: [
        { id: "a", value: String.raw`$\{(1,0,1),(0,1,1)\}$` },
        { id: "b", value: String.raw`$\{(1,0,1),(0,1,0)\}$` },
        { id: "c", value: String.raw`$\{(1,1,2)\}$` },
        { id: "d", value: String.raw`$\{(1,1,2),(2,2,4)\}$` },
      ],
      correctId: "a",
      explanation: String.raw`הוקטור הכללי הוא $(x,y,x+y)=x(1,0,1)+y(0,1,1)$, ולכן הבסיס הוא $\{(1,0,1),(0,1,1)\}$. באפשרות ב' הוקטור $(0,1,0)$ לא מקיים $z=x+y$ ($0\neq1$). באפשרות ג' וקטור בודד, שלא פורש מימד $2$. באפשרות ד' שני הוקטורים תלויים ($(2,2,4)=2(1,1,2)$).`,
      recap: "מציבים את התנאי בוקטור הכללי ופורקים." },
    { id: "C04-Q3",
      step: { type: "numeric",
        prompt: String.raw`מהו המימד של תת-המרחב $\{A\in M_{2\times2}(\mathbb{R})\,:\,\mathrm{Tr}A=0\}$ ?`,
        answer: 3, tol: 0,
        explain: String.raw`המטריצה הכללית $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ עם $a+d=0$ היא $\begin{pmatrix}a&b\\c&-a\end{pmatrix}$, כלומר שלושה משתנים חופשיים $a,b,c$. המימד $4-1=3$.` },
      recap: "עקבה אפס היא אילוץ אחד: מימד 3." },
    { id: "C04-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהו המימד של תת-המרחב $\{A\in M_{2\times2}(\mathbb{R})\,:\,A^T=-A\}$ ?`,
        answer: 1, tol: 0,
        explain: String.raw`התנאי $A^T=-A$ נותן $a=-a$, $d=-d$ ו-$b=-c$. לכן $a=d=0$ והמטריצה היא $\begin{pmatrix}0&b\\-b&0\end{pmatrix}=b\begin{pmatrix}0&1\\-1&0\end{pmatrix}$: משתנה חופשי אחד, מימד $1$.` },
      recap: "אנטי-סימטריות 2x2: מימד 1." },
    { id: "C04-Q5",
      step: { type: "numeric",
        prompt: String.raw`מהו המימד של תת-המרחב $\{p\in\mathbb{R}_3[x]\,:\,p(1)=p(-1)\}$ ?`,
        answer: 3, tol: 0,
        explain: String.raw`עבור $p=ax^3+bx^2+cx+d$ התנאי $p(1)=p(-1)$ הוא $a+b+c+d=-a+b-c+d$, כלומר $2a+2c=0$ ו-$c=-a$. המשתנים החופשיים הם $a,b,d$, ולכן המימד $4-1=3$.` },
      recap: "פולינומים: עוברים לוקטור המקדמים." },
    { id: "C04-Q6",
      step: { type: "order",
        prompt: String.raw`סדרו את שלבי מציאת הבסיס של $W=\{(x,y,z)\,:\,y=2x\}$.`,
        lines: [
          String.raw`וקטור כללי של $\mathbb{R}^3$ הוא $(x,y,z)$`,
          String.raw`מציבים את התנאי $y=2x$ ומקבלים $(x,\,2x,\,z)$`,
          String.raw`פורקים לצירוף: $x(1,2,0)+z(0,0,1)$`,
          String.raw`הבסיס הוא $\{(1,2,0),(0,0,1)\}$ והמימד $2$`,
        ],
        explain: String.raw`קודם הוקטור הכללי, אחר כך הצבת התנאי, ורק אז אפשר לפרק לפי המשתנים החופשיים $x$ ו-$z$. הבסיס נקרא מהפירוק.` },
      recap: "כללי, מציבים תנאי, פורקים, קוראים בסיס." },
  ],
});
