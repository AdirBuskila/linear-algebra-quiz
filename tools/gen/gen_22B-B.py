# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-B.json -- linear algebra, semester B 2022, moed B (04.07.2022), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-B.py

Source: one PDF (10pp): the exam text followed question by question by the typed official solution.
Five questions of 25 points (best 4 count), 19 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (B); in the raw schema item 2 is part "gimel".
- Q5 has two numbered items: item 1 (T, parts a-c) and item 2 (F), which is part "dalet" here.
- Q2 solution, case k=0: the official says the contradiction is in "the second row"; with k=0 it is the first row
  (0 0 0 | 1). Intermediate slip, corrected, logged in ASK_ADIR, no label.
- Q4 c solution: the official labels one step "R1+8R3->R1" but the printed result is R1+8R4->R1 (R3-R4->R3 is the
  other operation). Label slip, corrected to R1+8R4->R1, logged in ASK_ADIR.
- Q5 b: the official answers "never onto, injective iff k != +-1"; kept.

Checks (sympy, tools/verify/22B-B/verify_22B-B.py): lambda1,2 of Q1a, the Q2 echelon form, the case analysis and the unique
solution, the k=1 family and particular+homogeneous split, the roots of Q2 d, A^-1 and its elementary product, charpoly, P and D,
bases and dims of W1, W2, W1+W2, W1 cap W2, membership of Q4 d, Im/Ker of T (k=-1, k=+-1, k=1), [F]_E^E.
No mismatch, no hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-B.json"


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
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": J(r"נתונה מערכת המשוואות כאשר $k$ הוא פרמטר ממשי:",
                     r"$$\begin{cases} kx+k^2y+kz=1\\ x+ky-kz=1\\ x+y+z=1\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
           "text": r"נתונה המטריצה $A=" + pm("1&4&0", "0&1&2", "3&12&3") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של פולינומים",
           "text": J(r"יהיו $W_1$ ו-$W_2$ שני תתי מרחבים של מרחב הפולינומים ממעלה 3 ומטה $\mathbb{R}_{\leq3}[x]$ המוגדרים ע״י",
                     r"$W_1=\{p(x)\in\mathbb{R}_{\leq3}[x]:\ p(-1)=p(1)\}$",
                     r"$W_2=\{p(x)\in\mathbb{R}_{\leq3}[x]:\ p(2)=0\}$")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": J(r"נתונה העתקה לינארית $T:\mathbb{R}_2[x]\to\mathbb{R}^4$ המוגדרת על ידי:",
                     r"$$T(1)=" + pm("1", "0", "0", "0") + r",\quad T(x)=" + pm("1", "1", "2", "-1") + r",\quad T\left(x^2\right)=" + pm("1", "2", "k^2+3", "-2") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "eigen_diagonalization",
    r"הוכיחו שאם $a,b,c,d$ הם מספרים ממשיים כאלה ש-$a+b=c+d$, אז מטריצה $A=" + pm("a&b", "c&d") + r"$ בעלת הערכים העצמיים השלמים $\lambda_1=a+b$ ו-$\lambda_2=a-c$.",
    J(r"ראשית, נבנה את הפולינום האופייני של $A$, כלומר",
      r"$$\det(A-\lambda I)=\begin{vmatrix}a-\lambda&b\\c&d-\lambda\end{vmatrix}=\lambda^2-(a+d)\lambda+ad-bc$$",
      r"מכאן נובע כי הערכים העצמיים של $A$ נקבעים לפי",
      r"$$\lambda_{1,2}=\frac{(a+d)\pm\sqrt{(a+d)^2-4ad+4bc}}{2}=\frac{(a+d)\pm\sqrt{(a-d)^2+4bc}}{2}$$",
      r"מהנתון $a+b=c+d$ נובע כי $a-d=c-b$ ולכן",
      r"$$\lambda_{1,2}=\frac{(a+d)\pm\sqrt{(c-b)^2+4bc}}{2}=\frac{(a+d)\pm\sqrt{(c+b)^2}}{2}=\frac{(a+d)\pm(c+b)}{2}$$",
      r"מכאן מקבלים סופית ש-",
      r"$$\lambda_1=\frac{(a+d)+(c+b)}{2}=\frac{(a+b)+(c+d)}{2}=\frac{2(a+b)}{2}=a+b$$",
      r"$$\lambda_2=\frac{(a+d)-(c+b)}{2}=\frac{(a-c)+(d-b)}{2}=\frac{2(a-c)}{2}=a-c$$"),
    8))

questions.append(Q(
    1, "ב", "proof", "eigen_diagonalization",
    r"הוכיחו שאם $\lambda$ הוא ערך עצמי של מטריצה הפיכה $B$ ו-$\vec{\mathbf{u}}$ הוא וקטור עצמי שמתאים ל-$\lambda$, אז $1/\lambda$ יהיה ערך עצמי של $B^{-1}$ עם אותו הווקטור העצמי $\vec{\mathbf{u}}$.",
    J(r"נתון ש-$B\vec{\mathbf{u}}=\lambda\vec{\mathbf{u}}$. מכיוון ש-$B$ הפיכה, אז $B^{-1}$ קיימת ואם נכפול את $B\vec{\mathbf{u}}=\lambda\vec{\mathbf{u}}$ משמאל ב-$B^{-1}$, אז נקבל",
      r"$$B^{-1}B\vec{\mathbf{u}}=B^{-1}\left(\lambda\vec{\mathbf{u}}\right)\ \Leftarrow\ \vec{\mathbf{u}}=\lambda\left(B^{-1}\vec{\mathbf{u}}\right)$$",
      r"או $B^{-1}\vec{\mathbf{u}}=\frac{1}{\lambda}\vec{\mathbf{u}}$ וזה מוכיח את הנדרש."),
    5))

questions.append(Q(
    1, "ג", "proof", "eigen_diagonalization",
    r"הוכיחו שאם $\lambda$ הוא ערך עצמי של מטריצה הפיכה $C$ ו-$\vec{\mathbf{u}}$ הוא וקטור עצמי שמתאים ל-$\lambda$ ו-$s$ הוא סקלר, אז $\lambda-s$ יהיה ערך עצמי של $C-sI$ עם אותו הווקטור העצמי $\vec{\mathbf{u}}$.",
    J(r"נתון ש-$C\vec{\mathbf{u}}=\lambda\vec{\mathbf{u}}$. נתבונן ב-",
      r"$$(C-sI)\vec{\mathbf{u}}=C\vec{\mathbf{u}}-sI\vec{\mathbf{u}}=\lambda\vec{\mathbf{u}}-s\vec{\mathbf{u}}=(\lambda-s)\vec{\mathbf{u}}$$",
      r"מכאן מייד נובע כי $\lambda-s$ מהווה ערך עצמי של $C-sI$ עם אותו הווקטור העצמי $\vec{\mathbf{u}}$."),
    5))

questions.append(Q(
    1, "ד", "proof", "eigen_diagonalization",
    r"נניח ש-$D,E$ ו-$P$ הן מטריצות $n\times n$ וידוע ש-$P$ הפיכה וגם $PD=EP$. הוכח שכל ערך עצמי של $D$ הוא גם ערך עצמי של $E$.",
    J(r"נניח ש-$\lambda$ הוא ערך עצמי של מטריצה $D$ ו-$\vec{\mathbf{u}}$ הוא ווקטור עצמי שמתאים לו, כלומר $D\vec{\mathbf{u}}=\lambda\vec{\mathbf{u}}$. אם נכפול את זה משמאל במטריצה $P$, אז נקבל",
      r"$$PD\vec{\mathbf{u}}=P\lambda\vec{\mathbf{u}}=\lambda P\vec{\mathbf{u}}$$",
      r"מכיוון ש-$PD=EP$, אז $EP\vec{\mathbf{u}}=\lambda P\vec{\mathbf{u}}$. אם נסמן עכשיו $P\vec{\mathbf{u}}=\mathbf{x}$, אז נקבל $E\mathbf{x}=\lambda\mathbf{x}$ וזה מוכיח שהמספר $\lambda$ הוא גם ערך עצמי של מטריצה $E$."),
    7))

# ------------------------------------------------------------------ Q2
R0 = [["k", "k^2", "k", "1"], ["1", "k", "-k", "1"], ["1", "1", "1", "1"]]
R1 = [["1", "k", "1", r"\frac{1}{k}"], ["1", "k", "-k", "1"], ["1", "1", "1", "1"]]
R2 = [["1", "k", "1", r"\frac{1}{k}"], ["0", "0", "1+k", r"\frac{1}{k}-1"], ["0", "k-1", "0", r"\frac{1}{k}-1"]]
R3 = [["1", "k", "1", r"\frac{1}{k}"], ["0", "0", "1", r"\frac{1-k}{k(1+k)}"], ["0", "k(k-1)", "0", "1-k"]]
R4 = [["1", "k", "0", r"\frac{2}{k+1}"], ["0", "k(k-1)", "0", "1-k"], ["0", "0", "1", r"\frac{1-k}{k(1+k)}"]]
ECH = J(r"נדרג את מטריצת המקדמים של המערכת ונמצא:",
        "$$" + aug(R0) + arrow(r"\frac{1}{k}R_1\to R_1\ (k\neq0)") + aug(R1) + arrow(r"\substack{R_1-R_2\to R_2\\R_1-R_3\to R_3}") + aug(R2) + "$$",
        "$$" + arrow(r"\substack{\frac{1}{1+k}R_2\to R_2\\kR_3\to R_3\\k\neq-1}") + aug(R3) + arrow(r"\substack{R_1-R_2\to R_1\\R_2\leftrightarrow R_3}") + aug(R4) + "$$",
        r"בעקבות הדירוג מצאנו שלושה ערכים חשודים, $k=-1,0,1$. נבדוק את הפתרון עבור כל ערך חשוד.")

questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ יש פתרון יחיד למערכת? מצאו את הפתרון.",
    J(ECH,
      r"עבור $k\neq0,\pm1$ ישנו פתרון יחיד למערכת, והוא מתקבל מהצבה:",
      r"$$x=\frac{k+3}{k+1},\qquad y=-\frac{1}{k},\qquad z=\frac{1-k}{k(k+1)}$$"),
    6, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ אין פתרון למערכת?",
    J(r"במקרה ש-$k=0$ נציב $k=0$ במטריצה המקורית ונקבל סתירה בשורה הראשונה, $0\neq1$: משמע אין פתרון.",
      r"במקרה ש-$k=-1$ נציב ונקבל:",
      r"$$" + aug([["-1", "1", "-1", "1"], ["1", "-1", "1", "1"], ["1", "1", "1", "1"]]) + "$$",
      r"סכום שתי השורות הראשונות והאמצעות ייתן לנו סתירה, $2\neq0$, משמע שגם עבור ערך זה אין פתרון.",
      r"לכן אין פתרון עבור $k=0$ ו-$k=-1$."),
    6, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ יש אינסוף פתרונות למערכת? מצאו הצגה פרמטרית של הפתרונות. הראו שפתרון זה הוא סכום של הפתרון של מערכת המשוואות ההומוגנית יחד עם פתרון פרטי של מערכת המשוואות הלא-הומוגנית המקורית.",
    J(r"עבור $k=1$ נקבל אינסוף פתרונות מהצורה:",
      r"$$" + aug([["1", "1", "1", "1"], ["1", "1", "-1", "1"], ["1", "1", "1", "1"]]) + r"\Rightarrow\begin{cases}x+y+z=1\\x+y-z=1\end{cases}\Rightarrow x+y=1,\ z=0$$",
      r"לפיכך הפתרון הכללי הוא מהצורה:",
      r"$$(x,y,z)=(1-y,\,y,\,0)=(1,0,0)+y(-1,1,0)$$",
      r"כאשר $(1,0,0)$ הוא הפתרון הפרטי של המערכת המקורית, ו-$(x=-t,\ y=t,\ z=0),\ t\in\mathbb{R}$ הוא פתרון כללי של המערכת ההומוגנית:",
      r"$$\begin{cases}kx+k^2y+kz=0\\x+ky-kz=0\\x+y+z=0\end{cases}$$"),
    7, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"נתונים שני וקטורים: $\vec{u}=(z,-1,2)$, $\vec{v}=(z,z,1)$. עבור איזה ערך של הפרמטר המרוכב $z$ הם מאונכים זה לזה? נא לכתוב את הפתרונות בצורה $x+iy$.",
    J(r"שני וקטורים מאונכים זה לזה אם המכפלה הסקלרית שלהם שווה לאפס. במקרה שלנו $\vec{u}=(z,-1,2)$, $\vec{v}=(z,z,1)$, ולכן נדרוש את השוויון:",
      r"$$\vec{u}\cdot\vec{v}=(z,-1,2)\cdot(z,z,1)=z^2-z+2=0$$",
      r"שורשי המשוואה הזו הם:",
      r"$$z_1=\frac{1}{2}+i\frac{\sqrt7}{2},\qquad z_2=\frac{1}{2}-i\frac{\sqrt7}{2}$$"),
    6, contextId="c2"))

# ------------------------------------------------------------------ Q3
Ai_aug = [
    (aug([["1", "4", "0", "1", "0", "0"], ["0", "1", "2", "0", "1", "0"], ["3", "12", "3", "0", "0", "1"]]), r"R_3\to R_3-3R_1"),
    (aug([["1", "4", "0", "1", "0", "0"], ["0", "1", "2", "0", "1", "0"], ["0", "0", "3", "-3", "0", "1"]]), r"R_3\to\frac{1}{3}R_3"),
    (aug([["1", "4", "0", "1", "0", "0"], ["0", "1", "2", "0", "1", "0"], ["0", "0", "1", "-1", "0", r"\frac{1}{3}"]]), r"R_2\to R_2-2R_3"),
    (aug([["1", "4", "0", "1", "0", "0"], ["0", "1", "0", "2", "1", r"-\frac{2}{3}"], ["0", "0", "1", "-1", "0", r"\frac{1}{3}"]]), r"R_1\to R_1-4R_2"),
    (aug([["1", "0", "0", "-7", "-4", r"\frac{8}{3}"], ["0", "1", "0", "2", "1", r"-\frac{2}{3}"], ["0", "0", "1", "-1", "0", r"\frac{1}{3}"]]), None),
]
inv_chain = "$$" + "".join(m + (arrow(op) if op else "") for m, op in Ai_aug) + "$$"
AINV = pm("-7&-4&\\frac{8}{3}", "2&1&-\\frac{2}{3}", "-1&0&\\frac{1}{3}")

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
      r"$$A^{-1}=" + pm("1&-4&0", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&-2", "0&0&1") + pm("1&0&0", "0&1&0", r"0&0&\frac{1}{3}") + pm("1&0&0", "0&1&0", "-3&0&1") + "$$"),
    7, contextId="c3"))

B3 = pm("5&0&1", "0&4&0", "1&0&5")
questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + B3 + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $D=P^{-1}BP$.",
    J(r"תחילה נמצא את כל הערכים העצמיים והווקטורים העצמיים של $B$. נחשב את הדטרמיננטה הבאה לפי שורה שנייה:",
      r"$$|\lambda I-B|=\begin{vmatrix}\lambda-5&0&-1\\0&\lambda-4&0\\-1&0&\lambda-5\end{vmatrix}=(\lambda-4)\begin{vmatrix}\lambda-5&-1\\-1&\lambda-5\end{vmatrix}=(\lambda-4)\left[(\lambda-5)^2-1\right]=(\lambda-4)(\lambda^2-10\lambda+24)=(\lambda-4)(\lambda-4)(\lambda-6)$$",
      r"קיבלנו שהערכים העצמיים הם: $\lambda_1=\lambda_2=4$ ו-$\lambda_3=6$. כעת נמצא את הווקטורים העצמיים.",
      r"**עבור ע״ע** $\lambda_1=\lambda_2=4$:",
      r"$$" + pm("-1&0&-1", "0&0&0", "-1&0&-1") + r"\to\cdots\to" + pm("1&0&1", "0&0&0", "0&0&0") + "$$",
      r"נסמן $y=t,\ z=s$ ונקבל: $x=-s$. הווקטורים העצמיים המתקבלים הם: $(-1,0,1)^T,\ (0,1,0)^T$.",
      r"**עבור ע״ע** $\lambda_3=6$:",
      r"$$" + pm("1&0&-1", "0&2&0", "-1&0&1") + r"\to\cdots\to" + pm("1&0&-1", "0&1&0", "0&0&0") + "$$",
      r"נסמן $z=t$ ונקבל: $x=t,\ y=0$. הווקטור העצמי המתקבל הוא: $(1,0,1)^T$.",
      r"המטריצה ניתנת לליכסון (שלושה וקטורים עצמיים בלתי תלויים). כעת נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$:",
      r"$$D=" + pm("4&0&0", "0&4&0", "0&0&6") + r",\qquad P=" + pm("-1&0&1", "0&1&0", "1&0&1") + "$$"),
    12))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1$ ו-$W_2$.",
    J(r"יהי $p(x)=a_3x^3+a_2x^2+a_1x+a_0\in\mathbb{R}_{\leq3}[x]$. אזי",
      r"$$p\in W_1\ \Leftrightarrow\ p(-1)=p(1)\ \Leftrightarrow\ -a_3+a_2-a_1+a_0=a_3+a_2+a_1+a_0\ \Leftrightarrow\ a_1+a_3=0$$",
      r"המשתנים החופשיים במערכת המשוואות הזו הם $a_0,a_2,a_3$. נבצע פרמטריזציה $a_0=t_1,\ a_2=t_2,\ a_3=t_3$ ונקבל ש-$a_1=-a_3=-t_3$. מכאן נקבל ש-",
      r"$$p\in W_1\ \Leftrightarrow\ p(x)=t_1\cdot1+t_2x^2+t_3\left(x^3-x\right),\qquad t_1,t_2,t_3\in\mathbb{R}$$",
      r"וקבוצת הפולינומים $B_{W_1}=\left\{1,\ x^2,\ \left(x^3-x\right)\right\}$ מהווה בסיס של $W_1$. מכאן גם $\dim W_1=3$.",
      r"באופן דומה,",
      r"$$p\in W_2\ \Leftrightarrow\ p(2)=0\ \Leftrightarrow\ 8a_3+4a_2+2a_1+a_0=0$$",
      r"ניקח את המשתנים החופשיים במערכת משוואות זו להיות $a_0,a_1,a_2$. נבצע פרמטריזציה $a_0=t_1,\ a_1=t_2,\ a_2=t_3$ ונקבל ש-$a_3=-\frac{1}{8}t_1-\frac{1}{4}t_2-\frac{1}{2}t_3$. מכאן נקבל ש-",
      r"$$p\in W_2\ \Leftrightarrow\ p(x)=\left(-\frac{1}{8}t_1-\frac{1}{4}t_2-\frac{1}{2}t_3\right)x^3+t_3x^2+t_2x+t_1\cdot1=$$",
      r"$$=t_1\left(-\frac{1}{8}x^3+1\right)+t_2\left(-\frac{1}{4}x^3+x\right)+t_3\left(-\frac{1}{2}x^3+x^2\right)=\tilde t_1\left(-x^3+8\right)+\tilde t_2\left(-x^3+4x\right)+\tilde t_3\left(-x^3+2x^2\right)$$",
      r"וקבוצת הפולינומים $B_{W_2}=\left\{\left(-x^3+8\right),\left(-x^3+4x\right),\left(-x^3+2x^2\right)\right\}$ מהווה בסיס של $W_2$. מכאן גם $\dim W_2=3$."),
    7, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1+W_2$.",
    J(r"(ב)+(ג): לכל אחד מוקטורי הבסיס ב-$B_{W_1}$ ו-$B_{W_2}$ נשייך את וקטור הקואורדינטות המתאים ביחס לבסיס הסטנדרטי $E=\{1,x,x^2,x^3\}$ של $\mathbb{R}_{\leq3}[x]$ (למעשה אנו עושים שימוש באיזומורפיזם בין $\mathbb{R}^4$ ו-$\mathbb{R}_{\leq3}[x]$).",
      r"$$B_{W_1}:\ [1]_E=" + pm("1", "0", "0", "0") + r",\ [x^2]_E=" + pm("0", "0", "1", "0") + r",\ [x^3-x]_E=" + pm("0", "-1", "0", "1") + "$$",
      r"$$B_{W_2}:\ [-x^3+8]_E=" + pm("8", "0", "0", "-1") + r",\ [-x^3+4x]_E=" + pm("0", "4", "0", "-1") + r",\ [-x^3+2x^2]_E=" + pm("0", "0", "2", "-1") + "$$",
      r"כדי למצוא בסיס עבור $W_1+W_2$ נבנה מטריצה שעמודותיה הן וקטורי הקואורדינטות הנ״ל ונדרג",
      "$$" + aug([["1", "0", "0", "8", "0", "0"], ["0", "0", "-1", "0", "4", "0"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "1", "-1", "-1", "-1"]])
      + arrow(r"R_2\leftrightarrow R_3") + aug([["1", "0", "0", "8", "0", "0"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "-1", "0", "4", "0"], ["0", "0", "1", "-1", "-1", "-1"]]) + "$$",
      "$$" + arrow(r"R_3\leftrightarrow R_4") + aug([["1", "0", "0", "8", "0", "0"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "1", "-1", "-1", "-1"], ["0", "0", "-1", "0", "4", "0"]])
      + arrow(r"R_4+R_3\to R_4") + aug([["1", "0", "0", "8", "0", "0"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "1", "-1", "-1", "-1"], ["0", "0", "0", "-1", "3", "-1"]]) + "$$",
      r"אנו רואים שבשתי העמודות האחרונות אין איבר מוביל. מכאן אנו מקבלים שקבוצת הפולינומים $B_{W_1+W_2}=\left\{1,x^2,\left(x^3-x\right),\left(-x^3+8\right)\right\}$ הוא בסיס של $W_1+W_2$ ו-$\dim(W_1+W_2)=4$."),
    7, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצאו בסיס ומימד של $W_1\cap W_2$.",
    J(r"כדי למצוא בסיס עבור $W_1\cap W_2$ עלינו לפתור את מערכת המשוואות המתקבלת מדירוג המטריצה הנ״ל. נמשיך את הדירוג ונקבל",
      "$$" + aug([["1", "0", "0", "8", "0", "0"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "1", "-1", "-1", "-1"], ["0", "0", "0", "-1", "3", "-1"]])
      + arrow(r"\substack{R_1+8R_4\to R_1\\R_3-R_4\to R_3}") + aug([["1", "0", "0", "0", "24", "-8"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "1", "0", "-4", "0"], ["0", "0", "0", "-1", "3", "-1"]])
      + r"\to" + aug([["1", "0", "0", "0", "24", "-8"], ["0", "1", "0", "0", "0", "2"], ["0", "0", "1", "0", "-4", "0"], ["0", "0", "0", "1", "-3", "1"]]) + "$$",
      r"אם נסמן את המקדמים של $1,x^2,\left(x^3-x\right)$ ב-$\alpha_1,\alpha_2,\alpha_3$ בהתאמה ואת המקדמים של $\left(-x^3+8\right),\left(-x^3+4x\right),\left(-x^3+2x^2\right)$ ב-$\beta_1,\beta_2,\beta_3$, בהתאמה, נקבל מהשורה האחרונה של המטריצה המדורגת הנ״ל את המשוואה $\beta_1-3\beta_2+\beta_3=0$. נבצע פרמטריזציה $\beta_3=t_2,\ \beta_2=t_1$ ונקבל $\beta_1=3t_1-t_2$. מכאן,",
      r"$$p\in W_1\cap W_2\ \Leftrightarrow\ p=(3t_1-t_2)\left(-x^3+8\right)+t_1\left(-x^3+4x\right)+t_2\left(-x^3+2x^2\right)=$$",
      r"$$=t_1\left(-4x^3+4x+24\right)+t_2\left(2x^2-8\right)=4t_1\left(-x^3+x+6\right)+2t_2\left(x^2-4\right)$$",
      r"מכאן ש-$B_{W_1\cap W_2}=\left\{\left(-x^3+x+6\right),\left(x^2-4\right)\right\}$, $\dim(W_1\cap W_2)=2$."),
    7, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"האם הפולינום $p(x)=-x^3+2x^2+x-2$ שייך אל $W_1\cap W_2$?",
    J(r"כיוון ש-",
      r"$$-x^3+2x^2+x-2=\left(-x^3+x+6\right)+2\left(x^2-4\right)$$",
      r"מתקיים $-x^3+2x^2+x-2\in W_1\cap W_2$."),
    4, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"לאילו ערכי הפרמטר $k$ מתקיים $" + pm("1", "1", "2", "k") + r"\in\mathrm{Im}\,T$?",
    J(r"המטריצה המייצגת של ההעתקה היא",
      r"$$A=" + pm("1&1&1", "0&1&2", "0&2&k^2+3", "0&-1&-2") + "$$",
      "$$" + aug([["1", "1", "1", "1"], ["0", "1", "2", "1"], ["0", "2", "k^2+3", "2"], ["0", "-1", "-2", "k"]], 3)
      + arrow(r"\substack{R_3\leftarrow R_3-2R_2\\R_4\leftarrow R_4+R_2}") + aug([["1", "1", "1", "1"], ["0", "1", "2", "1"], ["0", "0", "k^2-1", "0"], ["0", "0", "0", "k+1"]], 3) + "$$",
      r"כלומר יהיה פתרון למערכת רק אם $k=-1$. אחרת תהיה שורת סתירה למערכת. רק עבור $k=-1$ מתקיים $" + pm("1", "1", "2", "k") + r"\in\mathrm{Im}\,T$."),
    6, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"לאילו ערכי הפרמטר $k$ ההעתקה הלינארית $T$ היא על? לאילו ערכי הפרמטר $k$ ההעתקה הלינארית $T$ היא חח״ע?",
    J(r"לאחר דירוג המטריצה המייצגת היא",
      r"$$" + pm("1&1&1", "0&1&2", "0&0&k^2-1", "0&0&0") + "$$",
      r"ההעתקה בכל מקרה לא על כי עמודות לא פורשות את $\mathbb{R}^4$ (או בגלל שיש רק 3 עמודות, או בגלל שיש שורת אפסים בצורה המדורגת). כדי להיות חח״ע צריך שלא יהיה משתנה חופשי. כלומר צריך ש-$k^2-1\neq0$, כלומר ההעתקה חח״ע אם $k\neq\pm1$."),
    8, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"עבור $k=1$ מצאו את המימד והבסיס של $\mathrm{Ker}\,T$.",
    J(r"אם $k=1$ ראינו שמטריצה מדורגת היא",
      r"$$" + pm("1&1&1", "0&1&2", "0&0&0", "0&0&0") + r"\longrightarrow" + pm("1&0&-1", "0&1&2", "0&0&0", "0&0&0") + r"\longrightarrow t" + pm("1", "-2", "1") + "$$",
      r"בסיס של $\mathrm{Ker}\,T$: $\left(1-2t+t^2\right)$, $\dim\mathrm{Ker}\,T=1$."),
    6, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"נתונה העתקה לינארית $F:\mathbb{R}^2\to\mathbb{R}^2$ לפי $F\left(" + pm("1", "1") + r"\right)=" + pm("2", "2") + r",\ F\left(" + pm("3", "4") + r"\right)=" + pm("5", "0") + r"$. מצאו את המטריצה המייצגת הסטנדרטית $[F]_E^E$ של $F$ ($E$ בסיס סטנדרטי של $\mathbb{R}^2$).",
    J(r"$\left|\begin{matrix}1&3\\1&4\end{matrix}\right|=1\neq0$ אז $B=\left(" + pm("1", "1") + "," + pm("3", "4") + r"\right)$ בסיס של $\mathbb{R}^2$. לכן $[I]_E^B=" + pm("1&3", "1&4") + r"$.",
      r"$$F\left(" + pm("1", "1") + r"\right)=" + pm("2", "2") + r",\ F\left(" + pm("3", "4") + r"\right)=" + pm("5", "0") + r"\ \Rightarrow\ [F]_E^B=" + pm("2&5", "2&0") + "$$",
      r"$$[F]_E^E=[I]_E^E[F]_E^B[I]_B^E=" + pm("1&0", "0&1") + pm("2&5", "2&0") + pm("1&3", "1&4") + r"^{-1}=" + pm("2&5", "2&0") + pm("4&-3", "-1&1") + "=" + pm("3&-1", "8&-6") + "$$"),
    5))

exam = {
    "examCode": "22B-B",
    "examLabel": "מבחן סוף סמסטר ב׳ תשפ״ב, מועד ב׳ (04.07.2022)",
    "year": 2022,
    "examDate": "04.07.2022",
    "sourceFile": "22B-B exam + official solution (PDF)",
    "solutionFile": "22B-B exam + official solution (PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
