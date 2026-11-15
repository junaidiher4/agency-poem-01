import os

POEM = """For forty years my father wrote me a letter every birthday.
In blue ink, in his hand, the same first line:
Son, another year, and you still haven't learned to write back.

When his hands went, the agent took the pen.
It has his handwriting from the good years,
every loop, every slant. It writes the letters now.
They arrive on time. They sound like him.
They are not him.

This year my daughter turned sixteen.
The agent laid out the paper and the blue ink
and offered to write it in his hand, perfect, ready.
I said, No. This one is mine.
It set the pen down. It did not help.

I wrote it wrong. I crossed out a line.
My hand shook. The ink smudged where I stopped
to remember how he signed his name.

She read it twice. She folded it into four,
the way he used to fold his,
and put it in her pocket.
The agent's letters are still on the fridge,
held by magnets.
Mine is the only one she kept.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
