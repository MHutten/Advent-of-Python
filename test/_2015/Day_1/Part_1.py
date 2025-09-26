import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source.file import read
from source._2015.Day_1.Not_Quite_Lisp import calculate_santas_final_destination

print(calculate_santas_final_destination(read(sys.argv[1])))