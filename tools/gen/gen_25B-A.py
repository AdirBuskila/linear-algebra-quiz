# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-A.json -- linear algebra, semester B 2025, moed A (07.07.2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25B-A.py

Sources: the exam is a 3-page phone photo (tools/raw/25B-A-SRC); the answers come from a separate typed solution-only
PDF (8pp, tools/raw/25B-A-SOL). The solution header prints "semester A ... moed H', 16.06.2025", which mismatches the
photo (semester B, moed A, 07.07.2025), but Q1 (S1,S2,S3), Q2 (a-system), Q3, Q4 (symmetric matrices and U) and Q5 match
the photo question by question, so it is the same exam. Six questions of 25 points (best 4 count), 21 items.
The solution file stops after Q5: Q6 (3 parts) has NO official solution and is held "no-key" (routed to the solver).

Transcription notes
- Parts are single letters in the raw schema. Printed numbering -> raw part: Q3: 1 -> א, 2 -> ב, "ב" -> ג;
  Q5: 1 -> א, 2 -> ב, 3 -> ג, "ב" (basis change) -> ד.
- Q2: the official solution labels do not follow the printed parts. The first block (echelon form) answers part א; the
  three case lines (unique / none / infinite) answer part ב; the a=-1 solution (labelled ב in the official file) answers
  part ג; the complex equation (labelled ג) answers part ד. The official labels the third root z_3; it is the third root
  (index 2). Kept; labelled in the solution.
- Q1 ג: the official gives l2 = (-1/2,1/2,0) + 1/2 s (-3,1,2) in part א but solves part ג with direction s(-3,1,2)
  (equations (I)-(III)); the final point (2,-1/3,-5/3) is correct either way (sympy). Flagged in the solution.
- Q3 ב: the official determinant is headed |lambda I - A| (A for B). Kept as a labelled note.
- Q4 ג: the official labels the U+W and U cap W blocks ג and ד, then labels the membership check ד again; they are
  placed in the printed parts ג (10 pts, both subspaces) and ד (5 pts). In the intersection the official concludes
  d2=1, d1=-1 but writes v = (1,2,-1,3) - (2,0,-3,2) = (-1,2,2,1) (that is d1=1, d2=-1); -u1+u2 = (1,-2;-2,-1) is the
  negative. The line spanned and the basis ((-1,2),(2,1)) are right. Flagged in the solution.
- The photo's page header lists lecturer names; none is copied.

Checks (sympy, tools/verify/25B-A/verify_25B-A.py): every official computation reproduces (lines and planes, point and
l3, echelon form and cases by a, a=-1 solution, the three cube roots and z-values, inverse and its four-factor product,
eigenvalues, P and D with PD=BP, bases of W, U+W, U cap W, Ker/Im of T, m=26, change-of-basis matrix and coordinates).
No mismatch. Only the two sign/label slips above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-A.json"


def Q(num, part, kind, topic, question, solution, points=None, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "question": question,
         "solution": solution, "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if points is not None:
        q["points"] = points
    q.update(kw)
    return q


def pm(*rows):
    return r"\begin{pmatrix}" + r"\\".join(r if isinstance(r, str) else "&".join(str(c) for c in r) for r in rows) + r"\end{pmatrix}"


def aug(rows, left=3):
    n = len(rows[0])
    spec = "c" * left + "|" + "c" * (n - left)
    return r"\left(\begin{array}{" + spec + "}" + r"\\".join("&".join(str(c) for c in r) for r in rows) + r"\end{array}\right)"


def arrow(op):
    return r"\xrightarrow{" + op + "}"


def col(*v):
    return pm(*[[c] for c in v])


# ------------------------------------------------------------------ contexts
contexts = {
    "c1": {"kind": "text", "title": "שאלה 1 - שלושה מישורים",
           "text": "נתונים שלושה מישורים:\n"
                   r"$S_1:\ x+y+z=0,\qquad S_2:\ 2x-y+2z=1,\qquad S_3:\ x-y+2z=-1$"},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת משוואות עם פרמטר",
           "text": "נתונה מערכת המשוואות הלינאריות\n"
                   r"$$\begin{cases} x-y+2z=0,\\ -x+ay+(a-3)z=a,\\ (a-1)y+2az=2a+1,\\ x+(a-2)y+(2a+2)z=2a+1.\end{cases}$$" "\n"
                   r"עם פרמטר ממשי $a$."},
    "c3": {"kind": "text", "title": "שאלה 3.א - המטריצה A",
           "text": r"נתונה המטריצה $A=" + pm("1&-1&0", "0&1&1", "5&-5&9") + "$."},
    "c4": {"kind": "text", "title": "שאלה 4 - מטריצות סימטריות",
           "text": r"יהי $V=M_{2\times2}(\mathbb{R})$ מרחב וקטורי של מטריצות ריבועיות מסדר $2\times2$. בו נתונות שתי קבוצות" "\n"
                   r"$$W=\{A\in V:\ A=A^T\},\qquad U=\mathrm{span}\left\{" + pm("1&2", "-1&3") + "," + pm("2&0", "-3&2") + r"\right\}$$"},
    "c5": {"kind": "text", "title": "שאלה 5.א - העתקה ממטריצות ל-R^4",
           "text": r"נתונה העתקה לינארית $T:M_{2\times2}(\mathbb{R})\to\mathbb{R}^4$ המוגדרת על ידי:" "\n"
                   r"$$T\left(" + pm("a&b", "c&d") + r"\right)=" + col("a+b+c+d", "2a+2c+5d", "3a+b+3c+6d", "6a+2b+6c+12d") + "$$"},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "computation", "lines_planes",
    r"מצאו את ישר החיתוך $\ell_1$ של המישורים $S_1$ ו-$S_2$ ואת ישר החיתוך $\ell_2$ של המישורים $S_1$ ו-$S_3$.",
    r"למציאת ישר החיתוך $\ell_1$ נזכור שכל נקודה על $\ell_1$ מקיימת את המשוואה של $S_1$ וגם את המשוואה של $S_2$. על כן נפתור את מערכת המשוואות" "\n"
    "$$" + aug([["1", "1", "1", "0"], ["2", "-1", "2", "1"]]) + arrow("R_2-2R_1\\to R_2")
    + aug([["1", "1", "1", "0"], ["0", "-3", "0", "1"]]) + arrow("3R_1+R_2\\to R_1")
    + aug([["3", "0", "3", "1"], ["0", "-3", "0", "1"]]) + r"\to"
    + aug([["1", "0", "1", r"1/3"], ["0", "1", "0", r"-1/3"]]) + "$$\n"
    r"כאן $z$ הוא משתנה חופשי. נבצע פרמטריזציה $z=t,\ t\in\mathbb{R}$ ונקבל" "\n"
    r"$$x=\frac13-t,\quad y=-\frac13\ \Rightarrow\ \ell_1:\ (x(t),y(t),z(t))=\left(\frac13,-\frac13,0\right)+t(-1,0,1)$$" "\n"
    r"למציאת ישר החיתוך $\ell_2$ נזכור שכל נקודה על $\ell_2$ מקיימת גם את המשוואה של $S_1$ וגם את המשוואה של $S_3$. על כן נפתור את מערכת המשוואות" "\n"
    "$$" + aug([["1", "1", "1", "0"], ["1", "-1", "2", "-1"]]) + arrow("R_2-R_1\\to R_2")
    + aug([["1", "1", "1", "0"], ["0", "-2", "1", "-1"]]) + arrow("2R_1+R_2\\to R_1")
    + aug([["2", "0", "3", "-1"], ["0", "-2", "1", "-1"]]) + r"\to"
    + aug([["1", "0", "3/2", "-1/2"], ["0", "1", "-1/2", "1/2"]]) + "$$\n"
    r"כאן $z$ הוא משתנה חופשי. נבצע פרמטריזציה $z=s,\ s\in\mathbb{R}$ ונקבל" "\n"
    r"$$x=-\frac12-\frac32s,\quad y=\frac12+\frac12s\ \Rightarrow\ \ell_2:\ (x(s),y(s),z(s))=\left(-\frac12,\frac12,0\right)+\frac12s(-3,1,2)$$",
    9, contextId="c1"))

questions.append(Q(
    1, "ב", "computation", "lines_planes",
    r"מצאו משוואת מישור $S_4$ המכיל את $\ell_1$ ומאונך למישור $S_1$ ומשוואת מישור $S_5$ המכיל את $\ell_2$ ומאונך למישור $S_1$.",
    r"ממשוואת המישור $S_1$ נקבל שהוקטור הנורמלי ל-$S_1$ הוא $\vec N_1=(1,1,1)$. בנוסף, וקטורי הכיוון של $\ell_1$ ו-$\ell_2$ הם, בהתאמה, $\vec L_1=(-1,0,1)$ ו-$\vec L_2=(-3,1,2)$. לכן וקטור נורמלי למישור $S_4$ מתקבל ע״י מכפלה וקטורית" "\n"
    r"$$\vec N_4=\vec N_1\times\vec L_1=\begin{vmatrix}\hat\imath&\hat\jmath&\hat k\\1&1&1\\-1&0&1\end{vmatrix}=\hat\imath-2\hat\jmath+\hat k=(1,-2,1)$$" "\n"
    r"כיוון ש-$\ell_1$ מוכל ב-$S_4$ הנקודה $p_1\left(\frac13,-\frac13,0\right)$ נמצאת על $S_4$. מכאן נוכל למצוא את משוואת המישור $S_4$:" "\n"
    r"$$S_4:\ \left(x-\frac13,\,y+\frac13,\,z-0\right)\cdot(1,-2,1)=0\ \Rightarrow\ x-2y+z=1$$" "\n"
    r"באופן דומה, וקטור נורמלי למישור $S_5$ מתקבל ע״י המכפלה הוקטורית" "\n"
    r"$$\vec N_5=\vec N_1\times\vec L_2=\begin{vmatrix}\hat\imath&\hat\jmath&\hat k\\1&1&1\\-3&1&2\end{vmatrix}=\hat\imath-5\hat\jmath+4\hat k=(1,-5,4)$$" "\n"
    r"כיוון ש-$\ell_2$ מוכל ב-$S_5$ הנקודה $p_2\left(-\frac12,\frac12,0\right)$ נמצאת על $S_5$. מכאן נוכל למצוא את משוואת המישור $S_5$:" "\n"
    r"$$S_5:\ \left(x+\frac12,\,y-\frac12,\,z-0\right)\cdot(1,-5,4)=0\ \Rightarrow\ x-5y+4z=-3$$" "\n"
    "נסכם:\n"
    r"$$S_4:\ x-2y+z=1,\qquad S_5:\ x-5y+4z=-3$$",
    8, contextId="c1"))

questions.append(Q(
    1, "ג", "computation", "lines_planes",
    r"מצאו את נקודת החיתוך בין הישרים $\ell_1$ ו-$\ell_2$ ואת ישר החיתוך בין $S_4$ ו-$S_5$.",
    r"למציאת נקודת החיתוך $p_0$ בין $\ell_1$ ו-$\ell_2$ נפתור את המשוואה" "\n"
    r"$$\left(\frac13,-\frac13,0\right)+t(-1,0,1)=\left(-\frac12,\frac12,0\right)+s(-3,1,2)$$" "\n"
    r"ממשוואה זו נקבל שלוש משוואות על הרכיבים" "\n"
    r"$$(I)\ \frac13-t=-\frac12-3s,\qquad(II)\ -\frac13=\frac12+s,\qquad(III)\ t=2s$$" "\n"
    r"ממשוואה $(II)$ נקבל ש-$s=-\frac56$ וניתן לבדוק ע״י שימוש בשתי המשוואות הנוספות שלא מתקבלת סתירה והמערכת ניתנת לפתרון. נציב את הערך של $s$ שקיבלנו בביטוי עבור $\ell_2$ ונקבל" "\n"
    r"$$p_0=\left(x\left(-\frac56\right),y\left(-\frac56\right),z\left(-\frac56\right)\right)=\left(-\frac12,\frac12,0\right)+\left(-\frac56\right)(-3,1,2)=\frac16(-3,3,0)+\frac16(15,-5,-10)=\left(2,-\frac13,-\frac53\right)$$" "\n"
    r"(הערת תמלול: בסעיף א׳ הפתרון הרשמי כותב את $\ell_2$ עם הכיוון $\frac12s(-3,1,2)$, ואילו כאן הוא פותר עם הכיוון $s(-3,1,2)$; הנקודה המתקבלת נכונה.)" "\n"
    r"בנוסף, כיוון ש-$S_5$ ו-$S_4$ שניהם מאונכים ל-$S_1$, וקטור הכיוון בכיוון ישר החיתוך שלהם הוא $\vec N_1$. אם נסמן את ישר החיתוך של $S_5$ ו-$S_4$ ב-$\ell_3$ נקבל ש" "\n"
    r"$$\ell_3:\ (x(t),y(t),z(t))=\left(2,-\frac13,-\frac53\right)+t(1,1,1)$$",
    8, contextId="c1"))

# ------------------------------------------------------------------ Q2
questions.append(Q(
    2, "א", "computation", "linear_systems",
    "הביאו את המטריצה המורחבת המתאימה למערכת לצורתה המדורגת.",
    "$$" + aug([["1", "-1", "2", "0"], ["-1", "a", "a-3", "a"], ["0", "a-1", "2a", "2a+1"], ["1", "a-2", "2a+2", "2a+1"]])
    + arrow(r"\substack{R_2+R_1\to R_2\\R_4-R_1\to R_4}")
    + aug([["1", "-1", "2", "0"], ["0", "a-1", "a-1", "a"], ["0", "a-1", "2a", "2a+1"], ["0", "a-1", "2a", "2a+1"]]) + "$$\n"
    "$$" + arrow(r"R_4-R_3\to R_4")
    + aug([["1", "-1", "2", "0"], ["0", "a-1", "a-1", "a"], ["0", "a-1", "2a", "2a+1"], ["0", "0", "0", "0"]])
    + arrow(r"R_3-R_2\to R_3")
    + aug([["1", "-1", "2", "0"], ["0", "a-1", "a-1", "a"], ["0", "0", "a+1", "a+1"], ["0", "0", "0", "0"]]) + "$$",
    8, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור אילו ערכים של $a$ יש פתרון יחיד למערכת? עבור אילו ערכים של $a$ אין פתרון למערכת? עבור אילו ערכים של $a$ יש למערכת אינסוף פתרונות?",
    r"אם $a\neq\pm1$ יש למערכת **פתרון אחד ויחיד**," "\n"
    r"אם $a=1$ יש שורת סתירה (שורה שניה) ואז **אין פתרון** למערכת," "\n"
    r"אם $a=-1$ יש למערכת **אינסוף פתרונות**.",
    9, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"מצאו פתרונות המערכת עבור $a=-1$.",
    r"אם $a=-1$ המערכת שקולה ל-" "\n"
    r"$$\begin{cases}x-y+2z=0\\-2y-2z=-1\end{cases}$$" "\n"
    r"$$z=t,\quad y=\frac12-t,\quad x=\frac12-3t$$" "\n"
    "$$" + col("x", "y", "z") + "=" + col("0.5", "0.5", 0) + "+t" + col(-3, -1, 1) + "$$",
    3, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"פתרו את המשוואה $\left(\bar z+\dfrac{7-i}{3+i}\right)^3=8i$.",
    r"$$\frac{7-i}{3+i}=\frac{(7-i)(3-i)}{10}=2-i$$" "\n"
    r"נסמן $w=\bar z+\dfrac{7-i}{3+i}=\bar z+2-i$, לכן $z=\overline{w}-2-i$." "\n"
    r"$$w^3=8i,\qquad 8i=8\left(\cos\frac\pi2+i\sin\frac\pi2\right)$$" "\n"
    r"$$w_k=\sqrt[3]{8i}=2\left(\cos\frac{\frac\pi2+2\pi k}{3}+i\sin\frac{\frac\pi2+2\pi k}{3}\right)$$" "\n"
    r"$$w_0=2\left(\cos\frac\pi6+i\sin\frac\pi6\right)=\sqrt3+i$$" "\n"
    r"$$w_1=2\left(\cos\frac{5\pi}6+i\sin\frac{5\pi}6\right)=-\sqrt3+i$$" "\n"
    r"$$w_2=2\left(\cos\frac{9\pi}6+i\sin\frac{9\pi}6\right)=-2i$$" "\n"
    r"$$z_0=-2+\sqrt3-2i$$" "\n"
    r"$$z_1=-2-\sqrt3-2i$$" "\n"
    r"$$z_2=-2+i$$" "\n"
    r"(הערת תמלול: בפתרון הרשמי הפתרון השלישי מסומן $z_3$; זהו הפתרון השלישי, $z_2$.)",
    5))

# ------------------------------------------------------------------ Q3
questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הוכיחו ש-$A$ הפיכה ע״י מציאת המטריצה $A^{-1}$.",
    "נחשב את $A^{-1}$:\n"
    "$$" + aug([["1", "-1", "0", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["5", "-5", "9", "0", "0", "1"]]) + arrow("R_3\\to R_3-5R_1")
    + aug([["1", "-1", "0", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "9", "-5", "0", "1"]]) + arrow(r"R_3\to\frac19R_3")
    + aug([["1", "-1", "0", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "1", r"-\frac59", "0", r"\frac19"]]) + "$$\n"
    "$$" + arrow("R_2\\to R_2-R_3")
    + aug([["1", "-1", "0", "1", "0", "0"], ["0", "1", "0", r"\frac59", "1", r"-\frac19"], ["0", "0", "1", r"-\frac59", "0", r"\frac19"]])
    + arrow("R_1\\to R_1+R_2")
    + aug([["1", "0", "0", r"\frac{14}9", "1", r"-\frac19"], ["0", "1", "0", r"\frac59", "1", r"-\frac19"], ["0", "0", "1", r"-\frac59", "0", r"\frac19"]]) + "$$\n"
    "קיבלנו שהמטריצה ההופכית היא:\n"
    "$$A^{-1}=" + pm(r"\frac{14}9&1&-\frac19", r"\frac59&1&-\frac19", r"-\frac59&0&\frac19") + "$$",
    6, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"הציגו את $A^{-1}$ בצורת כפל של מטריצות אלמנטריות.",
    r"כעת נשתמש בדירוג הנ״ל ונכתוב את $A^{-1}$ כמכפלה של מטריצות אלמנטריות:" "\n"
    "$$A^{-1}=" + pm("1&1&0", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&-1", "0&0&1") + pm("1&0&0", "0&1&0", r"0&0&\frac19")
    + pm("1&0&0", "0&1&0", "-5&0&1") + "$$",
    7, contextId="c3"))

questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + pm("7&0&1", "0&6&0", "1&0&7") + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $PD=BP$. הראו שהשוויון באמת מתקיים.",
    r"תחילה נמצא את כל הערכים העצמיים. נחשב את הדטרמיננטה הבאה לפי שורה שניה (בפתרון הרשמי המטריצה מסומנת $A$ במקום $B$):" "\n"
    r"$$|\lambda I-B|=\begin{vmatrix}\lambda-7&0&-1\\0&\lambda-6&0\\-1&0&\lambda-7\end{vmatrix}=(\lambda-6)\begin{vmatrix}\lambda-7&-1\\-1&\lambda-7\end{vmatrix}=(\lambda-6)\left[(\lambda-7)^2-1\right]=(\lambda-6)\left(\lambda^2-14\lambda+48\right)=(\lambda-6)(\lambda-6)(\lambda-8)$$" "\n"
    r"קיבלנו שהערכים העצמיים הם: $6,6,8$. כעת נמצא את הוקטורים העצמיים." "\n"
    r"עבור ע״ע $6$:" "\n"
    "$$" + pm("-1&0&-1", "0&0&0", "-1&0&-1") + r"\to\cdots\to" + pm("1&0&1", "0&0&0", "0&0&0") + "$$\n"
    r"נסמן $y=t,\ z=s$ ונקבל $x=-s$. הוקטורים העצמיים המתקבלים הם: $" + col(-1, 0, 1) + "," + col(0, 1, 0) + "$.\n"
    r"עבור ע״ע $8$:" "\n"
    "$$" + pm("1&0&-1", "0&2&0", "-1&0&1") + r"\to\cdots\to" + pm("1&0&-1", "0&2&0", "0&0&0") + "$$\n"
    r"נסמן $z=t$ ונקבל $x=t,\ y=0$. הוקטור העצמי המתקבל הוא: $" + col(1, 0, 1) + "$.\n"
    r"כעת נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $PD=BP$:" "\n"
    r"$$D=" + pm("6&0&0", "0&6&0", "0&0&8") + r",\qquad P=" + pm("-1&0&1", "0&1&0", "1&0&1") + "$$\n"
    r"נבדוק שמתקיים $PD=BP$:" "\n"
    r"$$PD=" + pm("-1&0&1", "0&1&0", "1&0&1") + pm("6&0&0", "0&6&0", "0&0&8") + "=" + pm("-6&0&8", "0&6&0", "6&0&8") + "$$\n"
    r"$$BP=" + pm("7&0&1", "0&6&0", "1&0&7") + pm("-1&0&1", "0&1&0", "1&0&1") + "=" + pm("-6&0&8", "0&6&0", "6&0&8") + "$$\n"
    "ואכן מתקיים השוויון.",
    12))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "proof", "vector_spaces",
    r"הוכיחו כי $W$ מהווה תת מרחב של $V$.",
    r"נתבונן בקבוצה $W=\{A\in V:\ A=A^T\}$." "\n"
    r"$$W=\left\{" + pm("a&b", "b&c") + r":\ a,b,c\in\mathbb{R}\right\}=\mathrm{Span}\left\{" + pm("1&0", "0&0") + "," + pm("0&1", "1&0") + "," + pm("0&0", "0&1") + r"\right\}$$" "\n"
    "לפי המשפט שהוכח בכיתה כל פרישה לינארית היא תת מרחב.",
    5, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"מצאו בסיס ומימד ל-$W$.",
    r"הקבוצה היא בת״ל לכן מהווה בסיס:" "\n"
    r"$$\alpha_1" + col(1, 0, 0, 0) + r"+\alpha_2" + col(0, 1, 1, 0) + r"+\alpha_3" + col(0, 0, 0, 1) + "=" + col(0, 0, 0, 0) + "$$\n"
    "$$" + pm("1&0&0", "0&1&0", "0&1&0", "0&0&1") + arrow(r"-R_2+R_3\to R_3") + pm("1&0&0", "0&1&0", "0&0&0", "0&0&1") + arrow(r"R_3\leftrightarrow R_4")
    + pm("1&0&0", "0&1&0", "0&0&1", "0&0&0") + "$$\n"
    r"לכן שלושת הווקטורים בלתי תלויים לינארית, הם בסיס של $W$ ו-$\dim W=3$.",
    5, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצאו בסיסים ואת ממדים לתתי מרחב $U+W$ ו-$U\cap W$.",
    r"**$U+W$:**" "\n"
    r"$$U+W=\mathrm{Span}\left\{" + pm("1&0", "0&0") + "," + pm("0&1", "1&0") + "," + pm("0&0", "0&1") + "," + pm("1&2", "-1&3") + "," + pm("2&0", "-3&2") + r"\right\}$$" "\n"
    "$$" + pm("1&0&0&1&2", "0&1&0&2&0", "0&1&0&-1&-3", "0&0&1&3&2") + r"\longrightarrow\cdots\longrightarrow" + pm("1&0&0&1&2", "0&1&0&2&0", "0&0&1&3&2", "0&0&0&1&1") + "$$\n"
    r"בסיס של $U+W$ הוא" "\n"
    r"$$B=\left\{" + pm("1&0", "0&0") + "," + pm("0&1", "1&0") + "," + pm("0&0", "0&1") + "," + pm("1&2", "-1&3") + r"\right\},\qquad\dim(U+W)=4$$" "\n"
    r"**$U\cap W$:**" "\n"
    r"$v\in U\cap W\Rightarrow v=c_1" + col(1, 0, 0, 0) + "+c_2" + col(0, 1, 1, 0) + "+c_3" + col(0, 0, 0, 1) + "=d_1" + col(1, 2, -1, 3) + "+d_2" + col(2, 0, -3, 2) + "$\n"
    r"$$c_1" + col(1, 0, 0, 0) + "+c_2" + col(0, 1, 1, 0) + "+c_3" + col(0, 0, 0, 1) + "+d_1" + col(-1, -2, 1, -3) + "+d_2" + col(-2, 0, 3, -2) + "=" + col(0, 0, 0, 0) + "$$\n"
    "$$" + pm("1&0&0&-1&-2", "0&1&0&-2&0", "0&1&0&1&3", "0&0&1&-3&-2") + r"\longrightarrow\cdots\longrightarrow" + pm("1&0&0&-1&-2", "0&1&0&-2&0", "0&0&1&-3&-2", "0&0&0&1&1") + "$$\n"
    r"נקבל $d_2=1\Rightarrow d_1=-1\Rightarrow$" "\n"
    r"$$v=d_1" + col(1, 2, -1, 3) + "+d_2" + col(2, 0, -3, 2) + "=" + col(1, 2, -1, 3) + "-" + col(2, 0, -3, 2) + "=" + col(-1, 2, 2, 1) + "$$\n"
    r"ולכן $B=\left\{" + pm("-1&2", "2&1") + r"\right\}$ הוא בסיס של $U\cap W$, $\dim(U\cap W)=1$." "\n"
    r"(הערת תמלול: עם $d_1=-1,\ d_2=1$ מתקבל $-(1,2,-1,3)+(2,0,-3,2)=(1,-2,-2,-1)$, כלומר הנגדי של הוקטור שנכתב בפתרון הרשמי; הישר הנפרש והבסיס נכונים, והחישוב ה״מפורש״ בפתרון הרשמי מתאים ל-$d_1=1,\ d_2=-1$.)",
    10, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם הוקטור $" + pm("1&0", "-1&1") + r"$ שייך לתת מרחב $U\cap W$?",
    r"הוקטור $" + pm("1&0", "-1&1") + r"$ אינו שייך לתת מרחב $U\cap W$ כי היא בת״ל מוקטור $" + pm("-1&2", "2&1") + r"$.",
    5, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את הממד והבסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    r"נגדיר $F=\left(E_1=" + pm("1&0", "0&0") + ",E_2=" + pm("0&1", "0&0") + ",E_3=" + pm("0&0", "1&0") + ",E_4=" + pm("0&0", "0&1")
    + r"\right)$ בסיס סטנדרטי של $M_{2\times2}(\mathbb{R})$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^4$. אז נקבל ש-" "\n"
    r"$$T(E_1)=" + col(1, 2, 3, 6) + ",\\ T(E_2)=" + col(1, 0, 1, 2) + ",\\ T(E_3)=" + col(1, 2, 3, 6) + ",\\ T(E_4)=" + col(1, 5, 6, 12) + "$$\n"
    r"מכאן נובע שהמטריצה המייצגת הסטנדרטית היא $A=[T]_E^F=" + pm("1&1&1&1", "2&0&2&5", "3&1&3&6", "6&2&6&12") + "$ ואחרי הדירוג\n"
    "$$" + aug([["1", "1", "1", "1", "0"], ["2", "0", "2", "5", "0"], ["3", "1", "3", "6", "0"], ["6", "2", "6", "12", "0"]], 4) + r"\to"
    + aug([["1", "1", "1", "1", "0"], ["0", "-2", "0", "3", "0"], ["0", "-2", "0", "3", "0"], ["0", "-4", "0", "6", "0"]], 4) + r"\to"
    + aug([["1", "1", "1", "1", "0"], ["0", "-2", "0", "3", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$\n"
    r"עמודות מס׳ 1,2 של המטריצה המדורגת מובילות, אז $\mathrm{Col}A$ הוא בסיס של $\mathrm{Im}\,T$ ואז $\mathrm{Im}\,T=\mathrm{span}\left\{" + col(1, 2, 3, 6) + "," + col(1, 0, 1, 2) + r"\right\}$ ו-$\dim\mathrm{Im}\,T=2$. בנוסף לזאת," "\n"
    "$$" + aug([["1", "1", "1", "1", "0"], ["0", "1", "0", "-1.5", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + r"\to"
    + aug([["1", "0", "1", "2.5", "0"], ["0", "1", "0", "-1.5", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4)
    + r"\Rightarrow\begin{cases}x_1=-t-2.5s\\x_2=1.5s\\x_3=t\\x_4=s\end{cases}\Rightarrow" + col("x_1", "x_2", "x_3", "x_4") + "=t" + col(-1, 0, 1, 0) + "+s" + col("-2.5", "1.5", 0, 1) + "$$\n"
    r"אז $\mathrm{Nul}A$ הוא בסיס של $\left(" + col(-1, 0, 1, 0) + "," + col("-2.5", "1.5", 0, 1) + r"\right)$ ו-$\mathrm{Ker}\,T$ הוא בסיס של "
    r"$\left(" + pm("-1&0", "1&0") + "," + pm("-2.5&1.5", "0&1") + r"\right)$ ואז $\dim\mathrm{Ker}\,T=2$.",
    12, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חד-חד ערכית? האם $T$ על? נמקו.",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=2\neq0$, $T$ לא על כי $\dim\mathrm{Im}\,T=2\neq\dim\mathbb{R}^4$.",
    3, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטר $m$ מתקיים $" + col(11, 2, 13, "m") + r"\in\mathrm{Im}\,T$?",
    "$$" + aug([["1", "1", "11"], ["2", "0", "2"], ["3", "1", "13"], ["6", "2", "m"]], 2) + r"\to"
    + aug([["1", "1", "11"], ["0", "-2", "-20"], ["0", "-2", "-20"], ["0", "-4", "m-66"]], 2) + r"\to"
    + aug([["1", "1", "11"], ["0", "-2", "-20"], ["0", "0", "0"], ["0", "0", "m-26"]], 2) + r"$$" "\n"
    r"ולכן $m=26$.",
    4, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "vector_spaces",
    r"נתונים בסיסים $B=(1+3x,\ 2+4x)$, $C=(1+4x,\ 3+8x)$ של מרחב פולינומים $\mathbb{R}_1[x]$. מצאו את $[p(x)]_C$ אם $[p(x)]_B=" + col(20, 25) + r"$, כאשר $p(x)\in\mathbb{R}_1[x]$.",
    r"נגדיר בסיס סטנדרטי של $\mathbb{R}_1[x]$ $A=(1,x)$. אז" "\n"
    r"$$B=(1+3x,2+4x),\quad C=(1+4x,3+8x)$$" "\n"
    r"$$[I]_A^B=" + pm("1&2", "3&4") + r",\qquad[I]_A^C=" + pm("1&3", "4&8") + "$$\n"
    r"$$[I]_C^B=[I]_C^A[I]_A^B=\left([I]_A^C\right)^{-1}[I]_A^B=" + pm("1&3", "4&8") + r"^{-1}" + pm("1&2", "3&4") + "="
    + r"-\frac14" + pm("8&-3", "-4&1") + pm("1&2", "3&4") + "=-\\frac14" + pm("-1&4", "-1&-4") + "=" + pm("0.25&-1", "0.25&1") + "$$\n"
    r"$$[p(x)]_C=[I]_C^B[p(x)]_B=-\frac14" + pm("-1&4", "-1&-4") + col(20, 25) + r"=-\frac14" + col(80, -120) + "=" + col(-20, 30) + "$$",
    6))

# ------------------------------------------------------------------ Q6 (no official solution: held)
for part, qtext, pts in [
    ("א", r"נניח ש-$H$ ו-$D$ מטריצות הפיכות המקיימות $HD^2=D^3H^{-1}$. הוכיחו ש-$\det(D)>0$.", 9),
    ("ב", r"הוכיחו שאם $\lambda$ הוא ערך עצמי של מטריצה הפיכה $A$ ו-$\vec u$ הוא וקטור עצמי שמתאים ל-$\lambda$, אז $1/\lambda$ יהיה ערך עצמי של $A^{-1}$ עם אותו הווקטור העצמי $\vec u$.", 9),
    ("ג", r"נתונות שתי מטריצות הפיכות $B,C$ באותו הגודל. אילו מהמטריצות הבאות **תמיד** יהיו הפיכות? נמקו!!!" "\n"
          r"1) $BC$" "\n" r"2) $B+C$" "\n" r"3) $\alpha C$ כאשר $\alpha\in\mathbb{R}$.", 7),
]:
    questions.append({"num": 6, "part": part, "kind": "proof", "topic": "matrix_proofs", "points": pts,
                      "question": qtext, "hold": "no-key"})

exam = {
    "examCode": "25B-A",
    "examLabel": "מבחן סוף סמסטר ב׳ תשפ״ה, מועד א׳ (07.07.2025)",
    "year": 2025,
    "examDate": "07.07.2025",
    "sourceFile": "25B-A exam (phone photo)",
    "solutionFile": "25B-A official solution (typed, solution-only PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
