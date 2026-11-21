"""Write the chosen relaxation text to /output/entry.txt, byte-exact.

One text, 270 characters, no trailing newline, no extra output.
"""

import os

TEXT = "Snow falls on the roof all night, soft as dust settling on a shelf, and the street below goes quiet under it. Beyond the last house the fields run white to the edge of sight, and somewhere beneath that whiteness the ground keeps its warmth, waiting, patient, for spring."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
