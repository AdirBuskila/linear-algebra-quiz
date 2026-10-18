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
      r"$$W_2=\sqrt{\sqrt2}\left(\cos\frac{13\pi}{8}+i\sin\frac{13\pi}{8}\right)=0.455-1.0986i$$",
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
    rubric=rub((r"דירוג $A$ לצורה מדורגת $R$ בשלוש פעולות שורה", 4),
               (r"רישום מטריצות הפעולות $E_1$ (החלפה), $E_2$ ($R_3+2R_1$), $E_3$ ($R_3-R_2$)", 3),
               (r"היפוך: $A=E_1^{-1}E_2^{-1}E_3^{-1}R$", 3),
               (r"זיהוי $E=E_1^{-1}$, $F=E_2^{-1}$, $G=E_3^{-1}$ וכתיבת $A=EFGR$", 3)),
    pitfalls=[r"לכתוב $A=E_3E_2E_1R$ בלי להפוך את מטריצות הפעולות (מתקבל $E_3E_2E_1A=R$).",
              r"להפוך פעולה בסימן שגוי: ההופכית של $R_3+2R_1$ היא $R_3-2R_1$."],
    steps=[
        num(r"מהי דרגת $A$ (מספר השורות הלא אפסיות ב-$R$)?", 2, r"$R$ היא $\begin{pmatrix}1&3&3&8\\0&1&7&8\\0&0&0&0\end{pmatrix}$."),
        cho(r"מדוע מטריצות $E,F,G$ הן ההפכיות של מטריצות פעולות השורה?", r"כי $E_3E_2E_1A=R$, ולכן $A=E_1^{-1}E_2^{-1}E_3^{-1}R$",
            [r"כי $A=E_3E_2E_1R$", r"כי פעולות השורה מבוצעות על $R$ ולא על $A$", r"כי $A=E_1E_2E_3R$ עבור פעולות השורה עצמן"],
            r"הדירוג נותן $E_3E_2E_1A=R$. הצבת מטריצות הפעולות עצמן בצורה $A=E_3E_2E_1R$ או $A=E_1E_2E_3R$ אינה נכונה (בדיקה ישירה), והפעולות מבוצעות על $A$."),
        num(r"מהו האיבר בשורה 3 עמודה 1 של $F=E_2^{-1}$ (ההופכית של $R_3+2R_1$)?", -2, r"ההופכית היא $R_3-2R_1$."),
        num(r"מהו האיבר בשורה 3 עמודה 2 של $G=E_3^{-1}$ (ההופכית של $R_3-R_2$)?", 1, r"ההופכית היא $R_3+R_2$."),
    ])

ENR[(1, "ב")] = dict(
    rubric=rub((r"העברת אגף: $B^3-5B=4I$ והוצאת $B$ כגורם: $B\left(B^2-5I\right)=4I$", 2),
               (r"חלוקה ב-4: $B\cdot\frac14\left(B^2-5I\right)=I$", 2),
               (r"מסקנה: $B$ הפיכה", 1),
               (r"הביטוי $B^{-1}=\frac14\left(B^2-5I\right)$", 2)),
    pitfalls=[r"לרשום $B^{-1}=B^2-5I$ בלי לחלק ב-4.",
              r"להוציא את $B$ כגורם מהביטוי $B^3-5B-4I$ בלי להעביר קודם את $4I$ לאגף השני."],
    steps=[
        odr("סדרו את שורות ההוכחה ש-$B$ הפיכה.",
            [r"$B^3-5B-4I=0$", r"$B^3-5B=4I$", r"$B\left(B^2-5I\right)=4I$", r"$B\cdot\frac{1}{4}\left(B^2-5I\right)=I$", r"$B^{-1}=\frac{1}{4}\left(B^2-5I\right)$"],
            r"כל שורה נובעת מקודמתה, והשורה האחרונה היא ההגדרה של מטריצה הפיכה."),
        fnd("בהוכחה הבאה שורה אחת שגויה. סמנו אותה.",
            [r"$B^3-5B-4I=0$", r"$B^3-5B=-4I$", r"$B\left(B^2-5I\right)=4I$", r"$B\cdot\frac{1}{4}\left(B^2-5I\right)=I$", r"$B^{-1}=\frac{1}{4}\left(B^2-5I\right)$"], 1,
            r"העברת $4I$ לאגף ימין נותנת $B^3-5B=4I$ ולא $-4I$."),
        cho(r"איזה ביטוי הוא $B^{-1}$?", r"$\frac{1}{4}\left(B^2-5I\right)$",
            [r"$B^2-5I$", r"$-\frac{1}{4}\left(B^2-5I\right)$", r"$\frac{1}{4}\left(B^2+5I\right)$"],
            r"בדיקה עם הסקלר $B=-1$ (פותר את $B^3-5B-4=0$): $B^{-1}=-1$, והביטוי הנכון נותן $\frac{1-5}{4}=-1$, ואילו האחרים נותנים $-4,\ 1,\ \frac32$."),
        num(r"בדיקה סקלרית: $B=-1$ מקיים $B^3-5B-4=0$. כמה שווה $\frac14\left(B^2-5\right)$?", -1, r"$\frac{1-5}{4}=-1=B^{-1}$.", 0),
    ])

ENR[(1, "ג")] = dict(
    rubric=rub((r"כפל משמאל ב-$C^{-1}$ וקבלת $XD=I+C^{-1}D$", 2),
               (r"כפל מימין ב-$D^{-1}$", 2),
               (r"התוצאה $X=D^{-1}+C^{-1}$", 1)),
    pitfalls=[r"לכפול את אחד האגפים משמאל ואת האחר מימין, ובכך לשבור את השוויון (מטריצות אינן מתחלפות).",
              r"לרשום $X=\frac{C+D}{CD}$ כאילו היו מספרים."],
    steps=[
        cho(r"כיצד מבודדים את $X$ מתוך $CXD=C+D$? מאיזה צד מכפילים ב-$C^{-1}$?",
            r"משמאל, כי $C$ עומדת משמאל ל-$X$, ושני האגפים מוכפלים באותו צד",
            [r"מימין, וכך $C$ מתבטלת", r"מכל צד, כי כפל מטריצות קומוטטיבי", r"לא מכפילים, אלא מחלקים ב-$C$"],
            r"$C^{-1}C=I$ רק כשהמטריצה ההפוכה צמודה ל-$C$, כלומר משמאל. כפל מימין לא מבטל את $C$, כפל מטריצות אינו קומוטטיבי, ואין חילוק במטריצות."),
        odr("סדרו את שלבי הפתרון.",
            [r"$CXD=C+D$", r"$XD=I+C^{-1}D$", r"$X=\left(I+C^{-1}D\right)D^{-1}$", r"$X=D^{-1}+C^{-1}$"],
            r"כפל משמאל ב-$C^{-1}$, כפל מימין ב-$D^{-1}$, ופתיחת סוגריים: $D^{-1}+C^{-1}DD^{-1}$."),
        num(r"בדיקה במקרה סקלרי: $C=3$, $D=6$ ו-$CXD=C+D$. מהו $X$?", 0.5, r"$X=\frac{9}{18}=\frac12=\frac16+\frac13=D^{-1}+C^{-1}$.", 0.0001),
    ])

ENR[(2, "א")] = dict(
    rubric=rub((r"סידור מחדש של השורות כך שהמקדם 1 ייפתח", 1),
               (r"הפעולות $R_2-3R_1$ ו-$R_3-2R_1$", 3),
               (r"הפעולה $3R_3-2R_2$ שמאפסת את עמודה 2 בשורה 3", 3),
               (r"הצורה המדורגת עם שורה שלישית $\left(0\ 0\ 9-k^2\mid3-k\right)$", 2)),
    pitfalls=[r"לחלק בפרמטר (למשל ב-$k$) מבלי לבדוק את המקרה $k=0$.",
              r"טעות סימן באגף הימני: $R_2-3R_1$ נותנת $3-k-3(1-k)=2k$."],
    steps=[
        cho(r"מדוע מסדרים מחדש את השורות לפני הדירוג?", r"כדי שאיבר מוביל קבוע (1) יופיע בשורה הראשונה ולא נחלק בביטוי עם פרמטר",
            [r"כי החלפת שורות משנה את קבוצת הפתרונות", r"כי אי אפשר לדרג בלי להחליף שורות", r"כי החלפת שורות מאפסת את שורת הסתירה"],
            r"החלפת שורות היא פעולת שורה חוקית ואינה משנה את קבוצת הפתרונות; הדירוג אפשרי גם בלעדיה, אבל עם איבר מוביל $2$ או $k+1$ בראש היינו נאלצים לחלק בביטוי עם פרמטר."),
        num(r"אחרי $R_2-3R_1$ מהו האיבר בשורה 2 עמודה 2 עבור $k=1$?", -3, r"האיבר הוא $-3k$."),
        num(r"אחרי $R_3-2R_1$ מהו האיבר בשורה 3 עמודה 3 עבור $k=3$?", -12, r"האיבר הוא $3-2k-k^2=3-6-9=-12$."),
        num(r"בצורה המדורגת הסופית מהו האיבר בשורה 3 עמודה 4 עבור $k=1$?", 2, r"האיבר הוא $3-k=2$."),
    ])

ENR[(2, "ב")] = dict(
    rubric=rub((r"פתרון יחיד כאשר שלושת האיברים המובילים שונים מאפס: $k\neq0,3,-3$", 3),
               (r"אינסוף פתרונות עבור $k=0$ ו-$k=3$ (שורת אפסים מלאה)", 3),
               (r"אין פתרון עבור $k=-3$ (שורה $(0\ 0\ 0\mid6)$)", 2)),
    pitfalls=[r"להסיק שאין פתרון בכל מקרה שבו מתאפס איבר מוביל: צריך לבדוק גם את אגף ימין.",
              r"לשכוח את אחד מהערכים $k=0$ או $k=3$ שנותנים אינסוף פתרונות."],
    steps=[
        num(r"מהי דרגת מטריצת המקדמים עבור $k=3$?", 2, r"שורה 3 מתאפסת לגמרי (כולל אגף ימין), ושורות 1,2 לא אפסיות."),
        num(r"מהי דרגת המטריצה המורחבת עבור $k=-3$?", 3, r"מופיעה שורה $(0\ 0\ 0\mid6)$."),
        num(r"מהי דרגת מטריצת המקדמים עבור $k=0$?", 2, r"שורה 2 מתאפסת ושורות 1,3 לא אפסיות."),
        cho(r"עבור איזה ערך של $k$ אין פתרון?", r"$k=-3$",
            [r"$k=3$", r"$k=0$", r"$k=3$ וגם $k=-3$"],
            r"ב-$k=3$ וב-$k=0$ הדרגות של $A$ ושל $[A|b]$ שוות (2) ולכן יש אינסוף פתרונות; רק ב-$k=-3$ הדרגות שונות."),
    ])

ENR[(2, "ג")] = dict(
    rubric=rub((r"הצבת $k=0$ בצורה המדורגת", 1),
               (r"זיהוי המשתנה החופשי $y=t$", 1),
               (r"$z=\frac13$", 1),
               (r"$x=1-t$ והצגה פרמטרית", 1)),
    pitfalls=[r"לשכוח לחלק ב-9 ולרשום $z=3$ במקום $z=\frac13$ מהמשוואה $9z=3$.",
              r"לשכוח שהמשתנה החופשי הוא $y$ ולא $z$."],
    steps=[
        num(r"כמה משתנים חופשיים יש כאשר $k=0$?", 1, r"שורה 2 מתאפסת ונשארות שתי משוואות בשלושה נעלמים."),
        num(r"מהו $z$ כאשר $k=0$?", 0.3333, r"$3z=1$ ולכן $z=\frac13$.", 0.001),
        num(r"בפתרון $x=1-t$, $y=t$: מהו $x$ עבור $t=3$?", -2, r"$x=1-3=-2$."),
    ])

ENR[(2, "ד")] = dict(
    rubric=rub((r"נוסחת השורשים והדיסקרימיננטה $-1-i$", 1),
               (r"הצגה קוטבית של $-1-i$", 1),
               (r"חישוב שני השורשים הריבועיים", 1),
               (r"שני הפתרונות $z_1,z_2$", 1)),
    pitfalls=[r"טעות בארגומנט של $-1-i$ (זהו רבע שלישי: $\frac{5\pi}{4}$ ולא $\frac{\pi}{4}$).",
              r"לשכוח את השורש השני (שורש ריבועי מרוכב כולל שני ערכים)."],
    steps=[
        num(r"מהו הארגומנט של $-1-i$ במעלות (בין 0 ל-360)?", 225, r"$-1-i=\sqrt2\left(\cos225^\circ+i\sin225^\circ\right)$."),
        num(r"מהו המודול של השורש הריבועי של $-1-i$?", 1.1892, r"המודול הוא $\sqrt{\sqrt2}=2^{1/4}\approx1.1892$.", 0.001),
        num(r"מהו החלק הממשי של $z_1=\frac{-i+W_1}{2}$ עבור $W_1\approx-0.455+1.0986i$?", -0.2275, r"$\frac{-0.455}{2}\approx-0.2275$.", 0.001),
    ])

ENR[(3, "א")] = dict(
    rubric=rub((r"חישוב הדטרמיננטה בעזרת דירוג", 2),
               (r"$\det A=-(k+1)(k-1)^3$ ואפסים $k=\pm1$", 1),
               (r"מסקנה: $A$ הפיכה אם ורק אם $k\neq\pm1$", 1)),
    pitfalls=[r"טעות סימן ב-$\det A$ (הסימן אינו משפיע על קבוצת האפסים).",
              r"לשכוח את אחד משני האפסים $k=1$ או $k=-1$."],
    steps=[
        num(r"מהו $\det A$ עבור $k=2$?", -3, r"$-(k+1)(k-1)^3=-3\cdot1=-3$."),
        num(r"מהו $\det A$ עבור $k=0$?", 1, r"$-(1)(-1)^3=1$."),
        cho(r"עבור אילו ערכי $k$ המטריצה $A$ אינה הפיכה?", r"$k=1$ וגם $k=-1$",
            [r"$k=1$ בלבד", r"$k=-1$ בלבד", r"$k=0$ וגם $k=1$"],
            r"הדטרמיננטה $-(k+1)(k-1)^3$ מתאפסת בדיוק ב-$k=\pm1$, ולכן לא מספיק ערך אחד; ב-$k=0$ הערך הוא 1."),
    ])

ENR[(3, "ב")] = dict(
    rubric=rub((r"הצבת $k=1$ וקבלת מטריצה עם שלוש שורות שוות", 1),
               (r"דירוג לדרגה 1", 2),
               (r"בסיס $\{(1,1,1)^T\}$ וממד 1", 1)),
    pitfalls=[r"לקחת את שורות המטריצה כבסיס של מרחב העמודות."],
    steps=[
        num(r"מהי דרגת $A$ עבור $k=1$?", 1, r"כל שלוש השורות שוות $(1\ 1\ 1)$."),
        cho(r"מהו בסיס של $\mathrm{Col}(A)$ עבור $k=1$?", r"$\{(1,1,1)^T\}$",
            [r"$\{(1,0,0)^T\}$", r"$\{(1,2,3)^T\}$", r"$\{(1,1,1)^T,\,(2,2,2)^T\}$"],
            r"כל עמודות $A$ הן $(1,1,1)^T$. הווקטורים $(1,0,0)^T$ ו-$(1,2,3)^T$ אינם כפולות שלו, ושני הווקטורים $(1,1,1)^T,(2,2,2)^T$ תלויים ולכן אינם בסיס."),
    ])

ENR[(3, "ג")] = dict(
    rubric=rub((r"קיום פתרון לכל $\vec b$ שקול לדרגה $3$", 2),
               (r"דרגת $A$ היא 3 בדיוק כאשר $\det A\neq0$", 1),
               (r"מסקנה: $k\neq\pm1$", 1)),
    pitfalls=[r"לבדוק עקביות עבור $\vec b$ מסוים במקום לבדוק שהדרגה מלאה."],
    steps=[
        cho(r"מהו התנאי לכך שלמערכת $A\vec x=\vec b$ יש פתרון לכל $\vec b\in\mathbb{R}^3$?", r"$\mathrm{rank}\,A=3$",
            [r"$\mathrm{rank}\,A<3$", r"$\det A=0$", r"$k=1$"],
            r"אם $\mathrm{rank}\,A<3$ (כלומר $\det A=0$, כמו ב-$k=1$) קיימים $\vec b$ שאינם בתמונה, ולכן אין פתרון לכל $\vec b$."),
        num(r"מהי דרגת $A$ עבור $k=2$?", 3, r"$\det A=-3\neq0$."),
    ])

ENR[(3, "ד")] = dict(
    rubric=rub((r"הפולינום האופייני והערכים העצמיים $0,1,-1$", 3),
               (r"בדיקה שהערכים העצמיים שונים זה מזה, ולכן $B$ ניתנת ללכסון", 1),
               (r"וקטור עצמי לכל אחד משלושת הערכים", 6),
               (r"בדיקת תקינות הווקטורים", 1),
               (r"כתיבת $D$ ו-$P$ בסדר מתאים", 2)),
    pitfalls=[r"לסדר את עמודות $P$ שלא בהתאמה לסדר האיברים ב-$D$.",
              r"לקחת את אחד הווקטורים העצמיים כווקטור האפס (וקטור עצמי חייב להיות שונה מאפס)."],
    steps=[
        num(r"מהו עקבה של $B$ (סכום האיברים באלכסון)?", 0, r"$-2+2+0=0=0+1+(-1)$, סכום הערכים העצמיים."),
        num(r"מהו $\det B$?", 0, r"$0$ הוא ערך עצמי, ולכן $\det B=0\cdot1\cdot(-1)=0$."),
        cho(r"מדוע $B$ ניתנת ללכסון?", r"כי יש לה שלושה ערכים עצמיים שונים זה מזה",
            [r"כי היא סימטרית", r"כי $\det B=0$", r"כי יש לה ערך עצמי $0$"],
            r"$B$ אינה סימטרית; $\det B=0$ וערך עצמי $0$ אינם מבטיחים ליכסון (למשל $\begin{pmatrix}0&1\\0&0\end{pmatrix}$). שלושה ערכים עצמיים שונים נותנים שלושה וקטורים עצמיים בלתי תלויים."),
        num(r"מהו הרכיב הראשון של $B\mathbf{v}_3$ עבור $\mathbf{v}_3=(-1,-2,1)^T$ ($\lambda=1$)?", -1, r"$-2\cdot(-1)+1\cdot(-2)-1\cdot1=-1=\lambda\cdot(-1)$."),
    ])

ENR[(4, "א")] = dict(
    rubric=rub((r"זיהוי שהמטריצה השלישית תלויה: היא $5$ כפול הראשונה ועוד $3$ כפול השנייה", 2),
               (r"בסיס של $W_1$ וממד 2", 1),
               (r"פרמטריזציה של $W_2$ מהמשוואה $a+b-c-d=0$", 2),
               (r"בסיס של $W_2$ וממד 3", 1)),
    pitfalls=[r"לכלול את המטריצה התלויה השלישית בבסיס של $W_1$.",
              r"לשכוח שבתנאי $a+b=c+d$ נשארים שלושה משתנים חופשיים."],
    steps=[
        num(r"המטריצה השלישית פורשת $\begin{pmatrix}5&5\\6&9\end{pmatrix}=5\begin{pmatrix}1&1\\0&0\end{pmatrix}+c\begin{pmatrix}0&0\\2&3\end{pmatrix}$. מהו $c$?", 3, r"$3\cdot(2,3)=(6,9)$."),
        num(r"מהו המימד של $W_1$?", 2, r"השלישית תלויה בשתי הראשונות, והשתיים הראשונות בלתי תלויות."),
        num(r"מהו המימד של $W_2$?", 3, r"משוואה אחת בארבעה נעלמים משאירה שלושה משתנים חופשיים."),
        cho(r"איזו מטריצה שייכת ל-$W_2$ (כלומר $a+b=c+d$)?", r"$\begin{pmatrix}2&1\\1&2\end{pmatrix}$",
            [r"$\begin{pmatrix}1&2\\3&4\end{pmatrix}$", r"$\begin{pmatrix}1&1\\1&2\end{pmatrix}$", r"$\begin{pmatrix}0&0\\1&0\end{pmatrix}$"],
            r"במטריצה הנכונה $a+b=3=c+d$. באחרות: $3\neq7$, $2\neq3$, $0\neq1$."),
    ])

ENR[(4, "ב")] = dict(
    rubric=rub((r"בניית מטריצה משלושת וקטורי $W_2$ ושני וקטורי $W_1$", 3),
               (r"דירוג וקבלת דרגה 4", 2),
               (r"$\dim(W_1+W_2)=4$ ובסיס", 2)),
    pitfalls=[r"להסיק $\dim(W_1+W_2)=\dim W_1+\dim W_2=5$ בלי לבדוק תלות (הסכום ממדו לכל היותר 4).",
              r"לכתוב את הסכום כקבוצה של 5 וקטורים בלי להוריד את התלוי."],
    steps=[
        num(r"מהו $\dim(W_1+W_2)$?", 4, r"דרגת המטריצה היא 4."),
        cho(r"מדוע $W_1+W_2=M_{2\times2}$?", r"כי $W_1+W_2$ תת-מרחב של $M_{2\times2}$ שממדו 4, כממד המרחב כולו",
            [r"כי $\dim W_1+\dim W_2=5>4$", r"כי $W_1\subseteq W_2$", r"כי $W_1\cap W_2=\{0\}$"],
            r"סכום המימדים אינו ממד הסכום; $\begin{pmatrix}1&1\\0&0\end{pmatrix}\in W_1$ אינה ב-$W_2$ ($2\neq0$) ולכן $W_1\not\subseteq W_2$; והחיתוך אינו טריוויאלי (ממדו 1)."),
    ])

ENR[(4, "ג")] = dict(
    rubric=rub((r"משפט המימדים: $\dim(W_1\cap W_2)=2+3-4=1$", 2),
               (r"פתרון המערכת ההומוגנית על מקדמי הצירוף", 2),
               (r"הצבה והצגת המטריצה $\begin{pmatrix}5&5\\4&6\end{pmatrix}$", 3)),
    pitfalls=[r"לחשב רק את המימד ולשכוח למצוא מטריצת בסיס.",
              r"לעבור על הסימנים בין הצד של $W_1$ לצד של $W_2$ במערכת ההומוגנית."],
    steps=[
        num(r"מהו $\dim(W_1\cap W_2)$?", 1, r"$2+3-4=1$."),
        num(r"עבור המטריצה $\begin{pmatrix}5&5\\4&6\end{pmatrix}$: מהו $c+d$ (וזה גם $a+b$, כלומר היא ב-$W_2$)?", 10, r"$4+6=10=5+5$."),
        num(r"המטריצה $\begin{pmatrix}5&5\\4&6\end{pmatrix}=5\begin{pmatrix}1&1\\0&0\end{pmatrix}+s\begin{pmatrix}0&0\\2&3\end{pmatrix}$. מהו $s$?", 2, r"$2\cdot(2,3)=(4,6)$."),
    ])

ENR[(4, "ד")] = dict(
    rubric=rub((r"בחירת שתי מטריצות ב-$U$ ובדיקה שהן ב-$U$", 2),
               (r"חישוב הסכום $\begin{pmatrix}2&0\\2&0\end{pmatrix}$", 1),
               (r"הראה שהסכום אינו ב-$U$ ולכן $U$ אינה סגורה לחיבור", 2)),
    pitfalls=[r"לבדוק רק שמטריצת האפס שייכת ל-$U$ ולהסיק שהיא תת-מרחב.",
              r"לבחור שתי מטריצות שהסכום שלהן מקיים את התנאי במקרה."],
    steps=[
        cho(r"איזו תכונה של תת-מרחב נכשלת ב-$U$?", r"סגירות לחיבור",
            [r"הכלת מטריצת האפס", r"סגירות לכפל בסקלר", r"כל התכונות נכשלות"],
            r"מטריצת האפס ב-$U$ ($0\cdot0=0$). כפל בסקלר $k$ נותן $(ka+kb)(kc+kd)=k^2(a+b)(c+d)=0$, ולכן מתקיים. רק החיבור נכשל."),
        num(r"עבור הסכום $\begin{pmatrix}2&0\\2&0\end{pmatrix}$ מהו $(a+b)(c+d)$?", 4, r"$2\cdot2=4\neq0$, ולכן הסכום אינו ב-$U$."),
        num(r"עבור $\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ מהו $(a+b)(c+d)$?", 0, r"$0\cdot2=0$, ולכן המטריצה ב-$U$."),
    ])

ENR[(5, "א")] = dict(
    rubric=rub((r"ציון שתי התכונות שיש לבדוק", 1),
               (r"חיבור: $T(M_1+M_2)$ מפורש", 2),
               (r"חיבור: השוואה ל-$T(M_1)+T(M_2)$", 1),
               (r"כפל בסקלר: $T(\alpha M)=\alpha T(M)$", 2)),
    pitfalls=[r"לבדוק רק חיבור ולשכוח כפל בסקלר.",
              r"לרשום $T(\alpha M)=T(M)$ בלי להוציא את $\alpha$."],
    steps=[
        cho(r"מה צריך לבדוק כדי להוכיח ש-$T$ לינארית?", r"$T(u+v)=T(u)+T(v)$ וגם $T(\alpha u)=\alpha T(u)$",
            [r"רק $T(0)=0$", r"$T(uv)=T(u)T(v)$", r"ש-$T$ חד-חד-ערכית"],
            r"התנאי $T(0)=0$ הכרחי אך אינו מספיק (למשל $T(M)=(a^2,0)$ מקיימת אותו ואינה לינארית); כפל מטריצות אינו מופיע בהגדרה; וחח״ע אינה חלק מההגדרה."),
        odr("סדרו את שלבי הוכחת החיבור.",
            [r"$T(M_1+M_2)=T\begin{pmatrix}a_1+a_2&b_1+b_2\\c_1+c_2&d_1+d_2\end{pmatrix}$",
             r"$=\begin{pmatrix}(a_1+a_2)+(b_1+b_2)\\(d_1+d_2)+(c_1+c_2)\end{pmatrix}$",
             r"$=\begin{pmatrix}a_1+b_1\\d_1+c_1\end{pmatrix}+\begin{pmatrix}a_2+b_2\\d_2+c_2\end{pmatrix}$",
             r"$=T(M_1)+T(M_2)$"],
            r"מציבים בהגדרת $T$, מקבצים לפי $M_1$ ו-$M_2$, וחוזרים להגדרת $T$."),
        fnd("בהוכחה הבאה שורה אחת שגויה. סמנו אותה.",
            [r"$T(M_1+M_2)=T\begin{pmatrix}a_1+a_2&b_1+b_2\\c_1+c_2&d_1+d_2\end{pmatrix}$",
             r"$=\begin{pmatrix}(a_1+a_2)+(b_1+b_2)\\(d_1+d_2)(c_1+c_2)\end{pmatrix}$",
             r"$=\begin{pmatrix}a_1+b_1\\d_1+c_1\end{pmatrix}+\begin{pmatrix}a_2+b_2\\d_2+c_2\end{pmatrix}$",
             r"$=T(M_1)+T(M_2)$"], 1,
            r"לפי ההגדרה הרכיב השני הוא סכום $(d_1+d_2)+(c_1+c_2)$ ולא מכפלה."),
    ])

ENR[(5, "ב")] = dict(
    rubric=rub((r"הצבה בהגדרת הגרעין: $a+b=0$ ו-$c+d=0$", 4),
                (r"בסיס $\left\{\begin{pmatrix}1&-1\\0&0\end{pmatrix},\begin{pmatrix}0&0\\1&-1\end{pmatrix}\right\}$ וממד 2", 2),
                (r"משפט המימדים: $\dim\mathrm{Im}(T)=4-2=2$", 2),
                (r"$\mathrm{Im}(T)=\mathbb{R}^2$ ובסיס סטנדרטי", 2)),
    pitfalls=[r"לפתור את ההעתקה $(a+d,b+c)$ מהפתרון המקורי במקום ההעתקה המודפסת $(a+b,d+c)$.",
              r"לשכוח שבסיס התמונה כולל שני וקטורים כי $\mathrm{Im}(T)=\mathbb{R}^2$."],
    steps=[
        cho(r"איזו מטריצה שייכת ל-$\ker T$?", r"$\begin{pmatrix}1&-1\\0&0\end{pmatrix}$",
            [r"$\begin{pmatrix}1&1\\0&0\end{pmatrix}$", r"$\begin{pmatrix}1&0\\0&-1\end{pmatrix}$", r"$\begin{pmatrix}0&0\\1&1\end{pmatrix}$"],
            r"$T\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a+b,\,d+c)$. למטריצה הנכונה התוצאה $(0,0)$; לאחרות $(2,0)$, $(1,-1)$, $(0,2)$."),
        num(r"מהו $\dim\ker T$?", 2, r"שני משתנים חופשיים: $a$ ו-$c$."),
        num(r"מהו $\dim\mathrm{Im}\,T$?", 2, r"משפט המימדים: $4-2=2$, ולכן $\mathrm{Im}\,T=\mathbb{R}^2$."),
    ])

ENR[(5, "ג")] = dict(
    rubric=rub((r"חישוב הגרעין מהסעיף הקודם: ממדו 2", 1),
               (r"הגרעין אינו טריוויאלי ולכן $T$ אינה חח״ע", 2),
               (r"מסקנה: $T$ אינה הפיכה", 1)),
    pitfalls=[r"להסיק שהיא אינה הפיכה מכך שאינה על; ההעתקה כאן כן על."],
    steps=[
        cho(r"האם $T$ הפיכה, ומדוע?", r"אינה הפיכה כי הגרעין שלה אינו טריוויאלי",
            [r"אינה הפיכה כי אינה על", r"הפיכה כי היא על", r"הפיכה כי $\dim\mathrm{Im}\,T=\dim\mathbb{R}^2$"],
            r"$T$ כן על ($\mathrm{Im}\,T=\mathbb{R}^2$), ולכן הנימוק 'אינה על' שגוי; אך על בלבד אינו מספיק להפיכות, ונדרשת גם חח״ע, שנכשלת כי $\dim\ker T=2$."),
        num(r"מהו $\dim\ker T$?", 2, r"הגרעין כולל את כל המטריצות $\begin{pmatrix}a&-a\\c&-c\end{pmatrix}$."),
    ])

ENR[(5, "ד")] = dict(
    rubric=rub((r"חישוב $T$ על ארבעת איברי $B_1$", 1),
               (r"הצגת כל תמונה כצירוף של $(1,0),(1,-1)$", 2),
               (r"סידור הקואורדינטות כעמודות: $\begin{pmatrix}1&2&3&4\\0&0&-1&-2\end{pmatrix}$", 2)),
    pitfalls=[r"לרשום את הקואורדינטות ביחס לבסיס הסטנדרטי ולא ביחס ל-$B_2$.",
              r"לסדר את הקואורדינטות כשורות במקום כעמודות."],
    steps=[
        cho(r"כיצד בנויה המטריצה $[T]_{B_2}^{B_1}$?", r"העמודה ה-$j$ היא וקטור הקואורדינטות של $T$ של האיבר ה-$j$ ב-$B_1$ ביחס ל-$B_2$",
            [r"השורה ה-$j$ היא וקטור הקואורדינטות של $T$ של האיבר ה-$j$ ב-$B_1$ ביחס ל-$B_2$", r"העמודה ה-$j$ היא הקואורדינטות של $T$ של האיבר ה-$j$ ב-$B_2$ ביחס ל-$B_1$", r"העמודה ה-$j$ היא $T$ של האיבר ה-$j$ ב-$B_1$ ביחס לבסיס הסטנדרטי"],
            r"המטריצה היא מגודל $2\times4$, כך ש-4 עמודות מתאימות ל-4 איברי $B_1$ וכל עמודה בת 2 קואורדינטות. האפשרות האחרונה ברשימה (קואורדינטות ביחס לבסיס הסטנדרטי) הייתה נותנת $\begin{pmatrix}1&2&2&2\\0&0&1&2\end{pmatrix}$."),
        num(r"$T\begin{pmatrix}1&1\\1&0\end{pmatrix}=(2,1)=\alpha(1,0)+\beta(1,-1)$. מהו $\alpha$?", 3, r"$\beta=-1$ ו-$\alpha+\beta=2$ ולכן $\alpha=3$."),
        num(r"באותה משוואה, מהו $\beta$?", -1, r"השני: $-\beta=1$."),
        num(r"$T\begin{pmatrix}1&1\\1&1\end{pmatrix}=(2,2)=\alpha(1,0)+\beta(1,-1)$. מהו $\beta$?", -2, r"$-\beta=2$ ולכן $\beta=-2$ ו-$\alpha=4$."),
    ])

for q in questions:
    if q.get("hold"):
        continue
    e = ENR.get((q["num"], q["part"]))
    assert e is not None, (q["num"], q["part"])
    if q.get("points") is not None:
        assert sum(r["points"] for r in e["rubric"]) == q["points"], (q["num"], q["part"])
    assert 2 <= len(e["steps"]) <= 5 and 1 <= len(e["pitfalls"]) <= 3 and 3 <= len(e["rubric"]) <= 5, (q["num"], q["part"])
    q.update(rubric=e["rubric"], rubricSource="ai-verified", pitfalls=e["pitfalls"], steps=e["steps"], stepsSource="ai-verified")


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
