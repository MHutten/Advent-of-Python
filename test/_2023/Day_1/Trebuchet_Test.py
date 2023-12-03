import unittest
import src._2023.Day_1.Trebuchet as Trebuchet
from test.Read_Input import read_input

class Trebuchet_Test(unittest.TestCase):

    calibration_values: str

    def setUp(self):
        self.calibration_values = read_input('_2023\Day_1\input.txt')

    # Part 1

    # Provided Examples

    def test_sum_up_12_38_15_77(self):
        self.assertEqual(142, Trebuchet.sum_up_calibration_values('1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'))

    # Additional Cases

    @unittest.skip
    def test_sum_up_single_number(self):
        pass

    @unittest.skip
    def test_sum_up_single_digit_number(self):
        pass

    @unittest.skip
    def test_line_contains_no_digits(self):
        pass

#     # Challenge

    def test_part_1(self):
       self.assertEqual(54951, Trebuchet.sum_up_calibration_values(self.calibration_values))

    # Part 2

    # Provided Examples

    def test_sum_up_29_83_23_24_42_14_76(self):
        self.assertEqual(281, Trebuchet.sum_up_calibration_values('two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen', True))

    # Additional Cases

    @unittest.skip
    def test_sum_up_single_number_with_string_digits(self):
        pass

    @unittest.skip
    def test_sum_up_with_two_string_digits(self):
        pass

    @unittest.skip
    def test_sum_up_with_regular_and_string_digit(self):
        pass

    @unittest.skip
    def test_sum_up_with_string_and_regular_digit(self):
        pass

    @unittest.skip
    def test_sum_up_single_digit_number_with_string_digits(self):
        pass

    @unittest.skip
    def test_line_contains_no_digits_with_string_digits(self):
        pass

    @unittest.skip
    def test_line_contains_overlapping_string_digits(self):
        pass

    # Challenge

    def test_part_2(self):
        self.assertEqual(55218, Trebuchet.sum_up_calibration_values(self.calibration_values, True))