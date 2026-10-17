# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json -- linear algebra, semester B 2023, moed B (05.07.2023), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23B-B.py

Source: exam PDF (3pp) + the "+ solution" PDF (7pp, typed full solutions). The same solution file is the one mislabeled
as "2020 semester A moed B" in the folder tree (byte-identical); there is no real 20A-B sitting.
Five questions of 25 points (best 4 count), 20 items. No figures.

Transcription notes
- Q1 is four unrelated items (the exam says there is no connection between the parts).
- Q1 point split: the exam prints (7,5,6,7) for (a,b,c,d); the solution file prints (7,6,7,5). The exam is followed.
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (B); in the raw schema item 2 is part "gimel".
- Q5 has two numbered items: item 1 (T, parts a-d) and item 2 (change of basis), which is part "he".
- Q2: the official solution treats a=0 (infinitely many solutions) and a=-1 (no solution) as the special cases.
- Q5 c/d: the exam prints m x^0 + 2023x - 2023x^2; the solution writes it as m + 2023t - 2023t^2. Same polynomial.

Checks (sympy, tools/verify/23B-B/verify_23B-B.py): every official computation reproduces (parametric solution of Q2,
roots, both inverses and the elementary-matrix product, charpoly, P and D with PD=BP, W1/W2 bases and dimensions,
W1+W2 and W1 cap W2, Ker/Im of T, m=20230, k=101, [I]_C^B). No mismatch, no hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"


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
    "c1": {"kind": "text", "title": "שאלה 1", "text": "אין שום קשר בין הסעיפים."},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": J(r"נתונה מערכת המשוואות עם פרמטר ממשי $a$:",
                     r"$$\begin{cases} ax+y+z=2\\ x+y+2z=5\\ x-y+az=a+1\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
           "text": r"נתונה המטריצה $A=" + pm("1&6&0", "0&1&2", "5&30&3") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של פולינומים",
           "text": J(r"במרחב הפולינומים $\mathbb{R}_3[x]$ נגדיר שני תתי-מרחבים",
                     r"$W_1=\{p(x)\in\mathbb{R}_3[x]\mid p'(1)=p(-1)=0\}$",
                     r"$W_2=\{p(x)=ax^3+bx^2+cx+d\in\mathbb{R}_3[x]\mid a-b-c+d=0\}$")},
    "c5": {"kind": "text", "title": "שאלה 5 - סעיפים א עד ד",
           "text": J(r"נתונה העתקה לינארית $T:\mathbb{R}_2[x]\to\mathbb{R}^4$ המוגדרת על ידי:",
                     r"$$T(1)=" + pm("1", "1", "1", "1") + r",\quad T(x)=" + pm("1", "2", "1", "1") + r",\quad T(x^2)=" + pm("11", "12", "11", "11") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "eigen_diagonalization",
    r"ידוע ש-$\lambda\neq0$ הוא ערך עצמי שמתאים לווקטור עצמי $\mathbf{x}$ של מטריצה הפיכה $B$. הוכיחו ש-$\mathbf{x}$ הוא גם ווקטור עצמי של $B^{-1}$. מהו ערך עצמי של $B^{-1}$ המתאים ל-$\mathbf{x}$?",
    J(r"נתון ש-$B\mathbf{x}=\lambda\mathbf{x}$. נכפול את זה משני הצדדים משמאל ב-$B^{-1}$ ונקבל $B^{-1}B\mathbf{x}=\lambda B^{-1}\mathbf{x}$, או",
      r"$$\mathbf{x}=I\mathbf{x}=\lambda B^{-1}\mathbf{x}\ \Leftarrow\ B^{-1}\mathbf{x}=\frac{1}{\lambda}\mathbf{x}$$",
      r"זה מוכיח ש-$\mathbf{x}$ הוא גם ווקטור עצמי של $B^{-1}$ עם ערך עצמי $\frac{1}{\lambda}$."),
    7, contextId="c1"))

questions.append(Q(
    1, "ב", "computation", "matrix_algebra",
    r"ידוע שהמטריצות $A,B$ הפיכות כך שמתקיים $AXB=A+B$. מצאו את המטריצה $X$.",
    J(r"$$AXB=A+B\ \Rightarrow\ A^{-1}AXB=A^{-1}(A+B)\ \Rightarrow\ XB=I+A^{-1}B\ \Rightarrow\ XBB^{-1}=\left(I+A^{-1}B\right)B^{-1}$$",
      r"מכאן נקבל סופית:",
      r"$$X=B^{-1}+A^{-1}$$"),
    5, contextId="c1"))

questions.append(Q(
    1, "ג", "proof", "matrix_proofs",
    r"תהי $A\in M_{n\times n}(\mathbb{R})$ מטריצה המקיימת את $A^3-5A-4I=0$. הוכח ש-$A$ היא הפיכה ומצאו את הביטוי עבור $A^{-1}$ באמצעות מטריצה $A$.",
    J(r"נרשום את המשוואה בצורה $A^3-5A=4I$. מכאן",
      r"$$A\left(\frac{1}{4}\left(A^2-5I\right)\right)=I\ \Leftarrow\ A^{-1}=\frac{1}{4}\left(A^2-5I\right)$$",
      r"כלומר $A$ הפיכה, וההופכית שלה היא $\frac{1}{4}(A^2-5I)$."),
    6, contextId="c1"))

questions.append(Q(
    1, "ד", "proof", "eigen_diagonalization",
    r"נניח ש-$A,B$ ו-$P$ הן מטריצות $n\times n$ וידוע ש-$P$ הפיכה וגם $PA=BP$. הוכיחו שכל ערך עצמי של $A$ הוא גם ערך עצמי של $B$.",
    J(r"נניח ש-$\lambda$ הוא ערך עצמי של $A$ כך שמתקיים $A\mathbf{x}=\lambda\mathbf{x}$ עבור $\mathbf{x}$ מסוים. אז",
      r"$$PA\mathbf{x}=P\lambda\mathbf{x}=\lambda P\mathbf{x}=BP\mathbf{x}$$",
      r"אם נסמן $\mathbf{y}=P\mathbf{x}$, אז נוכל לרשום $BP\mathbf{x}=\lambda P\mathbf{x}$, כלומר $B\mathbf{y}=\lambda\mathbf{y}$. "
      r"מכיוון ש-$P$ הפיכה ו-$\mathbf{x}\neq 0$, גם $\mathbf{y}=P\mathbf{x}\neq 0$, ולכן $\lambda$ הוא ערך עצמי של $B$."),
    7, contextId="c1"))

# ------------------------------------------------------------------ Q2
R0 = [["a", "1", "1", "2"], ["1", "1", "2", "5"], ["1", "-1", "a", "a+1"]]
R1 = [["a+1", "0", "a+1", "a+3"], ["1", "1", "2", "5"], ["2", "0", "a+2", "a+6"]]
R2 = [["1", "0", "1", r"\frac{a+3}{a+1}"], ["1", "1", "2", "5"], ["2", "0", "a+2", "a+6"]]
R3 = [["1", "0", "1", r"\frac{a+3}{a+1}"], ["0", "2", "2-a", "4-a"], ["2", "0", "a+2", "a+6"]]
R4 = [["1", "0", "1", r"\frac{a+3}{a+1}"], ["0", "2", "2-a", "4-a"], ["0", "0", "a", r"\frac{(a+6)(a+1)-2(a+3)}{a+1}"]]
R5 = [["1", "0", "1", r"\frac{a+3}{a+1}"], ["0", "2", "2-a", "4-a"], ["0", "0", "a(a+1)", "a(a+5)"]]
ECH = J(r"נדרג ונמצא:",
        "$$" + aug(R0) + arrow(r"\substack{R_1+R_3\to R_1\\R_2+R_3\to R_3}") + aug(R1) + arrow(r"\frac{1}{a+1}R_1\to R_1\ (a\neq-1)") + aug(R2) + "$$",
        "$$" + arrow(r"2R_2-R_3\to R_2") + aug(R3) + arrow(r"R_3-2R_1\to R_3") + aug(R4) + arrow(r"(a+1)R_3\to R_3") + aug(R5) + "$$")

questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"עבור אילו ערכים של הפרמטר $a$ יש פתרון יחיד למערכת? כתבו את הפתרון כפונקציה של הפרמטר, $(x(a),y(a),z(a))$.",
    J(ECH,
      r"במהלך הדירוג מצאנו שלושה ערכים חשודים: $a=0,-1$. בשורה השלישית נציב $a=0$ ונקבל שורת אפסים, כלומר אינסוף פתרונות. עבור $a=-1$, נציב בשורה השלישית ונקבל סתירה.",
      r"לסיכום, פתרון יחיד מתקבל עבור כל $a\neq 0,-1$:",
      r"$$x=-\frac{2}{a+1},\qquad y=\frac{3(a-1)}{a+1},\qquad z=\frac{a+5}{a+1}$$"),
    7, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $a$ אין פתרון למערכת?",
    r"מהדירוג בסעיף הקודם: עבור $a=-1$ מתקבלת סתירה בשורה השלישית, ולכן **אין פתרון** למערכת כאשר $a=-1$.",
    6, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $a$ יש אינסוף פתרונות למערכת? הציגו את אינסוף הפתרונות בצורה פרמטרית.",
    J(r"אינסוף פתרונות עבור $a=0$. נציב $a=0$ במערכת המקורית:",
      r"$$\begin{cases} y+z=2\\ x+y+2z=5\\ x-y=1\end{cases}\ \Rightarrow\ (x,y,z)=(3-z,\,2-z,\,z)=(3,2,0)+z(-1,-1,1),\quad z\in\mathbb{R}$$"),
    7, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"נתונה המשוואה $z^2-(2+i)z+(-1+7i)=0$. חשבו את השורשים והציגו אותם בצורה $x+iy$.",
    J(r"נמצא את שני השורשים המרוכבים של המשוואה. נציב בנוסחת הבינום:",
      r"$$z_{1,2}=\frac{2+i\pm\sqrt{(2+i)^2-4(-1+7i)}}{2}=\frac{2+i\pm\sqrt{7-24i}}{2}$$",
      r"נחשב את השורש: $\sqrt{7-24i}=a+ib\Rightarrow 7-24i=(a+ib)^2=a^2-b^2+i\,2ab$",
      r"$$\Rightarrow\ \begin{cases}a^2-b^2=7\\ ab=-12\end{cases}\ \Rightarrow\ \begin{cases}a=4,\ b=-3\\ a=-4,\ b=3\end{cases}$$",
      r"ונקבל את השורשים:",
      r"$$z_1=\frac{2+i+(4-3i)}{2}=3-i,\qquad z_2=\frac{2+i-(4-3i)}{2}=-1+2i$$"),
    5, contextId="c2"))

# ------------------------------------------------------------------ Q3
Ai_aug = [
    (aug([["1", "6", "0", "1", "0", "0"], ["0", "1", "2", "0", "1", "0"], ["5", "30", "3", "0", "0", "1"]]), r"R_3\to R_3-5R_1"),
    (aug([["1", "6", "0", "1", "0", "0"], ["0", "1", "2", "0", "1", "0"], ["0", "0", "3", "-5", "0", "1"]]), r"R_3\to\frac{1}{3}R_3"),
    (aug([["1", "6", "0", "1", "0", "0"], ["0", "1", "2", "0", "1", "0"], ["0", "0", "1", r"-\frac{5}{3}", "0", r"\frac{1}{3}"]]), r"R_2\to R_2-2R_3"),
    (aug([["1", "6", "0", "1", "0", "0"], ["0", "1", "0", r"\frac{10}{3}", "1", r"-\frac{2}{3}"], ["0", "0", "1", r"-\frac{5}{3}", "0", r"\frac{1}{3}"]]), r"R_1\to R_1-6R_2"),
    (aug([["1", "0", "0", "-19", "-6", "4"], ["0", "1", "0", r"\frac{10}{3}", "1", r"-\frac{2}{3}"], ["0", "0", "1", r"-\frac{5}{3}", "0", r"\frac{1}{3}"]]), None),
]
inv_chain = "$$" + "".join(m + (arrow(op) if op else "") for m, op in Ai_aug) + "$$"
AINV = pm("-19&-6&4", r"\frac{10}{3}&1&-\frac{2}{3}", r"-\frac{5}{3}&0&\frac{1}{3}")

questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הוכיחו ש-$A$ הפיכה על ידי מציאת המטריצה $A^{-1}$.",
    J(r"נחשב את $A^{-1}$:", inv_chain,
      r"קיבלנו שהמטריצה ההופכית היא:",
      r"$$A^{-1}=" + AINV + "$$"),
    6, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"הציגו את $A^{-1}$ בצורת מכפלה של מטריצות אלמנטריות.",
    J(r"כעת נשתמש בדירוג הנ״ל ונכתוב את $A^{-1}$ כמכפלה של מטריצות אלמנטריות:",
      r"$$A^{-1}=" + pm("1&-6&0", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&-2", "0&0&1") + pm("1&0&0", "0&1&0", r"0&0&\frac{1}{3}") + pm("1&0&0", "0&1&0", "-5&0&1") + "$$"),
    7, contextId="c3"))

B3 = pm("1&2&1", "-3&6&1", "0&0&4")
questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + B3 + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $PD=BP$. בדקו שזה מתקיים בפועל.",
    J(r"תחילה נמצא את כל הערכים העצמיים והווקטורים העצמיים של $B$. נחשב את הדטרמיננטה הבאה לפי שורה שלישית:",
      r"$$|\lambda I-B|=\begin{vmatrix}\lambda-1&-2&-1\\3&\lambda-6&-1\\0&0&\lambda-4\end{vmatrix}=(\lambda-4)\begin{vmatrix}\lambda-1&-2\\3&\lambda-6\end{vmatrix}=(\lambda-4)[(\lambda-1)(\lambda-6)+6]=(\lambda-4)(\lambda^2-7\lambda+12)=(\lambda-4)(\lambda-3)(\lambda-4)$$",
      r"קיבלנו שהערכים העצמיים הם: $3,4$. כעת נמצא את הווקטורים העצמיים.",
      r"**עבור ע״ע 3:**",
      r"$$" + pm("2&-2&-1", "3&-3&-1", "0&0&-1") + r"\to\cdots\to" + pm("1&-1&0", "0&0&1", "0&0&0") + "$$",
      r"נסמן $y=t$ ונקבל $x=t,\ z=0$. הוקטור העצמי המתקבל הוא $(1,1,0)^T$.",
      r"**עבור ע״ע 4:**",
      r"$$" + pm("3&-2&-1", "3&-2&-1", "0&0&0") + r"\to\cdots\to" + pm(r"1&-\frac{2}{3}&-\frac{1}{3}", "0&0&0", "0&0&0") + "$$",
      r"נסמן $y=t,\ z=s$ ונקבל $x=\frac{2}{3}t+\frac{1}{3}s$. הוקטורים העצמיים המתקבלים הם $\left(\frac{2}{3},1,0\right)^T,\ \left(\frac{1}{3},0,1\right)^T$, וניתן לכתוב גם כך: $(2,3,0)^T,\ (1,0,3)^T$.",
      r"המטריצה ניתנת לליכסון (שלושה וקטורים עצמיים בלתי תלויים). כעת נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$ (כלומר $PD=BP$):",
      r"$$D=" + pm("3&0&0", "0&4&0", "0&0&4") + r",\qquad P=" + pm("1&2&1", "1&3&0", "0&0&3") + "$$",
      r"נבדוק שמתקיים $PD=BP$:",
      r"$$PD=" + pm("1&2&1", "1&3&0", "0&0&3") + pm("3&0&0", "0&4&0", "0&0&4") + "=" + pm("3&8&4", "3&12&0", "0&0&12") + "$$",
      r"$$BP=" + pm("1&2&1", "-3&6&1", "0&0&4") + pm("1&2&1", "1&3&0", "0&0&3") + "=" + pm("3&8&4", "3&12&0", "0&0&12") + "$$",
      r"ואכן מתקיים השוויון."),
    12))

# ------------------------------------------------------------------ Q4
RB = [["1", "1", "-1", "-3", "2"], ["1", "0", "0", "2", "-3"], ["0", "1", "0", "5", "0"], ["0", "0", "1", "0", "5"]]
RB2 = [["1", "0", "0", "0", "-1"], ["0", "1", "0", "0", "5"], ["0", "0", "1", "0", "5"], ["0", "0", "0", "1", "-1"]]
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1$ ו-$W_2$.",
    J(r"הצורה הכללית של פולינום $p(x)\in\mathbb{R}_3[x]$ היא $p(x)=ax^3+bx^2+cx+d$. נטיל את התנאים המגדירים את $W_1$:",
      r"$$p'(1)=[3ax^2+2bx+c]_{x=1}=3a+2b+c=0,\qquad p(-1)=-a+b-c+d=0$$",
      r"קיבלנו מערכת משוואות הומוגנית. נפתור מערכת זו:",
      r"$$" + pm("3&2&1&0", "-1&1&-1&1") + r"\xrightarrow{\text{reduce}}" + pm(r"1&0&\frac{3}{5}&-\frac{2}{5}", r"0&1&-\frac{2}{5}&\frac{3}{5}") + "$$",
      r"כאן $c,d$ הם משתנים חופשיים. נבצע פרמטריזציה $c=s,\ d=t$ ונקבל",
      r"$$a=-\frac{3}{5}s+\frac{2}{5}t,\quad b=\frac{2}{5}s-\frac{3}{5}t\ \Rightarrow\ " + pm("a", "b", "c", "d") + "=" + r"\frac{1}{5}s" + pm("-3", "2", "5", "0") + r"+\frac{1}{5}t" + pm("2", "-3", "0", "5") + "$$",
      r"מכאן נקבל ש-$B_{W_1}=\{(-3x^3+2x^2+5x),\,(2x^3-3x^2+5)\}$ הוא בסיס של $W_1$ ו-$\dim(W_1)=2$.",
      r"נמצא בסיס של $W_2$. תת-המרחב $W_2$ מוגדר על ידי המשוואה $a-b-c+d=0$. במערכת זו $b,c,d$ הם משתנים חופשיים. נבצע פרמטריזציה $b=r,\ c=s,\ d=t$ ונקבל",
      r"$$" + pm("a", "b", "c", "d") + "=" + pm("r+s-t", "r", "s", "t") + "=r" + pm("1", "1", "0", "0") + "+s" + pm("1", "0", "1", "0") + "+t" + pm("-1", "0", "0", "1") + "$$",
      r"מכאן נקבל ש-$B_{W_2}=\{(x^3+x^2),\,(x^3+x),\,(-x^3+1)\}$ הוא בסיס של $W_2$ ו-$\dim(W_2)=3$."),
    6, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1+W_2$.",
    J(r"כדי למצוא בסיסים ל-$W_1+W_2$ ו-$W_1\cap W_2$ נבנה מטריצה שעמודותיה הן (וקטורי הקואורדינטות של) וקטורי הבסיס שמצאנו:",
      "$$" + aug(RB, 4) + r"\xrightarrow{\text{reduce}}" + aug(RB2, 4) + "$$",
      r"מהדירוג הנ״ל נקבל שקיימים 4 וקטורים בבסיס של $W_1+W_2$. מכאן ש-$\dim(W_1+W_2)=4$. כיוון ש-$W_1+W_2$ הוא תת-מרחב של $\mathbb{R}_3[x]$ ו-$\dim(\mathbb{R}_3[x])=4$ נקבל ש-$W_1+W_2=\mathbb{R}_3[x]$ ולכן נוכל לקחת כבסיס של $W_1+W_2$ כל בסיס של $\mathbb{R}_3[x]$. למשל, הבסיס הסטנדרטי $E=\{1,x,x^2,x^3\}$."),
    8, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1\cap W_2$.",
    J(r"ממשפט המימדים לתתי-מרחב נקבל ש",
      r"$$\dim(W_1\cap W_2)=\dim(W_1)+\dim(W_2)-\dim(W_1+W_2)=2+3-4=1$$",
      r"כדי למצוא בסיס עבור $W_1\cap W_2$ נפתור את המערכת ההומוגנית המוגדרת על ידי המטריצה שדירגנו. אם נסמן את המקדמים של וקטורי הבסיס של $W_1$ ב-$\alpha_1,\alpha_2,\alpha_3$ ואת המקדמים של וקטורי הבסיס של $W_2$ ב-$\beta_1,\beta_2,\beta_3$ אזי $\beta_2$ הוא משתנה חופשי. נבצע פרמטריזציה $\beta_2=t$ ונקבל $\beta_1=\beta_2=t$. מכאן נקבל,",
      r"$$p(x)\in W_1\cap W_2\ \Leftrightarrow\ " + pm("a", "b", "c", "d") + "=t" + pm("-3", "2", "5", "0") + "+t" + pm("2", "-3", "0", "5") + "=t" + pm("-1", "-1", "5", "5") + "$$",
      r"ולכן $B_{W_1\cap W_2}=\{(-x^3-x^2+5x+5)\}$ הוא בסיס של $W_1\cap W_2$."),
    8, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם $2x^3+2x^2-10x-10\in W_1\cap W_2$?",
    r"$2x^3+2x^2-10x-10=-2\left(-x^3-x^2+5x+5\right)\in W_1\cap W_2$. כלומר, **כן**.",
    3, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד ובסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    J(r"נסמן ב-$F=(1,t,t^2)$ בסיס סטנדרטי של $\mathbb{R}_2[t]$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^4$. מטריצה מייצגת סטנדרטית היא",
      r"$$A=[T]_E^F=" + pm("1&1&11", "1&2&12", "1&1&11", "1&1&11") + "$$",
      r"$$" + aug([["1", "1", "11", "0"], ["1", "2", "12", "0"], ["1", "1", "11", "0"], ["1", "1", "11", "0"]], 3) + r"\Leftrightarrow" + aug([["1", "1", "11", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], 3) + "$$",
      r"עמודות מס׳ 1,2 של המטריצה המדורגת מובילות, אז העמודות מס׳ 1,2 של $A$ הן בסיס של $\mathrm{Col}\,A$, כלומר בסיס של $\mathrm{Im}\,T$ הוא $\left\{" + pm("1", "1", "1", "1") + "," + pm("1", "2", "1", "1") + r"\right\}$ ואז $\dim\mathrm{Im}\,T=2$.",
      r"$$" + aug([["1", "1", "11", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "0"]], 3) + r"\Leftrightarrow" + aug([["1", "0", "10", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "0"]], 3)
      + r"\Leftrightarrow\begin{cases}x_1=-10s\\x_2=-s\\x_3=s\end{cases}\Leftrightarrow" + pm("x_1", "x_2", "x_3") + "=s" + pm("-10", "-1", "1") + "$$",
      r"אז בסיס של $\mathrm{Ker}\,T$ הוא $\left(-10-t+t^2\right)$ ו-$\dim\mathrm{Ker}\,T=1$."),
    11, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ חד חד ערכית? האם $T$ על? נמקו.",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=1\neq0$, ו-$T$ לא על כי $\dim\mathrm{Im}\,T=2\neq\dim\mathbb{R}^4$.",
    3, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטר $m$ מתקיים $mx^0+2023x-2023x^2\in\mathrm{Ker}\,T$?",
    J(r"$$m+2023t-2023t^2=k\left(-10-t+t^2\right)=-10k-kt+kt^2$$",
      r"$$m=-10k,\quad 2023=-k,\quad -2023=k\ \Rightarrow\ k=-2023\ \Rightarrow\ m=20230$$"),
    3, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"לאילו ערכים של $k$ מתקיים $" + pm("101", "102", "101", "k") + r"\in\mathrm{Im}\,T$?",
    J(r"$$" + aug([["1", "1", "101"], ["1", "2", "102"], ["1", "1", "101"], ["1", "1", "k"]], 2) + r"\to" + aug([["1", "1", "101"], ["0", "1", "1"], ["0", "0", "0"], ["0", "0", "k-101"]], 2)
      + r"\to" + aug([["1", "1", "101"], ["0", "1", "1"], ["0", "0", "k-101"], ["0", "0", "0"]], 2) + "$$",
      r"ולכן $k=101$."),
    3, contextId="c5"))

questions.append(Q(
    5, "ה", "computation", "linear_maps",
    r"נתונים בסיסים $B=\left(" + pm("1", "10") + "," + pm("1", "11") + r"\right)$, $C=\left(" + pm("1", "4") + "," + pm("5", "19") + r"\right)$ של מרחב $\mathbb{R}^2$. מצאו את מטריצת המעבר $[I]_C^B$ מבסיס $B$ לבסיס $C$.",
    J(r"**שיטה 1.** $E$ בסיס סטנדרטי של $\mathbb{R}^2$:",
      r"$$[I]_E^B=" + pm("1&1", "10&11") + r",\quad [I]_E^C=" + pm("1&5", "4&19") + "$$",
      r"$$[I]_C^B=[I]_C^E[I]_E^B=\left([I]_E^C\right)^{-1}[I]_E^B=" + pm("1&5", "4&19") + r"^{-1}" + pm("1&1", "10&11") + "=" + pm("-19&5", "4&-1") + pm("1&1", "10&11") + "=" + pm("31&36", "-6&-7") + "$$",
      r"**שיטה 2.**",
      r"$$" + aug([["1", "5", "1", "1"], ["4", "19", "10", "11"]], 2) + r"\to" + aug([["1", "5", "1", "1"], ["0", "-1", "6", "7"]], 2) + r"\to" + aug([["1", "5", "1", "1"], ["0", "1", "-6", "-7"]], 2)
      + r"\to" + aug([["1", "0", "31", "36"], ["0", "1", "-6", "-7"]], 2) + r"\to[I]_C^B=" + pm("31&36", "-6&-7") + "$$"),
    5))

exam = {
    "examCode": "23B-B",
    "examLabel": "מבחן סוף סמסטר ב׳ תשפ״ג, מועד ב׳ (05.07.2023)",
    "year": 2023,
    "examDate": "05.07.2023",
    "sourceFile": "23B-B exam (PDF)",
    "solutionFile": "23B-B official solution (PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
