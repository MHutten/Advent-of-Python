from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_10.Elves_Look_Elves_Say import look_and_say

class ElvesLookElvesSayTestCase(TestCase):

    def test__look_and_say__good_weather__1(self):
        self.assertEqual(look_and_say("1"), "11")

    def test__look_and_say__good_weather__11(self):
        self.assertEqual(look_and_say("11"), "21")

    def test__look_and_say__good_weather__21(self):
        self.assertEqual(look_and_say("21"), "1211")

    def test__look_and_say__good_weather__1211(self):
        self.assertEqual(look_and_say("1211"), "111221")

    def test__look_and_say__good_weather__111221(self):
        self.assertEqual(look_and_say("111221"), "312211")


if __name__ == "__main__":
    main()