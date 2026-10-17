# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-B.json -- linear algebra, semester A 2023, moed B (23.02.2023), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-B.py

Source: one PDF (8pp): the exam text followed question by question by the typed official solution.
Five questions of 25 points (best 4 count), 19 items. No figures.

Transcription notes
- Q3 has two numbered items: item 1 (A, parts a,b) and item 2 (B); in the raw schema item 2 is part "gimel".
- Q2 d: the official lists z_4 = 5^(1/6) cis(300.86); the third cube root is (206.57+720)/3 = 308.86 degrees. Final-answer
  slip, so the item ships with the minimal fix, solutionSource "solved", official False and a visible "official with
  correction" prefix. The official also prints "sqrt5 cis(tan^-1(1/2)) = sqrt5 cis(206.57)" (the principal value is 26.57,
  the solution then explains the quadrant); the explanation is kept, no label needed.
- Q3 item 2: the exam asks for BP=PD; the official writes PD=BP. Same statement.

Checks (sympy, tools/verify/23A-B/verify_23A-B.py): the echelon form and the three cases of Q2, the general solution (t,-2,3),
the roots of Q2 d (with 308.86), A^-1 and its elementary product, charpoly, P and D with BP=PD, dims and bases of U, W, U+W,
U cap W, Ker/Im T, p=10 q=0, [T]_C^B by both methods. Only mismatch: the 300.86 above. No hold.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-B.json"


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
           "text": J(r"נתונה מערכת המשוואות כאשר $a$ הוא פרמטר ממשי:",
                     r"$$\begin{cases} ax+2ay+3az=4a\\ ax+(2a+1)y+(3a+1)z=4a+1\\ ax+(2a-1)y=2-a\end{cases}$$")},
    "c3": {"kind": "text", "title": "שאלה 3 - סעיפים א ו-ב",
           "text": r"נתונה המטריצה $A=" + pm("1&-2&-2", "0&-1&0", "-1&2&3") + r"$."},
    "c4": {"kind": "text", "title": "שאלה 4 - תתי מרחבים של פולינומים",
           "text": J(r"יהי $V=\mathbb{R}_3[x]$ מרחב הפולינומים עם מקדמים ממשיים ממעלה 3 לכל היותר. נגדיר שתי תתי-קבוצות של $V$, $U$ ו-$W$, באופן הבא:",
                     r"$U=\{p(x)\in\mathbb{R}_3[x]\mid p(1)=p'(1)\}$",
                     r"$W=\{p(x)\in\mathbb{R}_3[x]\mid p(x)=p(-x)\}$")},
    "c5": {"kind": "text", "title": "שאלה 5 - ההעתקה T",
           "text": J(r"נתונה העתקה לינארית $T:\mathbb{R}^4\to\mathbb{R}_3[t]$ המוגדרת על ידי:",
                     r"$$T" + pm("1", "0", "0", "0") + r"=1+x+x^2+x^3,\ T" + pm("0", "1", "0", "0") + r"=1+x+2x^2+3x^3,$$",
                     r"$$T" + pm("0", "0", "1", "0") + r"=3+3x+4x^2+5x^3,\ T" + pm("0", "0", "0", "1") + r"=1+x+x^2+5x^3$$")},
}

questions = []

# ------------------------------------------------------------------ Q1
questions.append(Q(
    1, "א", "proof", "matrix_proofs",
    r"תהי $A$ מטריצה ריבועית המקיימת את $A^3-A+I=0$. הוכיחו שהיא הפיכה.",
    J(r"$$A^3-A+I=0\ \Rightarrow\ A-A^3=I\ \Rightarrow\ A(I-A^2)=I\ \Rightarrow\ A^{-1}=I-A^2$$",
      r"כלומר $A$ הפיכה, וההופכית שלה היא $I-A^2$."),
    6))

questions.append(Q(
    1, "ב", "proof", "matrix_proofs",
    r"נתון ש-$C^m=0$ ו-$B^k=0$, כאשר $B,C$ מטריצות ריבועיות מאותו סדר ו-$m,k\in\mathbb{N}$ (טבעיים). הוכיחו שאם מתקיים $BC=CB$, אז קיים מספר טבעי $n$ כזה שיתקיים $(BC)^n=0$.",
    J(r"$$(BC)^n=(BC)(BC)\cdots(BC)=B^nC^n$$",
      r"(השוויון האחרון נכון כי $BC=CB$.) ברור שאם ניקח $n\geq k$ אז $B^n=0$ ולכן $(BC)^n=0$. אם ניקח $n\geq m$, אז $C^n=0$ ושוב מקבלים $(BC)^n=0$."),
    7))

questions.append(Q(
    1, "ג", "proof", "matrix_proofs",
    r"נתון ש-$DE=0$ כאשר $D\neq0$ ו-$E\neq0$ הן מטריצות ריבועיות מאותו סדר. הוכיחו ש-$D$ ו-$E$ שתיהן מטריצות לא הפיכות.",
    J(r"נניח ש-$D$ הפיכה, כלומר קיימת לה $D^{-1}$. אז, אם נכפול את השוויון $DE=0$ משמאל ב-$D^{-1}$, אז נקבל",
      r"$$E=IE=D^{-1}DE=D^{-1}\cdot 0=0$$",
      r"בסתירה לנתון.",
      r"מצד שני, אם נניח ש-$E$ הפיכה וקיימת לה $E^{-1}$. אז, נכפול את השוויון $DE=0$ מימין ב-$E^{-1}$ ונקבל",
      r"$$D=DI=DEE^{-1}=0\cdot E^{-1}=0$$",
      r"בסתירה לנתון. זה מוכיח ש-$D$ ו-$E$ שתיהן לא הפיכות."),
    5))

questions.append(Q(
    1, "ד", "proof", "eigen_diagonalization",
    r"תהי $F$ מטריצה ריבועית מסדר 2 בעלת הערכים העצמיים $\lambda_1$ ו-$\lambda_2$. הוכיחו שלמטריצה משוחלפת $F^T$ יש אותם הערכים העצמיים.",
    J(r"נסמן $F=" + pm("a&b", "c&d") + r"$. ידוע שהערכים העצמיים של $F$ מהווים שורשים של הפולינום האופייני שלה, כלומר שורשים של",
      r"$$\det(F-\lambda I)=\begin{vmatrix}a-\lambda&b\\c&d-\lambda\end{vmatrix}=\lambda^2-(a+d)\lambda+ad-bc$$",
      r"אז $F^T=" + pm("a&c", "b&d") + r"$ והפולינום האופייני שלה",
      r"$$\det(F^T-\lambda I)=\begin{vmatrix}a-\lambda&c\\b&d-\lambda\end{vmatrix}=\lambda^2-(a+d)\lambda+ad-bc$$",
      r"הוא זהה לחלוטין לפולינום האופייני של $F$ ולכן בעל אותם השורשים בדיוק."),
    7))

# ------------------------------------------------------------------ Q2
R0 = [["a", "2a", "3a", "4a"], ["a", "2a+1", "3a+1", "4a+1"], ["a", "2a-1", "0", "2-a"]]
R1 = [["a", "2a", "3a", "4a"], ["0", "1", "1", "1"], ["0", "-1", "-3a", "2-5a"]]
R2 = [["a", "2a", "3a", "4a"], ["0", "1", "1", "1"], ["0", "0", "1-3a", "3-5a"]]
ECH = J(r"ראשית נבנה את המטריצה המורחבת המתאימה למערכת ונדרג אותה:",
        "$$" + aug(R0) + arrow(r"\substack{R_2\to R_2-R_1\\R_3\to R_3-R_1}") + aug(R1) + arrow(r"R_3\to R_3+R_2") + aug(R2) + "$$")

questions.append(Q(
    2, "א", "computation", "linear_systems",
    r"הציגו את המערכת בעזרת מטריצה מורחבת ודרגו אותה.",
    ECH,
    9, contextId="c2"))

questions.append(Q(
    2, "ב", "computation", "linear_systems",
    r"עבור איזה ערך של הפרמטר $a$ אין פתרון למערכת? יש פתרון יחיד? יש אינסוף פתרונות שונים?",
    J(r"נעזר במטריצה המדורגת מסעיף א.",
      r"**אין פתרון:** עבור $a=\frac{1}{3}$ שורה שלישית היא שורת סתירה $\left(0\ \ 0\ \ 0\ \middle|\ \frac{4}{3}\right)$ ולכן במקרה זה אין פתרון.",
      r"**פתרון יחיד:** אם $a\neq\frac{1}{3},\ a\neq0$ אז בכל אחת מהעמודות 1,2,3 יש מקדם מוביל, ולכן כל הנעלמים $x,y,z$ הם משתנים מובילים (קשורים) ולכן למערכת **פתרון יחיד**. (הערה: דרך אחרת לטפל במקרה זה היא לחשב את הדטרמיננטה של מטריצת המקדמים המצומצמת, לקבל $a(1-3a)$ ולהסיק אותה מסקנה.)",
      r"**אינסוף פתרונות:** נותרה רק האפשרות $a=0$. נציב במטריצה שהגענו אליה ונמשיך לדרג:",
      r"$$" + pm("0&0&0&0", "0&1&1&1", "0&0&1&3") + arrow(r"R_2\to R_2-R_3") + pm("0&0&0&0", "0&1&0&-2", "0&0&1&3") + "$$",
      r"ובהחלפת שורות מתקבל:",
      r"$$" + pm("0&1&0&-2", "0&0&1&3", "0&0&0&0") + "$$",
      r"קיבלנו כי עבור $a=0$ המערכת שקולה למערכת המשוואות $\begin{cases}y=-2\\z=3\end{cases}$ ואילו $x$ משתנה חופשי ולכן יש למערכת **אינסוף פתרונות** במקרה זה."),
    5, contextId="c2"))

questions.append(Q(
    2, "ג", "computation", "linear_systems",
    r"מצאו פתרון כללי של המערכת כאשר קיימים אינסוף פתרונות.",
    r"נציב במקום המשתנה החופשי $x$ פרמטר $t$ ונקבל את הפתרון הכללי $\{(t,-2,3)\mid t\in\mathbb{R}\}$ שהוא ישר במרחב.",
    5, contextId="c2"))

SOL_2D = J(r"נרשום את המשוואה כ-$z\left(z^3+(2+i)\right)=0$. לכן $z_1=0$ הוא פתרון ראשון שלה, וכעת יש לפתור את המשוואה $z^3=-2-i$. ראשית, נמיר את $-2-i$ לצורה טריגונומטרית:",
           r"$$-2-i=\sqrt{2^2+1^2}\,\mathrm{cis}\left(\tan^{-1}\frac{1}{2}\right)=\sqrt5\,\mathrm{cis}(206.57)$$",
           r"(לטנגנס יש שני פתרונות בתחום 0 עד 360: 26.57 וכן 206.57 בגלל המחזוריות של 180. מכיוון שהמספר המרוכב נמצא ברבע השלישי, בחרנו את הזוית 206.57.)",
           r"יהי $z=r\,\mathrm{cis}(\theta)$ פתרון של $z^3=-2-i$. ולכן $z^3=r^3\,\mathrm{cis}(3\theta)=\sqrt5\,\mathrm{cis}(206.57)$, ומכאן ש-$r=\sqrt[6]{5}$ ו-$\theta=\frac{206.57}{3}+\frac{360k}{3}$, כאשר $k=0,1,2$, ומכאן שהפתרונות למשוואה $z^3=-2-i$ הם:",
           r"$$z_2=\sqrt[6]{5}\,\mathrm{cis}(68.86),\qquad z_3=\sqrt[6]{5}\,\mathrm{cis}(188.86),\qquad z_4=\sqrt[6]{5}\,\mathrm{cis}(308.86)$$",
           r"**הערה:** בפתרון הרשמי כתוב $\mathrm{cis}(300.86)$ עבור $z_4$; הערך הנכון הוא $\frac{206.57+720}{3}=308.86$.")
questions.append(Q(
    2, "ד", "computation", "complex_numbers",
    r"מצאו את כל הפתרונות המרוכבים של $z^4+(2+i)z=0$.",
    "**הפתרון הרשמי עם תיקון:** זווית הפתרון הרביעי תוקנה מ-300.86 ל-308.86.\n" + SOL_2D,
    6, contextId="c2", solutionSource="solved", official=False))

# ------------------------------------------------------------------ Q3
Ai_aug = [
    (aug([["1", "-2", "-2", "1", "0", "0"], ["0", "-1", "0", "0", "1", "0"], ["-1", "2", "3", "0", "0", "1"]]), r"R_3\to R_3+R_1"),
    (aug([["1", "-2", "-2", "1", "0", "0"], ["0", "-1", "0", "0", "1", "0"], ["0", "0", "1", "1", "0", "1"]]), r"R_2\to-R_2"),
    (aug([["1", "-2", "-2", "1", "0", "0"], ["0", "1", "0", "0", "-1", "0"], ["0", "0", "1", "1", "0", "1"]]), r"R_1\to R_1+2R_3"),
    (aug([["1", "-2", "0", "3", "0", "2"], ["0", "1", "0", "0", "-1", "0"], ["0", "0", "1", "1", "0", "1"]]), r"R_1\to R_1+2R_2"),
    (aug([["1", "0", "0", "3", "-2", "2"], ["0", "1", "0", "0", "-1", "0"], ["0", "0", "1", "1", "0", "1"]]), None),
]
inv_chain = "$$" + "".join(m + (arrow(op) if op else "") for m, op in Ai_aug) + "$$"
AINV = pm("3&-2&2", "0&-1&0", "1&0&1")

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
      r"$$A^{-1}=" + pm("1&2&0", "0&1&0", "0&0&1") + pm("1&0&2", "0&1&0", "0&0&1") + pm("1&0&0", "0&-1&0", "0&0&1") + pm("1&0&0", "0&1&0", "1&0&1") + "$$"),
    7, contextId="c3"))

B3 = pm("3&1&1", "1&3&1", "0&0&2")
questions.append(Q(
    3, "ג", "computation", "eigen_diagonalization",
    r"נתונה מטריצה $B=" + B3 + r"$. האם $B$ ניתנת לליכסון? במידה וכן, מצאו מטריצה הפיכה $P$ ומטריצה אלכסונית $D$ כך שמתקיים $BP=PD$.",
    J(r"תחילה נמצא את כל הערכים העצמיים והווקטורים העצמיים של $B$. נחשב את הדטרמיננטה הבאה לפי שורה שלישית:",
      r"$$|\lambda I-B|=\begin{vmatrix}\lambda-3&-1&-1\\-1&\lambda-3&-1\\0&0&\lambda-2\end{vmatrix}=(\lambda-2)\begin{vmatrix}\lambda-3&-1\\-1&\lambda-3\end{vmatrix}=(\lambda-2)\left[(\lambda-3)^2-1\right]=(\lambda-2)(\lambda^2-6\lambda+8)=(\lambda-2)(\lambda-2)(\lambda-4)$$",
      r"קיבלנו שהערכים העצמיים הם: $2,2,4$. כעת נמצא את הווקטורים העצמיים.",
      r"**עבור ע״ע 2:**",
      r"$$" + pm("-1&-1&-1", "-1&-1&-1", "0&0&0") + r"\to\cdots\to" + pm("1&1&1", "0&0&0", "0&0&0") + "$$",
      r"נסמן $y=t,\ z=s$ ונקבל $x=-t-s$. הווקטורים העצמיים המתקבלים הם $(-1,1,0)^T,\ (-1,0,1)^T$.",
      r"**עבור ע״ע 4:**",
      r"$$" + pm("1&-1&-1", "-1&1&-1", "0&0&2") + r"\to\cdots\to" + pm("1&-1&0", "0&0&1", "0&0&0") + "$$",
      r"נסמן $y=t$ ונקבל $x=t,\ z=0$. הווקטור העצמי המתקבל הוא $(1,1,0)^T$.",
      r"המטריצה ניתנת לליכסון (שלושה וקטורים עצמיים בלתי תלויים). כעת נמצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $PD=BP$:",
      r"$$D=" + pm("2&0&0", "0&2&0", "0&0&4") + r",\qquad P=" + pm("-1&-1&1", "1&0&1", "0&1&0") + "$$"),
    12))

# ------------------------------------------------------------------ Q4
questions.append(Q(
    4, "א", "computation", "vector_spaces",
    r"הראו ש-$U$ הוא תת מרחב של $V$, ומצאו לו בסיס ומימד.",
    J(r"האיבר הכללי במרחב הפולינומים $\mathbb{R}_3[x]$ הוא מהצורה $p(x)=ax^3+bx^2+cx+d$, $p'(x)=3ax^2+2bx+c$. תת-הקבוצה $U$ מוגדרת ע״י אילוץ אחד:",
      r"$$p(1)=a+b+c+d=3a+2b+c=p'(1)\ \Rightarrow\ d=2a+b$$",
      r"לפיכך האיבר הכללי ב-$U$ הוא מהצורה $p(x)=a\left(x^3+2\right)+b\left(x^2+1\right)+cx$. לפיכך אנו רואים שזהו אכן מרחב וקטורי, עם בסיס בלתי תלוי לינארית:",
      r"$$\dim U=3,\qquad U=\mathrm{Sp}\left\{x^3+2,\ x^2+1,\ x\right\}$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ב", "computation", "vector_spaces",
    r"הראו ש-$W$ הוא תת מרחב של $V$, ומצאו לו בסיס ומימד.",
    J(r"תת-הקבוצה $W$ גם היא מוגדרת ע״י אילוץ אחד, והוא שכל הפולינומים חייבים להיות זוגיים:",
      r"$$p(x)=ax^3+bx^2+cx+d=-ax^3+bx^2-cx+d=p(-x)\ \Rightarrow\ ax^3+cx=0\ \Rightarrow\ p(x)=bx^2+d$$",
      r"לפיכך האיבר הכללי ב-$W$ הוא כל פולינום זוגי. אנו רואים שזהו אכן מרחב וקטורי, עם בסיס בלתי תלוי לינארית:",
      r"$$\dim W=2,\qquad W=\mathrm{Sp}\left\{x^2,\ 1\right\}$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ג", "computation", "vector_spaces",
    r"מצאו את הבסיס והמימד של $U+W$.",
    J(r"קל לחשב את בסיס הסכום $U+W$ לפי בחינת איחוד הבסיסים והשוואתם:",
      r"$$U+W=\mathrm{Sp}\left\{x^2,1,x^3+2,x^2+1,x\right\}=\mathrm{Sp}\left\{x^3,x^2,x,1\right\}=\mathbb{R}_3[x]\ \Rightarrow\ \dim(U+W)=4$$"),
    6, contextId="c4"))

questions.append(Q(
    4, "ד", "computation", "vector_spaces",
    r"מצאו את הבסיס והמימד של $U\cap W$, והראו שמתקיים משפט המימדים.",
    J(r"את החיתוך $U\cap W$ נקבל מהשוואת הצירופים הלינאריים:",
      r"$$a\left(x^3+2\right)+b\left(x^2+1\right)+cx=dx^2+e$$",
      r"$$\Rightarrow\ ax^3+x^2(b-d)+cx+(2a+b-e)=0\ \Rightarrow\ a=0,\ b=d,\ c=0$$",
      r"לפיכך $\dim(U\cap W)=1$, $U\cap W=\mathrm{Sp}\left\{x^2+1\right\}$, וכן",
      r"$$\dim(U+W)=\dim(U)+\dim(W)-\dim(U\cap W)\ \Rightarrow\ 4=3+2-1$$"),
    7, contextId="c4"))

# ------------------------------------------------------------------ Q5
questions.append(Q(
    5, "א", "computation", "linear_maps",
    r"מצאו את המימד והבסיס של $\mathrm{Im}\,T$, $\mathrm{Ker}\,T$.",
    J(r"נסמן ב-$F=\left(1,x,x^2,x^3\right)$ בסיס סטנדרטי של $\mathbb{R}_3[t]$ ו-$E$ בסיס סטנדרטי של $\mathbb{R}^4$. מטריצה מייצגת סטנדרטית היא",
      r"$$A=[T]_F^E=" + pm("1&1&3&1", "1&1&3&1", "1&2&4&1", "1&3&5&5") + "$$",
      "$$" + aug([["1", "1", "3", "1", "0"], ["1", "1", "3", "1", "0"], ["1", "2", "4", "1", "0"], ["1", "3", "5", "5", "0"]], 4)
      + r"\to" + aug([["1", "1", "3", "1", "0"], ["0", "0", "0", "0", "0"], ["0", "1", "1", "0", "0"], ["0", "2", "2", "4", "0"]], 4)
      + r"\to" + aug([["1", "1", "3", "1", "0"], ["0", "1", "1", "0", "0"], ["0", "1", "1", "2", "0"], ["0", "0", "0", "0", "0"]], 4)
      + r"\to" + aug([["1", "1", "3", "1", "0"], ["0", "1", "1", "0", "0"], ["0", "0", "0", "2", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$",
      r"עמודות מס׳ 1,2,4 של המטריצה המדורגת מובילות, אז בסיס של $\mathrm{Col}\,A$ הוא $\left\{" + pm("1", "1", "1", "1") + "," + pm("1", "1", "2", "3") + "," + pm("1", "1", "1", "5") + r"\right\}$, כלומר בסיס של $\mathrm{Im}\,T$ הוא $\left(1+x+x^2+x^3,\ 1+x+2x^2+3x^3,\ 1+x+x^2+5x^3\right)$ ואז $\dim\mathrm{Im}\,T=3$.",
      "$$" + aug([["1", "1", "3", "1", "0"], ["0", "1", "1", "0", "0"], ["0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0"]], 4)
      + r"\to" + aug([["1", "1", "3", "0", "0"], ["0", "1", "1", "0", "0"], ["0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0"]], 4)
      + r"\to" + aug([["1", "0", "2", "0", "0"], ["0", "1", "1", "0", "0"], ["0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0"]], 4) + "$$",
      r"$$\Rightarrow\begin{cases}x_1=-2t\\x_2=-t\\x_3=t\\x_4=0\end{cases}\Rightarrow" + pm("x_1", "x_2", "x_3", "x_4") + "=t" + pm("-2", "-1", "1", "0") + "$$",
      r"אז בסיס של $\mathrm{Ker}\,T$ (בסיס של $\mathrm{Nul}\,A$) הוא $\left\{" + pm("-2", "-1", "1", "0") + r"\right\}$ ואז $\dim\mathrm{Ker}\,T=1$."),
    10, contextId="c5"))

questions.append(Q(
    5, "ב", "computation", "linear_maps",
    r"האם $T$ היא חד חד ערכית? האם $T$ היא על? נמקו!",
    r"$T$ לא חד חד ערכית כי $\dim\mathrm{Ker}\,T=1\neq0$, ו-$T$ לא על כי $\dim\mathrm{Im}\,T=3\neq4=\dim\mathbb{R}_3[t]$.",
    3, contextId="c5"))

questions.append(Q(
    5, "ג", "computation", "linear_maps",
    r"לאילו ערכים של פרמטרים $p,q$ מתקיים $" + pm("p", "5", "-5", "q") + r"\in\mathrm{Ker}\,T$?",
    r"$$" + pm("p", "5", "-5", "q") + "=t" + pm("-2", "-1", "1", "0") + r"\ \Rightarrow\ \begin{cases}p=-2t\\5=-t\\-5=t\\q=0\end{cases}\ \Rightarrow\ t=-5\ \Rightarrow\ p=10,\ q=0$$",
    5, contextId="c5"))

questions.append(Q(
    5, "ד", "computation", "linear_maps",
    r"מצאו את המטריצה המייצגת $[T]_C^B$ ($M_{C\leftarrow B}(T)$) של $T$ ביחס לבסיסים $B$ ו-$C$ נתונים, אם $B=\left(" + ",".join(pm(*c) for c in [("1", "1", "0", "0"), ("0", "1", "1", "0"), ("0", "0", "1", "1"), ("0", "0", "0", "1")]) + r"\right)$ בסיס של $\mathbb{R}^4$ ו-$C=\left(x^3,1,x^2,x\right)$ בסיס של $\mathbb{R}_3[t]$.",
    J(r"**שיטה 1.**",
      r"$$[T]_C^B=[I]_C^F[T]_F^E[I]_E^B=" + pm("0&0&0&1", "1&0&0&0", "0&0&1&0", "0&1&0&0") + pm("1&1&3&1", "1&1&3&1", "1&2&4&1", "1&3&5&5") + pm("1&0&0&0", "1&1&0&0", "0&1&1&0", "0&0&1&1") + "=$$",
      r"$$=" + pm("1&3&5&5", "1&1&3&1", "1&2&4&1", "1&1&3&1") + pm("1&0&0&0", "1&1&0&0", "0&1&1&0", "0&0&1&1") + "=" + pm("4&8&10&5", "2&4&4&1", "3&6&5&1", "2&4&4&1") + "$$",
      r"**שיטה 2.**",
      r"$$\left[T" + pm("1", "1", "0", "0") + r"\right]_C=\left[" + pm("2", "2", "3", "4") + r"\right]_C=" + pm("4", "2", "3", "2") + r",\qquad \left[T" + pm("0", "1", "1", "0") + r"\right]_C=\left[" + pm("4", "4", "6", "8") + r"\right]_C=" + pm("8", "4", "6", "4") + "$$",
      r"$$\left[T" + pm("0", "0", "1", "1") + r"\right]_C=\left[" + pm("4", "4", "5", "10") + r"\right]_C=" + pm("10", "4", "5", "4") + r",\qquad \left[T" + pm("0", "0", "0", "1") + r"\right]_C=\left[" + pm("1", "1", "1", "5") + r"\right]_C=" + pm("5", "1", "1", "1") + "$$",
      r"$$[T]_C^B=" + pm("4&8&10&5", "2&4&4&1", "3&6&5&1", "2&4&4&1") + "$$"),
    7, contextId="c5"))

exam = {
    "examCode": "23A-B",
    "examLabel": "מבחן סוף סמסטר א׳ תשפ״ג, מועד ב׳ (23.02.2023)",
    "year": 2023,
    "examDate": "23.02.2023",
    "sourceFile": "23A-B exam + official solution (PDF)",
    "solutionFile": "23A-B exam + official solution (PDF)",
    "contexts": contexts,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
