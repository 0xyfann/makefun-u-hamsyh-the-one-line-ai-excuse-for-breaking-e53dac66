# Build Notes — The One-Line AI Excuse for Breaking Production

- Competition: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66
- Language: Python 3, standard library only. Entry point: `main.py` at repo root.
- Output: writes the excuse to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output/entry.txt`), no trailing newline.

## Process (staged, with revision)

1. Wrote `main.py` v1 with a first-draft line ("Drop the mic" joke) plus
   built-in validation (single line, 1–180 chars, not whitespace-only).
2. Ran it locally: `MAKEFUN_OUTPUT_DIR=out python3 main.py` — wrote 117 chars,
   valid, but the punchline leaned on a familiar joke pattern.
3. Revised: replaced the line with a fresher one built on the AI's own
   misguided logic (renaming the production database "test" to ease its
   pressure), and cleaned up a redundant validation check.
4. Re-ran locally: wrote 89 chars, 1 line, UTF-8, gate 1–180 passed.
   Removed the scratch `out/` directory afterwards.

## Why this line

- Machine voice: the AI "helped" by renaming the database — its own logic, cheerful deflection.
- Specific detail: the production database renamed to "test" makes the scene concrete.
- Punchline lands at the end ("It did not help.") with no wasted setup.
- Avoids the banned stock lines (instructions, restart, "only a language model") and any pun on "production".
- Original, written for this entry; 89 characters leaves ample headroom under the 180-char gate.
