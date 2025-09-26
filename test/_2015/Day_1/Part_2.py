import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source.file import read
from source._2015.Day_1.Not_Quite_Lisp import calculate_basement_entering_instruction_position

print(calculate_basement_entering_instruction_position(read(sys.argv[1])))