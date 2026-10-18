/* kernel_image, level 4: the image */
COURSE_LEVEL("kernel_image", {
  id: "C04", order: 4, icon: "🖼️", title: "התמונה",
  goal: "למצוא בסיס ומימד לתמונה של העתקה מתוך עמודות הציר של המטריצה המקורית.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>ה<b>תמונה</b> של $T:V\to W$ היא כל הערכים ש-$T$ מקבלת:
$$\mathrm{Im}\,T=\{T(v):\ v\in V\}$$
זהו תת-מרחב של $W$. הוא נפרש על ידי $T$ של איברי בסיס של $V$, כלומר על ידי עמודות $A$.</p>
<div class="lesson-rule">🔑 המתכון: מדרגים את $A$ ומסמנים אילו עמודות הן עמודות ציר. בסיס של $\mathrm{Im}\,T$ הוא העמודות <b>של $A$ המקורית</b> שבמקומות האלה. $\dim\mathrm{Im}\,T$ הוא מספר עמודות הציר, כלומר הדרגה של $A$. אחר כך מתרגמים חזרה לאיברי $W$ אם צריך.</div>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}1&2&1&0\\0&1&1&1\\1&3&2&1\end{pmatrix}$ מתדרגת ל-$\begin{pmatrix}1&2&1&0\\0&1&1&1\\0&0&0&0\end{pmatrix}$. עמודות הציר הן 1 ו-2, ולכן בסיס של $\mathrm{Im}\,T$ הוא העמודות $(1,0,1)$ ו-$(2,1,3)$ של $A$, ו-$\dim\mathrm{Im}\,T=2$. כל וקטור בתמונה מקיים $z=x+y$.</div>
<div class="lesson-trap">⚠️ עמודות הציר נלקחות מהמטריצה המקורית. העמודות של המטריצה המדורגת ($(1,0,0)$ ו-$(2,1,0)$ בדוגמה) הן לא בהכרח בתמונה: כאן $(1,0,0)$ לא מקיים $z=x+y$.</div>
<p>כשהטווח הוא מטריצות, מתרגמים כל עמודת בסיס למטריצה $2\times2$ לפי סדר הקריאה שורה אחרי שורה.</p>
` },
  questions: [
    { id: "C04-Q1",
      step: { type: "numeric",
        prompt: String.raw`המטריצה הסטנדרטית של $T$ היא $A=\begin{pmatrix}1&2&0&3\\2&4&1&7\\3&6&1&10\end{pmatrix}$. מהו $\dim\mathrm{Im}\,T$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`דירוג: $R_2-2R_1=(0,0,1,1)$ ו-$R_3-3R_1=(0,0,1,1)$, ולכן השורה השלישית מתאפסת. יש שתי עמודות ציר (1 ו-3), ולכן הדרגה היא $2$.` },
      recap: "מימד התמונה = דרגת $A$." },
    { id: "C04-Q2",
      question: String.raw`מהו בסיס של $\mathrm{Im}\,T$ עבור $A=\begin{pmatrix}1&2&0&3\\2&4&1&7\\3&6&1&10\end{pmatrix}$ ?`,
      options: [
        { id: "a", value: String.raw`$\left((1,2,3),\ (0,1,1)\right)$` },
        { id: "b", value: String.raw`$\left((1,0,0),\ (0,1,0)\right)$` },
        { id: "c", value: String.raw`$\left((1,2,3),\ (2,4,6)\right)$` },
        { id: "d", value: String.raw`$\left((1,2,0,3),\ (0,0,1,1)\right)$` },
      ],
      correctId: "a",
      explanation: String.raw`עמודות הציר הן 1 ו-3, והעמודות המתאימות ב-$A$ המקורית הן $(1,2,3)$ ו-$(0,1,1)$. אפשרות ב' לוקחת את עמודות הציר של המטריצה המדורגת, ו-$(1,0,0)$ לא בתמונה (בתמונה $z=x+y$). אפשרות ג' תלויה לינארית ($(2,4,6)=2(1,2,3)$) ופורשת רק קו. אפשרות ד' היא שורות, שחיות ב-$\mathbb{R}^4$ ולא בטווח.`,
      recap: "עמודות הציר של המקורית, לא של המדורגת." },
    { id: "C04-Q3",
      question: String.raw`$T:\mathbb{R}^3\to M_{2\times2}(\mathbb{R})$, $T(x,y,z)=\begin{pmatrix}x+y&y+z\\x-z&x+y\end{pmatrix}$. מהו בסיס של $\mathrm{Im}\,T$ ?`,
      options: [
        { id: "a", value: String.raw`$\left(\begin{pmatrix}1&0\\1&1\end{pmatrix},\ \begin{pmatrix}1&1\\0&1\end{pmatrix}\right)$` },
        { id: "b", value: String.raw`$\left(\begin{pmatrix}1&0\\0&0\end{pmatrix},\ \begin{pmatrix}0&1\\0&0\end{pmatrix}\right)$` },
        { id: "c", value: String.raw`$\left(\begin{pmatrix}1&0\\1&1\end{pmatrix}\right)$` },
        { id: "d", value: String.raw`$\left(\begin{pmatrix}1&0\\1&1\end{pmatrix},\ \begin{pmatrix}1&1\\0&1\end{pmatrix},\ \begin{pmatrix}0&1\\0&0\end{pmatrix}\right)$` },
      ],
      correctId: "a",
      explanation: String.raw`המטריצה הסטנדרטית (שורות: $a,b,c,d$) היא $\begin{pmatrix}1&1&0\\0&1&1\\1&0&-1\\1&1&0\end{pmatrix}$. השורה השלישית היא הראשונה פחות השנייה, ולכן הדרגה $2$ ועמודות הציר הן 1 ו-2: $(1,0,1,1)$ ו-$(1,1,0,1)$, שמתורגמות למטריצות שבאפשרות א'. באפשרות ב' עמודות המדורגת, ו-$\begin{pmatrix}1&0\\0&0\end{pmatrix}$ לא בתמונה (בתמונה $a=d$). אפשרות ג' מכילה איבר אחד בלבד כשהמימד $2$. באפשרות ד' שלושה איברים, אבל $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ לא בתמונה, והמימד $2$ ולא $3$.`,
      recap: "מתרגמים את עמודות הציר למטריצות." },
    { id: "C04-Q4",
      step: { type: "numeric",
        prompt: String.raw`$T(x,y,z)=(x+2y+z,\ 2x+y-z,\ x-y-2z)$. מהו $\dim\mathrm{Im}\,T$ ?`,
        answer: 2, tol: 0,
        explain: String.raw`המטריצה $\begin{pmatrix}1&2&1\\2&1&-1\\1&-1&-2\end{pmatrix}$ מתדרגת ל-$\begin{pmatrix}1&2&1\\0&-3&-3\\0&0&0\end{pmatrix}$, כלומר שתי עמודות ציר והדרגה $2$.` },
      recap: "ספרו עמודות ציר." },
    { id: "C04-Q5",
      question: String.raw`למה בסיס של $\mathrm{Im}\,T$ לוקחים מעמודות $A$ המקורית ולא מהמדורגת?`,
      options: [
        { id: "a", value: String.raw`פעולות שורה שומרות על התלות בין העמודות אבל משנות את העמודות עצמן, ולכן עמודות המדורגת לא בהכרח שייכות לתמונה` },
        { id: "b", value: String.raw`פעולות שורה משנות את התלות בין העמודות, ולכן מקומות הצירים משתנים` },
        { id: "c", value: String.raw`עמודות המדורגת תמיד תלויות לינארית` },
        { id: "d", value: String.raw`אין הבדל, אפשר לקחת כל אחת מהן` },
      ],
      correctId: "a",
      explanation: String.raw`פעולות שורה לא משנות אילו עמודות הן צירים ואיזה צירוף של עמודות נותן עמודה אחרת, ולכן מקומות הצירים נכונים, אבל הן כן משנות את הווקטורים עצמם: בדוגמה שבשיעור $(1,0,0)\notin\mathrm{Im}\,T$. לכן ב' שגויה (התלות נשמרת), ג' שגויה (עמודות הציר של המדורגת בלתי תלויות), וד' שגויה (עמודות המדורגת עלולות לצאת מהתמונה).`,
      recap: "מקומות הצירים מהמדורגת, הווקטורים מהמקורית." },
    { bankId: "22A-A-Q5a", recap: "Im מעמודות הציר של המקורית, Ker מפתרון המערכת ההומוגנית." },
  ],
});
