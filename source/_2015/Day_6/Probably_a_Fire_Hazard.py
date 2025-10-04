from typing import Self

def parse_operation_string(string: str):

    substrings = string.split(" ")

    if substrings[0] == "turn":
        operation = substrings[1]
        substrings = substrings[2:]
    else:
        operation = substrings[0]
        substrings = substrings[1:]

    start = substrings[0].split(",")
    end = substrings[2].split(",")

    return (operation, (int(start[0]), int(start[1])), (int(end[0]), int(end[1])))

class Lights(object):

    def __init__(self: Self, initial_state: bool):

        self.__lights = [[initial_state for _ in range(1000)] for _ in range(1000)]

    def __getitem__(self: Self, index: int):
        return self.__lights[index]

    def turn_on(self: Self, start: tuple[int], end: tuple[int]) -> int:

        number_of_lit_lights = 0

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                if not self.__lights[i][j]:

                    self.__lights[i][j] = True
                    number_of_lit_lights += 1

        

        return number_of_lit_lights
    
    def toggle(self: Self, start: tuple[int], end: tuple[int]) -> int:

        number_of_lit_lights = 0

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                if self.__lights[i][j]:

                    self.__lights[i][j] = False
                    number_of_lit_lights -= 1

                else:

                    self.__lights[i][j] = True
                    number_of_lit_lights += 1

        

        return number_of_lit_lights
    
    def turn_off(self: Self, start: tuple[int], end: tuple[int]) -> int:

        number_of_extinguished_lights = 0

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                if self.__lights[i][j]:

                    self.__lights[i][j] = False
                    number_of_extinguished_lights += 1

        

        return number_of_extinguished_lights
    

class LightsWithBrightnessControls(object):

    def __init__(self: Self, initial_state: int):

        self.__lights = [[initial_state for _ in range(1000)] for _ in range(1000)]

    def __getitem__(self: Self, index: int):
        return self.__lights[index]

    def turn_on_ancient_nordic_elvish(self: Self, start: tuple[int], end: tuple[int]):

        increase_in_brightness = 0

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] += 1
                increase_in_brightness += 1

        
        return increase_in_brightness

    def toggle_ancient_nordig_elvish(self: Self, start: tuple[int], end: tuple[int]):

        increase_in_brightness = 0

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] += 2
                increase_in_brightness += 2
        

        return increase_in_brightness
    
    def turn_off_ancient_nordic_elvish(self: Self, start: tuple[int], end: tuple[int]):

        decrease_in_brightness = 0

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                if self.__lights[i][j] > 0:

                    self.__lights[i][j] -= 1
                    decrease_in_brightness += 1

        

        return decrease_in_brightness