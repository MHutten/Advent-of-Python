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

    def turn_on(self: Self, start: tuple[int], end: tuple[int]):

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] = True


    
    def toggle(self: Self, start: tuple[int], end: tuple[int]):

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] = not self.__lights[i][j]

        

    def turn_off(self: Self, start: tuple[int], end: tuple[int]):

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] = False



    def get_number_of_lit_lights(self: Self) -> int:

        number_of_lit_lights = 0

        for i in range(1000):

            for j in range(1000):

                if self.__lights[i][j]:

                    number_of_lit_lights += 1

        

        return number_of_lit_lights
    

class LightsWithBrightnessControls(object):

    def __init__(self: Self, initial_state: int):

        self.__lights = [[initial_state for _ in range(1000)] for _ in range(1000)]

    def __getitem__(self: Self, index: int):
        return self.__lights[index]

    def turn_on_ancient_nordic_elvish(self: Self, start: tuple[int], end: tuple[int]):

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] += 1

        

    def toggle_ancient_nordig_elvish(self: Self, start: tuple[int], end: tuple[int]):

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                self.__lights[i][j] += 2
        

    
    def turn_off_ancient_nordic_elvish(self: Self, start: tuple[int], end: tuple[int]):

        for i in range(start[0], end[0] + 1):

            for j in range(start[1], end[1] + 1):

                if self.__lights[i][j] > 0:

                    self.__lights[i][j] -= 1

        


    def calculate_total_brightness(self: Self) -> int:

        brightness = 0

        for i in range(1000):

            for j in range(1000):

                brightness += self.__lights[i][j]

        
        return brightness