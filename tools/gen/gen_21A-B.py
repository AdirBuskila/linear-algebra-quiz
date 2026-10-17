# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-B.json -- linear algebra, semester A 2021, moed B (22.02.2021), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-B.py

Source: one PDF (4pp, exam only; page 4 is blank). There is NO answer source for this sitting (GATE1: 21A-B has no
solution), so every item is held "no-key" for the solver. The questions are transcribed in full.
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

questions = [
    H(1, "א", "proof", "matrix_proofs", r"הראו כי $\det A=0$.", 7, "c1a"),
    H(1, "ב", "proof", "matrix_proofs", r"האם $B$ הפיכה? נמקו!", 6, "c1a"),
    H(1, "ג", "computation", "vector_spaces", r"מצאו בסיס ומימד של מרחב העמודות של $C$ כאשר היא איננה הפיכה.", 6, "c1b"),
    H(1, "ד", "computation", "vector_spaces", r"בנו בסיס של $\mathbb{R}^3$ שמכיל בתוכו בסיס של מרחב העמודות של $C$ מסעיף א׳.", 6, "c1b"),

    H(2, "א", "computation", "linear_systems", r"הביאו את מטריצת המקדמים המורחבת של המערכת לצורה מדורגת.", 7, "c2"),
    H(2, "ב", "computation", "linear_systems", r"מצאו עבור אילו ערכי $a,b$ יש למערכת אינסוף פתרונות, פתרון יחיד או שאין לה פתרון כלל.", 4, "c2"),
    H(2, "ג", "computation", "linear_systems", r"עבור $a=2$ ו-$b=1$ פתרו את המערכת וכתבו את כל הפתרונות.", 4, "c2"),
    H(2, "ד", "computation", "linear_systems", r"עבור $a=-1$ ו-$b=4$ פתרו את המערכת וכתבו את כל הפתרונות.", 4, "c2"),
    H(2, "ה", "computation", "complex_numbers", r"הראו שלמשוואה $4z=\overline{z}^{\,2}$ יש ארבעה פתרונות, כתבו את כולם.", 6),

    H(3, "א", "computation", "rank_inverse", r"כתבו את $A^{-1}$ כמכפלה של מטריצות אלמנטריות.", 8, "c3a"),
    H(3, "ב", "computation", "eigen_diagonalization", r"מצאו את כל הערכים העצמיים והווקטורים העצמיים של $B$.", 9, "c3b"),
    H(3, "ג", "computation", "eigen_diagonalization", r"האם $B$ ניתנת ללכסון? אם כן, מצאו את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}BP$. אם לא, אז נמקו למה!", 8, "c3b"),

    H(4, "א", "computation", "vector_spaces", r"מצאו בסיס ומימד של תתי המרחבים $V$ ו-$W$.", 6, "c4"),
    H(4, "ב", "computation", "vector_spaces", r"חשבו תת מרחב $V+W$, מצאו בסיס ומימד של תת מרחב זה.", 8, "c4"),
    H(4, "ג", "computation", "vector_spaces", r"חשבו תת מרחב $V\cap W$, מצאו בסיס ומימד של תת מרחב זה.", 8, "c4"),
    H(4, "ד", "computation", "vector_spaces",
      r"האם הווקטור $" + pm("1", "3", "2") + r"$ שייך לתת מרחב $V\cap W$? האם הוא שייך לתת מרחב $V+W$?", 3, "c4"),

    H(5, "א", "proof", "linear_maps", r"הוכיחו כי $T$ היא העתקה לינארית.", 7, "c5"),
    H(5, "ב", "computation", "linear_maps", r"מצאו את הבסיס והמימד של $\mathrm{Ker}(T)$.", 8, "c5"),
    H(5, "ג", "computation", "linear_maps", r"מצאו את הבסיס והמימד של $\mathrm{Im}(T)$.", 8, "c5"),
    H(5, "ד", "computation", "linear_maps", r"האם $T$ היא העתקה הפיכה? נמקו!", 2, "c5"),
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
