# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-B.json -- linear algebra, semester A 2021, moed B (22.02.2021), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-B.py

Source: one PDF (4pp, exam only; page 4 is blank). There is NO answer source for this sitting (GATE1: 21A-B has no
solution), so every item was held "no-key" and then solved by the solver (solutionSource "solved", official false,
checked in tools/verify/21A-B/verify_21A-B.py).
Five questions of 25 points (best 4 count), 20 items. No figures.

Transcription notes
- Q1 has two numbered items: item 1 (A, B with AB=B; parts a,b = 7+6 pts) and item 2 (C; parts a,b = 6+6 pts). In the raw
  schema the four sub-parts are א, ב, ג, ד in printed order.
- Q3 has item 1 (A, 8 pts) and item 2 (B, parts 1,2 = 9+8 pts): parts א, ב, ג in printed order.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21A-B.json"


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
    "c1a": {"kind": "text", "title": "שאלה 1 - סעיפים א ו-ב",
            "text": r"נתונות שתי מטריצות ריבועיות $A,B$ מסדר $n$ אי זוגי המקיימות את המשוואה $AB=B$. בנוסף ידוע כי $A$ אנטי סימטרית."},
    "c1b": {"kind": "text", "title": "שאלה 1 - סעיפים ג ו-ד",
            "text": r"נתונה המטריצה $C=" + pm("1&0&0", "5&a&0", "2&a&1") + r"$."},
    "c2": {"kind": "text", "title": "שאלה 2 - מערכת עם שני פרמטרים",
           "text": J(r"נתונה מערכת המשוואות הבאה, כאשר $a,b\in\mathbb{R}$ פרמטרים ממשיים.",
                     r"$$\begin{cases}2x-y+z=3\\ x-y+z=2\\ 3x-y-az=b\end{cases}$$")},
    "c3a": {"kind": "text", "title": "שאלה 3 - סעיף א",
            "text": r"נתונה המטריצה $A=" + pm("1&2&1", "0&1&3", "3&8&8") + r"$."},
    "c3b": {"kind": "text", "title": "שאלה 3 - סעיף ב",
            "text": r"נתונה מטריצה $B=" + pm("5&0&1", "0&4&0", "1&0&5") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של המרחב",
           "text": J(r"יהיו $V$ ו-$W$ שני תתי מרחבים של $\mathbb{R}^3$ המוגדרים כדלקמן:",
                     r"$$V=\mathrm{Sp}\left\{" + pm("0", "1", "1") + "," + pm("1", "2", "3") + "," + pm("1", "1", "2") + "," + pm("1", "3", "4") + r"\right\}$$",
                     r"$$W=\left\{" + pm("x", "y", "z") + r"\ \middle|\ x-z=2y;\ x,y,z\in\mathbb{R}\right\}$$")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": J(r"נסמן $\mathbb{M}_2(\mathbb{R})$ קבוצת מטריצות ריבועיות $2\times2$ ו-$\mathbb{R}_2[x]$ מרחב של פולינומים ממשיים ממעלה שתיים לכל היותר. תהי העתקה $T:\mathbb{M}_2(\mathbb{R})\to\mathbb{R}_2[x]$ מוגדרת לפי",
                     r"$$T\left(" + pm("a&b", "c&d") + r"\right)=(a+2b+8c+d)+(-3a+2b+5d)x+(a+b+5c)x^2$$")},
}

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


def col(*v):
    return pm(*[[c] for c in v])


M2 = lambda a, b, c, d: pm(f"{a}&{b}", f"{c}&{d}")

questions = [
    # ------------------------------------------------------------------ Q1
    S(1, "א", "proof", "matrix_proofs", r"הראו כי $\det A=0$.",
      J(r"$A$ אנטי סימטרית, כלומר $A^T=-A$. נשתמש ב-$\det\left(A^T\right)=\det A$ וב-$\det(cA)=c^n\det A$ עבור מטריצה מסדר $n$:",
        r"$$\det A=\det\left(A^T\right)=\det(-A)=(-1)^n\det A=-\det A$$",
        r"(השוויון האחרון כי $n$ אי זוגי). מכאן $2\det A=0$, ולכן $\det A=0$."),
      7, "c1a"),
    S(1, "ב", "proof", "matrix_proofs", r"האם $B$ הפיכה? נמקו!",
      J(r"$B$ **אינה** הפיכה. נניח בשלילה ש-$B$ הפיכה. נכפיל את $AB=B$ מימין ב-$B^{-1}$:",
        r"$$ABB^{-1}=BB^{-1}\ \Rightarrow\ A=I$$",
        r"אבל $\det I=1$, בסתירה לסעיף (א) ($\det A=0$). לכן $B$ אינה הפיכה.",
        r"(דרך נוספת: מ-$AB=B$ נקבל $\det A\cdot\det B=\det B$, ומכיוון ש-$\det A=0$ נקבל $\det B=0$.)"),
      6, "c1a"),
    S(1, "ג", "computation", "vector_spaces", r"מצאו בסיס ומימד של מרחב העמודות של $C$ כאשר היא איננה הפיכה.",
      J(r"$C$ משולשית תחתונה, ולכן $\det C=1\cdot a\cdot1=a$. $C$ אינה הפיכה בדיוק כאשר $a=0$, ואז",
        r"$$C=" + pm("1&0&0", "5&0&0", "2&0&1") + "$$",
        r"העמודה השנייה היא עמודת אפס, והעמודות הראשונה והשלישית אינן פרופורציוניות, ולכן הן בלתי תלויות לינארית. מכאן",
        r"$$B_{\mathrm{Col}\,C}=\left\{" + col(1, 5, 2) + "," + col(0, 0, 1) + r"\right\},\qquad \dim\mathrm{Col}\,C=2$$"),
      6, "c1b"),
    S(1, "ד", "computation", "vector_spaces", r"בנו בסיס של $\mathbb{R}^3$ שמכיל בתוכו בסיס של מרחב העמודות של $C$ מסעיף א׳.",
      J(r"נשלים את הבסיס מסעיף (ג) בווקטור $" + col(0, 1, 0) + r"$ ונבדוק שהשלושה בלתי תלויים לינארית:",
        r"$$\begin{vmatrix}1&0&0\\5&0&1\\2&1&0\end{vmatrix}=1\cdot\begin{vmatrix}0&1\\1&0\end{vmatrix}=-1\neq0$$",
        r"לכן שלושה וקטורים בלתי תלויים ב-$\mathbb{R}^3$ (שמימדו $3$) הם בסיס:",
        r"$$\left\{" + col(1, 5, 2) + "," + col(0, 0, 1) + "," + col(0, 1, 0) + r"\right\}$$"),
      6, "c1b"),

    # ------------------------------------------------------------------ Q2
    S(2, "א", "computation", "linear_systems", r"הביאו את מטריצת המקדמים המורחבת של המערכת לצורה מדורגת.",
      J(r"$$" + aug([[2, -1, 1, 3], [1, -1, 1, 2], [3, -1, "-a", "b"]]) + arrow(r"R_1\leftrightarrow R_2") + aug([[1, -1, 1, 2], [2, -1, 1, 3], [3, -1, "-a", "b"]]) + "$$",
        r"$$" + arrow(r"\substack{R_2\to R_2-2R_1\\R_3\to R_3-3R_1}") + aug([[1, -1, 1, 2], [0, 1, -1, -1], [0, 2, "-a-3", "b-6"]])
        + arrow(r"R_3\to R_3-2R_2") + aug([[1, -1, 1, 2], [0, 1, -1, -1], [0, 0, "-a-1", "b-4"]]) + "$$"),
      7, "c2"),
    S(2, "ב", "computation", "linear_systems", r"מצאו עבור אילו ערכי $a,b$ יש למערכת אינסוף פתרונות, פתרון יחיד או שאין לה פתרון כלל.",
      J(r"לפי השורה האחרונה בצורה המדורגת, $(0\ 0\ \ {-a-1}\,|\,b-4)$:",
        r"**פתרון יחיד:** $a\neq-1$ (כל $b$), כי אז $r(A)=r(A|b)=3$.",
        r"**אינסוף פתרונות:** $a=-1$ ו-$b=4$, כי אז השורה האחרונה מתאפסת ו-$r(A)=r(A|b)=2<3$.",
        r"**אין פתרון:** $a=-1$ ו-$b\neq4$, כי אז השורה האחרונה היא $(0\ 0\ 0\,|\,b-4)$ עם $b-4\neq0$, כלומר $r(A)=2<r(A|b)=3$."),
      4, "c2"),
    S(2, "ג", "computation", "linear_systems", r"עבור $a=2$ ו-$b=1$ פתרו את המערכת וכתבו את כל הפתרונות.",
      J(r"נציב בצורה המדורגת מסעיף (א):",
        r"$$" + aug([[1, -1, 1, 2], [0, 1, -1, -1], [0, 0, -3, -3]]) + "$$",
        r"מהשורה השלישית $z=1$, מהשנייה $y=-1+z=0$, ומהראשונה $x=2+y-z=1$. הפתרון היחיד:",
        r"$$(x,y,z)=(1,0,1)$$",
        r"בדיקה: $2-0+1=3$, $1-0+1=2$, $3-0-2=1$."),
      4, "c2"),
    S(2, "ד", "computation", "linear_systems", r"עבור $a=-1$ ו-$b=4$ פתרו את המערכת וכתבו את כל הפתרונות.",
      J(r"נציב בצורה המדורגת מסעיף (א); השורה השלישית מתאפסת:",
        r"$$" + aug([[1, -1, 1, 2], [0, 1, -1, -1], [0, 0, 0, 0]]) + "$$",
        r"נבחר $z=t$ חופשי. מהשורה השנייה $y=t-1$, ומהראשונה $x=2+y-z=2+(t-1)-t=1$. כל הפתרונות:",
        r"$$\left\{" + col(1, "t-1", "t") + r":\ t\in\mathbb{R}\right\}=\left\{" + col(1, -1, 0) + "+t" + col(0, 1, 1) + r":\ t\in\mathbb{R}\right\}$$"),
      4, "c2"),
    S(2, "ה", "computation", "complex_numbers", r"הראו שלמשוואה $4z=\overline{z}^{\,2}$ יש ארבעה פתרונות, כתבו את כולם.",
      J(r"**ערך מוחלט:** $|4z|=\left|\overline{z}^{\,2}\right|$ נותן $4|z|=|z|^2$, ולכן $|z|=0$ או $|z|=4$.",
        r"**$|z|=0$:** $z=0$, ואכן $4\cdot0=0^2$.",
        r"**$|z|=4$:** נכתוב $z=4\,\mathrm{cis}\,\theta$, אז $\overline{z}=4\,\mathrm{cis}(-\theta)$ ו-$\overline{z}^{\,2}=16\,\mathrm{cis}(-2\theta)$. המשוואה היא",
        r"$$16\,\mathrm{cis}\,\theta=16\,\mathrm{cis}(-2\theta)\ \Rightarrow\ \theta=-2\theta+2\pi k\ \Rightarrow\ \theta=\frac{2\pi k}{3},\quad k=0,1,2$$",
        r"$$z_1=4\,\mathrm{cis}\,0=4,\qquad z_2=4\,\mathrm{cis}\left(\frac{2\pi}{3}\right)=-2+2\sqrt3\,i,\qquad z_3=4\,\mathrm{cis}\left(\frac{4\pi}{3}\right)=-2-2\sqrt3\,i$$",
        r"לכן יש בדיוק ארבעה פתרונות: $z=0,\ 4,\ -2+2\sqrt3\,i,\ -2-2\sqrt3\,i$.",
        r"בדיקה עבור $z=-2+2\sqrt3\,i$: $\overline{z}^{\,2}=\left(-2-2\sqrt3\,i\right)^2=4+8\sqrt3\,i-12=-8+8\sqrt3\,i=4z$."),
      6),

    # ------------------------------------------------------------------ Q3
    S(3, "א", "computation", "rank_inverse", r"כתבו את $A^{-1}$ כמכפלה של מטריצות אלמנטריות.",
      J(r"נדרג את $(A\,|\,I)$ ונרשום את פעולות השורה:",
        "$$" + aug([[1, 2, 1, 1, 0, 0], [0, 1, 3, 0, 1, 0], [3, 8, 8, 0, 0, 1]]) + arrow(r"R_3\to R_3-3R_1")
        + aug([[1, 2, 1, 1, 0, 0], [0, 1, 3, 0, 1, 0], [0, 2, 5, -3, 0, 1]]) + arrow(r"R_3\to R_3-2R_2")
        + aug([[1, 2, 1, 1, 0, 0], [0, 1, 3, 0, 1, 0], [0, 0, -1, -3, -2, 1]]) + "$$",
        "$$" + arrow(r"R_3\to -R_3") + aug([[1, 2, 1, 1, 0, 0], [0, 1, 3, 0, 1, 0], [0, 0, 1, 3, 2, -1]])
        + arrow(r"R_2\to R_2-3R_3") + aug([[1, 2, 1, 1, 0, 0], [0, 1, 0, -9, -5, 3], [0, 0, 1, 3, 2, -1]]) + "$$",
        "$$" + arrow(r"R_1\to R_1-R_3") + aug([[1, 2, 0, -2, -2, 1], [0, 1, 0, -9, -5, 3], [0, 0, 1, 3, 2, -1]])
        + arrow(r"R_1\to R_1-2R_2") + aug([[1, 0, 0, 16, 8, -5], [0, 1, 0, -9, -5, 3], [0, 0, 1, 3, 2, -1]]) + "$$",
        r"$$A^{-1}=" + pm("16&8&-5", "-9&-5&3", "3&2&-1") + "$$",
        r"לכל פעולת שורה מתאימה מטריצה אלמנטרית $E_1,\dots,E_6$ (הפעולה על $I$), ו-$E_6E_5E_4E_3E_2E_1A=I$, ולכן $A^{-1}=E_6E_5E_4E_3E_2E_1$ (הפעולה האחרונה היא הגורם השמאלי):",
        "$$A^{-1}=" + pm("1&-2&0", "0&1&0", "0&0&1") + pm("1&0&-1", "0&1&0", "0&0&1") + pm("1&0&0", "0&1&-3", "0&0&1")
        + pm("1&0&0", "0&1&0", "0&0&-1") + pm("1&0&0", "0&1&0", "0&-2&1") + pm("1&0&0", "0&1&0", "-3&0&1") + "$$"),
      8, "c3a"),
    S(3, "ב", "computation", "eigen_diagonalization", r"מצאו את כל הערכים העצמיים והווקטורים העצמיים של $B$.",
      J(r"נפתח לפי השורה השנייה:",
        r"$$|\lambda I-B|=\begin{vmatrix}\lambda-5&0&-1\\0&\lambda-4&0\\-1&0&\lambda-5\end{vmatrix}=(\lambda-4)\left[(\lambda-5)^2-1\right]=(\lambda-4)(\lambda-4)(\lambda-6)$$",
        r"הערכים העצמיים: $\lambda=4$ (ריבוי אלגברי $2$) ו-$\lambda=6$.",
        r"**עבור $\lambda=4$:** $B-4I=" + pm("1&0&1", "0&0&0", "1&0&1") + r"\to" + pm("1&0&1", "0&0&0", "0&0&0") + r"$, כלומר $x=-z$, ו-$y,z$ חופשיים:",
        r"$$" + col("x", "y", "z") + "=" + col("-z", "y", "z") + "=y" + col(0, 1, 0) + "+z" + col(-1, 0, 1) + "$$",
        r"הווקטורים העצמיים הם הצירופים השונים מאפס של $" + col(0, 1, 0) + r"$ ו-$" + col(-1, 0, 1) + "$.",
        r"**עבור $\lambda=6$:** $B-6I=" + pm("-1&0&1", "0&-2&0", "1&0&-1") + r"\to" + pm("1&0&-1", "0&1&0", "0&0&0") + r"$, כלומר $x=z$, $y=0$: הווקטור העצמי $" + col(1, 0, 1) + r"$ (וכפולותיו השונות מאפס)."),
      9, "c3b"),
    S(3, "ג", "computation", "eigen_diagonalization", r"האם $B$ ניתנת ללכסון? אם כן, מצאו את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$. אם לא, אז נמקו למה!",
      J(r"כן. לערך העצמי $4$ ריבוי אלגברי $2$ ומרחב עצמי ממימד $2$, ולערך העצמי $6$ ריבוי $1$ ומרחב עצמי ממימד $1$. לכן יש ל-$B$ שלושה וקטורים עצמיים בלתי תלויים, ו-$B$ לכסינה:",
        "$$D=" + pm("4&0&0", "0&4&0", "0&0&6") + r",\qquad P=" + pm("0&-1&1", "1&0&0", "0&1&1") + "$$",
        r"(עמודות $P$ הן הווקטורים העצמיים, באותו סדר כמו הערכים העצמיים על האלכסון של $D$). בדיקה: $|P|=2\neq0$ ו-$BP=PD=" + pm("0&-4&6", "4&0&0", "0&4&6") + "$."),
      8, "c3b"),

    # ------------------------------------------------------------------ Q4
    S(4, "א", "computation", "vector_spaces", r"מצאו בסיס ומימד של תתי המרחבים $V$ ו-$W$.",
      J(r"**בסיס ל-$V$:** נדרג מטריצה ששורותיה הן הווקטורים הפורשים (בסדר $(1,1,2),(0,1,1),(1,2,3),(1,3,4)$):",
        "$$" + pm("1&1&2", "0&1&1", "1&2&3", "1&3&4") + arrow(r"\substack{R_3\to R_3-R_1\\R_4\to R_4-R_1}") + pm("1&1&2", "0&1&1", "0&1&1", "0&2&2")
        + arrow(r"\substack{R_3\to R_3-R_2\\R_4\to R_4-2R_2}") + pm("1&1&2", "0&1&1", "0&0&0", "0&0&0") + "$$",
        r"הדרגה $2$ (ואכן $(1,2,3)=(1,1,2)+(0,1,1)$ ו-$(1,3,4)=(1,1,2)+2(0,1,1)$). לכן",
        r"$$B_V=\left\{" + col(1, 1, 2) + "," + col(0, 1, 1) + r"\right\},\qquad \dim V=2$$",
        r"**בסיס ל-$W$:** מ-$x-z=2y$ נקבל $x=2y+z$, ו-$y,z$ חופשיים:",
        r"$$" + col("x", "y", "z") + "=" + col("2y+z", "y", "z") + "=y" + col(2, 1, 0) + "+z" + col(1, 0, 1) + "$$",
        r"$$B_W=\left\{" + col(2, 1, 0) + "," + col(1, 0, 1) + r"\right\},\qquad \dim W=2$$"),
      6, "c4"),
    S(4, "ב", "computation", "vector_spaces", r"חשבו תת מרחב $V+W$, מצאו בסיס ומימד של תת מרחב זה.",
      J(r"$V+W=\mathrm{Sp}\left(B_V\cup B_W\right)$. נדרג:",
        "$$" + pm("1&1&2", "0&1&1", "2&1&0", "1&0&1") + arrow(r"\substack{R_3\to R_3-2R_1\\R_4\to R_4-R_1}") + pm("1&1&2", "0&1&1", "0&-1&-4", "0&-1&-1")
        + arrow(r"\substack{R_3\to R_3+R_2\\R_4\to R_4+R_2}") + pm("1&1&2", "0&1&1", "0&0&-3", "0&0&0") + "$$",
        r"הדרגה $3=\dim\mathbb{R}^3$, ולכן $V+W=\mathbb{R}^3$:",
        r"$$B_{V+W}=\left\{" + col(1, 0, 0) + "," + col(0, 1, 0) + "," + col(0, 0, 1) + r"\right\},\qquad \dim(V+W)=3$$"),
      8, "c4"),
    S(4, "ג", "computation", "vector_spaces", r"חשבו תת מרחב $V\cap W$, מצאו בסיס ומימד של תת מרחב זה.",
      J(r"וקטור כללי ב-$V$ הוא $\alpha(1,1,2)+\beta(0,1,1)=(\alpha,\ \alpha+\beta,\ 2\alpha+\beta)$. הוא שייך ל-$W$ אם $x-z=2y$:",
        r"$$\alpha-(2\alpha+\beta)=2(\alpha+\beta)\ \Rightarrow\ -\alpha-\beta=2\alpha+2\beta\ \Rightarrow\ \beta=-\alpha$$",
        r"ולכן הווקטורים המשותפים הם $\alpha(1,0,1)$, $\alpha\in\mathbb{R}$:",
        r"$$B_{V\cap W}=\left\{" + col(1, 0, 1) + r"\right\},\qquad \dim(V\cap W)=1$$",
        r"בדיקה לפי משפט המימדים: $\dim(V+W)=2+2-1=3$, בהתאם לסעיף (ב)."),
      8, "c4"),
    S(4, "ד", "computation", "vector_spaces",
      r"האם הווקטור $" + col(1, 3, 2) + r"$ שייך לתת מרחב $V\cap W$? האם הוא שייך לתת מרחב $V+W$?",
      J(r"**$V\cap W$:** לפי סעיף (ג) כל וקטור ב-$V\cap W$ הוא מהצורה $(t,0,t)$. ב-$(1,3,2)$ הרכיב השני $3\neq0$, ולכן הווקטור **אינו** שייך ל-$V\cap W$. "
        r"(גם ישירות: $x-z=1-2=-1\neq2y=6$, כך שהוא אפילו לא ב-$W$.)",
        r"**$V+W$:** לפי סעיף (ב) $V+W=\mathbb{R}^3$, ולכן הווקטור **שייך** ל-$V+W$. למשל $(1,3,2)=\frac73(0,1,1)+\left(1,\frac23,-\frac13\right)$, כאשר הווקטור הראשון ב-$V$ והשני ב-$W$ (כי $1-\left(-\frac13\right)=\frac43=2\cdot\frac23$)."),
      3, "c4"),

    # ------------------------------------------------------------------ Q5
    S(5, "א", "proof", "linear_maps", r"הוכיחו כי $T$ היא העתקה לינארית.",
      J(r"נסמן $T(M)=f_1(M)+f_2(M)x+f_3(M)x^2$ עבור $M=" + M2("a", "b", "c", "d") + r"$, כאשר",
        r"$$f_1=a+2b+8c+d,\qquad f_2=-3a+2b+5d,\qquad f_3=a+b+5c$$",
        r"יהיו $M_1=" + M2("a_1", "b_1", "c_1", "d_1") + r"$, $M_2=" + M2("a_2", "b_2", "c_2", "d_2") + r"$ ו-$\alpha\in\mathbb{R}$. **חיבור:** המקדם החופשי של $T(M_1+M_2)$ הוא",
        r"$$(a_1+a_2)+2(b_1+b_2)+8(c_1+c_2)+(d_1+d_2)=(a_1+2b_1+8c_1+d_1)+(a_2+2b_2+8c_2+d_2)$$",
        r"ובאותו אופן",
        r"$$-3(a_1+a_2)+2(b_1+b_2)+5(d_1+d_2)=(-3a_1+2b_1+5d_1)+(-3a_2+2b_2+5d_2)$$",
        r"$$(a_1+a_2)+(b_1+b_2)+5(c_1+c_2)=(a_1+b_1+5c_1)+(a_2+b_2+5c_2)$$",
        r"ולכן $T(M_1+M_2)=T(M_1)+T(M_2)$.",
        r"**כפל בסקלר:** כל מקדם הוא ביטוי לינארי ב-$a,b,c,d$ בלי איבר חופשי, למשל $\alpha a+2\alpha b+8\alpha c+\alpha d=\alpha(a+2b+8c+d)$, ולכן $T(\alpha M)=\alpha T(M)$.",
        r"שני התנאים מתקיימים, ולכן $T$ העתקה לינארית."),
      7, "c5"),
    S(5, "ב", "computation", "linear_maps", r"מצאו את הבסיס והמימד של $\mathrm{Ker}(T)$.",
      J(r"$T(M)=0$ אם ורק אם שלושת המקדמים מתאפסים. נדרג את מטריצת המקדמים (העמודות: $a,b,c,d$):",
        "$$" + pm("1&2&8&1", "-3&2&0&5", "1&1&5&0") + arrow(r"\substack{R_2\to R_2+3R_1\\R_3\to R_3-R_1}") + pm("1&2&8&1", "0&8&24&8", "0&-1&-3&-1")
        + arrow(r"\substack{R_2\to\frac18R_2\\R_3\to R_3+R_2}") + pm("1&2&8&1", "0&1&3&1", "0&0&0&0") + arrow(r"R_1\to R_1-2R_2") + pm("1&0&2&-1", "0&1&3&1", "0&0&0&0") + "$$",
        r"נבחר $c=s$, $d=t$ חופשיים: $a=-2s+t$, $b=-3s-t$. לכן",
        r"$$M=" + M2("-2s+t", "-3s-t", "s", "t") + "=s" + M2(-2, -3, 1, 0) + "+t" + M2(1, -1, 0, 1) + "$$",
        r"$$B_{\mathrm{Ker}(T)}=\left\{" + M2(-2, -3, 1, 0) + "," + M2(1, -1, 0, 1) + r"\right\},\qquad \dim\mathrm{Ker}(T)=2$$",
        r"(שתי המטריצות אינן פרופורציוניות, ולכן בלתי תלויות)."),
      8, "c5"),
    S(5, "ג", "computation", "linear_maps", r"מצאו את הבסיס והמימד של $\mathrm{Im}(T)$.",
      J(r"$\mathrm{Im}(T)$ נפרש על ידי תמונות איברי הבסיס הסטנדרטי של $\mathbb{M}_2(\mathbb{R})$:",
        r"$$T\left(" + M2(1, 0, 0, 0) + r"\right)=1-3x+x^2,\quad T\left(" + M2(0, 1, 0, 0) + r"\right)=2+2x+x^2,\quad T\left(" + M2(0, 0, 1, 0) + r"\right)=8+5x^2,\quad T\left(" + M2(0, 0, 0, 1) + r"\right)=1+5x$$",
        r"אלה עמודות מטריצת המקדמים מסעיף (ב). בצורה המדורגת שם העמודות המובילות הן הראשונה והשנייה, ולכן",
        r"$$B_{\mathrm{Im}(T)}=\left\{1-3x+x^2,\ 2+2x+x^2\right\},\qquad \dim\mathrm{Im}(T)=2$$",
        r"בהתאם למשפט המימדים: $\dim\mathrm{Im}(T)=4-\dim\mathrm{Ker}(T)=4-2=2$."),
      8, "c5"),
    S(5, "ד", "computation", "linear_maps", r"האם $T$ היא העתקה הפיכה? נמקו!",
      J(r"**לא.** $\mathrm{Ker}(T)\neq\{0\}$ ($\dim\mathrm{Ker}(T)=2$), ולכן $T$ אינה חד-חד ערכית; וגם $\dim\mathrm{Im}(T)=2<3=\dim\mathbb{R}_2[x]$, ולכן אינה על. "
        r"(בכלל, העתקה בין מרחבים ממימדים שונים, $4\neq3$, אינה יכולה להיות הפיכה.)"),
      2, "c5"),
]

exam = {
    "examCode": "21A-B",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״א, מועד ב׳ (22.02.2021)",
    "year": 2021,
    "examDate": "22.02.2021",
    "sourceFile": "21A-B exam (PDF, 4pp, exam only)",
    "solutionFile": "none",
    "contexts": contexts,
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
