from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_08.Matchsticks import calculate_encoded_length, calculate_memory_length

class MatchsticksTestCase(TestCase):

    def test__calculate_memory_length__good_weather__quote_quote(self):
        self.assertEqual(calculate_memory_length("\"\""), 0)

    def test__calculate_memory_length__good_weather__quote_abc_quote(self):
        self.assertEqual(calculate_memory_length("\"abc\""), 3)

    def test__calculate_memory_length__good_weather__quote_aaa_backslash_quote_aaa_quote(self):
        self.assertEqual(calculate_memory_length("\"aaa\\\"aaa\""), 7)

    def test__calculate_memory_length__good_weather__quote_backslash_x27_quote(self):
        self.assertEqual(calculate_memory_length("\"\\x27\""), 1)

    def test__calculate_encoded_length__good_weather__quote_quote(self):
        self.assertEqual(calculate_encoded_length("\"\""), 6)

    def test__calculate_encoded_length__good_weather__quote_abc_quote(self):
        self.assertEqual(calculate_encoded_length("\"abc\""), 9)

    def test__calculate_encoded_length__good_weather__quote_aaa_backslash_quote_aaa_quote(self):
        self.assertEqual(calculate_encoded_length("\"aaa\\\"aaa\""), 16)

    def test__calculate_encoded_length__good_weather__quote_backslash_x27_quote(self):
        self.assertEqual(calculate_encoded_length("\"\\x27\""), 11)


if __name__ == "__main__":
    main()