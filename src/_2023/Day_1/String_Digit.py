from typing import Protocol
from enum import Enum

class String_Digit(Protocol):

    __DIGIT: int
    __STRING: str
    __id: int

    def compare_character(self, char: str) -> bool | int:
        return self
    
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
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result

    
class Two():

    def __init__(self):
        self.__DIGIT: int = 2
        self.__STRING: str = 'two'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Three():

    def __init__(self):
        self.__DIGIT: int = 3
        self.__STRING: str = 'three'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Four():

    def __init__(self):
        self.__DIGIT: int = 4
        self.__STRING: str = 'four'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Five():

    def __init__(self):
        self.__DIGIT: int = 5
        self.__STRING: str = 'five'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Six():

    def __init__(self):
        self.__DIGIT: int = 6
        self.__STRING: str = 'six'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Seven():

    def __init__(self):
        self.__DIGIT: int = 7
        self.__STRING: str = 'seven'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Eight():

    def __init__(self):
        self.__DIGIT: int = 8
        self.__STRING: str = 'eight'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
class Nine():

    def __init__(self):
        self.__DIGIT: int = 9
        self.__STRING: str = 'nine'
        self.__id: int = 0

    def compare_character(self, char: str) -> bool | int:
        result: bool | int = compare_character(self, char, self.__DIGIT, self.__STRING, self.__id)

        if type(result) == bool and result:
            self.__id += 1
        else:
            self.__id = 0

        return result
    
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