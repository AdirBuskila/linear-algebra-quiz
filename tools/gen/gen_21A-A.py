# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-A.json -- linear algebra, semester A 2021, moed A (24.01.2021), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-A.py

Source: one PDF (3pp, exam only; page 3 is blank). There is NO answer source for this sitting (GATE1: 21A-A has no
solution), so every item is held "no-key" for the solver. The questions are transcribed in full.
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

questions = [
    H(1, "א", "proof", "matrix_proofs", r"הראו כי $A$ הפיכה ע״י מציאת ביטוי של המטריצה ההפוכה באמצעות $A$.", 7, "c1"),
    H(1, "ב", "proof", "matrix_proofs", r"הוכיחו כי $A^{-1}$ מטריצה סימטרית.", 7, "c1"),
    H(1, "ג", "computation", "determinants", r"חשבו את הדטרמיננטה $|A|$.", 7, "c1"),
    H(1, "ד", "computation", "determinants", r"חשבו את הדטרמיננטה $\left|A^{-1}\right|$.", 4, "c1"),

    H(2, "א", "computation", "linear_systems", r"הביאו את המטריצה המורחבת של המערכת לצורת מדורגת קנונית.", 9, "c2"),
    H(2, "ב", "computation", "linear_systems", r"מצאו עבור אילו ערכי $a$ יש למערכת אינסוף פתרונות, פתרון יחיד או שאין לה פתרון כלל.", 8, "c2"),
    H(2, "ג", "computation", "linear_systems", r"עבור $a=-1$ פתרו את המערכת וכתבו את כל הפתרונות.", 4, "c2"),
    H(2, "ד", "computation", "complex_numbers", r"מצאו את כל הפתרונות המרוכבים של המשוואה $z^4+8z=0$.", 4),

    H(3, "א", "computation", "rank_inverse", r"עבור אילו ערכי $a$ המטריצה $A$ הפיכה?", 6, "c3a"),
    H(3, "ב", "computation", "rank_inverse", r"מצאו את $A^{-1}$ עבור $a=2$.", 6, "c3a"),
    H(3, "ג", "computation", "eigen_diagonalization", r"מצאו את כל הערכים העצמיים והווקטורים העצמיים של $B$.", 8, "c3b"),
    H(3, "ד", "computation", "eigen_diagonalization", r"מצאו את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$.", 5, "c3b"),

    H(4, "א", "computation", "vector_spaces", r"מצאו בסיס ומימד של תתי המרחבים $U$ ו-$W$.", 6, "c4"),
    H(4, "ב", "computation", "vector_spaces", r"חשבו תת מרחב $U+W$, מצאו בסיס ומימד של תת מרחב זה.", 8, "c4"),
    H(4, "ג", "computation", "vector_spaces", r"חשבו תת מרחב $U\cap W$, מצאו בסיס ומימד של תת מרחב זה.", 8, "c4"),
    H(4, "ד", "computation", "vector_spaces", r"יהי $q(x)$ פולינום כלשהו השייך לתת מרחב $U\cap W$. מצאו $q(2)+q(-2)$.", 3, "c4"),

    H(5, "א", "proof", "linear_maps", r"הוכיחו כי $T$ היא העתקה לינארית.", 6, "c5"),
    H(5, "ב", "computation", "linear_maps", r"מצאו את הבסיסים והמימדים של $\mathrm{Ker}(T)$ ו-$\mathrm{Im}(T)$.", 9, "c5"),
    H(5, "ג", "computation", "linear_maps", r"האם $T$ חד-חד ערכית? האם היא על? נמקו את תשובתכם.", 3, "c5"),
    H(5, "ד", "computation", "linear_maps",
      r"מצאו את כל המטריצות ב-$\mathbb{M}_2(\mathbb{R})$ שתמונתם נותנת וקטור $" + pm("1", "1", "1") + r"$. האם הן מהוות תת מרחב של $\mathbb{M}_2(\mathbb{R})$?", 7, "c5"),
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
