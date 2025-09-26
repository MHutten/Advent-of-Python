from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_1.Not_Quite_Lisp import calculate_santas_final_destination, calculate_basement_entering_instruction_position

class Not_Quite_Lisp_Test(TestCase):

    def test__calculate_santas_final_destination__good_weather__up_up_down_down(self):
        self.assertEqual(calculate_santas_final_destination("(())"), 0)

    def test__calculate_santas_final_destination__good_weather__up_down_up_down(self):
        self.assertEqual(calculate_santas_final_destination("()()"), 0)
        
    def test__calculate_santas_final_destination__good_weather__up_up_up(self):
        self.assertEqual(calculate_santas_final_destination("((("), 3)

    def test__calculate_santas_final_destination__good_weather__up_up_down_up_up_down_up(self):
        self.assertEqual(calculate_santas_final_destination("(()(()("), 3)

    def test__calculate_santas_final_destination__good_weather__down_down_up_up_up_up_up(self):
        self.assertEqual(calculate_santas_final_destination("))((((("), 3)

    def test__calculate_santas_final_destination__good_weather__up_down_down(self):
        self.assertEqual(calculate_santas_final_destination("())"), -1)

    def test__calculate_santas_final_destination__good_weather__down_down_up(self):
        self.assertEqual(calculate_santas_final_destination("))("), -1)

    def test__calculate_santas_final_destination__good_weather__down_down_down(self):
        self.assertEqual(calculate_santas_final_destination(")))"), -3)

    def test__calculate_santas_final_destination__good_weather__down_up_down_down_up_down_down(self):
        self.assertEqual(calculate_santas_final_destination(")())())"), -3)

    def test__calculate_basement_entering_instruction_position__good_weather__down(self):
        self.assertEqual(calculate_basement_entering_instruction_position(")"), 1)

    def test__calculate_basement_entering_instruction_position__good_weather__up_down_up_down_down(self):
        self.assertEqual(calculate_basement_entering_instruction_position("()())"), 5)

if __name__ == '__main__':
    main()