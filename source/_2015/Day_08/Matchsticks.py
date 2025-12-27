from string import hexdigits

def calculate_memory_length(string: str) -> int:

    length = 0
    index = 1

    while index < len(string) - 1:

        if string[index] != '\\':
            index += 1
        elif string[index + 1] == '\\' or string[index + 1] == '\"':
            index += 2
        elif string[index + 1] == 'x' and string[index + 2] in hexdigits and string[index + 3] in hexdigits:
            index += 4
        else:
            raise Exception("Unexpected next characters '{}', '{}', and '{}' in string \"{}\"".format(string[index + 1], string[index + 2], string[index + 3], string))
        
        length += 1

    return length

def calculate_encoded_length(string: str) -> int:

    length = 2

    for character in string:

        if character == '\"' or character == '\\':
            length += 2
        else:
            length += 1

    return length