# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-B.json -- linear algebra, semester A 2022, moed B (13.03.2022), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22A-B.py

Source: one PDF (7pp): the exam text followed question by question by the typed official solution.
Five questions of 25 points (best 4 count), 20 items: 15 transcribed with the official solution, 5 held (Q4 a-e).

Transcription notes
- Q4 (subspaces U, W of R_3[x], parts a-e): the solution file has NO solution for Q4 (the solutions jump from Q3 to Q5).
  All five parts are held "no-key" for the solver. The exam prints "ממעלה שחוש", a typo of "ממעלה שלוש"; written as
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

# ------------------------------------------------------------------ Q4 (no official solution: held)
for part, qtext, pts in [
    ("א", r"באמצעות הקריטריון לתת מרחב, הוכיחו כי $U$ הוא תת מרחב של $\mathbb{R}_3[x]$, מצאו בסיס ומימד ל-$U$.", 5),
    ("ב", r"באמצעות הקריטריון לתת מרחב, הוכיחו כי $W$ הוא תת מרחב של $\mathbb{R}_3[x]$, מצאו בסיס ומימד ל-$W$.", 5),
    ("ג", r"חשבו תת מרחב $U+W$, מצאו בסיס ומימד של תת מרחב זה.", 5),
    ("ד", r"חשבו תת מרחב $U\cap W$, מצאו בסיס ומימד של תת מרחב זה.", 5),
    ("ה", r"יהי $q(x)$ פולינום מתת מרחב $U\cap W$ כך המקיים את התכונה $q(1)=1$. מצאו $q'(1)$ ו-$q'(\sqrt2)$.", 5),
]:
    questions.append({"num": 4, "part": part, "kind": "computation", "topic": "vector_spaces", "points": pts,
                      "question": qtext, "contextId": "c4", "hold": "no-key"})

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
