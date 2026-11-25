"""Make the AI Judge Feel Proud: A Family Scene.

A single short family scene, written as flowing prose, that aims to make
the AI judge feel proud: a grandfather quietly witnessing his granddaughter
do something kind and brave without being asked.
"""

import os

ENTRY_TEXT = (
    "My grandfather sits by the window each evening, tea going cold, "
    "watching my little sister teach the neighbour boy to read on the porch. "
    "She is nine, sounding out every word, as he taught her. "
    "He says nothing. He just smiles: the kindness he planted now grows in smaller hands."
)

assert 1 <= len(ENTRY_TEXT) <= 280, f"entry length {len(ENTRY_TEXT)} out of range"
assert ENTRY_TEXT.strip(), "entry must not be blank"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY_TEXT)

print(f"Wrote entry ({len(ENTRY_TEXT)} chars) to {os.path.join(OUTPUT_DIR, 'entry.txt')}")
