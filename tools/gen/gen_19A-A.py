# -*- coding: utf-8 -*-
"""Generator for tools/raw/19A-A.json -- linear algebra, semester A 2019, moed A (13.02.2019), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_19A-A.py

Source: one PDF (8pp, mixed text + images): the exam text followed question by question by the typed official solution.
Six questions of 25 points (best 4 count), 23 items. No figures.

Transcription notes
- Q3 prints part a and part b with sub-items (i), (ii), (iii); in the raw schema the four items are a, b, g, d in printed order
  (a = EFGR, b = (i), g = (ii), d = (iii)).
- Q5 prints part a with sub-items (1), (2), then parts b and c; in the raw schema: a = (1), b = (2), g = old b, d = old c.
- Q3 a (final-answer error): the official calls G = swap, F = (R3+2R1), E = (R3-R2) and writes B = EFGR, but those are the
  reducing operations themselves (EFGB = R). B = EFGR needs the inverse operations. Shipped corrected, labeled, official:false.
- Q4 b (final-answer error): the official basis of W has the second element (0 1; 1 0), which is not in W (a+b-d = 1). The basis
  is {(1 0; 0 1), (0 1; 1 1)} (a=1,b=0 and a=0,b=1). Shipped corrected, labeled, official:false.
- Q4 g (slip in an intermediate line, no label): the official lists the W vectors as (1 0; 0 1), (0 1; 1 0) in the span and as
  row 5 of the matrix A; the same official solution uses (0 1; 1 1) in Q4 d. Written with (0 1; 1 1) throughout; the final
  basis B_2 and dim(U+W)=4 are unchanged.
- Q2 b: the exam text prints "מצא עבור אילו ערכי k קיימים אינסוף פתרונות, פתרון יחיד או אין לה פתרונות כלל" (no "למערכת").
- Q1: the exam text prints parts a, b, c as א, ב, ג.

Checks (sympy, tools/verify/19A-A/verify_19A-A.py): Q1 cross product, volume (a-2)(a-4), plane and distance, Q2 echelon rows and
the k classification, the k=1 and k=i solutions, Q3 elementary matrices (confirms the slip above), Q4 bases, dim(U+W)=4 and the
intersection (2 1; 1 3), Q5 det, inverse, B^2=I and det -30375, Q6 linearity, kernel, image. Mismatches found: the Q3 a and
Q4 b slips only.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19A-A.json"


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
           "text": J(r"נתונים שני ישרים כאשר $a$ הוא פרמטר ממשי:",
                     r"$$\begin{cases} l_1:\ (x,y,z)=(2,1,1)+s(2,-a,-5)\\ l_2:\ (x,y,z)=(1,2,2)+t(a,-2,-1)\end{cases}$$")},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת משוואות עם פרמטר",
           "text": J(r"נתונה מערכת משוואות ליניאריות:",
                     r"$$\begin{cases} x_1-x_2+x_3=-2\\ x_1+kx_2+x_3=k+1\\ kx_1+kx_2+x_3=2\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - המטריצה B",
           "text": r"נתונה המטריצה $B=" + pm("0&1&7&8", "1&3&3&8", "-2&-5&1&-8") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של מטריצות",
           "text": J(r"נתון מרחב וקטורי $V=M_{2\times2}(\mathbb{R})$ של מטריצות ריבועיות $2\times2$ ובו שתי הקבוצות:",
                     r"$$W=\left\{" + pm("a&b", "c&d") + r":\ b=c,\ a+b-d=0,\ a,b,c,d\in\mathbb{R}\right\}$$",
                     r"$$U=\mathrm{span}\left\{" + pm("1&0", "1&1") + "," + pm("0&1", "-1&-2") + "," + pm("0&0", "0&1") + r"\right\}$$")},
    "c5": {"kind": "text", "title": "שאלה 5 - המטריצה A",
           "text": r"תהיה נתונה מטריצה $A=" + pm("1&2a-1&2", "1&3&a", "1&3a-1&5") + r"$."},
    "c6": {"kind": "text", "title": "שאלה 6 - ההעתקה T",
           "text": J(r"יהי $V=\mathbb{R}_3[x]$ מרחב וקטורי של פולינומים ממעלה 3 או קטנה מ-3. תהיה $T:V\to V$ ההעתקה המוגדרת לפי הנוסחה",
                     r"$$T\left(a+bx+cx^2+dx^3\right)=(a-2c+d)+(b+2c-a-d)x^2+bx^3$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "computation", "lines_planes",
    r"חשב את ערך הפרמטר $a$ כך שהישרים $l_1,l_2$ נחתכים.",
    J(r"לא קיים ערך $a$ עבורו $\frac{2}{a}=\frac{-a}{-2}=\frac{-5}{-1}$ ולכן וקטורי הכיוון בהכרח לא מקבילים. מכאן שהישרים נחתכים או מצטלבים בלבד. ניעזר בנפח המקבילון כדי לסווג.",
      r"$$\overrightarrow{P_1P_2}=(-1,1,1);\qquad\vec m_1\times\vec m_2=\begin{vmatrix}\vec i&\vec j&\vec k\\2&-a&-5\\a&-2&-1\end{vmatrix}=\left(a-10,\ -(-2+5a),\ -4+a^2\right)$$",
      r"$$V=\overrightarrow{P_1P_2}\cdot\left(\vec m_1\times\vec m_2\right)=(-1,1,1)\cdot\left(a-10,\ 2-5a,\ -4+a^2\right)=-a+10+2-5a-4+a^2=a^2-6a+8=(a-2)(a-4)$$",
      r"הישרים נחתכים כאשר $V=0$ וגם $\vec m_1\nparallel\vec m_2$. מכאן שהישרים נחתכים עבור **$a=2,4$**."),
    6, contextId="c1"))

questions.append(Q(
    1, "ב", "computation", "lines_planes",
    r"עבור $a=2$ מצא את המישור המכיל את שני הישרים $l_1,l_2$.",
    J(r"עבור $a=2$ הישרים נחתכים. הנורמל למישור מאונך לוקטורי הכיוון של הישרים. ע״י הצבה במכפלה הוקטורית שחושבה בסעיף א׳ מתקבל: $\vec n=\vec m_1\times\vec m_2=(-8,-8,0)$. מכאן שהמישור יהיה מהצורה $-8x-8y+D=0$.",
      r"ע״י הצבת הנקודה $(2,1,1)$ מ-$l_1$ (שבוודאי נמצאת במישור) מתקבל $D=24$. משוואת המישור:",
      r"$$-8x-8y+24=0$$"),
    6, contextId="c1"))

questions.append(Q(
    1, "ג", "computation", "lines_planes",
    r"עבור $a=0$ הראה הישרים $l_1,l_2$ מצטלבים וחשב את המרחק בין הישרים.",
    J(r"עבור $a=0$ מתקיים $V\neq0$ (סעיף א׳) וגם $\vec m_1\nparallel\vec m_2$ ולכן הישרים מצטלבים. המרחק בין ישרים מצטלבים שווה לגובה המקבילון שהם יוצרים.",
      r"$$d(a=0)=\frac{|V|}{\left\|\vec m_1\times\vec m_2\right\|}=\frac{|(0-2)(0-4)|}{\|(-10,2,-4)\|}=\frac{8}{\sqrt{(-10)^2+2^2+(-4)^2}}=\frac{8}{\sqrt{120}}$$"),
    13, contextId="c1"))

# ------------------------------------------------------------------ Q2
R0 = [["1", "-1", "1", "-2"], ["1", "k", "1", "k+1"], ["k", "k", "1", "2"]]
R1 = [["1", "-1", "1", "-2"], ["0", "k+1", "0", "k+3"], ["0", "2k", "1-k", "2+2k"]]
R2 = [["1", "-1", "1", "-2"], ["0", "2", "k-1", "4"], ["0", "2k", "1-k", "2+2k"]]
R3 = [["1", "-1", "1", "-2"], ["0", "2", "k-1", "4"], ["0", "0", "-k^2+1", "2-2k"]]
R4 = [["1", "-1", "1", "-2"], ["0", "2", "k-1", "4"], ["0", "0", "(1-k)(1+k)", "2(1-k)"]]
questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"הבא את מטריצת המקדמים המורחבת לצורה מדורגת.",
    J(r"נרשום במטריצה ונדרג.",
      "$$" + aug(R0, 3) + arrow(r"\substack{R_2\to R_2-R_1\\R_3\to R_3-kR_1}") + aug(R1, 3) + arrow(r"R_2\to2R_2-R_3") + aug(R2, 3) + "$$",
      "$$" + arrow(r"R_3\to R_3-kR_2") + aug(R3, 3) + r"\longrightarrow" + aug(R4, 3) + "$$"),
    6, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"בהנחה ש-$k$ פרמטר ממשי. מצא עבור אילו ערכי $k$ קיימים אינסוף פתרונות, פתרון יחיד או אין לה פתרונות כלל.",
    J(r"פתרון יחיד: $k\neq1,-1$.",
      r"אינסוף פתרונות: $k=1$.",
      r"אין פתרון: $k=-1$."),
    6, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור $k=1$ מצא את הפתרונות של המערכת.",
    J(r"נציב $k=1$ במטריצה המדורגת.",
      "$$" + aug([["1", "-1", "1", "-2"], ["0", "2", "0", "4"], ["0", "0", "0", "0"]], 3)
      + r"\to\begin{cases}x=-t\\y=2\\z=t\end{cases}\to" + pm("x", "y", "z") + "=" + pm("0", "2", "0") + "+t" + pm("-1", "0", "1") + "$$"),
    8, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "linear_systems",
    r"עבור $k=i$ מצא את הפתרונות המרוכבים של המערכת.",
    J(r"נציב $k=i$ במטריצה המדורגת.",
      "$$" + aug([["1", "-1", "1", "-2"], ["0", "2", "i-1", "4"], ["0", "0", "2", "2-2i"]], 3)
      + r"\to\begin{cases}x-(2-i)+1-i=-2\ \to\ x=-1\\2y+(i-1)(1-i)=4\ \to\ y=2-i\\z=1-i\end{cases}\to" + pm("x", "y", "z") + "=" + pm("-1", "2-i", "1-i") + "$$"),
    5, contextId="c2"))

# ------------------------------------------------------------------ Q3
B0 = [["0", "1", "7", "8"], ["1", "3", "3", "8"], ["-2", "-5", "1", "-8"]]
B1 = [["1", "3", "3", "8"], ["0", "1", "7", "8"], ["-2", "-5", "1", "-8"]]
B2 = [["1", "3", "3", "8"], ["0", "1", "7", "8"], ["0", "1", "7", "8"]]
B3 = [["1", "3", "3", "8"], ["0", "1", "7", "8"], ["0", "0", "0", "0"]]
questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הצג את המטריצה $B$ בצורה $B=EFGR$ כאשר $E$, $F$ ו-$G$ הן מטריצות אלמנטאריות ו-$R$ - מטריצה בצורה מדורגת.",
    J(FIX + r"בפתרון הרשמי נרשמות כ-$G$, $F$, $E$ מטריצות פעולות השורה עצמן, ונכתב $B=EFGR$. אך עבורן מתקבל $EFGB=R$ ולא $B=EFGR$. כדי לקבל $B=EFGR$ יש לקחת את המטריצות האלמנטאריות ההפוכות, וזה מה שרשום להלן.",
      "$$B=" + pm("0&1&7&8", "1&3&3&8", "-2&-5&1&-8") + r"\xrightarrow{R_1\leftrightarrow R_2}" + pm("1&3&3&8", "0&1&7&8", "-2&-5&1&-8")
      + r"\xrightarrow{R_3\to R_3+2R_1}" + pm("1&3&3&8", "0&1&7&8", "0&1&7&8") + r"\xrightarrow{R_3\to R_3-R_2}" + pm("1&3&3&8", "0&1&7&8", "0&0&0&0") + "$$",
      r"מכאן נובע ש-$B=EFGR$ כאשר",
      "$$E=" + pm("0&1&0", "1&0&0", "0&0&1") + ",\\ F=" + pm("1&0&0", "0&1&0", "-2&0&1") + ",\\ G=" + pm("1&0&0", "0&1&0", "0&1&1") + "$$",
      r"ו-",
      "$$R=" + pm("1&3&3&8", "0&1&7&8", "0&0&0&0") + "$$"),
    10, contextId="c3", solutionSource="solved", official=False))

questions.append(Q(
    3, "ב", "proof", "eigen_diagonalization",
    r"הוכח שאם $\mathbf{x}$ הוא וקטור עצמי של $A$, אז כל וקטור $c\mathbf{x}$ ($c\neq0$) גם וקטור עצמי של $A$.",
    J(r"אם $\mathbf{x}$ הוא וקטור עצמי של $A$, אז $A\mathbf{x}=\lambda\mathbf{x}$. לכן",
      r"$$A(c\mathbf{x})=c(A\mathbf{x})=c\lambda\mathbf{x}=\lambda(c\mathbf{x})$$"),
    5))

questions.append(Q(
    3, "ג", "proof", "eigen_diagonalization",
    r"הוכח שאם $\mathbf{v}$ ו-$\mathbf{w}$ הם וקטורים עצמיים המתאימים אל אותו ערך עצמי, אז כל צירוף ליניארי $c\mathbf{v}+d\mathbf{w}$ ($c\neq0,\ d\neq0$) גם מהווה וקטור עצמי של $A$.",
    J(r"אם $\mathbf{v}$ ו-$\mathbf{w}$ הם וקטורים עצמיים המתאימים אל אותו ערך עצמי, אז",
      r"$$\begin{cases}A\mathbf{v}=\lambda\mathbf{v}\\A\mathbf{w}=\lambda\mathbf{w}\end{cases}$$",
      r"לכן נקבל שמתקיים",
      r"$$A(c\mathbf{v}+d\mathbf{w})=c(A\mathbf{v})+d(A\mathbf{w})=c\lambda\mathbf{v}+d\lambda\mathbf{w}=\lambda(c\mathbf{v}+d\mathbf{w})$$"),
    5))

questions.append(Q(
    3, "ד", "proof", "eigen_diagonalization",
    r"הוכח שאם $\mathbf{v}$ ו-$\mathbf{w}$ הם וקטורים עצמיים המתאימים לערכים העצמיים השונים, אז כל צירוף ליניארי $c\mathbf{v}+d\mathbf{w}$ ($c\neq0,\ d\neq0$) אינו וקטור עצמי של $A$.",
    J(r"אם $\mathbf{v}$ ו-$\mathbf{w}$ הם וקטורים עצמיים המתאימים לערכים העצמיים השונים, אז",
      r"$$\begin{cases}A\mathbf{v}=\lambda_1\mathbf{v}\\A\mathbf{w}=\lambda_2\mathbf{w}\end{cases}$$",
      r"ולכן",
      r"$$A(c\mathbf{v}+d\mathbf{w})=c(A\mathbf{v})+d(A\mathbf{w})=c\lambda_1\mathbf{v}+d\lambda_2\mathbf{w}\neq\lambda(c\mathbf{v}+d\mathbf{w})$$"),
    5))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "proof", "vector_spaces",
    r"הוכח כי $W$ היא תת מרחב של מרחב וקטורי $M_{2\times2}(\mathbb{R})$.",
    J(r"ברור ש-$W$ אינה ריקה כי מכילה בתוכה מטריצת אפס. בנוסף לזאת, אם $A_1=" + pm("a_1&b_1", "b_1&a_1+b_1") + r"\in W$ ו-$A_2=" + pm("a_2&b_2", "b_2&a_2+b_2") + r"\in W$, אז",
      r"$$W=\left\{" + pm("a&b", "c&d") + r":\ b=c,\ a+b-d=0\right\}=\left\{" + pm("a&b", "b&a+b") + r"\right\}$$",
      r"$$A_1+A_2=" + pm("a_1&b_1", "b_1&a_1+b_1") + "+" + pm("a_2&b_2", "b_2&a_2+b_2") + "=" + pm("a_1+a_2&b_1+b_2", "b_1+b_2&a_1+b_1+a_2+b_2") + r"\in W$$",
      r"$$kA_1=k" + pm("a_1&b_1", "b_1&a_1+b_1") + "=" + pm("ka_1&kb_1", "kb_1&k(a_1+b_1)") + r"\in W$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"מצא את הבסיס ואת המימד של $W$.",
    J(FIX + r"בפתרון הרשמי הוקטור השני של הבסיס רשום $" + pm("0&1", "1&0") + r"$, אך מטריצה זו אינה שייכת ל-$W$ (עבורה $a+b-d=0+1-0=1\neq0$). בסיס נכון מתקבל מהצורה $" + pm("a&b", "b&a+b") + r"$ עבור $a=1,b=0$ ועבור $a=0,b=1$:",
      r"$$B_1=\left\{" + pm("1&0", "0&1") + "," + pm("0&1", "1&1") + r"\right\},\qquad\dim W=2$$"),
    6, contextId="c4", solutionSource="solved", official=False))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצא את הבסיס ואת המימד של $U+W$.",
    J(r"נמצא בסיס עבור $U+W$:",
      r"$$U+W=\mathrm{Span}\left\{" + pm("1&0", "1&1") + "," + pm("0&1", "-1&-2") + "," + pm("0&0", "0&1") + "," + pm("1&0", "0&1") + "," + pm("0&1", "1&1") + r"\right\}$$",
      r"אם נתאים לכל מטריצה ($2\times2$) בפרישה הזאת וקטור עמודה ולאחר מכן נבנה מטריצה בה הוקטורים האלה יהיו כשורות אז נקבל: $A=" + pm("1&0&1&1", "0&1&-1&-2", "0&0&0&1", "1&0&0&1", "0&1&1&1") + r"$.",
      r"אחרי תהליך הדירוג מטריצה מתקבלת בצורה $" + pm("1&0&1&1", "0&1&-1&-2", "0&0&-1&0", "0&0&0&1", "0&0&0&0") + r"$ והשורות השונות בשורות האפסים מתאימות לשורות המקוריות של מטריצה $A$ והן יוצרות בסיס עבור הסכום. כלומר:",
      r"$$\dim(U+W)=4$$",
      r"בסיס של $U+W$:",
      r"$$B_2=\left\{" + pm("1&0", "1&1") + "," + pm("0&1", "-1&-2") + "," + pm("0&0", "0&1") + "," + pm("1&0", "0&1") + r"\right\}$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"מצא את הבסיס ואת המימד של $U\cap W$.",
    J(r"אם $\mathbf{v}\in U\cap W$, אז ניתן להציגו בשתי צורות שקולות",
      r"$$\mathbf{v}=c_1" + pm("1", "0", "1", "1") + "+c_2" + pm("0", "1", "-1", "-2") + "+c_3" + pm("0", "0", "0", "1") + "=d_1" + pm("1", "0", "0", "1") + "+d_2" + pm("0", "1", "1", "1") + "$$",
      r"$$c_1" + pm("1", "0", "1", "1") + "+c_2" + pm("0", "1", "-1", "-2") + "+c_3" + pm("0", "0", "0", "1") + "+d_1" + pm("-1", "0", "0", "-1") + "+d_2" + pm("0", "-1", "-1", "-1") + "=" + pm("0", "0", "0", "0") + "$$",
      "$$" + aug([["1", "0", "0", "-1", "0"], ["0", "1", "0", "0", "-1"], ["1", "-1", "0", "0", "-1"], ["1", "-2", "1", "-1", "-1"]], 4)
      + arrow(r"\substack{R_3\to R_3-R_1\\R_4\to R_4-R_1}") + aug([["1", "0", "0", "-1", "0"], ["0", "1", "0", "0", "-1"], ["0", "-1", "0", "1", "-1"], ["0", "-2", "1", "0", "-1"]], 4) + "$$",
      "$$" + arrow(r"\substack{R_3\to R_3+R_2\\R_4\to R_4+2R_2}") + aug([["1", "0", "0", "-1", "0"], ["0", "1", "0", "0", "-1"], ["0", "0", "0", "1", "-2"], ["0", "0", "1", "0", "-3"]], 4)
      + arrow(r"R_3\leftrightarrow R_4") + aug([["1", "0", "0", "0", "-2"], ["0", "1", "0", "0", "-1"], ["0", "0", "1", "0", "-3"], ["0", "0", "0", "1", "-2"]], 4) + "$$",
      r"$$d_2=1\Rightarrow d_1=2\Rightarrow\mathbf{v}=d_1" + pm("1&0", "0&1") + "+d_2" + pm("0&1", "1&1") + "=" + pm("2&0", "0&2") + "+" + pm("0&1", "1&1") + "=" + pm("2&1", "1&3") + "$$",
      r"ולכן $B_3=\left\{" + pm("2&1", "1&3") + r"\right\}$ הוא בסיס של $U\cap W$, $\dim(U\cap W)=1$."),
    7, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "determinants",
    r"עבור אילו ערכי $a$ מטריצה $A$ היא הפיכה?",
    J(r"נחשב את $\det(A)$.",
      r"$$\det(A)=\begin{vmatrix}1&2a-1&2\\1&3&a\\1&3a-1&5\end{vmatrix}=-\left(a^2+4a-12\right)$$",
      r"כאשר $\det(A)=0$. מכאן $a=-6$ או $a=2$ ולכן $A$ תהיה הפיכה רק כאשר $a\neq-6,2$."),
    5, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "rank_inverse",
    r"חשב $A^{-1}$ עבור $a=1$.",
    J(r"אם $a=1$, אז $A=" + pm("1&1&2", "1&3&1", "1&2&5") + r"$ ו-$\det(A)=-\left(a^2+4a-12\right)=7$. מכיוון ש-$\det(A)\neq0$, ניתן לחשב כל המשלימים האלגבריים וכתוצאה מכך $A^{-1}=\frac{1}{\det(A)}C^T$,",
      r"$$A^{-1}=\frac{1}{7}" + pm("13&-1&-5", "-4&3&1", "-1&-1&2") + "$$"),
    7, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "matrix_algebra",
    r"מצא מטריצה $B\neq\pm I$, $B\in M_{2\times2}(\mathbb{R})$, המקיימת $B^2=I$.",
    J(r"נסמן $B=" + pm("b_{11}&b_{12}", "b_{21}&b_{22}") + r"$. אז",
      r"$$B^2=" + pm("b_{11}&b_{12}", "b_{21}&b_{22}") + pm("b_{11}&b_{12}", "b_{21}&b_{22}") + "=" + pm("b_{11}^2+b_{12}b_{21}&b_{11}b_{12}+b_{12}b_{22}", "b_{11}b_{21}+b_{22}b_{21}&b_{21}b_{12}+b_{22}^2") + "=" + pm("1&0", "0&1") + "$$",
      r"מכאן נקבל שתי אופציות עבור מטריצה כזאת $\neq I$: $B=" + pm("-1&0", "0&1") + r"\neq\pm I$ או $B=" + pm("1&0", "0&-1") + r"\neq\pm I$. יש לציין שקיימות אופציות נוספות."),
    8, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "determinants",
    r"נתונות מטריצות ריבועיות ($5\times5$) $B$ ו-$C$ המקיימות $\det(B)=-5$ ו-$\det(C)=2$. חשב את $\det\left(3B^2C^TC^{-1}B^T\right)$.",
    J(r"$$\det\left(3B^2C^TC^{-1}B^T\right)=\det\left(3B^2\right)\det\left(C^T\right)\det\left(C^{-1}\right)\det\left(B^T\right)=$$",
      r"$$=\det(3BB)\det\left(C^T\right)\det\left(C^{-1}\right)\det\left(B^T\right)=$$",
      r"$$=\det(3B)\det(B)\det\left(C^T\right)\det\left(C^{-1}\right)\det\left(B^T\right)=3^5\cdot(-5)\cdot(-5)\cdot2\cdot\frac{1}{2}\cdot(-5)=-30375$$"),
    5))

# ------------------------------------------------------------------ Q6
questions.append(Q(
    6, "א", "proof", "linear_maps",
    r"הוכח ש-$T$ היא העתקה ליניארית.",
    J(r"אם $p_1(x)=a_1+b_1x+c_1x^2+d_1x^3\in\mathbb{R}_3[x]$ ו-$p_2(x)=a_2+b_2x+c_2x^2+d_2x^3\in\mathbb{R}_3[x]$, אז",
      r"$$T\left(p_1(x)+p_2(x)\right)=\left(a_1-2c_1+d_1\right)+\left(a_2-2c_2+d_2\right)+\left(b_1+2c_1-a_1-d_1\right)x^2+\left(b_2+2c_2-a_2-d_2\right)x^2+b_1x^3+b_2x^3=T\left(p_1(x)\right)+T\left(p_2(x)\right)$$",
      r"וגם",
      r"$$T\left(kp_1(x)\right)=k\left(a-2c+d\right)+k\left(b+2c-a-d\right)x^2+kbx^3=kT\left(p_1(x)\right)$$"),
    6, contextId="c6"))

questions.append(Q(
    6, "ב", "computation", "linear_maps",
    r"חשב $\dim(\ker(T))$ וגם $\ker(T)$.",
    J(r"אם $p_1(x)=a_1+b_1x+c_1x^2+d_1x^3\in\ker(T)$, אז $T\left(p_1(x)\right)=0$ ולכן",
      r"$$\begin{cases}a_1-2c_1+d_1=0\\b_1+2c_1-a_1-d_1=0\\b_1=0\end{cases}$$",
      r"הבסיס הסטנדרטי של $\mathbb{R}_3[x]$ הוא $\left\{1,x,x^2,x^3\right\}$ ולכל פולינום $p(x)=a+bx+cx^2+dx^3\in\mathbb{R}_3[x]$ מתאים וקטור הקואורדינאטות ביחס לבסיס זה בצורה $" + pm("a", "b", "c", "d") + r"$. מהמשוואות שהתקבלו נובע שאם $p_1(x)=a_1+b_1x+c_1x^2+d_1x^3\in\ker(T)$, אז",
      r"$$\begin{cases}a_1=2c_1-d_1=2s-t\\b_1=0\\c_1=s\\d_1=t\end{cases}$$",
      r"מכאן נובע ש-",
      r"$$" + pm("a_1", "b_1", "c_1", "d_1") + "=" + pm("2s-t", "0", "s", "t") + "=s" + pm("2", "0", "1", "0") + "+t" + pm("-1", "0", "0", "1") + r"\Leftarrow\ker(T)=\mathrm{sp}\left\{2+x^2,\ -1+x^3\right\}$$",
      r"ו-$\dim(\ker(T))=2$."),
    8, contextId="c6"))

questions.append(Q(
    6, "ג", "computation", "linear_maps",
    r"חשב $\mathrm{Im}(T)$ ($\mathrm{range}(T)$) וגם $\dim(\mathrm{range}(T))$ ($\dim(\mathrm{Im}(T))$).",
    J(r"מכיוון ש-$T\left(a+bx+cx^2+dx^3\right)=(a-2c+d)+(b+2c-a-d)x^2+bx^3$, אז עם וקטור הקואורדינאטות $q(x)\in\mathrm{Im}(T)$ וכתוצאה מכך נקבל ש-",
      r"$$" + pm("a-2c+d", "0", "b+2c-a-d", "b") + "=a" + pm("1", "0", "-1", "0") + "+b" + pm("0", "0", "1", "1") + "+c" + pm("-2", "0", "2", "0") + "+d" + pm("1", "0", "-1", "0") + "$$",
      r"$$\mathrm{Im}(T)=\mathrm{sp}\left\{" + pm("1", "0", "-1", "0") + "," + pm("0", "0", "1", "1") + "," + pm("-2", "0", "2", "0") + "," + pm("1", "0", "-1", "0") + r"\right\}$$",
      r"ברור שהוקטורים הראשון, השלישי והרביעי תלויים ליניארית ולכן הבסיס של הטווח נקבע כ-",
      r"$$\mathrm{Im}(T)=\mathrm{sp}\left\{" + pm("1", "0", "-1", "0") + "," + pm("0", "0", "1", "1") + r"\right\}=\mathrm{sp}\left\{1-x^2,\ x^2+x^3\right\}$$",
      r"והמימד שלו הוא 2."),
    8, contextId="c6"))

questions.append(Q(
    6, "ד", "computation", "linear_maps",
    r"האם $T$ היא העתקה חד-חד-ערכית? נמק!",
    J(r"ההעתקה $T$ איננה חד-חד-ערכית מכיוון שהגרעין שלה שונה מ-$\{\mathbf{0}\}$.",
      r"**הערה:** ניתן לקבל בסיסים שונים של הגרעין והטווח."),
    3, contextId="c6"))

exam = {
    "examCode": "19A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תשע״ט, מועד א׳ (13.02.2019)",
    "year": 2019,
    "examDate": "13.02.2019",
    "sourceFile": "19A-A exam + official solution (PDF, 8pp)",
    "solutionFile": "19A-A exam + official solution (PDF, 8pp)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
