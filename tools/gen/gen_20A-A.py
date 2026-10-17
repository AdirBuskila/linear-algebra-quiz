# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-A.json -- linear algebra, semester A 2020, moed A (16.02.2020), bank sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20A-A.py

Source: one PDF (2pp, exam only). There is NO answer source for this sitting, so every item is held "no-key" for the solver.
The questions are transcribed in full. Five questions of 25 points (best 4 count), 20 items. No figures.

Why no key: the file triage paired with this exam ("סמ׳ א מועד א פתרון.pdf" in the 2020 folder, 14pp) is NOT the solution of
this exam. Its questions (AA^T+A^2=3I, the system x-y-az=a, A with 2a/3/6, B=(6 0 2;1 4 0;0 0 3), W,U in R_2[x], T on
M_2x2) are exactly the questions of 21A-A (24.01.2021). It contains no planes pi_1, pi_2 with k, no z^5=3i+5, no W_1,W_2 in R^3
and no T(x,y,z)=(x-y,-2x+2y,2z). It is reported to the orchestrator as a candidate key source for 21A-A.

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

questions = [
    H(1, "א", "computation", "lines_planes", r"חשב את ערכו של $k$ כך שהמישורים יהיו מקבילים וחשב את המרחק ביניהם.", 6, "c1"),
    H(1, "ב", "computation", "lines_planes", r"חשב את ערכו של $k$ כך שהמישורים יהיו מאונכים.", 6, "c1"),
    H(1, "ג", "computation", "lines_planes", r"עבור $k=2$ מצא מישור שמאונך ל-$\pi_1$ ו-$\pi_2$ ועובר דרך הנק׳ $(1,1,1)$.", 7, "c1"),
    H(1, "ד", "computation", "complex_numbers", r"פתור את המשוואה $z^5=3i+5$.", 6),

    H(2, "א", "computation", "vector_spaces", r"נגדיר את **מרחב האפס** של מטריצה $A$ כאוסף הפתרונות $\mathbf{x}$ של מערכת משוואות הומוגנית $A\mathbf{x}=\mathbf{0}$. מצא בסיס של מרחב האפס וגם את מימדו.", 7, "c2"),
    H(2, "ב", "computation", "vector_spaces", r"מצא בסיס של מרחב השורות של מטריצה $A$ ואת מימדו.", 7, "c2"),
    H(2, "ג", "computation", "vector_spaces", r"מצא בסיס של מרחב העמודות של מטריצה $A$ ואת מימדו.", 7, "c2"),
    H(2, "ד", "computation", "vector_spaces", r"בדוק שהסכום של מימד מרחב האפס ומימד של מרחב העמודות שווה למספר העמודות של $A$.", 4, "c2"),

    H(3, "א", "computation", "rank_inverse", r"עבור אילו ערכי $a$ המטריצה $A$ הפיכה?", 5, "c3a"),
    H(3, "ב", "computation", "rank_inverse", r"חשב את $A^{-1}$ עבור $a=1$.", 5, "c3a"),
    H(3, "ג", "computation", "eigen_diagonalization", r"מצא את כל הערכים העצמיים והווקטורים העצמיים של $A$.", 9, "c3b"),
    H(3, "ד", "computation", "eigen_diagonalization", r"מצא את המטריצה האלכסונית $D$ והמטריצה ההפיכה $P$ כך שמתקיים $D=P^{-1}AP$.", 6, "c3b"),

    H(4, "א", "computation", "vector_spaces", r"מצא בסיס ומימד של תתי מרחבים $W_1$ ו-$W_2$.", 6, "c4"),
    H(4, "ב", "computation", "vector_spaces", r"חשב תת מרחב $W_1+W_2$, מצא בסיס ומימד של תת מרחב זה.", 7, "c4"),
    H(4, "ג", "computation", "vector_spaces", r"חשב תת מרחב $W_1\cap W_2$, מצא בסיס ומימד של תת מרחב זה.", 7, "c4"),
    H(4, "ד", "computation", "vector_spaces", r"האם הווקטור $" + pm("3", "1", "-1") + r"$ שייך לתת מרחב $W_1\cap W_2$?", 5, "c4"),

    H(5, "א", "proof", "linear_maps", r"הראה כי $T$ היא העתקה לינארית.", 6, "c5"),
    H(5, "ב", "computation", "linear_maps", r"מצא הבסיסים והמימדים של $\mathrm{Ker}(T)$ ו-$\mathrm{Im}(T)$.", 8, "c5"),
    H(5, "ג", "computation", "linear_maps", r"האם $T$ חד-חד ערכית? האם היא על? נמקו את תשובתכם.", 4, "c5"),
    H(5, "ד", "computation", "linear_maps",
      r"מצא את המטריצה המייצגת $T_{B_2}^{B_1}$ של ההעתקה ביחס לבסיסים $B_1=\left\{" + pm("1", "1", "1") + "," + pm("0", "1", "1") + "," + pm("0", "0", "1") + r"\right\}$ ו-$B_2=\left\{" + pm("1", "0", "0") + "," + pm("0", "1", "1") + "," + pm("1", "1", "0") + r"\right\}$.", 7, "c5"),
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
