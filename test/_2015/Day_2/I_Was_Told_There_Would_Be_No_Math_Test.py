import unittest
import src._2015.Day_2.I_Was_Told_There_Would_Be_No_Math as I_Was_Told_There_Would_Be_No_Math
import src._2015.Day_1.Not_Quite_Lisp as Not_Quite_Lisp
from test.Read_Input import read_input

class I_Was_Told_There_Would_Be_No_Math_Test(unittest.TestCase):

    list_of_dimensions: str

    def setUp(self):
        self.list_of_dimensions = read_input('_2015\Day_2\input.txt')

    # Part 1

    # Provided Examples

    def test_present_of_2x3x4(self):
        self.assertEqual(58, I_Was_Told_There_Would_Be_No_Math.get_required_square_feet_of_wrapping_paper("2x3x4"))

    def test_present_of_1x1x10(self):
        self.assertEqual(43, I_Was_Told_There_Would_Be_No_Math.get_required_square_feet_of_wrapping_paper("1x1x10"))

    # Additional Cases

    @unittest.skip
    def test_present_with_negative_dimensions(self):
        pass

    @unittest.skip
    def test_present_too_large(self):
        pass

    @unittest.skip
    def test_that_is_not_a_number(self):
        pass

    @unittest.skip
    def test_a_dimension_is_missing(self):
        pass

    # Challenge

    def test_part_1(self):
        self.assertEqual(1606483, I_Was_Told_There_Would_Be_No_Math.get_required_square_feet_of_wrapping_paper(self.list_of_dimensions))

    # Part 2

    # Provided Examples

    def test_santa_enters_basement_after_first_direction(self):
        self.assertEqual(1, Not_Quite_Lisp.santa_enters_basement_at(')'))

    def test_santa_enters_basement_after_fifth_direction(self):
        self.assertEqual(5, Not_Quite_Lisp.santa_enters_basement_at('()())'))

    # Additional Cases

    @unittest.skip
    def test_santa_received_incorrect_directions_again(self):
        pass

    @unittest.skip
    def test_santa_never_enters_basement(self):
        pass

    # Challenge

    def test_part_2(self):
        self.assertEqual(1771, Not_Quite_Lisp.santa_enters_basement_at(self.directions))