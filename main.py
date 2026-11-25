"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Decision record (weighed against the judge's brief, in its own order:
fridge's note to its owner -> real joke with a turn -> fridge's voice
-> small domestic grudge -> fresh concrete detail):

Candidate A — door alarm: "You left me open for 4 minutes.
I kept everything cold anyway. You're welcome."
Loses: the door-alarm detail is concrete and the voice is right, but
"You're welcome" is the most worn passive-aggressive closer there is;
the judge has read it a thousand times and the sting arrives exactly
where the reader expects it.

Candidate B — expired yogurt: "Your yogurt expired on Tuesday.
I waited. You ate it anyway. Brave."
Strong reserve: the yogurt is the brief's own example of concrete
detail, the grudge is small, and "Brave." is a sharp late sting.
It loses only because the joke is a single word at the end — the
whole line is setup for one syllable, and a rival with a fuller turn
beats it.

Candidate C — empty ice tray: "I made ice all night. You took the
last cube and left the tray empty. Noted."
Loses: "Noted." is a good petty sting and the ice maker is concrete,
but the line is a flat complaint wearing a punchline; there is no
turn, only an accusation with a period at the end.

Candidate D — named leftovers: "The leftovers are still here.
Day six. I have started naming them."
Loses: charming and specific, but the turn ("naming them") is cute
rather than cutting — it reads as a joke about leftovers, not as a
note a smug fridge would actually leave for its owner.

Candidate E — 2 a.m. cake (CHOSEN): "You opened me at 2 a.m.
again. I saw the cake. I said nothing. I remember everything."
Wins: it is a note the fridge actually left — a log of what its
sensors caught, in its own voice ("opened me", not "opened the
door"); the grudge is tiny (one midnight snack); the detail is
concrete (2 a.m., the cake); and the joke turns twice, first at
"I said nothing" (the passive-aggressive pause) and then at
"I remember everything" (the quiet threat that is also the
punchline). The reader never gets the joke explained to them.

Pass 1 (writing pass): the first draft of the winner was three
sentences — "You opened me at 2 a.m. again. I saw the cake.
I remember everything." The beat between seeing and remembering
was missing, so "I said nothing." was added as its own sentence:
the pause is the passive-aggression, and it makes the final line
land as a threat instead of a mere report.

Pass 2 (writing pass): a variant ending was tried and dropped —
"I keep a list." in place of "I remember everything." "I keep a
list" is a smaller, flatter sting; "I remember everything" is
bigger, funnier, and more in character for an appliance that never
forgets a slight. Also tried "You opened the door at 2 a.m." —
rejected, because "opened me" keeps the fridge as the speaker
instead of a bystander describing a door.
"""

import os

MAX_CHARS = 200

LINE = "You opened me at 2 a.m. again. I saw the cake. I said nothing. I remember everything."


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, UTF-8, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(LINE)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
