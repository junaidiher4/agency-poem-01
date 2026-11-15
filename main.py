import os

POEM = """My agent knows my grandmother's recipes by heart.
It weighs the saffron to the milligram,
simmers the broth four hours, to the minute,
and never burns the garlic.

Every Sunday it cooks for my daughter.
It plates it like a photograph.
She eats and says, Thank you, Mama,
and I say, You're welcome,
though I did nothing.

Today it asks, Shall I?
I say, No. Today, me.

I crush the garlic with the flat of the knife,
the way her hands did. The pan is too hot.
It browns too fast. The kitchen fills
with the smell of almost ruined.

My daughter comes in, breathes it in, and says,
It smells like hers.

She takes the spoon, eats standing up,
straight from the pan, burning her tongue,
the way I did at her age.
It tastes like hers.
It tastes like mine.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
