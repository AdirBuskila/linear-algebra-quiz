# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-A.json -- linear algebra, semester A 2023, moed A (02.02.2023), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-A.py

Source: one PDF (9pp): the exam text followed question by question by the typed official solution.
Five questions of 25 points (best 4 count), 19 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (B); in the raw schema item 2 is part "gimel".
- Q1 c: the official solution writes det(C^5)=3206-3205=1. The true product is 34*89-55*55=3026-3025=1. Typo in the
  official line (the conclusion det(C^5)=1 is right); flagged inside the solution text.
- Q3 item 2: the official solution calls the matrix A, the exam calls it B. Written as B here.
- Q4 c: the second intermediate matrix of the official reduction has an arithmetic slip in its fourth row; only the
  initial matrix and the conclusion (rank 4) are reproduced, and the slip is flagged inside the solution text.
- Q2 d: the official roots are decimal approximations; kept, with the exact form added in the solution.

Checks (sympy, tools/verify/23A-A/verify_23A-A.py): every official result reproduces (C^-2, determinants, Q2 cases and the
k=2 family, the roots, A^-1 and its elementary factors, charpoly, P and D, dims of U, W, U+W, U cap W, Ker/Im T, q=35,
[T]_C^B). No mismatch, no hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-A.json"


def J(*lines):
    return "\n".join(lines)


def Q(num, part, kind, topic, question, solution, points, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question,
         "solution": solution, "solutionSource": "official-pdf", "official": True, "confidence": "high"}
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
           "text": J(r"נתונה המערכת",
                     r"$$\begin{cases} 2x+ky-z=-2\\ x-3z=-3\\ x+2y+kz=1\end{cases}$$",
                     r"כאשר $k$ הוא פרמטר ממשי.")},
    "c3": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
           "text": r"נתונה המטריצה $A=" + pm("1&5&1", "2&11&0", "0&0&1") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של מטריצות",
           "text": J(r"יהי $V=M_{2\times2}(\mathbb{R})$ מרחב המטריצות הריבועיות מסדר 2. נגדיר בו שני תתי-מרחבים $U$ ו-$W$ באופן הבא",
                     r"$U=\mathrm{Sp}\left\{" + pm("1&2", "3&4") + "," + pm("1&1", "-1&1") + "," + pm("1&0", "-1&3") + r"\right\}$,",
                     r"$W=\left\{A\in V\mid A=A^T\ \wedge\ \mathrm{Tr}(A)=0\right\}$")},
    "c5": {"kind": "text", "title": "שאלה 5 - העתקה ממטריצות ל-R4",
           "text": J(r"נתונה העתקה לינארית $T:M_{2\times2}(\mathbb{R})\to\mathbb{R}^4$ המוגדרת על ידי הנוסחה",
                     r"$$T\left(" + pm("a&b", "c&d") + r"\right)=" + pm("a+b+2c+2d", "a+2b+3c-2d", "3a+4b+7c+2d", "3a+5b+8c-2d") + "$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "eigen_diagonalization",
    r"הוכח שאם $\vec v$ ו-$\vec w$ הם וקטורים עצמיים **המתאימים לאותו ערך עצמי** $\lambda$ של מטריצה ריבועית $A$, אז כל צירוף ליניארי $c\vec v+d\vec w$ ($c\neq0,\ d\neq0$) גם מהווה וקטור עצמי של $A$.",
    J(r"נתון שמתקיים $\begin{cases}A\vec v=\lambda\vec v\\ A\vec w=\lambda\vec w\end{cases}$. מכאן",
      r"$$A(c\vec v+d\vec w)=c(A\vec v)+d(A\vec w)=c\lambda\vec v+d\lambda\vec w=\lambda(c\vec v+d\vec w)$$",
      r"וזה מוכיח ש-$c\vec v+d\vec w$ הוא וקטור עצמי נוסף של מטריצה $A$."),
    5))

questions.append(Q(
    1, "ב", "proof", "eigen_diagonalization",
    r"הוכח שאם $\vec v$ ו-$\vec w$ הם וקטורים עצמיים **המתאימים לערכים עצמיים שונים** של מטריצה ריבועית $B$, אז כל צירוף ליניארי $c\vec v+d\vec w$ ($c\neq0,\ d\neq0$) אינו מהווה וקטור עצמי של $B$.",
    J(r"נתון שמתקיים $\begin{cases}B\vec v=\lambda_1\vec v\\ B\vec w=\lambda_2\vec w\end{cases}$ כאשר $\lambda_1\neq\lambda_2$. מכאן, $c\neq0,\ d\neq0$ ואם $B(c\vec v+d\vec w)=c(B\vec v)+d(B\vec w)=c\lambda_1\vec v+d\lambda_2\vec w$, אז אין שום אפשרות להגיע לשוויון $B(c\vec v+d\vec w)=\lambda(c\vec v+d\vec w)$."),
    5))

questions.append(Q(
    1, "ג", "computation", "rank_inverse",
    r"תהי $C$ מטריצה ריבועית מסדר 2 המקיימת את $C^5=" + pm("34&-55", "-55&89") + r"$ וגם $C^3=" + pm("5&-8", "-8&13") + r"$. הוכח ש-$C$ הפיכה וחשבו את $C^{-2}$.",
    J(r"ראשית, $\det\left(C^3\right)=\det(C\cdot C\cdot C)=\det{}^3(C)=65-64=1\neq0$ וגם $\det\left(C^5\right)=3206-3205=1\neq0$ "
      r"(שימו לב: בטקסט הרשמי כתוב $3206-3205$, אך החישוב הנכון הוא $34\cdot89-55^2=3026-3025=1$; המסקנה $\det\left(C^5\right)=1$ נכונה). "
      r"ולכן $\det(C)\neq0$ ו-$C$ היא מטריצה הפיכה.",
      r"מכיוון ש-$C^5$ היא מטריצה ריבועית מסדר 2, אז $C^{-5}=\left(C^5\right)^{-1}$, ומדובר כאן במטריצות ריבועיות מסדר 2, ולכן $C^{-5}=" + pm("89&55", "55&34") + "$. מכאן נקבל ש",
      r"$$C^{-2}=C^3\cdot C^{-5}=" + pm("5&-8", "-8&13") + r"\cdot" + pm("89&55", "55&34") + "=" + pm("5&3", "3&2") + "$$"),
    7))

questions.append(Q(
    1, "ד", "proof", "determinants",
    r"נתונות שלוש מטריצות ריבועיות $A,B,P$ מאותו הסדר וידוע ש-$P$ היא הפיכה ומתקיים $A=P^{-1}BP$. הוכח ש-$A$ תהיה הפיכה אם ורק אם $B$ הפיכה.",
    J(r"אם נניח ש-$A$ הפיכה, אז $0\neq\det(A)=\det\left(P^{-1}BP\right)=\det\left(P^{-1}\right)\det(B)\det(P)$ ומכיוון ש-$P$ הפיכה, אז $\det(P)\neq0$, והשוויון האחרון יתקיים רק כאשר $\det(B)\neq0$, כלומר $B$ הפיכה.",
      r"מצד שני, אם נניח ש-$B$ הפיכה ועבור $\det(B)\neq0$, אז $0\neq\det(A)=\det\left(P^{-1}BP\right)=\det\left(P^{-1}\right)\det(B)\det(P)$, כלומר גם $A$ הפיכה."),
    8))

# ------------------------------------------------------------------ Q2
SYS = [["2", "k", "-1", "-2"], ["1", "0", "-3", "-3"], ["1", "2", "k", "1"]]
SW = [["1", "0", "-3", "-3"], ["2", "k", "-1", "-2"], ["1", "2", "k", "1"]]
S1 = [["1", "2", "k", "1"], ["1", "0", "-3", "-3"], ["2", "k", "-1", "-2"]]
S2 = [["1", "2", "k", "1"], ["0", "2", "k+3", "4"], ["0", "4-k", "2k+1", "4"]]
S3 = [["1", "2", "k", "1"], ["0", "2", "k+3", "4"], ["0", "0", "k^2+3k-10", "4k-8"]]

questions.append(Q(
    2, "א", "computation", "linear_systems",
    "הצג את המערכת בעזרת מטריצה מורחבת ודרג אותה.",
    J(r"נדרג את המטריצה של המערכת:",
      "$$" + aug(SYS) + r"\Leftrightarrow" + aug(S1) + r"\Leftrightarrow" + aug(S2) + r"\Leftrightarrow" + aug(S3) + "$$"),
    9, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $k$ אין פתרון למערכת? יש פתרון יחיד? יש אינסוף פתרונות שונים?",
    J(r"עבור $k=-5$ אין למערכת פתרון (כי מתקבלת שורת סתירה בשורה האחרונה). עבור $k=2$ יש למערכת אינסוף פתרונות (שכן השורה האחרונה מתאפסת). בשאר המקרים למערכת קיים פתרון יחיד.",
      r"השורה האחרונה במטריצה המדורגת: $$(k+5)(k-2)\,z=4(k-2)$$"),
    5, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"מצא פתרון של המערכת עבור $k=2$.",
    J(r"עבור $k=2$ נקבל $\begin{cases}x+2y+2z=1\\ 2y+5z=4\end{cases}$, ולכן מתקבלת המערכת",
      "$$" + aug([["1", "2", "2", "1"], ["0", "2", "5", "4"], ["0", "0", "0", "0"]]) + "$$",
      r"$z$ משתנה חופשי. ולכן פתרון המערכת הוא",
      r"$$\begin{cases}x=-3+3t\\ y=2-2.5t\\ z=t\end{cases},\qquad t\in\mathbb{R}$$"),
    5, contextId="c2"))

questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"מצא את כל הפתרונות המרוכבים של $z^2+(3i-4)z+2i=0$.",
    J(r"נפתור את המשוואה $z^2+(3i-4)z+2i=0$ באמצעות משוואה ריבועית:",
      r"$$z_{1,2}=\frac{-(3i-4)\pm\sqrt{(3i-4)^2-8i}}{2}=\frac{(4-3i)\pm\sqrt{-9-24i+16-8i}}{2}=\frac{(4-3i)\pm\sqrt{7-32i}}{2}$$",
      r"כעת נחשב בנפרד את $\sqrt{7-32i}$: אנו למעשה מחפשים $w$ המקיים $w^2=7-32i$. נרשום $w=r\,\mathrm{cis}(\theta)$. על פי דמואבר $w^2=r^2\mathrm{cis}(2\theta)$. נרשום את $7-32i$ בצורה טריגונומטרית:",
      r"$$7-32i=\sqrt{7^2+32^2}\,\mathrm{cis}\left(\tan^{-1}\left(-\frac{32}{7}\right)\right)\approx32.76\,\mathrm{cis}(-77.66^\circ)$$",
      r"ולכן:",
      r"$$r^2\mathrm{cis}(2\theta)=32.76\,\mathrm{cis}(-77.66^\circ)\ \Rightarrow\ \begin{cases}r^2=32.76\\ \theta=-\frac{77.66}{2}+180k\end{cases}$$",
      r"ומכאן ש-$r=5.72$ ו-$\theta_1=-38.83^\circ,\ \theta_2=141.17^\circ$. לכן:",
      r"$$w_1=5.72\,\mathrm{cis}(-38.83^\circ)=4.46-3.59i,\qquad w_2=5.72\,\mathrm{cis}(141.17^\circ)=-4.46+3.59i$$",
      r"כעת נציב זאת חזרה במשוואה הריבועית, לקבל את השורשים המבוקשים:",
      r"$$z_1=\frac{(4-3i)+(4.46-3.59i)}{2}\approx4.23-3.295i,\qquad z_2=\frac{(4-3i)-(4.46-3.59i)}{2}\approx-0.23+0.295i$$",
      r"(הערכים בפתרון הרשמי מקורבים. הצורה המדויקת: $z_{1,2}=\frac{(4-3i)\pm\sqrt{7-32i}}{2}$.)"),
    6, contextId="c2"))

# ------------------------------------------------------------------ Q3
chain = [
    (aug([["1", "5", "1", "1", "0", "0"], ["2", "11", "0", "0", "1", "0"], ["0", "0", "1", "0", "0", "1"]]), r"R_2\to R_2-2R_1"),
    (aug([["1", "5", "1", "1", "0", "0"], ["0", "1", "-2", "-2", "1", "0"], ["0", "0", "1", "0", "0", "1"]]), r"R_2\to R_2+2R_3"),
    (aug([["1", "5", "1", "1", "0", "0"], ["0", "1", "0", "-2", "1", "2"], ["0", "0", "1", "0", "0", "1"]]), r"R_1\to R_1-R_3"),
    (aug([["1", "5", "0", "1", "0", "-1"], ["0", "1", "0", "-2", "1", "2"], ["0", "0", "1", "0", "0", "1"]]), r"R_1\to R_1-5R_2"),
    (aug([["1", "0", "0", "11", "-5", "-11"], ["0", "1", "0", "-2", "1", "2"], ["0", "0", "1", "0", "0", "1"]]), None),
]
inv_chain = "$$" + "".join(m + (arrow(op) if op else "") for m, op in chain) + "$$"

questions.append(Q(
    3, "א", "computation", "rank_inverse",
    r"הוכח ש-$A$ הפיכה על ידי מציאת המטריצה $A^{-1}$.",
    J(r"נחשב את $A^{-1}$:", inv_chain,
      r"קיבלנו שהמטריצה ההופכית היא:",
      r"$$A^{-1}=" + pm("11&-5&-11", "-2&1&2", "0&0&1") + "$$"),
    6, contextId="c3"))

questions.append(Q(
    3, "ב", "computation", "rank_inverse",
    r"הצג את $A^{-1}$ בצורה של מכפלה של מטריצות אלמנטריות.",
    J(r"כעת נשתמש בדירוג הנ״ל ונכתוב את $A^{-1}$ כמכפלה של מטריצות אלמנטריות:",
      r"$$A^{-1}=" + pm("1&-5&0", "0&1&0", "0&0&1") + pm("1&0&-1", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&2", "0&0&1") + pm("1&0&0", "-2&1&0", "0&0&1") + "$$"),
    7, contextId="c3"))

B3 = pm("1&0&0", "-1&6&1", "-1&5&2")
questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + B3 + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצא מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $D=P^{-1}BP$.",
    J(r"תחילה נמצא את כל הערכים העצמיים והווקטורים העצמיים של $B$. נחשב את הדטרמיננטה הבאה לפי שורה ראשונה:",
      r"$$|\lambda I-B|=\begin{vmatrix}\lambda-1&0&0\\1&\lambda-6&-1\\1&-5&\lambda-2\end{vmatrix}=(\lambda-1)\begin{vmatrix}\lambda-6&-1\\-5&\lambda-2\end{vmatrix}=(\lambda-1)[(\lambda-6)(\lambda-2)-5]=(\lambda-1)(\lambda^2-8\lambda+7)=(\lambda-1)(\lambda-1)(\lambda-7)$$",
      r"קיבלנו שהערכים העצמיים הם: $1,1,7$. כעת נמצא את הווקטורים העצמיים.",
      r"**עבור ע״ע 1:**",
      r"$$" + pm("0&0&0", "1&-5&-1", "1&-5&-1") + r"\to\cdots\to" + pm("1&-5&-1", "0&0&0", "0&0&0") + "$$",
      r"נסמן $y=t,\ z=s$ ונקבל $x=5t+s$. הווקטורים העצמיים המתקבלים הם $(5,1,0)^T,\ (1,0,1)^T$.",
      r"**עבור ע״ע 7:**",
      r"$$" + pm("6&0&0", "1&1&-1", "1&-5&5") + r"\to\cdots\to" + pm("1&0&0", "0&1&-1", "0&0&0") + "$$",
      r"נסמן $z=t$ ונקבל $x=0,\ y=t$. הווקטור העצמי המתקבל הוא $(0,1,1)^T$.",
      r"המטריצה ניתנת לליכסון (שלושה וקטורים עצמיים בלתי תלויים). כעת נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$:",
      r"$$D=" + pm("1&0&0", "0&1&0", "0&0&7") + r",\qquad P=" + pm("5&1&0", "1&0&1", "0&1&1") + "$$"),
    12))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"מצא את הבסיס והמימד של $U$.",
    J(r"על מנת למצוא את הבסיס של $U$ נבדוק את התלות הליניארית בקבוצה הפורשת:",
      r"$$\begin{cases}a+b+c=0\\ 2a+b=0\\ 3a-b-c=0\\ 4a+b+3c=0\end{cases}\ \Rightarrow\ a=0\Rightarrow b=0\Rightarrow c=0$$",
      r"לפיכך הקבוצה הפורשת בלתי תלויה לינארית, ומהווה בסיס שלם ל-$U$, ו-$\dim U=3$."),
    6, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"מצא את הבסיס והמימד של $W$.",
    J(r"לגבי $W$, נשים לב שלפנינו שני אילוצים. מצד אחד, כל מטריצה ששייכת ל-$W$ חייבת להיות סימטרית, ומצד שני העקבה של כל מטריצה צריכה להיות שווה לאפס. נבטא זאת כך:",
      r"$$A=" + pm("a&b", "c&d") + r"\xrightarrow{A=A^T}" + pm("a&b", "b&d") + r"\xrightarrow{\mathrm{Tr}(A)=0}" + pm("a&b", "b&-a") + "=a" + pm("1&0", "0&-1") + "+b" + pm("0&1", "1&0") + "$$",
      r"לפיכך התנאים לקיומו של $W$ כתת מרחב של $V$ מתקיימים, והבסיס והמימד נתונים:",
      r"$$W=\mathrm{Sp}\left\{" + pm("1&0", "0&-1") + "," + pm("0&1", "1&0") + r"\right\},\qquad\dim W=2$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצא את הבסיס והמימד של $U+W$.",
    J(r"על מנת לקבוע את הבסיס והמימד של הסכום $U+W$, נבקש לבדוק אי-תלות בבסיס המשותף, וזאת על ידי ייצוג כל מטריצה (מטריצה) בתור שורה, ודירוג. נציג את הבסיס של $W$ ואת הבסיס של $U$ כשורות:",
      r"$$\left\{" + pm("1&0", "0&-1") + "," + pm("0&1", "1&0") + "," + pm("1&2", "3&4") + "," + pm("1&1", "-1&1") + "," + pm("1&0", "-1&3") + r"\right\}\ \Rightarrow\ " + pm("1&0&0&-1", "0&1&1&0", "1&2&3&4", "1&1&-1&1", "1&0&-1&3") + "$$",
      r"אחרי דירוג מתקבלת דרגה 4 (הערה: במטריצת הביניים המופיעה בפתרון הרשמי, בשורה הרביעית יש טעות חישוב; המסקנה על הדרגה נכונה). כלומר, שורה (מטריצה) אחת תלויה לינארית, ו-$\dim(U+W)=4=\dim V$. לפיכך $U+W=V$, ונקבע את הבסיס להיות הבסיס הסטנדרטי של $M_{2\times2}(\mathbb{R})$:",
      r"$$U+W=\mathrm{Sp}\left\{" + pm("1&0", "0&0") + "," + pm("0&1", "0&0") + "," + pm("0&0", "0&1") + "," + pm("0&0", "1&0") + r"\right\}$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"מצא את הבסיס והמימד של $U\cap W$, והראה שמתקיים משפט המימדים.",
    J(r"את החיתוך $U\cap W$ נחשב מהדרישה שהצירופים הליניאריים של $U$ ו-$W$ שווים:",
      r"$$a" + pm("1&2", "3&4") + "+b" + pm("1&1", "-1&1") + "+c" + pm("1&0", "-1&3") + "=e" + pm("1&0", "0&-1") + "+f" + pm("0&1", "1&0") + "$$",
      r"מדרישה זו נקבל תנאים על המקדמים:",
      r"$$\begin{cases}a+b+c=e\\ 2a+b=f\\ 3a-b-c=f\\ 4a+b+3c=-e\end{cases}\ \Rightarrow\ \begin{cases}5a+2b+4c=0\\ a-2b-c=0\end{cases}\ \Rightarrow\ c=-2a\Rightarrow b=\frac{3}{2}a$$",
      r"$$a" + pm("1&2", "3&4") + r"+\frac{3}{2}a" + pm("1&1", "-1&1") + "-2a" + pm("1&0", "-1&3") + r"=\frac{a}{2}" + pm("1&7", "7&-1") + "$$",
      r"$$\Rightarrow\ U\cap W=\mathrm{Sp}\left\{" + pm("1&7", "7&-1") + r"\right\},\qquad\dim(U\cap W)=1$$",
      r"אכן מתקיים משפט המימדים:",
      r"$$\dim(U+W)=\dim(U)+\dim(W)-\dim(U\cap W)\ \Rightarrow\ 4=3+2-1$$"),
    7, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצא את המימד ובסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    J(r"נסמן ב-$F=(E_1,E_2,E_3,E_4)$ את הבסיס הסטנדרטי של $M_{2\times2}(\mathbb{R})$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^4$.",
      r"$$T(E_1)=" + pm("1", "1", "3", "3") + r",\ T(E_2)=" + pm("1", "2", "4", "5") + r",\ T(E_3)=" + pm("2", "3", "7", "8") + r",\ T(E_4)=" + pm("2", "-2", "2", "-2") + "$$",
      r"מטריצה מייצגת סטנדרטית היא $A=[T]_E^F=" + pm("1&1&2&2", "1&2&3&-2", "3&4&7&2", "3&5&8&-2") + "$.",
      r"$$" + aug([["1", "1", "2", "2", "0"], ["1", "2", "3", "-2", "0"], ["3", "4", "7", "2", "0"], ["3", "5", "8", "-2", "0"]], 4) + r"\to" + aug([["1", "1", "2", "2", "0"], ["0", "1", "1", "-4", "0"], ["0", "1", "1", "-4", "0"], ["0", "2", "2", "-8", "0"]], 4)
      + r"\to" + aug([["1", "1", "2", "2", "0"], ["0", "1", "1", "-4", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$",
      r"ומכאן, ברור לנו שעמודות הציר של המטריצה הן העמודות מס׳ 1,2 של המטריצה המדורגת (עמודות מובילות), אז העמודות $\left\{" + pm("1", "1", "3", "3") + "," + pm("1", "2", "4", "5") + r"\right\}$ מהוות בסיס של מרחב העמודה של $\mathrm{Col}\,A$ ז״א בסיס של $\mathrm{Im}\,T$ ואז $\dim\mathrm{Im}\,T=2$.",
      r"$$" + aug([["1", "1", "2", "2", "0"], ["0", "1", "1", "-4", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4) + r"\to" + aug([["1", "0", "1", "6", "0"], ["0", "1", "1", "-4", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 4)
      + r"\Rightarrow\begin{cases}x_1=-t-6s\\x_2=-t+4s\\x_3=t\\x_4=s\end{cases}\Rightarrow" + pm("x_1", "x_2", "x_3", "x_4") + "=t" + pm("-1", "-1", "1", "0") + "+s" + pm("-6", "4", "0", "1") + "$$",
      r"אז בסיס של $\mathrm{Ker}\,T$ הוא $\left(" + pm("-1&-1", "1&0") + "," + pm("-6&4", "0&1") + r"\right)$ ז״א בסיס של $\mathrm{Nul}\,A$, ואז $\dim\mathrm{Ker}\,T=2$."),
    10, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ היא חד חד ערכית? האם היא על? נמק!",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=2\neq0$, ולא על כי $\dim\mathrm{Im}\,T=2\neq\dim\mathbb{R}^4$.",
    3, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטר $q$ מתקיים $" + pm("11", "12", "34", "q") + r"\in\mathrm{Im}\,T$?",
    J(r"$$" + aug([["1", "1", "11"], ["1", "2", "12"], ["3", "4", "34"], ["3", "5", "q"]], 2) + r"\to" + aug([["1", "1", "11"], ["0", "1", "1"], ["0", "1", "1"], ["0", "2", "q-33"]], 2)
      + r"\to" + aug([["1", "1", "11"], ["0", "1", "1"], ["0", "0", "0"], ["0", "0", "q-35"]], 2) + r"\to" + aug([["1", "1", "11"], ["0", "1", "1"], ["0", "0", "q-35"], ["0", "0", "0"]], 2) + "$$",
      r"ומכאן נובע ש-$q=35$."),
    5, contextId="c5"))

BB = "\\left(" + pm("0&0", "2&0") + "," + pm("2&0", "0&0") + "," + pm("0&2", "0&0") + "," + pm("0&0", "0&2") + "\\right)"
CC = "\\left(" + pm("0", "0", "-1", "0") + "," + pm("0", "0", "0", "-1") + "," + pm("1", "0", "0", "0") + "," + pm("0", "1", "0", "0") + "\\right)"
questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"מצא את המטריצה המייצגת $[T]_C^B$ של $T$, אם $B=" + BB + r"$ בסיס של $M_{2\times2}(\mathbb{R})$ ו-$C=" + CC + r"$ בסיס של $\mathbb{R}^4$.",
    J(r"**לפי הגדרה של מטריצה של $T$ ביחס לבסיסים נתונים:** $T_{C\leftarrow B}=\left[(T(b_1))_C\ \ (T(b_2))_C\ \ (T(b_3))_C\ \ (T(b_4))_C\right]$, כאשר",
      r"$$T(b_1)=" + pm("4", "6", "14", "16") + r",\ T(b_2)=" + pm("2", "2", "6", "6") + r",\ T(b_3)=" + pm("2", "4", "8", "10") + r",\ T(b_4)=" + pm("4", "-4", "4", "-4") + "$$",
      r"נפרק כל אחד מהם לפי הבסיס $C$ (מערכת $\alpha,\beta,\gamma,\delta$ עבור צירוף של וקטורי $C$ לפי הסדר), ומתקבל:",
      r"$$(T(b_1))_C=" + pm("-14", "-16", "4", "6") + r",\ (T(b_2))_C=" + pm("-6", "-6", "2", "2") + r",\ (T(b_3))_C=" + pm("-8", "-10", "2", "4") + r",\ (T(b_4))_C=" + pm("-4", "4", "4", "-4") + "$$",
      r"והמטריצה המנדרשת מתקבלת בצורה",
      r"$$[T]_C^B=" + pm("-14&-6&-8&-4", "-16&-6&-10&4", "4&2&2&4", "6&2&4&-4") + "$$",
      r"**פתרון אחר:**",
      r"$$[T]_C^B=[I]_C^E[T]_E^F[I]_F^B=" + pm("0&0&-1&0", "0&0&0&-1", "1&0&0&0", "0&1&0&0") + pm("1&1&2&2", "1&2&3&-2", "3&4&7&2", "3&5&8&-2") + pm("0&2&0&0", "0&0&2&0", "2&0&0&0", "0&0&0&2")
      + "=" + pm("-3&-4&-7&-2", "-3&-5&-8&2", "1&1&2&2", "1&2&3&-2") + pm("0&2&0&0", "0&0&2&0", "2&0&0&0", "0&0&0&2") + "=" + pm("-14&-6&-8&-4", "-16&-6&-10&4", "4&2&2&4", "6&2&4&-4") + "$$"),
    7, contextId="c5"))

exam = {
    "examCode": "23A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״ג, מועד א׳ (02.02.2023)",
    "year": 2023,
    "examDate": "02.02.2023",
    "sourceFile": "23A-A exam + official solution (single PDF)",
    "solutionFile": "23A-A exam + official solution (single PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
