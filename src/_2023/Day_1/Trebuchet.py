#import String_Digit as sd
from typing import Protocol
from enum import Enum

class String_Digit(Protocol):

    def compare_character(self, char: str) -> bool | int:
        return self

    def compare_initial_character(char: str):
        return String_Digit()
    
def compare_character(sd: String_Digit, char: str, digit: int, string: str, id: int) -> bool | int:
    equal: bool = char == string[id]

    if not equal:
        return False

    if id == len(string) - 1:
        return digit
    
    return True
    
class One():

    def __init__(self):
        self.__DIGIT: int = 1
        self.__STRING: str = 'one'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 'o':
            return One()
    
class Two():

    def __init__(self):
        self.__DIGIT: int = 2
        self.__STRING: str = 'two'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 't':
            return Two()
    
class Three():

    def __init__(self):
        self.__DIGIT: int = 3
        self.__STRING: str = 'three'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 't':
            return Three()
    
class Four():

    def __init__(self):
        self.__DIGIT: int = 4
        self.__STRING: str = 'four'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 'f':
            return Four()
    
class Five():

    def __init__(self):
        self.__DIGIT: int = 5
        self.__STRING: str = 'five'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 'f':
            return Five()
    
class Six():

    def __init__(self):
        self.__DIGIT: int = 6
        self.__STRING: str = 'six'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 's':
            return Six()
    
class Seven():

    def __init__(self):
        self.__DIGIT: int = 7
        self.__STRING: str = 'seven'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 's':
            return Seven()
    
class Eight():

    def __init__(self):
        self.__DIGIT: int = 8
        self.__STRING: str = 'eight'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 'e':
            return Eight()
    
class Nine():

    def __init__(self):
        self.__DIGIT: int = 9
        self.__STRING: str = 'nine'
        self.__id: int = 1

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1

        return result
    
    def compare_initial_character(char: str):
        if char == 'n':
            return Nine()
        
class String_Digits(Enum):
    ONE     = One
    TWO     = Two
    THREE   = Three
    FOUR    = Four
    FIVE    = Five
    SIX     = Six
    SEVEN   = Seven
    EIGHT   = Eight
    NINE    = Nine
    
    def compare_initial_character(self, char: str):
        return self.value.compare_initial_character(char)

def sum_up_calibration_values(calibration_values: str, with_string_digits: bool = False) -> int:
    sum: int = 0

    if with_string_digits:
        for line in calibration_values.split('\n'):
            sum += extract_digits_and_string_digits(line)
    else:
        for line in calibration_values.split('\n'):
            sum += extract_only_digits(line)

    return sum
    
def extract_digits_and_string_digits(calibration_line: str) -> int:
    first_digit: int = 0
    last_digit: int = 0
    string_digits: list[String_Digit] = []

    for char in calibration_line:

        if char.isdigit():
            if first_digit == 0:
                first_digit = int(char)
            last_digit = int(char)

        surviving_string_digits: list[String_Digit] = []

        for string_digit in string_digits:
            result: bool | int = string_digit.compare_character(char)

            if type(result) == bool and result:
                surviving_string_digits.append(string_digit)

            if type(result) == int:
                if first_digit == 0:
                    first_digit = result
                last_digit = result

        string_digits = surviving_string_digits.copy()

        for string_digit in String_Digits:
            new_digit: String_Digit = string_digit.compare_initial_character(char)
            if new_digit is not None:
                string_digits.append(new_digit)

    return 10 * first_digit + last_digit

def extract_only_digits(calibration_line: str) -> int:
    first_digit: int = 0
    last_digit: int = 0

    for char in calibration_line:
        if char.isdigit():
            if first_digit == 0:
                first_digit = int(char)
            last_digit = int(char)
            
    return 10 * first_digit + last_digit