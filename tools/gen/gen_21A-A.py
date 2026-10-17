# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-A.json -- linear algebra, semester A 2021, moed A (24.01.2021), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-A.py

Source: one PDF (3pp, exam only; page 3 is blank). There is NO answer source for this sitting (GATE1: 21A-A has no
solution), so every item was held "no-key" and then solved by the solver (solutionSource "solved", official false,
checked in tools/verify/21A-A/verify_21A-A.py). Q3 b stays held: A is singular at the printed a=2 (det A=-6(a-2)(6a+7)).
Q1 c/d: the data fix |A|^2=27/8 only; both signs occur (A=+-sqrt(3/2) I), so the answer is +-3sqrt6/4.
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

HOLD_Q3B = ("misprint: det A = -6(a-2)(6a+7), so A is singular exactly at a=2 (rows 1 and 2 both equal (4,3,6)); "
            "A^-1 does not exist for the printed value and the intended a is unknown")


def S(num, part, kind, topic, question, solution, points, ctx=None):
    """solved by the solver (no answer source exists for this sitting)"""
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question,
         "solution": solution, "solutionSource": "solved", "official": False, "confidence": "high"}
    if ctx:
        q["contextId"] = ctx
    return q


def aug(rows, left=3):
    n = len(rows[0])
    spec = "c" * left + "|" + "c" * (n - left)
    return r"\left(\begin{array}{" + spec + "}" + r"\\".join("&".join(str(c) for c in r) for r in rows) + r"\end{array}\right)"


def arrow(op):
    return r"\xrightarrow{" + op + "}"


M2 = lambda a, b, c, d: pm(f"{a}&{b}", f"{c}&{d}")
KER5 = M2(-1, 1, -1, -1)

questions = [
    # ------------------------------------------------------------------ Q1
    S(1, "א", "proof", "matrix_proofs", r"הראו כי $A$ הפיכה ע״י מציאת ביטוי של המטריצה ההפוכה באמצעות $A$.",
      J(r"נחסר את המשוואה השנייה מהראשונה:",
        r"$$\left(AA^T+A^2\right)-\left(AA^T-A^2\right)=3I-0\ \Rightarrow\ 2A^2=3I\ \Rightarrow\ A\cdot\left(\frac23A\right)=I$$",
        r"באותו אופן, חיבור שתי המשוואות נותן $2AA^T=3I$, כלומר $A\cdot\left(\frac23A^T\right)=I$.",
        r"עבור מטריצות ריבועיות, אם $AB=I$ אז $A$ הפיכה ו-$B=A^{-1}$. לכן $A$ הפיכה ו-",
        r"$$A^{-1}=\frac23A$$",
        r"(ובאותו אופן גם $A^{-1}=\frac23A^T$)."),
      7, "c1"),
    S(1, "ב", "proof", "matrix_proofs", r"הוכיחו כי $A^{-1}$ מטריצה סימטרית.",
      J(r"מסעיף (א) $A^{-1}=\frac23A$ וגם $A^{-1}=\frac23A^T$. לכן $\frac23A=\frac23A^T$, כלומר $A^T=A$. מכאן",
        r"$$\left(A^{-1}\right)^T=\left(\frac23A\right)^T=\frac23A^T=\frac23A=A^{-1}$$",
        r"ולכן $A^{-1}$ מטריצה סימטרית."),
      7, "c1"),
    S(1, "ג", "computation", "determinants", r"חשבו את הדטרמיננטה $|A|$.",
      J(r"מסעיף (א) $2A^2=3I$, כלומר $A^2=\frac32I$. נפעיל דטרמיננטה (המטריצה מסדר $3$, ולכן $|cI|=c^3$):",
        r"$$|A|^2=\left|A^2\right|=\left|\frac32I\right|=\left(\frac32\right)^3=\frac{27}{8}\ \Rightarrow\ |A|=\pm\sqrt{\frac{27}{8}}=\pm\frac{3\sqrt6}{4}$$",
        r"הנתונים אינם קובעים את הסימן: המטריצות $A=\sqrt{\frac32}\,I$ ו-$A=-\sqrt{\frac32}\,I$ סימטריות, ולכן לשתיהן $AA^T=A^2=\frac32I$, והן מקיימות את שתי המשוואות הנתונות. הדטרמיננטות שלהן הן $\frac{3\sqrt6}{4}$ ו-$-\frac{3\sqrt6}{4}$.",
        r"לכן $|A|=\pm\frac{3\sqrt6}{4}$."),
      7, "c1"),
    S(1, "ד", "computation", "determinants", r"חשבו את הדטרמיננטה $\left|A^{-1}\right|$.",
      J(r"מתקיים $\left|A^{-1}\right|=\frac{1}{|A|}$, ולכן מסעיף (ג):",
        r"$$\left|A^{-1}\right|=\pm\frac{4}{3\sqrt6}=\pm\frac{2\sqrt6}{9}$$",
        r"(עם אותו סימן כמו $|A|$). בדיקה: $\left|A^{-1}\right|=\left|\frac23A\right|=\left(\frac23\right)^3|A|=\frac{8}{27}\cdot\left(\pm\frac{3\sqrt6}{4}\right)=\pm\frac{2\sqrt6}{9}$."),
      4, "c1"),

    # ------------------------------------------------------------------ Q2
    S(2, "א", "computation", "linear_systems", r"הביאו את המטריצה המורחבת של המערכת לצורת מדורגת קנונית.",
      J(r"המטריצה המורחבת ודירוג שלה:",
        "$$" + aug([[1, -1, "-a", "a"], ["a", 1, -1, "-a"], [1, "a", 1, -1]])
        + arrow(r"\substack{R_2\to R_2-aR_1\\R_3\to R_3-R_1}")
        + aug([[1, -1, "-a", "a"], [0, "a+1", "a^2-1", "-a^2-a"], [0, "a+1", "a+1", "-a-1"]]) + "$$",
        r"**המקרה $a=-1$:** השורות השנייה והשלישית מתאפסות, ונקבל את הצורה המדורגת הקנונית",
        "$$" + aug([[1, -1, 1, -1], [0, 0, 0, 0], [0, 0, 0, 0]]) + "$$",
        r"**המקרה $a\neq-1$:** נחלק את השורות השנייה והשלישית ב-$a+1$ (שימו לב ש-$a^2-1=(a-1)(a+1)$ ו-$-a^2-a=-a(a+1)$):",
        "$$" + arrow(r"\substack{R_2\to\frac{1}{a+1}R_2\\R_3\to\frac{1}{a+1}R_3}")
        + aug([[1, -1, "-a", "a"], [0, 1, "a-1", "-a"], [0, 1, 1, -1]])
        + arrow(r"R_3\to R_3-R_2")
        + aug([[1, -1, "-a", "a"], [0, 1, "a-1", "-a"], [0, 0, "2-a", "a-1"]]) + "$$",
        r"**המקרה $a=2$:** השורה האחרונה היא $(0\ 0\ 0\,|\,1)$. נמשיך ($R_1\to R_1+R_2$, ואז ניקוי העמודה האחרונה בעזרת $R_3$):",
        "$$" + aug([[1, -1, -2, 2], [0, 1, 1, -2], [0, 0, 0, 1]]) + r"\to" + aug([[1, 0, -1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]) + "$$",
        r"**המקרה $a\neq2,-1$:** נחלק את $R_3$ ב-$2-a$ ונקבל $z=\frac{a-1}{2-a}=\frac{1-a}{a-2}$. אחר כך $R_2\to R_2-(a-1)R_3$, $R_1\to R_1+aR_3$ ולבסוף $R_1\to R_1+R_2$. נקבל את הצורה המדורגת הקנונית",
        "$$" + aug([[1, 0, 0, r"\frac{1-a}{a-2}"], [0, 1, 0, r"\frac{1}{a-2}"], [0, 0, 1, r"\frac{1-a}{a-2}"]]) + "$$",
        r"למשל $y=-a-(a-1)\cdot\frac{a-1}{2-a}=\frac{-a(2-a)-(a-1)^2}{2-a}=\frac{-1}{2-a}=\frac{1}{a-2}$, ו-$x=a+y+az=\frac{a(a-2)+1+a(1-a)}{a-2}=\frac{1-a}{a-2}$."),
      9, "c2"),
    S(2, "ב", "computation", "linear_systems", r"מצאו עבור אילו ערכי $a$ יש למערכת אינסוף פתרונות, פתרון יחיד או שאין לה פתרון כלל.",
      J(r"מהדירוג בסעיף (א):",
        r"**פתרון יחיד:** עבור $a\neq2,-1$ מתקיים $r(A)=r(A|b)=3$, והפתרון הוא $\left(\frac{1-a}{a-2},\ \frac{1}{a-2},\ \frac{1-a}{a-2}\right)$.",
        r"**אין פתרון:** עבור $a=2$ מתקבלת השורה $(0\ 0\ 0\,|\,1)$, כלומר $r(A)=2<r(A|b)=3$.",
        r"**אינסוף פתרונות:** עבור $a=-1$ מתקיים $r(A)=r(A|b)=1<3$, ויש שני משתנים חופשיים.",
        r"(בהתאם לכך $|A|=-(a-2)(a+1)^2$, שמתאפס בדיוק עבור $a=2$ ו-$a=-1$.)"),
      8, "c2"),
    S(2, "ג", "computation", "linear_systems", r"עבור $a=-1$ פתרו את המערכת וכתבו את כל הפתרונות.",
      J(r"עבור $a=-1$ שלוש המשוואות הן $x-y+z=-1$, $-x+y-z=1$, $x-y+z=-1$, כלומר כולן אותה משוואה (ראו סעיף (א)):",
        r"$$x-y+z=-1$$",
        r"נבחר $y=s$, $z=t$ חופשיים ונקבל $x=-1+s-t$. אוסף כל הפתרונות:",
        r"$$\left\{\begin{pmatrix}-1+s-t\\s\\t\end{pmatrix}:\ s,t\in\mathbb{R}\right\}=\left\{\begin{pmatrix}-1\\0\\0\end{pmatrix}+s\begin{pmatrix}1\\1\\0\end{pmatrix}+t\begin{pmatrix}-1\\0\\1\end{pmatrix}:\ s,t\in\mathbb{R}\right\}$$"),
      4, "c2"),
    S(2, "ד", "computation", "complex_numbers", r"מצאו את כל הפתרונות המרוכבים של המשוואה $z^4+8z=0$.",
      J(r"$$z^4+8z=z\left(z^3+8\right)=0$$",
        r"ולכן $z=0$ או $z^3=-8$. נכתוב $-8=8\,\mathrm{cis}(\pi)$, ולפי נוסחת השורשים:",
        r"$$z_k=\sqrt[3]{8}\,\mathrm{cis}\left(\frac{\pi+2\pi k}{3}\right)=2\,\mathrm{cis}\left(\frac{\pi+2\pi k}{3}\right),\quad k=0,1,2$$",
        r"$$z_0=2\,\mathrm{cis}\left(\frac{\pi}{3}\right)=1+\sqrt3\,i,\qquad z_1=2\,\mathrm{cis}(\pi)=-2,\qquad z_2=2\,\mathrm{cis}\left(\frac{5\pi}{3}\right)=1-\sqrt3\,i$$",
        r"לכן ארבעת הפתרונות הם $z=0,\ -2,\ 1+\sqrt3\,i,\ 1-\sqrt3\,i$."),
      4),

    # ------------------------------------------------------------------ Q3
    S(3, "א", "computation", "rank_inverse", r"עבור אילו ערכי $a$ המטריצה $A$ הפיכה?",
      J(r"$A$ הפיכה אם ורק אם $|A|\neq0$. נפתח לפי השורה הראשונה:",
        r"$$|A|=2a\begin{vmatrix}a+1&4a-2\\5&2\end{vmatrix}-3\begin{vmatrix}4&4a-2\\1&2\end{vmatrix}+6\begin{vmatrix}4&a+1\\1&5\end{vmatrix}$$",
        r"$$=2a(2a+2-20a+10)-3(8-4a+2)+6(20-a-1)=2a(12-18a)-3(10-4a)+6(19-a)$$",
        r"$$=-36a^2+30a+84=-6\left(6a^2-5a-14\right)=-6(a-2)(6a+7)$$",
        r"לכן $A$ הפיכה עבור $a\neq2$ ו-$a\neq-\frac76$."),
      6, "c3a"),
    dict(H(3, "ב", "computation", "rank_inverse", r"מצאו את $A^{-1}$ עבור $a=2$.", 6, "c3a"), hold=HOLD_Q3B),
    S(3, "ג", "computation", "eigen_diagonalization", r"מצאו את כל הערכים העצמיים והווקטורים העצמיים של $B$.",
      J(r"$$|\lambda I-B|=\begin{vmatrix}\lambda-6&0&-2\\-1&\lambda-4&0\\0&0&\lambda-3\end{vmatrix}=(\lambda-3)\begin{vmatrix}\lambda-6&0\\-1&\lambda-4\end{vmatrix}=(\lambda-3)(\lambda-4)(\lambda-6)$$",
        r"(פיתוח לפי השורה השלישית). הערכים העצמיים הם $3,4,6$.",
        r"**עבור $\lambda=3$:** $B-3I=" + pm("3&0&2", "1&1&0", "0&0&0") + r"$. מהשורה השנייה $y=-x$ ומהראשונה $z=-\frac32x$. נבחר $x=-2$: הווקטור העצמי $\begin{pmatrix}-2\\2\\3\end{pmatrix}$ (וכל כפולה שלו שונה מאפס).",
        r"**עבור $\lambda=4$:** $B-4I=" + pm("2&0&2", "1&0&0", "0&0&-1") + r"$. מהשורה השנייה $x=0$, מהשלישית $z=0$, ו-$y$ חופשי: הווקטור העצמי $\begin{pmatrix}0\\1\\0\end{pmatrix}$.",
        r"**עבור $\lambda=6$:** $B-6I=" + pm("0&0&2", "1&-2&0", "0&0&-3") + r"$. מהשורה הראשונה $z=0$ ומהשנייה $x=2y$: הווקטור העצמי $\begin{pmatrix}2\\1\\0\end{pmatrix}$."),
      8, "c3b"),
    S(3, "ד", "computation", "eigen_diagonalization", r"מצאו את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$.",
      J(r"ל-$B$ שלושה ערכים עצמיים שונים, ולכן שלושת הווקטורים העצמיים מסעיף (ג) בלתי תלויים לינארית ו-$B$ לכסינה. נשים אותם כעמודות של $P$, ואת הערכים העצמיים באותו סדר על האלכסון של $D$:",
        "$$D=" + pm("3&0&0", "0&4&0", "0&0&6") + r",\qquad P=" + pm("-2&0&2", "2&1&1", "3&0&0") + "$$",
        r"בדיקה: $|P|=3\cdot\begin{vmatrix}0&2\\1&1\end{vmatrix}=-6\neq0$, ו-$BP=PD=" + pm("-6&0&12", "6&4&6", "9&0&0") + "$."),
      5, "c3b"),

    # ------------------------------------------------------------------ Q4
    S(4, "א", "computation", "vector_spaces", r"מצאו בסיס ומימד של תתי המרחבים $U$ ו-$W$.",
      J(r"נשתמש בהצגה הקואורדינטית $a_0+a_1x+a_2x^2\ \longleftrightarrow\ (a_0,a_1,a_2)$.",
        r"**בסיס ל-$U$:** נדרג מטריצה ששורותיה הן $1+x,\ 2-x^2,\ 2x+x^2$:",
        "$$" + pm("1&1&0", "2&0&-1", "0&2&1") + arrow(r"R_2\to R_2-2R_1") + pm("1&1&0", "0&-2&-1", "0&2&1") + arrow(r"R_3\to R_3+R_2") + pm("1&1&0", "0&-2&-1", "0&0&0") + "$$",
        r"התקבלה שורת אפס: אכן $2x+x^2=2(1+x)-\left(2-x^2\right)$. שני הפולינומים הראשונים אינם פרופורציוניים, ולכן",
        r"$$B_U=\left\{1+x,\ 2-x^2\right\},\qquad \dim U=2$$",
        r"**בסיס ל-$W$:** $p'(1)=a_1+2a_2=0$, כלומר $a_1=-2a_2$, ולכן",
        r"$$p(x)=a_0-2a_2x+a_2x^2=a_0\cdot1+a_2\left(x^2-2x\right),\quad a_0,a_2\in\mathbb{R}$$",
        r"$$B_W=\left\{1,\ x^2-2x\right\},\qquad \dim W=2$$"),
      6, "c4"),
    S(4, "ב", "computation", "vector_spaces", r"חשבו תת מרחב $U+W$, מצאו בסיס ומימד של תת מרחב זה.",
      J(r"$U+W=\mathrm{Sp}\left\{1+x,\ 2-x^2,\ 1,\ x^2-2x\right\}$. נדרג מטריצה ששורותיה הן הווקטורים הקואורדינטיים:",
        "$$" + pm("1&0&0", "1&1&0", "2&0&-1", "0&-2&1") + arrow(r"\substack{R_2\to R_2-R_1\\R_3\to R_3-2R_1}") + pm("1&0&0", "0&1&0", "0&0&-1", "0&-2&1")
        + arrow(r"\substack{R_4\to R_4+2R_2\\R_4\to R_4+R_3}") + pm("1&0&0", "0&1&0", "0&0&-1", "0&0&0") + "$$",
        r"הדרגה היא $3=\dim\mathbb{R}_2[x]$, ולכן $U+W=\mathbb{R}_2[x]$:",
        r"$$B_{U+W}=\left\{1,\ x,\ x^2\right\},\qquad \dim(U+W)=3$$"),
      8, "c4"),
    S(4, "ג", "computation", "vector_spaces", r"חשבו תת מרחב $U\cap W$, מצאו בסיס ומימד של תת מרחב זה.",
      J(r"פולינום כללי ב-$U$ הוא",
        r"$$p(x)=\alpha(1+x)+\beta\left(2-x^2\right)=(\alpha+2\beta)+\alpha x-\beta x^2$$",
        r"והוא שייך ל-$W$ אם $p'(1)=a_1+2a_2=\alpha-2\beta=0$, כלומר $\alpha=2\beta$. אז",
        r"$$p(x)=2\beta(1+x)+\beta\left(2-x^2\right)=\beta\left(4+2x-x^2\right),\quad \beta\in\mathbb{R}$$",
        r"$$B_{U\cap W}=\left\{4+2x-x^2\right\},\qquad \dim(U\cap W)=1$$",
        r"בדיקה לפי משפט המימדים: $\dim(U+W)=\dim U+\dim W-\dim(U\cap W)=2+2-1=3$, בהתאם לסעיף (ב)."),
      8, "c4"),
    S(4, "ד", "computation", "vector_spaces", r"יהי $q(x)$ פולינום כלשהו השייך לתת מרחב $U\cap W$. מצאו $q(2)+q(-2)$.",
      J(r"מסעיף (ג) $q(x)=\beta\left(4+2x-x^2\right)$ עבור $\beta\in\mathbb{R}$ כלשהו. לכן",
        r"$$q(2)=\beta(4+4-4)=4\beta,\qquad q(-2)=\beta(4-4-4)=-4\beta$$",
        r"$$q(2)+q(-2)=4\beta-4\beta=0$$",
        r"התשובה היא $0$ לכל פולינום ב-$U\cap W$."),
      3, "c4"),

    # ------------------------------------------------------------------ Q5
    S(5, "א", "proof", "linear_maps", r"הוכיחו כי $T$ היא העתקה לינארית.",
      J(r"יהיו $M_1=" + M2("a_1", "b_1", "c_1", "d_1") + r"$, $M_2=" + M2("a_2", "b_2", "c_2", "d_2") + r"$ ו-$\alpha\in\mathbb{R}$. **חיבור:**",
        r"$$T(M_1+M_2)=T\left(" + M2("a_1+a_2", "b_1+b_2", "c_1+c_2", "d_1+d_2") + r"\right)=" + pm("(a_1+a_2)+(b_1+b_2)", "(b_1+b_2)+(c_1+c_2)", "(b_1+b_2)+(d_1+d_2)") + "="
        + pm("a_1+b_1", "b_1+c_1", "b_1+d_1") + "+" + pm("a_2+b_2", "b_2+c_2", "b_2+d_2") + r"=T(M_1)+T(M_2)$$",
        r"**כפל בסקלר:**",
        r"$$T(\alpha M_1)=T\left(" + M2(r"\alpha a_1", r"\alpha b_1", r"\alpha c_1", r"\alpha d_1") + r"\right)=" + pm(r"\alpha a_1+\alpha b_1", r"\alpha b_1+\alpha c_1", r"\alpha b_1+\alpha d_1") + r"=\alpha" + pm("a_1+b_1", "b_1+c_1", "b_1+d_1") + r"=\alpha T(M_1)$$",
        r"שני התנאים מתקיימים, ולכן $T$ העתקה לינארית."),
      6, "c5"),
    S(5, "ב", "computation", "linear_maps", r"מצאו את הבסיסים והמימדים של $\mathrm{Ker}(T)$ ו-$\mathrm{Im}(T)$.",
      J(r"**הגרעין:** $T\left(" + M2("a", "b", "c", "d") + r"\right)=\vec 0$ אם ורק אם",
        r"$$\begin{cases}a+b=0\\b+c=0\\b+d=0\end{cases}\ \Rightarrow\ a=-b,\ c=-b,\ d=-b$$",
        r"$$\mathrm{Ker}(T)=\left\{" + M2("-b", "b", "-b", "-b") + r":\ b\in\mathbb{R}\right\}=\mathrm{Sp}\left\{" + KER5 + r"\right\}$$",
        r"בסיס: $\left\{" + KER5 + r"\right\}$, ו-$\dim\mathrm{Ker}(T)=1$.",
        r"**התמונה:** לפי משפט המימדים $\dim\mathrm{Im}(T)=\dim\mathbb{M}_2(\mathbb{R})-\dim\mathrm{Ker}(T)=4-1=3=\dim\mathbb{R}^3$, ולכן $\mathrm{Im}(T)=\mathbb{R}^3$. "
        r"ואכן $T\left(" + M2(1, 0, 0, 0) + r"\right)=" + pm("1", "0", "0") + r"$, $T\left(" + M2(0, 0, 1, 0) + r"\right)=" + pm("0", "1", "0") + r"$, $T\left(" + M2(0, 0, 0, 1) + r"\right)=" + pm("0", "0", "1") + "$.",
        r"בסיס: $\left\{" + pm("1", "0", "0") + "," + pm("0", "1", "0") + "," + pm("0", "0", "1") + r"\right\}$, ו-$\dim\mathrm{Im}(T)=3$."),
      9, "c5"),
    S(5, "ג", "computation", "linear_maps", r"האם $T$ חד-חד ערכית? האם היא על? נמקו את תשובתכם.",
      J(r"$T$ **אינה** חד-חד ערכית, כי $\mathrm{Ker}(T)\neq\{0\}$ ($\dim\mathrm{Ker}(T)=1$): למשל $T\left(" + KER5 + r"\right)=\vec 0=T(0)$.",
        r"$T$ **היא** על, כי $\mathrm{Im}(T)=\mathbb{R}^3$ ($\dim\mathrm{Im}(T)=3=\dim\mathbb{R}^3$)."),
      3, "c5"),
    S(5, "ד", "computation", "linear_maps",
      r"מצאו את כל המטריצות ב-$\mathbb{M}_2(\mathbb{R})$ שתמונתם נותנת וקטור $" + pm("1", "1", "1") + r"$. האם הן מהוות תת מרחב של $\mathbb{M}_2(\mathbb{R})$?",
      J(r"נפתור $T\left(" + M2("a", "b", "c", "d") + r"\right)=" + pm("1", "1", "1") + "$:",
        r"$$\begin{cases}a+b=1\\b+c=1\\b+d=1\end{cases}\ \Rightarrow\ a=1-t,\ b=t,\ c=1-t,\ d=1-t,\quad t\in\mathbb{R}$$",
        r"$$\left\{" + M2("1-t", "t", "1-t", "1-t") + r":\ t\in\mathbb{R}\right\}=\left\{" + M2(1, 0, 1, 1) + "+t" + KER5 + r":\ t\in\mathbb{R}\right\}$$",
        r"(פתרון פרטי ועוד הגרעין מסעיף (ב)).",
        r"הקבוצה **אינה** תת מרחב: מטריצת האפס אינה שייכת אליה, כי $T(0)=\vec 0\neq" + pm("1", "1", "1") + r"$ (ובאופן ישיר: $b=t=0$ ו-$a=1-t=0$ אינם מתקיימים יחד)."),
      7, "c5"),
]

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
