# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-A.json -- linear algebra, semester A 2022, moed A (09.02.2022), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22A-A.py

Source: one PDF (12pp): the exam text followed question by question by the official solution (typed; Q4 handwritten).
Five questions of 25 points (best 4 count), 19 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (B); item 2 is part "gimel" here.
- Q5 has two numbered items: item 1 (T, parts a-c) and item 2 (F); item 2 is part "dalet" here.
- Q4 prints W_1 twice; the second definition (vector b) is W_2 (the solution says so). Written as W_2.
- Q2 b (final-answer error): the official says b!=6 -> no solution, b=6 -> infinitely many. Row 2 of its own final matrix is
  (0 a^2-a a^2-a 0 | a), which is 0=1 at a=1, so a=1 has no solution for ANY b. Shipped corrected, labeled, official:false.
- Q2 c, d (final-answer errors): the official prints x=4-t2 (c) and x=4-t (d); the first equation x+2w=4 gives x=4-2w.
  Shipped corrected, labeled, official:false.

Checks (sympy, tools/verify/22A-A/verify_22A-A.py): Q1c CD and det=0, Q2 echelon form, rank/consistency table, the three
solution sets, Q2e root sum, Q3 A^-1 and the elementary product, charpoly, P and D, Q4 bases/sum/intersection/membership,
Q5 kernel, rank, [F]. Mismatches found are exactly the three Q2 slips above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-A.json"


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
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם שני פרמטרים",
           "text": J(r"נתונה מערכת המשוואות הבאה, כאשר $a,b\in\mathbb{R}$ פרמטרים ממשיים כלשהם:",
                     r"$$\begin{cases} x+2w=4\\ (a^2-a)y+(a^2-a)z=a\\ x+(a-1)z+(a+1)w=a+3\\ 2x+(a^2-a)y+(a^2+a-2)z+(2a+2)w=3a+b\end{cases}$$")},
    "c3a": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
            "text": r"נתונה מטריצה ריבועית $A=" + pm("1&3&0", "0&3&1", "1&3&1") + r"$."},
    "c3b": {"kind": "text", "title": "שאלה 3 - סעיף ג",
            "text": r"נתונה מטריצה $B=" + pm("1&1&0", "0&-2&0", "-1&0&3") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - שני תתי מרחבים של המרחב",
           "text": J(r"יהיו $W_1$ ו-$W_2$ שני תתי מרחבים של $\mathbb{R}^3$ המוגדרים כדלקמן:",
                     r"$$W_1=\left\{\vec r=" + pm("x", "y", "z") + r"\ \middle|\ \vec r\perp\vec a;\ \vec a=" + pm("1", "2", "-1") + r";\ x,y,z\in\mathbb{R}\right\}$$",
                     r"$$W_2=\left\{\vec r'=" + pm("x'", "y'", "z'") + r"\ \middle|\ \vec r'\perp\vec b;\ \vec b=" + pm("2", "1", "-1") + r";\ x',y',z'\in\mathbb{R}\right\}$$")},
    "c51": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
            "text": J(r"נתונה העתקה לינארית $T:\mathrm{M}_{2\times2}(\mathbb{R})\to\mathbb{R}^3$ המוגדרת על ידי הנוסחה",
                      r"$$T\left(" + pm("a&b", "c&d") + r"\right)=" + pm("a+b+c+d", "a+2b+2c+2d", "a+2b+3c+3d") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "determinants",
    r"נניח ש-$C$, $D$ מטריצות הפיכות המקיימות $CD^2=D^3C^{-1}$. הוכיחו ש-$\det(D)>0$.",
    J(r"מטריצות $C,D$ הפיכות, פירושו של דבר $\det C\neq0$, $\det D\neq0$. נשתמש בעובדה זו ובתכונות של פעולת הדטרמיננטה על כפל מטריצות:",
      r"$$\det\left(CD^2\right)=\det\left(D^3C^{-1}\right)\Rightarrow\det(C)\det\left(D^2\right)=\det\left(D^3\right)\det\left(C^{-1}\right)$$",
      r"$$\det\left(D^2\right)=\det(DD)=\det(D)\det(D)=(\det(D))^2,\qquad\det\left(D^3\right)=\det(DDD)=(\det(D))^3,\qquad\det\left(C^{-1}\right)=1/\det(C)$$",
      r"לכן נקבל",
      r"$$\det(C)(\det(D))^2=(\det(D))^3\frac{1}{\det(C)}\Rightarrow(\det(C))^2(\det(D))^2=(\det(D))^3$$",
      r"$$\Rightarrow0=(\det(D))^2\left(\det(D)-(\det(C))^2\right)\Rightarrow\det(D)=(\det(C))^2>0$$"),
    10))

questions.append(Q(
    1, "ב", "proof", "matrix_proofs",
    r"תהי $A$ מטריצה מסדר $n\times n$ מעל שדה $\mathbb{F}$ כך שהמטריצה $A-I_n$ הפיכה. $I_n$ היא מטריצת היחידה מסדר $n$. נניח שמתקיים $A^2=A$. הוכיחו ש-$A=0$.",
    J(r"מצד אחד",
      r"$$(A-I_n)(A-I_n)=AA-AI_n-I_nA+I_nI_n=A-A-A+I_n=-(A-I_n)$$",
      r"מאידך, $A-I_n$ הפיכה, ולכן אפשר להכפיל את שני האגפים ב-$(A-I_n)^{-1}$:",
      r"$$(A-I_n)\underbrace{(A-I_n)(A-I_n)^{-1}}_{I_n}=-\underbrace{(A-I_n)(A-I_n)^{-1}}_{I_n}$$",
      r"$$(A-I_n)I_n=-I_n\Rightarrow A-I_n=-I_n\Rightarrow A=-I_n+I_n=0$$"),
    10))

questions.append(Q(
    1, "ג", "proof", "matrix_algebra",
    r"תהיינה $C$ ו-$D$ מטריצות אנטי סימטריות מסדר $n$. הוכיחו או תנו דוגמה נגדית: מטריצה $CD$ היא הפיכה.",
    J(r"הטענה אינה נכונה. למשל, אם",
      r"$$C=" + pm("0&1&2", "-1&0&3", "-2&-3&0") + r",\qquad D=" + pm("0&1&1", "-1&0&1", "-1&-1&0") + r"$$",
      r"וחישוב $CD=" + pm("-3&-2&1", "-3&-4&-1", "3&-2&-5") + r"$ קל מראה ש-$\det(CD)=0$. כלומר, מטריצה $CD$ אינה הפיכה."),
    5))

# ------------------------------------------------------------------ Q2
A0 = [["1", "0", "0", "2", "4"], ["0", "a^2-a", "a^2-a", "0", "a"], ["1", "0", "a-1", "a+1", "a+3"], ["2", "a^2-a", "a^2+a-2", "2a+2", "3a+b"]]
A1 = [["1", "0", "0", "2", "4"], ["0", "a^2-a", "a^2-a", "0", "a"], ["0", "0", "a-1", "a-1", "a-1"], ["0", "a^2-a", "a^2+a-2", "2a-2", "3a+b-8"]]
A2 = [["1", "0", "0", "2", "4"], ["0", "a^2-a", "a^2-a", "0", "a"], ["0", "0", "a-1", "a-1", "a-1"], ["0", "0", "2a-2", "2a-2", "2a+b-8"]]
A3 = [["1", "0", "0", "2", "4"], ["0", "a^2-a", "a^2-a", "0", "a"], ["0", "0", "a-1", "a-1", "a-1"], ["0", "0", "0", "0", "b-6"]]
ECH2 = J(r"נבצע דירוג כדלקמן:",
         "$$" + aug(A0, 4) + arrow(r"\substack{R_3\to R_3-R_1\\R_4\to R_4-2R_1}") + aug(A1, 4) + "$$",
         "$$" + arrow(r"R_4\to R_4-R_2") + aug(A2, 4) + arrow(r"R_4\to R_4-2R_3") + aug(A3, 4) + "$$")

questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"הביאו את מטריצת המקדמים המורחבת של המערכת לצורה מדורגת.",
    J(r"מטריצת המקדמים המורחבת של המערכת הינה",
      "$$" + aug(A0, 4) + "$$", ECH2),
    7, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"מצאו עבור אילו ערכי $a,b$ יש למערכת אינסוף פתרונות, פתרון יחיד או שאין לה פתרון כלל.",
    J(FIX + r"בפתרון הרשמי נקבע שעבור $b\neq6$ אין פתרון ועבור $b=6$ יש אינסוף פתרונות. השורה השנייה במטריצה המדורגת, $(0\ \ a^2-a\ \ a^2-a\ \ 0\mid a)$, היא עבור $a=1$ השורה $(0\ 0\ 0\ 0\mid1)$, כלומר $0=1$ (סתירה), כך שעבור $a=1$ אין פתרון לכל $b$.",
      r"מהדירוג רואים:",
      r"- אם $b\neq6$ או $a=1$: אין פתרון למערכת (השורה האחרונה היא $0=b-6\neq0$, או השורה השנייה היא $0=1$ כאשר $a=1$).",
      r"- אם $b=6$ ו-$a\neq1$: יש למערכת אינסוף פתרונות (השורה האחרונה היא $0=0$, והדרגה קטנה מ-4 כמספר הנעלמים).",
      r"- אין מקרה שבו יש פתרון יחיד: הדרגה של מטריצת המקדמים קטנה מ-4 תמיד."),
    4, contextId="c2", solutionSource="solved", official=False))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור $a=0,\ b=6$ פתרו את המערכת וכתבו את כל הפתרונות.",
    J(FIX + r"בפתרון הרשמי נכתב $x=4-t_2$; מהמשוואה הראשונה $x+2w=4$ נובע $x=4-2t_2$.",
      r"המטריצה המתקבלת מהדירוג עבור $a=0,\ b=6$ היא",
      r"$$\left(\begin{array}{cccc|c}1&0&0&2&4\\0&0&0&0&0\\0&0&-1&-1&-1\\0&0&0&0&0\end{array}\right)$$",
      r"אוסף הפתרונות הינו",
      r"$$" + pm("x", "y", "z", "w") + "=" + pm("4-2t_2", "t_1", "1-t_2", "t_2") + r",\qquad t_1,t_2\in\mathbb{R}$$"),
    4, contextId="c2", solutionSource="solved", official=False))

questions.append(Q(
    2, "ד", "computation", "linear_systems",
    r"עבור $a=2,\ b=6$ פתרו את המערכת וכתבו את כל הפתרונות.",
    J(FIX + r"בפתרון הרשמי נכתב $x=4-t$; מהמשוואה הראשונה $x+2w=4$ נובע $x=4-2t$.",
      r"המטריצה המתקבלת מהדירוג עבור $a=2,\ b=6$ היא",
      r"$$\left(\begin{array}{cccc|c}1&0&0&2&4\\0&2&2&0&2\\0&0&1&1&1\\0&0&0&0&0\end{array}\right)$$",
      r"אוסף הפתרונות הינו",
      r"$$" + pm("x", "y", "z", "w") + "=" + pm("4-2t", "t", "1-t", "t") + r",\qquad t\in\mathbb{R}$$"),
    4, contextId="c2", solutionSource="solved", official=False))

questions.append(Q(
    2, "ה", "proof", "complex_numbers",
    r"נסמן ב-$z_0,z_1,z_2$ את כל הפתרונות של המשוואה $z^3=1$. הראו כי מתקיים $z_0+z_1+z_2=0$.",
    J(r"לפי נוסחת השורשים מתקיים",
      r"$$z_k=\cos\left(\frac{2\pi k}{3}\right)+i\sin\left(\frac{2\pi k}{3}\right)$$",
      r"ולכן מתקיים",
      r"$$z_0z_0=z_0\quad z_0z_1=z_1\quad z_0z_2=z_2$$",
      r"$$z_1z_0=z_1\quad z_1z_1=z_2\quad z_1z_2=z_0$$",
      r"$$z_2z_0=z_2\quad z_2z_1=z_0\quad z_2z_2=z_1$$",
      r"בפרט",
      r"$$z_0(z_0+z_1+z_2)=z_0+z_1+z_2$$",
      r"$$z_1(z_0+z_1+z_2)=z_1+z_2+z_0$$",
      r"$$z_2(z_0+z_1+z_2)=z_2+z_0+z_1$$",
      r"כלומר, מכפלה במספר המרוכב $z_k$ משנה את סדר המחוברים ב-$z_0+z_1+z_2$. נשים לב שמאחר ו-$z_1,z_2\neq1$ המספר היחיד שמקיים את המשוואה $z_1w=w$ (או $z_2w=w$) הוא המספר $w=0$. נסמן $w=z_0+z_1+z_2$. אז $z_1w=w$ ולכן $w=0$."),
    6))

# ------------------------------------------------------------------ Q3
Ai_aug = [
    (aug([["1", "3", "0", "1", "0", "0"], ["0", "3", "1", "0", "1", "0"], ["1", "3", "1", "0", "0", "1"]]), r"R_3-R_1"),
    (aug([["1", "3", "0", "1", "0", "0"], ["0", "3", "1", "0", "1", "0"], ["0", "0", "1", "-1", "0", "1"]]), r"R_2-R_3"),
    (aug([["1", "3", "0", "1", "0", "0"], ["0", "3", "0", "1", "1", "-1"], ["0", "0", "1", "-1", "0", "1"]]), r"R_1-R_2"),
    (aug([["1", "0", "0", "0", "-1", "1"], ["0", "3", "0", "1", "1", "-1"], ["0", "0", "1", "-1", "0", "1"]]), r"\frac{1}{3}R_2"),
    (aug([["1", "0", "0", "0", "-1", "1"], ["0", "1", "0", r"\frac{1}{3}", r"\frac{1}{3}", r"-\frac{1}{3}"], ["0", "0", "1", "-1", "0", "1"]]), None),
]
inv_chain = "$$" + "".join(m + (arrow(op) if op else "") for m, op in Ai_aug) + "$$"
AINV = pm("0&-1&1", r"\frac{1}{3}&\frac{1}{3}&-\frac{1}{3}", "-1&0&1")

questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הוכיחו ש-$A$ הפיכה על ידי מציאת המטריצה $A^{-1}$.",
    J(inv_chain, r"כלומר", r"$$A^{-1}=" + AINV + "$$"),
    6, contextId="c3a"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"הציגו את $A^{-1}$ בצורת כפל של מטריצות אלמנטריות.",
    J(r"התהליך שפותח בסעיף הקודם ניתן לתאר על ידי $E_4E_3E_2E_1A=I$ כאשר $E_4,E_3,E_2,E_1$ הן מטריצות אלמנטאריות המתקבלות בהתאם לפעולות השורה שבוצעו בצורה",
      r"$$E_1=" + pm("1&0&0", "0&1&0", "-1&0&1") + r",\ E_2=" + pm("1&0&0", "0&1&-1", "0&0&1") + r",\ E_3=" + pm("1&-1&0", "0&1&0", "0&0&1") + r",\ E_4=" + pm("1&0&0", r"0&\frac{1}{3}&0", "0&0&1") + "$$",
      r"מהמשוואה $E_4E_3E_2E_1A=I$ נובע ש-$A^{-1}=E_4E_3E_2E_1$."),
    7, contextId="c3a"))

questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"האם $B$ ניתנת ללכסון? במידה וכן, מצאו את $D$ מטריצה אלכסונית ו-$P$ מטריצה הפיכה כך שיתקיים $D=P^{-1}BP$.",
    J(r"ראשית, נחשב",
      r"$$\det(B-\lambda I)=\det" + pm(r"1-\lambda&1&0", r"0&-2-\lambda&0", r"-1&0&3-\lambda") + r"=(1-\lambda)(-2-\lambda)(3-\lambda)$$",
      r"ומכאן נובע שהערכים העצמיים של $B$ הם $\lambda_1=1,\ \lambda_2=-2,\ \lambda_3=3$. מכיוון שכל הערכים העצמיים הם ממשיים ושונים זה מזה, אז נקבל מסקנה ש-$B$ ניתנת ללכסון. עכשיו נמצא הווקטורים העצמיים של $B$.",
      r"(*) עבור $\lambda_1=1$ נקבל",
      r"$$B-\lambda_1I=B-I=" + pm("0&1&0", "0&-3&0", "-1&0&2") + r"\to" + pm("1&0&-2", "0&1&0", "0&0&0") + r"\Rightarrow\varphi_1=" + pm("2", "0", "1") + "$$",
      r"(*) עבור $\lambda_2=-2$ נקבל",
      r"$$B-\lambda_2I=B+2I=" + pm("3&1&0", "0&0&0", "-1&0&5") + r"\to" + pm("1&0&-5", "0&1&15", "0&0&0") + r"\Rightarrow\varphi_2=" + pm("5", "-15", "1") + "$$",
      r"(*) עבור $\lambda_3=3$ נקבל",
      r"$$B-\lambda_3I=B-3I=" + pm("-2&1&0", "0&-5&0", "-1&0&0") + r"\to" + pm("1&0&0", "0&1&0", "0&0&0") + r"\Rightarrow\varphi_3=" + pm("0", "0", "1") + "$$",
      r"מכאן נובע שאחת האופציות הקיימות עבור מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שיתקיים $D=P^{-1}BP$ היא",
      r"$$P=" + pm("2&5&0", "0&-15&0", "1&1&1") + r",\qquad D=" + pm("1&0&0", "0&-2&0", "0&0&3") + "$$"),
    12, contextId="c3b"))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של תתי המרחבים $W_1$ ו-$W_2$.",
    J(r"עבור $\vec r\in W_1$ תת מרחב $W_1$ מתקיים $\left(\vec r\cdot\vec a\right)=0$, כך ש-$x+2y-z=0$. כלומר, כל וקטור מ-$W_1$ הוא מהצורה",
      r"$$\vec r=" + pm("x", "y", "x+2y") + "=x" + pm("1", "0", "1") + "+y" + pm("0", "1", "2") + r",\qquad x,y\in\mathbb{R}$$",
      r"ולכן $W_1=\mathrm{Sp}\left\{" + pm("1", "0", "1") + "," + pm("0", "1", "2") + r"\right\}$. קבוצת הווקטורים שבפרט היא בלתי תלויה לינארית (כי אף אחד מהם אינו כפל בסקלר של השני), ולכן זה בסיס:",
      r"$$B_{W_1}=\left\{" + pm("1", "0", "1") + "," + pm("0", "1", "2") + r"\right\},\qquad\dim W_1=2$$",
      r"עבור $\vec r'\in W_2$ תת מרחב $W_2$ מתקיים $\left(\vec r'\cdot\vec b\right)=0$, כך ש-$2x+y-z=0$. כלומר, כל וקטור מ-$W_2$ הוא מהצורה",
      r"$$\vec r'=" + pm("x", "y", "2x+y") + "=x" + pm("1", "0", "2") + "+y" + pm("0", "1", "1") + r",\qquad x,y\in\mathbb{R}$$",
      r"ולכן $W_2=\mathrm{Sp}\left\{" + pm("1", "0", "2") + "," + pm("0", "1", "1") + r"\right\}$. קבוצת הווקטורים בלתי תלויה לינארית, ולכן זה בסיס:",
      r"$$B_{W_2}=\left\{" + pm("1", "0", "2") + "," + pm("0", "1", "1") + r"\right\},\qquad\dim W_2=2$$"),
    7, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"חשבו תת מרחב $W_1+W_2$, מצאו בסיס ומימד של תת מרחב זה.",
    J(r"$$W_1+W_2=\mathrm{Sp}\left\{B_{W_1},B_{W_2}\right\}=\mathrm{Sp}\left\{" + pm("1", "0", "1") + "," + pm("0", "1", "2") + "," + pm("1", "0", "2") + "," + pm("0", "1", "1") + r"\right\}$$",
      r"קבוצת הווקטורים הנ״ל היא קבוצה תלויה לינארית, ולכן יש לדרג, למשל (שורות המטריצה הן הווקטורים):",
      r"$$" + pm("1&0&1", "0&1&2", "1&0&2", "0&1&1") + arrow(r"\substack{R_2\to R_2-R_4\\R_3\to R_3-R_1}") + pm("1&0&1", "0&0&1", "0&0&1", "0&1&1") + arrow(r"R_2\leftrightarrow R_4") + pm("1&0&1", "0&1&1", "0&0&1", "0&0&1") + "$$",
      r"$$" + arrow(r"\substack{R_4\to R_4-R_3\\R_2\to R_2-R_3\\R_1\to R_1-R_3}") + pm("1&0&0", "0&1&0", "0&0&1", "0&0&0") + "$$",
      r"מכאן אנו קובעים את הבסיס:",
      r"$$B_{W_1+W_2}=\left\{" + pm("1", "0", "0") + "," + pm("0", "1", "0") + "," + pm("0", "0", "1") + r"\right\},\qquad\dim(W_1+W_2)=3$$"),
    7, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"חשבו תת מרחב $W_1\cap W_2$, מצאו בסיס ומימד של תת מרחב זה.",
    J(r"כל ווקטור $\vec w$ השייך ל-$W_1\cap W_2$ ניתן לרשום בשתי צורות:",
      r"$$\begin{cases}\vec w=\alpha_1" + pm("1", "0", "1") + r"+\alpha_2" + pm("0", "1", "2") + r"\\[2mm]\vec w=-\beta_1" + pm("1", "0", "2") + r"-\beta_2" + pm("0", "1", "1") + r"\end{cases}$$",
      r"מכאן נקבל מערכת המשוואות ההומוגנית בנעלמים $\{\alpha_1,\alpha_2,\beta_1,\beta_2\}$:",
      r"$$" + pm("1&0&1&0", "0&1&0&1", "1&2&2&1") + pm(r"\alpha_1", r"\alpha_2", r"\beta_1", r"\beta_2") + "=" + pm("0", "0", "0") + "$$",
      r"נדרג את מטריצת המקדמים:",
      r"$$" + pm("1&0&1&0", "0&1&0&1", "1&2&2&1") + arrow(r"R_3\to R_3-R_1") + pm("1&0&1&0", "0&1&0&1", "0&2&1&1") + arrow(r"R_3\to R_3-2R_2") + pm("1&0&1&0", "0&1&0&1", r"0&0&1&-1") + "$$",
      r"העמודה האחרונה ללא איבר מוביל, ולכן $\beta_2=t,\ t\in\mathbb{R}$, ומכאן $\beta_1=\beta_2=t$.",
      r"מכאן, כל ווקטור $\vec w$ השייך ל-$W_1\cap W_2$ ניתן לרשום בצורה הבאה:",
      r"$$\vec w=-t" + pm("1", "0", "2") + "-t" + pm("0", "1", "1") + "=-t" + pm("1", "1", "3") + "$$",
      r"כלומר $W_1\cap W_2=\mathrm{Sp}\left\{" + pm("1", "1", "3") + r"\right\}$, ולכן",
      r"$$B_{W_1\cap W_2}=\left\{" + pm("1", "1", "3") + r"\right\},\qquad\dim(W_1\cap W_2)=1$$"),
    7, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם הווקטור $" + pm("2", "2", "6") + r"$ שייך לתת מרחב $W_1\cap W_2$? נמקו!",
    J(r"מכיוון שהווקטור $" + pm("2", "2", "6") + r"$ הוא כפולה של $" + pm("1", "1", "3") + r"$, שהוא הווקטור הבסיס של $W_1\cap W_2$, הוא שייך לתת מרחב $W_1\cap W_2$."),
    4, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד והבסיס של $\mathrm{Im}\,T$ ושל $\mathrm{Ker}\,T$.",
    J(r"נסמן $B=\left(E_1=" + pm("1&0", "0&0") + r",E_2=" + pm("0&1", "0&0") + r",E_3=" + pm("0&0", "1&0") + r",E_4=" + pm("0&0", "0&1") + r"\right)$, בסיס סטנדרטי של $\mathrm{M}_{2\times2}(\mathbb{R})$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^3$.",
      r"$$T(E_1)=" + pm("1", "1", "1") + r",\ T(E_2)=" + pm("1", "2", "2") + r",\ T(E_3)=" + pm("1", "2", "3") + r",\ T(E_4)=" + pm("1", "2", "3") + "$$",
      r"המטריצה המייצגת הסטנדרטית היא",
      r"$$A=[T]_E^B=" + pm("1&1&1&1", "1&2&2&2", "1&2&3&3") + "$$",
      r"$$" + aug([["1", "1", "1", "1", "0"], ["1", "2", "2", "2", "0"], ["1", "2", "3", "3", "0"]], 4) + r"\to" + aug([["1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0"], ["0", "1", "2", "2", "0"]], 4) + r"\to" + aug([["1", "1", "1", "1", "0"], ["0", "1", "1", "1", "0"], ["0", "0", "1", "1", "0"]], 4) + "$$",
      r"עמודות מס׳ 1,2,3 של המטריצה המדורגת מובילות, אז בסיס של $\mathrm{Im}\,T$ הוא $\mathrm{Col}A$, כלומר $\left\{" + pm("1", "1", "1") + "," + pm("1", "2", "2") + "," + pm("1", "2", "3") + r"\right\}$, ואז $\dim(\mathrm{Im}\,T)=3$.",
      r"$$" + aug([["1", "1", "0", "0", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "1", "0"]], 4) + r"\to" + aug([["1", "0", "0", "0", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "1", "0"]], 4) + r"\Rightarrow\begin{cases}x_1=0\\x_2=0\\x_3=-t\\x_4=t\end{cases}\Rightarrow" + pm("x_1", "x_2", "x_3", "x_4") + "=t" + pm("0", "0", "-1", "1") + "$$",
      r"אז בסיס של $\mathrm{Nul}A$ הוא $\left\{" + pm("0", "0", "-1", "1") + r"\right\}$, ז״א בסיס של $\mathrm{Ker}\,T$ הוא $\left\{" + pm("0&0", "-1&1") + r"\right\}$ ואז $\dim(\mathrm{Ker}\,T)=1$."),
    12, contextId="c51"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חד חד ערכית? האם $T$ על? נמקו.",
    J(r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=1\neq0$, $T$ על כי $\dim\mathrm{Im}\,T=3=\dim\mathbb{R}^3$."),
    4, contextId="c51"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטר $k$ מתקיים $" + pm("k&0", "2&-2") + r"\in\mathrm{Ker}\,T$?",
    J(r"$$" + pm("k&0", "2&-2") + r"\in\mathrm{Ker}\,T\Leftrightarrow\left[" + pm("k&0", "2&-2") + r"\right]_B=" + pm("k", "0", "2", "-2") + r"\in\mathrm{Nul}A$$",
      r"$$" + pm("k", "0", "2", "-2") + "=t" + pm("0", "0", "-1", "1") + r"\Rightarrow t=-2\Rightarrow k=0$$"),
    4, contextId="c51"))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"נתונה העתקה לינארית $F:\mathbb{R}^2\to\mathbb{R}^2$ כך ש-$F\left(" + pm("2", "3") + r"\right)=" + pm("7", "3") + r",\ F\left(" + pm("3", "5") + r"\right)=" + pm("5", "2") + r"$. מצאו את המטריצה המייצגת $[F]_E^E$ של $F$. ($E$ בסיס סטנדרטי של $\mathbb{R}^2$)",
    J(r"נסמן $B=\left\{" + pm("2", "3") + "," + pm("3", "5") + r"\right\}$ בסיס של $\mathbb{R}^2$ (כי $\begin{vmatrix}2&3\\3&5\end{vmatrix}=1\neq0$). לכן $[I]_E^B=" + pm("2&3", "3&5") + r"$.",
      r"$$F\left(" + pm("2", "3") + r"\right)=" + pm("7", "3") + r",\ F\left(" + pm("3", "5") + r"\right)=" + pm("5", "2") + r"\Rightarrow[F]_E^B=" + pm("7&5", "3&2") + "$$",
      r"$$[F]_E^E=[I]_E^E[F]_E^B[I]_B^E=" + pm("1&0", "0&1") + pm("7&5", "3&2") + r"\left(" + pm("2&3", "3&5") + r"\right)^{-1}=" + pm("7&5", "3&2") + pm("5&-3", "-3&2") + "=" + pm("20&-11", "9&-5") + "$$"),
    5))

# ------------------------------------------------------------------ assemble
exam = {
    "examCode": "22A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״ב, מועד א׳ (09.02.2022)",
    "year": 2022,
    "examDate": "09.02.2022",
    "sourceFile": "22A-A exam with official solution (PDF, 12pp)",
    "solutionFile": "22A-A exam with official solution (PDF, 12pp)",
    "contexts": contexts,
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
