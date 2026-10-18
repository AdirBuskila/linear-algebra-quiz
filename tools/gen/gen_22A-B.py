# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-B.json -- linear algebra, semester A 2022, moed B (13.03.2022), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22A-B.py

Source: one PDF (7pp): the exam text followed question by question by the typed official solution.
Five questions of 25 points (best 4 count), 20 items: 15 transcribed with the official solution, 5 held (Q4 a-e).

Transcription notes
- Q4 (subspaces U, W of R_3[x], parts a-e): the solution file has NO solution for Q4 (the solutions jump from Q3 to Q5).
  All five parts were held "no-key" and are now solved by the solver
  (solutionSource "solved", official false; checks appended to verify_22A-B.py). The exam prints "ממעלה שחוש", a typo of "ממעלה שלוש"; written as
  the latter.
- Q2 labels: the exam prints the parts as א (10 pts), א (5), ב (5), ג (5): the two labels collide. The official solution
  labels them א, ב, ג, ד; those labels are used here (a: classification, b: a=2,b=1, c: a=5,b=7, d: the matrix).
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (C,D); in the raw schema item 2 is part "gimel".
- Q5 has two numbered items: item 1 (T, parts a-c) and item 2 (F), which is part "dalet" here.
- Q1 b: the exam asks to show that A is invertible; the official solution concludes "B is invertible". Its argument
  (2^4 det(A) det(B) != 0) gives both det(A) != 0 and det(B) != 0 (A is also immediate from |A|=2); a one-line remark is
  added to the solution, logged in ASK_ADIR as FYI.
- Q1 d: the official prints det(B^1)=32/81 (typo for B^-1); written as B^-1, value unchanged.
- Q3 item 1 b: the official's basis (1,2,3),(0,1,2),(0,0,1) is not a set of rows of A; its first two rows span the row space of A
  (the second equals -(1/3)(row2-4 row1)), the third completes the basis. Kept as is.

Checks (sympy, tools/verify/22A-B/verify_22A-B.py): det identity of Q1 a, det(B)=81/32 for a model, the Q2 case analysis
(unique for a != 5,-1; a=5: b=7 infinite else none; a=-1: b=-5 infinite else none), the a=2 solution, the a=5,b=7 family,
det of Q2 d and its roots, det and adjugate inverse of Q3, rank 2 at a=9 and the completed basis, the antisymmetry model of Q3.2,
Ker/Im of T, k=4, [F]_B^B. No mismatch.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-B.json"


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
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם שני פרמטרים",
           "text": J(r"נתונה המערכת עם הפרמטרים $a,b\in\mathbb{R}$:",
                     r"$$\begin{cases} x+2y+2z=1\\ x+ay+3z=3\\ x+11y+az=b\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
           "text": r"נתונה המטריצה $A=" + pm("1&2&3", "4&5&6", "7&8&a") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של פולינומים",
           "text": J(r"יהי $\mathbb{R}_3[x]$ מרחב של פולינומים ממשיים ממעלה שלוש לכל היותר. נגדיר שתי תתי קבוצות של מרחב זה:",
                     r"$U=\{p(x)\in\mathbb{R}_3[x]:\ p(-x)=-p(x)\}$",
                     r"$W=\{p(x)\in\mathbb{R}_3[x]:\ p'(1)=0\}$")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": J(r"נתונה העתקה לינארית $T:\mathbb{R}_3[t]\to\mathbb{R}^3$ המוגדרת על ידי:",
                     r"$$T(1)=" + pm("1", "1", "1") + r",\ T(t)=" + pm("1", "2", "3") + r",\ T\left(t^2\right)=" + pm("-1", "0", "1") + r",\ T\left(t^3\right)=" + pm("3", "4", "5") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "determinants",
    r"נתון $(PQ)^{-1}CPQ=D$. הוכיחו $|C|=|D|$.",
    J(r"אם נחשב דטרמיננט משני הצדדים של המשוואה הנתונה, אז נקבל ש-",
      r"$$\det\left[(PQ)^{-1}CPQ\right]=\det(D)\Rightarrow\det\left[Q^{-1}P^{-1}CPQ\right]=\det(D)\Rightarrow$$",
      r"$$\Rightarrow\det\left(Q^{-1}\right)\det\left(P^{-1}\right)\det(C)\det(P)\det(Q)=\det D\Rightarrow\frac{1}{\det(Q)}\cdot\frac{1}{\det(P)}\det(C)\det(P)\det(Q)=\det(D)\Rightarrow\det(C)=\det(D)$$"),
    7))

questions.append(Q(
    1, "ב", "proof", "determinants",
    r"נתונות $A,B$ מטריצות מסדר 4 המקיימות $2AB+3I=0$ ובנוסף $|A|=2$. הראו כי $A$ הפיכה.",
    J(r"נתון ש-$2AB+3I=0$, אז $2AB=-3I$. מכאן נקבל",
      r"$$\det(2AB)=\det(-3I)\Rightarrow\det(2A)\det(B)=(-3)^4\det(I)=3^4\neq0$$",
      r"ומכאן $\det(2A)\det(B)=2^4\det(A)\det(B)\neq0\Leftarrow\det(B)\neq0$ ולכן **$B$ היא מטריצה הפיכה**.",
      r"**הערה:** מאי-האפסיות של המכפלה $2^4\det(A)\det(B)$ נובע גם $\det(A)\neq0$, כלומר $A$ הפיכה (וזה נובע גם ישירות מהנתון $|A|=2$)."),
    7))

questions.append(Q(
    1, "ג", "computation", "determinants",
    r"חשבו את $|B|$.",
    J(r"מהמשוואה $\det(2A)\det(B)=(-3)^4\det(I)=3^4$ נקבל ש-$2^4\cdot2\cdot\det(B)=3^4$ ומכאן נובע ש-",
      r"$$\det(B)=\frac{3^4}{2^5}=\frac{81}{32}$$"),
    8))

questions.append(Q(
    1, "ד", "computation", "determinants",
    r"חשבו את $\left|B^{-1}\right|$.",
    J(r"מהתוצאה של הסעיף הקודם נובע ש-",
      r"$$\det\left(B^{-1}\right)=\frac{32}{81}$$"),
    3))

# ------------------------------------------------------------------ Q2
R0 = [["1", "2", "2", "1"], ["1", "a", "3", "3"], ["1", "11", "a", "b"]]
R1 = [["1", "2", "2", "1"], ["0", "a-2", "1", "2"], ["0", "9", "a-2", "b-1"]]
R2 = [["1", "2", "2", "1"], ["0", "1", r"\frac{1}{a-2}", r"\frac{2}{a-2}"], ["0", "9", "a-2", "b-1"]]
ECH = J(r"המטריצה המורחבת של המערכת הינה",
        "$$" + aug(R0) + "$$",
        r"נבצע דירוג",
        "$$" + aug(R0) + arrow(r"\substack{R_2\to R_2-R_1\\R_3\to R_3-R_1}") + aug(R1) + arrow(r"R_2\to\frac{R_2}{a-2}") + aug(R2) + "$$")

SOL_2A = J(ECH,
           r"כאשר הפעולה האחרונה ביצענו תחת ההנחה $a\neq2$. נסתכל בנפרד על המקרה $a=2$.",
           "$$" + aug([["1", "2", "2", "1"], ["0", "0", "1", "2"], ["0", "9", "0", "b-1"]]) + arrow(r"R_3\to\frac{R_3}{9}") + aug([["1", "2", "2", "1"], ["0", "0", "1", "2"], ["0", "1", "0", r"\frac{b-1}{9}"]]) + arrow(r"R_2\leftrightarrow R_3") + aug([["1", "2", "2", "1"], ["0", "1", "0", r"\frac{b-1}{9}"], ["0", "0", "1", "2"]]) + "$$",
           r"לכן במקרה זה קיים פתרון יחיד הנתון על ידי",
           r"$$" + pm("x", "y", "z") + "=" + pm(r"-3-\frac{2(b-1)}{9}", r"\frac{b-1}{9}", "2") + "$$",
           r"נמשיך בדירוג תחת ההנחה $a\neq2$",
           "$$" + aug([["1", "2", "2", "1"], ["0", "1", r"\frac{1}{a-2}", r"\frac{2}{a-2}"], ["0", "9", "a-2", "b-1"]]) + arrow(r"R_3\to R_3-9R_2")
           + aug([["1", "2", "2", "1"], ["0", "1", r"\frac{1}{a-2}", r"\frac{2}{a-2}"], ["0", "0", r"a-2-\frac{9}{a-2}", r"b-1-\frac{18}{a-2}"]]) + "$$",
           r"$$a-2-\frac{9}{a-2}=0\Leftrightarrow a^2-4a+4-9=0\Leftrightarrow a=5,-1$$",
           r"**ולכן אם $a\neq5,-1$ קיים למערכת פתרון יחיד.** במקרה שבו $a=5,-1$ נבדוק",
           r"$$b-1-\frac{18}{a-2}=0\Leftrightarrow(a-2)(b-1)-18=0$$",
           r"ולכן אם $a=5$ אז $3(b-1)=18$ ולכן **תחת ההנחה $a=5$ למערכת אין פתרונות אם $b\neq7$ ויש אינסוף פתרונות אם $b=7$.**",
           r"אם $a=-1$ מתקבלת המשוואה $-3(b-1)=18\Rightarrow b=-5$ כלומר **תחת ההנחה $a=-1$ למערכת אין פתרונות אם $b\neq-5$ ואינסוף פתרונות אם $b=-5$.**")
questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"קבעו עבור אלו ערכי $a,b\in\mathbb{R}$ למערכת יש פתרון יחיד/אינסוף פתרונות/אין פתרון.",
    SOL_2A,
    10, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"הציגו את כל פתרונות המערכת במקרה $a=2,\ b=1$.",
    J(r"כפי שקיבלנו בסעיף א׳ הפתרון היחיד במקרה הנ״ל הינו",
      r"$$" + pm("x", "y", "z") + "=" + pm("-3", "0", "2") + "$$"),
    5, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"הציגו את כל פתרונות המערכת במקרה $a=5,\ b=7$.",
    J(r"עבור $a=5,\ b=7$ מתקבלת המערכת",
      r"$$" + aug([["1", "2", "2", "1"], ["0", "1", r"\frac{1}{3}", r"\frac{2}{3}"], ["0", "0", "0", "0"]]) + "$$",
      r"המשתנה החופשי הינו $z=t$ ומתקבל אוסף הפתרונות",
      r"$$" + pm("x", "y", "z") + "=" + pm(r"-\frac{1}{3}-\frac{4}{3}t", r"\frac{2}{3}-\frac{t}{3}", "t") + "=" + pm(r"-\frac{1}{3}", r"\frac{2}{3}", "0") + r"+t\cdot" + pm(r"-\frac{4}{3}", r"-\frac{1}{3}", "1") + "$$"),
    5, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"נתונה המטריצה $A=" + pm("1&2&-2", "0&z&1", "1&0&z") + r"$ כאשר $z\in\mathbb{C}$ מספר מרוכב כל שהוא. מצאו עבור אלו ערכי $z$ המטריצה הפיכה.",
    J(r"הדטרמיננטה של המטריצה היא",
      r"$$\det\left(" + pm("1&2&-2", "0&z&1", "1&0&z") + r"\right)=z^2+2z+2$$",
      r"ולכן המטריצה אינה הפיכה בדיוק כאשר",
      r"$$z^2+2z+2=0$$",
      r"השורשים של המשוואה הינם",
      r"$$z_{1,2}=\frac{-2\pm\sqrt{4-8}}{2}=-1\pm i$$",
      r"כלומר $A$ הפיכה עבור כל $z\neq-1\pm i$."),
    5, contextId="c2"))

# ------------------------------------------------------------------ Q3
CF = pm("5a-48&-4a+42&-3", "-2a+24&a-21&6", "-3&6&-3")
ADJ = pm("5a-48&-2a+24&-3", "-4a+42&a-21&6", "-3&6&-3")
questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"עבור אילו ערכי הפרמטר $a$ המטריצה $A$ הפיכה? במקרה ש-$A$ הפיכה, חשבו את $A^{-1}$.",
    J(r"נחשב את הדטרמיננטה של $A$ ונבדוק מתי היא מתאפסת.",
      r"$$\det A=1\cdot\begin{vmatrix}5&6\\8&a\end{vmatrix}-2\cdot\begin{vmatrix}4&6\\7&a\end{vmatrix}+3\cdot\begin{vmatrix}4&5\\7&8\end{vmatrix}=-3a+27$$",
      r"הדטרמיננטה מתאפסת כאשר $a=9$.",
      r"עבור $a\neq9$ נחשב את $A^{-1}$ ע״י חישוב המטריצה $\mathrm{adj}(A)$. נחשב תחילה את מטריצת משלימים אלגבריים $C$ שמתאימה ל-$A$, כלומר $C=\mathrm{cof}(A)$:",
      r"$$C=\mathrm{cof}(A)=" + CF + "$$",
      r"והמטריצה ההופכית היא: $A^{-1}=\frac{1}{\det A}C^T=\frac{1}{\det A}\mathrm{adj}(A)$",
      r"$$A^{-1}=\frac{1}{-3a+27}" + ADJ + "$$"),
    8, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"עבור ערכי $a$ שעבורם $A$ אינה הפיכה, חשבו את דרגתה, $\mathrm{rank}(A)$, והשלימו את שורות $A$ לבסיס ל-$\mathbb{R}^3$.",
    J(r"עבור $a=9$, נקבל:",
      r"$$A=" + pm("1&2&3", "4&5&6", "7&8&9") + r"\sim" + pm("1&2&3", "0&1&2", "0&1&2") + r"\sim" + pm("1&2&3", "0&1&2", "0&0&0") + "$$",
      r"לפיכך $\mathrm{rank}(A)=2$. להשלים ל-$\mathbb{R}^3$:",
      r"$$A\to" + pm("1&2&3", "0&1&2", "0&0&1") + "$$"),
    7, contextId="c3"))

questions.append(Q(
    3, "ג", "proof", "matrix_proofs",
    r"תהיינה $C,D$ מטריצות סימטריות מאותו סדר ונתון כי $CD=-DC$. הוכח או תן דוגמה נגדית: מטריצה $CD$ היא מטריצה אנטי סימטרית.",
    J(r"$D$ ו-$C$ סימטריות, כלומר $D^T=D$ ו-$C^T=C$. מטריצה $CD$ היא מטריצה אנטי סימטרית אם מתקיים $(CD)^T=-CD$. נשתמש בחוקי השיחלוף והנתון ש-$CD=-DC$ ואז נקבל:",
      r"$$(CD)^T=D^TC^T=DC$$",
      r"אבל $CD=-DC$ ומכאן סופית נקבל:",
      r"$$(CD)^T=D^TC^T=DC=-CD$$",
      r"והטענה כאן נכונה."),
    10))

# ------------------------------------------------------------------ Q4 (no official solution: solved by the solver)
def S(part, question, solution, points):
    return Q(4, part, "computation", "vector_spaces", question, solution, points, contextId="c4",
             solutionSource="solved", official=False)


questions.append(S(
    "א", r"באמצעות הקריטריון לתת מרחב, הוכיחו כי $U$ הוא תת מרחב של $\mathbb{R}_3[x]$, מצאו בסיס ומימד ל-$U$.",
    J(r"**קריטריון לתת מרחב:**",
      r"1. פולינום האפס $0(x)$ מקיים $0(-x)=0=-0(x)$, ולכן $0\in U$ (ובפרט $U\neq\emptyset$).",
      r"2. סגירות לחיבור: אם $p,q\in U$ אז $(p+q)(-x)=p(-x)+q(-x)=-p(x)-q(x)=-(p+q)(x)$, ולכן $p+q\in U$.",
      r"3. סגירות לכפל בסקלר: אם $p\in U$ ו-$\alpha\in\mathbb{R}$ אז $(\alpha p)(-x)=\alpha p(-x)=-\alpha p(x)=-(\alpha p)(x)$, ולכן $\alpha p\in U$.",
      r"לכן $U$ תת מרחב של $\mathbb{R}_3[x]$.",
      r"**בסיס ומימד:** עבור $p(x)=a_0+a_1x+a_2x^2+a_3x^3$:",
      r"$$p(-x)=a_0-a_1x+a_2x^2-a_3x^3,\qquad -p(x)=-a_0-a_1x-a_2x^2-a_3x^3$$",
      r"השוואת מקדמים נותנת $a_0=-a_0$ ו-$a_2=-a_2$, כלומר $a_0=a_2=0$, ו-$a_1,a_3$ חופשיים. לכן $p(x)=a_1x+a_3x^3$:",
      r"$$B_U=\left\{x,\ x^3\right\},\qquad \dim U=2$$"),
    5))

questions.append(S(
    "ב", r"באמצעות הקריטריון לתת מרחב, הוכיחו כי $W$ הוא תת מרחב של $\mathbb{R}_3[x]$, מצאו בסיס ומימד ל-$W$.",
    J(r"**קריטריון לתת מרחב:**",
      r"1. לפולינום האפס $0'(1)=0$, ולכן $0\in W$.",
      r"2. סגירות לחיבור: אם $p,q\in W$ אז $(p+q)'(1)=p'(1)+q'(1)=0+0=0$, ולכן $p+q\in W$.",
      r"3. סגירות לכפל בסקלר: אם $p\in W$ ו-$\alpha\in\mathbb{R}$ אז $(\alpha p)'(1)=\alpha p'(1)=0$, ולכן $\alpha p\in W$.",
      r"לכן $W$ תת מרחב של $\mathbb{R}_3[x]$.",
      r"**בסיס ומימד:** עבור $p(x)=a_0+a_1x+a_2x^2+a_3x^3$ מתקיים $p'(x)=a_1+2a_2x+3a_3x^2$, ולכן $p'(1)=a_1+2a_2+3a_3=0$, כלומר $a_1=-2a_2-3a_3$:",
      r"$$p(x)=a_0+(-2a_2-3a_3)x+a_2x^2+a_3x^3=a_0\cdot1+a_2\left(x^2-2x\right)+a_3\left(x^3-3x\right)$$",
      r"שלושת הפולינומים $1,\ x^2-2x,\ x^3-3x$ בלתי תלויים (מעלותיהם $0,2,3$ שונות), ולכן",
      r"$$B_W=\left\{1,\ x^2-2x,\ x^3-3x\right\},\qquad \dim W=3$$"),
    5))

questions.append(S(
    "ג", r"חשבו תת מרחב $U+W$, מצאו בסיס ומימד של תת מרחב זה.",
    J(r"$U+W=\mathrm{Sp}\left(B_U\cup B_W\right)=\mathrm{Sp}\left\{x,\ x^3,\ 1,\ x^2-2x,\ x^3-3x\right\}$.",
      r"נדרג מטריצה ששורותיה הן הווקטורים הקואורדינטיים לפי $(a_0,a_1,a_2,a_3)$:",
      "$$" + pm("1&0&0&0", "0&1&0&0", "0&-2&1&0", "0&0&0&1", "0&-3&0&1") + arrow(r"\substack{R_3\to R_3+2R_2\\R_5\to R_5+3R_2-R_4}") + pm("1&0&0&0", "0&1&0&0", "0&0&1&0", "0&0&0&1", "0&0&0&0") + "$$",
      r"הדרגה $4=\dim\mathbb{R}_3[x]$, ולכן $U+W=\mathbb{R}_3[x]$:",
      r"$$B_{U+W}=\left\{1,\ x,\ x^2,\ x^3\right\},\qquad \dim(U+W)=4$$"),
    5))

questions.append(S(
    "ד", r"חשבו תת מרחב $U\cap W$, מצאו בסיס ומימד של תת מרחב זה.",
    J(r"פולינום ב-$U$ הוא $p(x)=\alpha x+\beta x^3$ (סעיף (א)). אז $p'(x)=\alpha+3\beta x^2$, והוא שייך ל-$W$ אם",
      r"$$p'(1)=\alpha+3\beta=0\ \Rightarrow\ \alpha=-3\beta$$",
      r"ולכן $p(x)=\beta\left(x^3-3x\right)$, $\beta\in\mathbb{R}$:",
      r"$$B_{U\cap W}=\left\{x^3-3x\right\},\qquad \dim(U\cap W)=1$$",
      r"בדיקה לפי משפט המימדים: $\dim(U+W)=2+3-1=4$, בהתאם לסעיף (ג)."),
    5))

questions.append(S(
    "ה", r"יהי $q(x)$ פולינום מתת מרחב $U\cap W$ כך המקיים את התכונה $q(1)=1$. מצאו $q'(1)$ ו-$q'(\sqrt2)$.",
    J(r"מסעיף (ד) $q(x)=\beta\left(x^3-3x\right)$. התנאי $q(1)=1$ נותן $\beta(1-3)=1$, כלומר $\beta=-\frac12$:",
      r"$$q(x)=-\frac12x^3+\frac32x,\qquad q'(x)=-\frac32x^2+\frac32$$",
      r"$$q'(1)=-\frac32+\frac32=0,\qquad q'\left(\sqrt2\right)=-\frac32\cdot2+\frac32=-\frac32$$",
      r"(התוצאה $q'(1)=0$ צפויה מראש, כי $q\in W$.)"),
    5))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד ובסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    J(r"נסמן $B=\left(1,t,t^2,t^3\right)$ בסיס סטנדרטי של $\mathbb{R}_3[t]$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^3$. מטריצה מייצגת סטנדרטית היא",
      r"$$A=[T]_E^B=" + pm("1&1&-1&3", "1&2&0&4", "1&3&1&5") + "$$",
      "$$" + aug([["1", "1", "-1", "3", "0"], ["1", "2", "0", "4", "0"], ["1", "3", "1", "5", "0"]], 4)
      + r"\to" + aug([["1", "1", "-1", "3", "0"], ["0", "1", "1", "1", "0"], ["0", "2", "2", "2", "0"]], 4)
      + r"\to" + aug([["1", "1", "-1", "3", "0"], ["0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$",
      r"עמודות מס׳ 1,2 של המטריצה המדורגת מובילות, אז $\mathrm{Col}\,A$ בסיס של $\left\{" + pm("1", "1", "1") + "," + pm("1", "2", "3") + r"\right\}$, כלומר בסיס של $\mathrm{Im}\,T$ ואז $\dim\mathrm{Im}\,T=2$.",
      "$$" + r"\to" + aug([["1", "0", "-2", "2", "0"], ["0", "1", "1", "1", "0"], ["0", "0", "0", "0", "0"]], 4)
      + r"\Rightarrow\begin{cases}x_1=2t-2s\\x_2=-t-s\\x_3=t\\x_4=s\end{cases}\Rightarrow" + pm("x_1", "x_2", "x_3", "x_4") + "=t" + pm("2", "-1", "1", "0") + "+s" + pm("-2", "-1", "0", "1") + "$$",
      r"אז $\mathrm{Ker}\,T$ בסיס של $\mathrm{Nul}\,A$ הוא $\left(2-t+t^2,\ -2-t+t^3\right)$ ואז $\dim\mathrm{Ker}\,T=2$."),
    12, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חד חד ערכית? האם $T$ על? נמקו.",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=2\neq0$, ו-$T$ לא על כי $\dim\mathrm{Im}\,T=2\neq3=\dim\mathbb{R}^3$.",
    4, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטר $k$ מתקיים $" + pm("k", "7", "10") + r"\in\mathrm{Im}\,T$?",
    J(r"$$" + pm("k", "7", "10") + r"\in\mathrm{Im}\,T\Leftrightarrow" + pm("k", "7", "10") + "=x_1" + pm("1", "1", "1") + "+x_2" + pm("1", "2", "3") + "$$",
      "$$" + aug([["1", "1", "k"], ["1", "2", "7"], ["1", "3", "10"]], 2) + r"\to" + aug([["1", "1", "k"], ["0", "1", "7-k"], ["0", "2", "10-k"]], 2) + r"\to" + aug([["1", "1", "k"], ["0", "1", "7-k"], ["0", "0", "-4+k"]], 2) + r"\Rightarrow-4+k=0\Rightarrow k=4$$"),
    4, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"נתונה העתקה לינארית $F:\mathbb{R}^2\to\mathbb{R}^2$ כך ש-$F\left(" + pm("a", "b") + r"\right)=" + pm("a+b", "a-b") + r"$. מצאו את המטריצה המייצגת $[F]_B^B$ של $F$, כאשר $B=\left\{" + pm("5", "17") + "," + pm("2", "7") + r"\right\}$ בסיס של $\mathbb{R}^2$.",
    J(r"$E$ בסיס סטנדרטי של $\mathbb{R}^2$. $\left|\begin{matrix}5&2\\17&7\end{matrix}\right|=1\neq0$ אז $B=\left(" + pm("5", "17") + "," + pm("2", "7") + r"\right)$ בסיס של $\mathbb{R}^2$. לכן $[I]_E^B=" + pm("5&2", "17&7") + r"$.",
      r"$$F\left(" + pm("a", "b") + r"\right)=" + pm("a+b", "a-b") + r"\Rightarrow F\left(" + pm("1", "0") + r"\right)=" + pm("1", "1") + r",\ F\left(" + pm("0", "1") + r"\right)=" + pm("1", "-1") + r"\Rightarrow[F]_E^E=" + pm("1&1", "1&-1") + "$$",
      r"$$[F]_B^B=[I]_B^E[F]_E^E[I]_E^B=" + pm("5&2", "17&7") + r"^{-1}" + pm("1&1", "1&-1") + pm("5&2", "17&7") + "=" + pm("7&-2", "-17&5") + pm("22&9", "-12&-5") + "$$",
      r"$$=" + pm("154+24&63+10", "-374-60&-153-25") + "=" + pm("178&73", "-434&-178") + "$$"),
    5))

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
    rubric=rub((r"נטילת דטרמיננטה משני אגפי המשוואה $(PQ)^{-1}CPQ=D$", 1),
               (r"כפליות הדטרמיננטה על המכפלה: $\det\left(Q^{-1}\right)\det\left(P^{-1}\right)\det(C)\det(P)\det(Q)$", 2),
               (r"$\det\left(M^{-1}\right)=\frac{1}{\det M}$ עבור $M=P,Q$", 2),
               (r"צמצום $\det P$ ו-$\det Q$ (שונים מאפס כי $P,Q$ הפיכות)", 1),
               (r"המסקנה $\det C=\det D$", 1)),
    pitfalls=[r"לצמצם את המטריצות עצמן ולטעון ש-$(PQ)^{-1}CPQ=C$ (הכפל אינו חילופי); הצמצום חוקי רק על הדטרמיננטות, שהן מספרים.",
              r"לרשום $\det\left(P^{-1}\right)=\det P$ במקום $\frac{1}{\det P}$."],
    steps=[
        cho(r"איזו תכונה של הדטרמיננטה מאפשרת לפרק את $\det\left[(PQ)^{-1}CPQ\right]$ לגורמים?",
            r"$\det(XY)=\det X\cdot\det Y$ לכל שתי מטריצות ריבועיות מאותו סדר",
            [r"$\det(X+Y)=\det X+\det Y$", r"$\det(\alpha X)=\alpha\det X$ לכל מטריצה מסדר $2$ ומעלה", r"$\det\left(X^{-1}\right)=\det X$"],
            r"הכפליות היא התכונה שבה הפתרון משתמש. שלוש האפשרויות האחרות שגויות: למשל עבור $X=Y=I_2$ מתקבל $\det(X+Y)=4\neq2=\det X+\det Y$; $\det(2I_2)=4\neq2\det I_2$; ועבור $X=2I_2$ מתקבל $\det\left(X^{-1}\right)=\frac14\neq4=\det X$."),
        odr(r"סדרו את שרשרת החישוב.",
            [r"$\det\left[(PQ)^{-1}CPQ\right]=\det D$",
             r"$\det\left(Q^{-1}\right)\det\left(P^{-1}\right)\det(C)\det(P)\det(Q)=\det D$",
             r"$\frac{1}{\det Q}\cdot\frac{1}{\det P}\cdot\det C\cdot\det P\cdot\det Q=\det D$",
             r"$\det C=\det D$"],
            r"מחשבים דטרמיננטה בשני האגפים, מפרקים לפי כפליות ושימוש ב-$(PQ)^{-1}=Q^{-1}P^{-1}$, מציבים $\det\left(M^{-1}\right)=\frac{1}{\det M}$ ומצמצמים."),
        fnd(r"בשרשרת הבאה שורה אחת שגויה. מצאו אותה.",
            [r"$\det\left[(PQ)^{-1}CPQ\right]=\det D$",
             r"$\det\left(Q^{-1}\right)\det\left(P^{-1}\right)\det(C)\det(P)\det(Q)=\det D$",
             r"$\det Q\cdot\det P\cdot\det C\cdot\det P\cdot\det Q=\det D$",
             r"$\det C=\det D$"], 2,
            r"$\det\left(Q^{-1}\right)=\frac{1}{\det Q}$ ולא $\det Q$; השורה השגויה לא מצטמצמת ל-$\det C$."),
        num(r"עבור $P=\begin{pmatrix}1&2\\3&7\end{pmatrix}$, $Q=\begin{pmatrix}2&1\\5&3\end{pmatrix}$, $C=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ ו-$D=(PQ)^{-1}CPQ$, מהו $|D|$?", 10,
            r"$|C|=12-2=10$ ולכן $|D|=|C|=10$."),
    ])

ENR[(1, "ב")] = dict(
    rubric=rub((r"העברת אגף: $2AB=-3I$ ונטילת דטרמיננטה", 1),
               (r"$\det(-3I)=(-3)^4=81$ עבור מטריצות מסדר $4$", 2),
               (r"$\det(2AB)=2^4\det A\det B$", 2),
               (r"$2^4\det A\det B=81\neq0$ ולכן כל גורם שונה מאפס, ובפרט $\det A\neq0$", 2)),
    pitfalls=[r"לכתוב $\det(2A)=2\det A$ במקום $2^4\det A$ (גורם הכפל מוכפל בכל אחת מארבע השורות).",
              r"לחשב $\det(-3I)=-3$ או $-81$ במקום $(-3)^4=81$."],
    steps=[
        num(r"מהו $\det(-3I)$ עבור המטריצה $-3I$ מסדר $4$?", 81, r"$\det(-3I_4)=(-3)^4=81$."),
        cho(r"מהו $\det(2AB)$ עבור מטריצות $A,B$ מסדר $4$?", r"$2^4\det A\det B$",
            [r"$2\det A\det B$", r"$\det A\det B$", r"$2^4\left(\det A+\det B\right)$"],
            r"הכפלה בסקלר $2$ של מטריצה מסדר $4$ מכפילה את הדטרמיננטה ב-$2^4$, והדטרמיננטה של מכפלה היא מכפלת הדטרמיננטות."),
        odr(r"סדרו את שלבי ההוכחה.",
            [r"$2AB=-3I$",
             r"$\det(2AB)=\det(-3I)=(-3)^4=81$",
             r"$2^4\det(A)\det(B)=81\neq0$",
             r"לכן $\det A\neq0$ (וגם $\det B\neq0$), כלומר $A$ הפיכה"],
            r"השלבים תלויים זה בזה: קודם מעבירים אגף, אחר כך מחשבים דטרמיננטה, ורק מהמכפלה השונה מאפס מסיקים על הגורמים."),
        num(r"מהו $\det(2A)$ אם $|A|=2$ ו-$A$ מסדר $4$?", 32, r"$2^4\cdot2=32$."),
    ])

ENR[(1, "ג")] = dict(
    rubric=rub((r"המשוואה $\det(2A)\det(B)=\det(-3I)$", 2),
               (r"$\det(-3I)=(-3)^4=81$", 2),
               (r"$\det(2A)=2^4\cdot2=32$", 2),
               (r"פתרון המשוואה $32\det B=81$ ולכן $\det B=\frac{81}{32}$", 2)),
    pitfalls=[r"לחשב $\det(2A)=2\cdot2=4$ במקום $2^4\cdot2=32$.",
              r"לשכוח שהמשוואה היא $\det(2AB)=\det(-3I)$ ולא $\det(AB)=\det(-3I)$."],
    steps=[
        cho(r"איזו משוואה על $\det B$ מתקבלת?", r"$32\det B=81$",
            [r"$32\det B=-81$", r"$4\det B=81$", r"$32\det B=9$"],
            r"$\det(2A)=2^4\cdot2=32$ ו-$\det(-3I)=(-3)^4=81$. הטעויות האחרות: סימן שלילי, $\det(2A)=4$, ו-$(-3)^2$ במקום $(-3)^4$."),
        num(r"מהו $|B|$ (ערך עשרוני)?", 2.53125, r"$\det B=\frac{81}{32}=2.53125$.", tol=0.0001),
    ])

ENR[(1, "ד")] = dict(
    rubric=rub((r"$B$ הפיכה ולכן $\det B\neq0$ והמשוואה $\det B\cdot\det B^{-1}=1$ מוגדרת", 1),
               (r"$\det\left(B^{-1}\right)=\frac{1}{\det B}$", 1),
               (r"הצבה: $\frac{32}{81}$", 1)),
    pitfalls=[r"להשאיר $\det\left(B^{-1}\right)=\det B$ (זה נכון רק כאשר $\det B=\pm1$)."],
    steps=[
        cho(r"איזה קשר מתקיים בין $\det\left(B^{-1}\right)$ ל-$\det B$?", r"$\det\left(B^{-1}\right)=\frac{1}{\det B}$",
            [r"$\det\left(B^{-1}\right)=\det B$", r"$\det\left(B^{-1}\right)=-\det B$"],
            r"מ-$BB^{-1}=I$ מקבלים $\det B\cdot\det\left(B^{-1}\right)=1$."),
        num(r"מהו $\left|B^{-1}\right|$ (ערך עשרוני, ארבע ספרות אחרי הנקודה)?", 0.3951, r"$\frac{32}{81}\approx0.3951$.", tol=0.0001),
    ])

ENR[(2, "א")] = dict(
    rubric=rub((r"כתיבת המטריצה המורחבת ודירוג: $R_2\to R_2-R_1$, $R_3\to R_3-R_1$", 2),
               (r"המקרה $a=2$ בנפרד: פתרון יחיד לכל $b$", 2),
               (r"עבור $a\neq2$: $R_3\to R_3-9R_2$ והאיבר $a-2-\frac{9}{a-2}=0\Leftrightarrow a=5,-1$", 2),
               (r"$a=5$: פתרון יחיד לא קיים; אינסוף פתרונות אם $b=7$ ואין פתרון אם $b\neq7$", 2),
               (r"$a=-1$: אינסוף פתרונות אם $b=-5$ ואין פתרון אם $b\neq-5$", 2)),
    pitfalls=[r"לחלק ב-$a-2$ בלי לבדוק את המקרה $a=2$ בנפרד.",
              r"להסיק שאין פתרון בכל מקרה ש-$a=5,-1$, בלי לבדוק את $b$ (שם יש אינסוף פתרונות עבור $b=7$ ו-$b=-5$ בהתאמה)."],
    steps=[
        cho(r"עבור אילו ערכי $a$ מטריצת המקדמים אינה הפיכה (הדטרמיננטה מתאפסת)?", r"$a=5$ ו-$a=-1$",
            [r"$a=2$ בלבד", r"$a=5$ בלבד", r"$a=2$ ו-$a=-1$"],
            r"הדטרמיננטה של מטריצת המקדמים היא $(a-5)(a+1)$, ולכן מתאפסת רק עבור $a=5,-1$; עבור $a=2$ היא שונה מאפס."),
        cho(r"מה קורה עבור $a=2$, כאשר $b$ כלשהו?", r"פתרון יחיד לכל $b$",
            [r"אין פתרון לכל $b$", r"אינסוף פתרונות לכל $b$"],
            r"עבור $a=2$ מטריצת המקדמים הפיכה (דרגה $3$), ולכן יש פתרון יחיד לכל $b$."),
        num(r"עבור $a=5$: לאיזה ערך $b$ יש למערכת אינסוף פתרונות?", 7, r"$3(b-1)-18=0\Rightarrow b=7$."),
        num(r"עבור $a=-1$: לאיזה ערך $b$ יש למערכת אינסוף פתרונות?", -5, r"$-3(b-1)-18=0\Rightarrow b=-5$."),
    ])

ENR[(2, "ב")] = dict(
    rubric=rub((r"הצבה $a=2,b=1$ וקבלת המטריצה המדורגת", 2),
               (r"מציאת $z=2$ ו-$y=0$", 2),
               (r"הצבה לאחור: $x=1-2y-2z=-3$", 1)),
    pitfalls=[r"להשתמש בצורה המדורגת של המקרה $a\neq2$ (שבה מחלקים ב-$a-2$) במקום לטפל במקרה $a=2$ בנפרד."],
    steps=[
        num(r"עבור $a=2,b=1$ מהו $z$?", 2, r"מהשורה $0\ 0\ 1\,|\,2$ מתקבל $z=2$."),
        num(r"מהו $y$?", 0, r"$y=\frac{b-1}{9}=0$."),
        num(r"מהו $x$?", -3, r"$x=1-2y-2z=1-0-4=-3$."),
    ])

ENR[(2, "ג")] = dict(
    rubric=rub((r"הצבה $a=5,b=7$ והשורה האחרונה מתאפסת", 1),
               (r"$z=t$ משתנה חופשי", 1),
               (r"$y=\frac{2}{3}-\frac{t}{3}$", 1),
               (r"$x=-\frac13-\frac43t$", 1),
               (r"הצגה בצורה וקטורית: פתרון פרטי $+\,t\cdot$ וקטור כיוון", 1)),
    pitfalls=[r"לשכוח לכתוב את הפתרון הכללי (עם הפרמטר $t$) ולהסתפק בפתרון פרטי אחד.",
              r"טעות סימן בהצבה לאחור $x=1-2y-2z$."],
    steps=[
        num(r"מהי דרגת מטריצת המקדמים עבור $a=5$?", 2, r"השורה השלישית מתאפסת לאחר הדירוג, ונשארות שתי שורות לא אפס."),
        num(r"כמה משתנים חופשיים יש במקרה זה?", 1, r"$3-2=1$."),
        num(r"מהו $x$ כאשר $t=0$ (פתרון פרטי)? (ערך עשרוני, ארבע ספרות)", -0.3333, r"$x=-\frac13$.", tol=0.0001),
        num(r"מהו $y$ כאשר $t=1$? (ערך עשרוני, ארבע ספרות)", 0.3333, r"$y=\frac23-\frac13=\frac13$.", tol=0.0001),
    ])

ENR[(2, "ד")] = dict(
    rubric=rub((r"חישוב הדטרמיננטה $z^2+2z+2$ (למשל פיתוח לפי עמודה ראשונה)", 2),
               (r"$A$ הפיכה אם ורק אם $\det A\neq0$", 1),
               (r"פתרון $z^2+2z+2=0$ בנוסחת השורשים: $z=-1\pm i$", 1),
               (r"מסקנה: $A$ הפיכה לכל $z\neq-1\pm i$", 1)),
    pitfalls=[r"לפתור את המשוואה $\det A=0$ ולהסיק שאלה הערכים להפיכות (ההפך הוא הנכון).",
              r"לעבוד בממשיים ולהסיק שהמטריצה הפיכה לכל $z\in\mathbb{R}$ בלי לבדוק את השורשים המרוכבים."],
    steps=[
        num(r"מהי $\det A$ עבור $z=1$?", 5, r"$z^2+2z+2=1+2+2=5$."),
        num(r"מהי $\det A$ עבור $z=0$?", 2, r"$z^2+2z+2=2$."),
        cho(r"מהם פתרונות המשוואה $z^2+2z+2=0$?", r"$z=-1+i$ ו-$z=-1-i$",
            [r"$z=1+i$ ו-$z=1-i$", r"$z=-1+2i$ ו-$z=-1-2i$", r"$z=-2$ ו-$z=0$"],
            r"$z=\frac{-2\pm\sqrt{4-8}}{2}=-1\pm i$; בהצבת האפשרויות האחרות הביטוי אינו מתאפס."),
        cho(r"עבור אילו $z$ המטריצה $A$ הפיכה?", r"$z\neq-1+i$ וגם $z\neq-1-i$",
            [r"$z=-1\pm i$ בלבד", r"$z\in\mathbb{R}$ בלבד", r"$z\neq-1$"],
            r"הפיכה בדיוק כאשר $\det A\neq0$. עבור $z=-1$ הדטרמיננטה היא $1\neq0$ ולכן $A$ הפיכה גם שם."),
    ])

ENR[(3, "א")] = dict(
    rubric=rub((r"חישוב $\det A=-3a+27$", 2),
               (r"$A$ הפיכה אם ורק אם $a\neq9$", 1),
               (r"חישוב מטריצת המשלימים האלגבריים $C$", 3),
               (r"$A^{-1}=\frac{1}{\det A}C^T$ (שחלוף!)", 1),
               (r"רישום $A^{-1}$ הסופית", 1)),
    pitfalls=[r"לשכוח לשחלף את מטריצת המשלימים האלגבריים: $A^{-1}=\frac{1}{\det A}C^T$ ולא $\frac{1}{\det A}C$.",
              r"טעות בסימני השחמט $(-1)^{i+j}$ בחישוב המשלימים."],
    steps=[
        num(r"מהי $\det A$ כאשר $a=0$?", 27, r"$\det A=-3a+27$, ובהצבה $a=0$ מתקבל $27$."),
        num(r"מהו המשלים האלגברי $C_{11}$ עבור $a=0$?", -48, r"$C_{11}=\begin{vmatrix}5&6\\8&0\end{vmatrix}=-48$."),
        cho(r"איזו נוסחה נותנת את $A^{-1}$?", r"$A^{-1}=\frac{1}{\det A}C^T$",
            [r"$A^{-1}=\frac{1}{\det A}C$", r"$A^{-1}=\det A\cdot C^T$", r"$A^{-1}=\frac{1}{\det A}C^{-1}$"],
            r"הנוסחה היא $\frac{1}{\det A}\mathrm{adj}(A)$ כאשר $\mathrm{adj}(A)=C^T$. עבור $a=0$ המטריצה $C$ אינה סימטרית, ולכן ההבדל בין $C$ ל-$C^T$ משנה את התוצאה."),
        num(r"מהי הכניסה בשורה 1 עמודה 2 של $A^{-1}$ כאשר $a=0$? (ערך עשרוני, ארבע ספרות)", 0.8889, r"היא $\frac{C_{21}}{\det A}=\frac{24}{27}=\frac89$.", tol=0.0001),
    ])

ENR[(3, "ב")] = dict(
    rubric=rub((r"הצבה $a=9$ ודירוג המטריצה", 2),
               (r"דרגה $\mathrm{rank}(A)=2$", 2),
               (r"שתי השורות הראשונות של הצורה המדורגת בלתי תלויות ופורשות את מרחב השורות", 1),
               (r"השלמה בווקטור $(0,0,1)$", 1),
               (r"בדיקה שהשלושה בלתי תלויים", 1)),
    pitfalls=[r"לבחור להשלמה וקטור שנמצא כבר בפרישה של השורות (למשל כפולה של שורה), ולכן לא לקבל בסיס.",
              r"לספור את שורת האפס כשורה בלתי תלויה ולקבל דרגה $3$."],
    steps=[
        num(r"מהי דרגת $A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}$?", 2, r"אחרי דירוג נשארות שתי שורות שאינן אפס."),
        num(r"בדירוג, אחרי $R_2\to R_2-4R_1$, מהי הכניסה בשורה 2 עמודה 2?", -3, r"$5-4\cdot2=-3$."),
        cho(r"איזה וקטור משלים את $(1,2,3),(0,1,2)$ לבסיס של $\mathbb{R}^3$?", r"$(0,0,1)$",
            [r"$(2,4,6)$", r"$(1,3,5)$", r"$(4,5,6)$"],
            r"הווקטור $(0,0,1)$ נותן דטרמיננטה $1\neq0$. האחרים נמצאים כבר בפרישה של $(1,2,3),(0,1,2)$: $(2,4,6)=2(1,2,3)$, $(1,3,5)=(1,2,3)+(0,1,2)$, $(4,5,6)=4(1,2,3)-3(0,1,2)$."),
        num(r"מהי הדטרמיננטה של המטריצה ששורותיה $(1,2,3),(0,1,2),(0,0,1)$?", 1, r"מטריצה משולשית עליונה: מכפלת האלכסון $1\cdot1\cdot1=1\neq0$."),
    ])

ENR[(3, "ג")] = dict(
    rubric=rub((r"הגדרה: $M$ אנטי סימטרית אם $M^T=-M$", 2),
               (r"חוק השחלוף: $(CD)^T=D^TC^T$ (הסדר מתהפך)", 3),
               (r"שימוש בסימטריה $C^T=C$, $D^T=D$ ובקבלת $DC$", 2),
               (r"שימוש בנתון $CD=-DC$ ובקבלת $(CD)^T=-CD$", 2),
               (r"מסקנה: הטענה נכונה", 1)),
    pitfalls=[r"לכתוב $(CD)^T=C^TD^T$ ולשכוח שהשחלוף הופך את סדר המכפלה.",
              r"להסיק $CD=DC$ מכך ש-$C,D$ סימטריות; הנתון הוא דווקא $CD=-DC$."],
    steps=[
        cho(r"האם הטענה ($CD$ אנטי סימטרית) נכונה?", r"נכונה, ויש להוכיח אותה",
            [r"שגויה, ויש לתת דוגמה נגדית"],
            r"השחלוף וההנחות נותנים $(CD)^T=-CD$, ולכן הטענה נכונה. בדיקה על $C=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ אכן נותנת מטריצה אנטי סימטרית."),
        odr(r"סדרו את שלבי ההוכחה.",
            [r"$(CD)^T=D^TC^T$",
             r"$=DC$ (כי $C,D$ סימטריות)",
             r"$=-CD$ (כי $CD=-DC$)",
             r"לכן $(CD)^T=-CD$, כלומר $CD$ אנטי סימטרית"],
            r"כל שורה נובעת מהקודמת: שחלוף, סימטריה, הנתון, ומסקנה."),
        fnd(r"בהוכחה הבאה שורה אחת שגויה. מצאו אותה.",
            [r"$(CD)^T=C^TD^T$",
             r"$=CD$ (כי $C,D$ סימטריות)",
             r"$=-DC$ (כי $CD=-DC$)",
             r"לכן $(CD)^T=-DC$"], 0,
            r"שחלוף של מכפלה הופך את הסדר: $(CD)^T=D^TC^T$."),
        num(r"עבור $C=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ (שתיהן סימטריות, ומקיימות $CD=-DC$), מהי הכניסה בשורה 1 עמודה 2 של $CD$?", -1, r"$CD=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, והיא אנטי סימטרית."),
    ])

ENR[(4, "א")] = dict(
    rubric=rub((r"קריטריון: $0\in U$", 1),
               (r"סגירות לחיבור: $(p+q)(-x)=-(p+q)(x)$", 1),
               (r"סגירות לכפל בסקלר: $(\alpha p)(-x)=-(\alpha p)(x)$", 1),
               (r"השוואת מקדמים: $a_0=a_2=0$", 1),
               (r"בסיס $\{x,x^3\}$ ומימד $2$", 1)),
    pitfalls=[r"לבדוק רק שפולינום מסוים שייך ל-$U$, במקום להוכיח סגירות לכל זוג פולינומים.",
              r"לכלול ב-$U$ את הפולינומים הזוגיים ($1,x^2$), שמקיימים $p(-x)=p(x)$ ולא $p(-x)=-p(x)$."],
    steps=[
        num(r"עבור $p(x)=a_0+a_1x+a_2x^2+a_3x^3\in U$, מהו $a_0$?", 0, r"$a_0=-a_0$ ולכן $a_0=0$."),
        odr(r"סדרו את הוכחת הסגירות לחיבור.",
            [r"$(p+q)(-x)=p(-x)+q(-x)$",
             r"$=-p(x)-q(x)$",
             r"$=-(p+q)(x)$",
             r"לכן $p+q\in U$"],
            r"מציבים את ההגדרה, משתמשים ב-$p,q\in U$, ומוציאים סימן מינוס."),
        cho(r"מהו בסיס של $U$?", r"$\{x,\ x^3\}$",
            [r"$\{1,\ x^2\}$", r"$\{x,\ x^2,\ x^3\}$", r"$\{x\}$"],
            r"$U$ הוא הפולינומים האי-זוגיים. $1,x^2$ זוגיים; $x^2\notin U$; ו-$\{x\}$ אינו פורש את $x^3$."),
        num(r"מהו $\dim U$?", 2, r"הבסיס $\{x,x^3\}$ כולל שני איברים."),
    ])

ENR[(4, "ב")] = dict(
    rubric=rub((r"קריטריון: $0\in W$ וסגירות לחיבור ולכפל בסקלר (הנגזרת לינארית)", 2),
               (r"$p'(1)=a_1+2a_2+3a_3=0$", 1),
               (r"ביטוי $a_1=-2a_2-3a_3$ והצבה בפולינום", 1),
               (r"בסיס $\{1,x^2-2x,x^3-3x\}$ ומימד $3$", 1)),
    pitfalls=[r"לשכוח שהנגזרת מחושבת בנקודה $x=1$ ולרשום $a_1+a_2+a_3=0$.",
              r"לא לבדוק שהווקטורים שנמצאו בלתי תלויים."],
    steps=[
        num(r"מהו $p'(1)$ עבור $p(x)=x^3$?", 3, r"$p'(x)=3x^2$ ולכן $p'(1)=3$."),
        odr(r"סדרו את שלבי מציאת הבסיס.",
            [r"$p'(x)=a_1+2a_2x+3a_3x^2$",
             r"$p'(1)=a_1+2a_2+3a_3=0$",
             r"$a_1=-2a_2-3a_3$",
             r"$p=a_0\cdot1+a_2\left(x^2-2x\right)+a_3\left(x^3-3x\right)$"],
            r"גוזרים, מציבים $x=1$, מבודדים $a_1$ ומציבים חזרה."),
        cho(r"מהו בסיס של $W$?", r"$\{1,\ x^2-2x,\ x^3-3x\}$",
            [r"$\{1,\ x,\ x^2\}$", r"$\{x^2-2x,\ x^3-3x\}$", r"$\{1,\ x^2-1,\ x^3-1\}$"],
            r"בבסיס הנכון לכל פולינום $p'(1)=0$: $1\to0$, $x^2-2x\to0$, $x^3-3x\to0$. עבור $x$ מתקבל $1$; עבור $x^2-1$ מתקבל $2$; עבור $x^3-1$ מתקבל $3$. הקבוצה $\{x^2-2x,\ x^3-3x\}$ בלתי תלויה אך אינה פורשת (מימד $2$ במקום $3$)."),
        num(r"מהו $\dim W$?", 3, r"שלושה וקטורים בבסיס."),
    ])

ENR[(4, "ג")] = dict(
    rubric=rub((r"$U+W=\mathrm{Sp}\left(B_U\cup B_W\right)$", 1),
               (r"כתיבת הווקטורים הקואורדינטיים לפי $(a_0,a_1,a_2,a_3)$ כשורות במטריצה", 1),
               (r"דירוג: שורת אפס, הדרגה $4$", 2),
               (r"מסקנה: $U+W=\mathbb{R}_3[x]$, בסיס $\{1,x,x^2,x^3\}$, מימד $4$", 1)),
    pitfalls=[r"לקחת את כל חמשת הפולינומים כבסיס; הם תלויים (דרגה $4$ בלבד).",
              r"לחבר את המימדים $2+3=5$ בלי להחסיר את $\dim(U\cap W)$."],
    steps=[
        cho(r"איזו קבוצה פורשת את $U+W$?", r"$B_U\cup B_W$, האיחוד של הבסיסים",
            [r"$B_U\cap B_W$, החיתוך של הבסיסים", r"$B_U$ בלבד", r"$B_W$ בלבד"],
            r"סכום תתי מרחבים נפרש על ידי איחוד הפורשים. החיתוך של הבסיסים ריק; $B_U$ לא כולל את $1$; $B_W$ לא כולל את $x$."),
        num(r"מהי דרגת המטריצה ששורותיה הווקטורים הקואורדינטיים של חמשת הפולינומים?", 4, r"הדרגה $4=\dim\mathbb{R}_3[x]$."),
        num(r"כמה מחמשת הפולינומים תלויים בארבעת האחרים (חמש פחות הדרגה)?", 1, r"$5-4=1$ (למשל $x^3-3x$ הוא צירוף של $x$ ו-$x^3$, שכבר נמצאים בקבוצה)."),
    ])

ENR[(4, "ד")] = dict(
    rubric=rub((r"פולינום ב-$U$ הוא $\alpha x+\beta x^3$", 1),
               (r"התנאי $p'(1)=\alpha+3\beta=0$", 2),
               (r"הצגה $\beta\left(x^3-3x\right)$, בסיס ומימד $1$", 1),
               (r"בדיקה במשפט המימדים: $2+3-1=4$", 1)),
    pitfalls=[r"לחשב את החיתוך כאיחוד הבסיסים (או כחיתוך הבסיסים, שהוא ריק) במקום לפתור את התנאי.",
              r"לשכוח שהנגזרת של $x^3$ היא $3x^2$ ולרשום $\alpha+\beta=0$."],
    steps=[
        num(r"עבור $p=\alpha x+\beta x^3$, אם $\beta=1$ ו-$p'(1)=0$, מהו $\alpha$?", -3, r"$p'(1)=\alpha+3\beta=0\Rightarrow\alpha=-3$."),
        cho(r"מהו בסיס של $U\cap W$?", r"$\{x^3-3x\}$",
            [r"$\{x^3+3x\}$", r"$\{x-3x^3\}$", r"$\{x,\ x^3-3x\}$"],
            r"רק $x^3-3x$ אי-זוגי וגם $p'(1)=3-3=0$. הפולינום $x^3+3x$ מקיים $p'(1)=6$; $x-3x^3$ מקיים $p'(1)=-8$; ו-$x\notin W$ כי $p'(1)=1$."),
        num(r"לפי משפט המימדים, אם $\dim U=2$, $\dim W=3$ ו-$\dim(U\cap W)=1$, מהו $\dim(U+W)$?", 4, r"$2+3-1=4$, בהתאם לסעיף הקודם."),
    ])

ENR[(4, "ה")] = dict(
    rubric=rub((r"שימוש בסעיף ד: $q=\beta\left(x^3-3x\right)$", 1),
               (r"$q(1)=1$ נותן $\beta=-\frac12$", 1),
               (r"גזירה: $q'(x)=-\frac32x^2+\frac32$", 1),
               (r"$q'(1)=0$", 1),
               (r"$q'\left(\sqrt2\right)=-\frac32$", 1)),
    pitfalls=[r"לשכוח ש-$q\in W$ ולכן $q'(1)=0$ בלי חישוב.",
              r"לחשב $q'(\sqrt2)$ בלי לגזור קודם, כלומר להציב $\sqrt2$ ב-$q$."],
    steps=[
        num(r"אם $q=\beta\left(x^3-3x\right)$ ו-$q(1)=1$, מהו $\beta$?", -0.5, r"$\beta(1-3)=1\Rightarrow\beta=-\frac12$."),
        num(r"מהו $q'(1)$?", 0, r"$q\in W$ ולכן $q'(1)=0$."),
        num(r"מהו $q'\left(\sqrt2\right)$? (ערך עשרוני)", -1.5, r"$q'(x)=-\frac32x^2+\frac32$, ובהצבה $-3+\frac32=-\frac32$.", tol=0.0001),
    ])

ENR[(5, "א")] = dict(
    rubric=rub((r"כתיבת המטריצה המייצגת $A=[T]_E^B$ מהתמונות של איברי הבסיס", 2),
               (r"דירוג $A$ ומציאת העמודות המובילות", 2),
               (r"בסיס של $\mathrm{Im}\,T$ הוא עמודות 1,2 של $A$ המקורית, ו-$\dim\mathrm{Im}\,T=2$", 2),
               (r"דירוג עד הצורה המדורגת המצומצמת ומציאת המשתנים החופשיים $x_3,x_4$", 3),
               (r"בסיס $\mathrm{Nul}\,A$: $(2,-1,1,0)$ ו-$(-2,-1,0,1)$, ותרגומם לפולינומים $2-t+t^2$ ו-$-2-t+t^3$, מימד $2$", 3)),
    pitfalls=[r"לקחת את עמודות הצורה המדורגת כבסיס של $\mathrm{Im}\,T$; יש לקחת את העמודות המתאימות מהמטריצה המקורית.",
              r"לשכוח לתרגם את וקטורי $\mathrm{Nul}\,A$ (קואורדינטות) בחזרה לפולינומים ב-$\mathbb{R}_3[t]$."],
    steps=[
        num(r"מהי דרגת $A=\begin{pmatrix}1&1&-1&3\\1&2&0&4\\1&3&1&5\end{pmatrix}$?", 2, r"אחרי דירוג נשארות שתי שורות שאינן אפס."),
        cho(r"מהו בסיס של $\mathrm{Im}\,T$?", r"$\left\{(1,1,1),\ (1,2,3)\right\}$",
            [r"$\left\{(1,0,0),\ (1,1,0)\right\}$", r"$\left\{(1,1,1)\right\}$", r"$\left\{(1,1,1),\ (2,2,2)\right\}$"],
            r"העמודות המובילות של $A$ המקורית נותנות בסיס. עמודות הצורה המדורגת $(1,0,0),(1,1,0)$ אינן ב-$\mathrm{Im}\,T$ (למשל $(1,0,0)$ אינו צירוף של $(1,1,1),(1,2,3)$); הווקטור $(1,1,1)$ לבדו פורש קו בלבד; והזוג $(1,1,1),(2,2,2)$ תלוי."),
        num(r"מהו $\dim\mathrm{Ker}\,T$?", 2, r"$4-\mathrm{rank}(A)=4-2=2$."),
        num(r"עבור $t=1,s=0$ בפתרון הכללי של $A\vec x=0$, מהו $x_2$?", -1, r"$\vec x=t(2,-1,1,0)+s(-2,-1,0,1)$, ולכן $x_2=-1$."),
    ])

ENR[(5, "ב")] = dict(
    rubric=rub((r"$T$ חד חד ערכית אם ורק אם $\mathrm{Ker}\,T=\{0\}$", 1),
               (r"$\dim\mathrm{Ker}\,T=2\neq0$, ולכן $T$ אינה חד חד ערכית", 1),
               (r"$T$ על אם ורק אם $\dim\mathrm{Im}\,T=\dim\mathbb{R}^3=3$", 1),
               (r"$\dim\mathrm{Im}\,T=2<3$, ולכן $T$ אינה על", 1)),
    pitfalls=[r"להשוות את $\dim\mathrm{Im}\,T$ למימד התחום ($4$) במקום למימד הטווח ($3$) כשבודקים ״על״."],
    steps=[
        num(r"מהו $\dim\mathrm{Ker}\,T$?", 2, r"מהסעיף הקודם."),
        cho(r"האם $T$ חד חד ערכית?", r"לא, כי $\dim\mathrm{Ker}\,T=2\neq0$",
            [r"כן, כי $\dim\mathrm{Im}\,T=2$", r"כן, כי $\mathrm{Ker}\,T\neq\{0\}$"],
            r"חד חד ערכית אם ורק אם הגרעין טריוויאלי."),
        cho(r"האם $T$ על?", r"לא, כי $\dim\mathrm{Im}\,T=2<3=\dim\mathbb{R}^3$",
            [r"כן, כי במטריצה $A$ יש $4$ עמודות", r"כן, כי $\mathrm{Ker}\,T\neq\{0\}$"],
            r"על אם ורק אם הדרגה שווה למימד הטווח $3$."),
    ])

ENR[(5, "ג")] = dict(
    rubric=rub((r"$v\in\mathrm{Im}\,T$ אם ורק אם $v$ צירוף של בסיס התמונה", 1),
               (r"הרכבת המטריצה המורחבת עם $v=(k,7,10)$", 1),
               (r"דירוג: השורה האחרונה $0\ 0\,|\,k-4$", 1),
               (r"עקביות אם ורק אם $k=4$", 1)),
    pitfalls=[r"לדרג רק את מטריצת המקדמים ולשכוח את עמודת אגף ימין עם $k$."],
    steps=[
        num(r"בשורה האחרונה בצורה המדורגת, אגף ימין הוא $k-4$. מהו הערך שלו עבור $k=7$?", 3, r"$7-4=3$."),
        num(r"לאיזה $k$ הווקטור $(k,7,10)$ שייך ל-$\mathrm{Im}\,T$?", 4, r"נדרש $k-4=0$."),
        num(r"עבור $k=4$ מתקיים $(4,7,10)=x_1(1,1,1)+x_2(1,2,3)$. מהו $x_1$?", 1, r"$x_1+x_2=4$, $x_1+2x_2=7$, ולכן $x_2=3$, $x_1=1$."),
    ])

ENR[(5, "ד")] = dict(
    rubric=rub((r"בדיקה ש-$B$ בסיס: דטרמיננטה $1\neq0$", 1),
               (r"המטריצה $[F]_E^E=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$", 1),
               (r"נוסחת החלפת בסיס $[F]_B^B=P^{-1}[F]_E^EP$", 1),
               (r"חישוב $P^{-1}=\begin{pmatrix}7&-2\\-17&5\end{pmatrix}$ והכפלה", 1),
               (r"התוצאה $\begin{pmatrix}178&73\\-434&-178\end{pmatrix}$", 1)),
    pitfalls=[r"לכתוב את הנוסחה בסדר הפוך $P[F]_E^EP^{-1}$.",
              r"טעות חשבונית בהכפלת מטריצות $2\times2$ (מומלץ לבדוק ש-$\mathrm{tr}[F]_B^B=\mathrm{tr}[F]_E^E=0$)."],
    steps=[
        num(r"מהי הדטרמיננטה של $P=\begin{pmatrix}5&2\\17&7\end{pmatrix}$ (עמודותיה הווקטורים של $B$)?", 1, r"$35-34=1\neq0$, ולכן $B$ בסיס."),
        cho(r"איזו נוסחה נותנת את $[F]_B^B$ (כאשר $P$ מטריצת עמודות הבסיס $B$)?", r"$P^{-1}[F]_E^EP$",
            [r"$P[F]_E^EP^{-1}$", r"$P^{-1}[F]_E^E$", r"$[F]_E^EP^{-1}$"],
            r"הצגת וקטור בבסיס $B$ היא $P^{-1}$ כפול הווקטור, ולכן $[F]_B^B=P^{-1}[F]_E^EP$. שאר הנוסחאות נותנות מטריצות אחרות."),
        num(r"מהי הכניסה בשורה 1 עמודה 1 של $[F]_B^B$?", 178, r"$7\cdot22+(-2)(-12)=154+24=178$."),
        num(r"מהי הכניסה בשורה 1 עמודה 2 של $[F]_B^B$?", 73, r"$7\cdot9+(-2)(-5)=63+10=73$."),
    ])


for q in questions:
    if q.get("hold"):
        continue
    e = ENR[(q["num"], q["part"])]
    if q.get("points") is not None:
        assert sum(r["points"] for r in e["rubric"]) == q["points"], (q["num"], q["part"])
    assert 2 <= len(e["steps"]) <= 5 and 1 <= len(e["pitfalls"]) <= 3 and 3 <= len(e["rubric"]) <= 5, (q["num"], q["part"])
    q.update(rubric=e["rubric"], rubricSource="ai-draft", pitfalls=e["pitfalls"], steps=e["steps"], stepsSource="ai-draft")


exam = {
    "examCode": "22A-B",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״ב, מועד ב׳ (13.03.2022)",
    "year": 2022,
    "examDate": "13.03.2022",
    "sourceFile": "22A-B exam + official solution (PDF)",
    "solutionFile": "22A-B exam + official solution (PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
