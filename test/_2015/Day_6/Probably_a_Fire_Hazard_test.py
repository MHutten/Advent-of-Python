from unittest import main, TestCase

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from source._2015.Day_6.Probably_a_Fire_Hazard import Lights, LightsWithBrightnessControls

class ProbablyaFireHazardTestCase(TestCase):

    def test__turn_on__good_weather__0_0_trough_999_999(self):
        
        lights = Lights(False)

        self.assertEqual(lights.turn_on((0, 0), (999, 999)), 1000000)

        for i in range(1000):

            for j in range(1000):

                self.assertTrue(lights[i][j])



    def test__toggle__good_weather__0_0_trough_999_0(self):

        lights = Lights(False)

        for index in range(1000):

            if index % 2 == 0:

                lights[index][0] = True

        
        self.assertEqual(lights.toggle((0, 0), (999, 0)), 0)

        for i in range(1000):

            if index % 2 == 0:

                self.assertFalse(lights[index][0])

            else:

                self.assertTrue(lights[index][0])

            for j in range(1, 1000):

                self.assertFalse(lights[i][j])


    
    def test__turn_off__good_weather__499_499_trough_500_500(self):

        lights = Lights(True)

        self.assertEqual(lights.turn_off((499, 499), (500, 500)), 4)

        for i in range(1000):

            for j in range(1000):

                if i >= 499 and i <= 500 and j >= 499 and j <= 500:

                    self.assertFalse(lights[i][j])

                else:

                    self.assertTrue(lights[i][j])




    def test__turn_on_ancient_nordic_elvish__good_weather__0_0_trough_0_0(self):

        lights = LightsWithBrightnessControls(0)

        self.assertEqual(lights.turn_on_ancient_nordic_elvish((0, 0), (0, 0)), 1)

        self.assertEqual(lights[0][0], 1)

        for i in range(1, 1000):

            for j in range(1, 1000):

                self.assertEqual(lights[i][j], 0)

    

    def test__toggle_ancient_nordic_elvish__good_weather__0_0_trough_999_999(self):

        lights = LightsWithBrightnessControls(0)

        self.assertEqual(lights.toggle_ancient_nordig_elvish((0, 0), (999, 999)), 2000000)

        for i in range(1000):

            for j in range(1000):

                self.assertEqual(lights[i][j], 2)




if __name__ == "__main__":
    main()