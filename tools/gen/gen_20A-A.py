# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-A.json -- linear algebra, semester A 2020, moed A (16.02.2020), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20A-A.py

Source: one PDF (2pp, exam only). There is NO answer source for this sitting, so every item was held "no-key" and is now solved
by the solver (solutionSource "solved", official false; checks in tools/verify/20A-A/verify_20A-A.py). The questions are
transcribed in full. Five questions of 25 points (best 4 count), 20 items. No figures.

Why no key: the file triage paired with this exam ("סמ׳ א מועד א פתרון.pdf" in the 2020 folder, 14pp) is NOT the solution of
this exam. Its questions (AA^T+A^2=3I, the system x-y-az=a, A with 2a/3/6, B=(6 0 2;1 4 0;0 0 3), W,U in R_2[x], T on
M_2x2) are exactly the questions of 21A-A (24.01.2021). It contains no planes pi_1, pi_2 with k, no z^5=3i+5, no W_1,W_2 in R^3
and no T(x,y,z)=(x-y,-2x+2y,2z). It is now used as the official key of 21A-A.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts 1,2 = 5+5 pts) and item 2 (B, parts 1,2 = 9+6 pts). In the raw schema the four
  sub-parts are א, ב, ג, ד in printed order (A1, A2, B1, B2).
- Q1 d prints z^5 = 3i+5.
- Q4 prints the second subspace with the condition x-y=z+y.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20A-A.json"


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
    "c1": {"kind": "text", "title": "שאלה 1 - שני מישורים",
           "text": J(r"נתונים שני מישורים כאשר $k$ הוא פרמטר ממשי:",
                     r"$$\begin{cases}\pi_1:\ x-2y+z+5=0\\ \pi_2:\ kx-y+kz-2=0\end{cases}$$")},
    "c2": {"kind": "text", "title": "שאלה 2 - המטריצה A",
           "text": r"נתונה מטריצה $A=" + pm("1&0&1&1", "1&1&2&0", "0&1&1&-1") + r"$."},
    "c3a": {"kind": "text", "title": "שאלה 3 - סעיף א",
            "text": r"תהי נתונה המטריצה $A=" + pm("2&1&-1", "1&a&1", "3&1&-a") + r"$ כאשר $a$ הוא פרמטר ממשי."},
    "c3b": {"kind": "text", "title": "שאלה 3 - סעיף ב",
            "text": r"תהי נתונה מטריצה $A=" + pm("1&1&-1", "1&1&1", "1&1&1") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - שני תתי מרחבים של המרחב",
           "text": J(r"יהיו $W_1$ ו-$W_2$ שני תתי מרחבים של $\mathbb{R}^3$ המוגדרים כדלקמן:",
                     r"$$W_1=\mathrm{Sp}\left\{" + pm("1", "2", "3") + "," + pm("2", "3", "1") + "," + pm("3", "1", "2") + "," + pm("1", "1", "1") + r"\right\}$$",
                     r"$$W_2=\left\{" + pm("x", "y", "z") + r"\ \middle|\ x-y=z+y;\ x,y,z\in\mathbb{R}\right\}$$")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": r"תהי $T:\mathbb{R}^3\to\mathbb{R}^3$ ההעתקה הלינארית כך ש-$T" + pm("x", "y", "z") + "=" + pm("x-y", "-2x+2y", "2z") + r"$."},
}

def S(num, part, kind, topic, question, solution, points, ctx=None):
    """solved by the solver (no answer source exists for this sitting)"""
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "points": points, "question": question,
         "solution": solution, "solutionSource": "solved", "official": False, "confidence": "high"}
    if ctx:
        q["contextId"] = ctx
    return q


def arrow(op):
    return r"\xrightarrow{" + op + "}"


def col(*v):
    return pm(*[[c] for c in v])


ANG = r"\frac{\arctan\frac35+2\pi k}{5}"

questions = [
    # ------------------------------------------------------------------ Q1
    S(1, "א", "computation", "lines_planes", r"חשב את ערכו של $k$ כך שהמישורים יהיו מקבילים וחשב את המרחק ביניהם.",
      J(r"הווקטורים הנורמליים הם $\vec n_1=(1,-2,1)$ ו-$\vec n_2=(k,-1,k)$. המישורים מקבילים כאשר הנורמלים פרופורציוניים, $\vec n_2=\mu\vec n_1$:",
        r"$$k=\mu,\qquad -1=-2\mu,\qquad k=\mu\ \Rightarrow\ \mu=\frac12,\quad k=\frac12$$",
        r"עבור $k=\frac12$: $\pi_2:\ \frac12x-y+\frac12z-2=0$, ואחרי כפל ב-$2$: $\pi_2:\ x-2y+z-4=0$. האיברים החופשיים ($5$ ו-$-4$) שונים, ולכן המישורים מקבילים ושונים.",
        r"המרחק בין המישורים המקבילים $x-2y+z+5=0$ ו-$x-2y+z-4=0$:",
        r"$$d=\frac{|5-(-4)|}{\sqrt{1^2+(-2)^2+1^2}}=\frac{9}{\sqrt6}=\frac{3\sqrt6}{2}$$",
        r"(בדיקה: הנקודה $(-5,0,0)\in\pi_1$, ומרחקה מ-$\pi_2$ הוא $\frac{|-5-0+0-4|}{\sqrt6}=\frac{9}{\sqrt6}$.)"),
      6, "c1"),
    S(1, "ב", "computation", "lines_planes", r"חשב את ערכו של $k$ כך שהמישורים יהיו מאונכים.",
      J(r"המישורים מאונכים כאשר הנורמלים מאונכים:",
        r"$$\vec n_1\cdot\vec n_2=(1,-2,1)\cdot(k,-1,k)=k+2+k=2k+2=0\ \Rightarrow\ k=-1$$"),
      6, "c1"),
    S(1, "ג", "computation", "lines_planes", r"עבור $k=2$ מצא מישור שמאונך ל-$\pi_1$ ו-$\pi_2$ ועובר דרך הנק׳ $(1,1,1)$.",
      J(r"עבור $k=2$: $\vec n_1=(1,-2,1)$, $\vec n_2=(2,-1,2)$. מישור המאונך לשני המישורים הוא מישור שהנורמל שלו $\vec N$ מאונך ל-$\vec n_1$ ול-$\vec n_2$, ולכן",
        r"$$\vec N=\vec n_1\times\vec n_2=\begin{vmatrix}\hat\imath&\hat\jmath&\hat k\\1&-2&1\\2&-1&2\end{vmatrix}=(-4+1)\hat\imath-(2-2)\hat\jmath+(-1+4)\hat k=(-3,0,3)=-3(1,0,-1)$$",
        r"נבחר $\vec N=(1,0,-1)$. המישור דרך $(1,1,1)$:",
        r"$$1\cdot(x-1)+0\cdot(y-1)-1\cdot(z-1)=0\ \Rightarrow\ x-z=0$$",
        r"בדיקה: $(1,0,-1)\cdot(1,-2,1)=0$, $(1,0,-1)\cdot(2,-1,2)=0$, והנקודה $(1,1,1)$ מקיימת $1-1=0$."),
      7, "c1"),
    S(1, "ד", "computation", "complex_numbers", r"פתור את המשוואה $z^5=3i+5$.",
      J(r"נכתוב את $5+3i$ בהצגה קוטבית: $r=|5+3i|=\sqrt{25+9}=\sqrt{34}$, והזווית ברביע הראשון היא $\theta=\arctan\frac35$ (בערך $30.96^\circ$). כלומר $5+3i=\sqrt{34}\,\mathrm{cis}\left(\arctan\frac35\right)$.",
        r"לפי נוסחת השורשים:",
        r"$$z_k=\sqrt[5]{\sqrt{34}}\,\mathrm{cis}\left(" + ANG + r"\right)=\sqrt[10]{34}\,\mathrm{cis}\left(" + ANG + r"\right),\quad k=0,1,2,3,4$$",
        r"בערך: $\sqrt[10]{34}\approx1.423$, והזוויות הן בערך $6.19^\circ,\ 78.19^\circ,\ 150.19^\circ,\ 222.19^\circ,\ 294.19^\circ$ (הפרש של $72^\circ$ בין שורשים סמוכים)."),
      6),

    # ------------------------------------------------------------------ Q2
    S(2, "א", "computation", "vector_spaces", r"נגדיר את **מרחב האפס** של מטריצה $A$ כאוסף הפתרונות $\mathbf{x}$ של מערכת משוואות הומוגנית $A\mathbf{x}=\mathbf{0}$. מצא בסיס של מרחב האפס וגם את מימדו.",
      J(r"נדרג את $A$:",
        "$$" + pm("1&0&1&1", "1&1&2&0", "0&1&1&-1") + arrow(r"R_2\to R_2-R_1") + pm("1&0&1&1", "0&1&1&-1", "0&1&1&-1") + arrow(r"R_3\to R_3-R_2") + pm("1&0&1&1", "0&1&1&-1", "0&0&0&0") + "$$",
        r"המשתנים $x_3=s$, $x_4=t$ חופשיים, ו-$x_1=-s-t$, $x_2=-s+t$:",
        r"$$\mathbf{x}=" + col("-s-t", "-s+t", "s", "t") + "=s" + col(-1, -1, 1, 0) + "+t" + col(-1, 1, 0, 1) + "$$",
        r"$$B_{\mathrm{Nul}A}=\left\{" + col(-1, -1, 1, 0) + "," + col(-1, 1, 0, 1) + r"\right\},\qquad \dim\mathrm{Nul}A=2$$"),
      7, "c2"),
    S(2, "ב", "computation", "vector_spaces", r"מצא בסיס של מרחב השורות של מטריצה $A$ ואת מימדו.",
      J(r"פעולות שורה אינן משנות את מרחב השורות, ולכן השורות השונות מאפס בצורה המדורגת מסעיף (א) הן בסיס:",
        r"$$B_{\mathrm{Row}A}=\left\{(1,0,1,1),\ (0,1,1,-1)\right\},\qquad \dim\mathrm{Row}A=2$$",
        r"(ואכן השורה השלישית של $A$ היא $R_2-R_1$.)"),
      7, "c2"),
    S(2, "ג", "computation", "vector_spaces", r"מצא בסיס של מרחב העמודות של מטריצה $A$ ואת מימדו.",
      J(r"בצורה המדורגת העמודות המובילות הן הראשונה והשנייה, ולכן העמודות המתאימות **של $A$ המקורית** הן בסיס למרחב העמודות:",
        r"$$B_{\mathrm{Col}A}=\left\{" + col(1, 1, 0) + "," + col(0, 1, 1) + r"\right\},\qquad \dim\mathrm{Col}A=2$$",
        r"(העמודה השלישית היא סכום שתי הראשונות, והרביעית היא הראשונה פחות השנייה.)"),
      7, "c2"),
    S(2, "ד", "computation", "vector_spaces", r"בדוק שהסכום של מימד מרחב האפס ומימד של מרחב העמודות שווה למספר העמודות של $A$.",
      J(r"$$\dim\mathrm{Nul}A+\dim\mathrm{Col}A=2+2=4$$",
        r"ול-$A$ יש $4$ עמודות, כנדרש (משפט הדרגה: מספר המשתנים החופשיים ועוד מספר העמודות המובילות שווה למספר העמודות)."),
      4, "c2"),

    # ------------------------------------------------------------------ Q3
    S(3, "א", "computation", "rank_inverse", r"עבור אילו ערכי $a$ המטריצה $A$ הפיכה?",
      J(r"$A$ הפיכה אם ורק אם $|A|\neq0$. נפתח לפי השורה הראשונה:",
        r"$$|A|=2\begin{vmatrix}a&1\\1&-a\end{vmatrix}-1\begin{vmatrix}1&1\\3&-a\end{vmatrix}+(-1)\begin{vmatrix}1&a\\3&1\end{vmatrix}=2\left(-a^2-1\right)-(-a-3)-(1-3a)$$",
        r"$$=-2a^2+4a=-2a(a-2)$$",
        r"לכן $A$ הפיכה עבור $a\neq0$ ו-$a\neq2$."),
      5, "c3a"),
    S(3, "ב", "computation", "rank_inverse", r"חשב את $A^{-1}$ עבור $a=1$.",
      J(r"עבור $a=1$: $A=" + pm("2&1&-1", "1&1&1", "3&1&-1") + r"$ ו-$|A|=-2\cdot1\cdot(1-2)=2$. נחשב את המטריצה המצורפת (מטריצת הקופקטורים המשוחלפת):",
        r"$$C_{11}=-2,\ C_{12}=4,\ C_{13}=-2,\quad C_{21}=0,\ C_{22}=1,\ C_{23}=1,\quad C_{31}=2,\ C_{32}=-3,\ C_{33}=1$$",
        r"$$A^{-1}=\frac{1}{|A|}\mathrm{adj}(A)=\frac12" + pm("-2&0&2", "4&1&-3", "-2&1&1") + "=" + pm(r"-1&0&1", r"2&\frac12&-\frac32", r"-1&\frac12&\frac12") + "$$",
        r"בדיקה: $AA^{-1}=I$ (למשל השורה הראשונה: $2\cdot(-1)+1\cdot2-1\cdot(-1)=1$, $0+\frac12-\frac12=0$, $2-\frac32-\frac12=0$)."),
      5, "c3a"),
    S(3, "ג", "computation", "eigen_diagonalization", r"מצא את כל הערכים העצמיים והווקטורים העצמיים של $A$.",
      J(r"$$|\lambda I-A|=\begin{vmatrix}\lambda-1&-1&1\\-1&\lambda-1&-1\\-1&-1&\lambda-1\end{vmatrix}$$",
        r"נחסר את השורה השלישית מהשנייה (הדטרמיננטה לא משתנה) ונקבל בשורה השנייה $(0,\ \lambda,\ -\lambda)=\lambda(0,1,-1)$:",
        r"$$|\lambda I-A|=\lambda\begin{vmatrix}\lambda-1&-1&1\\0&1&-1\\-1&-1&\lambda-1\end{vmatrix}=\lambda\left[(\lambda-1)\begin{vmatrix}1&-1\\-1&\lambda-1\end{vmatrix}+(-1)\begin{vmatrix}-1&1\\1&-1\end{vmatrix}\right]=\lambda\left[(\lambda-1)(\lambda-2)+0\right]=\lambda(\lambda-1)(\lambda-2)$$",
        r"הערכים העצמיים: $0,1,2$.",
        r"**עבור $\lambda=0$:** $A\to" + pm("1&1&-1", "0&0&2", "0&0&0") + r"$, כלומר $z=0$, $x=-y$: הווקטור העצמי $" + col(-1, 1, 0) + "$.",
        r"**עבור $\lambda=1$:** $A-I=" + pm("0&1&-1", "1&0&1", "1&1&0") + r"$, כלומר $y=z$, $x=-z$: הווקטור העצמי $" + col(-1, 1, 1) + "$.",
        r"**עבור $\lambda=2$:** $A-2I=" + pm("-1&1&-1", "1&-1&1", "1&1&-1") + r"$. מהשורות השנייה והשלישית: $x-y+z=0$ ו-$x+y-z=0$, ולכן $x=0$, $y=z$: הווקטור העצמי $" + col(0, 1, 1) + "$.",
        r"(הווקטורים העצמיים הם כל הכפולות השונות מאפס של הווקטורים האלה.)"),
      9, "c3b"),
    S(3, "ד", "computation", "eigen_diagonalization", r"מצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}AP$.",
      J(r"ל-$A$ שלושה ערכים עצמיים שונים, ולכן היא לכסינה. נשים את הווקטורים העצמיים כעמודות של $P$, באותו סדר כמו הערכים העצמיים ב-$D$:",
        "$$D=" + pm("0&0&0", "0&1&0", "0&0&2") + r",\qquad P=" + pm("-1&-1&0", "1&1&1", "0&1&1") + "$$",
        r"בדיקה: $|P|=1\neq0$, ו-$AP=PD=" + pm("0&-1&0", "0&1&2", "0&1&2") + "$."),
      6, "c3b"),

    # ------------------------------------------------------------------ Q4
    S(4, "א", "computation", "vector_spaces", r"מצא בסיס ומימד של תתי מרחבים $W_1$ ו-$W_2$.",
      J(r"**$W_1$:** נדרג מטריצה ששורותיה הן הווקטורים הפורשים (בסדר $(1,1,1),(1,2,3),(2,3,1),(3,1,2)$):",
        "$$" + pm("1&1&1", "1&2&3", "2&3&1", "3&1&2") + arrow(r"\substack{R_2\to R_2-R_1\\R_3\to R_3-2R_1\\R_4\to R_4-3R_1}") + pm("1&1&1", "0&1&2", "0&1&-1", "0&-2&-1")
        + arrow(r"\substack{R_3\to R_3-R_2\\R_4\to R_4+2R_2}") + pm("1&1&1", "0&1&2", "0&0&-3", "0&0&3") + arrow(r"R_4\to R_4+R_3") + pm("1&1&1", "0&1&2", "0&0&-3", "0&0&0") + "$$",
        r"הדרגה $3$, ולכן $W_1=\mathbb{R}^3$:",
        r"$$B_{W_1}=\left\{" + col(1, 0, 0) + "," + col(0, 1, 0) + "," + col(0, 0, 1) + r"\right\},\qquad \dim W_1=3$$",
        r"**$W_2$:** $x-y=z+y$ שקול ל-$x=2y+z$, ו-$y,z$ חופשיים:",
        r"$$" + col("x", "y", "z") + "=" + col("2y+z", "y", "z") + "=y" + col(2, 1, 0) + "+z" + col(1, 0, 1) + "$$",
        r"$$B_{W_2}=\left\{" + col(2, 1, 0) + "," + col(1, 0, 1) + r"\right\},\qquad \dim W_2=2$$"),
      6, "c4"),
    S(4, "ב", "computation", "vector_spaces", r"חשב תת מרחב $W_1+W_2$, מצא בסיס ומימד של תת מרחב זה.",
      J(r"$W_1=\mathbb{R}^3$, ולכן $W_1+W_2=\mathbb{R}^3$ (תת מרחב של $\mathbb{R}^3$ המכיל את $W_1$):",
        r"$$B_{W_1+W_2}=\left\{" + col(1, 0, 0) + "," + col(0, 1, 0) + "," + col(0, 0, 1) + r"\right\},\qquad \dim(W_1+W_2)=3$$"),
      7, "c4"),
    S(4, "ג", "computation", "vector_spaces", r"חשב תת מרחב $W_1\cap W_2$, מצא בסיס ומימד של תת מרחב זה.",
      J(r"$W_2\subseteq\mathbb{R}^3=W_1$, ולכן $W_1\cap W_2=W_2$:",
        r"$$B_{W_1\cap W_2}=\left\{" + col(2, 1, 0) + "," + col(1, 0, 1) + r"\right\},\qquad \dim(W_1\cap W_2)=2$$",
        r"בדיקה לפי משפט המימדים: $\dim(W_1+W_2)=3+2-2=3$."),
      7, "c4"),
    S(4, "ד", "computation", "vector_spaces", r"האם הווקטור $" + pm("3", "1", "-1") + r"$ שייך לתת מרחב $W_1\cap W_2$?",
      J(r"$W_1\cap W_2=W_2$, ולכן צריך לבדוק את התנאי $x-y=z+y$:",
        r"$$x-y=3-1=2,\qquad z+y=-1+1=0,\qquad 2\neq0$$",
        r"לכן הווקטור **אינו** שייך ל-$W_1\cap W_2$ (הוא שייך ל-$W_1=\mathbb{R}^3$ אך לא ל-$W_2$)."),
      5, "c4"),

    # ------------------------------------------------------------------ Q5
    S(5, "א", "proof", "linear_maps", r"הראה כי $T$ היא העתקה לינארית.",
      J(r"יהיו $\mathbf{u}=(x_1,y_1,z_1)$, $\mathbf{v}=(x_2,y_2,z_2)$ ו-$\alpha\in\mathbb{R}$. **חיבור:**",
        r"$$T(\mathbf{u}+\mathbf{v})=" + col("(x_1+x_2)-(y_1+y_2)", "-2(x_1+x_2)+2(y_1+y_2)", "2(z_1+z_2)") + "=" + col("x_1-y_1", "-2x_1+2y_1", "2z_1") + "+" + col("x_2-y_2", "-2x_2+2y_2", "2z_2") + r"=T(\mathbf{u})+T(\mathbf{v})$$",
        r"**כפל בסקלר:**",
        r"$$T(\alpha\mathbf{u})=" + col(r"\alpha x_1-\alpha y_1", r"-2\alpha x_1+2\alpha y_1", r"2\alpha z_1") + r"=\alpha" + col("x_1-y_1", "-2x_1+2y_1", "2z_1") + r"=\alpha T(\mathbf{u})$$",
        r"שני התנאים מתקיימים, ולכן $T$ העתקה לינארית."),
      6, "c5"),
    S(5, "ב", "computation", "linear_maps", r"מצא הבסיסים והמימדים של $\mathrm{Ker}(T)$ ו-$\mathrm{Im}(T)$.",
      J(r"**הגרעין:** $T(x,y,z)=\mathbf{0}$ אם ורק אם",
        r"$$\begin{cases}x-y=0\\-2x+2y=0\\2z=0\end{cases}\ \Rightarrow\ x=y,\ z=0$$",
        r"$$\mathrm{Ker}(T)=\left\{t" + col(1, 1, 0) + r":\ t\in\mathbb{R}\right\},\qquad B_{\mathrm{Ker}(T)}=\left\{" + col(1, 1, 0) + r"\right\},\qquad \dim\mathrm{Ker}(T)=1$$",
        r"**התמונה:**",
        r"$$T" + col("x", "y", "z") + "=x" + col(1, -2, 0) + "+y" + col(-1, 2, 0) + "+z" + col(0, 0, 2) + "$$",
        r"הווקטור השני הוא מינוס הראשון, ולכן $\mathrm{Im}(T)=\mathrm{Sp}\left\{" + col(1, -2, 0) + "," + col(0, 0, 1) + r"\right\}$, ושני הווקטורים בלתי תלויים:",
        r"$$B_{\mathrm{Im}(T)}=\left\{" + col(1, -2, 0) + "," + col(0, 0, 1) + r"\right\},\qquad \dim\mathrm{Im}(T)=2$$",
        r"בהתאם למשפט המימדים: $1+2=3=\dim\mathbb{R}^3$."),
      8, "c5"),
    S(5, "ג", "computation", "linear_maps", r"האם $T$ חד-חד ערכית? האם היא על? נמקו את תשובתכם.",
      J(r"$T$ **אינה** חד-חד ערכית, כי $\mathrm{Ker}(T)\neq\{\mathbf{0}\}$: למשל $T(1,1,0)=\mathbf{0}=T(\mathbf{0})$.",
        r"$T$ **אינה** על, כי $\dim\mathrm{Im}(T)=2<3=\dim\mathbb{R}^3$ (למשל $(1,0,0)\notin\mathrm{Im}(T)$, כי בתמונה הרכיב השני הוא תמיד $-2$ כפול הראשון)."),
      4, "c5"),
    S(5, "ד", "computation", "linear_maps",
      r"מצא את המטריצה המייצגת $T_{B_2}^{B_1}$ של ההעתקה ביחס לבסיסים $B_1=\left\{" + pm("1", "1", "1") + "," + pm("0", "1", "1") + "," + pm("0", "0", "1") + r"\right\}$ ו-$B_2=\left\{" + pm("1", "0", "0") + "," + pm("0", "1", "1") + "," + pm("1", "1", "0") + r"\right\}$.",
      J(r"העמודה ה-$i$ של $T_{B_2}^{B_1}$ היא וקטור הקואורדינטות לפי $B_2$ של התמונה של הווקטור ה-$i$ ב-$B_1$. התמונות:",
        r"$$T" + col(1, 1, 1) + "=" + col(0, 0, 2) + r",\qquad T" + col(0, 1, 1) + "=" + col(-1, 2, 2) + r",\qquad T" + col(0, 0, 1) + "=" + col(0, 0, 2) + "$$",
        r"קואורדינטות לפי $B_2$ של וקטור כללי $(p,q,r)$: מ-$\alpha" + col(1, 0, 0) + r"+\beta" + col(0, 1, 1) + r"+\gamma" + col(1, 1, 0) + "=" + col("p", "q", "r") + r"$ נקבל $\alpha+\gamma=p$, $\beta+\gamma=q$, $\beta=r$, כלומר",
        r"$$\beta=r,\qquad \gamma=q-r,\qquad \alpha=p-q+r$$",
        r"לכן $[(0,0,2)]_{B_2}=(2,2,-2)$ ו-$[(-1,2,2)]_{B_2}=(-1,2,0)$, ו-",
        r"$$T_{B_2}^{B_1}=" + pm("2&-1&2", "2&2&2", "-2&0&-2") + "$$",
        r"בדיקה לעמודה השנייה: $-1" + col(1, 0, 0) + "+2" + col(0, 1, 1) + "+0" + col(1, 1, 0) + "=" + col(-1, 2, 2) + "$."),
      7, "c5"),
]


exam = {
    "examCode": "20A-A",
    "examLabel": "מבחן סוף סמסטר א׳ תש״פ, מועד א׳ (16.02.2020)",
    "year": 2020,
    "examDate": "16.02.2020",
    "sourceFile": "20A-A exam (PDF, 2pp, exam only)",
    "solutionFile": "none",
    "contexts": contexts,
    "questions": questions,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
