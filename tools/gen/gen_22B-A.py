# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-A.json -- linear algebra, semester B 2022, moed A (07.06.2022), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-A.py

Source: one PDF (10pp, the last page is blank): the exam text followed question by question by the typed official solution.
Five questions of 25 points (best 4 count), 19 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (B); in the raw schema item 2 is part "gimel". The official
  solution calls the item-2 matrix A; written as B here.
- Q5 has two numbered items: item 1 (T, parts a-c) and item 2 (F), which is part "dalet" here.
- Q1 c/d FINAL-ANSWER ERROR: the official derives det^2(A) = (5/2)^4 and then states det(A) = 25/4 (and det(A^-1) = 4/25).
  The sign is not determined: A = diag(a,a,a,-a) with a^2 = 5/2 satisfies both equations and has det = -25/4. The correct
  answers are +-25/4 and +-4/25. Both items ship with the minimal fix, solutionSource "solved", official False and the
  visible prefix "official with correction" (standing ruling), verified by script.
- Q4 a: the official writes the parametrization of x+2y-3z=0 as s(-2,0,1)+t(3,0,1); the next line (and the correct
  decomposition) is v3=(-2,1,0). Intermediate slip, corrected, logged in ASK_ADIR, no label.
- Q4 b/c: the third basis vector of W1+W2 in the official is the third matrix column (2,-1,0) = -v3; kept as printed.
- Q2 d: the official lists the roots in exponential/trigonometric form; the exam asks for x+iy, so the exact algebraic form is
  added in the solution.

Checks (sympy, tools/verify/22B-A/verify_22B-A.py): A^-1=(A^T+A)/5 and symmetry on a model, the determinant sign counterexample,
the Q2 echelon form, the k=3 family and the k!=3 solution, det of the 2x2 and its roots, A^-1 and its elementary product,
charpoly/P/D of Q3, bases and dims of W1, W2, W1+W2, W1 cap W2 and membership, Ker/Im of T and k=5, [F]_B^B.
Only mismatch: the determinant sign of Q1 c/d. No hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-A.json"


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


contexts = {
    "c1": {"kind": "text", "title": "שאלה 1",
           "text": r"נתונה מטריצה $A$ ממשית מסדר $4\times4$ המקיימת את המשוואות $AA^T+A^2=5I$ ו-$AA^T-A^2=0$."},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": J(r"נתונה מערכת המשוואות כאשר $k$ הוא פרמטר ממשי:",
                     r"$$\begin{cases} x+y+kz=2\\ 3x+4y+2z=k\\ 2x+3y-z=1\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
           "text": r"נתונה המטריצה $A=" + pm("1&2&0", "0&1&1", "2&4&2") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של R^3",
           "text": J(r"נגדיר שני תתי מרחב $W_1$ ו-$W_2$ של $\mathbb{R}^3$ ע״י",
                     r"$W_1=\{A\vec{x}:\ \vec{x}\in\mathbb{R}^3\},\qquad A=" + pm("1&2&-4", "-2&3&-13", "-1&-1&1") + r"$",
                     r"$W_2=\left\{" + pm("x", "y", "z") + r"\in\mathbb{R}^3:\ x+2y-3z=0\right\}$")},
    "c5": {"kind": "text", "title": "שאלה 5 - סעיפים א עד ג",
           "text": J(r"נתונה העתקה לינארית $T:\mathbb{R}^4\to\mathbb{R}_2[x]$ המוגדרת על ידי:",
                     r"$$T" + pm("a", "b", "c", "d") + r"=(a+b+c+d)+(a+b+3c+3d)x+(-a-b+c+d)x^2$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "matrix_proofs",
    r"הראו כי $A$ הפיכה ע״י מציאת ביטוי של המטריצה ההפוכה באמצעות $A$.",
    J(r"מהמשוואה $AA^T+A^2=5I$ נובע כי $A\left(A^T+A\right)=5I$ או $A\cdot\frac{1}{5}\left(A^T+A\right)=I$. זאת אומרת ש-$A$ כן הפיכה כך ש-",
      r"$$A^{-1}=\frac{1}{5}\left(A^T+A\right)$$"),
    7, contextId="c1"))

questions.append(Q(
    1, "ב", "proof", "matrix_proofs",
    r"האם $A^{-1}$ מטריצה סימטרית?",
    J(r"נבנה מטריצה $\left(A^{-1}\right)^T$:",
      r"$$\left(A^{-1}\right)^T=\frac{1}{5}\left(A^T+A\right)^T=\frac{1}{5}\left(A+A^T\right)=A^{-1}$$",
      r"וזה מוכיח שהמטריצה $A^{-1}$ היא מטריצה סימטרית. **כן.**"),
    7, contextId="c1"))

questions.append(Q(
    1, "ג", "computation", "determinants",
    r"חשבו את הדטרמיננטה $|A|$.",
    J(r"**הפתרון הרשמי עם תיקון:** בפתרון הרשמי נקבע $\det(A)=\frac{25}{4}$; מהשוויון $\det^2(A)=\left(\frac{5}{2}\right)^4$ נובע רק ש-$\det(A)=\pm\frac{25}{4}$.",
      r"מהמשוואות הנתונות נוכל לקבל כי $AA^T=A^2$ ו-$AA^T+A^2=5I$, כלומר $2A^2=5I$, או במילים אחרות $A^2=\frac{5}{2}I$. לכן",
      r"$$\det\left(A^2\right)=\left(\frac{5}{2}\right)^4\det(I)\ \Leftarrow\ A^2=\frac{5}{2}I\ \Leftarrow\ 2A^2=5I$$",
      r"ולכן $\det^2(A)=\left(\frac{5}{2}\right)^4$. מכאן סופית נקבל ש-",
      r"$$\det(A)=\pm\frac{25}{4}$$",
      r"**הערה:** שני הסימנים אפשריים. למשל $A=\mathrm{diag}(a,a,a,a)$ עם $a=\sqrt{5/2}$ נותנת $\det(A)=\frac{25}{4}$, ואילו $A=\mathrm{diag}(a,a,a,-a)$ מקיימת את שתי המשוואות ($AA^T=A^2=a^2I$ ו-$2a^2=5$) ו-$\det(A)=-\frac{25}{4}$."),
    7, contextId="c1", solutionSource="solved", official=False))

questions.append(Q(
    1, "ד", "computation", "determinants",
    r"חשבו את הדטרמיננטה $\left|A^{-1}\right|$.",
    J(r"**הפתרון הרשמי עם תיקון:** בפתרון הרשמי נקבע $\det\left(A^{-1}\right)=\frac{4}{25}$; בהתאם לסעיף הקודם התוצאה היא $\pm\frac{4}{25}$.",
      r"$$\det\left(A^{-1}\right)=\frac{1}{\det(A)}=\pm\frac{4}{25}$$"),
    4, contextId="c1", solutionSource="solved", official=False))

# ------------------------------------------------------------------ Q2
R0 = [["1", "1", "k", "2"], ["3", "4", "2", "k"], ["2", "3", "-1", "1"]]
R1 = [["1", "1", "k", "2"], ["0", "-1", "3k-2", "6-k"], ["0", "-1", "2k+1", "3"]]
R2 = [["1", "0", "4k-2", "8-k"], ["0", "1", "2-3k", "k-6"], ["0", "-1", "2k+1", "3"]]
R3 = [["1", "0", "4k-2", "8-k"], ["0", "1", "2-3k", "k-6"], ["0", "0", "3-k", "k-3"]]
ECH = J(r"דירוג נותן לנו:",
        "$$" + aug(R0) + arrow(r"\substack{3R_1-R_2\to R_2\\2R_1-R_3\to R_3}") + aug(R1) + arrow(r"\substack{R_2+R_1\to R_1\\-R_2\to R_2}") + aug(R2) + arrow(r"R_2+R_3\to R_3") + aug(R3) + "$$")

questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ יש פתרון יחיד למערכת? מצאו את הפתרון.",
    J(ECH,
      r"עבור $k\neq3$, נקבל פתרון יחיד מהצורה:",
      "$$" + aug([["1", "0", "4k-2", "8-k"], ["0", "1", "2-3k", "k-6"], ["0", "0", "1", "-1"]]) + r"\Rightarrow\begin{cases}x=3(k+2)\\y=-2(k+2)\\z=-1\end{cases}$$"),
    6, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ אין פתרון למערכת?",
    J(r"מהמטריצה המדורגת בסעיף א, השורה השלישית היא $\left(0\ \ 0\ \ 3-k\ \middle|\ k-3\right)$: עבור $k\neq3$ יש פתרון יחיד, ועבור $k=3$ היא שורת אפסים (אינסוף פתרונות).",
      r"אין ערך של $k$ עבורו אין פתרון למערכת."),
    6, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ יש אינסוף פתרונות למערכת? מצאו הצגה פרמטרית של הפתרונות. הראו שפתרון זה הוא סכום של הפתרון של מערכת המשוואות ההומוגנית יחד עם פתרון פרטי של מערכת המשוואות הלא-הומוגנית המקורית.",
    J(r"נבדוק תחילה את הערך $k=3$. עבור ערך זה נקבל אינסוף פתרונות:",
      "$$" + aug([["1", "1", "3", "2"], ["3", "4", "2", "3"], ["2", "3", "-1", "1"]]) + r"\to" + aug([["1", "0", "10", "5"], ["0", "1", "-7", "-3"], ["0", "0", "0", "0"]])
      + r"\Rightarrow\begin{cases}x=5-10z\\y=-3+7z\\0=0\end{cases}$$",
      r"אזי הפתרון הכללי נתון:",
      r"$$(x,y,z)=(5-10z,\,-3+7z,\,z)=(5,-3,0)+z(-10,7,1)$$",
      r"הפתרון הכללי הזה מורכב משני חלקים. הפתרון הפרטי, $(5,-3,0)$, שפותר את המערכת המקורית, והפתרון הכללי של המערכת ההומוגנית $z(-10,7,1)$."),
    7, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"עבור איזה ערך של הפרמטר המרוכב $z$ המטריצה $A=" + pm("1-i&iz", "z^2&1+i") + r"$ הפיכה. נא לכתוב את הפתרונות בצורה $x+iy$.",
    J(r"המטריצה $A$ הפיכה אם ורק אם הדטרמיננטה שלה שונה מאפס. נחשב ונמצא:",
      r"$$\det A=(1-i)(1+i)-iz^3=1-i^2-iz^3=2-iz^3$$",
      r"נחשב מתי $\det A=0\ \Leftarrow\ 2-iz^3=0\ \Leftarrow\ z^3=-2i$.",
      r"$$z^3=-2i=2(0-i)=2\left(\cos\frac{3\pi}{2}+i\sin\frac{3\pi}{2}\right)=2\left(\cos\left(\frac{3\pi}{2}+2\pi k\right)+i\sin\left(\frac{3\pi}{2}+2\pi k\right)\right)=2e^{i\left(\frac{3\pi}{2}+2\pi k\right)}\ \Rightarrow\ z_k=2^{1/3}e^{i\left(\frac{\pi}{2}+\frac{2\pi}{3}k\right)}$$",
      r"ישנם שלושה פתרונות:",
      r"$$z_0=2^{1/3}e^{i\frac{\pi}{2}}=2^{1/3}\left(\cos\frac{\pi}{2}+i\sin\frac{\pi}{2}\right)=i\,2^{1/3}$$",
      r"$$z_1=2^{1/3}e^{i\left(\frac{\pi}{2}+\frac{2\pi}{3}\right)}=2^{1/3}e^{i\left(\pi+\frac{\pi}{6}\right)}=-2^{1/3}\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right)$$",
      r"$$z_2=2^{1/3}e^{i\left(\frac{\pi}{2}+\frac{4\pi}{3}\right)}=2^{1/3}e^{i\left(2\pi-\frac{\pi}{6}\right)}=2^{1/3}\left(\cos\frac{\pi}{6}-i\sin\frac{\pi}{6}\right)$$",
      r"בצורה $x+iy$: $z_0=2^{1/3}i$, $z_1=-2^{1/3}\left(\frac{\sqrt3}{2}+\frac{1}{2}i\right)$, $z_2=2^{1/3}\left(\frac{\sqrt3}{2}-\frac{1}{2}i\right)$.",
      r"**סיכום:** עבור $z\neq z_0,z_1,z_2$ המטריצה הפיכה."),
    6, contextId="c2"))

# ------------------------------------------------------------------ Q3
Ai_aug = [
    (aug([["1", "2", "0", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["2", "4", "2", "0", "0", "1"]]), r"R_3\to R_3-2R_1"),
    (aug([["1", "2", "0", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "2", "-2", "0", "1"]]), r"R_3\to0.5R_3"),
    (aug([["1", "2", "0", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "1", "-1", "0", "0.5"]]), r"R_2\to R_2-R_3"),
    (aug([["1", "2", "0", "1", "0", "0"], ["0", "1", "0", "1", "1", "-0.5"], ["0", "0", "1", "-1", "0", "0.5"]]), r"R_1\to R_1-2R_2"),
    (aug([["1", "0", "0", "-1", "-2", "1"], ["0", "1", "0", "1", "1", "-0.5"], ["0", "0", "1", "-1", "0", "0.5"]]), None),
]
inv_chain = "$$" + "".join(m + (arrow(op) if op else "") for m, op in Ai_aug) + "$$"
AINV = pm("-1&-2&1", "1&1&-0.5", "-1&0&0.5")

questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הוכיחו ש-$A$ הפיכה על ידי מציאת המטריצה $A^{-1}$.",
    J(r"נחשב את $A^{-1}$:", inv_chain,
      r"קיבלנו שהמטריצה ההופכית היא:",
      r"$$A^{-1}=" + AINV + "$$"),
    6, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"הציגו את $A^{-1}$ בצורת כפל של מטריצות אלמנטריות.",
    J(r"כעת נשתמש בדירוג הנ״ל ונכתוב את $A^{-1}$ כמכפלה של מטריצות אלמנטריות:",
      r"$$A^{-1}=" + pm("1&-2&0", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&-1", "0&0&1") + pm("1&0&0", "0&1&0", "0&0&0.5") + pm("1&0&0", "0&1&0", "-2&0&1") + "$$"),
    7, contextId="c3"))

B3 = pm("2&1&1", "1&2&1", "0&0&1")
questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + B3 + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $D=P^{-1}BP$.",
    J(r"תחילה נמצא את כל הערכים העצמיים והווקטורים העצמיים של $B$. נחשב את הדטרמיננטה הבאה לפי שורה שלישית:",
      r"$$|\lambda I-B|=\begin{vmatrix}\lambda-2&-1&-1\\-1&\lambda-2&-1\\0&0&\lambda-1\end{vmatrix}=(\lambda-1)\begin{vmatrix}\lambda-2&-1\\-1&\lambda-2\end{vmatrix}=(\lambda-1)\left[(\lambda-2)^2-1\right]=(\lambda-1)(\lambda^2-4\lambda+3)=(\lambda-1)(\lambda-1)(\lambda-3)$$",
      r"קיבלנו שהערכים העצמיים הם: $1,3$. כעת נמצא את הווקטורים העצמיים.",
      r"**עבור ע״ע 1:**",
      r"$$" + pm("-1&-1&-1", "-1&-1&-1", "0&0&0") + r"\to\cdots\to" + pm("1&1&1", "0&0&0", "0&0&0") + "$$",
      r"נסמן $y=t,\ z=s$ ונקבל: $x=-t-s$. הווקטורים העצמיים המתקבלים הם: $(-1,1,0)^T,\ (-1,0,1)^T$.",
      r"**עבור ע״ע 3:**",
      r"$$" + pm("1&-1&-1", "-1&1&-1", "0&0&2") + r"\to\cdots\to" + pm("1&-1&0", "0&0&1", "0&0&0") + "$$",
      r"נסמן $y=t$ ונקבל: $x=t,\ z=0$. הווקטור העצמי המתקבל הוא: $(1,1,0)^T$.",
      r"כעת נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$:",
      r"$$D=" + pm("1&0&0", "0&1&0", "0&0&3") + r",\qquad P=" + pm("-1&-1&1", "1&0&1", "0&1&0") + "$$"),
    12))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1$ ו-$W_2$.",
    J(r"על פי ההגדרה של $W_1$ מתקיים $W_1=\mathrm{Col}(A)$. לכן נמצא בסיס ומימד של תת מרחב זה. לשם כך נדרג את $A$ ונקבל",
      r"$$A=" + pm("1&2&-4", "-2&3&-13", "-1&-1&1") + arrow(r"\substack{R_2+2R_1\to R_2\\R_3+R_1\to R_3}") + pm("1&2&-4", "0&7&-21", "0&1&-3") + arrow(r"7R_3-R_2\to R_3") + pm("1&2&-4", "0&7&-21", "0&0&0") + "$$",
      r"$$" + arrow(r"\frac{1}{7}R_2\to R_2") + pm("1&2&-4", "0&1&-3", "0&0&0") + arrow(r"R_1-2R_2\to R_1") + pm("1&0&2", "0&1&-3", "0&0&0") + "$$",
      r"כיוון שבעמודה האחרונה אין איבר מוביל נשמיט את הווקטור המתאים מהעמודות של $A$ ונקבל ש-",
      r"$$W_1=\mathrm{Col}(A)=\mathrm{span}\left\{\vec{v}_1=" + pm("1", "-2", "-1") + r",\ \vec{v}_2=" + pm("2", "3", "-1") + r"\right\}$$",
      r"כיוון ש-$\vec{v}_1$ ו-$\vec{v}_2$ הם בת״ל, הקבוצה $B_1=\{\vec{v}_1,\vec{v}_2\}$ מהווה בסיס של $W_1$ ו-$\dim(W_1)=2$. עתה נמצא בסיס ומימד של $W_2$. לשם כך נפתור את המשוואה",
      r"$$x+2y-3z=0$$",
      r"במערכת זו יש שני משתנים חופשיים. נבצע פרמטריזציה $y=s,\ z=t$ ונקבל ש-$x=-2s+3t$. מכאן שפתרון המערכת הוא",
      r"$$" + pm("x", "y", "z") + "=" + pm("-2s+3t", "s", "t") + "=s" + pm("-2", "1", "0") + "+t" + pm("3", "0", "1") + "$$",
      r"מכאן",
      r"$$W_2=\mathrm{span}\left\{\vec{v}_3=" + pm("-2", "1", "0") + r",\ \vec{v}_4=" + pm("3", "0", "1") + r"\right\}$$",
      r"כיוון ש-$\vec{v}_3$ ו-$\vec{v}_4$ הם בת״ל הקבוצה $B_2=\{\vec{v}_3,\vec{v}_4\}$ מהווה בסיס של $W_2$ ו-$\dim(W_2)=2$."),
    7, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1+W_2$.",
    J(r"(ב)+(ג): כדי למצוא בסיס ומימד של $W_1\cap W_2$ ו-$W_1+W_2$ נבנה מטריצה שעמודותיה הן וקטורי הבסיס של $W_1$ ו-$W_2$ שמצאנו ונדרג",
      "$$" + aug([["1", "2", "2", "-3"], ["-2", "3", "-1", "0"], ["-1", "-1", "0", "-1"]], 2) + arrow(r"\substack{R_2+2R_1\to R_2\\R_3+R_1\to R_3}") + aug([["1", "2", "2", "-3"], ["0", "7", "3", "-6"], ["0", "1", "2", "-4"]], 2) + arrow(r"7R_3-R_2\to R_3") + "$$",
      "$$" + aug([["1", "2", "2", "-3"], ["0", "7", "3", "-6"], ["0", "0", "11", "-22"]], 2) + arrow(r"\frac{1}{11}R_3\to R_3") + aug([["1", "2", "2", "-3"], ["0", "7", "3", "-6"], ["0", "0", "1", "-2"]], 2) + "$$",
      r"בשלב זה אנו רואים שבכל העמודות למעט העמודה האחרונה יש איבר מוביל. לכן נשמיט את הווקטור בעמודה האחרונה של המטריצה ונקבל בסיס $B_{W_1+W_2}$ עבור $W_1+W_2$",
      r"$$B_{W_1+W_2}=\left\{" + pm("1", "-2", "-1") + "," + pm("2", "3", "-1") + "," + pm("2", "-1", "0") + r"\right\},\quad\dim(W_1+W_2)=3\ \Rightarrow\ W_1+W_2=\mathbb{R}^3$$"),
    7, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1\cap W_2$.",
    J(r"כדי למצוא בסיס עבור $W_1\cap W_2$ נמשיך ונפתור את המערכת ההומוגנית",
      r"$$" + aug([["1", "2", "2", "-3"], ["0", "7", "3", "-6"], ["0", "0", "1", "-2"]], 2) + pm("\\alpha_1", "\\alpha_2", "\\beta_1", "\\beta_2") + "=" + pm("0", "0", "0") + "$$",
      r"במערכת הנ״ל $\beta_2$ הוא משתנה חופשי. נבצע פרמטריזציה $\beta_2=t$ ונקבל ש-$\beta_1=2\beta_2=2t$. מכאן",
      r"$$\vec{v}\in W_1\cap W_2\ \Leftrightarrow\ \vec{v}=2t" + pm("-2", "1", "0") + "+t" + pm("3", "0", "1") + "=t" + pm("-1", "2", "1") + "$$",
      r"מכאן נקבל בסיס עבור $W_1\cap W_2$",
      r"$$B_{W_1\cap W_2}=\left\{" + pm("-1", "2", "1") + r"\right\},\quad\dim(W_1\cap W_2)=1$$"),
    7, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם הווקטור $" + pm("5", "-10", "-5") + r"$ שייך אל $W_1\cap W_2$?",
    r"$$" + pm("5", "-10", "-5") + "=-5" + pm("-1", "2", "1") + r"\in W_1\cap W_2$$" + "\nכלומר, **כן**.",
    4, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד ובסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    J(r"נסמן $B=\left(1,x,x^2\right)$ בסיס סטנדרטי של $\mathbb{R}_2[x]$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^4$.",
      r"$$\left[T" + pm("1", "0", "0", "0") + r"\right]_B=\left[1+x-x^2\right]_B=" + pm("1", "1", "-1") + r",\quad \left[T" + pm("0", "1", "0", "0") + r"\right]_B=\left[1+x-x^2\right]_B=" + pm("1", "1", "-1") + "$$",
      r"$$\left[T" + pm("0", "0", "1", "0") + r"\right]_B=\left[1+3x+x^2\right]_B=" + pm("1", "3", "1") + r",\quad \left[T" + pm("0", "0", "0", "1") + r"\right]_B=\left[1+3x+x^2\right]_B=" + pm("1", "3", "1") + "$$",
      r"מטריצה מייצגת סטנדרטית היא",
      r"$$A=[T]_B^E=" + pm("1&1&1&1", "1&1&3&3", "-1&-1&1&1") + "$$",
      "$$" + aug([["1", "1", "1", "1", "0"], ["1", "1", "3", "3", "0"], ["-1", "-1", "1", "1", "0"]], 4) + r"\to" + aug([["1", "1", "1", "1", "0"], ["0", "0", "2", "2", "0"], ["0", "0", "2", "2", "0"]], 4) + r"\to" + aug([["1", "1", "1", "1", "0"], ["0", "0", "2", "2", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$",
      r"עמודות מס׳ 1,3 של המטריצה המדורגת מובילות, אז $\mathrm{Col}\,A$ בסיס של $\left\{" + pm("1", "1", "-1") + "," + pm("1", "3", "1") + r"\right\}$, כלומר בסיס של $\mathrm{Im}\,T$ הוא $\left(1+x-x^2,\ 1+3x+x^2\right)$ ואז $\dim(\mathrm{Im}\,T)=2$.",
      "$$" + r"\to" + aug([["1", "1", "1", "1", "0"], ["0", "0", "1", "1", "0"], ["0", "0", "0", "0", "0"]], 4) + r"\to" + aug([["1", "1", "0", "0", "0"], ["0", "0", "1", "1", "0"], ["0", "0", "0", "0", "0"]], 4)
      + r"\Rightarrow\begin{cases}x_1=-t\\x_2=t\\x_3=-s\\x_4=s\end{cases}\Rightarrow" + pm("x_1", "x_2", "x_3", "x_4") + "=t" + pm("-1", "1", "0", "0") + "+s" + pm("0", "0", "-1", "1") + "$$",
      r"אז $\mathrm{Ker}\,T$ בסיס של $\mathrm{Nul}\,A$ הוא $\left\{" + pm("-1", "1", "0", "0") + "," + pm("0", "0", "-1", "1") + r"\right\}$ ואז $\dim(\mathrm{Ker}\,T)=2$."),
    12, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חד חד ערכית? האם $T$ על? נמקו.",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=2\neq0$, ו-$T$ לא על כי $\dim(\mathrm{Im}\,T)=2\neq3=\dim\mathbb{R}_2[t]$.",
    4, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטר $k$ מתקיים $k+11t+t^2\in\mathrm{Im}\,T$?",
    J(r"$$k+11t+t^2\in\mathrm{Im}\,T\ \Leftrightarrow\ " + pm("k", "11", "1") + r"\in\mathrm{Col}\,A\ \Leftrightarrow\ " + pm("k", "11", "1") + "=x_1" + pm("1", "1", "-1") + "+x_2" + pm("1", "3", "1") + "$$",
      "$$" + aug([["1", "1", "k"], ["1", "3", "11"], ["-1", "1", "1"]], 2) + r"\to" + aug([["1", "1", "k"], ["0", "2", "11-k"], ["0", "2", "1+k"]], 2) + r"\to" + aug([["1", "1", "k"], ["0", "2", "11-k"], ["0", "0", "-10+2k"]], 2) + r"\Rightarrow-10+2k=0\Rightarrow k=5$$"),
    4, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"נתונה העתקה לינארית $F:\mathbb{R}_1[x]\to\mathbb{R}_1[x]$ כך ש-$F(a+bx)=(a-2b)+(-2a+4b)x$. מצאו את המטריצה המייצגת $[F]_B^B$ של $F$, כאשר $B=\{1-x,1+x\}$ בסיס של $\mathbb{R}_1[x]$.",
    J(r"$E=(1,x)$ בסיס סטנדרטי של $\mathbb{R}_1[x]$. $B=\{1-x,1+x\}$ בסיס אחר של $\mathbb{R}_1[x]$.",
      r"$\left|\begin{matrix}1&1\\-1&1\end{matrix}\right|=2\neq0$ אז $B=(1-x,1+x)$ בסיס של $\mathbb{R}_1[x]$. לכן $[I]_E^B=" + pm("1&1", "-1&1") + r"$.",
      r"$$F(a+bx)=(a-2b)+(-2a+4b)x\ \Rightarrow\ F(1-x)=3-6x,\ F(1+x)=-1+2x\ \Rightarrow\ [F]_E^B=" + pm("3&-1", "-6&2") + "$$",
      r"$$[F]_B^B=[I]_B^E[F]_E^B[I]_B^B=" + pm("1&1", "-1&1") + r"^{-1}" + pm("3&-1", "-6&2") + pm("1&0", "0&1") + r"=\frac{1}{2}" + pm("1&-1", "1&1") + pm("3&-1", "-6&2") + "$$",
      r"$$=\frac{1}{2}" + pm("9&-3", "-3&1") + "=" + pm(r"\frac{9}{2}&-\frac{3}{2}", r"-\frac{3}{2}&\frac{1}{2}") + "$$"),
    5))

exam = {
    "examCode": "22B-A",
    "examLabel": "מבחן סוף סמסטר ב׳ תשפ״ב, מועד א׳ (07.06.2022)",
    "year": 2022,
    "examDate": "07.06.2022",
    "sourceFile": "22B-A exam + official solution (PDF)",
    "solutionFile": "22B-A exam + official solution (PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
