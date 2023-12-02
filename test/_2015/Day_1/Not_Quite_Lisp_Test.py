import unittest
import src._2015.Day_1.Not_Quite_Lisp as Not_Quite_Lisp
from test.Read_Input import read_input

class Not_Quite_Lisp_Test(unittest.TestCase):

    directions: str

    def setUp(self):
        self.directions = read_input('_2015\Day_1\input.txt')

    # Part 1

    # Provided Examples

    def test_santa_ends_at_floor_0(self):
        self.assertEqual(0, Not_Quite_Lisp.get_santas_destination('(())'))
        self.assertEqual(0, Not_Quite_Lisp.get_santas_destination('()()'))

    def test_santa_ends_at_floor_3(self):
        self.assertEqual(3, Not_Quite_Lisp.get_santas_destination('((('))
        self.assertEqual(3, Not_Quite_Lisp.get_santas_destination('(()(()('))
        self.assertEqual(3, Not_Quite_Lisp.get_santas_destination('))((((('))

    def test_santa_ends_at_basement_floor_1(self):
        self.assertEqual(-1, Not_Quite_Lisp.get_santas_destination('())'))
        self.assertEqual(-1, Not_Quite_Lisp.get_santas_destination('))('))

    def test_santa_ends_at_basement_floor_3(self):
        self.assertEqual(-3, Not_Quite_Lisp.get_santas_destination(')))'))
        self.assertEqual(-3, Not_Quite_Lisp.get_santas_destination(')())())'))

    # Additional Cases

    @unittest.skip
    def test_santa_received_incorrect_directions(self):
        pass

    @unittest.skip
    def test_santa_went_too_high(self):
        pass

    @unittest.skip
    def test_santa_went_too_low(self):
        pass

    # Challenge

    def test_part_1(self):
        self.assertEqual(138, Not_Quite_Lisp.get_santas_destination(self.directions))

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