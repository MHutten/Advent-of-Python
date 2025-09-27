from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_2.I_Was_Told_There_Would_Be_No_Math import calculate_area_of_wrapping_paper, calculate_ribbon_length

class IWasToldThereWouldBeNoMathTestCase(TestCase):

    def test__calculate_area_of_wrapping_paper__good_weather__2x3x4(self):
        self.assertEqual(calculate_area_of_wrapping_paper(2, 3, 4), 58)
        
    def test__calculate_area_of_wrapping_paper__good_weather__1x1x10(self):
        self.assertEqual(calculate_area_of_wrapping_paper(1, 1, 10), 43)
        
    def test__calculate_ribbon_length__good_weather__2x3x4(self):
        self.assertEqual(calculate_ribbon_length(2, 3, 4), 34)
        
    def test__calculate_ribbon_length__good_weather__1x1x10(self):
        self.assertEqual(calculate_ribbon_length(1, 1, 10), 14)


if __name__ == '__main__':
    main()