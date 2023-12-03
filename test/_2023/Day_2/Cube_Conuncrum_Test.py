import unittest
import src._2023.Day_2.Cube_Conundrum as Cube_Conundrum
from test.Read_Input import read_input

class Cube_Conundrum_Test(unittest.TestCase):

    game_results: str

    def setUp(self):
        self.game_results = read_input('_2023\Day_2\input.txt')

    # Part 1

    # Provided Examples

    def test_possible_games_1_2_and_5_add_up_to_8(self):
        self.assertEqual(8, Cube_Conundrum.sum_up_ids_of_possible_games(read_input('_2023\Day_2\example.txt')))

#     # Additional Cases

#     @unittest.skip
#     def test_sum_up_single_number(self):
#         pass

#     @unittest.skip
#     def test_sum_up_single_digit_number(self):
#         pass

#     @unittest.skip
#     def test_line_contains_no_digits(self):
#         pass

#     # Challenge

    def test_part_1(self):
       self.assertEqual(2449, Cube_Conundrum.sum_up_ids_of_possible_games(self.game_results))

    # Part 2

    # Provided Examples

    def test_powers_add_up_to_2286(self):
        self.assertEqual(2286, Cube_Conundrum.sum_up_powers(read_input('_2023\Day_2\example.txt')))

#     # Additional Cases

#     @unittest.skip
#     def test_sum_up_single_number_with_string_digits(self):
#         pass

#     @unittest.skip
#     def test_sum_up_with_two_string_digits(self):
#         pass

#     @unittest.skip
#     def test_sum_up_with_regular_and_string_digit(self):
#         pass

#     @unittest.skip
#     def test_sum_up_with_string_and_regular_digit(self):
#         pass

#     @unittest.skip
#     def test_sum_up_single_digit_number_with_string_digits(self):
#         pass

#     @unittest.skip
#     def test_line_contains_no_digits_with_string_digits(self):
#         pass

#     @unittest.skip
#     def test_line_contains_overlapping_string_digits(self):
#         pass

    # Challenge

    def test_part_2(self):
       self.assertEqual(63981, Cube_Conundrum.sum_up_powers(self.game_results))