/* diagonalization, level 6: building P and D, checking AP=PD, powers */
COURSE_LEVEL("diagonalization", {
  id: "C06", order: 6, icon: "🛠️", title: "בניית P ו-D ובדיקה",
  goal: "לבנות $P$ ו-$D$ מהוקטורים והערכים העצמיים, לבדוק $AP=PD$, ולחשב חזקות.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כשיש מספיק וקטורים עצמיים, בונים את הליכסון כך:</p>
<div class="lesson-rule">🔑 <b>$P$</b> היא המטריצה שעמודותיה הוקטורים העצמיים. <b>$D$</b> אלכסונית עם הערכים העצמיים <b>באותו סדר</b>: העמודה $j$ של $P$ מתאימה לאיבר $j$ באלכסון של $D$. אז $AP=PD$.</div>
<p>הסיבה: העמודה $j$ של $AP$ היא $A\vec v_j=\lambda_j\vec v_j$, וזו בדיוק העמודה $j$ של $PD$. את הבדיקה מבצעים בחישוב <b>שני האגפים</b> $AP$ ו-$PD$, ואין צורך להפוך את $P$.</p>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ עם הוקטורים $(1,-2)^T$ עבור $\lambda=2$ ו-$(1,1)^T$ עבור $\lambda=5$:
$$P=\begin{pmatrix}1&1\\-2&1\end{pmatrix},\quad D=\begin{pmatrix}2&0\\0&5\end{pmatrix}.$$
$AP=\begin{pmatrix}2&5\\-4&5\end{pmatrix}$ וגם $PD=\begin{pmatrix}2&5\\-4&5\end{pmatrix}$.</div>
<p>חזקות: מ-$A=PDP^{-1}$ מקבלים $A^k=PD^kP^{-1}$, ו-$D^k$ אלכסונית עם הערכים בחזקת $k$. בפרט הערכים העצמיים של $A^k$ הם $\lambda^k$.</p>
<div class="lesson-trap">⚠️ מחליפים עמודות ב-$P$? מחליפים גם את האיברים התואמים ב-$D$. סדר שונה בין $P$ ל-$D$ הוא שגיאה נפוצה.</div>
` },
  questions: [
    { id: "C06-Q1",
      question: String.raw`ל-$A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ הערך העצמי $1$ עם הוקטור $(1,-2)^T$ והערך העצמי $4$ עם הוקטור $(1,1)^T$. איזה זוג $P,D$ מקיים $AP=PD$ ?`,
      options: [
        { id: "a", value: String.raw`$P=\begin{pmatrix}1&1\\-2&1\end{pmatrix},\ D=\begin{pmatrix}1&0\\0&4\end{pmatrix}$` },
        { id: "b", value: String.raw`$P=\begin{pmatrix}1&1\\-2&1\end{pmatrix},\ D=\begin{pmatrix}4&0\\0&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$P=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\ D=\begin{pmatrix}1&0\\0&4\end{pmatrix}$` },
        { id: "d", value: String.raw`$P=\begin{pmatrix}1&1\\-2&1\end{pmatrix},\ D=\begin{pmatrix}1&0\\0&1\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`בעמודה 1 של $P$ הוקטור של $\lambda=1$, ולכן $D_{11}=1$; בעמודה 2 הוקטור של $\lambda=4$, ולכן $D_{22}=4$. בב' סדר האלכסון הפוך. בג' העמודות של $P$ הן $(1,1)^T$ ו-$(1,-2)^T$ בסדר הפוך מה-$D$. בד' האלכסון חייב להכיל את הערכים העצמיים השונים.`,
      recap: "עמודה j של P תואמת לאיבר j של D." },
    { id: "C06-Q2",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ ו-$P=\begin{pmatrix}1&1\\-2&1\end{pmatrix}$. מהו האיבר בשורה 1 עמודה 2 של $AP$ ?`,
        answer: 4, tol: 0,
        explain: String.raw`זה המכפלה של שורה 1 של $A$ בעמודה 2 של $P$: $3\cdot1+1\cdot1=4$. אכן זה $4\cdot1$, כלומר $\lambda=4$ כפול האיבר הראשון בעמודה השנייה של $P$.` },
      recap: "AP עמודה־עמודה: A כפול כל וקטור." },
    { id: "C06-Q3",
      question: String.raw`בליכסון של $A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ בחרו $P=\begin{pmatrix}1&1\\-2&1\end{pmatrix}$ ו-$D=\mathrm{diag}(1,4)$. מחליפים בין שתי העמודות של $P$. מה צריך לעשות ב-$D$ כדי ש-$AP=PD$ ימשיך להתקיים?`,
      options: [
        { id: "a", value: String.raw`להחליף בין שני האיברים באלכסון, כלומר $D=\mathrm{diag}(4,1)$` },
        { id: "b", value: String.raw`להשאיר את $D$ כפי שהיא` },
        { id: "c", value: String.raw`להחליף את סימני שני האיברים` },
        { id: "d", value: String.raw`להפוך את $D$` },
      ],
      correctId: "a",
      explanation: String.raw`אחרי ההחלפה העמודה הראשונה של $P$ היא $(1,1)^T$ ששייכת ל-$\lambda=4$, ולכן $D_{11}=4$ ו-$D_{22}=1$. השארת $D$ כמות שהיא שוברת את $AP=PD$. החלפת סימנים או הפיכה נותנות ערכים שאינם ערכים עצמיים.`,
      recap: "מחליפים עמודות ב-P, מחליפים אותו דבר ב-D." },
    { id: "C06-Q4",
      step: { type: "numeric",
        prompt: String.raw`הערכים העצמיים של $A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ הם $1$ ו-$4$. מהו הערך העצמי הגדול של $A^5$ ?`,
        answer: 1024, tol: 0,
        explain: String.raw`הערכים העצמיים של $A^5$ הם $1^5=1$ ו-$4^5=1024$. הגדול הוא $1024$.` },
      recap: "לערכים העצמיים של A^k: λ^k." },
    { id: "C06-Q5",
      step: { type: "order",
        prompt: String.raw`סדרו את שלבי הליכסון של מטריצה $B$ מסדר 3.`,
        lines: [
          String.raw`מחשבים את $p(\lambda)=\det(\lambda I-B)$ ומוצאים את הערכים העצמיים`,
          String.raw`לכל ערך עצמי פותרים $(\lambda I-B)\vec x=\vec 0$ ומוצאים בסיס למרחב העצמי`,
          String.raw`בודקים שבכל ערך עצמי המימד הגיאומטרי שווה לאלגברי`,
          String.raw`בונים את $P$ מהוקטורים ואת $D$ מהערכים באותו סדר`,
          String.raw`מחשבים $BP$ ו-$PD$ ומראים שהם שווים`,
        ],
        explain: String.raw`אי אפשר לבנות את $P$ לפני שיודעים שיש מספיק וקטורים עצמיים (שלב הבדיקה), ואי אפשר לבדוק לפני שיש ערכים ומרחבים עצמיים. הבדיקה של $BP=PD$ היא האחרונה.` },
      recap: "ערכים, מרחבים, בדיקת ריבוי, P ו-D, בדיקה." },
    { id: "C06-Q6",
      step: { type: "findbug",
        prompt: String.raw`בבדיקה הבאה של $AP=PD$ עבור $A=\begin{pmatrix}3&1\\2&2\end{pmatrix}$, $P=\begin{pmatrix}1&1\\-2&1\end{pmatrix}$ ו-$D=\mathrm{diag}(1,4)$ שורה אחת שגויה. סמנו אותה.`,
        lines: [
          String.raw`$AP=\begin{pmatrix}1&4\\-2&4\end{pmatrix}$`,
          String.raw`$PD=\begin{pmatrix}1&1\\-2&1\end{pmatrix}\begin{pmatrix}1&0\\0&4\end{pmatrix}$`,
          String.raw`$PD=\begin{pmatrix}4&1\\-8&1\end{pmatrix}$`,
          String.raw`$AP=PD$ ולכן הליכסון נכון`,
        ],
        bugIndex: 2,
        explain: String.raw`כפל מימין ב-$D$ מכפיל כל עמודה בערך שלה: העמודה הראשונה ב-$1$ והשנייה ב-$4$, ולכן $PD=\begin{pmatrix}1&4\\-2&4\end{pmatrix}$. בשורה השגויה העמודות הוכפלו בסדר הפוך.` },
      recap: "PD: כל עמודה של P כפול הערך שלה." },
  ],
});
