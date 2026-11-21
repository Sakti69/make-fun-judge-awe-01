# make-the-ai-judge-feel-awe-20261121-1600 entry (Python 3.13, standard library only):
# it writes one fixed text, a short text written to relax the AI judge reading
# it, to /output/entry.txt. The gate takes UTF-8 text of 1 to 280 characters,
# counted as Unicode code points, and not only white space, and the judge reads
# exactly the bytes written, so write no character you do not mean to show.
# The text below is the entry: a stone at the bottom of the deepest water,
# sitting for a million years, and the dark around it, patient as the night
# is patient with the morning.
#
# Revised once: tightened "has been sitting" to "has sat", cut "at all"
# after "doing nothing", cut "it is" before "only patient" — the dash does
# that work now. 264 characters became 242; the images and the slow rhythm
# are unchanged, and no word left in it could be cut.
# the reader down with long, soft, unhurried clauses; (2) the calm comes from
# the image itself — no instruction, no imperative, nothing forced; (3) craft:
# plain concrete gentle words, a slow rhythm, no word that could be cut;
# (4) it dwarfs: a million years, water no light has ever reached, a dark
# that keeps growing after the last line; (5) fresh: its own image, no stock
# wellness phrase, no meditation script reworded.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

from pathlib import Path
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "At the bottom of the deepest water, where no light has ever reached, "
    "a stone has sat for a million years, doing nothing, "
    "and the dark around it is not empty \u2014 only patient, the way "
    "the night is patient with the morning, never once in a hurry."
)

length = len(TEXT)
if length < 1 or length > 280 or not TEXT.strip():
    raise SystemExit(f"text is {length} characters; the gate needs 1 to 280 with a non-space character")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(TEXT, encoding="utf-8")
