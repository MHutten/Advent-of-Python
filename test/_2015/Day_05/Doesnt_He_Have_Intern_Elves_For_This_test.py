from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_05.Doesnt_He_Have_Inter_Elves_For_This import is_nice, is_nice_now

class DoesntHeHaveInternElvesForThisTestCase(TestCase):

    def test__is_nice__good_weather__ugknbfddgicrmopn(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))

    def test__is_nice__good_weather__aaa(self):
        self.assertTrue(is_nice("aaa"))

    def test__is_nice__good_weather__jchzalrnumimnmhp(self):
        self.assertFalse(is_nice("jchzalrnumimnmhp"))

    def test__is_nice__good_weather__haegwjzuvuyypxyu(self):
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))

    def test__is_nice__good_weather__dvszwmarrgswjxmb(self):
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))

    def test__is_nice_now__good_weather__qjhvhtzxzqqjkmpb(self):
        self.assertTrue(is_nice_now("qjhvhtzxzqqjkmpb"))

    def test__is_nice_now__good_weather__xxyxx(self):
        self.assertTrue(is_nice_now("xxyxx"))

    def test__is_nice_now__good_weather__uurcxstgmygtbstg(self):
        self.assertFalse(is_nice_now("uurcxstgmygtbstg"))

    def test__is_nice_now__good_weather__ieodomkazucvgmuy(self):
        self.assertFalse(is_nice_now("ieodomkazucvgmuy"))


if __name__ == "__main__":
    main()