__VOWELS = "aeiou"
__NAUGHTY_SUBSTRINGS = ("ab", "cd", "pq", "xy")

def is_nice(string : str) -> bool:

    contains_consecutives = False
    vowel_count = 0

    if string[0] in __VOWELS:
        vowel_count += 1

    for index, value in enumerate(string[1:]):

        if string[index:index + 2] in __NAUGHTY_SUBSTRINGS:
            return False
        
        if value in __VOWELS:
            vowel_count += 1

        if value == string[index]:
            contains_consecutives = True

    return contains_consecutives and (vowel_count > 2)

def is_nice_now(string : str) -> bool:

    contains_multiple_non_overlapping_duplicate_pairs = False
    contains_repeating_character_seperated_by_one_character = False

    if string[:2] in string[2:]:
        contains_multiple_non_overlapping_duplicate_pairs = True

    for index, value in enumerate(string[2:]):

        if string[index + 1:index + 3] in string[index + 3:]:
            contains_multiple_non_overlapping_duplicate_pairs = True

        if value == string[index]:
            contains_repeating_character_seperated_by_one_character = True

        if contains_multiple_non_overlapping_duplicate_pairs and contains_repeating_character_seperated_by_one_character:
            return True
        
    return False