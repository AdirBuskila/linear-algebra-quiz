window.COURSES = {
 "param_systems": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "🧱",
    "title": "מטריצה מורחבת ופעולות שורה",
    "goal": "לכתוב מערכת כמטריצה מורחבת, לבצע פעולות שורה, ולזהות איברים מובילים ומשתנים חופשיים.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>את המערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>2</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y=3,\\ 2x-y=0</annotation></semantics></math></span> כותבים בקיצור כ<b>מטריצה מורחבת</b>: כל משוואה היא שורה, כל נעלם הוא עמודה, ומימין לקו האנכי עומדים האיברים החופשיים.</p>\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center\" columnlines=\"none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{cc|c}1&amp;1&amp;3\\\\2&amp;-1&amp;0\\end{array}\\right)</annotation></semantics></math></span>\n<p>שלוש <b>פעולות שורה אלמנטריות</b> לא משנות את קבוצת הפתרונות:</p>\n<ul>\n<li>החלפת שתי שורות.</li>\n<li>הכפלת שורה בסקלר <b>שונה מאפס</b>.</li>\n<li>הוספת כפולה של שורה אחת לשורה אחרת, למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-2R_1</annotation></semantics></math></span>.</li>\n</ul>\n<p>המטרה היא <b>צורה מדורגת</b>: בכל שורה האיבר הראשון שאינו אפס (<b>האיבר המוביל</b>) נמצא ימינה מהאיבר המוביל של השורה שמעליה, ושורות האפסים בתחתית. עמודה של נעלם שאין בה איבר מוביל היא <b>משתנה חופשי</b>.</p>\n<div class=\"lesson-ex\">דוגמה: במערכת למעלה מבצעים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-2R_1</annotation></semantics></math></span> ומקבלים את השורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mo>−</mo><mn>6</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ -3\\,|\\,-6)</annotation></semantics></math></span>. כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn><mi>y</mi><mo>=</mo><mo>−</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">-3y=-6</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=2</annotation></semantics></math></span>. בהצבה לאחור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=3-2=1</annotation></semantics></math></span>.\nבדיקה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">1+2=3</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>⋅</mo><mn>1</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">2\\cdot1-2=0</annotation></semantics></math></span>.</div>\n<div class=\"lesson-rule\">🔑 פעולת שורה חוקית היא החלפה, הכפלה בסקלר שאינו אפס, או הוספת כפולה של שורה לשורה אחרת. הכפלה באפס מוחקת משוואה, ולכן אסורה.</div>\n<div class=\"lesson-trap\">⚠️ מחשבים את הפעולה על <b>כל</b> השורה כולל האיבר שמימין לקו. שוכחים אותו, והמערכת כבר לא שקולה למקורית.</div>\n"
    },
    "questions": [
     {
      "id": "C01-Q1",
      "question": "מהי המטריצה המורחבת של המערכת $x+2y-z=4,\\ 3x-y=2,\\ y+5z=7$ ?",
      "options": [
       {
        "id": "a",
        "value": "$\\left(\\begin{array}{ccc|c}1&2&-1&4\\\\3&-1&0&2\\\\0&1&5&7\\end{array}\\right)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>5</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>7</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;4\\\\3&amp;-1&amp;0&amp;2\\\\0&amp;1&amp;5&amp;7\\end{array}\\right)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$\\left(\\begin{array}{ccc|c}1&2&-1&4\\\\3&-1&2&0\\\\0&1&5&7\\end{array}\\right)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>5</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>7</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;4\\\\3&amp;-1&amp;2&amp;0\\\\0&amp;1&amp;5&amp;7\\end{array}\\right)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$\\left(\\begin{array}{ccc|c}1&2&-1&4\\\\3&-1&1&2\\\\0&1&5&7\\end{array}\\right)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>5</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>7</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;4\\\\3&amp;-1&amp;1&amp;2\\\\0&amp;1&amp;5&amp;7\\end{array}\\right)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$\\left(\\begin{array}{ccc|c}1&2&1&4\\\\3&-1&0&2\\\\0&1&5&7\\end{array}\\right)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>5</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>7</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;1&amp;4\\\\3&amp;-1&amp;0&amp;2\\\\0&amp;1&amp;5&amp;7\\end{array}\\right)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "בשורה השנייה אין z, ולכן המקדם שלו הוא $0$ והאיבר החופשי הוא $2$: $(3\\ \\ -1\\ \\ 0\\,|\\,2)$. אפשרות ב' שמה את $2$ במקום המקדם של $z$. אפשרות ג' כותבת $1$ במקום $0$ למשתנה שחסר. אפשרות ד' שוכחת את הסימן המינוס של $z$ בשורה הראשונה.",
      "recap": "נעלם שחסר במשוואה נכנס עם מקדם 0.",
      "questionHtml": "מהי המטריצה המורחבת של המערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>4</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>3</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>y</mi><mo>+</mo><mn>5</mn><mi>z</mi><mo>=</mo><mn>7</mn></mrow><annotation encoding=\"application/x-tex\">x+2y-z=4,\\ 3x-y=2,\\ y+5z=7</annotation></semantics></math></span> ?",
      "explanationHtml": "בשורה השנייה אין z, ולכן המקדם שלו הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> והאיבר החופשי הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mtext>  </mtext><mo>−</mo><mn>1</mn><mtext>  </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3\\ \\ -1\\ \\ 0\\,|\\,2)</annotation></semantics></math></span>. אפשרות ב' שמה את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> במקום המקדם של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi></mrow><annotation encoding=\"application/x-tex\">z</annotation></semantics></math></span>. אפשרות ג' כותבת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> במקום <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> למשתנה שחסר. אפשרות ד' שוכחת את הסימן המינוס של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi></mrow><annotation encoding=\"application/x-tex\">z</annotation></semantics></math></span> בשורה הראשונה.",
      "recapHtml": "נעלם שחסר במשוואה נכנס עם מקדם 0."
     },
     {
      "id": "C01-Q2",
      "step": {
       "type": "numeric",
       "prompt": "נתונות השורות $(1\\ \\ 2\\,|\\,4)$ ו-$(3\\ \\ 7\\,|\\,5)$. מבצעים $R_2\\to R_2-3R_1$. מהו האיבר שמימין לקו בשורה החדשה?",
       "answer": -7,
       "tol": 0,
       "explain": "$(3\\ \\ 7\\,|\\,5)-3(1\\ \\ 2\\,|\\,4)=(0\\ \\ 1\\,|\\,-7)$. האיבר מימין לקו הוא $5-12=-7$.",
       "promptHtml": "נתונות השורות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mtext>  </mtext><mn>2</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>4</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1\\ \\ 2\\,|\\,4)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mtext>  </mtext><mn>7</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>5</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3\\ \\ 7\\,|\\,5)</annotation></semantics></math></span>. מבצעים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mn>3</mn><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-3R_1</annotation></semantics></math></span>. מהו האיבר שמימין לקו בשורה החדשה?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mtext>  </mtext><mn>7</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>5</mn><mo stretchy=\"false\">)</mo><mo>−</mo><mn>3</mn><mo stretchy=\"false\">(</mo><mn>1</mn><mtext>  </mtext><mn>2</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>4</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mo>−</mo><mn>7</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3\\ \\ 7\\,|\\,5)-3(1\\ \\ 2\\,|\\,4)=(0\\ \\ 1\\,|\\,-7)</annotation></semantics></math></span>. האיבר מימין לקו הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>5</mn><mo>−</mo><mn>12</mn><mo>=</mo><mo>−</mo><mn>7</mn></mrow><annotation encoding=\"application/x-tex\">5-12=-7</annotation></semantics></math></span>."
      },
      "recap": "פעולת שורה פועלת גם על האיבר שמימין לקו.",
      "recapHtml": "פעולת שורה פועלת גם על האיבר שמימין לקו."
     },
     {
      "id": "C01-Q3",
      "question": "איזו מהפעולות הבאות אינה פעולת שורה אלמנטרית?",
      "options": [
       {
        "id": "a",
        "value": "החלפת שתי שורות",
        "type": "text",
        "html": "החלפת שתי שורות"
       },
       {
        "id": "b",
        "value": "הכפלת שורה ב-$-2$",
        "type": "text",
        "html": "הכפלת שורה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "הכפלת שורה ב-$0$",
        "type": "text",
        "html": "הכפלת שורה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "הוספת פעמיים שורה אחת לשורה אחרת",
        "type": "text",
        "html": "הוספת פעמיים שורה אחת לשורה אחרת"
       }
      ],
      "correctId": "c",
      "explanation": "הכפלה ב-$0$ הופכת משוואה ל-$0=0$ ומאבדת מידע, ולכן המערכת החדשה אינה שקולה. החלפה, הכפלה בסקלר שונה מאפס (כולל $-2$) והוספת כפולה של שורה לשורה אחרת כולן חוקיות.",
      "recap": "מכפילים רק בסקלר שונה מאפס.",
      "questionHtml": "איזו מהפעולות הבאות אינה פעולת שורה אלמנטרית?",
      "explanationHtml": "הכפלה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> הופכת משוואה ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0=0</annotation></semantics></math></span> ומאבדת מידע, ולכן המערכת החדשה אינה שקולה. החלפה, הכפלה בסקלר שונה מאפס (כולל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span>) והוספת כפולה של שורה לשורה אחרת כולן חוקיות.",
      "recapHtml": "מכפילים רק בסקלר שונה מאפס."
     },
     {
      "id": "C01-Q4",
      "step": {
       "type": "numeric",
       "prompt": "בצורה המדורגת $\\left(\\begin{array}{cccc|c}1&2&0&3&1\\\\0&0&1&4&2\\end{array}\\right)$ יש ארבעה נעלמים. כמה משתנים חופשיים יש?",
       "answer": 2,
       "tol": 0,
       "explain": "האיברים המובילים נמצאים בעמודות $1$ ו-$3$. בעמודות $2$ ו-$4$ אין איבר מוביל, ולכן שני משתנים חופשיים: $4-2=2$.",
       "promptHtml": "בצורה המדורגת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center center\" columnlines=\"none none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{cccc|c}1&amp;2&amp;0&amp;3&amp;1\\\\0&amp;0&amp;1&amp;4&amp;2\\end{array}\\right)</annotation></semantics></math></span> יש ארבעה נעלמים. כמה משתנים חופשיים יש?",
       "explainHtml": "האיברים המובילים נמצאים בעמודות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>. בעמודות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span> אין איבר מוביל, ולכן שני משתנים חופשיים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">4-2=2</annotation></semantics></math></span>."
      },
      "recap": "משתנה חופשי = עמודה בלי איבר מוביל.",
      "recapHtml": "משתנה חופשי = עמודה בלי איבר מוביל."
     },
     {
      "id": "C01-Q5",
      "step": {
       "type": "order",
       "prompt": "סדרו את שלבי הפתרון של המערכת $x+y=3,\\ 2x-y=0$.",
       "lines": [
        "כותבים את המטריצה המורחבת: שורות $(1\\ \\ 1\\,|\\,3)$ ו-$(2\\ \\ -1\\,|\\,0)$",
        "מאפסים מתחת לאיבר המוביל: $R_2\\to R_2-2R_1$ נותן $(0\\ \\ -3\\,|\\,-6)$",
        "מהשורה השנייה $y=2$",
        "מציבים לאחור בשורה הראשונה: $x=3-2=1$"
       ],
       "explain": "קודם בונים את המטריצה, אחר כך מדרגים, ואז קוראים את הנעלם האחרון ומציבים לאחור. אי אפשר לחשב את $x$ לפני שיודעים את $y$.",
       "promptHtml": "סדרו את שלבי הפתרון של המערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>2</mn><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y=3,\\ 2x-y=0</annotation></semantics></math></span>.",
       "explainHtml": "קודם בונים את המטריצה, אחר כך מדרגים, ואז קוראים את הנעלם האחרון ומציבים לאחור. אי אפשר לחשב את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> לפני שיודעים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>.",
       "linesHtml": [
        "כותבים את המטריצה המורחבת: שורות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mtext>  </mtext><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1\\ \\ 1\\,|\\,3)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mtext>  </mtext><mo>−</mo><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2\\ \\ -1\\,|\\,0)</annotation></semantics></math></span>",
        "מאפסים מתחת לאיבר המוביל: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-2R_1</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mo>−</mo><mn>6</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ -3\\,|\\,-6)</annotation></semantics></math></span>",
        "מהשורה השנייה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=2</annotation></semantics></math></span>",
        "מציבים לאחור בשורה הראשונה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=3-2=1</annotation></semantics></math></span>"
       ]
      },
      "recap": "בונים, מדרגים, קוראים מלמטה, מציבים לאחור.",
      "recapHtml": "בונים, מדרגים, קוראים מלמטה, מציבים לאחור."
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "📊",
    "title": "דרגה ומשפט הפתרונות",
    "goal": "להסתכל על צורה מדורגת ולקבוע: אין פתרון, פתרון יחיד או אינסוף פתרונות.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p><b>הדרגה</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">r(A)</annotation></semantics></math></span> היא מספר השורות השונות מאפס בצורה המדורגת של מטריצת המקדמים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>A</mi></mrow><annotation encoding=\"application/x-tex\">A</annotation></semantics></math></span>. הדרגה של המטריצה המורחבת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mi mathvariant=\"normal\">∣</mi><mi>b</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">r(A|b)</annotation></semantics></math></span> נספרת בצורה המדורגת של המטריצה כולה, כולל העמודה שמימין לקו.</p>\n<div class=\"lesson-rule\">🔑 <b>משפט הפתרונות</b>, למערכת עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> נעלמים:\n<ul>\n<li>אם יש שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mo>⋯</mo><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>c</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ \\cdots\\ 0\\,|\\,c)</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>c</mi><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">c\\neq0</annotation></semantics></math></span> (כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo><mo>&lt;</mo><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mi mathvariant=\"normal\">∣</mi><mi>b</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">r(A)&lt;r(A|b)</annotation></semantics></math></span>): <b>אין פתרון</b>.</li>\n<li>אחרת, אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">r(A)=n</annotation></semantics></math></span>: <b>פתרון יחיד</b>.</li>\n<li>אחרת, אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo><mo>&lt;</mo><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">r(A)&lt;n</annotation></semantics></math></span>: <b>אינסוף פתרונות</b>, עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">n-r(A)</annotation></semantics></math></span> משתנים חופשיים.</li>\n</ul></div>\n<div class=\"lesson-ex\">בצורה המדורגת\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>6</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>8</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;1&amp;1&amp;6\\\\0&amp;1&amp;2&amp;8\\\\0&amp;0&amp;1&amp;3\\end{array}\\right)</annotation></semantics></math></span>\nהדרגה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>=</mo><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">3=n</annotation></semantics></math></span>, ולכן פתרון יחיד. מהשורה האחרונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">z=3</annotation></semantics></math></span>, אחר כך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>8</mn><mo>−</mo><mn>2</mn><mo>⋅</mo><mn>3</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=8-2\\cdot3=2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>6</mn><mo>−</mo><mn>2</mn><mo>−</mo><mn>3</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=6-2-3=1</annotation></semantics></math></span>. בדיקה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">1+2+3=6</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ שורת אפסים <b>שלמה</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,0)</annotation></semantics></math></span> לא סותרת: היא רק אומרת שמשוואה הייתה מיותרת. הסתירה היא רק שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>c</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,c)</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>c</mi><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">c\\neq0</annotation></semantics></math></span>. כשיש יותר משוואות מנעלמים, שורות אפסים כאלה נפוצות ואינן מקטינות את מספר הפתרונות.</div>\n<p>מערכת לינארית אף פעם לא מקבלת בדיוק שני פתרונות: או אפס, או אחד, או אינסוף.</p>\n"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "question": "מערכת מדורגת: $\\left(\\begin{array}{ccc|c}1&2&3&4\\\\0&1&1&2\\\\0&0&0&5\\end{array}\\right)$. מה מספר הפתרונות?",
      "options": [
       {
        "id": "a",
        "value": "אין פתרון",
        "type": "text",
        "html": "אין פתרון"
       },
       {
        "id": "b",
        "value": "פתרון יחיד",
        "type": "text",
        "html": "פתרון יחיד"
       },
       {
        "id": "c",
        "value": "אינסוף פתרונות",
        "type": "text",
        "html": "אינסוף פתרונות"
       },
       {
        "id": "d",
        "value": "אי אפשר לדעת בלי לדרג שוב",
        "type": "text",
        "html": "אי אפשר לדעת בלי לדרג שוב"
       }
      ],
      "correctId": "a",
      "explanation": "השורה האחרונה היא $0=5$, סתירה. זה המקרה $r(A)=2<3=r(A|b)$. אין צורך לדרג שוב, והמערכת כבר מדורגת.",
      "recap": "שורה (0 0 0 | c) עם c שונה מאפס = אין פתרון.",
      "questionHtml": "מערכת מדורגת: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>5</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;3&amp;4\\\\0&amp;1&amp;1&amp;2\\\\0&amp;0&amp;0&amp;5\\end{array}\\right)</annotation></semantics></math></span>. מה מספר הפתרונות?",
      "explanationHtml": "השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">0=5</annotation></semantics></math></span>, סתירה. זה המקרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn><mo>&lt;</mo><mn>3</mn><mo>=</mo><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mi mathvariant=\"normal\">∣</mi><mi>b</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">r(A)=2&lt;3=r(A|b)</annotation></semantics></math></span>. אין צורך לדרג שוב, והמערכת כבר מדורגת.",
      "recapHtml": "שורה (0 0 0 | c) עם c שונה מאפס = אין פתרון."
     },
     {
      "id": "C02-Q2",
      "question": "אותה מטריצה, אבל בשורה האחרונה האיבר החופשי הוא $0$: $\\left(\\begin{array}{ccc|c}1&2&3&4\\\\0&1&1&2\\\\0&0&0&0\\end{array}\\right)$. מה מספר הפתרונות?",
      "options": [
       {
        "id": "a",
        "value": "אין פתרון",
        "type": "text",
        "html": "אין פתרון"
       },
       {
        "id": "b",
        "value": "פתרון יחיד",
        "type": "text",
        "html": "פתרון יחיד"
       },
       {
        "id": "c",
        "value": "אינסוף פתרונות, עם משתנה חופשי אחד",
        "type": "text",
        "html": "אינסוף פתרונות, עם משתנה חופשי אחד"
       },
       {
        "id": "d",
        "value": "אינסוף פתרונות, עם שני משתנים חופשיים",
        "type": "text",
        "html": "אינסוף פתרונות, עם שני משתנים חופשיים"
       }
      ],
      "correctId": "c",
      "explanation": "$0=0$ היא משוואה נכונה תמיד. הדרגה היא $2$ ויש $3$ נעלמים, ולכן $3-2=1$ משתנה חופשי ואינסוף פתרונות. שני משתנים חופשיים היו נדרשים לדרגה $1$.",
      "recap": "שורת אפסים שלמה לא סותרת: n פחות הדרגה = חופשיים.",
      "questionHtml": "אותה מטריצה, אבל בשורה האחרונה האיבר החופשי הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>4</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;3&amp;4\\\\0&amp;1&amp;1&amp;2\\\\0&amp;0&amp;0&amp;0\\end{array}\\right)</annotation></semantics></math></span>. מה מספר הפתרונות?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0=0</annotation></semantics></math></span> היא משוואה נכונה תמיד. הדרגה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ויש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span> נעלמים, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">3-2=1</annotation></semantics></math></span> משתנה חופשי ואינסוף פתרונות. שני משתנים חופשיים היו נדרשים לדרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>.",
      "recapHtml": "שורת אפסים שלמה לא סותרת: n פחות הדרגה = חופשיים."
     },
     {
      "id": "C02-Q3",
      "step": {
       "type": "numeric",
       "prompt": "המערכת המדורגת $\\left(\\begin{array}{ccc|c}1&1&1&6\\\\0&1&2&8\\\\0&0&1&3\\end{array}\\right)$ מתאימה לנעלמים $x,y,z$. מהו $x$ ?",
       "answer": 1,
       "tol": 0,
       "explain": "$z=3$, אחר כך $y=8-2\\cdot3=2$ ו-$x=6-y-z=6-2-3=1$.",
       "promptHtml": "המערכת המדורגת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>6</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>8</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;1&amp;1&amp;6\\\\0&amp;1&amp;2&amp;8\\\\0&amp;0&amp;1&amp;3\\end{array}\\right)</annotation></semantics></math></span> מתאימה לנעלמים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi></mrow><annotation encoding=\"application/x-tex\">x,y,z</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">z=3</annotation></semantics></math></span>, אחר כך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>8</mn><mo>−</mo><mn>2</mn><mo>⋅</mo><mn>3</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=8-2\\cdot3=2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>6</mn><mo>−</mo><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>6</mn><mo>−</mo><mn>2</mn><mo>−</mo><mn>3</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=6-y-z=6-2-3=1</annotation></semantics></math></span>."
      },
      "recap": "פתרון יחיד: הצבה לאחור מהשורה האחרונה.",
      "recapHtml": "פתרון יחיד: הצבה לאחור מהשורה האחרונה."
     },
     {
      "id": "C02-Q4",
      "question": "למערכת של $4$ משוואות ב-$2$ נעלמים יש מטריצה מורחבת שהצורה המדורגת שלה היא $\\left(\\begin{array}{cc|c}1&0&1\\\\0&1&2\\\\0&0&0\\\\0&0&0\\end{array}\\right)$. מה מספר הפתרונות?",
      "options": [
       {
        "id": "a",
        "value": "אין פתרון, כי יש יותר משוואות מנעלמים",
        "type": "text",
        "html": "אין פתרון, כי יש יותר משוואות מנעלמים"
       },
       {
        "id": "b",
        "value": "פתרון יחיד",
        "type": "text",
        "html": "פתרון יחיד"
       },
       {
        "id": "c",
        "value": "אינסוף פתרונות",
        "type": "text",
        "html": "אינסוף פתרונות"
       },
       {
        "id": "d",
        "value": "שני פתרונות",
        "type": "text",
        "html": "שני פתרונות"
       }
      ],
      "correctId": "b",
      "explanation": "הדרגה היא $2=n$ ואין שורת סתירה, ולכן פתרון יחיד: $x=1,\\ y=2$. שתי שורות האפסים הן משוואות מיותרות ולא סתירה. מספר המשוואות לבדו לא קובע כלום, ושני פתרונות בדיוק אינם אפשריים.",
      "recap": "מה שקובע הוא הדרגה ושורות סתירה, לא מספר המשוואות.",
      "questionHtml": "למערכת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span> משוואות ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> נעלמים יש מטריצה מורחבת שהצורה המדורגת שלה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center\" columnlines=\"none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{cc|c}1&amp;0&amp;1\\\\0&amp;1&amp;2\\\\0&amp;0&amp;0\\\\0&amp;0&amp;0\\end{array}\\right)</annotation></semantics></math></span>. מה מספר הפתרונות?",
      "explanationHtml": "הדרגה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>=</mo><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">2=n</annotation></semantics></math></span> ואין שורת סתירה, ולכן פתרון יחיד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>y</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=1,\\ y=2</annotation></semantics></math></span>. שתי שורות האפסים הן משוואות מיותרות ולא סתירה. מספר המשוואות לבדו לא קובע כלום, ושני פתרונות בדיוק אינם אפשריים.",
      "recapHtml": "מה שקובע הוא הדרגה ושורות סתירה, לא מספר המשוואות."
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "numeric",
       "prompt": "למערכת עם $5$ נעלמים מתקיים $r(A)=r(A|b)=3$. כמה משתנים חופשיים יש?",
       "answer": 2,
       "tol": 0,
       "explain": "הדרגות שוות, ולכן יש פתרון. מספר המשתנים החופשיים הוא $n-r(A)=5-3=2$.",
       "promptHtml": "למערכת עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">5</annotation></semantics></math></span> נעלמים מתקיים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mi mathvariant=\"normal\">∣</mi><mi>b</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">r(A)=r(A|b)=3</annotation></semantics></math></span>. כמה משתנים חופשיים יש?",
       "explainHtml": "הדרגות שוות, ולכן יש פתרון. מספר המשתנים החופשיים הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>5</mn><mo>−</mo><mn>3</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">n-r(A)=5-3=2</annotation></semantics></math></span>."
      },
      "recap": "חופשיים = n פחות r(A).",
      "recapHtml": "חופשיים = n פחות r(A)."
     },
     {
      "id": "C02-Q6",
      "question": "מערכת של משוואות לינאריות ממשיות יכולה להיות בעלת בדיוק כמה פתרונות?",
      "options": [
       {
        "id": "a",
        "value": "0, 1 או אינסוף",
        "type": "text",
        "html": "0, 1 או אינסוף"
       },
       {
        "id": "b",
        "value": "0, 1, 2 או אינסוף",
        "type": "text",
        "html": "0, 1, 2 או אינסוף"
       },
       {
        "id": "c",
        "value": "תמיד לפחות פתרון אחד",
        "type": "text",
        "html": "תמיד לפחות פתרון אחד"
       },
       {
        "id": "d",
        "value": "תמיד אינסוף פתרונות כשיש פחות משוואות מנעלמים",
        "type": "text",
        "html": "תמיד אינסוף פתרונות כשיש פחות משוואות מנעלמים"
       }
      ],
      "correctId": "a",
      "explanation": "לפי משפט הפתרונות יש רק שלוש אפשרויות: אין פתרון, פתרון יחיד או אינסוף. אפשרות ג' שגויה כי יש מערכות סותרות. אפשרות ד' שגויה כי מערכת עם פחות משוואות מנעלמים יכולה להיות סותרת, למשל $x+y+z=1,\\ x+y+z=2$.",
      "recap": "אפס, אחד או אינסוף. אף פעם שניים.",
      "questionHtml": "מערכת של משוואות לינאריות ממשיות יכולה להיות בעלת בדיוק כמה פתרונות?",
      "explanationHtml": "לפי משפט הפתרונות יש רק שלוש אפשרויות: אין פתרון, פתרון יחיד או אינסוף. אפשרות ג' שגויה כי יש מערכות סותרות. אפשרות ד' שגויה כי מערכת עם פחות משוואות מנעלמים יכולה להיות סותרת, למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+y+z=2</annotation></semantics></math></span>.",
      "recapHtml": "אפס, אחד או אינסוף. אף פעם שניים."
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "🧭",
    "title": "פתרון כללי: פרמטר חופשי",
    "goal": "לכתוב את קבוצת הפתרונות של מערכת עם משתנה חופשי בצורה של פתרון פרטי ועוד פרמטר כפול וקטור כיוון.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>כשיש משתנה חופשי, מסמנים אותו באות, למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>∈</mo><mi mathvariant=\"double-struck\">R</mi></mrow><annotation encoding=\"application/x-tex\">t\\in\\mathbb{R}</annotation></semantics></math></span>, ומבטאים את שאר הנעלמים באמצעותה, מהשורה האחרונה כלפי מעלה. התוצאה נכתבת כ<b>פתרון כללי</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>x</mi><mo>⃗</mo></mover><mo>=</mo><mover accent=\"true\"><mi>p</mi><mo>⃗</mo></mover><mo>+</mo><mi>t</mi><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec x=\\vec p+t\\vec d</annotation></semantics></math></span>: וקטור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>p</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec p</annotation></semantics></math></span> קבוע (פתרון פרטי) ועוד <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">t</annotation></semantics></math></span> כפול וקטור כיוון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec d</annotation></semantics></math></span>.</p>\n<div class=\"lesson-ex\">נפתור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2</annotation></semantics></math></span>. הפעולה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-R_1</annotation></semantics></math></span> נותנת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>1</mn><mtext>  </mtext><mn>2</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 1\\ \\ 2\\,|\\,1)</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y+2z=1</annotation></semantics></math></span>. העמודה השלישית בלי איבר מוביל, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>.\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>2</mn><mi>t</mi><mo separator=\"true\">,</mo><mspace width=\"2em\"/><mi>x</mi><mo>=</mo><mn>1</mn><mo>−</mo><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>−</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mn>2</mn><mi>t</mi><mo stretchy=\"false\">)</mo><mo>−</mo><mi>t</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-2t,\\qquad x=1-y-z=1-(1-2t)-t=t</annotation></semantics></math></span>\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mtext> </mtext><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x,y,z)=(0,1,0)+t\\,(1,-2,1)</annotation></semantics></math></span>\nבדיקה במשוואה השנייה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mn>2</mn><mi>t</mi><mo stretchy=\"false\">)</mo><mo>+</mo><mn>3</mn><mi>t</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">t+2(1-2t)+3t=2</annotation></semantics></math></span>.</div>\n<div class=\"lesson-rule\">🔑 וקטור הכיוון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec d</annotation></semantics></math></span> הוא פתרון של המערכת ההומוגנית (אותו אגף שמאל עם אפסים מימין). הפתרון הפרטי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>p</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec p</annotation></semantics></math></span> מתקבל מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">t=0</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ מציבים חזרה במערכת <b>המקורית</b> כדי לבדוק. הצבת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">t=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">t=1</annotation></semantics></math></span> בכל המשוואות מגלה כמעט כל טעות.</div>\n"
    },
    "questions": [
     {
      "id": "C03-Q1",
      "step": {
       "type": "numeric",
       "prompt": "הצורה המדורגת היא $\\left(\\begin{array}{ccc|c}1&2&-1&3\\\\0&1&3&1\\end{array}\\right)$ והמשתנה החופשי הוא $z=t$. מהו $y$ כאשר $t=2$ ?",
       "answer": -5,
       "tol": 0,
       "explain": "מהשורה השנייה $y=1-3z=1-3t$. עבור $t=2$ מקבלים $y=1-6=-5$.",
       "promptHtml": "הצורה המדורגת היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;3\\\\0&amp;1&amp;3&amp;1\\end{array}\\right)</annotation></semantics></math></span> והמשתנה החופשי הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">t=2</annotation></semantics></math></span> ?",
       "explainHtml": "מהשורה השנייה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-3z=1-3t</annotation></semantics></math></span>. עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">t=2</annotation></semantics></math></span> מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>6</mn><mo>=</mo><mo>−</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">y=1-6=-5</annotation></semantics></math></span>."
      },
      "recap": "מבטאים כל נעלם מובל דרך המשתנה החופשי, מלמטה למעלה.",
      "recapHtml": "מבטאים כל נעלם מובל דרך המשתנה החופשי, מלמטה למעלה."
     },
     {
      "id": "C03-Q2",
      "question": "אותה צורה מדורגת, $\\left(\\begin{array}{ccc|c}1&2&-1&3\\\\0&1&3&1\\end{array}\\right)$ עם $z=t$. מהו הפתרון הכללי $(x,y,z)$ ?",
      "options": [
       {
        "id": "a",
        "value": "$(1,1,0)+t\\,(7,-3,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mtext> </mtext><mo stretchy=\"false\">(</mo><mn>7</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,1,0)+t\\,(7,-3,1)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$(1,1,0)+t\\,(-7,3,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mtext> </mtext><mo stretchy=\"false\">(</mo><mo>−</mo><mn>7</mn><mo separator=\"true\">,</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,1,0)+t\\,(-7,3,1)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$(3,1,0)+t\\,(7,-3,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mtext> </mtext><mo stretchy=\"false\">(</mo><mn>7</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3,1,0)+t\\,(7,-3,1)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$(1,1,0)+t\\,(7,3,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mtext> </mtext><mo stretchy=\"false\">(</mo><mn>7</mn><mo separator=\"true\">,</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,1,0)+t\\,(7,3,1)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$y=1-3t$ ו-$x=3-2y+z=3-2(1-3t)+t=1+7t$. לכן $(x,y,z)=(1,1,0)+t(7,-3,1)$. אפשרות ב' הופכת סימן בווקטור הכיוון. אפשרות ג' לוקחת את האיבר החופשי $3$ במקום הפתרון הפרטי. אפשרות ד' מחמיצה את הסימן של $y$.",
      "recap": "x = (איבר חופשי) פחות מקדמים כפול הנעלמים שכבר חושבו.",
      "questionHtml": "אותה צורה מדורגת, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;3\\\\0&amp;1&amp;3&amp;1\\end{array}\\right)</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>. מהו הפתרון הכללי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x,y,z)</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-3t</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>7</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">x=3-2y+z=3-2(1-3t)+t=1+7t</annotation></semantics></math></span>. לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mo stretchy=\"false\">(</mo><mn>7</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x,y,z)=(1,1,0)+t(7,-3,1)</annotation></semantics></math></span>. אפשרות ב' הופכת סימן בווקטור הכיוון. אפשרות ג' לוקחת את האיבר החופשי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span> במקום הפתרון הפרטי. אפשרות ד' מחמיצה את הסימן של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>.",
      "recapHtml": "x = (איבר חופשי) פחות מקדמים כפול הנעלמים שכבר חושבו."
     },
     {
      "id": "C03-Q3",
      "question": "איזה מהווקטורים הבאים הוא פתרון של המערכת $x+2y-z=3,\\ y+3z=1$ ?",
      "options": [
       {
        "id": "a",
        "value": "$(8,-2,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>8</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(8,-2,1)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$(8,2,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>8</mn><mo separator=\"true\">,</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(8,2,1)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$(1,1,1)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,1,1)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$(3,1,0)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3,1,0)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$(8,-2,1)$ מקיים $8-4-1=3$ וגם $-2+3=1$. עבור $(8,2,1)$ המשוואה השנייה נותנת $2+3=5\\neq1$. עבור $(1,1,1)$ המשוואה הראשונה נותנת $1+2-1=2\\neq3$. עבור $(3,1,0)$ המשוואה השנייה נותנת $1+0=1$ אבל הראשונה $3+2-0=5\\neq3$.",
      "recap": "בודקים פתרון בכל המשוואות המקוריות.",
      "questionHtml": "איזה מהווקטורים הבאים הוא פתרון של המערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x+2y-z=3,\\ y+3z=1</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>8</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(8,-2,1)</annotation></semantics></math></span> מקיים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>8</mn><mo>−</mo><mn>4</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">8-4-1=3</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-2+3=1</annotation></semantics></math></span>. עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>8</mn><mo separator=\"true\">,</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(8,2,1)</annotation></semantics></math></span> המשוואה השנייה נותנת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">2+3=5\\neq1</annotation></semantics></math></span>. עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,1,1)</annotation></semantics></math></span> המשוואה הראשונה נותנת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">1+2-1=2\\neq3</annotation></semantics></math></span>. עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3,1,0)</annotation></semantics></math></span> המשוואה השנייה נותנת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>0</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1+0=1</annotation></semantics></math></span> אבל הראשונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mo>−</mo><mn>0</mn><mo>=</mo><mn>5</mn><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3+2-0=5\\neq3</annotation></semantics></math></span>.",
      "recapHtml": "בודקים פתרון בכל המשוואות המקוריות."
     },
     {
      "id": "C03-Q4",
      "step": {
       "type": "order",
       "prompt": "סדרו את שלבי כתיבת הפתרון הכללי של $\\left(\\begin{array}{ccc|c}1&2&-1&3\\\\0&1&3&1\\end{array}\\right)$.",
       "lines": [
        "עמודה $3$ בלי איבר מוביל, ולכן $z$ חופשי",
        "מסמנים $z=t$",
        "מהשורה השנייה $y=1-3t$",
        "מהשורה הראשונה $x=3-2y+z=1+7t$",
        "כותבים $(x,y,z)=(1,1,0)+t(7,-3,1)$"
       ],
       "explain": "קודם מזהים את המשתנה החופשי, אחר כך $y$ מהשורה התחתונה, ורק אז $x$ כי הוא תלוי ב-$y$. הווקטור נכתב אחרון.",
       "promptHtml": "סדרו את שלבי כתיבת הפתרון הכללי של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;3\\\\0&amp;1&amp;3&amp;1\\end{array}\\right)</annotation></semantics></math></span>.",
       "explainHtml": "קודם מזהים את המשתנה החופשי, אחר כך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> מהשורה התחתונה, ורק אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> כי הוא תלוי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>. הווקטור נכתב אחרון.",
       "linesHtml": [
        "עמודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span> בלי איבר מוביל, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi></mrow><annotation encoding=\"application/x-tex\">z</annotation></semantics></math></span> חופשי",
        "מסמנים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>",
        "מהשורה השנייה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-3t</annotation></semantics></math></span>",
        "מהשורה הראשונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>7</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">x=3-2y+z=1+7t</annotation></semantics></math></span>",
        "כותבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mo stretchy=\"false\">(</mo><mn>7</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x,y,z)=(1,1,0)+t(7,-3,1)</annotation></semantics></math></span>"
       ]
      },
      "recap": "חופשי, פרמטר, מלמטה למעלה, וקטור.",
      "recapHtml": "חופשי, פרמטר, מלמטה למעלה, וקטור."
     },
     {
      "id": "C03-Q5",
      "step": {
       "type": "findbug",
       "prompt": "באחד השלבים בפתרון של $\\left(\\begin{array}{ccc|c}1&2&-1&3\\\\0&1&3&1\\end{array}\\right)$ יש טעות חשבונית. איזה?",
       "lines": [
        "מסמנים $z=t$",
        "מהשורה השנייה $y=1-3t$",
        "מהשורה הראשונה $x=3-2y+z$",
        "מציבים: $x=3-2(1-3t)+t=1+5t$"
       ],
       "bugIndex": 3,
       "explain": "$3-2(1-3t)+t=3-2+6t+t=1+7t$, לא $1+5t$. שלוש השורות האחרות נכונות.",
       "promptHtml": "באחד השלבים בפתרון של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo fence=\"true\">(</mo><mtable rowspacing=\"0.16em\" columnalign=\"center center center center\" columnlines=\"none none solid\" columnspacing=\"1em\"><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>2</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mrow><mo>−</mo><mn>1</mn></mrow></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd></mtr><mtr><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>0</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>3</mn></mstyle></mtd><mtd><mstyle scriptlevel=\"0\" displaystyle=\"false\"><mn>1</mn></mstyle></mtd></mtr></mtable><mo fence=\"true\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\left(\\begin{array}{ccc|c}1&amp;2&amp;-1&amp;3\\\\0&amp;1&amp;3&amp;1\\end{array}\\right)</annotation></semantics></math></span> יש טעות חשבונית. איזה?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>−</mo><mn>2</mn><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo>+</mo><mn>6</mn><mi>t</mi><mo>+</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>7</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">3-2(1-3t)+t=3-2+6t+t=1+7t</annotation></semantics></math></span>, לא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">1+5t</annotation></semantics></math></span>. שלוש השורות האחרות נכונות.",
       "linesHtml": [
        "מסמנים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>",
        "מהשורה השנייה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-3t</annotation></semantics></math></span>",
        "מהשורה הראשונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>z</mi></mrow><annotation encoding=\"application/x-tex\">x=3-2y+z</annotation></semantics></math></span>",
        "מציבים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mn>3</mn><mi>t</mi><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>5</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">x=3-2(1-3t)+t=1+5t</annotation></semantics></math></span>"
       ]
      },
      "recap": "בהצבה לאחור שמים לב לסימן: מינוס כפול מינוס.",
      "recapHtml": "בהצבה לאחור שמים לב לסימן: מינוס כפול מינוס."
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "🎚️",
    "title": "פרמטר ראשון: השורה האחרונה",
    "goal": "לדרג מערכת עם פרמטר, למצוא את הערכים הקריטיים ולסווג: פתרון יחיד, אין פתרון או אינסוף.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>במערכת עם פרמטר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> מדרגים כרגיל. אחרי הדירוג השורה האחרונה היא מהצורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>q</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ p(k)\\,|\\,q(k))</annotation></semantics></math></span>. <b>הערכים הקריטיים</b> הם האפסים של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">p(k)</annotation></semantics></math></span>.</p>\n<div class=\"lesson-rule\">🔑 מתכון:\n<ul>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p(k)\\neq0</annotation></semantics></math></span>: פתרון יחיד.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p(k)=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q(k)\\neq0</annotation></semantics></math></span>: אין פתרון.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p(k)=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q(k)=0</annotation></semantics></math></span>: אינסוף פתרונות.</li>\n</ul>\nבכל ערך קריטי מציבים אותו ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">q(k)</annotation></semantics></math></span> ובודקים.</div>\n<div class=\"lesson-ex\">נבחן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=k</annotation></semantics></math></span>. הפעולות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2-R_1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>3</mn></msub><mo>−</mo><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_3-R_1</annotation></semantics></math></span> נותנות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>1</mn><mtext> </mtext><mn>2</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 1\\ 2\\,|\\,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>1</mn><mtext> </mtext><mi>k</mi><mo>−</mo><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 1\\ k-1\\,|\\,k-1)</annotation></semantics></math></span>. אחר כך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>3</mn></msub><mo>−</mo><msub><mi>R</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_3-R_2</annotation></semantics></math></span> נותן\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ k-3\\,|\\,k-2)</annotation></semantics></math></span>\nאפס של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>k</mi><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">p(k)=k-3</annotation></semantics></math></span> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span>. עבורו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>1</mn><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q(3)=1\\neq0</annotation></semantics></math></span>, ולכן <b>אין פתרון</b>. לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq3</annotation></semantics></math></span> יש פתרון יחיד.\nאם האיבר החופשי בשורה השלישית היה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> במקום <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span>, השורה האחרונה הייתה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ k-3\\,|\\,0)</annotation></semantics></math></span>, וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> היו <b>אינסוף</b> פתרונות.</div>\n<div class=\"lesson-trap\">⚠️ אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">q(k)</annotation></semantics></math></span> הוא כפולה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">p(k)</annotation></semantics></math></span>, למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>3</mn><mo>−</mo><mi>k</mi><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 3-k\\,|\\,k-3)</annotation></semantics></math></span>, אז בכל ערך קריטי גם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q=0</annotation></semantics></math></span>, ולכן אף ערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> לא נותן \"אין פתרון\".</div>\n"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "step": {
       "type": "numeric",
       "prompt": "אחרי דירוג המערכת $x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=k$ השורה האחרונה היא $(0\\ \\ 0\\ \\ k-3\\,|\\,k-2)$. מהו הערך הקריטי של $k$ ?",
       "answer": 3,
       "tol": 0,
       "explain": "האפס של $p(k)=k-3$ הוא $k=3$.",
       "promptHtml": "אחרי דירוג המערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=k</annotation></semantics></math></span> השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ k-3\\,|\\,k-2)</annotation></semantics></math></span>. מהו הערך הקריטי של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> ?",
       "explainHtml": "האפס של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>k</mi><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">p(k)=k-3</annotation></semantics></math></span> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span>."
      },
      "recap": "ערך קריטי = אפס של המקדם האחרון.",
      "recapHtml": "ערך קריטי = אפס של המקדם האחרון."
     },
     {
      "id": "C04-Q2",
      "question": "באותה מערכת, מה קורה כאשר $k=3$ ? השורה האחרונה היא $(0\\ \\ 0\\ \\ k-3\\,|\\,k-2)$.",
      "options": [
       {
        "id": "a",
        "value": "אין פתרון",
        "type": "text",
        "html": "אין פתרון"
       },
       {
        "id": "b",
        "value": "פתרון יחיד",
        "type": "text",
        "html": "פתרון יחיד"
       },
       {
        "id": "c",
        "value": "אינסוף פתרונות",
        "type": "text",
        "html": "אינסוף פתרונות"
       },
       {
        "id": "d",
        "value": "לא ניתן לקבוע בלי לדעת את הפתרון",
        "type": "text",
        "html": "לא ניתן לקבוע בלי לדעת את הפתרון"
       }
      ],
      "correctId": "a",
      "explanation": "ב-$k=3$ השורה היא $(0\\ 0\\ 0\\,|\\,1)$, כלומר $0=1$: סתירה. פתרון יחיד היה דורש $p(k)\\neq0$. אינסוף פתרונות היה דורש $q(3)=0$, אבל $q(3)=3-2=1$.",
      "recap": "בערך קריטי: מציבים ב-q. שונה מאפס = אין פתרון.",
      "questionHtml": "באותה מערכת, מה קורה כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> ? השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ k-3\\,|\\,k-2)</annotation></semantics></math></span>.",
      "explanationHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> השורה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,1)</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">0=1</annotation></semantics></math></span>: סתירה. פתרון יחיד היה דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p(k)\\neq0</annotation></semantics></math></span>. אינסוף פתרונות היה דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q(3)=0</annotation></semantics></math></span>, אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo stretchy=\"false\">(</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">q(3)=3-2=1</annotation></semantics></math></span>.",
      "recapHtml": "בערך קריטי: מציבים ב-q. שונה מאפס = אין פתרון."
     },
     {
      "id": "C04-Q3",
      "question": "במערכת $x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=2$ השורה האחרונה אחרי דירוג היא $(0\\ \\ 0\\ \\ k-3\\,|\\,0)$. מה נכון?",
      "options": [
       {
        "id": "a",
        "value": "$k\\neq3$ פתרון יחיד, $k=3$ אינסוף פתרונות",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq3</annotation></semantics></math></span> פתרון יחיד, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> אינסוף פתרונות"
       },
       {
        "id": "b",
        "value": "$k\\neq3$ פתרון יחיד, $k=3$ אין פתרון",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq3</annotation></semantics></math></span> פתרון יחיד, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> אין פתרון"
       },
       {
        "id": "c",
        "value": "$k\\neq3$ אינסוף פתרונות, $k=3$ פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq3</annotation></semantics></math></span> אינסוף פתרונות, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> פתרון יחיד"
       },
       {
        "id": "d",
        "value": "לכל $k$ יש פתרון יחיד",
        "type": "text",
        "html": "לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> יש פתרון יחיד"
       }
      ],
      "correctId": "a",
      "explanation": "ב-$k=3$ השורה היא $(0\\ 0\\ 0\\,|\\,0)$, ללא סתירה, והדרגה היא $2<3$: אינסוף פתרונות. אפשרות ב' מתעלמת מכך שהאיבר החופשי הוא $0$. אפשרות ג' הופכת את המקרים.",
      "recap": "p=0 ו-q=0: אינסוף. p=0 ו-q שונה מאפס: אין.",
      "questionHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=2</annotation></semantics></math></span> השורה האחרונה אחרי דירוג היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ k-3\\,|\\,0)</annotation></semantics></math></span>. מה נכון?",
      "explanationHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> השורה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,0)</annotation></semantics></math></span>, ללא סתירה, והדרגה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>&lt;</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">2&lt;3</annotation></semantics></math></span>: אינסוף פתרונות. אפשרות ב' מתעלמת מכך שהאיבר החופשי הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>. אפשרות ג' הופכת את המקרים.",
      "recapHtml": "p=0 ו-q=0: אינסוף. p=0 ו-q שונה מאפס: אין."
     },
     {
      "id": "C04-Q4",
      "question": "אחרי דירוג, השורה האחרונה של מערכת היא $(0\\ \\ 0\\ \\ k^2-4\\,|\\,k+2)$. מה נכון?",
      "options": [
       {
        "id": "a",
        "value": "$k=2$ אין פתרון, $k=-2$ אינסוף פתרונות, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=2</annotation></semantics></math></span> אין פתרון, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=-2</annotation></semantics></math></span> אינסוף פתרונות, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       },
       {
        "id": "b",
        "value": "$k=2$ אינסוף פתרונות, $k=-2$ אין פתרון, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=2</annotation></semantics></math></span> אינסוף פתרונות, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=-2</annotation></semantics></math></span> אין פתרון, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       },
       {
        "id": "c",
        "value": "$k=\\pm2$ אין פתרון, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>±</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=\\pm2</annotation></semantics></math></span> אין פתרון, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       },
       {
        "id": "d",
        "value": "$k=2$ אין פתרון, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=2</annotation></semantics></math></span> אין פתרון, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       }
      ],
      "correctId": "a",
      "explanation": "$k^2-4=(k-2)(k+2)$, ולכן הערכים הקריטיים הם $2$ ו-$-2$. ב-$k=2$: $q=4\\neq0$, אין פתרון. ב-$k=-2$: $q=0$, אינסוף פתרונות. שני הערכים הקריטיים מתנהגים אחרת, ולכן חייבים לבדוק כל אחד בנפרד.",
      "recap": "מפרקים לגורמים ובודקים כל ערך קריטי לחוד.",
      "questionHtml": "אחרי דירוג, השורה האחרונה של מערכת היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><msup><mi>k</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ k^2-4\\,|\\,k+2)</annotation></semantics></math></span>. מה נכון?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mo>=</mo><mo stretchy=\"false\">(</mo><mi>k</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>k</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">k^2-4=(k-2)(k+2)</annotation></semantics></math></span>, ולכן הערכים הקריטיים הם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=2</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo>=</mo><mn>4</mn><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q=4\\neq0</annotation></semantics></math></span>, אין פתרון. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">k=-2</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q=0</annotation></semantics></math></span>, אינסוף פתרונות. שני הערכים הקריטיים מתנהגים אחרת, ולכן חייבים לבדוק כל אחד בנפרד.",
      "recapHtml": "מפרקים לגורמים ובודקים כל ערך קריטי לחוד."
     },
     {
      "id": "C04-Q5",
      "step": {
       "type": "numeric",
       "prompt": "במערכת $x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=k$ מציבים $k=4$. מהו $x$ ?",
       "answer": 2,
       "tol": 0,
       "explain": "השורה האחרונה היא $(0\\ 0\\ 1\\,|\\,2)$, כלומר $z=2$. אחר כך $y+2z=1$ נותן $y=-3$, ו-$x=1-y-z=1+3-2=2$. בדיקה במשוואה השלישית: $2-6+8=4=k$.",
       "promptHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>k</mi><mi>z</mi><mo>=</mo><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2,\\ x+2y+kz=k</annotation></semantics></math></span> מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">k=4</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ?",
       "explainHtml": "השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 1\\,|\\,2)</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">z=2</annotation></semantics></math></span>. אחר כך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y+2z=1</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">y=-3</annotation></semantics></math></span>, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn><mo>−</mo><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>−</mo><mn>2</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=1-y-z=1+3-2=2</annotation></semantics></math></span>. בדיקה במשוואה השלישית: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>−</mo><mn>6</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>4</mn><mo>=</mo><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">2-6+8=4=k</annotation></semantics></math></span>."
      },
      "recap": "ערך שאינו קריטי: פתרון יחיד, מציבים לאחור.",
      "recapHtml": "ערך שאינו קריטי: פתרון יחיד, מציבים לאחור."
     },
     {
      "id": "C04-Q6",
      "question": "אחרי דירוג, השורה האחרונה היא $(0\\ \\ 0\\ \\ 3-k\\,|\\,k-3)$. לאילו ערכי $k$ אין למערכת פתרון?",
      "options": [
       {
        "id": "a",
        "value": "לאף ערך של $k$",
        "type": "text",
        "html": "לאף ערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$k=3$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$k\\neq3$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq3</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "לכל ערך של $k$",
        "type": "text",
        "html": "לכל ערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "ב-$k=3$ השורה היא $(0\\ 0\\ 0\\,|\\,0)$, ולא סתירה. לכל $k\\neq3$ יש פתרון יחיד. לכן אין ערך של $k$ שנותן \"אין פתרון\". בשאלות כאלה התשובה \"אף ערך\" היא תשובה לגיטימית.",
      "recap": "אם q הוא כפולה של p, אין ערך עם סתירה.",
      "questionHtml": "אחרי דירוג, השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mn>3</mn><mo>−</mo><mi>k</mi><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>k</mi><mo>−</mo><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ 3-k\\,|\\,k-3)</annotation></semantics></math></span>. לאילו ערכי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אין למערכת פתרון?",
      "explanationHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span> השורה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,0)</annotation></semantics></math></span>, ולא סתירה. לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq3</annotation></semantics></math></span> יש פתרון יחיד. לכן אין ערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> שנותן \"אין פתרון\". בשאלות כאלה התשובה \"אף ערך\" היא תשובה לגיטימית.",
      "recapHtml": "אם q הוא כפולה של p, אין ערך עם סתירה."
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "🪤",
    "title": "המלכודת: לא מחלקים בפרמטר",
    "goal": "לדרג בלי לחלק בביטוי עם פרמטר, ואם חילקתם, לבדוק בנפרד את הערכים שבהם הביטוי מתאפס.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>אפשר לחלק שורה בביטוי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">p(k)</annotation></semantics></math></span> רק כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p(k)\\neq0</annotation></semantics></math></span>. אם חילקתם, הערכים שבהם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo stretchy=\"false\">(</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p(k)=0</annotation></semantics></math></span> הם <b>מקרים נפרדים</b>: מציבים אותם במטריצה <b>שלפני החלוקה</b> ומדרגים מחדש.</p>\n<div class=\"lesson-rule\">🔑 שלוש עצות לדירוג בטוח:\n<ul>\n<li>החליפו שורות כך שבפינה יהיה מספר פשוט, כמו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>, ולא הפרמטר.</li>\n<li>העדיפו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mi>k</mi><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-kR_1</annotation></semantics></math></span> על פני חלוקה.</li>\n<li>אם חילקתם בביטוי כמו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>a</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">a(1-a)</annotation></semantics></math></span>, הערכים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> חייבים בדיקה נפרדת.</li>\n</ul></div>\n<div class=\"lesson-ex\">נבחן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">kx+y=1,\\ x+ky=1</annotation></semantics></math></span>. מחליפים שורות ומקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mtext>  </mtext><mi>k</mi><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1\\ \\ k\\,|\\,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>k</mi><mtext>  </mtext><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(k\\ \\ 1\\,|\\,1)</annotation></semantics></math></span>. הפעולה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mi>k</mi><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-kR_1</annotation></semantics></math></span> נותנת\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>   </mtext><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ \\ 1-k^2\\,|\\,1-k)</annotation></semantics></math></span>\nו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>+</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">1-k^2=(1-k)(1+k)</annotation></semantics></math></span>. הערכים הקריטיים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=-1</annotation></semantics></math></span>.\n<ul>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=1</annotation></semantics></math></span>: השורה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\,|\\,0)</annotation></semantics></math></span>, ולכן אינסוף פתרונות.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=-1</annotation></semantics></math></span>: השורה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\,|\\,2)</annotation></semantics></math></span>, ולכן אין פתרון.</li>\n<li>כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>−</mo><mi>k</mi></mrow><mrow><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">y=\\frac{1-k}{1-k^2}=\\frac{1}{1+k}</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">x=\\frac{1}{1+k}</annotation></semantics></math></span>.</li>\n</ul></div>\n<div class=\"lesson-trap\">⚠️ חילוק ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> בצעד הראשון היה מוחק את המקרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">k=0</annotation></semantics></math></span> מהחשבון. כאן הוא אפילו לא הכרחי: החלפת שורות פותרת את העניין.</div>\n"
    },
    "questions": [
     {
      "id": "C05-Q1",
      "question": "בדירוג מערכת מחלקים את השורה השנייה ב-$a(1-a)$. לאילו ערכי $a$ החלוקה אסורה, ולכן הם דורשים בדיקה נפרדת?",
      "options": [
       {
        "id": "a",
        "value": "$a=0$ ו-$a=1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$a=1$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "c",
        "value": "$a=0$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a=0</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "d",
        "value": "$a=-1$ ו-$a=1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=-1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$a(1-a)=0$ כאשר $a=0$ או $a=1$. שני הערכים אסורים לחלוקה. אפשרויות ב' ו-ג' שוכחות אחד מהם, ואפשרות ד' מערבבת עם $1+a$.",
      "recap": "אפסים של הביטוי המחלק = מקרים נפרדים.",
      "questionHtml": "בדירוג מערכת מחלקים את השורה השנייה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>a</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">a(1-a)</annotation></semantics></math></span>. לאילו ערכי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">a</annotation></semantics></math></span> החלוקה אסורה, ולכן הם דורשים בדיקה נפרדת?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>a</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a(1-a)=0</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a=0</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span>. שני הערכים אסורים לחלוקה. אפשרויות ב' ו-ג' שוכחות אחד מהם, ואפשרות ד' מערבבת עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">1+a</annotation></semantics></math></span>.",
      "recapHtml": "אפסים של הביטוי המחלק = מקרים נפרדים."
     },
     {
      "id": "C05-Q2",
      "question": "במערכת $kx+y=1,\\ x+ky=1$, מהו הצעד הראשון הבטוח ביותר בדירוג?",
      "options": [
       {
        "id": "a",
        "value": "להחליף את השורות כדי שהאיבר $1$ יהיה בפינה",
        "type": "text",
        "html": "להחליף את השורות כדי שהאיבר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> יהיה בפינה"
       },
       {
        "id": "b",
        "value": "לחלק את השורה הראשונה ב-$k$",
        "type": "text",
        "html": "לחלק את השורה הראשונה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "להכפיל את השורה השנייה ב-$k$ ולהחסיר מהראשונה, בלי לבדוק את $k=0$",
        "type": "text",
        "html": "להכפיל את השורה השנייה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> ולהחסיר מהראשונה, בלי לבדוק את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">k=0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "לחלק את השורה השנייה ב-$k$",
        "type": "text",
        "html": "לחלק את השורה השנייה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "אחרי החלפת שורות הפינה היא $1$, ולא צריך לחלק בביטוי עם פרמטר. אפשרויות ב' ו-ד' מחלקות ב-$k$ ודורשות בדיקה נפרדת של $k=0$. אפשרות ג' מערבבת פעולות ומשאירה את הפינה כפרמטר.",
      "recap": "מחליפים שורות כדי לקבל 1 בפינה.",
      "questionHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">kx+y=1,\\ x+ky=1</annotation></semantics></math></span>, מהו הצעד הראשון הבטוח ביותר בדירוג?",
      "explanationHtml": "אחרי החלפת שורות הפינה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>, ולא צריך לחלק בביטוי עם פרמטר. אפשרויות ב' ו-ד' מחלקות ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> ודורשות בדיקה נפרדת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">k=0</annotation></semantics></math></span>. אפשרות ג' מערבבת פעולות ומשאירה את הפינה כפרמטר.",
      "recapHtml": "מחליפים שורות כדי לקבל 1 בפינה."
     },
     {
      "id": "C05-Q3",
      "step": {
       "type": "numeric",
       "prompt": "במערכת $kx+y=1,\\ x+ky=1$, עבור איזה ערך של $k$ אין פתרון?",
       "answer": -1,
       "tol": 0,
       "explain": "אחרי הדירוג: $(0\\ \\ 1-k^2\\,|\\,1-k)$. הערכים הקריטיים הם $k=\\pm1$. עבור $k=1$ הצד הימני $1-k=0$ (אינסוף פתרונות). עבור $k=-1$ הצד הימני $1-(-1)=2\\neq0$ (אין פתרון).",
       "promptHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">kx+y=1,\\ x+ky=1</annotation></semantics></math></span>, עבור איזה ערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אין פתרון?",
       "explainHtml": "אחרי הדירוג: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 1-k^2\\,|\\,1-k)</annotation></semantics></math></span>. הערכים הקריטיים הם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=\\pm1</annotation></semantics></math></span>. עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=1</annotation></semantics></math></span> הצד הימני <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><mi>k</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">1-k=0</annotation></semantics></math></span> (אינסוף פתרונות). עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=-1</annotation></semantics></math></span> הצד הימני <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">1-(-1)=2\\neq0</annotation></semantics></math></span> (אין פתרון)."
      },
      "recap": "בודקים כל ערך קריטי לחוד.",
      "recapHtml": "בודקים כל ערך קריטי לחוד."
     },
     {
      "id": "C05-Q4",
      "question": "מה הסיווג המלא של המערכת $kx+y=1,\\ x+ky=1$ ?",
      "options": [
       {
        "id": "a",
        "value": "$k=1$ אינסוף פתרונות, $k=-1$ אין פתרון, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=1</annotation></semantics></math></span> אינסוף פתרונות, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=-1</annotation></semantics></math></span> אין פתרון, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       },
       {
        "id": "b",
        "value": "$k=1$ אין פתרון, $k=-1$ אינסוף פתרונות, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=1</annotation></semantics></math></span> אין פתרון, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=-1</annotation></semantics></math></span> אינסוף פתרונות, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       },
       {
        "id": "c",
        "value": "$k=\\pm1$ אין פתרון, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=\\pm1</annotation></semantics></math></span> אין פתרון, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       },
       {
        "id": "d",
        "value": "$k=\\pm1$ אינסוף פתרונות, כל $k$ אחר פתרון יחיד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=\\pm1</annotation></semantics></math></span> אינסוף פתרונות, כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">k</annotation></semantics></math></span> אחר פתרון יחיד"
       }
      ],
      "correctId": "a",
      "explanation": "ב-$k=1$ שתי המשוואות זהות ($x+y=1$), ולכן אינסוף פתרונות. ב-$k=-1$ המשוואות הן $-x+y=1$ ו-$x-y=1$, שסכומן $0=2$: אין פתרון. שאר הערכים נותנים $1-k^2\\neq0$, פתרון יחיד.",
      "recap": "שני ערכים קריטיים יכולים להתנהג שונה.",
      "questionHtml": "מה הסיווג המלא של המערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">kx+y=1,\\ x+ky=1</annotation></semantics></math></span> ?",
      "explanationHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=1</annotation></semantics></math></span> שתי המשוואות זהות (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x+y=1</annotation></semantics></math></span>), ולכן אינסוף פתרונות. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=-1</annotation></semantics></math></span> המשוואות הן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-x+y=1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x-y=1</annotation></semantics></math></span>, שסכומן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">0=2</annotation></semantics></math></span>: אין פתרון. שאר הערכים נותנים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">1-k^2\\neq0</annotation></semantics></math></span>, פתרון יחיד.",
      "recapHtml": "שני ערכים קריטיים יכולים להתנהג שונה."
     },
     {
      "id": "C05-Q5",
      "step": {
       "type": "numeric",
       "prompt": "במערכת $kx+y=1,\\ x+ky=1$ מציבים $k=3$. מהו $x$ ?",
       "answer": 0.25,
       "tol": 0,
       "explain": "לפי הנוסחה $x=\\frac{1}{1+k}=\\frac{1}{4}=0.25$. בדיקה: $3\\cdot0.25+0.25=1$.",
       "promptHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">kx+y=1,\\ x+ky=1</annotation></semantics></math></span> מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">k=3</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ?",
       "explainHtml": "לפי הנוסחה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mn>0.25</mn></mrow><annotation encoding=\"application/x-tex\">x=\\frac{1}{1+k}=\\frac{1}{4}=0.25</annotation></semantics></math></span>. בדיקה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>0.25</mn><mo>+</mo><mn>0.25</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">3\\cdot0.25+0.25=1</annotation></semantics></math></span>."
      },
      "recap": "אחרי שדירגנו: x ו-y כפונקציה של k.",
      "recapHtml": "אחרי שדירגנו: x ו-y כפונקציה של k."
     },
     {
      "id": "C05-Q6",
      "step": {
       "type": "findbug",
       "prompt": "באחד השלבים בפתרון של $kx+y=1,\\ x+ky=1$ יש טעות. איזה?",
       "lines": [
        "מחליפים שורות: $(1\\ \\ k\\,|\\,1)$ ו-$(k\\ \\ 1\\,|\\,1)$",
        "$R_2\\to R_2-kR_1$ נותן $(0\\ \\ 1-k\\,|\\,1-k)$",
        "הערכים הקריטיים מתאפסים כאשר $1-k^2=0$, כלומר $k=\\pm1$",
        "לכל $k\\neq\\pm1$: $y=\\frac{1}{1+k}$"
       ],
       "bugIndex": 1,
       "explain": "$(k\\ \\ 1\\,|\\,1)-k(1\\ \\ k\\,|\\,1)=(0\\ \\ 1-k^2\\,|\\,1-k)$. המקדם הוא $1-k^2$ ולא $1-k$. שורות 3 ו-4 כבר מתבססות על $1-k^2$.",
       "promptHtml": "באחד השלבים בפתרון של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>k</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">kx+y=1,\\ x+ky=1</annotation></semantics></math></span> יש טעות. איזה?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>k</mi><mtext>  </mtext><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo><mo>−</mo><mi>k</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mtext>  </mtext><mi>k</mi><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(k\\ \\ 1\\,|\\,1)-k(1\\ \\ k\\,|\\,1)=(0\\ \\ 1-k^2\\,|\\,1-k)</annotation></semantics></math></span>. המקדם הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">1-k^2</annotation></semantics></math></span> ולא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><mi>k</mi></mrow><annotation encoding=\"application/x-tex\">1-k</annotation></semantics></math></span>. שורות 3 ו-4 כבר מתבססות על <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">1-k^2</annotation></semantics></math></span>.",
       "linesHtml": [
        "מחליפים שורות: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mtext>  </mtext><mi>k</mi><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1\\ \\ k\\,|\\,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>k</mi><mtext>  </mtext><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(k\\ \\ 1\\,|\\,1)</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>→</mo><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><mi>k</mi><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2\\to R_2-kR_1</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>1</mn><mo>−</mo><mi>k</mi><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo>−</mo><mi>k</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 1-k\\,|\\,1-k)</annotation></semantics></math></span>",
        "הערכים הקריטיים מתאפסים כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">1-k^2=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k=\\pm1</annotation></semantics></math></span>",
        "לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>k</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">k\\neq\\pm1</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>k</mi></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">y=\\frac{1}{1+k}</annotation></semantics></math></span>"
       ]
      },
      "recap": "k כפול k הוא k בריבוע.",
      "recapHtml": "k כפול k הוא k בריבוע."
     }
    ]
   },
   {
    "id": "C06",
    "order": 6,
    "icon": "🎛️",
    "title": "שני פרמטרים: כל המקרים",
    "goal": "לסווג מערכת עם שני פרמטרים לשלושת המקרים ולכתוב את הפתרון בכל מקרה.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>כשיש שני פרמטרים, השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi>p</mi><mo stretchy=\"false\">(</mo><mi>a</mi><mo stretchy=\"false\">)</mo><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>q</mi><mo stretchy=\"false\">(</mo><mi>a</mi><mo separator=\"true\">,</mo><mi>b</mi><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ p(a)\\,|\\,q(a,b))</annotation></semantics></math></span>. קודם מוצאים מתי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p=0</annotation></semantics></math></span>, ואז בודקים מתי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q=0</annotation></semantics></math></span> בתוך המקרה הזה.</p>\n<div class=\"lesson-ex\">נבחן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2,\\ x+2y+az=b</annotation></semantics></math></span>. הפעולות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2-R_1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>3</mn></msub><mo>−</mo><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_3-R_1</annotation></semantics></math></span> נותנות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>1</mn><mtext> </mtext><mn>2</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 1\\ 2\\,|\\,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>1</mn><mtext> </mtext><mi>a</mi><mo>−</mo><mn>1</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>b</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 1\\ a-1\\,|\\,b-1)</annotation></semantics></math></span>. הפעולה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>3</mn></msub><mo>−</mo><msub><mi>R</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_3-R_2</annotation></semantics></math></span> נותנת\n<span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>a</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>b</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ a-3\\,|\\,b-2)</annotation></semantics></math></span>\n<ul>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq3</annotation></semantics></math></span>: פתרון יחיד, לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span>. כאן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mfrac><mrow><mi>b</mi><mo>−</mo><mn>2</mn></mrow><mrow><mi>a</mi><mo>−</mo><mn>3</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">z=\\frac{b-2}{a-3}</annotation></semantics></math></span>.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo mathvariant=\"normal\">≠</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b\\neq2</annotation></semantics></math></span>: אין פתרון.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2</annotation></semantics></math></span>: אינסוף פתרונות. <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>2</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-2t</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">x=t</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mi>t</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x,y,z)=(0,1,0)+t(1,-2,1)</annotation></semantics></math></span>.</li>\n</ul></div>\n<div class=\"lesson-rule\">🔑 סדר העבודה: (1) דירוג בלי לחלק בפרמטר. (2) אפסי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi></mrow><annotation encoding=\"application/x-tex\">p</annotation></semantics></math></span> הם הערכים הקריטיים. (3) בכל ערך קריטי בודקים את האיבר החופשי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi></mrow><annotation encoding=\"application/x-tex\">q</annotation></semantics></math></span>. (4) בשאר הערכים מחלצים את הנעלמים כפונקציה של הפרמטרים.</div>\n<div class=\"lesson-trap\">⚠️ בפתרון יחיד אין \"מקרה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span>\": אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq3</annotation></semantics></math></span> הערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span> משפיע רק על הפתרון עצמו, לא על מספר הפתרונות.</div>\n"
    },
    "questions": [
     {
      "id": "C06-Q1",
      "step": {
       "type": "numeric",
       "prompt": "במערכת $x+y+z=1,\\ x+2y+3z=2,\\ x+2y+az=b$ השורה האחרונה אחרי דירוג היא $(0\\ \\ 0\\ \\ a-3\\,|\\,b-2)$. עבור איזה $a$ המקדם מתאפס?",
       "answer": 3,
       "tol": 0,
       "explain": "$a-3=0$ ב-$a=3$.",
       "promptHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">x+y+z=1,\\ x+2y+3z=2,\\ x+2y+az=b</annotation></semantics></math></span> השורה האחרונה אחרי דירוג היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>a</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mi>b</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ a-3\\,|\\,b-2)</annotation></semantics></math></span>. עבור איזה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">a</annotation></semantics></math></span> המקדם מתאפס?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>−</mo><mn>3</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a-3=0</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span>."
      },
      "recap": "מוצאים את אפס המקדם האחרון.",
      "recapHtml": "מוצאים את אפס המקדם האחרון."
     },
     {
      "id": "C06-Q2",
      "question": "באותה מערכת מציבים $a=3$ ו-$b=5$. מה קורה?",
      "options": [
       {
        "id": "a",
        "value": "אין פתרון",
        "type": "text",
        "html": "אין פתרון"
       },
       {
        "id": "b",
        "value": "פתרון יחיד",
        "type": "text",
        "html": "פתרון יחיד"
       },
       {
        "id": "c",
        "value": "אינסוף פתרונות",
        "type": "text",
        "html": "אינסוף פתרונות"
       },
       {
        "id": "d",
        "value": "פתרון יחיד אבל רק אם $b=2$",
        "type": "text",
        "html": "פתרון יחיד אבל רק אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "השורה האחרונה היא $(0\\ 0\\ 0\\,|\\,3)$: סתירה. הערך $b=2$ היה נותן אינסוף פתרונות ולא פתרון יחיד.",
      "recap": "a=3 ו-b שונה מ-2: אין פתרון.",
      "questionHtml": "באותה מערכת מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">b=5</annotation></semantics></math></span>. מה קורה?",
      "explanationHtml": "השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,3)</annotation></semantics></math></span>: סתירה. הערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2</annotation></semantics></math></span> היה נותן אינסוף פתרונות ולא פתרון יחיד.",
      "recapHtml": "a=3 ו-b שונה מ-2: אין פתרון."
     },
     {
      "id": "C06-Q3",
      "question": "באותה מערכת מציבים $a=3$ ו-$b=2$. מה קורה?",
      "options": [
       {
        "id": "a",
        "value": "אינסוף פתרונות, עם משתנה חופשי אחד",
        "type": "text",
        "html": "אינסוף פתרונות, עם משתנה חופשי אחד"
       },
       {
        "id": "b",
        "value": "אינסוף פתרונות, עם שני משתנים חופשיים",
        "type": "text",
        "html": "אינסוף פתרונות, עם שני משתנים חופשיים"
       },
       {
        "id": "c",
        "value": "אין פתרון",
        "type": "text",
        "html": "אין פתרון"
       },
       {
        "id": "d",
        "value": "פתרון יחיד",
        "type": "text",
        "html": "פתרון יחיד"
       }
      ],
      "correctId": "a",
      "explanation": "השורה האחרונה היא $(0\\ 0\\ 0\\,|\\,0)$. הדרגה היא $2$ ויש $3$ נעלמים, ולכן משתנה חופשי אחד ($z=t$) ואינסוף פתרונות.",
      "recap": "שורת אפסים שלמה: אינסוף, n פחות r חופשיים.",
      "questionHtml": "באותה מערכת מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2</annotation></semantics></math></span>. מה קורה?",
      "explanationHtml": "השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,0)</annotation></semantics></math></span>. הדרגה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ויש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span> נעלמים, ולכן משתנה חופשי אחד (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>) ואינסוף פתרונות.",
      "recapHtml": "שורת אפסים שלמה: אינסוף, n פחות r חופשיים."
     },
     {
      "id": "C06-Q4",
      "step": {
       "type": "numeric",
       "prompt": "באותה מערכת מציבים $a=5$ ו-$b=4$. מהו $y$ ?",
       "answer": -1,
       "tol": 0,
       "explain": "השורה האחרונה היא $(0\\ 0\\ 2\\,|\\,2)$, ולכן $z=1$. מהשורה השנייה $y=1-2z=-1$, ומהראשונה $x=1-y-z=1$. בדיקה במשוואה השלישית: $1-2+5=4=b$.",
       "promptHtml": "באותה מערכת מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">a=5</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">b=4</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> ?",
       "explainHtml": "השורה האחרונה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>2</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 2\\,|\\,2)</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">z=1</annotation></semantics></math></span>. מהשורה השנייה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>2</mn><mi>z</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=1-2z=-1</annotation></semantics></math></span>, ומהראשונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn><mo>−</mo><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1-y-z=1</annotation></semantics></math></span>. בדיקה במשוואה השלישית: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><mn>2</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>4</mn><mo>=</mo><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">1-2+5=4=b</annotation></semantics></math></span>."
      },
      "recap": "ערך שאינו קריטי: מחלצים z, אחר כך y, אחר כך x.",
      "recapHtml": "ערך שאינו קריטי: מחלצים z, אחר כך y, אחר כך x."
     },
     {
      "id": "C06-Q5",
      "question": "לאילו זוגות $(a,b)$ אין למערכת פתרון?",
      "options": [
       {
        "id": "a",
        "value": "$a=3$ ו-$b\\neq2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo mathvariant=\"normal\">≠</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b\\neq2</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$a\\neq3$ ו-$b\\neq2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo mathvariant=\"normal\">≠</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b\\neq2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$a=3$, לכל $b$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span>, לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$b\\neq2$, לכל $a$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo mathvariant=\"normal\">≠</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b\\neq2</annotation></semantics></math></span>, לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">a</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "סתירה מתקבלת רק כש-$p=0$ וגם $q\\neq0$, כלומר $a=3$ ו-$b\\neq2$. אפשרות ג' כוללת את $b=2$ שנותן אינסוף פתרונות. כש-$a\\neq3$ תמיד יש פתרון יחיד, ולכן ב' וד' שגויות.",
      "recap": "אין פתרון: p=0 וגם q שונה מאפס.",
      "questionHtml": "לאילו זוגות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>a</mi><mo separator=\"true\">,</mo><mi>b</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(a,b)</annotation></semantics></math></span> אין למערכת פתרון?",
      "explanationHtml": "סתירה מתקבלת רק כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>p</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">p=0</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>q</mi><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">q\\neq0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo mathvariant=\"normal\">≠</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b\\neq2</annotation></semantics></math></span>. אפשרות ג' כוללת את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2</annotation></semantics></math></span> שנותן אינסוף פתרונות. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq3</annotation></semantics></math></span> תמיד יש פתרון יחיד, ולכן ב' וד' שגויות.",
      "recapHtml": "אין פתרון: p=0 וגם q שונה מאפס."
     },
     {
      "id": "C06-Q6",
      "step": {
       "type": "numeric",
       "prompt": "עבור $a=3$ ו-$b=2$ הפתרון הכללי הוא $(x,y,z)=\\vec p+t\\vec d$ עם $z=t$. מהו הרכיב השני (של $y$) בווקטור הכיוון $\\vec d$ ?",
       "answer": -2,
       "tol": 0,
       "explain": "$y+2z=1$ ולכן $y=1-2t$, והמקדם של $t$ הוא $-2$. ואז $x=1-y-z=t$, כך ש-$\\vec d=(1,-2,1)$ ו-$\\vec p=(0,1,0)$.",
       "promptHtml": "עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2</annotation></semantics></math></span> הפתרון הכללי הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mover accent=\"true\"><mi>p</mi><mo>⃗</mo></mover><mo>+</mo><mi>t</mi><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">(x,y,z)=\\vec p+t\\vec d</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">z=t</annotation></semantics></math></span>. מהו הרכיב השני (של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>) בווקטור הכיוון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec d</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y+2z=1</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn><mo>−</mo><mn>2</mn><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">y=1-2t</annotation></semantics></math></span>, והמקדם של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">t</annotation></semantics></math></span> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span>. ואז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn><mo>−</mo><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">x=1-y-z=t</annotation></semantics></math></span>, כך ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\vec d=(1,-2,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>p</mi><mo>⃗</mo></mover><mo>=</mo><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">\\vec p=(0,1,0)</annotation></semantics></math></span>."
      },
      "recap": "וקטור הכיוון: המקדמים של t.",
      "recapHtml": "וקטור הכיוון: המקדמים של t."
     }
    ]
   },
   {
    "id": "C07",
    "order": 7,
    "icon": "📐",
    "title": "מערכת הומוגנית עם פרמטר",
    "goal": "לקבוע לפי הדרגה מתי למערכת הומוגנית יש רק פתרון טריוויאלי, מתי הפתרונות ישר ומתי מישור.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>במערכת <b>הומוגנית</b> (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>A</mi><mover accent=\"true\"><mi>x</mi><mo>⃗</mo></mover><mo>=</mo><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">A\\vec x=\\vec 0</annotation></semantics></math></span>) הצד הימני הוא אפסים, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>x</mi><mo>⃗</mo></mover><mo>=</mo><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec x=\\vec 0</annotation></semantics></math></span> תמיד פתרון: <b>אין מקרה של \"אין פתרון\"</b>. נשאר לשאול רק כמה פתרונות, וזה נקבע לפי הדרגה (בשלושה נעלמים).</p>\n<table>\n<thead><tr><th><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">r(A)</annotation></semantics></math></span></th><th>משתנים חופשיים</th><th>קבוצת הפתרונות</th></tr></thead>\n<tbody>\n<tr><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span></td><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span></td><td>רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span> (פתרון טריוויאלי)</td></tr>\n<tr><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span></td><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span></td><td>ישר דרך הראשית</td></tr>\n<tr><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span></td><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span></td><td>מישור דרך הראשית</td></tr>\n</tbody></table>\n<div class=\"lesson-ex\">נבחן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>a</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>a</mi><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=0,\\ ax+y=0,\\ x+ay=0</annotation></semantics></math></span>. הערכים הקריטיים הם אלה שבהם הדרגה יורדת. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> המערכת היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=0,\\ x+y=0</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">z=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mo>−</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=-x</annotation></semantics></math></span>: הישר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo separator=\"true\">,</mo><mi>y</mi><mo separator=\"true\">,</mo><mi>z</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>t</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x,y,z)=t(1,-1,0)</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=-1</annotation></semantics></math></span> השורה השנייה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">-x+y=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>, ומהראשונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mo>−</mo><mn>2</mn><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">z=-2x</annotation></semantics></math></span>: הישר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">t(1,1,-2)</annotation></semantics></math></span>. לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq\\pm1</annotation></semantics></math></span> הדרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span> ויש רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>.</div>\n<div class=\"lesson-rule\">🔑 במערכת הומוגנית מציבים את הערך הקריטי <b>לפני</b> החלוקה, מדרגים ומחשבים את הדרגה. מספר המשתנים החופשיים הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>−</mo><mi>r</mi><mo stretchy=\"false\">(</mo><mi>A</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">3-r(A)</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ \"פתרון טריוויאלי בלבד\" פירושו דרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>. אם שאלו \"לאילו ערכי הפרמטר יש פתרון לא טריוויאלי\", מחפשים את הערכים שבהם הדרגה קטנה מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>.</div>\n"
    },
    "questions": [
     {
      "id": "C07-Q1",
      "question": "מה נכון לגבי מערכת הומוגנית $A\\vec x=\\vec 0$ עם פרמטר?",
      "options": [
       {
        "id": "a",
        "value": "לכל ערך של הפרמטר יש לפחות פתרון אחד",
        "type": "text",
        "html": "לכל ערך של הפרמטר יש לפחות פתרון אחד"
       },
       {
        "id": "b",
        "value": "יש ערכי פרמטר שבהם אין פתרון",
        "type": "text",
        "html": "יש ערכי פרמטר שבהם אין פתרון"
       },
       {
        "id": "c",
        "value": "תמיד יש אינסוף פתרונות",
        "type": "text",
        "html": "תמיד יש אינסוף פתרונות"
       },
       {
        "id": "d",
        "value": "הפתרון היחיד האפשרי הוא $\\vec 0$",
        "type": "text",
        "html": "הפתרון היחיד האפשרי הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$\\vec x=\\vec 0$ מקיים כל מערכת הומוגנית, ולכן תמיד יש פתרון. אבל לא תמיד אינסוף: כשהדרגה מלאה הפתרון היחיד הוא $\\vec 0$, ובמקרה אחר יש אינסוף.",
      "recap": "הומוגנית: תמיד יש פתרון, השאלה כמה.",
      "questionHtml": "מה נכון לגבי מערכת הומוגנית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>A</mi><mover accent=\"true\"><mi>x</mi><mo>⃗</mo></mover><mo>=</mo><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">A\\vec x=\\vec 0</annotation></semantics></math></span> עם פרמטר?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>x</mi><mo>⃗</mo></mover><mo>=</mo><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec x=\\vec 0</annotation></semantics></math></span> מקיים כל מערכת הומוגנית, ולכן תמיד יש פתרון. אבל לא תמיד אינסוף: כשהדרגה מלאה הפתרון היחיד הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>, ובמקרה אחר יש אינסוף.",
      "recapHtml": "הומוגנית: תמיד יש פתרון, השאלה כמה."
     },
     {
      "id": "C07-Q2",
      "step": {
       "type": "numeric",
       "prompt": "במערכת ההומוגנית $x+y+z=0,\\ x+2y+3z=0,\\ x+2y+az=0$ השורה האחרונה אחרי דירוג היא $(0\\ \\ 0\\ \\ a-3\\,|\\,0)$. עבור איזה $a$ יש פתרון לא טריוויאלי?",
       "answer": 3,
       "tol": 0,
       "explain": "בדיוק כש-$a-3=0$, כלומר $a=3$, הדרגה יורדת ל-$2$. לכל $a\\neq3$ הדרגה $3$ ויש רק $\\vec 0$.",
       "promptHtml": "במערכת ההומוגנית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>a</mi><mi>z</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=0,\\ x+2y+3z=0,\\ x+2y+az=0</annotation></semantics></math></span> השורה האחרונה אחרי דירוג היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mn>0</mn><mtext>  </mtext><mi>a</mi><mo>−</mo><mn>3</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ 0\\ \\ a-3\\,|\\,0)</annotation></semantics></math></span>. עבור איזה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">a</annotation></semantics></math></span> יש פתרון לא טריוויאלי?",
       "explainHtml": "בדיוק כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>−</mo><mn>3</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a-3=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span>, הדרגה יורדת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>. לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq3</annotation></semantics></math></span> הדרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span> ויש רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>."
      },
      "recap": "פתרון לא טריוויאלי: הדרגה קטנה מ-n.",
      "recapHtml": "פתרון לא טריוויאלי: הדרגה קטנה מ-n."
     },
     {
      "id": "C07-Q3",
      "question": "באותה מערכת, מה קבוצת הפתרונות כאשר $a=3$ ?",
      "options": [
       {
        "id": "a",
        "value": "ישר דרך הראשית",
        "type": "text",
        "html": "ישר דרך הראשית"
       },
       {
        "id": "b",
        "value": "מישור דרך הראשית",
        "type": "text",
        "html": "מישור דרך הראשית"
       },
       {
        "id": "c",
        "value": "רק הנקודה $\\vec 0$",
        "type": "text",
        "html": "רק הנקודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "אין פתרון",
        "type": "text",
        "html": "אין פתרון"
       }
      ],
      "correctId": "a",
      "explanation": "ב-$a=3$ הדרגה היא $2$ ויש משתנה חופשי אחד: $y+2z=0$ ו-$x=-y-z=z$, כלומר $t(1,-2,1)$, ישר. מישור היה דורש דרגה $1$. אין \"אין פתרון\" במערכת הומוגנית.",
      "recap": "r=2 בשלושה נעלמים: ישר.",
      "questionHtml": "באותה מערכת, מה קבוצת הפתרונות כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> ?",
      "explanationHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a=3</annotation></semantics></math></span> הדרגה היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ויש משתנה חופשי אחד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y+2z=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mi>y</mi><mo>−</mo><mi>z</mi><mo>=</mo><mi>z</mi></mrow><annotation encoding=\"application/x-tex\">x=-y-z=z</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">t(1,-2,1)</annotation></semantics></math></span>, ישר. מישור היה דורש דרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>. אין \"אין פתרון\" במערכת הומוגנית.",
      "recapHtml": "r=2 בשלושה נעלמים: ישר."
     },
     {
      "id": "C07-Q4",
      "question": "במערכת ההומוגנית $x+y+z=0,\\ x+ay+z=0$ מה נכון?",
      "options": [
       {
        "id": "a",
        "value": "$a\\neq1$ הפתרונות ישר, $a=1$ הפתרונות מישור",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq1</annotation></semantics></math></span> הפתרונות ישר, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> הפתרונות מישור"
       },
       {
        "id": "b",
        "value": "$a\\neq1$ רק $\\vec 0$, $a=1$ ישר",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq1</annotation></semantics></math></span> רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> ישר"
       },
       {
        "id": "c",
        "value": "$a\\neq1$ הפתרונות מישור, $a=1$ ישר",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq1</annotation></semantics></math></span> הפתרונות מישור, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> ישר"
       },
       {
        "id": "d",
        "value": "$a\\neq1$ רק $\\vec 0$, $a=1$ מישור",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq1</annotation></semantics></math></span> רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> מישור"
       }
      ],
      "correctId": "a",
      "explanation": "$R_2-R_1$ נותן $(0\\ \\ a-1\\ \\ 0)$. כש-$a\\neq1$ יש שתי שורות שונות מאפס (דרגה $2$): ישר. כש-$a=1$ שתי המשוואות זהות (דרגה $1$): מישור. שתי משוואות בשלושה נעלמים אף פעם לא נותנות רק $\\vec 0$.",
      "recap": "דרגה 2: ישר. דרגה 1: מישור.",
      "questionHtml": "במערכת ההומוגנית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>a</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=0,\\ x+ay+z=0</annotation></semantics></math></span> מה נכון?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>R</mi><mn>2</mn></msub><mo>−</mo><msub><mi>R</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">R_2-R_1</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext>  </mtext><mi>a</mi><mo>−</mo><mn>1</mn><mtext>  </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ \\ a-1\\ \\ 0)</annotation></semantics></math></span>. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a\\neq1</annotation></semantics></math></span> יש שתי שורות שונות מאפס (דרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>): ישר. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> שתי המשוואות זהות (דרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>): מישור. שתי משוואות בשלושה נעלמים אף פעם לא נותנות רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mn>0</mn><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec 0</annotation></semantics></math></span>.",
      "recapHtml": "דרגה 2: ישר. דרגה 1: מישור."
     },
     {
      "id": "C07-Q5",
      "step": {
       "type": "numeric",
       "prompt": "עבור $a=1$ במערכת $x+y+z=0,\\ x+ay+z=0$ כמה משתנים חופשיים יש?",
       "answer": 2,
       "tol": 0,
       "explain": "ב-$a=1$ שתי המשוואות זהות, הדרגה $1$, ולכן $3-1=2$ משתנים חופשיים: מישור.",
       "promptHtml": "עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>a</mi><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=0,\\ x+ay+z=0</annotation></semantics></math></span> כמה משתנים חופשיים יש?",
       "explainHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> שתי המשוואות זהות, הדרגה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">3-1=2</annotation></semantics></math></span> משתנים חופשיים: מישור."
      },
      "recap": "חופשיים = 3 פחות הדרגה.",
      "recapHtml": "חופשיים = 3 פחות הדרגה."
     },
     {
      "id": "C07-Q6",
      "step": {
       "type": "numeric",
       "prompt": "במערכת $x+y+z=0,\\ ax+y=0,\\ x+ay=0$ מציבים $a=-1$. הפתרון הוא ישר $t(1,1,c)$. מהו $c$ ?",
       "answer": -2,
       "tol": 0,
       "explain": "ב-$a=-1$ המשוואות $-x+y=0$ ו-$x-y=0$ זהות, ולכן $y=x$. מהמשוואה הראשונה $z=-x-y=-2x$. עבור $x=1$ מקבלים $c=-2$.",
       "promptHtml": "במערכת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>a</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mtext> </mtext><mi>x</mi><mo>+</mo><mi>a</mi><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x+y+z=0,\\ ax+y=0,\\ x+ay=0</annotation></semantics></math></span> מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=-1</annotation></semantics></math></span>. הפתרון הוא ישר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>t</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mi>c</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">t(1,1,c)</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>c</mi></mrow><annotation encoding=\"application/x-tex\">c</annotation></semantics></math></span> ?",
       "explainHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=-1</annotation></semantics></math></span> המשוואות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">-x+y=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x-y=0</annotation></semantics></math></span> זהות, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>. מהמשוואה הראשונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>z</mi><mo>=</mo><mo>−</mo><mi>x</mi><mo>−</mo><mi>y</mi><mo>=</mo><mo>−</mo><mn>2</mn><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">z=-x-y=-2x</annotation></semantics></math></span>. עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>c</mi><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">c=-2</annotation></semantics></math></span>."
      },
      "recap": "מציבים את הערך הקריטי ופותרים.",
      "recapHtml": "מציבים את הערך הקריטי ופותרים."
     }
    ]
   },
   {
    "id": "C08",
    "order": 8,
    "icon": "🏆",
    "title": "בוס: שאלות מבחן אמיתיות",
    "goal": "לפתור שאלות פרמטר מבחינות קודמות: סיווג, פתרון כפונקציית הפרמטר, פתרון כללי ומערכת הומוגנית.",
    "source": "ai-verified",
    "boss": true,
    "lesson": {
     "html": "\n<p>בשלב הזה כל השאלות מבחינות אמיתיות. אותו מתכון תמיד:</p>\n<div class=\"lesson-rule\">🔑 (1) כותבים מטריצה מורחבת. (2) מדרגים בלי לחלק בפרמטר. (3) אפסי המקדם האחרון הם הערכים הקריטיים. (4) בכל ערך קריטי מציבים בשורה האחרונה ובודקים את האיבר החופשי. (5) שאר הערכים: פתרון יחיד, ואם צריך מחלצים אותו. (6) לפתרון כללי: משתנה חופשי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>=</mo><mi>t</mi></mrow><annotation encoding=\"application/x-tex\">=t</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mover accent=\"true\"><mi>x</mi><mo>⃗</mo></mover><mo>=</mo><mover accent=\"true\"><mi>p</mi><mo>⃗</mo></mover><mo>+</mo><mi>t</mi><mover accent=\"true\"><mi>d</mi><mo>⃗</mo></mover></mrow><annotation encoding=\"application/x-tex\">\\vec x=\\vec p+t\\vec d</annotation></semantics></math></span>. (7) במערכת הומוגנית שואלים על הדרגה בלבד.</div>\n<div class=\"lesson-trap\">⚠️ התשובה \"אף ערך של הפרמטר\" או \"לכל ערך\" היא תשובה אפשרית. כשהשורה האחרונה היא כפולה של המקדם, אין סתירה בשום ערך.</div>\n<div class=\"lesson-trap\">⚠️ מערכת עם יותר משוואות מנעלמים: משוואה מיותרת מתאפסת בדירוג ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mn>0</mn><mtext> </mtext><mi mathvariant=\"normal\">∣</mi><mtext> </mtext><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0\\ 0\\ 0\\,|\\,0)</annotation></semantics></math></span>, ואין צורך לחשוש ממנה.</div>\n"
    },
    "questions": [
     {
      "bankId": "22B-A-Q2a",
      "recap": "דירוג, ערך קריטי k=3, ופתרון יחיד כפונקציה של k.",
      "recapHtml": "דירוג, ערך קריטי k=3, ופתרון יחיד כפונקציה של k."
     },
     {
      "bankId": "22B-A-Q2b",
      "recap": "השורה האחרונה היא כפולה של 3-k, ולכן אין סתירה באף ערך.",
      "recapHtml": "השורה האחרונה היא כפולה של 3-k, ולכן אין סתירה באף ערך."
     },
     {
      "bankId": "24A-A-Q2b",
      "recap": "סתירה רק בערך קריטי שבו האיבר החופשי שונה מאפס.",
      "recapHtml": "סתירה רק בערך קריטי שבו האיבר החופשי שונה מאפס."
     },
     {
      "bankId": "25B-A-Q2b",
      "recap": "ארבע משוואות, אחת מתאפסת בדירוג, ואז מסווגים לפי המקדם האחרון.",
      "recapHtml": "ארבע משוואות, אחת מתאפסת בדירוג, ואז מסווגים לפי המקדם האחרון."
     },
     {
      "bankId": "25B-A-Q2c",
      "recap": "פתרון כללי: משתנה חופשי t ופתרון פרטי ועוד t כפול כיוון.",
      "recapHtml": "פתרון כללי: משתנה חופשי t ופתרון פרטי ועוד t כפול כיוון."
     },
     {
      "bankId": "25A-A-Q2c",
      "recap": "הומוגנית: הדרגה 2 נותנת ישר, ומציבים כל ערך קריטי לפני החלוקה.",
      "recapHtml": "הומוגנית: הדרגה 2 נותנת ישר, ומציבים כל ערך קריטי לפני החלוקה."
     }
    ]
   }
  ]
 }
};
