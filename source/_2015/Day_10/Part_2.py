import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from Elves_Look_Elves_Say import look_and_say

def main() -> None:

    string = sys.argv[1]

    for _ in range(50):
        string = look_and_say(string)

    print(len(string))

if __name__ == "__main__":
    main()