# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-A.json -- linear algebra, semester A 2025, moed A (23.02.2025), flagship sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25A-A.py

Source: sitting 25A-A, 12pp (exam text and official solution interleaved in one PDF). Five questions of 25 points
(best 4 count), 17 items. Q1-Q3 and Q5 are typed solutions, Q4's solution is handwritten (tablet) in the same file.
Flagship choice: 25B-A (newer) has no solution for Q6, 25A-B (newer) has none for Q4, so 25A-A is the most recent
sitting whose official solution covers every question. (The triage said 6 questions; the printed exam has 5.)

Transcription notes
- Q1: the exam does not name the lines; the official solution calls them l1 (first) and l2 (second). The labels are
  added in the shared context. Part (g) of the stem prints "השל" (typo for "של"); kept as printed.
- Q4 (the "d" part): the handwritten official line reads Q(x)=1*x^2+2*x^2+0*x+1*1. The intended combination is
  1*x^3+2*x^2+0*x+3*1 (Q is x^3+2x^2+3). The official typo is flagged inside the solution text.
- Q5 "b": the official text says dim Im T != dim R^4, but the codomain of T is M_2x2 (dimension 4) -- slip in the
  official solution, flagged inside the solution text. The conclusion (not onto) is unaffected.
- Q5 has two independent items (1, 2). Parts are single letters in the raw schema: a, b, c = items 1.a, 1.b, 1.c
  and d = item 2 (change-of-basis matrix).
- Q3 "b": the official solution gives D and P but does not display the product check BP=PD. Not added.

Checks (sympy, tools/verify/25A-A/verify_25A-A.py, 37 checks): every official computation reproduces
(intersection a=2, planes, rank by a, nullspaces at a=0,1,-1, inverse and its six-factor product, D and P,
bases and dimensions in R3[x], Ker/Im of T, a=b=-2, change-of-basis matrix). No mismatch, no hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-A.json"


def Q(num, part, kind, topic, question, solution, points, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question,
         "solution": solution, "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


def pm(*rows):
    """matrix; a row is a list of cells or one 'a&b&c' string"""
    return r"\begin{pmatrix}" + r"\\".join(r if isinstance(r, str) else "&".join(str(c) for c in r) for r in rows) + r"\end{pmatrix}"


def aug(rows, left=3):
    """augmented matrix with a vertical bar after `left` columns"""
    n = len(rows[0])
    spec = "c" * left + "|" + "c" * (n - left)
    return r"\left(\begin{array}{" + spec + "}" + r"\\".join("&".join(str(c) for c in r) for r in rows) + r"\end{array}\right)"


def arrow(op):
    return r"\xrightarrow{" + op + "}"


# ------------------------------------------------------------------ contexts
contexts = {
    "c1": {"kind": "text", "title": "שאלה 1 - שני ישרים",
           "text": "נתונים שני הישרים\n"
                   r"$\ell_1:\ (x,y,z)=(0,a,-a)+s(1,0,1),\ s\in\mathbb{R}$" "\n"
                   r"$\ell_2:\ (x,y,z)=(5,-4,-1)+t(a,-3,0),\ t\in\mathbb{R}$" "\n"
                   r"כאשר $a\neq 0$ מספר ממשי."},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת הומוגנית עם פרמטר",
           "text": "תהי המערכת הלינארית ההומוגנית הבאה:\n"
                   r"$$\begin{cases} ax+ay-z=0\\ a^2x+ay+(a^2-a)z=0\\ ax+ay+(2a+1)z=0\end{cases}$$"},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של פולינומים",
           "text": r"יהי $\mathbb{R}_3[x]$ מרחב של פולינומים ממשיים ממעלה שלוש לכל היותר. נגדיר שני תתי מרחבים של מרחב זה:" "\n"
                   r"$W_1=\{p(x)\in\mathbb{R}_3[x]:\ p(0)=p'(0)=p''(0)\}$" "\n"
                   r"$W_2=\{q(x)\in\mathbb{R}_3[x]:\ q'(0)=0\}$"},
    "c5": {"kind": "text", "title": "שאלה 5 - העתקה מפולינומים למטריצות",
           "text": r"נתונה העתקה לינארית $T:\mathbb{R}_3[x]\to M_{2\times2}(\mathbb{R})$ ממרחב הפולינומים ממעלה 3 ומטה אל מרחב המטריצות הריבועיות $2\times 2$, המוגדרת על ידי:" "\n"
                   r"$$T(1)=" + pm("1&1", "1&1") + r",\quad T(x)=" + pm("2&0", "2&5") + r",\quad "
                   r"T(x^2)=" + pm("12&10", "12&15") + r",\quad T(x^3)=" + pm("21&1", "21&51") + "$$"},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "computation", "lines_planes",
    r"מצאו $a>0$ עבורו $\ell_1$ ו-$\ell_2$ הם ישרים נחתכים.",
    r"וקטורי הכיוון של $\ell_1$ ו-$\ell_2$ הם, בהתאמה, $\vec L_1=(1,0,1)$ ו-$\vec L_2=(a,-3,0)$. "
    r"נשים לב לכך שלא קיים $\alpha\in\mathbb{R}$ סקלארי כך ש-$\vec L_2=\alpha\vec L_1$, ולכן הישרים אינם מקבילים. "
    "כדי לבדוק האם $\\ell_1$ ו-$\\ell_2$ נחתכים או מצטלבים ננסה למצוא נקודה משותפת:\n"
    r"$$(0,a,-a)+s(1,0,1)=(5,-4,-1)+t(a,-3,0),\quad s,t\in\mathbb{R}$$" "\n"
    "מכאן נקבל שלוש משוואות:\n"
    r"$$(I)\ s=5+at,\qquad (II)\ a=-4-3t,\qquad (III)\ -a+s=-1$$" "\n"
    r"ממשוואה $(III)$ נקבל $s=a-1$. נציב ב-$(I)$ ונקבל $a-1=5+at$. ממשוואה $(II)$ נקבל $t=-\frac{a+4}{3}$. נציב במשוואה הנ״ל ונקבל:" "\n"
    r"$$a-1=5+a\cdot\left(-\frac{a+4}{3}\right)\ \Rightarrow\ 3a-18=-a(a+4)\ \Rightarrow\ a^2+7a-18=0$$" "\n"
    r"$$a_{1,2}=\frac{-7\pm\sqrt{49+4\cdot 18}}{2}=\frac{-7\pm 11}{2}\ \Rightarrow\ a_1=-9,\quad a_2=2$$" "\n"
    r"וכיוון ש-$a>0$ נקבל $a=2$.",
    9, contextId="c1"))

questions.append(Q(
    1, "ב", "computation", "lines_planes",
    r"עבור הערך של $a$ מסעיף (א), מצאו את המשוואה של המישור המכיל את הישרים הנתונים $\ell_1$ ו-$\ell_2$.",
    r"נסמן את המישור המבוקש ב-$S_1$. נציב $a=2$ בוקטורי הכיוון מסעיף (א) ונקבל $\vec L_2=(2,-3,0)$ ו-$\vec L_1=(1,0,1)$. "
    r"עתה נוכל למצוא וקטור נורמלי ל-$S_1$ ע״י" "\n"
    r"$$\vec N_1=\vec L_1\times\vec L_2=\begin{vmatrix}\hat\imath&\hat\jmath&\hat k\\1&0&1\\2&-3&0\end{vmatrix}=3\hat\imath+2\hat\jmath-3\hat k=(3,2,-3)$$" "\n"
    r"בנוסף, כיוון ש-$\ell_1$ מוכל ב-$S_1$, נקבל שאם נציב $s=0$ בביטוי עבור $\ell_1$, הנקודה $p_0(0,2,-2)\in S_1$. "
    r"לכן, אם $p(x,y,z)\in S_1$, משוואת המישור ניתנת ע״י $\overrightarrow{p_0p}\cdot\vec N_1=0$:" "\n"
    r"$$(x-0,\,y-2,\,z+2)\cdot(3,2,-3)=0\ \Rightarrow\ 3x+2(y-2)-3(z+2)=0\ \Rightarrow\ 3x+2y-3z=10$$" "\n"
    r"על-כן הצורה הקנונית של משוואת המישור $S_1$ היא $S_1:\ 3x+2y-3z=10$.",
    8, contextId="c1"))

questions.append(Q(
    1, "ג", "computation", "lines_planes",
    r"מצאו את המשוואה השל המישור המכיל את הישר $\ell_1$ ומאונך למישור שמצאתם בסעיף (ב).",
    r"נסמן את המישור המבוקש ב-$S_2$. וקטור נורמלי ל-$S_2$, $\vec N_2$, צריך להיות מאונך ל-$\vec L_1$ ול-$\vec N_1$. מכאן נקבל" "\n"
    r"$$\vec N_2=\vec L_1\times\vec N_1=\begin{vmatrix}\hat\imath&\hat\jmath&\hat k\\1&0&1\\3&2&-3\end{vmatrix}=-2\hat\imath+6\hat\jmath+2\hat k=2(-1,3,1)$$" "\n"
    r"בנוסף, כיוון ש-$\ell_1$ מוכל ב-$S_2$ ומתקיים $p_0(0,2,-2)\in S_2$, אם $p(x,y,z)\in S_2$ אז $\overrightarrow{p_0p}\cdot\vec N_2=0$:" "\n"
    r"$$(x-0,\,y-2,\,z+2)\cdot(-1,3,1)=0\ \Rightarrow\ -x+3(y-2)+(z+2)=0\ \Rightarrow\ -x+3y+z=4$$" "\n"
    r"על-כן המשוואה הקנונית של המישור $S_2$ היא $S_2:\ -x+3y+z=4$.",
    8, contextId="c1"))

# ------------------------------------------------------------------ Q2
Z = [["a", "a", "-1", "0"], ["a^2", "a", "a^2-a", "0"], ["a", "a", "2a+1", "0"]]
Z1 = [["a", "a", "-1", "0"], ["0", "a-a^2", "a^2", "0"], ["0", "0", "2a+2", "0"]]
Z2 = [["a", "a", "-1", "0"], ["0", "1", r"\frac{a}{1-a}", "0"], ["0", "0", "1", "0"]]

questions.append(Q(
    2, "א", "computation", "linear_systems",
    "מצאו צורה מדורגת של מטריצה מורחבת.",
    "המטריצה המורחבת של המערכת, ודירוג שלה:\n"
    "$$" + aug(Z) + arrow(r"\substack{R_2\to R_2-a\cdot R_1\\R_3\to R_3-R_1}") + aug(Z1) + "$$\n"
    r"מתקיים:" "\n"
    "$$" + aug(Z1) + arrow(r"\substack{R_2\to R_2\cdot\frac{1}{a(1-a)}\\R_3\to R_3\cdot\frac{1}{2(a+1)}}") + aug(Z2) + "$$\n"
    r"כאשר החילוק בשורה 2 מותר עבור $a\neq 0,1$ והחילוק בשורה 3 מותר עבור $a\neq -1$.",
    8, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור אילו ערכי $a$ יש למערכת פתרון טריוויאלי בלבד (כלומר רק וקטור ה-$0$)?",
    r"עבור $a\neq 0,1,-1$ מתקיים $r(A)=3$, ולכן יש למערכת **פתרון יחיד** והוא הפתרון הטריוויאלי.",
    5, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור אילו ערכי $a$ הפתרון הכללי של המערכת הינו ישר (איבר חופשי אחד)?",
    r"**עבור $a=-1$:** נציב $a=-1$ בשלב שלפני החלוקה ונקבל את המטריצה" "\n"
    "$$" + pm("-1&-1&-1", "0&-2&1", "0&0&0") + "$$\n"
    r"ולכן עבור $a=-1$ מתקיים $r(A)=2$ ולמערכת **יש אינסוף פתרונות עם מקדם חופשי אחד**. "
    r"מהמשוואה השנייה נובע כי $z=2y$, ואם נציב קשר זה במשוואה הראשונה נקבל $x=-y-z=-y-2y=-3y$; $y$ משתנה חופשי. "
    r"מרחב הפתרונות במקרה זה נתון ע״י" "\n"
    r"$$\left\{\begin{pmatrix}-3y\\y\\2y\end{pmatrix}:\ y\in\mathbb{R}\right\}$$" "\n"
    r"**עבור $a=1$:** נציב $a=1$ בשלב שלפני החלוקה ונקבל את המטריצה" "\n"
    "$$" + pm("1&1&-1", "0&0&1", "0&0&4") + arrow(r"R_3\to R_3-4R_2") + pm("1&1&-1", "0&0&1", "0&0&0") + "$$\n"
    r"ולכן עבור $a=1$ מתקיים $r(A)=2$ ולמערכת **יש אינסוף פתרונות עם מקדם חופשי אחד**. "
    r"מהמשוואה השנייה נובע כי $z=0$, ואם נציב זאת במשוואה הראשונה נקבל $x+y+0=0\Rightarrow y=-x$; $x$ משתנה חופשי. "
    r"מרחב הפתרונות במקרה זה נתון ע״י" "\n"
    r"$$\left\{\begin{pmatrix}t\\-t\\0\end{pmatrix}:\ t\in\mathbb{R}\right\}$$",
    6, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "linear_systems",
    r"עבור אילו ערכי $a$ הפתרון הכללי של המערכת הינו מישור (2 איברים חופשיים)?",
    r"**עבור $a=0$:** נציב $a=0$ בשלב שלפני החלוקה ונקבל את המטריצה" "\n"
    "$$" + pm("0&0&-1", "0&0&0", "0&0&2") + arrow(r"R_3\to R_3+2R_1") + pm("0&0&-1", "0&0&0", "0&0&0") + "$$\n"
    r"ולכן במקרה זה $r(A)=1$ ולמערכת יש **אינסוף פתרונות עם 2 מקדמים חופשיים**. "
    r"מהמשוואה הראשונה נובע מיד כי $z=0$, ואילו $x,y$ משתנים חופשיים. מרחב הפתרונות במקרה זה נתון ע״י" "\n"
    r"$$\left\{\begin{pmatrix}x\\y\\0\end{pmatrix}:\ x,y\in\mathbb{R}\right\}$$",
    6, contextId="c2"))

# ------------------------------------------------------------------ Q3
questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"נתונה המטריצה $A=" + pm("1&2&1", "0&1&3", "3&8&8") + r"$. מצאו את $A^{-1}$ וכתבו אותה כמכפלה של מטריצות אלמנטריות.",
    r"תחילה נחשב את $A^{-1}$:" "\n"
    "$$" + aug([["1", "2", "1", "1", "0", "0"], ["0", "1", "3", "0", "1", "0"], ["3", "8", "8", "0", "0", "1"]])
    + arrow(r"R_3\to R_3-3R_1")
    + aug([["1", "2", "1", "1", "0", "0"], ["0", "1", "3", "0", "1", "0"], ["0", "2", "5", "-3", "0", "1"]]) + "$$\n"
    "$$" + arrow(r"R_3\to R_3-2R_2")
    + aug([["1", "2", "1", "1", "0", "0"], ["0", "1", "3", "0", "1", "0"], ["0", "0", "-1", "-3", "-2", "1"]])
    + arrow(r"R_3\to -R_3")
    + aug([["1", "2", "1", "1", "0", "0"], ["0", "1", "3", "0", "1", "0"], ["0", "0", "1", "3", "2", "-1"]]) + "$$\n"
    "$$" + arrow(r"R_2\to R_2-3R_3")
    + aug([["1", "2", "1", "1", "0", "0"], ["0", "1", "0", "-9", "-5", "3"], ["0", "0", "1", "3", "2", "-1"]])
    + arrow(r"R_1\to R_1-R_3")
    + aug([["1", "2", "0", "-2", "-2", "1"], ["0", "1", "0", "-9", "-5", "3"], ["0", "0", "1", "3", "2", "-1"]]) + "$$\n"
    "$$" + arrow(r"R_1\to R_1-2R_2")
    + aug([["1", "0", "0", "16", "8", "-5"], ["0", "1", "0", "-9", "-5", "3"], ["0", "0", "1", "3", "2", "-1"]]) + "$$\n"
    r"קיבלנו שהמטריצה ההופכית היא:" "\n"
    "$$A^{-1}=" + pm("16&8&-5", "-9&-5&3", "3&2&-1") + "$$\n"
    r"כעת נשתמש בדירוג הנ״ל ונכתוב את $A^{-1}$ כמכפלה של מטריצות אלמנטריות:" "\n"
    "$$A^{-1}=" + pm("1&-2&0", "0&1&0", "0&0&1") + pm("1&0&-1", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&-3", "0&0&1")
    + pm("1&0&0", "0&1&0", "0&0&-1") + pm("1&0&0", "0&1&0", "0&-2&1") + pm("1&0&0", "0&1&0", "-3&0&1") + "$$",
    10))

questions.append(Q(
    3, "ב", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + pm("9&0&1", "0&8&0", "1&0&9") + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $BP=PD$ (יש לבדוק שהשוויון מתקיים).",
    r"**1. הערכים העצמיים והווקטורים העצמיים של $B$.**" "\n"
    r"$$|\lambda I-B|=\begin{vmatrix}\lambda-9&0&-1\\0&\lambda-8&0\\-1&0&\lambda-9\end{vmatrix}=(\lambda-8)\begin{vmatrix}\lambda-9&-1\\-1&\lambda-9\end{vmatrix}=$$" "\n"
    r"$$=(\lambda-8)\left[(\lambda-9)^2-1\right]=(\lambda-8)(\lambda^2-18\lambda+80)=(\lambda-8)(\lambda-8)(\lambda-10)$$" "\n"
    r"קיבלנו שהערכים העצמיים הם $8,10$. כעת נמצא את הווקטורים העצמיים." "\n"
    r"**עבור $\lambda=8$:**" "\n"
    "$$" + pm("-1&0&-1", "0&0&0", "-1&0&-1") + r"\to\dots\to" + pm("1&0&1", "0&0&0", "0&0&0") + "$$\n"
    r"נסמן $y=t,\ z=s$ ונקבל $x=-s$. הוקטורים העצמיים המתקבלים הם $\begin{pmatrix}-1\\0\\1\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix}$." "\n"
    r"**עבור $\lambda=10$:**" "\n"
    "$$" + pm("1&0&-1", "0&2&0", "-1&0&1") + r"\to\dots\to" + pm("1&0&-1", "0&2&0", "0&0&0") + "$$\n"
    r"נסמן $z=t$ ונקבל $x=t,\ y=0$. הוקטור העצמי המתקבל הוא $\begin{pmatrix}1\\0\\1\end{pmatrix}$." "\n"
    r"**2.** נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$:" "\n"
    "$$D=" + pm("8&0&0", "0&8&0", "0&0&10") + r",\qquad P=" + pm("-1&0&1", "0&1&0", "1&0&1") + "$$",
    15))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של תתי המרחבים $W_1$ ו-$W_2$.",
    r"נגדיר את ההצגה הקואורדינטית של פולינום $p(x)\in\mathbb{R}_3[x]$ בבסיס הסטנדרטי: $p(x)=ax^3+bx^2+cx+d\ \longleftrightarrow\ (a,b,c,d)$." "\n"
    r"**מציאת בסיס ל-$W_1$:**" "\n"
    r"$$p(x)=ax^3+bx^2+cx+d,\ p(0)=d;\quad p'(x)=3ax^2+2bx+c,\ p'(0)=c;\quad p''(x)=6ax+2b,\ p''(0)=2b$$" "\n"
    r"ולכן $d=c=2b$. אם כן, הפולינום ב-$W_1$ הוא מהצורה" "\n"
    r"$$p(x)=ax^3+bx^2+2bx+2b=ax^3+b(x^2+2x+2),\quad a,b\in\mathbb{R}$$" "\n"
    r"ובהצגה הקואורדינטית $W_1=\mathrm{Sp}\left\{\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\2\\2\end{pmatrix}\right\}$. "
    r"הבסיס הוא $B_{W_1}=\{x^3,\ x^2+2x+2\}$ (שני וקטורים שאינם כפולה אחד של השני), ו-$\dim W_1=2$." "\n"
    r"**מציאת בסיס ל-$W_2$:** $q(x)=ax^3+bx^2+cx+d$, $q'(x)=3ax^2+2bx+c$, $q'(0)=c$, ולכן $c=0$. "
    r"אם כן, הפולינום ב-$W_2$ הוא מהצורה $q(x)=ax^3+bx^2+d$, $a,b,d\in\mathbb{R}$, כלומר $W_2=\mathrm{Sp}\{x^3,x^2,1\}$. "
    r"בהצגה הקואורדינטית $W_2=\mathrm{Sp}\left\{\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\0\\1\end{pmatrix}\right\}$. "
    r"הבסיס הוא $B_{W_2}=\{x^3,x^2,1\}$, ו-$\dim W_2=3$.",
    6, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"חשבו תת מרחב $W_1+W_2$, מצא בסיס ומימד של תת מרחב זה.",
    r"$W_1+W_2=\mathrm{Sp}\{B_{W_1},B_{W_2}\}=\mathrm{Sp}\{x^3,\ x^2+2x+2,\ x^3,\ x^2,\ 1\}$, כלומר בהצגה הקואורדינטית" "\n"
    r"$$W_1+W_2=\mathrm{Sp}\left\{\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\2\\2\end{pmatrix},\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\0\\1\end{pmatrix}\right\}$$" "\n"
    r"מכיוון שהווקטור הראשון והשלישי זהים, ניתן לפסול אחד מהם, ולבדוק האם הקבוצה הנותרת בת״ל ע״י דירוג מטריצה שכל שורה בה היא וקטור:" "\n"
    "$$" + pm("1&0&0&0", "0&1&0&0", "0&1&2&2", "0&0&0&1") + arrow(r"R_3\to R_3-R_2") + pm("1&0&0&0", "0&1&0&0", "0&0&2&2", "0&0&0&1")
    + arrow(r"\substack{R_3\to R_3/2\\R_3\to R_3-R_4}") + pm("1&0&0&0", "0&1&0&0", "0&0&1&0", "0&0&0&1") + "$$\n"
    r"קיבלנו מטריצה יחידה, ולכן 4 הווקטורים שנותרו מהווים קבוצה בת״ל. אם כן" "\n"
    r"$$B_{W_1+W_2}=\{x^3,x^2,x,1\},\qquad \dim(W_1+W_2)=4$$",
    8, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"חשבו תת מרחב $W_1\cap W_2$, מצא בסיס ומימד של תת מרחב זה.",
    r"נחפש וקטורים משותפים: נבחר צירוף לינארי של בסיס $W_1$ ובסיס $W_2$, ונדרוש ששני הצירופים שווים, כלומר" "\n"
    r"$$\alpha_1\begin{pmatrix}1\\0\\0\\0\end{pmatrix}+\alpha_2\begin{pmatrix}0\\1\\2\\2\end{pmatrix}+\beta_1\begin{pmatrix}1\\0\\0\\0\end{pmatrix}+\beta_2\begin{pmatrix}0\\1\\0\\0\end{pmatrix}+\beta_3\begin{pmatrix}0\\0\\0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\end{pmatrix}$$" "\n"
    r"(הסימון $\beta_i$ כולל את הסימן המינוס של צד $W_2$). נדרג את מטריצת המקדמים:" "\n"
    "$$" + pm("1&0&1&0&0", "0&1&0&1&0", "0&2&0&0&0", "0&2&0&0&1") + r"\to\dots\to" + pm("1&0&1&0&0", "0&1&0&0&0", "0&0&0&1&0", "0&0&0&0&1") + "$$\n"
    r"נקבל $\beta_1=t\in\mathbb{R}$ ו-$\beta_2=\beta_3=0$, ולכן $W_1\cap W_2=\mathrm{Sp}\left\{t\begin{pmatrix}1\\0\\0\\0\end{pmatrix}\right\}$. אם כן" "\n"
    r"$$B_{W_1\cap W_2}=\{x^3\},\qquad \dim(W_1\cap W_2)=1$$",
    8, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם הפולינום $Q(x)=x^3+2x^2+3$ שייך לתת מרחב $W_1+W_2$? נמקו את תשובתכם.",
    r"כן. $Q(x)=x^3+2x^2+3$ שייך ל-$W_1+W_2$ כי ניתן להציגו כצירוף לינארי של איברי הבסיס $B_{W_1+W_2}=\{x^3,x^2,x,1\}$:" "\n"
    r"$$Q(x)=1\cdot x^3+2\cdot x^2+0\cdot x+3\cdot 1$$" "\n"
    r"(הערת תמלול: בפתרון הרשמי כתוב בכתב יד $Q(x)=1\cdot x^2+2\cdot x^2+0\cdot x+1\cdot 1$ - טעות כתיבה; הצירוף הנכון הוא כמוצג למעלה.)",
    3, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד ובסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    r"בסיס סטנדרטי של $M_{2\times2}(\mathbb{R})$ הוא" "\n"
    r"$$E=\left(\begin{pmatrix}1&0\\0&0\end{pmatrix},\begin{pmatrix}0&1\\0&0\end{pmatrix},\begin{pmatrix}0&0\\1&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix}\right)$$" "\n"
    r"ו-$F=(1,x,x^2,x^3)$ הוא בסיס סטנדרטי של $\mathbb{R}_3[x]$. המטריצה המייצגת הסטנדרטית היא" "\n"
    "$$A=[T]_E^F=" + pm("1&2&12&21", "1&0&10&1", "1&2&12&21", "1&5&15&51") + "$$\n"
    "$$" + aug([["1", "2", "12", "21", "0"], ["1", "0", "10", "1", "0"], ["1", "2", "12", "21", "0"], ["1", "5", "15", "51", "0"]], 4)
    + r"\Leftrightarrow" + aug([["1", "2", "12", "21", "0"], ["0", "-2", "-2", "-20", "0"], ["0", "0", "0", "0", "0"], ["0", "3", "3", "30", "0"]], 4)
    + r"\Leftrightarrow" + aug([["1", "2", "12", "21", "0"], ["0", "1", "1", "10", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$\n"
    r"עמודות מס׳ 1,2 של המטריצה המדורגת מובילות, אז $\mathrm{Col}A$ בסיס של" "\n"
    r"$$\left(\begin{pmatrix}1\\1\\1\\1\end{pmatrix},\begin{pmatrix}2\\0\\2\\5\end{pmatrix}\right)$$" "\n"
    r"ז״א בסיס של $\mathrm{Im}\,T$ הוא $\left(\begin{pmatrix}1&1\\1&1\end{pmatrix},\begin{pmatrix}2&0\\2&5\end{pmatrix}\right)$ ו-$\dim\mathrm{Im}\,T=2$." "\n"
    r"בנוסף לזאת:" "\n"
    "$$" + aug([["1", "0", "10", "1", "0"], ["0", "1", "1", "10", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4)
    + r"\Leftrightarrow\begin{cases}x_1=-10s_1-1s_2\\x_2=-s_1-10s_2\\x_3=s_1\\x_4=s_2\end{cases}\Leftrightarrow"
    r"\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}=s_1\begin{pmatrix}-10\\-1\\1\\0\end{pmatrix}+s_2\begin{pmatrix}-1\\-10\\0\\1\end{pmatrix}$$" "\n"
    r"אז $\mathrm{Nul}A$ בסיס של $\left(\begin{pmatrix}-10\\-1\\1\\0\end{pmatrix},\begin{pmatrix}-1\\-10\\0\\1\end{pmatrix}\right)$, ז״א בסיס של $\mathrm{Ker}\,T$ הוא $\left(-10-x+x^2,\ -1-10x+x^3\right)$ ו-$\dim\mathrm{Ker}\,T=2$.",
    12, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חח״ע? האם $T$ על? נמקו.",
    r"$T$ לא חח״ע כי $\dim\mathrm{Ker}\,T=2\neq 0$, ו-$T$ לא על כי $\dim\mathrm{Im}\,T=2\neq\dim M_{2\times2}(\mathbb{R})=4$." "\n"
    r"(הערת תמלול: בפתרון הרשמי כתוב $\dim\mathbb{R}^4$ במקום $\dim M_{2\times2}(\mathbb{R})$ - אין זה משנה את המסקנה, כי $\dim M_{2\times2}(\mathbb{R})=4$.)",
    3, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטרים $a,b$ מתקיים $22+22x+ax^2+bx^3\in\mathrm{Ker}\,T$?",
    r"הפולינום שייך ל-$\mathrm{Ker}\,T$ אם ורק אם וקטור הקואורדינטות שלו $(22,22,a,b)$ הוא צירוף לינארי של בסיס ה-$\mathrm{Ker}\,T$, כלומר המערכת עם העמודה האחרונה $(22,22,a,b)$ פתירה:" "\n"
    "$$" + aug([["-10", "-1", "22"], ["-1", "-10", "22"], ["1", "0", "a"], ["0", "1", "b"]], 2) + r"\to"
    + aug([["-1", "-10", "22"], ["-10", "-1", "22"], ["1", "0", "a"], ["0", "1", "b"]], 2) + r"\to"
    + aug([["-1", "-10", "22"], ["0", "99", "-198"], ["0", "-10", "a+22"], ["0", "1", "b"]], 2) + r"\to"
    + aug([["-1", "-10", "22"], ["0", "1", "-2"], ["0", "-10", "a+22"], ["0", "1", "b"]], 2) + r"\to"
    + aug([["-1", "-10", "22"], ["0", "1", "-2"], ["0", "0", "a+2"], ["0", "0", "b+2"]], 2) + "$$\n"
    r"$$\begin{cases}a+2=0\\b+2=0\end{cases}\Rightarrow\begin{cases}a=-2\\b=-2\end{cases}$$",
    5, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "vector_spaces",
    r"נתונים בסיסים $B=\left(\begin{pmatrix}2\\2\end{pmatrix},\begin{pmatrix}0\\5\end{pmatrix}\right)$, $C=\left(\begin{pmatrix}1\\3\end{pmatrix},\begin{pmatrix}2\\7\end{pmatrix}\right)$ של מרחב $\mathbb{R}^2$. "
    r"מצאו את מטריצת המעבר $[I]_C^B$ מבסיס $B$ לבסיס $C$. (שאלה 5 סעיף 2; אין קשר בין סעיף 1 לסעיף 2.)",
    r"נסמן ב-$E$ בסיס סטנדרטי של $\mathbb{R}^2$:" "\n"
    r"$$[I]_E^B=\begin{pmatrix}2&0\\2&5\end{pmatrix},\qquad [I]_E^C=\begin{pmatrix}1&2\\3&7\end{pmatrix}$$" "\n"
    r"**שיטה 1:**" "\n"
    r"$$[I]_C^B=[I]_C^E[I]_E^B=\left([I]_E^C\right)^{-1}[I]_E^B=\begin{pmatrix}1&2\\3&7\end{pmatrix}^{-1}\begin{pmatrix}2&0\\2&5\end{pmatrix}=\begin{pmatrix}7&-2\\-3&1\end{pmatrix}\begin{pmatrix}2&0\\2&5\end{pmatrix}=\begin{pmatrix}10&-10\\-4&5\end{pmatrix}$$" "\n"
    r"**שיטה 2:**" "\n"
    "$$" + aug([["1", "2", "2", "0"], ["3", "7", "2", "5"]], 2) + r"\to" + aug([["1", "2", "2", "0"], ["0", "1", "-4", "5"]], 2) + r"\to"
    + aug([["1", "0", "10", "-10"], ["0", "1", "-4", "5"]], 2) + r"\to[I]_C^B=\begin{pmatrix}10&-10\\-4&5\end{pmatrix}$$",
    5))

exam = {
    "examCode": "25A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״ה, מועד א׳ (23.02.2025)",
    "year": 2025,
    "examDate": "23.02.2025",
    "sourceFile": "25A-A exam + official solution (single PDF)",
    "solutionFile": "25A-A exam + official solution (single PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
