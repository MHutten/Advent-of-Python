import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from file import read
from Not_Quite_Lisp import calculate_santas_final_destination

def main() -> None:

    print(calculate_santas_final_destination(read(sys.argv[1])))

if __name__ == "__main__":
    
    main()