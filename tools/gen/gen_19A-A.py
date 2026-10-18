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
    rubric=rub((r"הראה שוקטורי הכיוון אינם מקבילים לכל $a$", 1),
               (r"חישוב $\overrightarrow{P_1P_2}=(-1,1,1)$ והמכפלה הווקטורית $\vec m_1\times\vec m_2$", 2),
               (r"נפח המקבילון $V=(a-2)(a-4)$", 2),
               (r"מסקנה: $V=0$ עבור $a=2,4$", 1)),
    pitfalls=[r"לשכוח לבדוק שהכיוונים אינם מקבילים לפני שמסיקים חיתוך מ-$V=0$.",
              r"טעות סימן ברכיב $j$ של המכפלה הווקטורית."],
    steps=[
        cho(r"מהו התנאי לכך שהישרים נחתכים (כשהכיוונים אינם מקבילים)?", r"$V=\overrightarrow{P_1P_2}\cdot\left(\vec m_1\times\vec m_2\right)=0$",
            [r"$V\neq0$", r"$\vec m_1\cdot\vec m_2=0$", r"$\vec m_1\times\vec m_2=\vec 0$"],
            r"ב-$a=2$ הישרים נחתכים, ושם $V=0$, $\vec m_1\cdot\vec m_2=13\neq0$ ו-$\vec m_1\times\vec m_2\neq\vec 0$. $V\neq0$ פירושו ישרים מצטלבים."),
        num(r"מהו $V=(a-2)(a-4)$ עבור $a=0$?", 8, r"$(-2)(-4)=8$."),
        num(r"מהו $V$ עבור $a=3$?", -1, r"$(1)(-1)=-1\neq0$, ולכן אין חיתוך."),
        num(r"מהו הרכיב הראשון של $\vec m_1\times\vec m_2=(a-10,\ 2-5a,\ a^2-4)$ עבור $a=0$?", -10, r"$a-10=-10$."),
    ])

ENR[(1, "ב")] = dict(
    rubric=rub((r"עבור $a=2$ הישרים נחתכים ולכן קיים מישור המכיל אותם", 2),
               (r"וקטור נורמלי $\vec n=\vec m_1\times\vec m_2=(-8,-8,0)$", 2),
               (r"הצבת הנקודה $(2,1,1)$ וקבלת $D=24$ ומשוואת המישור", 2)),
    pitfalls=[r"לקחת את אחד מוקטורי הכיוון בתור וקטור נורמלי.",
              r"להציב נקודה שאינה על הישר ולקבל קבוע $D$ שגוי."],
    steps=[
        cho(r"מהו וקטור נורמלי למישור המכיל את שני הישרים?", r"$\vec m_1\times\vec m_2$, כי הוא ניצב לשני וקטורי הכיוון",
            [r"$\vec m_1$", r"$\overrightarrow{P_1P_2}$", r"$\vec m_1+\vec m_2$"],
            r"עבור $a=2$ הווקטורים $\vec m_1=(2,-2,-5)$, $\overrightarrow{P_1P_2}=(-1,1,1)$ ו-$\vec m_1+\vec m_2=(4,-4,-6)$ אינם ניצבים ל-$\vec m_1$ (המכפלות הסקלריות $18,\ -9,\ 42$)."),
        num(r"מהו הרכיב הראשון של $\vec n=\vec m_1\times\vec m_2$ עבור $a=2$?", -8, r"$a-10=-8$."),
        num(r"המישור $-8x-8y+D=0$ עובר דרך $(2,1,1)$. מהו $D$?", 24, r"$-16-8+D=0$."),
    ])

ENR[(1, "ג")] = dict(
    rubric=rub((r"$V\neq0$ וגם הכיוונים אינם מקבילים, ולכן הישרים מצטלבים", 3),
               (r"המכפלה הווקטורית $(-10,2,-4)$ ונורמה $\sqrt{120}$", 3),
               (r"הנוסחה $d=\frac{|V|}{\|\vec m_1\times\vec m_2\|}$", 3),
               (r"חישוב $d=\frac{8}{\sqrt{120}}$", 4)),
    pitfalls=[r"לחלק באורך $\overrightarrow{P_1P_2}$ במקום באורך המכפלה הווקטורית.",
              r"להסיק מ-$\vec m_1\cdot\vec m_2\neq0$ שהישרים מצטלבים."],
    steps=[
        cho(r"מדוע הישרים מצטלבים עבור $a=0$?", r"כי $V\neq0$ והכיוונים אינם מקבילים",
            [r"כי $V=0$", r"כי $\vec m_1\cdot\vec m_2\neq0$", r"כי $\vec m_1\parallel\vec m_2$"],
            r"ב-$a=0$, $V=8\neq0$ ו-$\vec m_1\nparallel\vec m_2$. התנאי $\vec m_1\cdot\vec m_2\neq0$ אינו קשור: גם ב-$a=2$ (שם הישרים נחתכים) המכפלה הסקלרית שונה מאפס."),
        num(r"מהו $V$ עבור $a=0$?", 8, r"$(0-2)(0-4)=8$."),
        num(r"מהי הנורמה $\|\vec m_1\times\vec m_2\|=\|(-10,2,-4)\|$ (בקירוב)?", 10.954, r"$\sqrt{100+4+16}=\sqrt{120}\approx10.954$.", 0.001),
        num(r"מהו המרחק $d=\frac{8}{\sqrt{120}}$ (בקירוב)?", 0.7303, r"$\frac{8}{10.954}\approx0.7303$.", 0.001),
    ])

ENR[(2, "א")] = dict(
    rubric=rub((r"כתיבת המטריצה המורחבת", 1),
               (r"הפעולות $R_2-R_1$ ו-$R_3-kR_1$", 2),
               (r"הפעולה $2R_2-R_3$ והפעולה $R_3-kR_2$", 2),
               (r"הצורה המדורגת הסופית עם שורה אחרונה $\left(0\ 0\ (1-k)(1+k)\mid2(1-k)\right)$", 1)),
    pitfalls=[r"לחלק ב-$(k+1)$ בלי לבדוק את המקרה $k=-1$.",
              r"טעות בעמודה האחרונה בפעולה $2R_2-R_3$."],
    steps=[
        num(r"אחרי $R_2-R_1$ מהו האיבר בשורה 2 עמודה 2 עבור $k=1$?", 2, r"האיבר הוא $k+1=2$."),
        num(r"אחרי $2R_2-R_3$ מהו האיבר בשורה 2 עמודה 3 עבור $k=5$?", 4, r"האיבר הוא $k-1=4$."),
        num(r"במטריצה המדורגת הסופית, מהו האיבר בשורה 3 עמודה 3 עבור $k=3$?", -8, r"האיבר הוא $(1-k)(1+k)=(-2)(4)=-8$."),
    ])

ENR[(2, "ב")] = dict(
    rubric=rub((r"$k\neq\pm1$: שלושה איברים מובילים ולכן פתרון יחיד", 2),
               (r"$k=1$: שורת אפסים מלאה ולכן אינסוף פתרונות", 2),
               (r"$k=-1$: שורת סתירה ולכן אין פתרון", 2)),
    pitfalls=[r"לבלבל בין $k=1$ (אינסוף פתרונות) ל-$k=-1$ (אין פתרון).",
              r"להסיק 'אין פתרון' רק מכך שמתאפס האיבר המוביל, בלי לבדוק את אגף ימין."],
    steps=[
        num(r"מהי דרגת מטריצת המקדמים עבור $k=1$?", 2, r"שורה 3 היא $(0\ 0\ 0\mid0)$."),
        num(r"מהי דרגת המטריצה המורחבת עבור $k=-1$?", 3, r"שורה 3 היא $(0\ 0\ 0\mid4)$ ולכן הדרגה גדלה."),
        num(r"מהי דרגת מטריצת המקדמים עבור $k=-1$?", 2, r"שורה 3 של מטריצת המקדמים מתאפסת."),
        cho(r"עבור איזה ערך של $k$ אין פתרון?", r"$k=-1$",
            [r"$k=1$", r"$k=1$ וגם $k=-1$", r"$k=0$"],
            r"ב-$k=1$ יש אינסוף פתרונות (הדרגות שוות 2), ב-$k=0$ הדרגה 3 ולכן פתרון יחיד. רק ב-$k=-1$ הדרגות שונות."),
    ])

ENR[(2, "ג")] = dict(
    rubric=rub((r"הצבת $k=1$ בצורה המדורגת", 3),
               (r"זיהוי המשתנה החופשי $z=t$ ופתרון $y=2$, $x=-t$", 2),
               (r"הצגה פרמטרית $(0,2,0)+t(-1,0,1)$", 3)),
    pitfalls=[r"לשכוח שהמשתנה החופשי הוא $z$ ולא $y$.",
              r"טעות סימן ב-$x=-t$."],
    steps=[
        num(r"מהו $y$ בכל פתרון עבור $k=1$?", 2, r"$2y=4$."),
        num(r"בפתרון $x=-t$, $z=t$: מהו $x$ כאשר $t=3$?", -3, r"$x=-3$."),
        cho(r"איזה וקטור הוא וקטור כיוון של קבוצת הפתרונות?", r"$(-1,0,1)$",
            [r"$(1,0,1)$", r"$(0,2,0)$", r"$(-1,2,1)$"],
            r"וקטור כיוון פותר את המערכת ההומוגנית: $y=0$ ו-$x+z=0$. $(0,2,0)$ ו-$(-1,2,1)$ מפרים $y=0$, ו-$(1,0,1)$ מפר $x+z=0$."),
    ])

ENR[(2, "ד")] = dict(
    rubric=rub((r"הצבת $k=i$ בצורה המדורגת", 1),
               (r"פתרון $z=1-i$ מהשורה השלישית", 2),
               (r"פתרון $y=2-i$ ו-$x=-1$ בהצבה לאחור", 2)),
    pitfalls=[r"טעות באריתמטיקה מרוכבת: $(i-1)(1-i)=2i$.",
              r"לשכוח ש-$i^2=-1$."],
    steps=[
        num(r"מהו החלק הממשי של $z=\frac{2-2i}{2}$?", 1, r"$z=1-i$."),
        num(r"מהו החלק המדומה של $z=1-i$?", -1, r"$-1$."),
        num(r"מהו החלק הממשי של $y$ כאשר $2y+(i-1)(1-i)=4$?", 2, r"$(i-1)(1-i)=2i$, ולכן $y=2-i$."),
    ])

ENR[(3, "א")] = dict(
    rubric=rub((r"דירוג $B$ לצורה מדורגת $R$ בשלוש פעולות שורה", 3),
               (r"רישום מטריצות פעולות השורה", 3),
               (r"היפוך מטריצות הפעולות והסדר $B=EFGR$", 4)),
    pitfalls=[r"לכתוב $B=EFGR$ עם מטריצות פעולות השורה עצמן (מתקבל $EFGB=R$).",
              r"להפוך פעולה בסימן שגוי."],
    steps=[
        num(r"מהי דרגת $B$?", 2, r"$R$ כוללת שתי שורות לא אפסיות."),
        cho(r"כיצד מתקבל $B=EFGR$ מפעולות השורה $e_1$ (החלפה), $e_2$ ($R_3+2R_1$), $e_3$ ($R_3-R_2$)?", r"$E=e_1^{-1}$, $F=e_2^{-1}$, $G=e_3^{-1}$",
            [r"$E=e_3$, $F=e_2$, $G=e_1$", r"$E=e_1$, $F=e_2$, $G=e_3$", r"$E=e_3^{-1}$, $F=e_2^{-1}$, $G=e_1^{-1}$"],
            r"הדירוג נותן $e_3e_2e_1B=R$ ולכן $B=e_1^{-1}e_2^{-1}e_3^{-1}R$. שלוש האפשרויות האחרות אינן שוות ל-$B$ (בדיקה ישירה)."),
        num(r"מהו האיבר בשורה 3 עמודה 1 של $F=e_2^{-1}$ (ההופכית של $R_3+2R_1$)?", -2, r"ההופכית היא $R_3-2R_1$."),
        num(r"מהו האיבר בשורה 3 עמודה 2 של $G=e_3^{-1}$ (ההופכית של $R_3-R_2$)?", 1, r"ההופכית היא $R_3+R_2$."),
    ])

ENR[(3, "ב")] = dict(
    rubric=rub((r"הנחה: $A\mathbf{x}=\lambda\mathbf{x}$", 1),
               (r"שימוש בלינאריות: $A(c\mathbf{x})=c(A\mathbf{x})$", 2),
               (r"הצבת $A\mathbf{x}=\lambda\mathbf{x}$ וקבלת $\lambda(c\mathbf{x})$", 1),
               (r"$c\mathbf{x}\neq0$ כי $c\neq0$ ו-$\mathbf{x}\neq0$", 1)),
    pitfalls=[r"לשכוח לבדוק ש-$c\mathbf{x}$ שונה מאפס.",
              r"לכתוב $A(c\mathbf{x})=(c+\lambda)\mathbf{x}$."],
    steps=[
        odr("סדרו את שורות ההוכחה.",
            [r"$A\mathbf{x}=\lambda\mathbf{x}$", r"$A(c\mathbf{x})=c(A\mathbf{x})$", r"$c(A\mathbf{x})=c\lambda\mathbf{x}$", r"$c\lambda\mathbf{x}=\lambda(c\mathbf{x})$"],
            r"הוצאת הסקלר בעזרת הלינאריות, הצבת הנתון, וסידור מחדש."),
        cho(r"מדוע דורשים $c\neq0$?", r"כי וקטור עצמי חייב להיות שונה מאפס, ו-$c\mathbf{x}\neq0$ רק כש-$c\neq0$",
            [r"כי עבור $c=0$ השוויון $A(c\mathbf{x})=\lambda(c\mathbf{x})$ אינו מתקיים", r"כי אחרת $\lambda=0$", r"כי אחרת $\mathbf{x}=0$"],
            r"עבור $c=0$ השוויון מתקיים ($0=0$), אך $c\mathbf{x}=0$ אינו וקטור עצמי. $\lambda$ ו-$\mathbf{x}$ אינם תלויים ב-$c$."),
        fnd("בהוכחה הבאה שורה אחת שגויה. סמנו אותה.",
            [r"$A\mathbf{x}=\lambda\mathbf{x}$", r"$A(c\mathbf{x})=c(A\mathbf{x})$", r"$c(A\mathbf{x})=(c+\lambda)\mathbf{x}$", r"$c\lambda\mathbf{x}=\lambda(c\mathbf{x})$"], 2,
            r"מציבים $A\mathbf{x}=\lambda\mathbf{x}$ ומקבלים $c\lambda\mathbf{x}$, מכפלה ולא סכום."),
    ])

ENR[(3, "ג")] = dict(
    rubric=rub((r"הנתונים $A\mathbf{v}=\lambda\mathbf{v}$ ו-$A\mathbf{w}=\lambda\mathbf{w}$ עם אותו $\lambda$", 1),
               (r"לינאריות: $A(c\mathbf{v}+d\mathbf{w})=c(A\mathbf{v})+d(A\mathbf{w})$", 1),
               (r"הצבה: $c\lambda\mathbf{v}+d\lambda\mathbf{w}$", 2),
               (r"הוצאת $\lambda$: $\lambda(c\mathbf{v}+d\mathbf{w})$", 1)),
    pitfalls=[r"להשתמש בערכים עצמיים שונים ולכן לא להוציא גורם משותף.",
              r"לכתוב $A(c\mathbf{v}+d\mathbf{w})=cA\mathbf{v}+dA\mathbf{w}$ ולשכוח את ההצבה."],
    steps=[
        odr("סדרו את שורות ההוכחה.",
            [r"$A\mathbf{v}=\lambda\mathbf{v}$ וגם $A\mathbf{w}=\lambda\mathbf{w}$", r"$A(c\mathbf{v}+d\mathbf{w})=c(A\mathbf{v})+d(A\mathbf{w})$", r"$=c\lambda\mathbf{v}+d\lambda\mathbf{w}$", r"$=\lambda(c\mathbf{v}+d\mathbf{w})$"],
            r"לינאריות, הצבה, והוצאת $\lambda$ כגורם משותף."),
        cho(r"מה נדרש מ-$\mathbf{v}$ ו-$\mathbf{w}$ כדי שההוכחה תעבוד?", r"שהם מתאימים לאותו ערך עצמי $\lambda$",
            [r"שהם בלתי תלויים", r"ש-$A$ הפיכה", r"ש-$A$ סימטרית"],
            r"ההוכחה אינה משתמשת בבלתי תלות (למשל $\mathbf{w}=2\mathbf{v}$ עובד), בהפיכות (למשל $A=0$) או בסימטריה; רק אותו $\lambda$ מאפשר להוציא גורם משותף."),
    ])

ENR[(3, "ד")] = dict(
    rubric=rub((r"שימוש בלינאריות של $A$", 1),
               (r"הצבה: $A(c\mathbf{v}+d\mathbf{w})=c\lambda_1\mathbf{v}+d\lambda_2\mathbf{w}$", 2),
               (r"השוואה ל-$\lambda(c\mathbf{v}+d\mathbf{w})$ והסקה שהם שונים כי $\lambda_1\neq\lambda_2$", 2)),
    pitfalls=[r"לבלבל עם הסעיף הקודם ולהניח שהערכים העצמיים שווים.",
              r"לא להבחין שלגורם $\lambda_1,\lambda_2$ אין גורם משותף."],
    steps=[
        cho(r"מה קורה כאשר $\lambda_1=\lambda_2=\lambda$?", r"$A(c\mathbf{v}+d\mathbf{w})=\lambda(c\mathbf{v}+d\mathbf{w})$, כלומר הצירוף כן וקטור עצמי",
            [r"הצירוף שווה לווקטור האפס בהכרח", r"בהכרח $\mathbf{v}=\mathbf{w}$", r"הצירוף אינו וקטור עצמי"],
            r"עם $\lambda_1=\lambda_2$ אפשר להוציא את $\lambda$ כגורם משותף. לדוגמה $A=I$ עם $\mathbf{v}=e_1$, $\mathbf{w}=e_2$: הצירוף $e_1+e_2$ שונה מאפס ומ-$\mathbf{v}$ ומתאים ל-$\lambda=1$."),
        num(r"דוגמה: $A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, $\mathbf{v}=e_1$, $\mathbf{w}=e_2$, $c=d=1$. מהו הרכיב השני של $A(\mathbf{v}+\mathbf{w})$?", 2, r"$A(1,1)^T=(1,2)^T$, שאינו כפולה של $(1,1)^T$."),
    ])

ENR[(4, "א")] = dict(
    rubric=rub((r"פישוט $W$ ל-$\begin{pmatrix}a&b\\b&a+b\end{pmatrix}$", 1),
               (r"$W$ אינה ריקה: מטריצת האפס ב-$W$", 1),
               (r"סגירות לחיבור", 2),
               (r"סגירות לכפל בסקלר", 2)),
    pitfalls=[r"לבדוק סגירות על דוגמאות מספריות בלבד במקום על פרמטרים כלליים.",
              r"לפשט את $d$ באופן שגוי (לא $d=a-b$)."],
    steps=[
        cho(r"מהי הצורה הכללית של מטריצה ב-$W$?", r"$\begin{pmatrix}a&b\\b&a+b\end{pmatrix}$",
            [r"$\begin{pmatrix}a&b\\b&a-b\end{pmatrix}$", r"$\begin{pmatrix}a&b\\-b&a+b\end{pmatrix}$", r"$\begin{pmatrix}a&b\\b&b-a\end{pmatrix}$"],
            r"התנאים $c=b$ ו-$d=a+b$. עבור $a=b=1$ האפשרויות האחרות נותנות $d=0$, $c=-1$, $d=0$ ולכן אינן שייכות."),
        num(r"מהו $d$ עבור $a=2$, $b=3$?", 5, r"$d=a+b=5$."),
        fnd("בהוכחה הבאה שורה אחת שגויה. סמנו אותה.",
            [r"$W=\left\{\begin{pmatrix}a&b\\b&a+b\end{pmatrix}\right\}$", r"$\vec 0\in W$ (עבור $a=b=0$), ולכן $W\neq\emptyset$",
             r"$A_1+A_2=\begin{pmatrix}a_1+a_2&b_1+b_2\\b_1+b_2&(a_1+a_2)+(b_1+b_2)\end{pmatrix}\in W$",
             r"$kA_1=\begin{pmatrix}ka_1&kb_1\\kb_1&ka_1+b_1\end{pmatrix}\in W$"], 3,
            r"האיבר (2,2) של $kA_1$ הוא $k(a_1+b_1)=ka_1+kb_1$ ולא $ka_1+b_1$; בלי התיקון המטריצה אינה ב-$W$ עבור $k\neq1$."),
    ])

ENR[(4, "ב")] = dict(
    rubric=rub((r"הצורה הכללית $\begin{pmatrix}a&b\\b&a+b\end{pmatrix}$", 2),
               (r"הצבת $(a,b)=(1,0)$ ו-$(0,1)$", 2),
               (r"בסיס $\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&1\end{pmatrix}\right\}$ וממד 2", 2)),
    pitfalls=[r"לבחור מטריצה שאינה מקיימת $a+b-d=0$ (למשל $\begin{pmatrix}0&1\\1&0\end{pmatrix}$).",
              r"לשכוח לבדוק בלתי תלות."],
    steps=[
        num(r"מהו $\dim W$?", 2, r"שני פרמטרים חופשיים $a,b$."),
        cho(r"איזו קבוצה היא בסיס של $W$?", r"$\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&1\end{pmatrix}\right\}$",
            [r"$\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix}\right\}$", r"$\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix}\right\}$", r"$\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&1\end{pmatrix},\begin{pmatrix}1&1\\1&2\end{pmatrix}\right\}$"],
            r"במטריצה $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ מתקבל $a+b-d=1\neq0$ ולכן אינה ב-$W$; קבוצה בת איבר אחד אינה פורשת את $W$; והקבוצה השלישית תלויה (הסכום של שתי הראשונות)."),
        num(r"המטריצה $\begin{pmatrix}3&2\\2&5\end{pmatrix}\in W$ שווה ל-$\alpha\begin{pmatrix}1&0\\0&1\end{pmatrix}+\beta\begin{pmatrix}0&1\\1&1\end{pmatrix}$. מהו $\beta$?", 2, r"$\beta$ הוא האיבר בשורה 1 עמודה 2."),
    ])

ENR[(4, "ג")] = dict(
    rubric=rub((r"פרישת $U+W$ משלוש מטריצות $U$ ושתי מטריצות הבסיס של $W$", 2),
               (r"מטריצה שבה המטריצות הן שורות, ודירוג", 2),
               (r"השורות המקוריות שאינן מתאפסות הן בסיס, וממד 4", 2)),
    pitfalls=[r"לכלול בבסיס גם את המטריצה התלויה.",
              r"לחשב רק את ממד הסכום ולא למצוא בסיס."],
    steps=[
        num(r"מהי דרגת המטריצה בת 5 השורות והארבע העמודות?", 4, r"הצורה המדורגת כוללת ארבע שורות לא אפסיות ושורת אפסים."),
        num(r"מהו $\dim U$ (שלוש המטריצות הפורשות בלתי תלויות)?", 3, r"שלוש השורות $(1,0,1,1)$, $(0,1,-1,-2)$, $(0,0,0,1)$ בלתי תלויות."),
        cho(r"מה אומר $\dim(U+W)=4$?", r"$U+W=M_{2\times2}(\mathbb{R})$",
            [r"$U+W=U$", r"$U+W=W$", r"$U+W$ תת-מרחב ממימד 3"],
            r"$\dim M_{2\times2}=4$, ו-$U+W$ תת-מרחב שלו באותו ממד. $\dim U=3$ ו-$\dim W=2$ ולכן הסכום אינו שווה ל-$U$ או ל-$W$."),
    ])

ENR[(4, "ד")] = dict(
    rubric=rub((r"הצגה כפולה של וקטור בחיתוך: צירוף בסיס $U$ וצירוף בסיס $W$", 2),
               (r"מערכת הומוגנית ודירוג", 2),
               (r"פתרון עם $d_2=1$, $d_1=2$", 2),
               (r"הבסיס $\begin{pmatrix}2&1\\1&3\end{pmatrix}$ וממד 1", 1)),
    pitfalls=[r"לשכוח את סימני המינוס כשמעבירים את צירוף $W$ לאגף השני.",
              r"לקחת את ההצגה בבסיס $U$ במקום להחזיר למטריצה."],
    steps=[
        num(r"מהו $\dim(U\cap W)$ לפי $\dim U+\dim W-\dim(U+W)$?", 1, r"$3+2-4=1$."),
        num(r"בפתרון $d_2=1$: מהו $d_1$ (כך ש-$d_1=2d_2$)?", 2, r"מהדירוג מתקבל $d_1=2d_2$."),
        num(r"המטריצה $\begin{pmatrix}2&1\\1&3\end{pmatrix}=c_1\begin{pmatrix}1&0\\1&1\end{pmatrix}+c_2\begin{pmatrix}0&1\\-1&-2\end{pmatrix}+c_3\begin{pmatrix}0&0\\0&1\end{pmatrix}$. מהו $c_3$?", 3, r"$c_1=2$, $c_2=1$, ובאיבר (2,2): $2-2+c_3=3$."),
    ])

ENR[(5, "א")] = dict(
    rubric=rub((r"חישוב הדטרמיננטה בעזרת פיתוח", 3),
               (r"$\det A=-(a+6)(a-2)$ ואפסים $a=-6,2$", 1),
               (r"מסקנה: $A$ הפיכה אם ורק אם $a\neq-6,2$", 1)),
    pitfalls=[r"טעות סימן בפתרון המשוואה הריבועית $a^2+4a-12=0$.",
              r"לרשום רק אחד משני האפסים."],
    steps=[
        num(r"מהו $\det A$ עבור $a=0$?", 12, r"$-(a^2+4a-12)=12$."),
        num(r"מהו $\det A$ עבור $a=1$?", 7, r"$-(1+4-12)=7$."),
        cho(r"עבור אילו ערכי $a$ המטריצה $A$ אינה הפיכה?", r"$a=-6$ וגם $a=2$",
            [r"$a=6$ וגם $a=-2$", r"$a=-6$ בלבד", r"$a=2$ בלבד"],
            r"$a^2+4a-12=(a+6)(a-2)$ מתאפס בדיוק ב-$a=-6$ וב-$a=2$."),
    ])

ENR[(5, "ב")] = dict(
    rubric=rub((r"הצבת $a=1$ וחישוב $\det A=7\neq0$", 1),
               (r"חישוב המשלימים האלגבריים", 3),
               (r"שחלוף המטריצה", 2),
               (r"חלוקה בדטרמיננטה: $A^{-1}=\frac17\begin{pmatrix}13&-1&-5\\-4&3&1\\-1&-1&2\end{pmatrix}$", 1)),
    pitfalls=[r"לשכוח לשחלף את מטריצת המשלימים האלגבריים.",
              r"טעות סימן במשלימים האלגבריים (תבנית השחמט)."],
    steps=[
        num(r"מהו $\det A$ עבור $a=1$?", 7, r"$-(1+4-12)=7$."),
        num(r"מהו המשלים האלגברי $C_{11}$ של $A=\begin{pmatrix}1&1&2\\1&3&1\\1&2&5\end{pmatrix}$?", 13, r"$3\cdot5-1\cdot2=13$."),
        num(r"מהו $7\cdot\left(A^{-1}\right)_{21}$ (האיבר בשורה 2 עמודה 1 של $\operatorname{adj}A$)?", -4, r"$C_{12}=-(1\cdot5-1\cdot1)=-4$, ו-$(A^{-1})_{21}=\frac{C_{12}}{\det A}$."),
        cho(r"איזו נוסחה נותנת את $A^{-1}$?", r"$\frac{1}{\det A}C^{T}$, כאשר $C$ מטריצת המשלימים האלגבריים",
            [r"$\frac{1}{\det A}C$", r"$(\det A)\cdot C^{T}$", r"$\frac{1}{\det A}M^{T}$, כאשר $M$ מטריצת המינורים בלי סימנים"],
            r"עבור $A$ זו $C\neq C^{T}$, והמינורים ללא סימנים שונים מהמשלימים האלגבריים, ולכן שלוש האפשרויות האחרות נותנות מטריצות שאינן ההופכית."),
    ])

ENR[(5, "ג")] = dict(
    rubric=rub((r"כתיבת $B^2$ באיברים", 3),
               (r"המשוואות על האיברים", 3),
               (r"דוגמה $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ ובדיקה", 2)),
    pitfalls=[r"להסיק $B=\pm I$ מתוך $B^2=I$, כמו במספרים ממשיים.",
              r"לבחור דוגמה בלי לחשב $B^2$ בפועל."],
    steps=[
        cho(r"איזו מטריצה מקיימת $B^2=I$ ואינה $\pm I$?", r"$\begin{pmatrix}-1&0\\0&1\end{pmatrix}$",
            [r"$\begin{pmatrix}1&1\\0&1\end{pmatrix}$", r"$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$", r"$\begin{pmatrix}2&0\\0&\frac12\end{pmatrix}$"],
            r"הריבועים של האחרות הם $\begin{pmatrix}1&2\\0&1\end{pmatrix}$, $-I$ ו-$\begin{pmatrix}4&0\\0&\frac14\end{pmatrix}$."),
        num(r"עבור $B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ מהו $\det B$ (נובע מ-$(\det B)^2=1$)?", -1, r"$\det B=-1$."),
    ])

ENR[(5, "ד")] = dict(
    rubric=rub((r"שימוש בכפליות הדטרמיננטה", 2),
               (r"$\det(3B)=3^5\det B$ עבור מטריצה $5\times5$", 1),
               (r"$\det(C^T)\det(C^{-1})=1$", 1),
               (r"התוצאה $-30375$", 1)),
    pitfalls=[r"לרשום $\det(3B)=3\det B$ במקום $3^5\det B$.",
              r"לשכוח ש-$\det\left(B^T\right)=\det B$."],
    steps=[
        cho(r"מהו $\det(3M)$ עבור מטריצה $M$ מסדר $5\times5$?", r"$3^5\det M$",
            [r"$3\det M$", r"$5\det M$", r"$15\det M$"],
            r"הכפלה בסקלר מכפילה כל אחת מחמש השורות ב-3, ולכן הדטרמיננטה מוכפלת ב-$3^5=243$."),
        num(r"מהו $\det\left(3B^2\right)$ עבור $\det B=-5$ (מטריצה $5\times5$)?", 6075, r"$3^5\cdot(-5)^2=243\cdot25=6075$."),
        num(r"מהו $\det\left(C^T\right)\det\left(C^{-1}\right)$ עבור $\det C=2$?", 1, r"$2\cdot\frac12=1$."),
        num(r"מהו $\det\left(3B^2C^TC^{-1}B^T\right)$?", -30375, r"$6075\cdot1\cdot(-5)=-30375$."),
    ])

ENR[(6, "א")] = dict(
    rubric=rub((r"הצבת $p_1+p_2$ בנוסחת $T$", 2),
               (r"שוויון ל-$T(p_1)+T(p_2)$", 1),
               (r"הצבת $kp_1$ ויציאת $k$", 2),
               (r"מסקנה: $T$ לינארית", 1)),
    pitfalls=[r"לבדוק רק את התכונה של החיבור ולשכוח את הכפל בסקלר.",
              r"לבדוק על פולינומים מסוימים בלבד."],
    steps=[
        cho(r"מה צריך לבדוק כדי להוכיח ש-$T$ לינארית?", r"$T(p_1+p_2)=T(p_1)+T(p_2)$ וגם $T(kp)=kT(p)$",
            [r"רק $T(0)=0$", r"$T(p_1p_2)=T(p_1)T(p_2)$", r"ש-$T$ חד-חד-ערכית"],
            r"התנאי $T(0)=0$ הכרחי אך אינו מספיק; כפל פולינומים אינו חלק מההגדרה; וחח״ע אינה נדרשת."),
        num(r"מהו המקדם של $x^2$ ב-$T(1+x^2)$ (עם $a=1$, $c=1$)?", 1, r"$(b+2c-a-d)=0+2-1-0=1$."),
        num(r"מהו המקדם של $x^2$ ב-$T(1)+T(x^2)$?", 1, r"$T(1)$ נותן $-1$ ו-$T(x^2)$ נותן $2$: סכום $1$, כמו בשורה הקודמת."),
    ])

ENR[(6, "ב")] = dict(
    rubric=rub((r"המשוואות $a-2c+d=0$, $b+2c-a-d=0$, $b=0$", 2),
               (r"פתרון עם משתנים חופשיים $c=s$, $d=t$ ו-$a=2s-t$", 3),
               (r"הצגה כצירוף $s(2,0,1,0)+t(-1,0,0,1)$", 2),
               (r"$\ker T=\mathrm{sp}\{2+x^2,\,-1+x^3\}$ וממד 2", 1)),
    pitfalls=[r"לשכוח את התנאי $b=0$.",
              r"טעות בהעברת אגף בפתרון $a=2c-d$."],
    steps=[
        cho(r"איזה פולינום שייך ל-$\ker T$?", r"$2+x^2$",
            [r"$1+x^2$", r"$x^3$", r"$x+x^2$"],
            r"עבור $2+x^2$: $a=2,\ c=1$ וכל שלושת המקדמים ב-$T$ מתאפסים. ל-$1+x^2$ המקדם החופשי $-1$, ל-$x^3$ המקדם החופשי $1$, ול-$x+x^2$ המקדם של $x^3$ הוא $1$."),
        num(r"מהו המימד של $\ker T$?", 2, r"שני משתנים חופשיים ($c$ ו-$d$)."),
        num(r"בפתרון $a=2c-d$: מהו $a$ עבור $c=3$, $d=1$?", 5, r"$2\cdot3-1=5$."),
    ])

ENR[(6, "ג")] = dict(
    rubric=rub((r"הצגת $T(p)$ כצירוף של ארבעה וקטורים", 2),
               (r"זיהוי הווקטורים התלויים", 3),
               (r"בסיס $\{1-x^2,\,x^2+x^3\}$", 2),
               (r"ממד 2", 1)),
    pitfalls=[r"לכלול גם את הווקטורים התלויים בבסיס.",
              r"לשכוח שמשפט המימדים נותן בדיקה: $4-2=2$."],
    steps=[
        num(r"מהו $\dim\mathrm{Im}\,T$ לפי משפט המימדים?", 2, r"$4-\dim\ker T=4-2=2$."),
        cho(r"איזו קבוצה היא בסיס של $\mathrm{Im}\,T$?", r"$\{1-x^2,\ x^2+x^3\}$",
            [r"$\{1-x^2,\ -2+2x^2\}$", r"$\{1-x^2,\ x^2+x^3,\ x^3\}$", r"$\{1,\ x^3\}$"],
            r"הקבוצה הראשונה תלויה; ב-$\{1-x^2,\,x^2+x^3,\,x^3\}$ יש וקטור שאינו בתמונה ($x^3\notin\mathrm{Im}\,T$); ו-$1,x^3$ אינם בתמונה."),
        num(r"מהו המקדם של $x^3$ ב-$T(x)$?", 1, r"$T(x)=x^2+x^3$ (עבור $b=1$)."),
    ])

ENR[(6, "ד")] = dict(
    rubric=rub((r"הגרעין אינו $\{\mathbf 0\}$", 1),
               (r"ולכן $T$ אינה חח״ע", 1),
               (r"נימוק: משפט על חח״ע וגרעין", 1)),
    pitfalls=[r"להסיק חח״ע מכך ש-$T$ לינארית."],
    steps=[
        cho(r"האם $T$ חד-חד-ערכית?", r"לא, כי הגרעין שלה שונה מ-$\{\mathbf 0\}$",
            [r"כן, כי $T$ לינארית", r"כן, כי הגרעין מכיל פולינום שונה מאפס", r"כן, כי $\dim\ker T=2\neq\dim V$"],
            r"העתקה לינארית חח״ע אם ורק אם הגרעין שלה טריוויאלי; כאן $\dim\ker T=2$."),
        num(r"מהו $\dim\ker T$?", 2, r"מהסעיף הקודם."),
    ])

for q in questions:
    if q.get("hold"):
        continue
    e = ENR.get((q["num"], q["part"]))
    assert e is not None, (q["num"], q["part"])
    if q.get("points") is not None:
        assert sum(r["points"] for r in e["rubric"]) == q["points"], (q["num"], q["part"])
    assert 2 <= len(e["steps"]) <= 5 and 1 <= len(e["pitfalls"]) <= 3 and 3 <= len(e["rubric"]) <= 5, (q["num"], q["part"])
    q.update(rubric=e["rubric"], rubricSource="ai-draft", pitfalls=e["pitfalls"], steps=e["steps"], stepsSource="ai-draft")


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
