# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-A.json -- linear algebra, semester A 2021, moed A (24.01.2021), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-A.py

Source: exam PDF (3pp, exam only; page 3 is blank) + solution file "סמ׳ א מועד א פתרון.pdf" (14pp; typed Q1-Q3, Q5,
handwritten Q4). The triage paired that solution file with 20A-A, but its content is the 21A-A solution (AA^T+A^2=3I,
this system, these A and B, T on M2x2, Q4 on R2[x]); rendered pages are in tools/raw/20A-A-SOL/.
Official solutions transcribed for 19 of 20 items, checked in tools/verify/21A-A/verify_21A-A.py.
- Q1 c/d: the official gives |A|=sqrt(27/8), |A^-1|=sqrt(8/27); the data fix only |A|^2=27/8 and both signs occur
  (A=+-sqrt(3/2) I). Shipped as +-, labeled "הפתרון הרשמי עם תיקון", official false.
- Q3 b (A^-1 at a=2) stays held: A is singular at a=2 (det A=-6(a-2)(6a+7)), and the solution file belongs to a version
  of the exam without this part (its Q3 is 8+9+8 points: invertibility, eigenpairs, D/P).
- Q4 b: the handwritten step label R4->R4+2R2 gives (0,2,3), not the printed row (0,0,2); the operation is R4->R4+R2.
  Corrected without a label (intermediate slip), logged in ASK_ADIR.
- Q2 c: the official prints the s-direction as (0,-1,1), which is not in the plane x-y+z=0; its own line x=t-s-1
  gives (-1,0,1). Final answer corrected, labeled, official false.
- Q2 d: explicit values of the three cube roots added in one bracketed line.
Five questions of 25 points (best 4 count), 20 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts 1,2 = 6+6 pts) and item 2 (B, parts 1,2 = 8+5 pts). In the raw schema the four
  sub-parts are א, ב, ג, ד in printed order (A1, A2, B1, B2).
- Q4 and Q5: printed parts א-ד.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21A-A.json"


def J(*lines):
    return "\n".join(lines)


def pm(*rows):
    return r"\begin{pmatrix}" + r"\\".join(r if isinstance(r, str) else "&".join(str(c) for c in r) for r in rows) + r"\end{pmatrix}"


def H(num, part, kind, topic, question, points, ctx=None):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question, "hold": "no-key"}
    if ctx:
        q["contextId"] = ctx
    return q


contexts = {
    "c1": {"kind": "text", "title": "שאלה 1 - המטריצה A",
           "text": J(r"נתונה מטריצה $A$ ממשית מסדר $3\times3$ המקיימת את המשוואות $AA^T+A^2=3I$ ו-$AA^T-A^2=0$.")},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם פרמטר",
           "text": J(r"נתונה מערכת המשוואות הבאה, כאשר $a\in\mathbb{R}$ פרמטר ממשי כלשהו:",
                     r"$$\begin{cases} x-y-az=a\\ ax+y-z=-a\\ x+ay+z=-1\end{cases}$$")},
    "c3a": {"kind": "text", "title": "שאלה 3 - סעיף א",
            "text": r"תהי נתונה המטריצה $A=" + pm("2a&3&6", r"4&a+1&4a-2", "1&5&2") + r"$ כאשר $a$ הוא פרמטר ממשי."},
    "c3b": {"kind": "text", "title": "שאלה 3 - סעיף ב",
            "text": r"תהי נתונה מטריצה $B=" + pm("6&0&2", "1&4&0", "0&0&3") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של פולינומים",
           "text": J(r"יהי $\mathbb{R}_2[x]=\left\{p(x)\mid a_0+a_1x+a_2x^2,\ a_0,a_1,a_2\in\mathbb{R}\right\}$ מרחב של פולינומים ממשיים ממעלה שתיים לכל היותר. נגדיר שני תתי מרחבים של מרחב זה:",
                     r"$$W=\left\{p(x)\in\mathbb{R}_2[x]:\ p'(1)=0\right\}$$",
                     r"ו-",
                     r"$$U=\mathrm{Sp}\left\{1+x,\ 2-x^2,\ 2x+x^2\right\}$$",
                     r"כאשר $p'(x)=\left(a_0+a_1x+a_2x^2\right)'=a_1+2a_2x$.")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": J(r"נסמן ב-$\mathbb{M}_2(\mathbb{R})$ קבוצת מטריצות ריבועיות $2\times2$ ונגדיר את ההעתקה $T:\mathbb{M}_2(\mathbb{R})\to\mathbb{R}^3$ המוגדרת לפי",
                     r"$$T\left(" + pm("a&b", "c&d") + r"\right)=" + pm("a+b", "b+c", "b+d") + "$$")},
}

HOLD_Q3B = ("misprint/not covered: det A = -6(a-2)(6a+7), so A is singular exactly at the printed a=2 (rows 1 and 2 both "
            "equal (4,3,6)); A^-1 does not exist there. The official solution file belongs to a version of the exam without "
            "this part (its Q3 A is one 8-pt item), so the intended a is unknown")

FIX = r"**הפתרון הרשמי עם תיקון:** "


def O(num, part, kind, topic, question, solution, points, ctx=None, **kw):
    """official solution (lecturer's typed/handwritten solution file)"""
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question,
         "solution": solution, "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if ctx:
        q["contextId"] = ctx
    q.update(kw)
    return q


def aug(rows, left=3):
    n = len(rows[0])
    spec = "c" * left + "|" + "c" * (n - left)
    return r"\left(\begin{array}{" + spec + "}" + r"\\".join("&".join(str(c) for c in r) for r in rows) + r"\end{array}\right)"


def arrow(op):
    return r"\xrightarrow{" + op + "}"


def col(*v):
    return pm(*[[c] for c in v])


M2 = lambda a, b, c, d: pm(f"{a}&{b}", f"{c}&{d}")
FR = lambda n, d: r"\frac{" + str(n) + "}{" + str(d) + "}"
RR = r"\frac{1-a}{a-2}"
ECH = [[1, 0, -1, 0], [0, 1, "(a-1)", "-a"], [0, 0, "-(a+1)(a-2)", "(a+1)(a-1)"]]

questions = [
    # ------------------------------------------------------------------ Q1
    O(1, "א", "proof", "matrix_proofs", r"הראו כי $A$ הפיכה ע״י מציאת ביטוי של המטריצה ההפוכה באמצעות $A$.",
      J(r"מהמשוואה $AA^T+A^2=3I$ נקבל $\frac13A\left(A^T+A\right)=A\cdot\frac13\left(A+A^T\right)=I$, כלומר קיימת הפיכה",
        r"$$A^{-1}=\frac13\left(A+A^T\right)$$"),
      7, "c1"),
    O(1, "ב", "proof", "matrix_proofs", r"הוכיחו כי $A^{-1}$ מטריצה סימטרית.",
      J(r"נרשום",
        r"$$\left(A^{-1}\right)^T=\left(\frac13\left(A+A^T\right)\right)^T=\frac13A^T+\frac13\left(A^T\right)^T=\frac13\left(A+A^T\right)=A^{-1}$$"),
      7, "c1"),
    O(1, "ג", "computation", "determinants", r"חשבו את הדטרמיננטה $|A|$.",
      J(FIX + r"בפתרון הרשמי נקבע $|A|=\sqrt{\frac{27}{8}}$; מהשוויון $|A|^2=\frac{27}{8}$ נובע רק ש-$|A|=\pm\sqrt{\frac{27}{8}}$.",
        r"נחלץ מהמשוואה $AA^T-A^2=0$ את $AA^T$, נציב ב-$AA^T+A^2=3I$ ונקבל $2A^2=3I$. לכן",
        r"$$\left|2A^2\right|=2^3|A|^2=3^3|I|$$",
        r"ונקבל לבסוף $|A|^2=\frac{27}{8}$, כלומר",
        r"$$|A|=\pm\sqrt{\frac{27}{8}}=\pm\frac{3\sqrt6}{4}$$",
        r"**הערה:** שני הסימנים אפשריים. המטריצות $A=\sqrt{\frac32}\,I$ ו-$A=-\sqrt{\frac32}\,I$ סימטריות, ולכן לשתיהן $AA^T=A^2=\frac32I$ והן מקיימות את שתי המשוואות; הדטרמיננטות שלהן הן $\frac{3\sqrt6}{4}$ ו-$-\frac{3\sqrt6}{4}$."),
      7, "c1", solutionSource="solved", official=False),
    O(1, "ד", "computation", "determinants", r"חשבו את הדטרמיננטה $\left|A^{-1}\right|$.",
      J(FIX + r"בפתרון הרשמי נקבע $\left|A^{-1}\right|=\sqrt{\frac{8}{27}}$; בהתאם לסעיף הקודם התוצאה היא $\pm\sqrt{\frac{8}{27}}$.",
        r"מאחר ו-$A$ הפיכה",
        r"$$\left|A^{-1}\right|=|A|^{-1}=\pm\sqrt{\frac{8}{27}}=\pm\frac{2\sqrt6}{9}$$",
        r"(עם אותו סימן כמו $|A|$)."),
      4, "c1", solutionSource="solved", official=False),

    # ------------------------------------------------------------------ Q2
    O(2, "א", "computation", "linear_systems", r"הביאו את המטריצה המורחבת של המערכת לצורת מדורגת קנונית.",
      J(r"מטריצת המקדמים המורחבת של המערכת הינה",
        "$$" + aug([[1, -1, "-a", "a"], ["a", 1, -1, "-a"], [1, "a", 1, -1]]) + "$$",
        r"נבצע דירוג כדלקמן:",
        "$$" + aug([[1, -1, "-a", "a"], ["a", 1, -1, "-a"], [1, "a", 1, -1]]) + arrow(r"\substack{R_2\to R_2-aR_1\\R_3\to R_3-R_1}")
        + aug([[1, -1, "-a", "a"], [0, "1+a", "a^2-1", "-a^2-a"], [0, "1+a", "1+a", "-a-1"]]) + "$$",
        "$$" + arrow(r"R_3\to R_3-R_2") + aug([[1, -1, "-a", "a"], [0, "1+a", "a^2-1", "-a^2-a"], [0, 0, "-a^2+a+2", "a^2-1"]])
        + "=" + aug([[1, -1, "-a", "a"], [0, "1+a", "(a+1)(a-1)", "-a(a+1)"], [0, 0, "-(a+1)(a-2)", "(a+1)(a-1)"]]) + "$$",
        r"עבור המקרה $a=-1$ נקבל",
        "$$" + aug([[1, -1, 1, -1], [0, 0, 0, 0], [0, 0, 0, 0]]) + "$$",
        r"נניח כי $a\neq-1$ ונמשיך בדירוג:",
        "$$" + arrow(r"R_2\to\frac{1}{a+1}R_2") + aug([[1, -1, "-a", "a"], [0, 1, "(a-1)", "-a"], [0, 0, "-(a+1)(a-2)", "(a+1)(a-1)"]])
        + arrow(r"R_1\to R_1+R_2") + aug(ECH) + "$$",
        r"נניח כי $a=2$ ונקבל",
        "$$" + aug([[1, 0, -1, 0], [0, 1, 1, -2], [0, 0, 0, 3]]) + "$$",
        r"נניח כי $a\neq2$ ונמשיך בדירוג:",
        "$$" + aug(ECH) + arrow(r"R_3\to-\frac{1}{(a+1)(a-2)}R_3") + aug([[1, 0, -1, 0], [0, 1, "(a-1)", "-a"], [0, 0, 1, RR]]) + "$$",
        "$$" + arrow(r"\substack{R_1\to R_1+R_3\\R_2\to R_2-(a-1)R_3}") + aug([[1, 0, 0, RR], [0, 1, 0, r"\frac{1}{a-2}"], [0, 0, 1, RR]]) + "$$"),
      9, "c2"),
    O(2, "ב", "computation", "linear_systems", r"מצאו עבור אילו ערכי $a$ יש למערכת אינסוף פתרונות, פתרון יחיד או שאין לה פתרון כלל.",
      J(r"מהדירוג בסעיף הקודם אנו רואים כי למערכת שלושה מצבים:",
        r"1. $a=-1$: למערכת אינסוף פתרונות, מאחר ומתקבלות שתי שורות אפסים במטריצה המורחבת המדורגת:",
        "$$" + aug([[1, -1, 1, -1], [0, 0, 0, 0], [0, 0, 0, 0]]) + "$$",
        r"2. $a=2$: אין פתרונות, מאחר ומתקבלת שורת סתירה במטריצה המורחבת המדורגת:",
        "$$" + aug([[1, 0, -1, 0], [0, 1, 1, -2], [0, 0, 0, 3]]) + "$$",
        r"3. בשאר המצבים, $a\neq-1,2$, מתקבל פתרון יחיד שהוא",
        r"$$" + col("x", "y", "z") + "=" + col(RR, r"\frac{1}{a-2}", RR) + "$$"),
      8, "c2"),
    O(2, "ג", "computation", "linear_systems", r"עבור $a=-1$ פתרו את המערכת וכתבו את כל הפתרונות.",
      J(FIX + r"בפתרון הרשמי הווקטור הכופל את $s$ מודפס $" + col(0, -1, 1) + r"$; הוא אינו פותר את המשוואה ההומוגנית $x-y+z=0$ ($0+1+1\neq0$). מהשוויון $x=t-s-1$ שבפתרון עצמו הווקטור הוא $" + col(-1, 0, 1) + "$.",
        r"עבור $a=-1$ מתקבלת המערכת שהמטריצה המורחבת שלה הינה",
        "$$" + aug([[1, -1, 1, -1], [0, 0, 0, 0], [0, 0, 0, 0]]) + "$$",
        r"המשתנים החופשיים הינם $y,z$. נקבע משתנים אלו על ידי הפרמטרים $y=t,\ z=s$ כאשר $t,s\in\mathbb{R}$. ערך המשתנה המוביל $x$ נקבע על ידי",
        r"$$x-y+z=-1\ \Rightarrow\ x=t-s-1$$",
        r"ולכן מרחב הפתרונות נתון על ידי",
        r"$$" + col("x", "y", "z") + "=" + col(-1, 0, 0) + "+t" + col(1, 1, 0) + "+s" + col(-1, 0, 1) + "$$",
        r"כלומר מרחב הפתרונות הוא מישור במרחב $\mathbb{R}^3$."),
      4, "c2", solutionSource="solved", official=False),
    O(2, "ד", "computation", "complex_numbers", r"מצאו את כל הפתרונות המרוכבים של המשוואה $z^4+8z=0$.",
      J(r"נשים לב כי מתקיים",
        r"$$F(z)=z^4+8z=z\left(z^3+8\right)$$",
        r"נסתכל על האפסים של המשוואה $z^3+8=0$, כלומר $z^3=-8$. הפתרונות של משוואה זו הינם",
        r"$$z_k=2\left(\cos\left(\frac{2\pi k}{3}+\frac{\pi}{3}\right)+i\sin\left(\frac{2\pi k}{3}+\frac{\pi}{3}\right)\right)$$",
        r"עבור $k=0,1,2$. ולכן הפתרונות של המשוואה המקורית $z^4+8z=0$ הינם $z_0,z_1,z_2$ יחד עם $z=0$.",
        r"(במפורש: $z_0=1+\sqrt3\,i$, $z_1=-2$, $z_2=1-\sqrt3\,i$.)"),
      4),

    # ------------------------------------------------------------------ Q3
    O(3, "א", "computation", "rank_inverse", r"עבור אילו ערכי $a$ המטריצה $A$ הפיכה?",
      J(r"נחשב את הדטרמיננטה של $A$ (לפי פיתוח שורה ראשונה):",
        r"$$|A|=\begin{vmatrix}2a&3&6\\4&a+1&4a-2\\1&5&2\end{vmatrix}=2a\cdot(2a+2-20a+10)-3\cdot(8-4a+2)+6\cdot(20-a-1)=-36a^2+30a+84$$",
        r"עבור $a=2,-\frac76$ מתקבלת דטרמיננטה $0$, ולכן המטריצה לא הפיכה. מכאן שעבור $a\neq2,-\frac76$ המטריצה $A$ הפיכה.",
        r"(ואכן $-36a^2+30a+84=-6(a-2)(6a+7)$.)"),
      6, "c3a"),
    dict(H(3, "ב", "computation", "rank_inverse", r"מצאו את $A^{-1}$ עבור $a=2$.", 6, "c3a"), hold=HOLD_Q3B),
    O(3, "ג", "computation", "eigen_diagonalization", r"מצאו את כל הערכים העצמיים והווקטורים העצמיים של $B$.",
      J(r"$$|\lambda I-B|=\begin{vmatrix}\lambda-6&0&-2\\-1&\lambda-4&0\\0&0&\lambda-3\end{vmatrix}=(\lambda-3)\begin{vmatrix}\lambda-6&0\\-1&\lambda-4\end{vmatrix}=(\lambda-3)(\lambda-6)(\lambda-4)$$",
        r"קיבלנו שהערכים העצמיים הם $3,4,6$. כל הע״ע שונים זה מזה ולכן יתקבלו עבורם ו״ע בת״ל. מכאן שמטריצה $B$ ניתנת לליכסון. כעת נמצא את הווקטורים העצמיים.",
        r"**עבור ע״ע $3$:**",
        "$$" + pm("-3&0&-2", "-1&-1&0", "0&0&0") + r"\to\dots\to" + pm(r"1&0&\frac23", r"0&1&-\frac23", "0&0&0") + "$$",
        r"נסמן $z=t$ ונקבל $x=-\frac23t,\ y=\frac23t$. הווקטור העצמי המתקבל הוא $" + col(r"-\frac23", r"\frac23", 1) + "$.",
        r"**עבור ע״ע $4$:**",
        "$$" + pm("-2&0&-2", "-1&0&0", "0&0&1") + r"\to\dots\to" + pm("1&0&0", "0&0&1", "0&0&0") + "$$",
        r"נסמן $y=t$ ונקבל $x=0,\ z=0$. הווקטור העצמי המתקבל הוא $" + col(0, 1, 0) + "$.",
        r"**עבור ע״ע $6$:**",
        "$$" + pm("0&0&-2", "-1&2&0", "0&0&3") + r"\to\dots\to" + pm("1&-2&0", "0&0&1", "0&0&0") + "$$",
        r"נסמן $y=t$ ונקבל $x=2t,\ z=0$. הווקטור העצמי המתקבל הוא $" + col(2, 1, 0) + "$."),
      8, "c3b"),
    O(3, "ד", "computation", "eigen_diagonalization", r"מצאו את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$.",
      J(r"נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$:",
        "$$D=" + pm("3&0&0", "0&4&0", "0&0&6") + r",\qquad P=" + pm(r"-\frac23&0&2", r"\frac23&1&1", "1&0&0") + "$$"),
      5, "c3b"),

    # ------------------------------------------------------------------ Q4 (official, handwritten)
    O(4, "א", "computation", "vector_spaces", r"מצאו בסיס ומימד של תתי המרחבים $U$ ו-$W$.",
      J(r"פולינום כללי $p(x)\in\mathbb{R}_2[x]$ הוא מהצורה $p(x)=a+bx+cx^2$ עבור $a,b,c\in\mathbb{R}$. ההצגה הווקטורית שלו היא $" + col("a", "b", "c") + "$.",
        r"**$U$:** בהצגה וקטורית תת המרחב $U$ הוא",
        r"$$U=\mathrm{Sp}\left\{" + col(1, 1, 0) + "," + col(2, 0, -1) + "," + col(0, 2, 1) + r"\right\}$$",
        r"קבוצת וקטורים זו מהווה קבוצה יוצרת עבור $U$. על מנת לבנות בסיס ל-$U$, יש לצמצם את הקבוצה עד קבלת קבוצה בלתי תלויה לינארית:",
        "$$" + pm("1&1&0", "2&0&-1", "0&2&1") + arrow(r"R_2\to R_2-2R_1") + pm("1&1&0", "0&-2&-1", "0&2&1") + arrow(r"R_3\to R_3+R_2") + pm("1&1&0", "0&-2&-1", "0&0&0") + "$$",
        r"מכאן, הבסיס ל-$U$: $B_U=\left\{" + col(1, 1, 0) + "," + col(0, 2, 1) + r"\right\}$, ובהצגה פולינומיאלית",
        r"$$B_U=\left\{1+x,\ 2x+x^2\right\},\qquad \dim U=2$$",
        r"**$W$:** בנוגע לתת מרחב $W$, הוא נתון על ידי $p(x)\in\mathbb{R}_2[x]$ כך ש-",
        r"$$p'(x)\big|_{x=1}=b+2cx\big|_{x=1}=b+2c=0$$",
        r"כלומר הם מהצורה",
        r"$$p(x)=a-2cx+cx^2=a+c\left(x^2-2x\right),\quad a,c\in\mathbb{R}$$",
        r"כך ש-$W=\mathrm{Sp}\left\{1,\ x^2-2x\right\}$, או בהצגה וקטורית $W=\mathrm{Sp}\left\{" + col(1, 0, 0) + "," + col(0, -2, 1) + r"\right\}$. "
        r"שני וקטורי הבסיס אינם פרופורציוניים, כתוצאה הם בלתי תלויים. אז הבסיס",
        r"$$B_W=\left\{1,\ x^2-2x\right\},\qquad \dim W=2$$"),
      6, "c4"),
    O(4, "ב", "computation", "vector_spaces", r"חשבו תת מרחב $U+W$, מצאו בסיס ומימד של תת מרחב זה.",
      J(r"$$U+W=\mathrm{Sp}\left\{B_U,B_W\right\}=\mathrm{Sp}\left\{" + col(1, 1, 0) + "," + col(0, 2, 1) + "," + col(1, 0, 0) + "," + col(0, -2, 1) + r"\right\}$$",
        r"נצמצם קבוצה זו עד קבלת קבוצה בלתי תלויה לינארית:",
        "$$" + pm("1&1&0", "0&2&1", "1&0&0", "0&-2&1") + arrow(r"\substack{R_1\to R_1-R_3\\R_4\to R_4+R_2}") + pm("0&1&0", "0&2&1", "1&0&0", "0&0&2")
        + arrow(r"R_2\to R_2-2R_1") + pm("0&1&0", "0&0&1", "1&0&0", "0&0&2") + arrow(r"R_4\to R_4-2R_2") + pm("1&0&0", "0&1&0", "0&0&1", "0&0&0") + "$$",
        r"(בשלב האחרון גם סידור השורות מחדש.) מכאן $B_{U+W}=\left\{" + col(1, 0, 0) + "," + col(0, 1, 0) + "," + col(0, 0, 1) + r"\right\}$, כך ש-",
        r"$$B_{U+W}=\left\{1,\ x,\ x^2\right\},\qquad \dim(U+W)=3$$"),
      8, "c4"),
    O(4, "ג", "computation", "vector_spaces", r"חשבו תת מרחב $U\cap W$, מצאו בסיס ומימד של תת מרחב זה.",
      J(r"מכיוון ש-$B_U=\left\{" + col(1, 1, 0) + "," + col(0, 2, 1) + r"\right\}$ ו-$B_W=\left\{" + col(1, 0, 0) + "," + col(0, -2, 1) + r"\right\}$, "
        r"כל וקטור $\vec v\in U\cap W$ ניתן לכתיבה בצורה:",
        r"$$\vec v=\alpha_1" + col(1, 1, 0) + r"+\alpha_2" + col(0, 2, 1) + r"=-\beta_1" + col(1, 0, 0) + r"-\beta_2" + col(0, -2, 1) + "$$",
        r"לאחר העברת אגפים נקבל את המערכת ההומוגנית",
        r"$$" + pm("1&0&1&0", "1&2&0&-2", "0&1&0&1") + col(r"\alpha_1", r"\alpha_2", r"\beta_1", r"\beta_2") + "=" + col(0, 0, 0) + "$$",
        r"פתרון המערכת:",
        "$$" + pm("1&0&1&0", "1&2&0&-2", "0&1&0&1") + arrow(r"R_2\to R_2-R_1") + pm("1&0&1&0", "0&2&-1&-2", "0&1&0&1")
        + arrow(r"R_2\to R_2-2R_3") + pm("1&0&1&0", "0&0&-1&-4", "0&1&0&1") + arrow(r"R_2\leftrightarrow R_3") + pm("1&0&1&0", "0&1&0&1", "0&0&-1&-4") + "$$",
        r"משתנה חופשי: $\beta_2=t\in\mathbb{R}$, ולכן $\beta_1=-4\beta_2=-4t$. מכאן",
        r"$$\vec v=4t" + col(1, 0, 0) + "-t" + col(0, -2, 1) + "=t" + col(4, 2, -1) + "$$",
        r"לכן $U\cap W=\mathrm{Sp}\left\{" + col(4, 2, -1) + r"\right\}$, ובהצגה פולינומיאלית",
        r"$$B_{U\cap W}=\left\{4+2x-x^2\right\},\qquad \dim(U\cap W)=1$$"),
      8, "c4"),
    O(4, "ד", "computation", "vector_spaces", r"יהי $q(x)$ פולינום כלשהו השייך לתת מרחב $U\cap W$. מצאו $q(2)+q(-2)$.",
      J(r"לכל פולינום השייך ל-$U\cap W$ יש צורה $q(x)=c\left(4+2x-x^2\right)$ כאשר $c\in\mathbb{R}$. אז:",
        r"$$q(x)+q(-x)=c\left(4+2x-x^2\right)+c\left(4-2x-x^2\right)=2c\left(4-x^2\right)$$",
        r"כתוצאה,",
        r"$$q(2)+q(-2)=0$$"),
      3, "c4"),

    # ------------------------------------------------------------------ Q5
    O(5, "א", "proof", "linear_maps", r"הוכיחו כי $T$ היא העתקה לינארית.",
      J(r"נסמן $A=" + M2("a_1", "b_1", "c_1", "d_1") + r"$, $B=" + M2("a_2", "b_2", "c_2", "d_2") + r"$. אז $A+B=" + M2("a_1+a_2", "b_1+b_2", "c_1+c_2", "d_1+d_2") + "$ ו-",
        r"$$T(A+B)=T" + M2("a_1+a_2", "b_1+b_2", "c_1+c_2", "d_1+d_2") + "=" + col("a_1+a_2+b_1+b_2", "b_1+b_2+c_1+c_2", "b_1+b_2+d_1+d_2") + "="
        + col("a_1+b_1", "b_1+c_1", "b_1+d_1") + "+" + col("a_2+b_2", "b_2+c_2", "b_2+d_2") + "=T(A)+T(B)$$",
        r"בנוסף, $\alpha A=" + M2(r"\alpha a_1", r"\alpha b_1", r"\alpha c_1", r"\alpha d_1") + "$ ו-",
        r"$$T(\alpha A)=T" + M2(r"\alpha a_1", r"\alpha b_1", r"\alpha c_1", r"\alpha d_1") + "=" + col(r"\alpha a_1+\alpha b_1", r"\alpha b_1+\alpha c_1", r"\alpha b_1+\alpha d_1")
        + r"=\alpha" + col("a_1+b_1", "b_1+c_1", "b_1+d_1") + r"=\alpha T(A)$$",
        r"ולכן העתקה $T$ היא לינארית."),
      6, "c5"),
    O(5, "ב", "computation", "linear_maps", r"מצאו את הבסיסים והמימדים של $\mathrm{Ker}(T)$ ו-$\mathrm{Im}(T)$.",
      J(r"אם $A=" + M2("a", "b", "c", "d") + r"\in\ker(T)$, אז",
        r"$$T(A)=T" + M2("a", "b", "c", "d") + "=" + col(0, 0, 0) + r"\ \Rightarrow\ \begin{cases}a+b=0\\b+c=0\\b+d=0\end{cases}$$",
        "$$" + pm("1&1&0&0", "0&1&1&0", "0&1&0&1") + r"\to" + pm("1&1&0&0", "0&1&1&0", "0&0&-1&1") + r"\to" + pm("1&1&0&0", "0&1&0&1", "0&0&-1&1") + r"\to" + pm("1&0&0&-1", "0&1&0&1", "0&0&1&-1") + "$$",
        r"המשוואות המתאימות לצורה המדורגת כאן הן $a-d=0,\ b+d=0,\ c-d=0$, ולכן $d=t,\ a=t,\ b=-t,\ c=t$, והפתרון מתקבל בצורה $" + M2("t", "-t", "t", "t") + "=t" + M2(1, -1, 1, 1) + "$. "
        r"במילים אחרות, $A\in\ker(T)$ אם ורק אם היא בעלת הצורה $t" + M2(1, -1, 1, 1) + "$. סיכום:",
        r"$$\ker(T)=\mathrm{Sp}\left\{" + M2(1, -1, 1, 1) + r"\right\},\qquad \dim(\ker(T))=1$$",
        r"**נעבור אל התמונה של $T$:**",
        r"$$T" + M2("a", "b", "c", "d") + "=" + col("a+b", "b+c", "b+d") + "=a" + col(1, 0, 0) + "+b" + col(1, 1, 1) + "+c" + col(0, 1, 0) + "+d" + col(0, 0, 1) + "$$",
        r"ומכאן נובע ש-$\mathrm{Im}(T)=\mathrm{Sp}\left\{" + col(1, 0, 0) + "," + col(1, 1, 1) + "," + col(0, 1, 0) + "," + col(0, 0, 1) + r"\right\}$, כלומר קבוצת וקטורים זו מהווה קבוצה פורשת עבור התמונה. "
        r"ברור שאחד הווקטורים בקבוצה הזאת מיותר, והבסיס עבור התמונה ניתן לקחת בצורה",
        r"$$\left\{" + col(1, 0, 0) + "," + col(1, 1, 1) + "," + col(0, 1, 0) + r"\right\},\qquad \dim(\mathrm{Im}(T))=3$$"),
      9, "c5"),
    O(5, "ג", "computation", "linear_maps", r"האם $T$ חד-חד ערכית? האם היא על? נמקו את תשובתכם.",
      J(r"מכיוון ש-$\dim(\ker(T))=1$, אז $\ker(T)\neq\{0\}$, ולכן $T$ אינה חד-חד-ערכית.",
        r"מכיוון ש-$\dim(\mathrm{Im}(T))=3$, אז $\mathrm{Im}(T)=\mathbb{R}^3$, ולכן $T$ היא העתקת על."),
      3, "c5"),
    O(5, "ד", "computation", "linear_maps",
      r"מצאו את כל המטריצות ב-$\mathbb{M}_2(\mathbb{R})$ שתמונתם נותנת וקטור $" + pm("1", "1", "1") + r"$. האם הן מהוות תת מרחב של $\mathbb{M}_2(\mathbb{R})$?",
      J(r"$$T(A)=T" + M2("a", "b", "c", "d") + "=" + col(1, 1, 1) + r"\ \Rightarrow\ \begin{cases}a+b=1\\b+c=1\\b+d=1\end{cases}$$",
        "$$" + aug([[1, 1, 0, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 1, 1]], 4) + r"\to" + aug([[1, 1, 0, 0, 1], [0, 1, 1, 0, 1], [0, 0, -1, 1, 0]], 4)
        + r"\Rightarrow\begin{cases}a+b=1\\b+c=1\\-c+d=0\\d=t\end{cases}\Rightarrow\begin{cases}a=t\\b=1-t\\c=t\\d=t\end{cases}$$",
        r"לכן, כל המטריצות ב-$\mathbb{M}_2(\mathbb{R})$ שתמונתן היא $" + col(1, 1, 1) + "$ הן מטריצות בעלות הצורה",
        r"$$A=" + M2("a", "b", "c", "d") + "=" + M2("t", "1-t", "t", "t") + "=" + M2("t", "-t", "t", "t") + "+" + M2(0, 1, 0, 0) + "=t" + M2(1, -1, 1, 1) + "+" + M2(0, 1, 0, 0) + "$$",
        r"לא קשה לראות שהקבוצה הזאת אינה מכילה בתוכה מטריצת אפסים, ולכן אינה מהווה תת מרחב של $\mathbb{M}_2(\mathbb{R})$."),
      7, "c5"),
]

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
    rubric=rub((r"פירוק $AA^T+A^2=A\left(A^T+A\right)$ מוציא את $A$ כגורם משמאל", 3),
               (r"חלוקה ב-$3$: $A\cdot\frac13\left(A+A^T\right)=I$", 2),
               (r"מסקנה: מטריצה ריבועית $X$ עם $AX=I$ היא ההפוכה, ולכן $A^{-1}=\frac13\left(A+A^T\right)$", 2)),
    pitfalls=[r"לפרק $AA^T+A^2$ בצורה $A\left(A^T+A^2\right)$ ולשכוח שהגורם $A$ מוכפל ב-$A$ ולא ב-$A^2$.",
              r"להניח ש-$A$ סימטרית כבר בסעיף זה ולכתוב $AA^T=A^2$ בלי הצדקה."],
    steps=[
        odr("סדרו את שלבי הפתרון.",
            [r"$AA^T+A^2=3I$",
             r"$A\left(A^T+A\right)=3I$",
             r"$A\cdot\frac13\left(A+A^T\right)=I$",
             r"$A^{-1}=\frac13\left(A+A^T\right)$"],
            "פירוק לגורמים, חלוקה ב-3, ומסקנה מהגדרת ההפוכה."),
        fnd("בחישוב הבא שורה אחת שגויה. מצאו אותה.",
            [r"$AA^T+A^2=3I$",
             r"$A\left(A^T+A^2\right)=3I$",
             r"$A\cdot\frac13\left(A+A^T\right)=I$",
             r"$A^{-1}=\frac13\left(A+A^T\right)$"], 1,
            r"הוצאת $A$ מ-$A^2$ משאירה $A$, לא $A^2$: $A\cdot A^2=A^3\neq A^2$."),
    ])

ENR[(1, "ב")] = dict(
    rubric=rub((r"שחלוף שני האגפים של $A^{-1}=\frac13\left(A+A^T\right)$", 2),
               (r"שחלוף סכום וכפל בסקלר: $\left(\frac13(A+A^T)\right)^T=\frac13A^T+\frac13\left(A^T\right)^T$", 2),
               (r"$\left(A^T\right)^T=A$", 2),
               (r"מסקנה: $\left(A^{-1}\right)^T=A^{-1}$, כלומר $A^{-1}$ סימטרית", 1)),
    pitfalls=[r"לשכוח ש-$\left(A^T\right)^T=A$ ולהשאיר $A^T+A^T$.",
              r"לחשב $\left(A^{-1}\right)^T=\left(A^T\right)^{-1}$ ולעצור שם בלי להשוות ל-$A^{-1}$."],
    steps=[
        odr("סדרו את שלבי החישוב.",
            [r"$\left(A^{-1}\right)^T=\left(\frac13\left(A+A^T\right)\right)^T$",
             r"$=\frac13A^T+\frac13\left(A^T\right)^T$",
             r"$=\frac13\left(A^T+A\right)$",
             r"$=A^{-1}$"],
            "שחלוף של הביטוי מסעיף א, שחלוף איבר איבר, ואז זיהוי $A^{-1}$."),
        fnd("בחישוב הבא שורה אחת שגויה. מצאו אותה.",
            [r"$\left(A^{-1}\right)^T=\left(\frac13\left(A+A^T\right)\right)^T$",
             r"$=\frac13A^T+\frac13A^T$",
             r"$=\frac13\left(A^T+A\right)$",
             r"$=A^{-1}$"], 1,
            r"$\left(A^T\right)^T=A$ ולא $A^T$; אחרת השורה הבאה אינה נובעת."),
    ])

ENR[(1, "ג")] = dict(
    rubric=rub((r"חיסור המשוואות נותן $2A^2=3I$", 2),
               (r"דטרמיננטה של שני האגפים: $2^3|A|^2=3^3$", 2),
               (r"$|A|^2=\frac{27}{8}$", 1),
               (r"$|A|=\pm\frac{3\sqrt6}{4}$ ושני הסימנים אפשריים", 2)),
    pitfalls=[r"להוציא שורש ולכתוב רק $|A|=+\sqrt{\frac{27}{8}}$, למרות ש-$A=-\sqrt{\frac32}I$ מקיימת את המשוואות.",
              r"לכתוב $|2A^2|=2|A|^2$ במקום $2^3|A|^2$ (המטריצה מסדר $3\times3$)."],
    steps=[
        num(r"מהי $\det(3I)$ עבור $I$ מסדר $3\times3$?", 27, "$3^3=27$."),
        num(r"מהו $|A|^2$?", 3.375, r"$2^3|A|^2=27$, כלומר $|A|^2=\frac{27}{8}$.", 0.0001),
        num(r"מהו הערך החיובי של $|A|$ בקירוב (טולרנס 0.001)?", 1.8371, r"$\sqrt{\frac{27}{8}}=\frac{3\sqrt6}{4}$.", 0.001),
        cho(r"אילו ערכים אפשריים ל-$|A|$?", r"שני הערכים $\pm\frac{3\sqrt6}{4}$",
            [r"רק הערך החיובי $\frac{3\sqrt6}{4}$", r"רק הערך השלילי $-\frac{3\sqrt6}{4}$", r"הערך $0$"],
            r"גם $A=\sqrt{\frac32}I$ וגם $A=-\sqrt{\frac32}I$ מקיימות את שתי המשוואות, ודטרמיננטותיהן הן בסימנים הפוכים."),
    ])

ENR[(1, "ד")] = dict(
    rubric=rub((r"$\left|A^{-1}\right|=|A|^{-1}$ כי $A$ הפיכה", 2),
               (r"הצבת $|A|=\pm\frac{3\sqrt6}{4}$", 1),
               (r"התוצאה $\pm\frac{2\sqrt6}{9}$ באותו סימן כמו $|A|$", 1)),
    pitfalls=[r"לכתוב $\left|A^{-1}\right|=-|A|$ או $|A|$ במקום ההופכי.",
              r"להשמיט את הסימן השלילי האפשרי."],
    steps=[
        num(r"מהו $\left|A^{-1}\right|^2$ בקירוב (טולרנס 0.001)?", 0.2963, r"$\frac{8}{27}$.", 0.001),
        num(r"מהו הערך החיובי של $\left|A^{-1}\right|$ בקירוב (טולרנס 0.001)?", 0.5443, r"$\sqrt{\frac{8}{27}}=\frac{2\sqrt6}{9}$.", 0.001),
        cho(r"מה הקשר בין הסימן של $\left|A^{-1}\right|$ לסימן של $|A|$?", "אותו סימן",
            ["סימן הפוך", "תמיד חיובי", "תמיד שלילי"],
            r"$\left|A^{-1}\right|=\frac1{|A|}$ ולכן הסימנים זהים; עבור $A=-\sqrt{\frac32}I$ שניהם שליליים."),
    ])

ENR[(2, "א")] = dict(
    rubric=rub((r"$R_2\to R_2-aR_1$ ו-$R_3\to R_3-R_1$", 2),
               (r"$R_3\to R_3-R_2$ נותן שורה $\left(0,0,-(a+1)(a-2)\mid(a+1)(a-1)\right)$", 2),
               (r"המקרה $a=-1$: שתי שורות אפסים", 1),
               (r"המקרה $a=2$: שורה $(0,0,0\mid3)$", 1),
               (r"עבור $a\neq-1,2$: הצורה הקנונית עם עמודה אחרונה $\frac{1-a}{a-2},\ \frac1{a-2},\ \frac{1-a}{a-2}$", 3)),
    pitfalls=[r"לחלק ב-$a+1$ בלי לטפל בנפרד במקרה $a=-1$.",
              r"לחלק ב-$(a+1)(a-2)$ בלי לטפל במקרה $a=2$."],
    steps=[
        num(r"עבור $a=3$, מהי הכניסה בעמודה 2 של שורה 2 אחרי $R_2\to R_2-aR_1$ (הביטוי $1+a$)?", 4, "$1+3=4$."),
        num(r"עבור $a=3$, מהו המקדם $-(a+1)(a-2)$ של $z$ בשורה 3?", -4, "$-(4)(1)=-4$."),
        num(r"עבור $a=3$, מהו $x$ בפתרון היחיד?", -2, r"$\frac{1-a}{a-2}=\frac{-2}{1}$."),
        num(r"עבור $a=3$, מהו $y$ בפתרון היחיד?", 1, r"$\frac1{a-2}=1$."),
    ])

ENR[(2, "ב")] = dict(
    rubric=rub((r"$a=-1$: שורות אפסים ולכן אינסוף פתרונות", 2),
               (r"$a=2$: שורת סתירה $(0,0,0\mid3)$ ולכן אין פתרון", 2),
               (r"שאר הערכים: פתרון יחיד", 2),
               (r"הפתרון היחיד $\left(\frac{1-a}{a-2},\frac1{a-2},\frac{1-a}{a-2}\right)$", 2)),
    pitfalls=[r"לבלבל בין המקרים: שורת סתירה ב-$a=2$ ולא ב-$a=-1$.",
              r"לשכוח שב-$a=-1$ גם אגף ימין מתאפס ולכן אין סתירה."],
    steps=[
        num(r"מהי דרגת מטריצת המקדמים עבור $a=-1$?", 1, "נשארת שורה אחת שאינה אפס."),
        num(r"מהי דרגת המטריצה המורחבת עבור $a=2$? (דרגת מטריצת המקדמים היא 2)", 3, "השורה $(0,0,0\\mid3)$ מוסיפה דרגה."),
        cho("איזה מיפוי נכון?", r"אינסוף פתרונות: $a=-1$; אין פתרון: $a=2$; פתרון יחיד: כל שאר הערכים",
            [r"אינסוף פתרונות: $a=2$; אין פתרון: $a=-1$; פתרון יחיד: כל שאר הערכים",
             r"אין פתרון: $a=-1$ וגם $a=2$; פתרון יחיד: כל שאר הערכים",
             r"אינסוף פתרונות: $a=-1$ וגם $a=2$; פתרון יחיד: כל שאר הערכים"],
            r"ב-$a=-1$ דרגת המקדמים והמורחבת שוות 1 (פחות מ-3), וב-$a=2$ דרגת המקדמים 2 והמורחבת 3."),
    ])

ENR[(2, "ג")] = dict(
    rubric=rub((r"הצבת $a=-1$ ומשוואה יחידה $x-y+z=-1$", 1),
               (r"המשתנים החופשיים $y=t,\ z=s$", 1),
               (r"$x=t-s-1$", 1),
               (r"כתיבה וקטורית עם וקטורי כיוון $(1,1,0)$ ו-$(-1,0,1)$ ווקטור מקום $(-1,0,0)$", 1)),
    pitfalls=[r"לכתוב את וקטור הכיוון של $s$ בצורה $(0,-1,1)$; הוא אינו פותר את $x-y+z=0$.",
              r"לשכוח את הווקטור הפרטי $(-1,0,0)$ ולתאר את מרחב הפתרונות כתת מרחב."],
    steps=[
        num(r"כמה משתנים חופשיים יש כאשר $a=-1$?", 2, "משוואה אחת בשלושה נעלמים."),
        num(r"עבור $t=2,\ s=1$, מהו $x$?", 0, "$x=t-s-1=2-1-1$."),
        cho(r"מהו וקטור הכיוון של $s$?", r"$(-1,0,1)$",
            [r"$(0,-1,1)$", r"$(1,0,1)$", r"$(-1,0,-1)$"],
            r"הוא צריך לפתור את $x-y+z=0$: רק $(-1,0,1)$ עושה זאת; ב-$(0,-1,1)$ מקבלים $2$, ב-$(1,0,1)$ מקבלים $2$, וב-$(-1,0,-1)$ מקבלים $-2$."),
    ])

ENR[(2, "ד")] = dict(
    rubric=rub((r"פירוק $z^4+8z=z\left(z^3+8\right)$", 1),
               (r"הפתרון $z=0$", 1),
               (r"שורשי $z^3=-8$ לפי נוסחת השורשים בהצגה קוטבית", 1),
               (r"שלושת השורשים $1+\sqrt3\,i,\ -2,\ 1-\sqrt3\,i$", 1)),
    pitfalls=[r"לשכוח את הפתרון $z=0$ ולהסתפק בשלושה שורשים.",
              r"לחשב שורשי $z^3=8$ במקום $z^3=-8$ (זווית ההתחלה $\frac\pi3$ ולא $0$)."],
    steps=[
        num(r"מהו המודול של כל פתרון שונה מאפס?", 2, r"$|z|^3=8$."),
        num("כמה פתרונות מרוכבים שונים יש למשוואה?", 4, r"$0$ ועוד שלושת שורשי $z^3=-8$."),
        num(r"מהו החלק המדומה של $z_0=1+\sqrt3\,i$ בקירוב (טולרנס 0.001)?", 1.732, r"$2\sin\frac\pi3=\sqrt3$.", 0.001),
    ])

ENR[(3, "א")] = dict(
    rubric=rub((r"$A$ הפיכה אם ורק אם $|A|\neq0$", 1),
               (r"חישוב הדטרמיננטה בפיתוח לפי שורה ראשונה: $-36a^2+30a+84$", 3),
               (r"השורשים $a=2$ ו-$a=-\frac76$", 1),
               (r"מסקנה: $A$ הפיכה עבור $a\neq2,-\frac76$", 1)),
    pitfalls=[r"טעות סימן באחד הצמצומים בפיתוח לפי שורה, למשל $2a(2a+2-20a+10)$.",
              r"לקבוע שהמטריצה הפיכה בדיוק כאשר $|A|=0$ (הפוך)."],
    steps=[
        num(r"מהי $|A|$ עבור $a=0$?", 84, "ממשוואת הדטרמיננטה $-36a^2+30a+84$."),
        num(r"מהי $|A|$ עבור $a=1$?", 78, "$-36+30+84$."),
        num(r"מהו ערך $a$ השני (השלילי) שבו $|A|=0$ בקירוב (טולרנס 0.001)?", -1.1667, r"$-\frac76$.", 0.001),
    ])

ENR[(3, "ג")] = dict(
    rubric=rub((r"פולינום אופייני $(\lambda-3)(\lambda-6)(\lambda-4)$ והערכים העצמיים $3,4,6$", 3),
               (r"ערכים עצמיים שונים ולכן $B$ לכסינה", 1),
               (r"וקטור עצמי עבור $3$: $\left(-\frac23,\frac23,1\right)$", 2),
               (r"וקטור עצמי עבור $4$: $(0,1,0)$", 1),
               (r"וקטור עצמי עבור $6$: $(2,1,0)$", 1)),
    pitfalls=[r"לשכוח שהשורה השלישית של $\lambda I-B$ נותנת את הגורם $(\lambda-3)$ ולהתבלבל בפיתוח.",
              r"לכתוב את הווקטור העצמי של $3$ בלי לבדוק $Bv=3v$."],
    steps=[
        num(r"מהו עקבת $B$ (סכום האלכסון)?", 13, r"$6+4+3$, שווה לסכום הערכים העצמיים."),
        num(r"מהי $\det B$?", 72, r"$3\cdot4\cdot6$."),
        num(r"בווקטור העצמי של $3$ עם $z=3$, מהו $x$?", -2, r"$x=-\frac23z$."),
        cho(r"איזה וקטור הוא וקטור עצמי של $B$ עבור הערך העצמי $4$?", r"$(0,1,0)$",
            [r"$(0,0,1)$", r"$(1,0,0)$", r"$(1,1,0)$"],
            r"$B(0,1,0)=(0,4,0)$. עבור $(0,0,1)$ מקבלים $(2,0,3)$, עבור $(1,0,0)$ מקבלים $(6,1,0)$, ועבור $(1,1,0)$ מקבלים $(6,5,0)$."),
    ])

ENR[(3, "ד")] = dict(
    rubric=rub((r"$D$ אלכסונית עם הערכים העצמיים $3,4,6$ על האלכסון", 2),
               (r"עמודות $P$ הן הווקטורים העצמיים באותו סדר כמו ב-$D$", 2),
               (r"$P$ הפיכה כי הווקטורים בלתי תלויים (ערכים עצמיים שונים)", 1)),
    pitfalls=[r"לסדר את עמודות $P$ בסדר שונה מסדר הערכים העצמיים ב-$D$.",
              r"לרשום את $P$ כמטריצת שורות במקום עמודות."],
    steps=[
        num(r"מהו $d_{33}$ ב-$D$ (הסדר הוא $3,4,6$)?", 6, "הערך העצמי השלישי."),
        num(r"מהי $\det P$ עבור $P=\begin{pmatrix}-\frac23&0&2\\\frac23&1&1\\1&0&0\end{pmatrix}$?", -2, "פיתוח לפי העמודה השנייה: $1\\cdot\\left(0-2\\right)$."),
        cho(r"אם $D=\mathrm{diag}(3,4,6)$, מהי העמודה השנייה של $P$?", r"$(0,1,0)$",
            [r"$(2,1,0)$", r"$\left(-\frac23,\frac23,1\right)$", r"$(0,0,1)$"],
            r"היא צריכה להיות וקטור עצמי של $4$. $(2,1,0)$ הוא של $6$, $\left(-\frac23,\frac23,1\right)$ של $3$, ו-$(0,0,1)$ אינו עצמי כלל."),
    ])

ENR[(4, "א")] = dict(
    rubric=rub((r"הצגה וקטורית של היוצרים של $U$ ודירוג: דרגה 2", 2),
               (r"בסיס $U$: $\{1+x,\ 2x+x^2\}$ ו-$\dim U=2$", 1),
               (r"תנאי $W$: $p'(1)=b+2c=0$", 1),
               (r"בסיס $W$: $\{1,\ x^2-2x\}$", 1),
               (r"$\dim W=2$ כי שני הווקטורים אינם פרופורציוניים", 1)),
    pitfalls=[r"לחשב $p'(1)$ בלי להציב $x=1$ ולקבל $b+2cx=0$.",
              r"לקחת את שלושת היוצרים של $U$ כבסיס למרות שהם תלויים."],
    steps=[
        num(r"מהי דרגת המטריצה שעמודותיה (או שורותיה) הן $(1,1,0),(2,0,-1),(0,2,1)$?", 2, "הצורה המדורגת כוללת שורת אפסים."),
        num(r"$2-x^2=\alpha(1+x)+\beta(2x+x^2)$. מהו $\alpha$?", 2, r"מהמקדם החופשי $\alpha=2$, ואז $\beta=-1$."),
        num(r"עבור $p=a+bx+cx^2\in W$ עם $c=3$, מהו $b$?", -6, "$b=-2c$."),
        num(r"מהו $\dim W$?", 2, "שני פרמטרים חופשיים, $a$ ו-$c$."),
    ])

ENR[(4, "ב")] = dict(
    rubric=rub((r"$U+W=\mathrm{Sp}\{B_U,B_W\}$", 2),
               (r"דירוג ארבעת הווקטורים", 3),
               (r"קבלת שלוש שורות בת״ל ושורת אפסים", 1),
               (r"בסיס $\{1,x,x^2\}$ ו-$\dim(U+W)=3$", 2)),
    pitfalls=[r"לקחת את ארבעת הווקטורים כבסיס בלי לבדוק תלות.",
              r"לחשוב ש-$U+W$ היא האיחוד $U\cup W$."],
    steps=[
        num(r"מהי הדרגה של המטריצה שעמודותיה $(1,1,0),(0,2,1),(1,0,0),(0,-2,1)$?", 3, "הצורה המדורגת מכילה שלוש שורות שאינן אפס."),
        num(r"מהו $\dim(U+W)$?", 3, "הדרגה."),
        cho(r"מדוע $U+W=\mathbb{R}_2[x]$?", r"כי $\dim(U+W)=3$ והוא תת מרחב של מרחב ממימד $3$",
            [r"כי $U=W$", r"כי $U+W=U\cup W$", r"כי $U\cap W=\{0\}$"],
            r"$U\neq W$ (למשל $1\in W\setminus U$), האיחוד אינו סגור לחיבור ($2+x$ אינו ב-$U$ ואינו ב-$W$), ו-$\dim(U\cap W)=1$."),
    ])

ENR[(4, "ג")] = dict(
    rubric=rub((r"השוואת צירוף של $B_U$ לצירוף של $B_W$", 2),
               (r"מערכת הומוגנית מסדר $3\times4$ ודירוגה", 2),
               (r"$\beta_1=-4\beta_2$ ומשתנה חופשי $\beta_2=t$", 2),
               (r"$U\cap W=\mathrm{Sp}\{4+2x-x^2\}$, מימד $1$", 2)),
    pitfalls=[r"לקחת את שני הבסיסים כמערכת אחת בלי להעביר אגף, ולכן לקבל סימנים שגויים.",
              r"לשכוח שבסיס החיתוך הוא הווקטור עצמו ולא הפרמטרים $\alpha,\beta$."],
    steps=[
        num(r"מהי דרגת המערכת ההומוגנית $3\times4$ בנעלמים $\alpha_1,\alpha_2,\beta_1,\beta_2$?", 3, "ארבעה נעלמים ופתרון עם פרמטר אחד."),
        num(r"עבור $\beta_2=1$, מהו $\beta_1$?", -4, r"$\beta_1=-4\beta_2$."),
        num(r"מהו מקדם $x^2$ בווקטור הבסיס של $U\cap W$ (עבור $t=1$)?", -1, r"$4+2x-x^2$."),
        cho(r"איזה פולינום שייך ל-$U\cap W$?", r"$4+2x-x^2$",
            [r"$1+x$", r"$1$", r"$x^2-2x$"],
            r"$1+x\in U$ אך $b+2c=1\neq0$ ולכן לא ב-$W$; $1\in W$ אך לא ב-$U$; $x^2-2x\in W$ אך אינו צירוף של $B_U$ (המקדם של $x$ היה צריך להיות $2$)."),
    ])

ENR[(4, "ד")] = dict(
    rubric=rub((r"כל $q\in U\cap W$ הוא $q(x)=c\left(4+2x-x^2\right)$", 1),
               (r"$q(2)=4c$ ו-$q(-2)=-4c$", 1),
               (r"הסכום $q(2)+q(-2)=0$", 1)),
    pitfalls=[r"להניח $c=1$ ולא לראות שהתוצאה אפס לכל $c$."],
    steps=[
        num(r"עבור $c=1$, מהו $q(2)$?", 4, "$4+4-4$."),
        num(r"עבור $c=1$, מהו $q(-2)$?", -4, "$4-4-4$."),
        num(r"מהו $q(2)+q(-2)$ עבור $c=7$?", 0, "$28-28$."),
    ])

ENR[(5, "א")] = dict(
    rubric=rub((r"חיבור: הצבת $A+B$ בהגדרת $T$", 2),
               (r"פירוק לסכום $T(A)+T(B)$", 1),
               (r"כפל בסקלר: הצבת $\alpha A$", 2),
               (r"הוצאת $\alpha$ ומסקנה: $T$ לינארית", 1)),
    pitfalls=[r"לבדוק את התנאים רק על דוגמה מספרית.",
              r"לשכוח אחד משני התנאים (חיבור או כפל בסקלר)."],
    steps=[
        odr("סדרו את שלבי הוכחת החיבור.",
            [r"$T(A+B)=T\begin{pmatrix}a_1+a_2&b_1+b_2\\c_1+c_2&d_1+d_2\end{pmatrix}$",
             r"$=\begin{pmatrix}(a_1+a_2)+(b_1+b_2)\\(b_1+b_2)+(c_1+c_2)\\(b_1+b_2)+(d_1+d_2)\end{pmatrix}$",
             r"$=\begin{pmatrix}a_1+b_1\\b_1+c_1\\b_1+d_1\end{pmatrix}+\begin{pmatrix}a_2+b_2\\b_2+c_2\\b_2+d_2\end{pmatrix}$",
             r"$=T(A)+T(B)$"],
            "הצבה, הגדרת $T$, פירוק לסכום, וזיהוי."),
        fnd("בחישוב הבא שורה אחת שגויה. מצאו אותה.",
            [r"$T(A+B)=T\begin{pmatrix}a_1+a_2&b_1+b_2\\c_1+c_2&d_1+d_2\end{pmatrix}$",
             r"$=\begin{pmatrix}(a_1+a_2)+(b_1+b_2)\\(b_1+b_2)+(c_1+c_2)\\(b_1+b_2)(d_1+d_2)\end{pmatrix}$",
             r"$=\begin{pmatrix}a_1+b_1\\b_1+c_1\\b_1+d_1\end{pmatrix}+\begin{pmatrix}a_2+b_2\\b_2+c_2\\b_2+d_2\end{pmatrix}$",
             r"$=T(A)+T(B)$"], 1,
            r"הרכיב השלישי של $T$ הוא $b+d$ (סכום) ולא מכפלה."),
        num(r"עבור $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, מהו הרכיב השני של $T(2A)$?", 10, r"$T(2A)=2T(A)$ ו-$T(A)=(3,5,6)$, כלומר $2\cdot5$."),
    ])

ENR[(5, "ב")] = dict(
    rubric=rub((r"הגרעין: מערכת $a+b=0,\ b+c=0,\ b+d=0$", 1),
               (r"דירוג, משתנה חופשי $d=t$ והפתרון $t\begin{pmatrix}1&-1\\1&1\end{pmatrix}$", 2),
               (r"בסיס הגרעין ו-$\dim\ker T=1$", 2),
               (r"התמונה נפרשת על ידי $(1,0,0),(1,1,1),(0,1,0),(0,0,1)$", 2),
               (r"בסיס התמונה $\{(1,0,0),(1,1,1),(0,1,0)\}$ ו-$\dim\mathrm{Im}\,T=3$", 2)),
    pitfalls=[r"לקחת את ארבעת הווקטורים הפורשים כבסיס התמונה: $(1,1,1)=(1,0,0)+(0,1,0)+(0,0,1)$.",
              r"לשכוח שהגרעין הוא מטריצות ולא וקטורים ב-$\mathbb{R}^3$."],
    steps=[
        cho(r"איזו מטריצה שייכת ל-$\ker T$?", r"$\begin{pmatrix}1&-1\\1&1\end{pmatrix}$",
            [r"$\begin{pmatrix}1&1\\1&1\end{pmatrix}$", r"$\begin{pmatrix}-1&1\\1&1\end{pmatrix}$", r"$\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$"],
            r"הנכונה נותנת $(0,0,0)$. האחרות נותנות $(2,2,2)$, $(0,2,2)$ ו-$(0,-2,0)$."),
        num(r"מהו $\dim\ker T$?", 1, "משתנה חופשי יחיד."),
        num(r"מהו $\dim\mathrm{Im}\,T$?", 3, "ארבעה וקטורים פורשים, אחד מיותר."),
        num(r"מהו הרכיב הראשון של $T\begin{pmatrix}1&-1\\1&1\end{pmatrix}$?", 0, "$a+b=1-1$."),
    ])

ENR[(5, "ג")] = dict(
    rubric=rub((r"$\ker T\neq\{0\}$ ולכן $T$ אינה חד-חד-ערכית", 1),
               (r"$\dim\mathrm{Im}\,T=3=\dim\mathbb{R}^3$ ולכן $T$ על", 1),
               (r"עקביות עם משפט המימדים: $1+3=4=\dim\mathbb{M}_2(\mathbb{R})$", 1)),
    pitfalls=[r"לטעון ש-$T$ אינה על כי $\dim\mathbb{M}_2(\mathbb{R})=4>3$; העתקה ממרחב גדול יותר יכולה להיות על."],
    steps=[
        cho("מהי המסקנה הנכונה?", "אינה חד-חד-ערכית, אך על",
            ["חד-חד-ערכית ועל", "חד-חד-ערכית אך לא על", "לא חד-חד-ערכית ולא על"],
            r"$\dim\ker T=1>0$ (לא חד-חד), ו-$\dim\mathrm{Im}\,T=3=\dim\mathbb{R}^3$ (על)."),
        cho("מה מוכיח ש-$T$ על?", r"$\dim\mathrm{Im}\,T=3=\dim\mathbb{R}^3$",
            [r"$\dim\ker T=1$", r"$\dim\mathbb{M}_2(\mathbb{R})=4>3$", r"$T$ לינארית"],
            r"הגרעין הלא טריוויאלי מראה שאינה חד-חד; מימד התחום גדול מ-3 אינו מבטיח על (למשל ההעתקה האפס); לינאריות אינה מבטיחה על."),
    ])

ENR[(5, "ד")] = dict(
    rubric=rub((r"המערכת $a+b=1,\ b+c=1,\ b+d=1$", 1),
               (r"דירוג המטריצה המורחבת", 2),
               (r"הפתרון הכללי $a=t,\ b=1-t,\ c=t,\ d=t$", 2),
               (r"צורה וקטורית: $t\begin{pmatrix}1&-1\\1&1\end{pmatrix}+\begin{pmatrix}0&1\\0&0\end{pmatrix}$", 1),
               (r"מטריצת האפס אינה בקבוצה ולכן אינה תת מרחב", 1)),
    pitfalls=[r"לטעון שהקבוצה תת מרחב כי היא כוללת פרמטר חופשי.",
              r"לשכוח את הווקטור הפרטי $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ ולהחזיר את הגרעין."],
    steps=[
        num(r"עבור $t=2$, מהו $b$ במטריצה בקבוצה?", -1, "$b=1-t$."),
        num(r"מהו הרכיב הראשון של $T$ של מטריצת האפס?", 0, r"אבל הרכיב הראשון הנדרש הוא $1$, ולכן $0$ אינה בקבוצה."),
        cho("איזו קבוצה היא קבוצת כל המטריצות שתמונתן $(1,1,1)$?",
            r"$\left\{t\begin{pmatrix}1&-1\\1&1\end{pmatrix}+\begin{pmatrix}0&1\\0&0\end{pmatrix}\right\}$",
            [r"$\left\{t\begin{pmatrix}1&-1\\1&1\end{pmatrix}\right\}$",
             r"$\left\{t\begin{pmatrix}1&-1\\1&1\end{pmatrix}+\begin{pmatrix}1&0\\0&0\end{pmatrix}\right\}$",
             r"$\left\{t\begin{pmatrix}1&1\\1&1\end{pmatrix}+\begin{pmatrix}0&1\\0&0\end{pmatrix}\right\}$"],
            r"הגרעין בלבד נותן $(0,0,0)$; הווקטור הפרטי $\begin{pmatrix}1&0\\0&0\end{pmatrix}$ נותן $(1,0,0)$; ו-$\begin{pmatrix}1&1\\1&1\end{pmatrix}$ אינה בגרעין ולכן מתקבל $(1+2t,1+2t,1+2t)$ ולא תמיד $(1,1,1)$."),
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
    "examCode": "21A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״א, מועד א׳ (24.01.2021)",
    "year": 2021,
    "examDate": "24.01.2021",
    "sourceFile": "21A-A exam (PDF, 3pp, exam only)",
    "solutionFile": "none",
    "contexts": contexts,
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
