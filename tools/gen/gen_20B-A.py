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
- Q1 d (z^3+(3i-4)z=0): the solution file has NO solution for it (it jumps from Q1 b to Q2). Held "no-key".
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

questions.append({"num": 1, "part": "ד", "kind": "computation", "topic": "complex_numbers", "points": 6,
                  "question": r"פתור את המשוואה מעל מספרים מרוכבים $z^3+(3i-4)z=0$.", "hold": "no-key"})

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
