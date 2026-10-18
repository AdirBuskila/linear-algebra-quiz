# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-A.json -- linear algebra, semester B 2020, moed A (18.06.2020), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20B-A.py

Source: one scanned PDF (11pp): the exam text with the official solution typed under each question (pages 1-8, solution
inserted question by question); pages 9-11 repeat Q6 and give its solution (page 11 also has a struck-out part "ה" that is not
part of the exam; not transcribed). Six questions of 25 points (best 4 count), 23 items. No figures.

Transcription notes
- Q1 prints item 1 (two lines, parts 1,2 = 6+7 pts), then parts b (6) and c (6). In the raw schema: a = 1.1, b = 1.2, g = old b,
  d = old c (the z^3 equation).
- Q4 prints item 1 (A with a; parts 1,2 = 5+5) and item 2 (B; parts 1,2 = 9+6): a, b, g, d in the raw schema.
- Q1 d (z^3+(3i-4)z=0): the solution file has NO solution for it (it jumps from Q1 b to Q2). Was held "no-key"; now solved
  (solutionSource "solved", official false, checks in tools/verify/20B-A/solve_Q1d.py).
- Q1 a 1 (final-answer error): the official takes M1M2 = (-1,3,-2); M2-M1 = (0-1,3-2,-2-0) = (-1,1,-2). With the printed vector its own
  determinant is 3k+9 (not the printed 3k+12), and k=-4 is wrong: the lines meet for k=-1 only. Shipped corrected, labeled, official:false.
- Q1 a 2 (final-answer error): same vector slip (and the printed triple product 18); the distance is 9/(3*sqrt2) = 3*sqrt2/2, not
  3*sqrt2. Shipped corrected, labeled, official:false.
- Q2 c (final-answer error): the official second row of the k=-1 matrix is (0 1 1 | -1) and it states x=-2z, y=-1-z. Row 2 of its own
  echelon form is (0 2 2k | k-1) = (0 2 -2 | -2), i.e. y-z=-1; the solution set is (0,-1,0)+t(0,1,1). Shipped corrected, labeled,
  official:false.
- Q2 a (slip in an intermediate line, no label): the step is labeled R3+kR1 but the printed row (0 -2 -2k | 1-k) is R3-kR1. Written R3-kR1.
- Q2 b (slip in an intermediate line, no label): the official writes "k!=1 או k!=-1" for the unique case; the sense is "וגם". Written so.
- Q6 b (notation, no label): the official writes "T: V->V"; the codomain is R^3. Written T: V->W with the same dimension argument.

Checks (sympy, tools/verify/20B-A/verify_20B-A.py): Q1 coplanarity and the k=-1 intersection, distance (also by minimisation), Q1 b
counterexample, Q2 echelon rows and classification, the true k=-1 solution set, Q3 rref/null/row/column spaces, Q4 det, inverse at
a=0, eigenvalues, P and D, Q5 intersection and dimensions, Q6 kernel, rank and preimage of (1,1,1). Mismatches found: the Q1 a 1,
Q1 a 2 and Q2 c slips above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-A.json"


def J(*lines):
    return "\n".join(lines)


def Q(num, part, kind, topic, question, solution, points, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question,
         "solution": solution, "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part is None:
        del q["part"]
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


FIX = r"**הפתרון הרשמי עם תיקון:** "

contexts = {
    "c1": {"kind": "text", "title": "שאלה 1 - שני ישרים",
           "text": J(r"נתונים שני ישרים $l_1$ ו-$l_2$ כאשר $k\in\mathbb{R}$ הוא פרמטר ממשי:",
                     r"$$l_1:\ \frac{x-1}{1}=\frac{y-2}{k}=\frac{z}{2},\qquad l_2:\ \frac{x}{2}=\frac{y-3}{1}=\frac{z+2}{1}$$")},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": J(r"נתונה מערכת של משוואות לינאריות, כאשר $k\in\mathbb{R}$ הוא פרמטר ממשי:",
                     r"$$\begin{cases} x-y+z=1\\ (k-1)x+(k+1)y+(k+1)z=k+1\\ kx-(2+k)y-kz=1\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - המטריצה A",
           "text": r"נתונה מטריצה $A=" + pm("1&0&1&1", "1&1&2&0", "0&1&1&-1") + r"$."},
    "c4a": {"kind": "text", "title": "שאלה 4 - סעיף א",
            "text": r"תהי נתונה המטריצה $A=" + pm("2a&4&4+2a", "a&3&5", "1&1&a") + r"$ כאשר $a$ הוא פרמטר ממשי."},
    "c4b": {"kind": "text", "title": "שאלה 4 - סעיף ב",
            "text": r"תהי נתונה מטריצה $B=" + pm("3&1&0", "0&2&0", "1&1&4") + r"$."},
    "c5": {"kind": "text", "title": "שאלה 5 - תתי הקבוצות W ו-U",
           "text": J(r"יהי $V=M_{2\times2}$ מרחב המטריצות בגודל $2\times2$ ויהיו $U,W$ תתי קבוצות כך ש-$U,W\subseteq V$.",
                     r"$$W=\left\{" + pm("a&2a", "b&c") + r"\ \middle|\ a,b,c\in\mathbb{R},\ a+b=0\right\},\qquad U=\mathrm{sp}\left\{" + pm("-1&2", "1&-3") + "," + pm("1&0", "-1&2") + r"\right\}$$")},
    "c6": {"kind": "text", "title": "שאלה 6 - ההעתקה T",
           "text": J(r"תהי $T$ העתקה לינארית $T:M_{2\times2}\to\mathbb{R}^3$ הנתונה על ידי:",
                     r"$$T" + pm("a&b", "c&d") + "=" + pm("a+b", "b+c", "b+d") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "computation", "lines_planes",
    r"מצא את ערכו של הפרמטר $k$ שעבורו הישרים יהיו נחתכים.",
    J(FIX + r"בפתרון הרשמי נרשם $\overrightarrow{M_1M_2}=(-1,3,-2)$ ומתקבל $k=-4$. אך $\overrightarrow{M_1M_2}=M_2-M_1=(0-1,\ 3-2,\ -2-0)=(-1,1,-2)$, והערך הנכון הוא $k=-1$ (עבור $k=-4$ הישרים אינם נחתכים).",
      r"$M_1(1,2,0)\in l_1$ וקטור כיוון של הישר $l_1$ הוא $\vec a_1=(1,k,2)$.",
      r"$M_2(0,3,-2)\in l_2$ וקטור כיוון של הישר $l_2$ הוא $\vec a_2=(2,1,1)$.",
      r"$\vec a_1,\vec a_2$ לא מקבילים כי $\frac{1}{2}=\frac{k}{1}=\frac{2}{1}$ לא מתקיים לכל $k$. אז מספיק להוכיח ש-$\vec a_1,\vec a_2,\overrightarrow{M_1M_2}$ קומפלנרים.",
      r"$$\overrightarrow{M_1M_2}=(-1,1,-2)$$",
      r"$$0=\begin{vmatrix}-1&1&-2\\1&k&2\\2&1&1\end{vmatrix}=-1\cdot(k-2)-1\cdot(1-4)-2\cdot(1-2k)=-k+2+3-2+4k=3k+3\Rightarrow k=-1$$"),
    6, contextId="c1", solutionSource="solved", official=False))

questions.append(Q(
    1, "ב", "computation", "lines_planes",
    r"עבור $k=2$ מצא את המרחק בין הישרים הנתונים.",
    J(FIX + r"בפתרון הרשמי נעשה שימוש בווקטור $(-1,3,-2)$ ומתקבלים $18$ ו-$d=3\sqrt2$. עם הווקטור הנכון $\overrightarrow{M_1M_2}=(-1,1,-2)$ מתקבל $d=\frac{3\sqrt2}{2}$.",
      r"$$d=\frac{\left|\left(\vec a_1\times\vec a_2\right)\cdot\overrightarrow{M_1M_2}\right|}{\left\|\vec a_1\times\vec a_2\right\|}$$",
      r"$$\left(\vec a_1\times\vec a_2\right)\cdot\overrightarrow{M_1M_2}=\begin{vmatrix}-1&1&-2\\1&2&2\\2&1&1\end{vmatrix}=3+6=9$$",
      r"$$\vec a_1\times\vec a_2=\left(\begin{vmatrix}2&2\\1&1\end{vmatrix},\ -\begin{vmatrix}1&2\\2&1\end{vmatrix},\ \begin{vmatrix}1&2\\2&1\end{vmatrix}\right)=(0,3,-3)$$",
      r"$$\left\|\vec a_1\times\vec a_2\right\|=\sqrt{0^2+3^2+(-3)^2}=3\sqrt2$$",
      r"$$d=\frac{9}{3\sqrt2}=\frac{3}{\sqrt2}=\frac{3\sqrt2}{2}$$"),
    7, contextId="c1", solutionSource="solved", official=False))

questions.append(Q(
    1, "ג", "proof", "vectors_geometry",
    r"הוכח או הפרך עם דוגמה נגדית: אם $\vec a\times\vec b=\vec a\times\vec c\neq\vec 0$ אז $\vec b=\vec c$.",
    J(r"הטענה אינה נכונה. $\vec a\times\left(\vec b-\vec c\right)=\vec 0$ אינו מחייב $\vec b=\vec c$.",
      r"דוגמה נגדית:",
      r"$$\vec a=(1,0,0),\ \vec b=(1,1,0),\ \vec c=(0,1,0)$$",
      r"$$\vec a\times\vec b=(0,0,1)\neq\vec 0,\qquad\vec a\times\vec c=(0,0,1)\neq\vec 0,\qquad\vec b\neq\vec c$$"),
    6))

questions.append(Q(
    1, "ד", "computation", "complex_numbers",
    r"פתור את המשוואה מעל מספרים מרוכבים $z^3+(3i-4)z=0$.",
    J(r"**אין פתרון רשמי לסעיף זה; הפתרון נכתב בעזרת AI ונבדק בסימבולית (sympy).**",
      r"נוציא את $z$ כגורם משותף:",
      r"$$z\left(z^2+3i-4\right)=0$$",
      r"כלומר $z=0$ או $z^2=4-3i$.",
      r"נחשב שורש ריבועי של $4-3i$: נניח $(a+ib)^2=4-3i$ עם $a,b$ ממשיים, ולכן",
      r"$$a^2-b^2=4,\qquad 2ab=-3$$",
      r"המודול של $4-3i$ הוא $5$, ולכן גם $a^2+b^2=5$. מכאן $a^2=\frac92$ ו-$b^2=\frac12$, ומהמשוואה $2ab=-3$ ל-$a,b$ סימנים הפוכים:",
      r"$$a=\frac{3}{\sqrt2},\ b=-\frac{1}{\sqrt2}$$",
      r"או",
      r"$$a=-\frac{3}{\sqrt2},\ b=\frac{1}{\sqrt2}$$",
      r"הפתרונות:",
      r"$$z=0,\qquad z=\pm\frac{3-i}{\sqrt2}=\pm\left(\frac{3\sqrt2}{2}-\frac{\sqrt2}{2}i\right)$$"),
    6, solutionSource="solved", official=False))

# ------------------------------------------------------------------ Q2
S0 = [["1", "-1", "1", "1"], ["k-1", "k+1", "k+1", "k+1"], ["k", "-2-k", "-k", "1"]]
S1 = [["1", "-1", "1", "1"], ["0", "2k", "2", "2"], ["0", "-2", "-2k", "1-k"]]
S2 = [["1", "-1", "1", "1"], ["0", "2", "2k", "k-1"], ["0", "2k", "2", "2"]]
S3 = [["1", "-1", "1", "1"], ["0", "2", "2k", "k-1"], ["0", "0", "2-2k^2", "2+k-k^2"]]
questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"רשום את מערכת כמטריצה מורחבת, הבא אותה לצורה מדורגת.",
    J("$$" + aug(S0) + arrow(r"\substack{R_2-(k-1)R_1\to R_2\\R_3-kR_1\to R_3}") + aug(S1) + arrow(r"R_2\leftrightarrow-R_3") + aug(S2) + "$$",
      "$$" + arrow(r"R_3-kR_2\to R_3") + aug(S3) + "$$"),
    8, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"מצא עבור אילו ערכי $k$ יש למערכת אינסוף פתרונות, פתרון יחיד או אין לה פתרונות כלל.",
    J(r"אם $k=1$ למערכת אין פתרון כי בשורה השלישית נקבל שורת סתירה.",
      "$$" + aug([["1", "-1", "1", "1"], ["0", "2", "2", "0"], ["0", "0", "0", "2"]]) + "$$",
      r"אם $k\neq1$ וגם $k\neq-1$ למערכת יש פתרון יחיד.",
      r"אם $k=-1$ השורה השלישית היא $(0\ 0\ 0\mid0)$ ולמערכת יש אינסוף פתרונות (ראו סעיף ג׳)."),
    9, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור $k=-1$ מצא את הפתרונות של המערכת.",
    J(FIX + r"בפתרון הרשמי נרשמה השורה השנייה $(0\ 1\ 1\mid-1)$ ונקבע $x=-2z$, $y=-1-z$. אך השורה השנייה במטריצה המדורגת היא $(0\ \ 2\ \ 2k\mid k-1)$, ועבור $k=-1$ היא $(0\ 2\ -2\mid-2)$, כלומר $y-z=-1$. (גם ישירות: השורה השנייה של המערכת המקורית היא $-2x=0$.)",
      r"אם $k=-1$ למערכת יש אינסוף פתרונות, נקבל",
      "$$" + aug([["1", "-1", "1", "1"], ["0", "2", "-2", "-2"], ["0", "0", "0", "0"]]) + r"\to" + aug([["1", "-1", "1", "1"], ["0", "1", "-1", "-1"], ["0", "0", "0", "0"]])
      + r"\Rightarrow\begin{cases}x=0\\y=-1+z\\z=z\in\mathbb{R}\end{cases}$$",
      r"$$" + pm("x", "y", "z") + "=" + pm("0", "-1", "0") + "+z" + pm("0", "1", "1") + "$$"),
    8, contextId="c2", solutionSource="solved", official=False))

# ------------------------------------------------------------------ Q3
questions.append(Q(
    3, "א", "computation", "vector_spaces",
    r"נגדיר את **מרחב האפס** של מטריצה $A$ כאוסף הפתרונות $\mathbf{x}$ של מערכת משוואות הומוגנית $A\mathbf{x}=\mathbf{0}$. מצא בסיס של מרחב האפס וגם את מימדו.",
    J(r"אם $A\mathbf{x}=\mathbf{0}$, אז",
      "$$A=" + pm("1&0&1&1", "1&1&2&0", "0&1&1&-1") + r"\to" + pm("1&0&1&1", "0&1&1&-1", "0&1&1&-1") + r"\to" + pm("1&0&1&1", "0&1&1&-1", "0&0&0&0") + "$$",
      r"ומכאן נובע ש-",
      "$$\\mathbf{x}=" + pm("x_1", "x_2", "x_3", "x_4") + "=" + pm("-s-t", "-s+t", "s", "t") + "=s" + pm("-1", "-1", "1", "0") + "+t" + pm("-1", "1", "0", "1") + "$$",
      r"לכן נקבל ש-",
      r"$$\mathrm{null\,sp}(A)=\mathrm{sp}\left\{" + pm("-1", "-1", "1", "0") + "," + pm("-1", "1", "0", "1") + r"\right\},\qquad\dim(\mathrm{null\,sp}(A))=2$$"),
    7, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "vector_spaces",
    r"מצא בסיס של מרחב השורות של מטריצה $A$ ואת מימדו.",
    J(r"מהדירוג של הסעיף א׳ נקבל ש-",
      r"$$\mathrm{row\,sp}(A)=\mathrm{sp}\left\{[1\ 0\ 1\ 1],\ [0\ 1\ 1\ -1]\right\}=\mathrm{sp}\left\{[1\ 0\ 1\ 1],\ [1\ 1\ 2\ 0]\right\}$$",
      r"וכתוצאה מכך $\dim(\mathrm{row\,sp}(A))=2$."),
    7, contextId="c3"))

questions.append(Q(
    3, "ג", "computation", "vector_spaces",
    r"מצא בסיס של מרחב העמודות של מטריצה $A$ ואת מימדו.",
    J(r"מהצורה המדורגת (סעיף א׳) נבע שהעמודות הראשונה והשנייה הן עמודות הציר של המטריצה $A$. כלומר, העמודות הראשונה והשנייה בצורה המקורית של $A$ יוצרות בסיס במרחב העמודות של $A$, כלומר",
      r"$$\mathrm{col\,sp}(A)=\mathrm{sp}\left\{" + pm("1", "1", "0") + "," + pm("0", "1", "1") + r"\right\}$$",
      r"ולכן $\dim(\mathrm{col\,sp}(A))=2$."),
    7, contextId="c3"))

questions.append(Q(
    3, "ד", "computation", "vector_spaces",
    r"בדוק שהסכום של מימד מרחב האפס ומימד של מרחב העמודות שווה למספר העמודות של $A$.",
    r"$$\dim(\mathrm{null\,sp}(A))+\dim(\mathrm{col\,sp}(A))=2+2=4$$ וזה שווה למספר העמודות של $A$.",
    4, contextId="c3"))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "determinants",
    r"עבור אילו ערכי $a$ המטריצה $A$ הפיכה?",
    J(r"נחשב את הדטרמיננטה של $A$:",
      r"$$\begin{vmatrix}2a&4&4+2a\\a&3&5\\1&1&a\end{vmatrix}=1\cdot\begin{vmatrix}4&4+2a\\3&5\end{vmatrix}-1\cdot\begin{vmatrix}2a&4+2a\\a&5\end{vmatrix}+a\cdot\begin{vmatrix}2a&4\\a&3\end{vmatrix}=$$",
      r"$$=(20-12-6a)-\left(10a-4a-2a^2\right)+a(6a-4a)=4a^2-12a+8=4\left(a^2-3a+2\right)=4(a-2)(a-1)$$",
      r"עבור $a=1,2$ הדטרמיננטה מתאפסת, ולכן המטריצה $A$ אינה הפיכה. ומכאן שכאשר $a\neq1,2$ המטריצה $A$ הפיכה."),
    5, contextId="c4a"))

T0 = [["0", "4", "4", "1", "0", "0"], ["0", "3", "5", "0", "1", "0"], ["1", "1", "0", "0", "0", "1"]]
T1 = [["1", "1", "0", "0", "0", "1"], ["0", "3", "5", "0", "1", "0"], ["0", "4", "4", "1", "0", "0"]]
T2 = [["1", "1", "0", "0", "0", "1"], ["0", "1", r"5/3", "0", r"1/3", "0"], ["0", "4", "4", "1", "0", "0"]]
T3 = [["1", "1", "0", "0", "0", "1"], ["0", "1", r"5/3", "0", r"1/3", "0"], ["0", "0", r"-8/3", "1", r"-4/3", "0"]]
T4 = [["1", "1", "0", "0", "0", "1"], ["0", "1", r"5/3", "0", r"1/3", "0"], ["0", "0", "1", r"-3/8", r"1/2", "0"]]
T5 = [["1", "1", "0", "0", "0", "1"], ["0", "1", "0", r"5/8", r"-1/2", "0"], ["0", "0", "1", r"-3/8", r"1/2", "0"]]
T6 = [["1", "0", "0", r"-5/8", r"1/2", "1"], ["0", "1", "0", r"5/8", r"-1/2", "0"], ["0", "0", "1", r"-3/8", r"1/2", "0"]]
questions.append(Q(
    4, "ב", "computation", "rank_inverse",
    r"חשב את $A^{-1}$ עבור $a=0$.",
    J(r"נציב $a=0$ ב-$A$ ונקבל $" + pm("0&4&4", "0&3&5", "1&1&0") + r"$, נחשב את ההופכית שלה:",
      "$$" + aug(T0) + arrow(r"R_1\leftrightarrow R_3") + aug(T1) + arrow(r"R_2\leftarrow R_2/3") + aug(T2) + "$$",
      "$$" + arrow(r"R_3\leftarrow R_3-4R_2") + aug(T3) + arrow(r"R_3\leftarrow R_3/(-8/3)") + aug(T4) + "$$",
      "$$" + arrow(r"R_2\leftarrow R_2-(5/3)R_3") + aug(T5) + arrow(r"R_1\leftarrow R_1-R_2") + aug(T6) + "$$",
      r"ולכן קיבלנו:",
      r"$$" + pm("0&4&4", "0&3&5", "1&1&0") + r"^{-1}=" + pm(r"-5/8&1/2&1", r"5/8&-1/2&0", r"-3/8&1/2&0") + "$$"),
    5, contextId="c4a"))

questions.append(Q(
    4, "ג", "computation", "eigen_diagonalization",
    r"מצא את כל הערכים העצמיים והווקטורים העצמיים של $B$.",
    J(r"$$|\lambda I-B|=\begin{vmatrix}\lambda-3&-1&0\\0&\lambda-2&0\\-1&-1&\lambda-4\end{vmatrix}=(\lambda-2)\begin{vmatrix}\lambda-3&0\\-1&\lambda-4\end{vmatrix}=(\lambda-2)[(\lambda-3)(\lambda-4)-0]=(\lambda-2)(\lambda-3)(\lambda-4)$$",
      r"קיבלנו שהערכים העצמיים הם $2,3,4$. כל הע״ע שונים זה מזה ולכן יתקבלו עבורם וי״ע בת״ל. מכאן שמטריצה $B$ ניתנת לליכסון. כעת נמצא את הווקטורים העצמיים.",
      r"עבור ע״ע $2$:",
      "$$" + pm("-1&-1&0", "0&0&0", "-1&-1&-2") + r"\to\cdots\to" + pm("1&1&0", "0&0&1", "0&0&0") + "$$",
      r"נסמן $y=t$ ונקבל $x=-t$, $z=0$. הוקטור העצמי המתקבל הוא: $" + pm("-1", "1", "0") + r"$.",
      r"עבור ע״ע $3$:",
      "$$" + pm("0&-1&0", "0&1&0", "-1&-1&-1") + r"\to\cdots\to" + pm("1&0&1", "0&1&0", "0&0&0") + "$$",
      r"נסמן $z=t$ ונקבל $x=-t$, $y=0$. הוקטור העצמי המתקבל הוא: $" + pm("-1", "0", "1") + r"$.",
      r"עבור ע״ע $4$:",
      "$$" + pm("1&-1&0", "0&2&0", "-1&-1&0") + r"\to\cdots\to" + pm("1&0&0", "0&1&0", "0&0&0") + "$$",
      r"נסמן $z=t$ ונקבל $x=0$, $y=0$. הוקטור העצמי המתקבל הוא: $" + pm("0", "0", "1") + r"$."),
    9, contextId="c4b"))

questions.append(Q(
    4, "ד", "computation", "eigen_diagonalization",
    r"מצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$.",
    J(r"$$D=" + pm("2&0&0", "0&3&0", "0&0&4") + r",\qquad P=" + pm("-1&-1&0", "1&0&0", "0&1&1") + "$$"),
    6, contextId="c4b"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "proof", "vector_spaces",
    r"הוכח כי $W$ הוא תת מרחב.",
    J(r"נתונה הקבוצה $W$, ראשית נפשט אותה:",
      r"$$W=\left\{" + pm("a&2a", "b&c") + r"\ \middle|\ a,b,c\in\mathbb{R},\ a+b=0\right\}=\left\{" + pm("a&2a", "b&c") + r"\ \middle|\ a,b,c\in\mathbb{R},\ b=-a\right\}=\left\{" + pm("a&2a", "-a&c") + r"\ \middle|\ a,c\in\mathbb{R}\right\}$$",
      r"נוכיח כי $W$ תת מרחב.",
      r"נראה כי $W$ אינה קבוצה ריקה: $\vec 0\in W\Rightarrow W\neq\emptyset$.",
      r"עבור שתי המטריצות המשתייכות ל-$W$ נראה כי הסכום שלהן גם שייך ל-$W$. עבור $A,B\in W$, $A=" + pm("a_1&2a_1", "-a_1&c_1") + r"$, $B=" + pm("a_2&2a_2", "-a_2&c_2") + r"$:",
      r"$$A+B=" + pm("a_1&2a_1", "-a_1&c_1") + "+" + pm("a_2&2a_2", "-a_2&c_2") + "=" + pm("a_1+a_2&2(a_1+a_2)", "-(a_1+a_2)&c_1+c_2") + r"\in W$$",
      r"סגירות לכפל בסקלר: עבור $A\in W$ ו-$\alpha\in\mathbb{R}$, $A=" + pm("a_1&2a_1", "-a_1&c_1") + r"$:",
      r"$$\alpha A=\alpha" + pm("a_1&2a_1", "-a_1&c_1") + "=" + pm(r"\alpha a_1&2(\alpha a_1)", r"-(\alpha a_1)&\alpha c_1") + r"\in W$$",
      r"ראינו כי 3 התנאים מתקיימים ולכן הקבוצה היא תת מרחב."),
    7, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "vector_spaces",
    r"מצא בסיס ומימד של $W$.",
    J(r"$$W=\left\{" + pm("a&2a", "-a&c") + r"\ \middle|\ a,c\in\mathbb{R}\right\}=\left\{a" + pm("1&2", "-1&0") + "+c" + pm("0&0", "0&1") + r"\ \middle|\ a,c\in\mathbb{R}\right\}=\mathrm{sp}\left\{" + pm("1&2", "-1&0") + "," + pm("0&0", "0&1") + r"\right\}$$",
      r"$$B_W=\left\{" + pm("1&2", "-1&0") + "," + pm("0&0", "0&1") + r"\right\},\qquad\dim(W)=2$$"),
    7, contextId="c5"))

V0 = [["1", "0", "-1", "1", "0"], ["2", "0", "2", "0", "0"], ["-1", "0", "1", "-1", "0"], ["0", "1", "-3", "2", "0"]]
V1 = [["1", "0", "-1", "1", "0"], ["0", "0", "4", "-2", "0"], ["0", "0", "0", "0", "0"], ["0", "1", "-3", "2", "0"]]
V2 = [["1", "0", "-1", "1", "0"], ["0", "1", "-3", "2", "0"], ["0", "0", "4", "-2", "0"], ["0", "0", "0", "0", "0"]]
questions.append(Q(
    5, "ג", "computation", "vector_spaces",
    r"מצא בסיס ומימד למרחב $W\cap U$.",
    J(r"כדי לפתור זאת ״נישר״ את המטריצות ונעביר אותן למרחב ווקטורים של $\mathbb{R}^4$ ונכתוב אותם כוקטורים במטריצה. נחפש צירוף $\alpha_1\vec w_1+\alpha_2\vec w_2+\beta_1\vec u_1+\beta_2\vec u_2=\vec 0$ כאשר $\vec w_1,\vec w_2$ הבסיס של $W$ ו-$\vec u_1,\vec u_2$ המטריצות הפורשות את $U$:",
      "$$" + aug(V0, 4) + arrow(r"\substack{R_2\to R_2-2R_1\\R_3\to R_3+R_1}") + aug(V1, 4) + arrow(r"R_4\leftrightarrow R_3") + aug(V1[:2] + [V1[3], V1[2]], 4) + "$$",
      "$$" + arrow(r"R_2\leftrightarrow R_3") + aug(V2, 4) + "$$",
      r"$$\begin{cases}\beta_2=t\\4\beta_1-2\beta_2=0\end{cases}\Rightarrow\begin{cases}\beta_2=t\\\beta_1=0.5t\end{cases}$$",
      r"$$W\cap U=0.5t" + pm("-1&2", "1&-3") + "+t" + pm("1&0", "-1&2") + "=t" + pm("0.5&1", "-0.5&0.5") + r"=\mathrm{sp}\left\{" + pm("0.5&1", "-0.5&0.5") + r"\right\}$$",
      r"$$B_{W\cap U}=\left\{" + pm("1&2", "-1&1") + r"\right\},\qquad\dim(W\cap U)=1$$"),
    6, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "vector_spaces",
    r"תן דוגמא למטריצה השייכת למרחב $M_{2\times2}$, שאינה נמצאת בקבוצה $W$.",
    J(r"המטריצה $C$ לא נמצאת ב-$W$, וכן שייכת למרחב המטריצות $2\times2$,",
      r"$$C=" + pm("1&1", "1&1") + r"\notin W$$"),
    5, contextId="c5"))

# ------------------------------------------------------------------ Q6
Z0 = [["1", "1", "0", "0", "0"], ["0", "1", "1", "0", "0"], ["0", "1", "0", "1", "0"]]
Z1 = [["1", "1", "0", "0", "0"], ["0", "1", "1", "0", "0"], ["0", "0", "-1", "1", "0"]]
Z2 = [["1", "1", "0", "0", "0"], ["0", "1", "0", "1", "0"], ["0", "0", "-1", "1", "0"]]
Z3 = [["1", "0", "0", "-1", "0"], ["0", "1", "0", "1", "0"], ["0", "0", "1", "-1", "0"]]
questions.append(Q(
    6, "א", "computation", "linear_maps",
    r"מצא בסיס ומימד ל-$\mathrm{Ker}(T)$.",
    J(r"$\mathrm{Ker}(T)$: תהי $A=" + pm("a&b", "c&d") + r"$ בגרעין של $T$, אז:",
      r"$$T(A)=T" + pm("a&b", "c&d") + r"=(0,0,0)\ \Rightarrow\ (a+b,\ b+c,\ b+d)=0$$",
      r"$$\begin{cases}a+b=0\\b+c=0\\b+d=0\end{cases}\qquad" + aug(Z0, 4) + r"\to" + aug(Z1, 4) + r"\to" + aug(Z2, 4) + r"\to" + aug(Z3, 4) + "$$",
      r"$n=4,\ r=3\ \Rightarrow\ \dim\ker T=4-3=1$",
      r"$$\begin{cases}a-d=0\\b+d=0\\c-d=0\end{cases}\qquad d=t,\ a=t,\ b=-t,\ c=t\qquad(a,b,c,d)=(t,-t,t,t)=t(1,-1,1,1)$$",
      r"לכן, מטריצה $A=" + pm("a&b", "c&d") + r"$ נמצאת בגרעין אם ורק אם היא מהצורה",
      r"$$A=" + pm("a&b", "c&d") + "=" + pm("t&-t", "t&t") + "=t" + pm("1&-1", "1&1") + "$$",
      r"לכן, בסיס ל-$\mathrm{Ker}(T)$ הוא: $\left\{" + pm("1&-1", "1&1") + r"\right\}$ ומימד הגרעין הוא 1."),
    7, contextId="c6"))

questions.append(Q(
    6, "ב", "computation", "linear_maps",
    r"מצא בסיס ומימד ל-$\mathrm{Im}(T)$.",
    J(r"לפי משפט, אם $T:V\to W$ אז: $\dim V=\dim\mathrm{Ker}(T)+\dim\mathrm{Im}(T)$. במקרה שלנו, $\dim V=4$ ולפי סעיף א׳, $\dim\mathrm{Ker}(T)=1$ לכן, $\dim\mathrm{Im}(T)=3$. כיוון ש-$\mathrm{Im}(T)$ הוא תת מרחב של $\mathbb{R}^3$ ממימד 3, הרי ש-$\mathrm{Im}T=\mathbb{R}^3$ וכל בסיס של $\mathbb{R}^3$ הוא גם בסיס של $\mathrm{Im}T$. נבחר, למשל את הבסיס הסטנדרטי:",
      r"$$\{(1,0,0),\ (0,1,0),\ (0,0,1)\}$$",
      r"אפשרות אחרת:",
      r"$$T(A)=T" + pm("a&b", "c&d") + "=(a+b,\\ b+c,\\ b+d)=a(1,0,0)+b(1,1,1)+c(0,1,0)+d(0,0,1)$$",
      r"לכן, הקבוצה $\{(1,0,0),(1,1,1),(0,1,0),(0,0,1)\}$ פורשת את $\mathrm{Im}(T)$, ואם נשמיט את הוקטורים התלויים נקבל בסיס לתמונה, למשל:",
      r"$$\{(1,0,0),\ (0,1,0),\ (0,0,1)\}$$"),
    7, contextId="c6"))

questions.append(Q(
    6, "ג", "computation", "linear_maps",
    r"האם $T$ היא חח״ע? האם $T$ על? נמק!",
    J(r"לפי משפט, העתקה $T$ היא חח״ע (1:1) אםם $\mathrm{Ker}(T)=\{0\}$. לפי סעיף א׳, $\mathrm{Ker}(T)\neq\{0\}$, לכן $T$ לא חח״ע.",
      r"לפי משפט, העתקה $T$ היא על אםם $\dim\mathrm{Im}(T)=\dim U$. לפי סעיף ב׳, $\dim\mathrm{Im}(T)=\dim U=\dim\mathbb{R}^3=3$, לכן $T$ היא על."),
    5, contextId="c6"))

questions.append(Q(
    6, "ד", "computation", "linear_maps",
    r"מצא את כל המטריצות ב-$\mathbb{R}^{2\times2}$ שתמונתם נותנת וקטור $(1,1,1)$. האם הן מהוות תת מרחב של $\mathbb{R}^{2\times2}$? נמק!",
    J(r"יש למצוא את כל המקורות של $(1,1,1)$, כלומר את כל המטריצות $A$ כך ש-$T(A)=(1,1,1)$:",
      r"$$T(A)=T" + pm("a&b", "c&d") + r"=(a+b,\ b+c,\ b+d)=(1,1,1)$$",
      r"$$\begin{cases}a+b=1\\b+c=1\\b+d=1\end{cases}\qquad" + aug([["1", "1", "0", "0", "1"], ["0", "1", "1", "0", "1"], ["0", "1", "0", "1", "1"]], 4) + r"\to" + aug([["1", "0", "-1", "0", "0"], ["0", "1", "1", "0", "1"], ["0", "0", "-1", "1", "0"]], 4) + r"\to" + aug([["1", "0", "0", "-1", "0"], ["0", "1", "0", "1", "1"], ["0", "0", "-1", "1", "0"]], 4) + "$$",
      r"$$\begin{cases}a-d=0\\b+d=1\\c-d=0\end{cases}\qquad a=c=d,\ b=1-d$$",
      r"$$A=" + pm("a&b", "c&d") + "=" + pm("d&1-d", "d&d") + "=d" + pm("1&-1", "1&1") + "+" + pm("0&1", "0&0") + "$$",
      r"לכן, אוסף המקורות של הוקטור $(1,1,1)$ הוא כל המטריצות מהצורה $\left\{" + pm("d&1-d", "d&d") + r"\right\}$.",
      r"מאחר שאוסף זה אינו מכיל את מטריצת ה-0 (מטריצת ה-0 היא מקור רק של וקטור ה-0 ולכן אינה נמצאת בין המקורות של הוקטור $(1,1,1)$), הרי שאוסף זה אינו מהווה תת-מרחב וקטורי של $\mathbb{R}^{2\times2}$."),
    6, contextId="c6"))

# ---- rubric / pitfalls / steps (ai-draft); every number is re-derived with sympy in tools/verify/<CODE>/verify_steps_<CODE>.py ----
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def num(prompt, ans, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": ans, "tol": tol, "explain": explain}


def cho(prompt, correct, others, explain):
    """the correct option is placed at a rotating position so the key is not always 'a'"""
    vals = list(others)
    pos = cho.n % (len(vals) + 1)
    cho.n += 1
    vals.insert(pos, correct)
    return {"type": "choice", "prompt": prompt, "options": opts(*vals), "correctId": IDS[pos], "explain": explain}


cho.n = 0


def odr(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def fnd(prompt, lines, bug, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": bug, "explain": explain}


ENR = {}


ENR[(1, "א")] = dict(
    rubric=rub((r"נקודות וקטורי כיוון של שני הישרים: $M_1(1,2,0)$, $\vec a_1=(1,k,2)$, $M_2(0,3,-2)$, $\vec a_2=(2,1,1)$", 2),
               (r"$\overrightarrow{M_1M_2}=M_2-M_1=(-1,1,-2)$", 1),
               (r"הדטרמיננטה של $\overrightarrow{M_1M_2},\vec a_1,\vec a_2$ שווה $3k+3$", 2),
               (r"$k=-1$", 1)),
    pitfalls=[r"לחשב $\overrightarrow{M_1M_2}$ בטעות (למשל $(-1,3,-2)$): הדטרמיננטה היא אז $3k+9$ ומתקבל $k=-3$ במקום $k=-1$.",
              r"לשכוח לוודא שהכיוונים אינם מקבילים."],
    steps=[
        cho(r"מהו התנאי לכך ששני ישרים במרחב נחתכים?", r"הכיוונים אינם מקבילים והווקטורים $\vec a_1,\vec a_2,\overrightarrow{M_1M_2}$ באותו מישור (דטרמיננטה אפס)",
            [r"המכפלה הסקלרית $\vec a_1\cdot\vec a_2$ שווה אפס", r"המכפלה הווקטורית $\vec a_1\times\vec a_2$ שווה אפס", r"הדטרמיננטה של $\vec a_1,\vec a_2,\overrightarrow{M_1M_2}$ שונה מאפס"],
            r"ב-$k=-1$ הישרים נחתכים, ושם $\vec a_1\cdot\vec a_2=3\neq0$ ו-$\vec a_1\times\vec a_2\neq0$, והדטרמיננטה מתאפסת. דטרמיננטה שונה מאפס פירושה ישרים מצטלבים."),
        num(r"מהו הרכיב השני של $\overrightarrow{M_1M_2}=M_2-M_1$?", 1, r"$3-2=1$."),
        num(r"מהו ערך הדטרמיננטה $3k+3$ כאשר $k=0$?", 3, r"$\begin{vmatrix}-1&1&-2\\1&0&2\\2&1&1\end{vmatrix}=3$."),
        num(r"עבור איזה $k$ הדטרמיננטה $3k+3$ מתאפסת?", -1, r"$3k+3=0\Rightarrow k=-1$."),
    ])

ENR[(1, "ב")] = dict(
    rubric=rub((r"שימוש בנוסחת המרחק בין ישרים מצטלבים", 2),
               (r"המכפלה הווקטורית $\vec a_1\times\vec a_2=(0,3,-3)$", 2),
               (r"המכפלה המעורבת $\left(\vec a_1\times\vec a_2\right)\cdot\overrightarrow{M_1M_2}=9$", 1),
               (r"$d=\frac{9}{3\sqrt2}=\frac{3\sqrt2}{2}$", 2)),
    pitfalls=[r"להשתמש בוקטור $\overrightarrow{M_1M_2}$ שגוי, למשל $(-1,3,-2)$: המכפלה המעורבת היא אז $15$ ומתקבל $\frac{5\sqrt2}{2}$ במקום $\frac{3\sqrt2}{2}$.",
              r"לשכוח את הערך המוחלט או לחלק באורך הווקטור $\overrightarrow{M_1M_2}$ במקום באורך המכפלה הווקטורית."],
    steps=[
        cho(r"איזו נוסחה נותנת את המרחק בין שני ישרים מצטלבים?", r"$\frac{\left|\left(\vec a_1\times\vec a_2\right)\cdot\overrightarrow{M_1M_2}\right|}{\left\|\vec a_1\times\vec a_2\right\|}$",
            [r"$\left\|\overrightarrow{M_1M_2}\right\|$", r"$\frac{\left|\vec a_1\cdot\vec a_2\right|}{\left\|\vec a_1\times\vec a_2\right\|}$", r"$\frac{\left\|\vec a_1\times\vec a_2\right\|}{\left\|\overrightarrow{M_1M_2}\right\|}$"],
            r"עבור $k=2$ הנוסחה הנכונה נותנת $\approx2.12$, ואילו האחרות נותנות $\sqrt6\approx2.45$, $\frac{6}{3\sqrt2}\approx1.41$ ו-$\frac{3\sqrt2}{\sqrt6}\approx1.73$."),
        num(r"מהו הרכיב השני של $\vec a_1\times\vec a_2$ עבור $\vec a_1=(1,2,2)$, $\vec a_2=(2,1,1)$?", 3, r"התוצאה היא $(0,3,-3)$."),
        num(r"מהי המכפלה המעורבת $\left(\vec a_1\times\vec a_2\right)\cdot\overrightarrow{M_1M_2}$ עבור $\overrightarrow{M_1M_2}=(-1,1,-2)$?", 9, r"$0\cdot(-1)+3\cdot1+(-3)(-2)=9$."),
        num(r"מהו המרחק $d$ (בקירוב לשלוש ספרות אחרי הנקודה)?", 2.1213, r"$d=\frac{9}{3\sqrt2}=\frac{3\sqrt2}{2}\approx2.1213$.", 0.001),
    ])

ENR[(1, "ג")] = dict(
    rubric=rub((r"קביעה שהטענה שקרית", 1),
               (r"העברת אגף: $\vec a\times(\vec b-\vec c)=\vec 0$ ואינו מחייב $\vec b=\vec c$", 2),
               (r"בחירת דוגמה נגדית $\vec a=(1,0,0)$, $\vec b=(1,1,0)$, $\vec c=(0,1,0)$", 2),
               (r"בדיקה: שתי המכפלות שוות $(0,0,1)\neq\vec 0$ ואילו $\vec b\neq\vec c$", 1)),
    pitfalls=[r"לצמצם $\vec a$ משני האגפים כאילו מדובר בכפל מספרים.",
              r"לבחור דוגמה שבה $\vec a\times\vec b=\vec 0$ (ההנחה דורשת שהמכפלה שונה מאפס)."],
    steps=[
        cho(r"מה מסיקים מ-$\vec a\times(\vec b-\vec c)=\vec 0$ כש-$\vec a\neq\vec 0$?", r"$\vec b-\vec c$ מקביל ל-$\vec a$, ולא בהכרח אפס",
            [r"$\vec b-\vec c=\vec 0$ בהכרח", r"$\vec b-\vec c$ ניצב ל-$\vec a$", r"$\vec a=\vec 0$"],
            r"בדוגמה $\vec b-\vec c=(1,0,0)=\vec a$: אינו אפס, אינו ניצב ל-$\vec a$ (המכפלה הסקלרית 1), ו-$\vec a\neq\vec 0$."),
        num(r"מהו הרכיב השלישי של $\vec a\times\vec b$ עבור $\vec a=(1,0,0)$, $\vec b=(1,1,0)$?", 1, r"$a_xb_y-a_yb_x=1\cdot1-0=1$."),
        num(r"מהו הרכיב הראשון של $\vec b-\vec c$?", 1, r"$1-0=1$, כלומר $\vec b\neq\vec c$."),
    ])

ENR[(2, "א")] = dict(
    rubric=rub((r"כתיבת המטריצה המורחבת", 1),
               (r"$R_2-(k-1)R_1$ ו-$R_3-kR_1$", 3),
               (r"החלפת שורות ושינוי סימן כדי שהאיבר $2$ יופיע בשורה 2", 1),
               (r"$R_3-kR_2$ והצורה המדורגת עם שורה אחרונה $\left(0\ 0\ 2-2k^2\mid2+k-k^2\right)$", 3)),
    pitfalls=[r"לכתוב $R_3+kR_1$ במקום $R_3-kR_1$ (טעות סימן).",
              r"לחלק בביטוי עם פרמטר בלי לבדוק את הערכים שמאפסים אותו."],
    steps=[
        cho(r"איזו פעולה מאפסת את האיבר בשורה 3 עמודה 2 במטריצה $\left(\begin{array}{ccc|c}1&-1&1&1\\0&2&2k&k-1\\0&2k&2&2\end{array}\right)$?", r"$R_3\to R_3-kR_2$",
            [r"$R_3\to R_3+kR_2$", r"$R_3\to R_3-R_2$", r"$R_3\to R_3-2kR_2$"],
            r"האיבר הוא $2k$ מול $2$ בשורה 2, ולכן צריך להחסיר $k$ פעמים שורה 2. שאר הפעולות מאפסות רק עבור ערכים בודדים של $k$ (או לא כלל)."),
        num(r"אחרי $R_2-(k-1)R_1$ ו-$R_3-kR_1$: מהו האיבר בשורה 2 עמודה 2 עבור $k=3$?", 6, r"האיבר הוא $2k=6$."),
        num(r"באותה מטריצה: מהו האיבר בשורה 3 עמודה 4 עבור $k=3$?", -2, r"האיבר הוא $1-k=-2$."),
        num(r"במטריצה המדורגת הסופית: מהו האיבר בשורה 3 עמודה 3 עבור $k=2$?", -6, r"האיבר הוא $2-2k^2=2-8=-6$."),
    ])

ENR[(2, "ב")] = dict(
    rubric=rub((r"$k=1$: שורת סתירה $(0\ 0\ 0\mid2)$ ולכן אין פתרון", 3),
               (r"$k\neq\pm1$: שלושה איברים מובילים ולכן פתרון יחיד", 3),
               (r"$k=-1$: שורת אפסים מלאה ולכן אינסוף פתרונות", 3)),
    pitfalls=[r"לרשום 'או' במקום 'וגם' בתנאי הפתרון היחיד: $k\neq1$ וגם $k\neq-1$.",
              r"לבלבל בין שורת אפסים מלאה (אינסוף פתרונות) לבין שורת סתירה (אין פתרון)."],
    steps=[
        num(r"מהי דרגת מטריצת המקדמים עבור $k=1$?", 2, r"שורה 3 היא $(0\ 0\ 0\mid2)$, ולכן ב-$A$ שורה אפס."),
        num(r"מהי דרגת המטריצה המורחבת עבור $k=1$?", 3, r"השורה $(0\ 0\ 0\mid2)$ מוסיפה איבר מוביל."),
        num(r"מהי דרגת המטריצה המורחבת עבור $k=-1$?", 2, r"השורה השלישית מתאפסת לגמרי, ולכן הדרגה 2 (גם ל-$A$)."),
        cho(r"עבור אילו ערכי $k$ יש פתרון יחיד?", r"$k\neq1$ וגם $k\neq-1$",
            [r"$k\neq1$ או $k\neq-1$", r"$k\neq1$ בלבד", r"$k\neq-1$ בלבד"],
            r"התנאי 'או' מתקיים לכל $k$, כולל $k=1$ (אין פתרון) ו-$k=-1$ (אינסוף פתרונות). כל אחד מהתנאים הבודדים כולל את אחד הערכים הבעייתיים."),
    ])

ENR[(2, "ג")] = dict(
    rubric=rub((r"הצבת $k=-1$ במטריצה המדורגת: שורה 2 היא $(0\ 2\ -2\mid-2)$", 3),
               (r"$x=0$, $y=z-1$ וזיהוי $z$ כחופשי", 3),
               (r"הצגה פרמטרית $(0,-1,0)+z(0,1,1)$", 2)),
    pitfalls=[r"לרשום את השורה השנייה בטעות כ-$(0\ 1\ 1\mid-1)$ ולקבל $x=-2z$.",
              r"לשכוח שהפתרון הוא ישר ולכתוב נקודה אחת."],
    steps=[
        num(r"מהו $x$ בכל פתרון של המערכת עבור $k=-1$? (השורה השנייה המקורית היא $-2x=0$)", 0, r"$(k-1)x=-2x=0$ ולכן $x=0$."),
        num(r"בפתרון $y=z-1$: מהו $y$ כאשר $z=3$?", 2, r"$y=3-1=2$."),
        cho(r"איזה וקטור הוא וקטור כיוון של קבוצת הפתרונות?", r"$(0,1,1)$",
            [r"$(-2,-1,1)$", r"$(1,1,1)$", r"$(0,-1,0)$"],
            r"וקטור כיוון חייב לקיים את המערכת ההומוגנית: $x=0$ ו-$y=z$. $(0,-1,0)$ הוא הפתרון הפרטי, ושני האחרים אינם מקיימים $x=0$."),
    ])

ENR[(3, "א")] = dict(
    rubric=rub((r"דירוג $A$ לצורה $\begin{pmatrix}1&0&1&1\\0&1&1&-1\\0&0&0&0\end{pmatrix}$", 2),
               (r"שני משתנים חופשיים $x_3=s$, $x_4=t$", 2),
               (r"פתרון כללי $s(-1,-1,1,0)+t(-1,1,0,1)$", 2),
               (r"בסיס של מרחב האפס ומימד 2", 1)),
    pitfalls=[r"לבחור את העמודות המובילות כמשתנים חופשיים במקום את העמודות ללא איבר מוביל.",
              r"טעות סימן בהעברת $x_3,x_4$ לאגף ימין."],
    steps=[
        num(r"מהי דרגת $A$?", 2, r"שני איברים מובילים בצורה המדורגת."),
        cho(r"איזה וקטור שייך למרחב האפס של $A$?", r"$(-1,1,0,1)$",
            [r"$(1,-1,1,0)$", r"$(1,1,1,1)$", r"$(0,0,1,1)$"],
            r"$A(-1,1,0,1)^T=(0,0,0)^T$. עבור האחרים, השורה הראשונה $(1\ 0\ 1\ 1)$ נותנת $2,\ 3,\ 2$ ולא 0."),
        num(r"בפתרון $x_2=-s+t$: מהו $x_2$ כאשר $s=2$, $t=1$?", -1, r"$-2+1=-1$."),
    ])

ENR[(3, "ב")] = dict(
    rubric=rub((r"שורות מדורגת לא אפסיות $[1\ 0\ 1\ 1]$ ו-$[0\ 1\ 1\ -1]$ הן בסיס", 3),
               (r"השורה השלישית של $A$ תלויה בשתיים הראשונות", 2),
               (r"מימד מרחב השורות הוא 2", 2)),
    pitfalls=[r"לכלול גם את שורת האפסים או את כל שלוש שורות $A$ בבסיס.",
              r"לקחת את עמודות הציר כבסיס של מרחב השורות."],
    steps=[
        num(r"מהו המימד של מרחב השורות של $A$?", 2, r"מספר השורות הלא אפסיות בצורה המדורגת."),
        num(r"השורה השלישית של $A$ היא $c\cdot R_2+d\cdot R_1$ (כש-$R_1=[1\ 0\ 1\ 1]$, $R_2=[1\ 1\ 2\ 0]$). מהו $d$?", -1, r"$R_3=R_2-R_1=[0\ 1\ 1\ -1]$."),
        cho(r"מה מהווה בסיס של מרחב השורות?", r"שתי השורות הלא אפסיות של הצורה המדורגת",
            [r"עמודות הציר של $A$", r"כל שלוש שורות $A$", r"שורת האפסים והשורה הראשונה"],
            r"עמודות הציר הן וקטורים ב-$\mathbb{R}^3$ ולא שורות; שלוש שורות $A$ תלויות ($R_3=R_2-R_1$); שורת האפסים לעולם אינה בבסיס."),
    ])

ENR[(3, "ג")] = dict(
    rubric=rub((r"זיהוי עמודות הציר: העמודות 1 ו-2", 2),
               (r"לקיחת העמודות המקוריות של $A$ כבסיס", 3),
               (r"מימד מרחב העמודות הוא 2", 2)),
    pitfalls=[r"לקחת את העמודות של הצורה המדורגת במקום העמודות המקוריות של $A$.",
              r"להכליל את כל ארבע העמודות לבסיס."],
    steps=[
        num(r"כמה עמודות ציר יש ב-$A$?", 2, r"שני איברים מובילים."),
        cho(r"מאיפה נלקחים וקטורי הבסיס של $\mathrm{Col}(A)$?", r"מהעמודות המקוריות של $A$ שבמיקום עמודות הציר",
            [r"מעמודות הצורה המדורגת", r"מכל ארבע עמודות $A$", r"משורות $A$"],
            r"עמודות הצורה המדורגת אינן שייכות למרחב העמודות (למשל $(1,0,0)^T\notin\mathrm{Col}(A)$); ארבע העמודות תלויות; ושורות $A$ הן וקטורים ב-$\mathbb{R}^4$."),
        num(r"העמודה הרביעית של $A$ היא $\mathrm{col}_1+c\cdot\mathrm{col}_2$. מהו $c$?", -1, r"$(1,1,0)^T-(0,1,1)^T=(1,0,-1)^T$."),
    ])

ENR[(3, "ד")] = dict(
    rubric=rub((r"הצבת $\dim(\mathrm{null\,sp}A)=2$ מהסעיף א", 1),
               (r"הצבת $\dim(\mathrm{col\,sp}A)=2$ מהסעיף ג", 1),
               (r"סכום $4$ ושוויון למספר העמודות", 2)),
    pitfalls=[r"להשוות את הסכום למספר השורות (3) במקום למספר העמודות (4)."],
    steps=[
        num(r"כמה עמודות יש ל-$A$?", 4, r"$A$ היא מטריצה $3\times4$."),
        cho(r"איזה משפט מתקיים?", r"$\dim\mathrm{Null}(A)+\mathrm{rank}(A)=$ מספר העמודות של $A$",
            [r"$\dim\mathrm{Null}(A)+\mathrm{rank}(A)=$ מספר השורות של $A$", r"$\dim\mathrm{Null}(A)=\mathrm{rank}(A)$ תמיד", r"$\dim\mathrm{Null}(A)\cdot\mathrm{rank}(A)=$ מספר העמודות"],
            r"כאן $2+2=4$ הוא מספר העמודות ולא מספר השורות (3); השוויון $\dim\mathrm{Null}=\mathrm{rank}$ מקרי; והמכפלה $4$ כאן במקרה."),
    ])

ENR[(4, "א")] = dict(
    rubric=rub((r"פיתוח הדטרמיננטה לפי שורה", 3),
               (r"$\det A=4(a-1)(a-2)$", 1),
               (r"מסקנה: הפיכה אם ורק אם $a\neq1,2$", 1)),
    pitfalls=[r"טעות סימן בפיתוח הדטרמיננטה (סימני המשלימים האלגבריים).",
              r"לרשום רק אחד משני האפסים."],
    steps=[
        num(r"מהו $\det A$ עבור $a=4$?", 24, r"$4(a-1)(a-2)=4\cdot3\cdot2=24$."),
        num(r"מהו $\det A$ עבור $a=0$?", 8, r"$4\cdot(-1)(-2)=8$."),
        cho(r"עבור אילו ערכי $a$ המטריצה $A$ אינה הפיכה?", r"$a=1$ וגם $a=2$",
            [r"$a=-1$ וגם $a=-2$", r"$a=1$ בלבד", r"$a=2$ בלבד"],
            r"$\det A=4(a-1)(a-2)$ מתאפס בדיוק ב-$a=1$ וב-$a=2$."),
    ])

ENR[(4, "ב")] = dict(
    rubric=rub((r"הצבת $a=0$ וכתיבת $[A\mid I]$", 1),
               (r"דירוג מטה: $R_1\leftrightarrow R_3$, חלוקה ב-3, $R_3-4R_2$, חלוקה ב-$-\frac83$", 2),
               (r"דירוג מעלה: $R_2-\frac53R_3$, $R_1-R_2$", 2)),
    pitfalls=[r"לשכוח את פעולת ההחלפה $R_1\leftrightarrow R_3$ ולהתחיל מאיבר מוביל 0.",
              r"טעות בחישוב השברים בעמודות של $I$."],
    steps=[
        num(r"מהו $\det A$ עבור $a=0$ (כך שההופכית קיימת)?", 8, r"$4(a-1)(a-2)=4\cdot2=8$."),
        num(r"מהי הכניסה בשורה 1 עמודה 1 של $A^{-1}$?", -0.625, r"$-\frac58$.", 0.001),
        num(r"מהי הכניסה בשורה 3 עמודה 2 של $A^{-1}$?", 0.5, r"$\frac12$.", 0.001),
    ])

ENR[(4, "ג")] = dict(
    rubric=rub((r"הפולינום האופייני והערכים העצמיים $2,3,4$", 3),
               (r"הערכים העצמיים שונים ולכן $B$ ניתנת ללכסון", 1),
               (r"וקטור עצמי $(-1,1,0)$ לערך $2$", 2),
               (r"וקטור עצמי $(-1,0,1)$ לערך $3$", 2),
               (r"וקטור עצמי $(0,0,1)$ לערך $4$", 1)),
    pitfalls=[r"לפתח את הדטרמיננטה לפי השורה השנייה (המכילה אפסים) ולטעות בסימן.",
              r"לרשום את הווקטור העצמי ללא לבדוק ש-$Bv=\lambda v$."],
    steps=[
        num(r"מהי עקבה של $B$ (סכום איברי האלכסון), השווה לסכום הערכים העצמיים?", 9, r"$3+2+4=9=2+3+4$."),
        num(r"מהו $\det B$, השווה למכפלת הערכים העצמיים?", 24, r"$2\cdot3\cdot4=24$."),
        cho(r"איזה וקטור הוא וקטור עצמי של $B$ עבור הערך $2$?", r"$(-1,1,0)$",
            [r"$(1,1,0)$", r"$(-1,0,1)$", r"$(0,0,1)$"],
            r"$B(-1,1,0)^T=(-2,2,0)^T=2(-1,1,0)^T$. לעומת זאת $B(1,1,0)^T=(4,2,2)^T$ אינו כפולה של הווקטור, ו-$(-1,0,1)$ ו-$(0,0,1)$ הם וקטורים עצמיים של $3$ ו-$4$."),
    ])

ENR[(4, "ד")] = dict(
    rubric=rub((r"$D=\mathrm{diag}(2,3,4)$", 2),
               (r"$P$ עם העמודות $(-1,1,0),(-1,0,1),(0,0,1)$ לפי סדר הערכים ב-$D$", 2),
               (r"$\det P\neq0$ ולכן $P$ הפיכה", 2)),
    pitfalls=[r"לסדר את עמודות $P$ שלא בהתאמה לסדר האיברים ב-$D$.",
              r"לקחת עמודות תלויות ולקבל $P$ לא הפיכה."],
    steps=[
        num(r"מהו $\det P$ (כך שהעמודות בלתי תלויות)?", 1, r"פיתוח לפי עמודה 3 נותן $1\cdot(0+1)=1$."),
        num(r"מהו האיבר בשורה 1 עמודה 2 של $PD$?", -3, r"$P_{12}\cdot D_{22}=-1\cdot3=-3$."),
        cho(r"עמודה 2 של $P$ היא וקטור עצמי של איזה ערך עצמי?", r"$3$",
            [r"$2$", r"$4$", r"$0$"],
            r"עמודה 2 היא $(-1,0,1)^T$ ו-$B(-1,0,1)^T=(-3,0,3)^T=3(-1,0,1)^T$. לכן היא מתאימה ל-$3$ ולא ל-$2$, ל-$4$ או ל-$0$."),
    ])

ENR[(5, "א")] = dict(
    rubric=rub((r"פישוט $W$ ל-$\left\{\begin{pmatrix}a&2a\\-a&c\end{pmatrix}\right\}$", 1),
               (r"$W$ אינה ריקה: מטריצת האפס ב-$W$", 1),
               (r"סגירות לחיבור", 2),
               (r"סגירות לכפל בסקלר", 2),
               (r"מסקנה: $W$ תת-מרחב", 1)),
    pitfalls=[r"לבדוק סגירות רק עבור איברים מסוימים ולא עבור פרמטרים כלליים.",
              r"לשכוח לבדוק שמטריצת האפס שייכת ל-$W$."],
    steps=[
        cho(r"אילו תנאים מגדירים תת-מרחב?", r"לא ריקה, סגורה לחיבור וסגורה לכפל בסקלר",
            [r"מכילה קבוצה סופית הפורשת אותה", r"סגורה לכפל מטריצות", r"מכילה את כל וקטורי הבסיס הסטנדרטי"],
            r"הקבוצה $\{e_1,e_2\}$ מכילה בסיס אך אינה תת-מרחב; ו-$W$ תת-מרחב אך אינה סגורה לכפל מטריצות ($\begin{pmatrix}1&2\\-1&0\end{pmatrix}^2=\begin{pmatrix}-1&2\\-1&-2\end{pmatrix}\notin W$)."),
        fnd("בהוכחה הבאה שורה אחת שגויה. סמנו אותה.",
            [r"$W=\left\{\begin{pmatrix}a&2a\\-a&c\end{pmatrix}\ \middle|\ a,c\in\mathbb{R}\right\}$",
             r"$\vec 0\in W$ (עבור $a=c=0$), ולכן $W\neq\emptyset$",
             r"$A_1+A_2=\begin{pmatrix}a_1+a_2&2(a_1+a_2)\\-(a_1+a_2)&c_1+c_2\end{pmatrix}\in W$",
             r"$\alpha A=\begin{pmatrix}\alpha a_1&2a_1\\-\alpha a_1&\alpha c_1\end{pmatrix}\in W$"], 3,
            r"באיבר (1,2) צריך להיות $2(\alpha a_1)$ ולא $2a_1$; כפי שכתוב כאן המטריצה אינה ב-$W$ עבור $\alpha\neq1$ (האיבר (1,2) חייב להיות כפול 2 מהאיבר (1,1))."),
        num(r"עבור $A_1$ עם $a_1=1$ ו-$A_2$ עם $a_2=2$, מהו האיבר בשורה 1 עמודה 2 של $A_1+A_2$?", 6, r"$2(a_1+a_2)=6$."),
    ])

ENR[(5, "ב")] = dict(
    rubric=rub((r"כתיבה כצירוף: $a\begin{pmatrix}1&2\\-1&0\end{pmatrix}+c\begin{pmatrix}0&0\\0&1\end{pmatrix}$", 3),
               (r"בלתי תלות של שתי המטריצות", 2),
               (r"בסיס $B_W$ ומימד 2", 2)),
    pitfalls=[r"לשכוח לבדוק בלתי תלות.",
              r"לבחור מטריצה שאינה ב-$W$ כאיבר בסיס."],
    steps=[
        num(r"מהו $\dim W$?", 2, r"שני פרמטרים חופשיים $a,c$."),
        cho(r"איזו קבוצה היא בסיס של $W$?", r"$\left\{\begin{pmatrix}1&2\\-1&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix}\right\}$",
            [r"$\left\{\begin{pmatrix}1&2\\-1&0\end{pmatrix},\begin{pmatrix}2&4\\-2&0\end{pmatrix}\right\}$", r"$\left\{\begin{pmatrix}1&2\\-1&0\end{pmatrix}\right\}$", r"$\left\{\begin{pmatrix}1&2\\-1&0\end{pmatrix},\begin{pmatrix}0&1\\0&0\end{pmatrix}\right\}$"],
            r"הקבוצה הראשונה תלויה (הכפלה פי 2), השנייה אינה פורשת את $W$, והשלישית כוללת מטריצה שאינה ב-$W$ (האיבר (1,2) אינו כפולה של האיבר (1,1))."),
        num(r"המטריצה $\begin{pmatrix}2&4\\-2&5\end{pmatrix}\in W$ היא $a\begin{pmatrix}1&2\\-1&0\end{pmatrix}+c\begin{pmatrix}0&0\\0&1\end{pmatrix}$. מהו $c$?", 5, r"$c$ הוא האיבר בשורה 2 עמודה 2."),
    ])

ENR[(5, "ג")] = dict(
    rubric=rub((r"העברה לוקטורים ב-$\mathbb{R}^4$ ובניית המטריצה מ-$\vec w_1,\vec w_2,\vec u_1,\vec u_2$", 2),
               (r"דירוג המטריצה לדרגה 3", 2),
               (r"פתרון עם $\beta_2=t$ ו-$\beta_1=0.5t$", 1),
               (r"הבסיס $\begin{pmatrix}1&2\\-1&1\end{pmatrix}$ וממד 1", 1)),
    pitfalls=[r"להסיק $\dim(W\cap U)=\dim W+\dim U=4$ בלי לבדוק תלות.",
              r"לבלבל בין מקדמי $U$ (ה-$\beta$) לבין מקדמי $W$ (ה-$\alpha$) בשחזור המטריצה."],
    steps=[
        num(r"מהי דרגת המטריצה $4\times4$ שעמודותיה $\vec w_1,\vec w_2,\vec u_1,\vec u_2$?", 3, r"הצורה המדורגת כוללת שורת אפסים."),
        cho(r"איזו נוסחה נותנת את $\dim(W\cap U)$?", r"$\dim W+\dim U-\dim(W+U)$",
            [r"$\dim W+\dim U+\dim(W+U)$", r"$\dim W\cdot\dim U$", r"$\dim W+\dim U$"],
            r"הנוסחה הנכונה נותנת $2+2-3=1$; האחרות נותנות $7,\,4,\,4$."),
        num(r"בבסיס $\begin{pmatrix}1&2\\-1&1\end{pmatrix}$ של החיתוך: מהו האיבר בשורה 2 עמודה 1?", -1, r"$-1$."),
    ])

ENR[(5, "ד")] = dict(
    rubric=rub((r"הבנת התנאים של $W$: $b=-a$ והאיבר (1,2) שווה $2a$", 2),
               (r"בחירת מטריצה שמפרה את התנאי, $\begin{pmatrix}1&1\\1&1\end{pmatrix}$", 2),
               (r"הצדקה: $2a=2\neq1$", 1)),
    pitfalls=[r"לבחור מטריצה שמקיימת את התנאים כמו $\begin{pmatrix}0&0\\0&0\end{pmatrix}$."],
    steps=[
        cho(r"איזו מטריצה אינה שייכת ל-$W$?", r"$\begin{pmatrix}1&1\\1&1\end{pmatrix}$",
            [r"$\begin{pmatrix}1&2\\-1&5\end{pmatrix}$", r"$\begin{pmatrix}0&0\\0&3\end{pmatrix}$", r"$\begin{pmatrix}2&4\\-2&0\end{pmatrix}$"],
            r"$W$ מכילה מטריצות מהצורה $\begin{pmatrix}a&2a\\-a&c\end{pmatrix}$. שלוש האחרות מהצורה הזאת ($a=1,0,2$)."),
        num(r"עבור $\begin{pmatrix}1&1\\1&1\end{pmatrix}$, מהו $a+b$ (ב-$W$ חייב להיות $a+b=0$)?", 2, r"$1+1=2\neq0$."),
    ])

ENR[(6, "א")] = dict(
    rubric=rub((r"המערכת $a+b=0$, $b+c=0$, $b+d=0$", 2),
               (r"דירוג וקבלת דרגה 3", 2),
               (r"פתרון עם המשתנה החופשי $d=t$: $(t,-t,t,t)$", 2),
               (r"בסיס $\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ וממד 1", 1)),
    pitfalls=[r"טעות סימן בפתרון: $b=-d$.",
              r"לשכוח שהגרעין כולל את כל הכפולות של מטריצת הבסיס."],
    steps=[
        num(r"מהי דרגת מטריצת המקדמים של המערכת?", 3, r"שלוש משוואות בלתי תלויות."),
        num(r"מהו המימד של $\mathrm{Ker}\,T$?", 1, r"$4-3=1$."),
        cho(r"איזו מטריצה שייכת ל-$\mathrm{Ker}\,T$?", r"$\begin{pmatrix}1&-1\\1&1\end{pmatrix}$",
            [r"$\begin{pmatrix}1&1\\1&1\end{pmatrix}$", r"$\begin{pmatrix}1&0\\0&1\end{pmatrix}$", r"$\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$"],
            r"$T\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a+b,\,b+c,\,b+d)$. למטריצה הנכונה $(0,0,0)$; לאחרות $(2,2,2)$, $(1,0,1)$, $(0,0,-2)$."),
        num(r"בפתרון $(a,b,c,d)=(t,-t,t,t)$: מהו $b$ כאשר $t=2$?", -2, r"$b=-t=-2$."),
    ])

ENR[(6, "ב")] = dict(
    rubric=rub((r"משפט המימדים: $\dim\mathrm{Im}(T)=4-1=3$", 3),
               (r"$\mathrm{Im}(T)\subseteq\mathbb{R}^3$ וממדו 3, ולכן שווה ל-$\mathbb{R}^3$", 2),
               (r"בסיס סטנדרטי של $\mathbb{R}^3$", 2)),
    pitfalls=[r"לרשום $\dim\mathrm{Im}(T)=4$ (ממד המרחב כולו) במקום להחסיר את הגרעין.",
              r"לבחור בסיס שאינו בסיס של $\mathbb{R}^3$ (וקטורים תלויים)."],
    steps=[
        num(r"מהו $\dim\mathrm{Im}(T)$?", 3, r"$\dim M_{2\times2}-\dim\mathrm{Ker}(T)=4-1$."),
        cho(r"מדוע $\mathrm{Im}(T)=\mathbb{R}^3$?", r"כי $\mathrm{Im}(T)$ תת-מרחב של $\mathbb{R}^3$ שממדו 3, כממד $\mathbb{R}^3$",
            [r"כי $\dim\mathrm{Im}(T)=\dim M_{2\times2}=4$", r"כי $\mathrm{Ker}(T)=\{0\}$", r"כי $T$ חד-חד-ערכית"],
            r"$\dim\mathrm{Im}(T)=3$ ולא 4; הגרעין אינו טריוויאלי (ממדו 1) ולכן $T$ אינה חח״ע."),
        num(r"מהו הרכיב השני של $T\begin{pmatrix}0&1\\0&0\end{pmatrix}$ (כלומר $b+c$ עבור $b=1$)?", 1, r"$T\begin{pmatrix}0&1\\0&0\end{pmatrix}=(1,1,1)$."),
    ])

ENR[(6, "ג")] = dict(
    rubric=rub((r"$T$ חח״ע אם ורק אם הגרעין טריוויאלי", 1),
               (r"הגרעין אינו טריוויאלי ולכן $T$ אינה חח״ע", 2),
               (r"$T$ על אם ורק אם $\dim\mathrm{Im}(T)=\dim\mathbb{R}^3$", 1),
               (r"$\dim\mathrm{Im}(T)=3$ ולכן $T$ על", 1)),
    pitfalls=[r"להסיק מכך שהתמונה כל $\mathbb{R}^3$ שגם החח״ע מתקיימת."],
    steps=[
        cho(r"האם $T$ חד-חד-ערכית ו/או על?", r"אינה חח״ע אך על",
            [r"חח״ע ועל", r"חח״ע אך לא על", r"אינה חח״ע ואינה על"],
            r"הגרעין ממדו 1 (לא חח״ע) והתמונה ממדה 3, כממד $\mathbb{R}^3$ (על)."),
        num(r"מהו $\dim\mathrm{Ker}(T)$?", 1, r"מהסעיף א׳."),
    ])

ENR[(6, "ד")] = dict(
    rubric=rub((r"המשוואות $a+b=1$, $b+c=1$, $b+d=1$ ודירוגן", 3),
               (r"הצורה הכללית $\begin{pmatrix}d&1-d\\d&d\end{pmatrix}$", 1),
               (r"מטריצת האפס אינה בקבוצה (כי $T(0)=\vec 0$) ולכן הקבוצה אינה תת-מרחב", 2)),
    pitfalls=[r"לטעות בכיוון: המקורות של $(1,1,1)$ אינם הגרעין.",
              r"להסיק שזהו תת-מרחב כי $T$ לינארית."],
    steps=[
        num(r"בפתרון $\begin{pmatrix}d&1-d\\d&d\end{pmatrix}$: מהו $b$ כאשר $d=2$?", -1, r"$b=1-d=-1$."),
        num(r"באותו פתרון: מהו $c$ כאשר $d=2$?", 2, r"$c=d=2$."),
        cho(r"האם הקבוצה היא תת-מרחב של $\mathbb{R}^{2\times2}$?", r"לא, כי מטריצת האפס אינה בה ($T(0)=\vec 0\neq(1,1,1)$)",
            [r"כן, כי $T$ לינארית", r"כן, כי היא מכילה את הגרעין של $T$", r"לא, כי הקבוצה ריקה"],
            r"איברי הגרעין נשלחים ל-$\vec 0$ ולא ל-$(1,1,1)$, ולכן אינם בקבוצה; הקבוצה אינה ריקה (למשל $d=0$); ולינאריות $T$ אינה הופכת מקור של וקטור שונה מאפס לתת-מרחב."),
    ])

ENR[(1, "ד")] = dict(
    rubric=rub((r"הוצאת $z$ כגורם משותף: $z=0$ או $z^2=4-3i$", 2),
               (r"הצבת $(a+ib)^2=4-3i$ ופירוק למערכת $a^2-b^2=4,\ 2ab=-3$", 2),
               (r"פתרון המערכת: $a=\pm\frac{3}{\sqrt2},\ b=\mp\frac{1}{\sqrt2}$", 1),
               (r"שלושת הפתרונות $z=0,\ \pm\frac{3-i}{\sqrt2}$", 1)),
    pitfalls=[r"לחלק את המשוואה ב-$z$ ולאבד את הפתרון $z=0$.",
              r"לשכוח את הסימן $\pm$ של השורש הריבועי ולהסתפק בפתרון אחד של $z^2=4-3i$."],
    steps=[
        cho(r"מהו הצעד הראשון הנכון בפתרון $z^3+(3i-4)z=0$?", r"להוציא $z$ כגורם משותף ולקבל $z\left(z^2+3i-4\right)=0$",
            [r"לחלק ב-$z$ ולהמשיך רק עם $z^2=4-3i$", r"להעביר אגף ולקחת שורש שלישי של $(4-3i)z$", r"להציב $z=a+ib$ ולפתוח את החזקה השלישית בלבד"],
            r"חלוקה ב-$z$ מאבדת את הפתרון $z=0$ (הוא אכן פתרון). אגף ימין $(4-3i)z$ אינו קבוע, ולכן אי אפשר לקחת שורש שלישי. הצבה ישירה של $z=a+ib$ אפשרית אבל מסורבלת; פירוק לגורמים מפשט."),
        num(r"מהו המודול של $4-3i$?", 5, r"$\sqrt{16+9}=5$, ומכאן $a^2+b^2=5$."),
        num(r"מהו החלק הממשי החיובי של השורש $\sqrt{4-3i}$? (עגלו לשלוש ספרות אחרי הנקודה)", 2.121, r"$a^2=\frac{5+4}{2}=\frac92$, ולכן $a=\frac{3}{\sqrt2}\approx2.121$.", 0.001),
        num(r"מהו החלק המדומה של השורש בעל החלק הממשי החיובי? (עגלו לשלוש ספרות אחרי הנקודה)", -0.707, r"$b=\frac{-3}{2a}=-\frac{1}{\sqrt2}\approx-0.707$.", 0.001),
    ])

for q in questions:
    if q.get("hold"):
        continue
    e = ENR.get((q["num"], q["part"]))
    assert e is not None, (q["num"], q["part"])
    if q.get("points") is not None:
        assert sum(r["points"] for r in e["rubric"]) == q["points"], (q["num"], q["part"])
    assert 2 <= len(e["steps"]) <= 5 and 1 <= len(e["pitfalls"]) <= 3 and 3 <= len(e["rubric"]) <= 5, (q["num"], q["part"])
    src = "ai-verified"  # Q1d refuted 2026-10-18 (_verify_20B-A_q1d.json)
    q.update(rubric=e["rubric"], rubricSource=src, pitfalls=e["pitfalls"], steps=e["steps"], stepsSource=src)


exam = {
    "examCode": "20B-A",
    "examLabel": "מבחן סוף סמסטר ב׳ תש״פ, מועד א׳ (18.06.2020)",
    "year": 2020,
    "examDate": "18.06.2020",
    "sourceFile": "20B-A exam + official solution (scanned PDF, 11pp)",
    "solutionFile": "20B-A exam + official solution (scanned PDF, 11pp)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
