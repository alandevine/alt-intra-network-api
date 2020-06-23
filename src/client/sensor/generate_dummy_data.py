import random
import os
import sys


def main():
    if len(sys.argv) > 1:
        freq = float(sys.argv[1])
    else:
        freq = .5

    assert 0 < freq < 1.0

    actions = ["dispense", "alerted"]

    if os.path.exists("entry"):
        while True:
            sample = random.uniform(0, 1)
            if sample < freq:
                action = random.choice(actions)
                with open("entry", "w") as f:
                    f.write(action)


if __name__ == "__main__":
    main()
