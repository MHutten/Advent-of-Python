from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_3.Perfectly_Spherical_Houses_in_a_Vacuum import calculate_number_of_visited_houses, calculate_number_of_visited_houses_with_robo_santa

class PerfectlySphericalHousesinaVacuumTestCase(TestCase):

    def test__calculate_number_of_visited_houses__good_weather__east(self):
        self.assertEqual(calculate_number_of_visited_houses(">"), 2)

    def test__calculate_number_of_visited_houses__good_weather__north_east_south_west(self):
        self.assertEqual(calculate_number_of_visited_houses("^>v<"), 4)

    def test__calculate_number_of_visited_houses__good_weather__north_south_repeated_5_times(self):
        self.assertEqual(calculate_number_of_visited_houses("^v^v^v^v^v"), 2)

    def test__calculate_number_of_visited_houses_with_robo_santa__good_weather__north_south(self):
        self.assertEqual(calculate_number_of_visited_houses_with_robo_santa("^v"), 3)

    def test__calculate_number_of_visited_houses_with_robo_santa__good_weather__north_east_south_west(self):
        self.assertEqual(calculate_number_of_visited_houses_with_robo_santa("^>v<"), 3)

    def test__calculate_number_of_visited_houses_with_robo_santa__good_weather__north_south_repeated_5_times(self):
        self.assertEqual(calculate_number_of_visited_houses_with_robo_santa("^v^v^v^v^v"), 11)


if __name__ == '__main__':
    main()