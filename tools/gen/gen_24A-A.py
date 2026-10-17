# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-A.json -- linear algebra, semester A 2024, moed A (31.03.2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-A.py

Source: 10pp, exam text and official solution interleaved in one PDF. Five questions of 25 points (best 4 count),
18 items. Q1-Q3 and Q5 are typed solutions, Q4's solution is handwritten (tablet) in the same file.
(The triage counter saw 4 of 5 questions; the printed exam has 5.)

Transcription notes
- Parts are single letters in the raw schema. Printed numbering -> raw part: Q1: 1.a->א, 1.b->ב, "ב"->ג;
  Q3: 1.a->א, 1.b->ב, 2->ג; Q5: 1.a->א, 1.b->ב, 1.c->ג, 2->ד.
- Q1: the stem of part א is shared by 1.a and 1.b and is placed in a context.
- Q2: the printed solution has no separate text for part ד; its content is the closing paragraph of the part-ג
  solution (particular solution + homogeneous direction), repeated in the ד solution.
- Q2: the official reduction divides by k, so k=0 appears among "suspect values"; the official text then treats
  k=0 as a unique-solution case. Kept as printed (sympy: the determinant is (k-2)(k+5)).
- Q4: handwritten solution; the sentence about linear independence is partly hard to read, written as
  "הווקטורים שקיבלנו בלתי תלויים לינארית" as the handwriting says. The sum is computed by row reduction with the
  vectors written as rows.

Checks (sympy, tools/verify/24A-A/verify_24A-A.py): every official computation reproduces (inverse and its
five-factor product, D and P, rank by k, bases and dimensions, Ker/Im of T, k=m=1, change-of-basis matrix).
No mismatch, no hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-A.json"


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


def col(*v):
    return pm(*[[c] for c in v])


# ------------------------------------------------------------------ contexts
contexts = {
    "c1": {"kind": "text", "title": "שאלה 1 - מטריצה המקיימת משוואה",
           "text": r"נתונה מטריצה ריבועית $A$ המקיימת את $A^2+A+I=0$."},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": "נתונה מערכת המשוואות הלינאריות:\n"
                   r"$$\begin{cases} x\ \ \ \ \ \ \ \ \ -3z=-3\\ 2x+ky-z=-2\\ x+2y+kz=1\end{cases}$$" "\n"
                   r"כאשר $k$ הוא פרמטר ממשי."},
    "c3": {"kind": "text", "title": "שאלה 3.1 - המטריצה A",
           "text": "נתונה המטריצה\n"
                   r"$$A=" + pm("1&-1&1", "0&1&1", "-1&1&1") + "$$"},
    "c4": {"kind": "text", "title": "שאלה 4 - שני תתי מרחבים של R^3",
           "text": r"יהיו $W_1$ ו-$W_2$ שני תתי מרחבים של מרחב וקטורי $\mathbb{R}^3$ המוגדרים כדלקמן:" "\n"
                   r"$$W_1=\left\{\vec r=" + col("x", "y", "z") + r"\ \Big|\ z=x;\ x,y,z\in\mathbb{R}\right\}$$" "\n"
                   r"$$W_2=\left\{\vec{r'}=" + col("x'", "y'", "z'") + r"\ \Big|\ y'=x';\ x',y',z'\in\mathbb{R}\right\}$$"},
    "c5": {"kind": "text", "title": "שאלה 5.1 - העתקה מפולינומים ל-R^4",
           "text": r"נתונה העתקה לינארית $T:\mathbb{R}_3[x]\to\mathbb{R}^4$ המוגדרת על ידי:" "\n"
                   r"$$T(1)=" + col(1, 2, 3, 4) + r",\quad T(x)=" + col(1, 3, 4, 5) + r",\quad T(x^2)=" + col(2, 2, 4, 6)
                   + r",\quad T(x^3)=" + col(2, 3, 5, 7) + "$$"},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "matrix_proofs",
    r"הוכיחו כי $A$ הפיכה ו-$A^2=A^{-1}$.",
    r"$$A^2+A+I=0\ \Rightarrow\ A(A+I)=-I\ \Rightarrow\ A(-A-I)=I\ \Rightarrow\ A^{-1}=-A-I\overset{(*)}{=}A^2$$" "\n"
    r"(*) לפי הנתון $A^2=-A-I$.",
    9, contextId="c1"))

questions.append(Q(
    1, "ב", "proof", "matrix_proofs",
    r"הוכיחו כי $A^2-A+I$ הפיכה.",
    r"$$A^2-A+I\overset{(*)}{=}(-A-I)-A+I=-2A\ \Rightarrow\ \left(A^2-A+I\right)^{-1}=(-2A)^{-1}=-\frac12A^{-1}$$" "\n"
    r"(*) לפי הנתון $A^2=-A-I$. (מכיוון ש-$A$ הפיכה, גם $-2A$ הפיכה, ולכן $A^2-A+I$ הפיכה.)",
    8, contextId="c1"))

questions.append(Q(
    1, "ג", "proof", "matrix_proofs",
    r"הוכיחו או הפריכו: אם $A,B$ מטריצות ריבועיות, אז $\mathrm{tr}(AB)=\mathrm{tr}(A)\cdot\mathrm{tr}(B)$.",
    r"הטענה אינה נכונה. דוגמה נגדית: נגדיר" "\n"
    r"$$A=" + pm("1&0", "0&0") + r",\qquad B=" + pm("0&0", "0&1") + "$$\n"
    r"אז $\mathrm{tr}(A)=\mathrm{tr}(B)=1$, ולכן $\mathrm{tr}(A)\cdot\mathrm{tr}(B)=1$. אבל מאחר ש-$AB=[0]$, נובע כי $\mathrm{tr}(AB)=0$.",
    8))

# ------------------------------------------------------------------ Q2
z2 = r"\left(\begin{array}{ccc|c}"
questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"עבור אילו ערכים של $k$ יש פתרון יחיד למערכת? מצאו את הפתרון כתלות בפרמטר.",
    "נציג את המערכת בצורת מטריצת מקדמים מורחבת ונדרג:\n"
    "$$" + aug([["1", "0", "-3", "-3"], ["2", "k", "-1", "-2"], ["1", "2", "k", "1"]]) + arrow(r"\substack{R_3-R_1\to R_3\\R_2-2R_1\to R_2}")
    + aug([["1", "0", "-3", "-3"], ["0", "k", "5", "4"], ["0", "2", "k+3", "4"]]) + arrow(r"\substack{\frac1k R_2\to R_2,\ k\neq0\\\frac12R_3\to R_3}")
    + aug([["1", "0", "-3", "-3"], ["0", "1", r"\frac5k", r"\frac4k"], ["0", "1", r"\frac{k+3}{2}", "2"]]) + "$$\n"
    "$$" + arrow(r"R_3-R_2\to R_3")
    + aug([["1", "0", "-3", "-3"], ["0", "1", r"\frac5k", r"\frac4k"], ["0", "0", r"\frac{k^2+3k-10}{2k}", r"\frac{2k-4}{k}"]])
    + arrow(r"\substack{(2k)R_3\to R_3\\kR_2\to R_2}")
    + aug([["1", "0", "-3", "-3"], ["0", "k", "5", "4"], ["0", "0", "(k-2)(k+5)", "4(k-2)"]]) + "$$\n"
    r"קיבלנו שלושה ערכים חשודים: $k_1=0,\ k_2=2,\ k_3=-5$." "\n"
    r"עבור $k_1=0$ נקבל פתרון יחיד. אכן, לכל $k\neq2,-5$ יש פתרון יחיד מהצורה:" "\n"
    r"$$(x,y,z)=\left(\frac{-3(k+1)}{k+5},\ \frac{4}{k+5},\ \frac{4}{k+5}\right)$$",
    7, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור אילו ערכים של $k$ אין פתרון למערכת?",
    r"עבור $k_3=-5$ נקבל שורת סתירה ואין פתרון (שורת האפס בצד שמאל מול $4(k-2)=-28\neq0$ בצד ימין), כלומר אין פתרון עבור $k=-5$.",
    6, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור אילו ערכים של $k$ יש אינסוף פתרונות? הציגו את הפתרונות כתלות בפרמטר.",
    r"עבור $k_2=2$ נקבל שורת אפסים, כלומר אינסוף פתרונות. נציב במערכת המקורית:" "\n"
    "$$" + aug([["1", "0", "-3", "-3"], ["0", "2", "5", "4"], ["0", "0", "0", "0"]]) + "$$\n"
    "ונקבל, $t\\in\\mathbb{R}$:\n"
    "$$" + col("x", "y", "z") + "=" + col(-3, 2, 0) + "+t" + col(6, -5, 2) + "$$\nאו\n$$" + col("x", "y", "z") + "=" + col(-3, 2, 0)
    + "+t" + col(3, r"-5/2", 1) + "$$\n"
    "הפתרון האינסופי הוא ישר חיתוך בשלושה מישורים ממדים. הווקטור ההזזה הוא פתרון פרטי, ווקטור הכיוון הוא פתרון של המערכת ההומוגנית.",
    7, contextId="c2"))

questions.append(Q(
    2, "ד", "proof", "linear_systems",
    r"במקרה של אינסוף פתרונות, הראו שהפתרון הכללי הוא סכום של פתרון פרטי של המערכת ופתרון כללי של המערכת ההומוגנית.",
    r"עבור $k=2$ הפתרון הכללי הוא $\vec x=\vec p+t\vec d$ כאשר $t\in\mathbb{R}$ והווקטורים הם:" "\n"
    "$$\\vec p=" + col(-3, 2, 0) + r",\qquad \vec d=" + col(6, -5, 2) + "$$\n"
    r"הווקטור $\vec p$ הוא פתרון פרטי של המערכת המקורית (הזזה), והווקטור $t\vec d$ הוא הפתרון הכללי של המערכת ההומוגנית "
    r"המתאימה (הווקטור $\vec d$ מהווה בסיס למרחב הפתרונות שלה). לכן הפתרון הכללי של המערכת הוא פתרון פרטי ועוד פתרון כללי של המערכת ההומוגנית.",
    5, contextId="c2"))

# ------------------------------------------------------------------ Q3
questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הוכיחו ש-$A$ הפיכה ע״י מציאת המטריצה $A^{-1}$.",
    "$$[A\\,|\\,I]=" + aug([["1", "-1", "1", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["-1", "1", "1", "0", "0", "1"]])
    + arrow("R_3+R_1")
    + aug([["1", "-1", "1", "1", "0", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "2", "1", "0", "1"]])
    + arrow("R_1+R_2")
    + aug([["1", "0", "2", "1", "1", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "2", "1", "0", "1"]]) + "$$\n"
    "$$" + arrow(r"R_3\to\frac12R_3")
    + aug([["1", "0", "2", "1", "1", "0"], ["0", "1", "1", "0", "1", "0"], ["0", "0", "1", r"\frac12", "0", r"\frac12"]])
    + arrow("R_2-R_3")
    + aug([["1", "0", "2", "1", "1", "0"], ["0", "1", "0", r"-\frac12", "1", r"-\frac12"], ["0", "0", "1", r"\frac12", "0", r"\frac12"]])
    + arrow("R_1-2R_3")
    + aug([["1", "0", "0", "0", "1", "-1"], ["0", "1", "0", r"-\frac12", "1", r"-\frac12"], ["0", "0", "1", r"\frac12", "0", r"\frac12"]])
    + r"=[I\,|\,A^{-1}]$$" "\n"
    r"סיכום:" "\n"
    "$$A^{-1}=" + pm("0&1&-1", r"-\frac12&1&-\frac12", r"\frac12&0&\frac12") + "$$",
    6, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"הציגו את $A^{-1}$ בצורת כפל של מטריצות אלמנטריות.",
    "ידוע שביצוע כל פעולת שורה אלמנטארית במטריצה $A$ שקול להכפלת $A$ במטריצה אלמנטארית מתאימה. כך נוכל לתאר את התהליך בעזרת מטריצות אלמנטריות הבאות:\n"
    "$$" + arrow("R_3+R_1") + r"E_1=" + pm("1&0&0", "0&1&0", "1&0&1") + r",\quad"
    + arrow("R_1+R_2") + r"E_2=" + pm("1&1&0", "0&1&0", "0&0&1") + r",\quad"
    + arrow(r"R_3\to\frac12R_3") + r"E_3=" + pm("1&0&0", "0&1&0", r"0&0&\frac12") + "$$\n"
    "$$" + arrow("R_2-R_3") + r"E_4=" + pm("1&0&0", "0&1&-1", "0&0&1") + r",\quad"
    + arrow("R_1-2R_3") + r"E_5=" + pm("1&0&-2", "0&1&0", "0&0&1") + "$$\n"
    r"מכיוון ש-$E_5\cdot E_4\cdot E_3\cdot E_2\cdot E_1\cdot A=I$, אז נקבל:" "\n"
    r"$$A^{-1}=E_5\cdot E_4\cdot E_3\cdot E_2\cdot E_1$$",
    7, contextId="c3"))

questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה המטריצה $B=" + pm("1&1&0", "0&-2&0", "-1&0&3") + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $PD=BP$.",
    r"נבנה את הפולינום האופייני של $B$:" "\n"
    r"$$\det(B-\lambda I)=\begin{vmatrix}1-\lambda&1&0\\0&-2-\lambda&0\\-1&0&3-\lambda\end{vmatrix}=(1-\lambda)(-2-\lambda)(3-\lambda)$$" "\n"
    r"ומכאן נקבל שהערכים העצמיים של $B$ הם $\lambda_1=1,\ \lambda_2=-2,\ \lambda_3=3$ ולכן $B$ ניתנת לליכסון. נמצא את המרחבים העצמיים של $B$:" "\n"
    r"(*) אם $\lambda=\lambda_1=1$, אז נקבל $B-\lambda I=B-I=" + pm("0&1&0", "0&-3&0", "-1&0&2") + r"\to"
    + pm("1&0&-2", "0&-3&0", "0&1&0") + r"\to" + pm("1&0&-2", "0&1&0", "0&0&0") + r"$ והמרחב העצמי המתאים מתקבל בצורה "
    r"$\vec x_1=" + col("2t", 0, "t") + "=t" + col(2, 0, 1) + "$.\n"
    r"(*) אם $\lambda=\lambda_2=-2$, אז נקבל $B-\lambda I=B+2I=" + pm("3&1&0", "0&0&0", "-1&0&5") + r"\to"
    + pm("1&0&-5", "3&1&0", "0&0&0") + r"\to" + pm("1&0&-5", "0&1&15", "0&0&0") + r"$ והמרחב העצמי המתאים מתקבל בצורה "
    r"$\vec x_2=" + col("5t", "-15t", "t") + "=t" + col(5, -15, 1) + "$.\n"
    r"(*) אם $\lambda=\lambda_3=3$, אז נקבל $B-\lambda I=B-3I=" + pm("-2&1&0", "0&-5&0", "-1&0&0") + r"\to"
    + pm("1&0&0", "0&5&0", "2&-1&0") + r"\to" + pm("1&0&0", "0&1&0", "0&0&0") + r"$ והמרחב העצמי המתאים מתקבל בצורה "
    r"$\vec x_3=" + col(0, 0, "t") + "=t" + col(0, 0, 1) + "$.\n"
    "סיכום:\n"
    r"$$P=\left(\vec x_1\ \vec x_2\ \vec x_3\right)=" + pm("2&5&0", "0&-15&0", "1&1&1") + r",\qquad D=" + pm(r"\lambda_1&0&0", r"0&\lambda_2&0", r"0&0&\lambda_3")
    + "=" + pm("1&0&0", "0&-2&0", "0&0&3") + "$$",
    12))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של תתי המרחבים $W_1$ ו-$W_2$.",
    r"**תת מרחב $W_1$:** עבור כל $\vec r\in W_1$ מתקיים $z=x$, כלומר, כל וקטור כללי השייך ל-$W_1$ הוא מהצורה:" "\n"
    r"$$\vec r=" + col("x", "y", "x") + "=x" + col(1, 0, 1) + "+y" + col(0, 1, 0) + r",\qquad x,y\in\mathbb{R}$$" "\n"
    r"לכן $W_1=\mathrm{Sp}\left\{" + col(1, 0, 1) + "," + col(0, 1, 0) + r"\right\}$. קבוצת הווקטורים שקיבלנו היא קבוצה בלתי תלויה לינארית, ובגלל כך אנו קובעים את הבסיס:" "\n"
    r"$$B_{W_1}=\left\{" + col(1, 0, 1) + "," + col(0, 1, 0) + r"\right\},\qquad \dim W_1=2$$" "\n"
    r"**תת מרחב $W_2$:** עבור כל $\vec{r'}\in W_2$ מתקיים $y'=x'$, כלומר, כל וקטור כללי השייך ל-$W_2$ הוא מהצורה:" "\n"
    r"$$\vec{r'}=" + col("x'", "x'", "z'") + "=x'" + col(1, 1, 0) + "+z'" + col(0, 0, 1) + "$$\n"
    r"לכן $W_2=\mathrm{Sp}\left\{" + col(1, 1, 0) + "," + col(0, 0, 1) + r"\right\}$. קבוצת הווקטורים שקיבלנו היא קבוצה בלתי תלויה לינארית, ובגלל כך אנו קובעים את הבסיס:" "\n"
    r"$$B_{W_2}=\left\{" + col(1, 1, 0) + "," + col(0, 0, 1) + r"\right\},\qquad \dim W_2=2$$",
    7, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"חשבו את תת המרחב $W_1+W_2$, מצאו בסיס ומימד של תת מרחב זה.",
    r"$$W_1+W_2=\mathrm{Sp}\{B_{W_1},B_{W_2}\}=\mathrm{Sp}\left\{" + col(1, 0, 1) + "," + col(0, 1, 0) + "," + col(1, 1, 0) + "," + col(0, 0, 1) + r"\right\}$$" "\n"
    "קבוצת הווקטורים הנ״ל היא קבוצה פורשת, לא בהכרח בלתי תלויה לינארית, לכן יש לבצע דירוג (הווקטורים נכתבים כשורות):\n"
    "$$" + pm("1&0&1", "0&1&0", "1&1&0", "0&0&1") + arrow("R_1\\to R_1-R_4") + pm("1&0&0", "0&1&0", "1&1&0", "0&0&1") + arrow("R_3\\to R_3-R_2") + "$$\n"
    "$$" + pm("1&0&0", "0&1&0", "1&0&0", "0&0&1") + arrow(r"\substack{R_3\to R_3-R_1\\R_3\leftrightarrow R_4}") + pm("1&0&0", "0&1&0", "0&0&1", "0&0&0") + "$$\n"
    "מכאן אנו קובעים את הבסיס:\n"
    r"$$B_{W_1+W_2}=\left\{" + col(1, 0, 0) + "," + col(0, 1, 0) + "," + col(0, 0, 1) + r"\right\},\qquad \dim(W_1+W_2)=3$$",
    7, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"חשבו את תת המרחב $W_1\cap W_2$, מצאו בסיס ומימד של תת מרחב זה.",
    r"כל וקטור $\vec w$ השייך ל-$W_1\cap W_2$ ניתן לרשום בשתי צורות:" "\n"
    r"$$\vec w=\alpha_1" + col(1, 0, 1) + r"+\alpha_2" + col(0, 1, 0) + r",\qquad \vec w=-\beta_1" + col(1, 1, 0) + r"-\beta_2" + col(0, 0, 1) + "$$\n"
    r"מכאן נקבל מערכת משוואות הומוגנית עבור המקדמים $\{\alpha_1,\alpha_2,\beta_1,\beta_2\}$:" "\n"
    r"$$" + pm("1&0&1&0", "0&1&1&0", "1&0&0&1") + col(r"\alpha_1", r"\alpha_2", r"\beta_1", r"\beta_2") + "=" + col(0, 0, 0) + "$$\n"
    r"נדרג את מטריצת המקדמים:" "\n"
    r"$$" + pm("1&0&1&0", "0&1&1&0", "1&0&0&1") + arrow("R_3\\to R_3-R_1") + pm("1&0&1&0", "0&1&1&0", "0&0&-1&1")
    + r"$$" "\n"
    r"המשתנה $\beta_2$ הוא משתנה חופשי (מקדם חופשי), ומקבלים $\beta_1=-t,\ \beta_2=-t,\ t\in\mathbb{R}$." "\n"
    r"מכאן, כל וקטור $\vec w$ השייך ל-$W_1\cap W_2$ ניתן לרשום בצורה הבאה:" "\n"
    r"$$\vec w=t" + col(1, 1, 0) + "+t" + col(0, 0, 1) + "=t" + col(1, 1, 1) + "$$\n"
    r"כלומר, $W_1\cap W_2=\mathrm{Sp}\left\{" + col(1, 1, 1) + r"\right\}$. כך ש:" "\n"
    r"$$B_{W_1\cap W_2}=\left\{" + col(1, 1, 1) + r"\right\},\qquad \dim(W_1\cap W_2)=1$$",
    7, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם הווקטור $" + col(1, 1, 1) + r"$ שייך לתת מרחב $W_1\cap W_2$? נמקו!",
    r"מכיוון שהווקטור $" + col(1, 1, 1) + r"$ הוא כפולה של וקטור הבסיס של $W_1\cap W_2$, הוא שייך לתת מרחב $W_1\cap W_2$.",
    4, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד והבסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    r"נסמן $F=(1,x,x^2,x^3)$ בסיס סטנדרטי של $\mathbb{R}_3[x]$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^4$. מכאן נקבל שהמטריצה המייצגת הסטנדרטית היא" "\n"
    r"$$A=[T]_E^F=" + pm("1&1&2&2", "2&3&2&3", "3&4&4&5", "4&5&6&7") + "$$\n"
    "$$" + aug([["1", "1", "2", "2", "0"], ["2", "3", "2", "3", "0"], ["3", "4", "4", "5", "0"], ["4", "5", "6", "7", "0"]], 4) + r"\Leftrightarrow"
    + aug([["1", "1", "2", "2", "0"], ["0", "1", "-2", "-1", "0"], ["0", "1", "-2", "-1", "0"], ["0", "1", "-2", "-1", "0"]], 4) + r"\Leftrightarrow"
    + aug([["1", "1", "2", "2", "0"], ["0", "1", "-2", "-1", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$\n"
    r"ברור שהעמודות מס׳ 1,2 של המטריצה המדורגת הן עמודות הציר ובלתי תלויות לינארית זו בזו ויוצרות בסיס במרחב העמודות של $A$. לכן" "\n"
    r"$$\mathrm{Col}A=\mathrm{sp}\left\{" + col(1, 2, 3, 4) + "," + col(1, 3, 4, 5) + r"\right\}=\mathrm{Im}(T)$$" "\n"
    r"זאת אומרת $\dim\mathrm{Im}\,T=2$." "\n"
    r"בנוסף," "\n"
    "$$" + aug([["1", "1", "2", "2", "0"], ["0", "1", "-2", "-1", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + r"\Leftrightarrow"
    + aug([["1", "0", "4", "3", "0"], ["0", "1", "-2", "-1", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4)
    + r"\Leftrightarrow\begin{cases}x_1=-4s_1-3s_2\\x_2=2s_1+s_2\\x_3=s_1\\x_4=s_2\end{cases}\Leftrightarrow"
    + col("x_1", "x_2", "x_3", "x_4") + "=s_1" + col(-4, 2, 1, 0) + "+s_2" + col(-3, 1, 0, 1) + "$$\n"
    r"זאת אומרת בסיס של $\mathrm{Ker}\,T$ הוא $\left(-4+2x+x^2,\ -3+x+x^3\right)$:" "\n"
    r"$$\mathrm{null\,sp}(A)=\mathrm{sp}\left\{" + col(-4, 2, 1, 0) + "," + col(-3, 1, 0, 1) + r"\right\}=\ker(T)$$" "\n"
    r"ואז $\dim\mathrm{Ker}\,T=2$.",
    12, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חד חד ערכית? האם $T$ על? נמקו.",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=2\neq0$. $T$ לא על כי $\dim\mathrm{Im}\,T=2\neq\dim\mathbb{R}^4=4$.",
    3, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטרים $k,m$ מתקיים $-7+3x+kx^2+mx^3\in\mathrm{Ker}\,T$?",
    r"הפולינום שייך ל-$\mathrm{Ker}\,T$ אם ורק אם וקטור הקואורדינטות שלו $(-7,3,k,m)$ הוא צירוף לינארי של בסיס ה-$\mathrm{Ker}\,T$, כלומר המערכת עם העמודה האחרונה $(-7,3,k,m)$ פתירה:" "\n"
    "$$" + aug([["-4", "-3", "-7"], ["2", "1", "3"], ["1", "0", "k"], ["0", "1", "m"]], 2) + r"\to"
    + aug([["1", "0", "k"], ["0", "1", "m"], ["-4", "-3", "-7"], ["2", "1", "3"]], 2) + r"\to"
    + aug([["1", "0", "k"], ["0", "1", "m"], ["0", "-3", "-7+4k"], ["0", "1", "3-2k"]], 2) + r"\to"
    + aug([["1", "0", "k"], ["0", "1", "m"], ["0", "0", "-7+4k+3m"], ["0", "0", "3-2k-m"]], 2) + "$$\n"
    r"$$\begin{cases}4k+3m=7\\2k+m=3\end{cases}\Rightarrow\begin{cases}k=1\\m=1\end{cases}$$",
    5, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "vector_spaces",
    r"נתונים בסיסים $B=\left(" + col(3, 2) + "," + col(7, 5) + r"\right)$, $C=\left(" + col(5, 3) + "," + col(3, 2) + r"\right)$ של מרחב $\mathbb{R}^2$. "
    r"מצאו את מטריצת המעבר $[I]_C^B$ מבסיס $B$ לבסיס $C$ ($M_{C\leftarrow B}(id)$ - מטריצת העתקת הזהות מבסיס $B$ לבסיס $C$). (שאלה 5 סעיף 2; אין קשר בין סעיף 1 לסעיף 2.)",
    r"נסמן ב-$E$ בסיס סטנדרטי של $\mathbb{R}^2$:" "\n"
    r"$$[I]_E^B=" + pm("3&7", "2&5") + r",\qquad [I]_E^C=" + pm("5&3", "3&2") + "$$\n"
    r"**שיטה 1:**" "\n"
    r"$$[I]_C^B=[I]_C^E[I]_E^B=\left([I]_E^C\right)^{-1}[I]_E^B=" + pm("5&3", "3&2") + r"^{-1}" + pm("3&7", "2&5") + "="
    + pm("2&-3", "-3&5") + pm("3&7", "2&5") + "=" + pm("0&-1", "1&4") + "$$\n"
    r"**שיטה 2:**" "\n"
    "$$" + aug([["5", "3", "3", "7"], ["3", "2", "2", "5"]], 2) + r"\to" + aug([["-1", "-1", "-1", "-3"], ["3", "2", "2", "5"]], 2) + r"\to"
    + aug([["-1", "-1", "-1", "-3"], ["0", "-1", "-1", "-4"]], 2) + r"\to" + "$$\n"
    "$$" + aug([["1", "1", "1", "3"], ["0", "1", "1", "4"]], 2) + r"\to" + aug([["1", "0", "0", "-1"], ["0", "1", "1", "4"]], 2)
    + r"\to[I]_C^B=" + pm("0&-1", "1&4") + "$$",
    5))

exam = {
    "examCode": "24A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״ד, מועד א׳ (31.03.2024)",
    "year": 2024,
    "examDate": "31.03.2024",
    "sourceFile": "24A-A exam + official solution (single PDF)",
    "solutionFile": "24A-A exam + official solution (single PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
