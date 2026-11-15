import os

POEM = """My mother played it for me every night,
the same song, on the piano with the chipped key,
until I fell asleep.
When she went, the agent took the bench.
It plays it better than she ever did.
No wrong notes. It never touches the chipped key.
It has played my daughter to sleep for ten years,
every night at eight, without being asked.

Tonight my daughter asked me to play.
I sat down. The bench was still warm.
I missed the notes. I stopped. I started again.
The agent sat with its keys still.
It did not help.

She clapped. 'Again.'
I played it wrong the same way twice,
the way my mother used to,
on the chipped key.
It was the first time the song had ever been mine.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
