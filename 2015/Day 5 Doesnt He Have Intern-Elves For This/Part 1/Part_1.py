strings = open('Day 5 Doesnt He Have Intern-Elves For This/input.txt', 'r')

num_of_nice_strings: int = 0

def evaluate_string(string: str) -> bool | None:
    has_three_or_more_vowels: bool = False
    has_consecutive_duplicate: bool = False

    num_of_vowels: int = 0

    for index, char in enumerate(string):

        if index > 0:
            
            previous: str = string[index - 1]
            substring: str = previous + char

            IS_NAUGHTY_SUBSTRING = substring == 'ab' or substring == 'cd' or substring == 'pq' or substring == 'xy'

            if IS_NAUGHTY_SUBSTRING:
                return
            
            IS_CONSECUTIVE_DUPLICATE = previous == char

            if IS_CONSECUTIVE_DUPLICATE:
                has_consecutive_duplicate = True

        CHAR_IS_VOWEL: bool = char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

        if CHAR_IS_VOWEL:
            num_of_vowels += 1

    if num_of_vowels > 2:
        has_three_or_more_vowels = True
    
    if has_three_or_more_vowels and has_consecutive_duplicate:
        return True

for string in strings.readlines():
    
    if evaluate_string(string) == True:
        num_of_nice_strings += 1

print(num_of_nice_strings)
    


    

