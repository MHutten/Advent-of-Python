import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read
from Not_Quite_Lisp import calculate_basement_entering_instruction_position

def main() -> None:

    print(calculate_basement_entering_instruction_position(read(sys.argv[1])))

if __name__ == "__main__":
    
    main()