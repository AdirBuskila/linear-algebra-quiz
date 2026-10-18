/* kernel_image, level 8: boss, real exam question 5 */
COURSE_LEVEL("kernel_image", {
  id: "C08", order: 8, icon: "🏆", title: "בוס: שאלה 5 מהמבחן",
  goal: "לפתור סעיפים אמיתיים ממבחנים: גרעין ותמונה, חח״ע ועל, פרמטר, ומטריצה מייצגת.",
  source: "ai-verified", boss: true,
  lesson: { html: String.raw`
<p>בשאלה 5 של המבחן תמיד יש העתקה $T$ בין $\mathbb{R}_n[x]$, $M_{2\times2}(\mathbb{R})$ ו-$\mathbb{R}^4$, ולה אותם סעיפים. לפני שמתחילים, מורידים את $T$ למטריצה סטנדרטית $A$.</p>
<ul>
<li><b>בסיס ומימד של Im ו-Ker</b>: מדרגים את $A$. עמודות ציר <b>מהמקורית</b> לתמונה, משתנים חופשיים לגרעין, ותרגום חזרה לפולינומים או למטריצות.</li>
<li><b>חח״ע ועל</b>: $\dim\mathrm{Ker}\,T\neq0$ לא חח״ע, $\dim\mathrm{Im}\,T<\dim W$ לא על, עם ההשוואה במפורש.</li>
<li><b>פרמטר</b>: מערכת עם בסיס Im או Ker, ושורות האפסים נותנות את התנאים.</li>
<li><b>מטריצה מייצגת</b>: עמודה $j$ היא $[T(b_j)]_C$, או $([I]_E^C)^{-1}A[I]_E^B$.</li>
</ul>
<div class="lesson-rule">🔑 בדיקה עצמית: $\dim\mathrm{Ker}\,T+\dim\mathrm{Im}\,T=\dim V$.</div>
` },
  questions: [
    { bankId: "23A-A-Q5a", recap: "Im מעמודות הציר של המקורית; Ker ממשתנים חופשיים; תרגום חזרה למטריצות." },
    { bankId: "23A-A-Q5b", recap: "חח״ע: $\\dim\\mathrm{Ker}\\neq0$. על: $\\dim\\mathrm{Im}\\neq\\dim W$." },
    { bankId: "25A-A-Q5a", recap: "סדר: מטריצה סטנדרטית, דירוג, בסיסים, תרגום לפולינומים או מטריצות." },
    { bankId: "24A-A-Q5c", recap: "שתי שורות אפסים נותנות שני תנאים על שני פרמטרים." },
    { bankId: "25B-A-Q5c", recap: "הפרמטר נקבע מהשורה שמימינה לא אפס." },
    { bankId: "23A-A-Q5d", recap: "$[T]_C^B$: עמודה לכל $T(b_j)$ מפורק לפי $C$." },
  ],
});
