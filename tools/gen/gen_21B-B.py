# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-B.json -- linear algebra, semester B 2021, moed B (25.07.2021), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21B-B.py

Source: one PDF (9pp): the exam text followed question by question by the typed official solutions ("פתרונות מלאים").
Five questions of 25 points (best 4 count), 20 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts a-c) and item 2 (B); item 2 is part "dalet" here.
- Q5 (final-answer / whole-solution error): the exam defines T(a b; c d) = (a+b, d+c), but the official solution works with
  the different map (a+d, b+c) (its kernel is (a+d,b+c)=(0,0), T(1 1;0 0)=(1,1), ...). The linearity proof, the kernel basis
  and the matrix of part d therefore do not answer the printed question. All four parts are shipped re-solved for the printed
  map, labeled "הפתרון הרשמי עם תיקון", solutionSource solved, official:false. Conclusions that survive (dim Ker=2,
  Im = R^2, not injective) are the same.
- Q3 a: the official writes det A = (k+1)(k-1)^3; the correct value is -(k+1)(k-1)^3 (sign slip, same zero set). Corrected,
  logged in ASK_ADIR, no label.
- Q2 a: the official reduction first reorders the rows (R2,R3,R1) without naming the operation; written as "סידור מחדש".

Checks (sympy, tools/verify/21B-B/verify_21B-B.py): Q1 E,F,G,R and A=EFGR, the inverse polynomial and X, Q2 determinant,
the three cases, k=0 family, the complex roots, Q3 determinant and zero set, k=1 column space, eigenvalues/eigenvectors, P and
D, Q4 bases of W1, W2, sum, intersection and the counterexample, Q5 kernel, image and matrix for the printed map.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-B.json"


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
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": J(r"נתונה מערכת משוואות לינאריות כאשר $k\in\mathbb{R}$ הוא פרמטר ממשי.",
                     r"$$\begin{cases}2x+2y+(3-k^2)z=3-k\\ x+(k+1)y+kz=1-k\\ 3x+3y-k^2z=3-k\end{cases}$$")},
    "c3a": {"kind": "text", "title": "שאלה 3 - סעיפים א-ג",
            "text": r"נתונה מטריצה ריבועית $A=" + pm("1&1&1", "k&k^2&1", r"k^2&2k^2-1&1") + r"$."},
    "c3b": {"kind": "text", "title": "שאלה 3 - סעיף ד",
            "text": r"נתונה מטריצה $B=" + pm("-2&1&-1", "1&2&3", "1&-1&0") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של מטריצות",
           "text": J(r"נגדיר $W_1,W_2\subseteq\mathbb{M}_{2\times2}$, כאשר $\mathbb{M}_{2\times2}$ מרחב המטריצות מסדר $2\times2$ עם איברים ממשיים.",
                     r"$$W_1=\mathrm{Span}\left(" + pm("1&1", "0&0") + "," + pm("0&0", "2&3") + "," + pm("5&5", "6&9") + r"\right),\qquad W_2=\left\{" + pm("a&b", "c&d") + r"\in\mathbb{M}_{2\times2}\ \middle|\ a+b=c+d\right\}$$")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": J(r"תהי נתונה ההעתקה $T:\mathbb{M}_{2\times2}\to\mathbb{R}^2$ המוגדרת לפי",
                     r"$$T\left(" + pm("a&b", "c&d") + r"\right)=" + pm("a+b", "d+c") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
Aq = pm("0&1&7&8", "1&3&3&8", "-2&-5&1&-8")
Rq = pm("1&3&3&8", "0&1&7&8", "0&0&0&0")
chain1 = ("$$" + Aq + r"\xrightarrow{E_1A}" + pm("1&3&3&8", "0&1&7&8", "-2&-5&1&-8") + r"\xrightarrow{E_2E_1A}" + pm("1&3&3&8", "0&1&7&8", "0&1&7&8") + r"\xrightarrow{E_3E_2E_1A}" + Rq + "$$")
questions.append(Q(
    1, "א", "computation", "rank_inverse",
    r"הציגו את המטריצה $A=" + Aq + r"$ בצורה $A=EFGR$ כאשר $E$, $F$ ו-$G$ מטריצות אלמנטאריות ו-$R$ - מטריצה בצורה המדורגת.",
    J(chain1,
      r"$$E_3=" + pm("1&0&0", "0&1&0", "0&-1&1") + r",\ E_2=" + pm("1&0&0", "0&1&0", "2&0&1") + r",\ E_1=" + pm("0&1&0", "1&0&0", "0&0&1") + r",\qquad E_3E_2E_1A=" + Rq + "=R$$",
      r"$$A=E_1^{-1}E_2^{-1}E_3^{-1}R\ \Leftarrow\ E_1A=E_2^{-1}E_3^{-1}R\ \Leftarrow\ E_2E_1A=E_3^{-1}R\ \Leftarrow\ E_3E_2E_1A=R$$",
      r"והמטריצות $G=E_3^{-1}=" + pm("1&0&0", "0&1&0", "0&1&1") + r",\ F=E_2^{-1}=" + pm("1&0&0", "0&1&0", "-2&0&1") + r",\ E=E_1^{-1}=" + pm("0&1&0", "1&0&0", "0&0&1") + "$."),
    13))

questions.append(Q(
    1, "ב", "proof", "matrix_proofs",
    r"תהי $B\in\mathbb{M}_{n\times n}$ מטריצה המקיימת את $B^3-5B-4I=0$. הוכיחו ש-$B$ היא הפיכה ומצאו את הביטוי עבור $B^{-1}$ באמצעות מטריצה $B$.",
    J(r"אם $B^3-5B-4I=0$, אז $B^3-5B=4I\Leftarrow B\left(B^2-5I\right)=4I\Leftarrow B\left(\frac{1}{4}\left(B^2-5I\right)\right)=I$.",
      r"מכאן נובע ש-$B$ הפיכה ו-$B^{-1}=\left(\frac{1}{4}\left(B^2-5I\right)\right)$."),
    7))

questions.append(Q(
    1, "ג", "computation", "matrix_algebra",
    r"המטריצות $C,D$ הפיכות ומקיימות $CXD=C+D$. מצאו את המטריצה $X$.",
    J(r"לפי הנתון $C,D$ הן הפיכות ולכן קיימות $C^{-1},D^{-1}$. אם נכפול את השוויון $CXD=C+D$ משמאל ב-$C^{-1}$ אז נקבל $C^{-1}CXD=C^{-1}C+C^{-1}D$ או $IXD=I+C^{-1}D$ ואם נכפול עכשיו את השוויון האחרון ב-$D^{-1}$ מימין, אז נקבל",
      r"$$IXDD^{-1}=ID^{-1}+C^{-1}DD^{-1}\ \Leftarrow\ X=D^{-1}+C^{-1}$$"),
    5))

# ------------------------------------------------------------------ Q2
R0 = [["2", "2", "3-k^2", "3-k"], ["1", "k+1", "k", "1-k"], ["3", "3", "-k^2", "3-k"]]
R1 = [["1", "k+1", "k", "1-k"], ["3", "3", "-k^2", "3-k"], ["2", "2", "3-k^2", "3-k"]]
R2 = [["1", "k+1", "k", "1-k"], ["0", "-3k", "-k^2-3k", "2k"], ["0", "-2k", "3-2k-k^2", "k+1"]]
R3 = [["1", "k+1", "k", "1-k"], ["0", "-3k", "-k^2-3k", "2k"], ["0", "0", "9-k^2", "3-k"]]
R4 = [["1", "k+1", "k", "1-k"], ["0", "-3k", "-k^2-3k", "2k"], ["0", "0", "(3-k)(3+k)", "3-k"]]
ECH = J("$$" + aug(R0) + arrow(r"\text{reorder}") + aug(R1) + arrow(r"\substack{R_2-3R_1\to R_2\\R_3-2R_1\to R_3}") + aug(R2) + "$$",
        "$$" + arrow(r"3R_3-2R_2\to R_3") + aug(R3) + r"\ \Rightarrow\ " + aug(R4) + "$$")

questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"הביאו את המטריצה המורחבת לצורה מדורגת.",
    J(r"נבצע דירוג של המטריצה המורחבת (תחילה נסדר מחדש את השורות כך שהשורה בעלת המקדם $1$ תהיה ראשונה):", ECH),
    9, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"מצאו עבור אילו ערכים של פרמטר $k$ יש למערכת פתרון יחיד, אינסוף פתרונות או שאין פתרון כלל.",
    J(r"פתרון יחיד: $k\neq0,\ k\neq3,\ k\neq-3$.",
      r"אינסוף פתרונות: $k=0$ או $k=3$.",
      r"אין פתרון: $k=-3$."),
    8, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור $k=0$ פתרו את המערכת וכתבו את כל הפתרונות.",
    J(r"$$" + aug([["1", "1", "0", "1"], ["0", "0", "0", "0"], ["0", "0", "9", "3"]]) + arrow(r"\text{yields}") + aug([["1", "1", "0", "1"], ["0", "0", "0", "0"], ["0", "0", "3", "1"]]) + "$$",
      r"$$z=\frac{1}{3},\qquad y=t,\qquad x=1-t,\qquad t\in\mathbb{R}$$"),
    4, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"מצאו את כל הפתרונות המרוכבים של המשוואה $z^2+iz+0.25i=0$.",
    J(r"$$z=\frac{-i+\sqrt{i^2-i}}{2}=-0.5i+0.5\sqrt{-1-i}$$",
      r"$$-1-i=\sqrt2\left(\cos\frac{5\pi}{4}+i\sin\frac{5\pi}{4}\right)$$",
      r"$$W_{1,2}=\sqrt{-1-i}=\sqrt{\sqrt2\left(\cos\frac{5\pi}{4}+i\sin\frac{5\pi}{4}\right)}$$",
      r"$$W_1=\sqrt{\sqrt2}\left(\cos\frac{5\pi}{8}+i\sin\frac{5\pi}{8}\right)=-0.455+1.0986i$$",
      r"$$W_2=\sqrt{\sqrt2}\left(\cos\frac{9\pi}{8}+i\sin\frac{9\pi}{8}\right)=0.455-1.0986i$$",
      r"$$z_1=-0.2275+0.049i$$",
      r"$$z_2=0.2275-1.049i$$"),
    4))

# ------------------------------------------------------------------ Q3
questions.append(Q(
    3, "א", "computation", "determinants",
    r"מצאו את כל ערכי הפרמטר $k$ עבורם $A$ תהיה הפיכה.",
    J(r"$$\det A=\det" + pm("1&1&1", "k&k^2&1", r"k^2&2k^2-1&1") + r"=\det" + pm("1&1&1", "0&k^2-k&1-k", r"0&2k^2-1-k^2&1-k^2") + r"=-(k+1)(k-1)^3$$",
      r"לכן עבור הפרמטרים $k\neq\pm1$ המטריצה הפיכה."),
    4, contextId="c3a"))

questions.append(Q(
    3, "ב", "computation", "vector_spaces",
    r"עבור $k=1$ מצאו בסיס ואת המימד של מרחב העמודות של $A$, $\mathrm{col}(A)$.",
    J(r"עבור $k=1$, $A=" + pm("1&1&1", "1&1&1", "1&1&1") + r"\to\dots\to" + pm("1&1&1", "0&0&0", "0&0&0") + r"$.",
      r"$\mathrm{rank}(A)=1$ ודרגת המטריצה היא $\dim\mathrm{Col}A=1$, לכן בסיס של $\mathrm{Col}(A)$ הוא וקטור $\left\{" + pm("1", "1", "1") + r"\right\}$."),
    4, contextId="c3a"))

questions.append(Q(
    3, "ג", "computation", "linear_systems",
    r"עבור אילו ערכי $k$ למערכת $A\cdot\vec x=\vec b$ יש פתרון לכל וקטור $\vec b$.",
    J(r"עבור $k\neq\pm1$ קיים פתרון לכל וקטור $\vec b\in\mathbb{R}^3$, כי במקרה הזה $\mathrm{rank}((A|\vec b))=\mathrm{rank}(A)=3$."),
    4, contextId="c3a"))

questions.append(Q(
    3, "ד", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + pm("-2&1&-1", "1&2&3", "1&-1&0") + r"$. האם $B$ ניתנת ללכסון? במידה וכן, מצאו את $D$ מטריצה אלכסונית ו-$P$ מטריצה הפיכה כך שיתקיים $D=P^{-1}BP$.",
    J(r"נמצא את הפולינום האופייני של המטריצה:",
      r"$$f_A(\lambda)=|A-\lambda I|=\det" + pm(r"-2-\lambda&1&-1", r"1&2-\lambda&3", r"1&-1&-\lambda") + r"=\lambda(1-\lambda)(1+\lambda)=0$$",
      r"נקבל $\lambda_1=0,\ \lambda_2=1,\ \lambda_3=-1$.",
      r"מטריצה $A$ ניתנת ללכסון כי כל הערכים העצמיים ממשיים ושונים זה מזה.",
      r"(א) עבור $\lambda_1=0$ נקבל",
      r"$$" + pm("-2&1&-1", "1&2&3", "1&-1&0") + r"\to\dots\to" + pm("-2&1&-1", "0&1&1", "0&0&0") + "$$",
      r"למשוואה ההומוגנית יש נעלם חופשי אחד, לכן $\dim W_{\lambda_1}=1$ ווקטור עצמי המתאים ל-$\lambda_1=0$ הוא $v_1=" + pm("-1", "-1", "1") + "$.",
      r"(ב) עבור $\lambda_2=-1$ נקבל",
      r"$$A+\lambda I=" + pm("-1&1&-1", "1&3&3", "1&-1&1") + r"\to\dots\to" + pm("1&0&-3/2", "0&1&1/2", "0&0&0") + "$$",
      r"לכן $\dim W_{\lambda_2}=1$. ווקטור עצמי המתאים ל-$\lambda_2=-1$ הוא $v_2=" + pm("-3", "-1", "2") + "$.",
      r"(ג) עבור $\lambda_3=1$ נקבל",
      r"$$A-\lambda I=" + pm("-3&1&-1", "1&1&3", "1&-1&-1") + r"\to\dots\to" + pm("1&0&1", "0&1&2", "0&0&0") + "$$",
      r"לכן $\dim W_{\lambda_3}=1$. ווקטור עצמי המתאים ל-$\lambda_3=1$ הוא $v_3=" + pm("-1", "-2", "1") + "$.",
      r"סיכום: קיימת המטריצה האלכסונית $D=" + pm("0&0&0", "0&1&0", "0&0&-1") + r"$ וקיימת המטריצה ההפוכה $P=" + pm("-1&-1&-3", "-1&-2&-1", "1&1&2") + r"$ כך ש-$D=P^{-1}AP$."),
    13))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של תתי המרחבים $W_1$, $W_2$.",
    J(r"נדרג את המטריצה שעמודותיה הן הוקטורים (כל מטריצה נכתבת כווקטור $(a,b,c,d)$):",
      r"$$" + pm("1&0&5", "1&0&5", "0&2&6", "0&3&9") + r"\to" + pm("1&0&5", "0&0&0", "0&2&6", "0&3&9") + r"\to" + pm("1&0&5", "0&2&6", "0&3&9", "0&0&0") + r"\to" + pm("1&0&5", "0&1&3", "0&1&3", "0&0&0") + r"\to" + pm("1&0&5", "0&1&3", "0&0&0", "0&0&0") + "$$",
      r"$$\dim U_1=2$$", r"בסיס של $U_1$:", r"$$\left\{" + pm("1", "1", "0", "0") + "," + pm("0", "0", "2", "3") + r"\right\}$$",
      r"$$\dim W_1=2$$", r"בסיס של $W_1$:", r"$$\left\{" + pm("1&1", "0&0") + "," + pm("0&0", "2&3") + r"\right\}$$",
      r"התנאי $a+b-c-d=0$ נותן $" + pm("a", "b", "c", "d") + "=t_1" + pm("-1", "1", "0", "0") + "+t_2" + pm("1", "0", "1", "0") + "+t_3" + pm("1", "0", "0", "1") + r"$.",
      r"$$\dim U_2=3$$", r"בסיס של $U_2$:", r"$$\left\{" + pm("-1", "1", "0", "0") + "," + pm("1", "0", "1", "0") + "," + pm("1", "0", "0", "1") + r"\right\}$$",
      r"$$\dim W_2=3$$", r"בסיס של $W_2$:", r"$$\left\{" + pm("-1&1", "0&0") + "," + pm("1&0", "1&0") + "," + pm("1&0", "0&1") + r"\right\}$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"חשבו תת מרחב $W_1+W_2$, מצאו בסיס ומימד של $W_1+W_2$. האם $W_1+W_2=\mathbb{M}_{2\times2}$? נמקו.",
    J(r"נפתור את $t_1" + pm("-1", "1", "0", "0") + "+t_2" + pm("1", "0", "1", "0") + "+t_3" + pm("1", "0", "0", "1") + "=s_1" + pm("1", "1", "0", "0") + "+s_2" + pm("0", "0", "2", "3") + "$:",
      r"$$" + aug([["-1", "1", "1", "1", "0"], ["1", "0", "0", "1", "0"], ["0", "1", "0", "0", "2"], ["0", "0", "1", "0", "3"]], 3) + r"\to" + aug([["-1", "1", "1", "1", "0"], ["0", "1", "1", "2", "0"], ["0", "1", "0", "0", "2"], ["0", "0", "1", "0", "3"]], 3) + r"\to" + aug([["-1", "1", "1", "1", "0"], ["0", "1", "1", "2", "0"], ["0", "0", "-1", "-2", "2"], ["0", "0", "1", "0", "3"]], 3) + r"\to" + aug([["-1", "1", "1", "1", "0"], ["0", "1", "1", "2", "0"], ["0", "0", "-1", "-2", "2"], ["0", "0", "0", "-2", "5"]], 3) + "$$",
      r"$$\dim(U_1+U_2)=4$$", r"בסיס של $U_1+U_2$:", r"$$\left\{" + pm("-1", "0", "1", "0") + "," + pm("0", "-1", "0", "1") + "," + pm("1", "0", "1", "0") + "," + pm("1", "1", "0", "0") + r"\right\}$$",
      r"$$\dim(W_1+W_2)=4$$", r"בסיס של $W_1+W_2$:", r"$$\left\{" + pm("-1&1", "0&0") + "," + pm("1&0", "1&0") + "," + pm("1&0", "0&1") + "," + pm("1&1", "0&0") + r"\right\}$$",
      r"$\dim(W_1+W_2)=4=\dim(M_{2\times2})$, $W_1+W_2\subseteq M_{2\times2}$ ולכן $W_1+W_2=M_{2\times2}$."),
    7, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1\cap W_2$.",
    J(r"נמשיך את הדירוג של המערכת מהסעיף הקודם:",
      r"$$" + aug([["-1", "1", "1", "1", "0"], ["0", "1", "1", "2", "0"], ["0", "0", "-1", "-2", "2"], ["0", "0", "0", "1", r"-\frac{5}{2}"]], 3) + r"\to\dots\to" + aug([["1", "0", "0", "0", r"\frac{5}{2}"], ["0", "1", "0", "0", "2"], ["0", "0", "1", "0", "3"], ["0", "0", "0", "1", r"-\frac{5}{2}"]], 3) + "$$",
      r"$$" + pm("t_1", "t_2", "t_3", "-s_1", "-s_2") + "=t" + pm("5", "4", "6", "-5", "-2") + r"\ \to\ s_1" + pm("1", "1", "0", "0") + "+s_2" + pm("0", "0", "2", "3") + "=5t" + pm("1", "1", "0", "0") + "+2t" + pm("0", "0", "2", "3") + "=t" + pm("5", "5", "4", "6") + "$$",
      r"$$\dim(U_1\cap U_2)=1$$", r"בסיס של $U_1\cap U_2$:", r"$$\left\{" + pm("5", "5", "4", "6") + r"\right\}$$",
      r"$$\dim(W_1\cap W_2)=1$$", r"בסיס של $W_1\cap W_2$:", r"$$\left\{" + pm("5&5", "4&6") + r"\right\}$$"),
    7, contextId="c4"))

questions.append(Q(
    4, "ד", "proof", "vector_spaces",
    r"הוכיחו או הפריכו: $U=\left\{" + pm("a&b", "c&d") + r"\in M_{2\times2}\ \middle|\ (a+b)(c+d)=0\right\}$ תת מרחב של $M_{2\times2}$.",
    J(r"$U$ לא תת מרחב של $M_{2\times2}$.",
      r"**דוגמה נגדית:** $" + pm("1&-1", "1&1") + "," + pm("1&1", "1&-1") + r"\in U$, אבל $" + pm("1&-1", "1&1") + "+" + pm("1&1", "1&-1") + "=" + pm("2&0", "2&0") + r"\notin U$."),
    5))

# ------------------------------------------------------------------ Q5 (official solution solves another map: re-solved)
NOTE5 = (FIX + r"בפתרון הרשמי נפתרת ההעתקה $T\left(" + pm("a&b", "c&d") + r"\right)=" + pm("a+d", "b+c") + r"$ ולא ההעתקה שבשאלה, $T\left(" + pm("a&b", "c&d") + r"\right)=" + pm("a+b", "d+c") + r"$. הפתרון להלן נערך להעתקה המודפסת בשאלה.")

questions.append(Q(
    5, "א", "proof", "linear_maps",
    r"הוכיחו כי $T$ היא העתקה לינארית.",
    J(NOTE5,
      r"נבדוק תנאי לינאריות. תחילה חיבור:",
      r"$$T\left(" + pm("a_1&b_1", "c_1&d_1") + "+" + pm("a_2&b_2", "c_2&d_2") + r"\right)=T\left(" + pm("a_1+a_2&b_1+b_2", "c_1+c_2&d_1+d_2") + r"\right)=" + pm("(a_1+a_2)+(b_1+b_2)", "(d_1+d_2)+(c_1+c_2)") + "$$",
      r"$$=" + pm("a_1+b_1", "d_1+c_1") + "+" + pm("a_2+b_2", "d_2+c_2") + "=T\\left(" + pm("a_1&b_1", "c_1&d_1") + r"\right)+T\left(" + pm("a_2&b_2", "c_2&d_2") + r"\right)$$",
      r"ועכשיו כפל בסקלר $\alpha$:",
      r"$$T\left(\alpha" + pm("a&b", "c&d") + r"\right)=T\left(" + pm(r"\alpha a&\alpha b", r"\alpha c&\alpha d") + r"\right)=" + pm(r"\alpha a+\alpha b", r"\alpha d+\alpha c") + r"=\alpha" + pm("a+b", "d+c") + r"=\alpha T\left(" + pm("a&b", "c&d") + r"\right)$$",
      r"כיוון שתנאי לינאריות מתקיימים, $T$ היא העתקה לינארית."),
    6, contextId="c5", solutionSource="solved", official=False))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"מצאו את הבסיסים והמימדים של $\mathrm{Im}(T)$ ו-$\ker(T)$.",
    J(NOTE5,
      r"ראשית נחשב את הגרעין:",
      r"$$\ker(T)=\left\{" + pm("a&b", "c&d") + r"\ \middle|\ T\left[" + pm("a&b", "c&d") + r"\right]=(0,0)\right\}=\left\{" + pm("a&b", "c&d") + r"\ \middle|\ (a+b,d+c)=(0,0)\right\}$$",
      r"$$=\left\{" + pm("a&b", "c&d") + r"\ \middle|\ a+b=0,\ c+d=0\right\}=\left\{" + pm("a&-a", "c&-c") + r"\ \middle|\ a,c\in\mathbb{R}\right\}$$",
      r"$$=\left\{a" + pm("1&-1", "0&0") + "+c" + pm("0&0", "1&-1") + r"\ \middle|\ a,c\in\mathbb{R}\right\}=\mathrm{Sp}\left\{" + pm("1&-1", "0&0") + "," + pm("0&0", "1&-1") + r"\right\}$$",
      r"המטריצות בלתי תלויות כי הן לא פרופורציוניות, ולכן הקבוצה $\left\{" + pm("1&-1", "0&0") + "," + pm("0&0", "1&-1") + r"\right\}$ היא בסיס לגרעין, ומכאן ש-$\dim(\ker(T))=2$.",
      r"על פי משפט המימדים להעתקה לינארית נובע: $\dim(\mathrm{Im}(T))=\dim(M_2(\mathbb{R}))-\dim(\ker(T))=4-2=2$. מכיוון ש-$\mathrm{Im}(T)$ הוא תת-מרחב של $\mathbb{R}^2$ מאותו מימד, הוא זהה לו, ולכן $\mathrm{Im}(T)=\mathbb{R}^2$ ובסיס סטנדרטי של $\mathbb{R}^2$ הוא $\{(1,0),(0,1)\}$."),
    10, contextId="c5", solutionSource="solved", official=False))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"האם $T$ הפיכה? נמקו.",
    J(NOTE5,
      r"כיוון שהגרעין אינו וקטור האפס בלבד, $T$ אינה חד-חד-ערכית, ולכן בפרט $T$ אינה העתקה הפיכה."),
    4, contextId="c5", solutionSource="solved", official=False))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"יהי $B_1=\left\{" + pm("1&0", "0&0") + "," + pm("1&1", "0&0") + "," + pm("1&1", "1&0") + "," + pm("1&1", "1&1") + r"\right\}$ בסיס ל-$\mathbb{M}_{2\times2}$ ויהי $B=\left\{" + pm("1", "0") + "," + pm("1", "-1") + r"\right\}$ בסיס ל-$\mathbb{R}^2$. חשבו את המטריצה המייצגת $[T]_{B_2}^{B_1}$.",
    J(NOTE5,
      r"נסמן $B_2=B$. נחשב את המטריצה המייצגת:",
      r"$$T\left[" + pm("1&0", "0&0") + r"\right]=(1,0)=\boxed{1}(1,0)+\boxed{0}(1,-1)$$",
      r"$$T\left[" + pm("1&1", "0&0") + r"\right]=(2,0)=\boxed{2}(1,0)+\boxed{0}(1,-1)$$",
      r"$$T\left[" + pm("1&1", "1&0") + r"\right]=(2,1)=\boxed{3}(1,0)+\boxed{(-1)}(1,-1)$$",
      r"$$T\left[" + pm("1&1", "1&1") + r"\right]=(2,2)=\boxed{4}(1,0)+\boxed{(-2)}(1,-1)$$",
      r"ולכן:",
      r"$$[T]_{B_2}^{B_1}=" + pm("1&2&3&4", "0&0&-1&-2") + "$$"),
    5, contextId="c5", solutionSource="solved", official=False))

# ------------------------------------------------------------------ assemble
exam = {
    "examCode": "21B-B",
    "examLabel": "מבחן סוף סמסטר ב׳ תשפ״א, מועד ב׳ (25.07.2021)",
    "year": 2021,
    "examDate": "25.07.2021",
    "sourceFile": "21B-B exam with official solutions (PDF, 9pp)",
    "solutionFile": "21B-B exam with official solutions (PDF, 9pp)",
    "contexts": contexts,
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
