def look_and_say(string: str) -> str:

    output = ""
    index = 0

    while index < len(string):

        digit = string[index]
        count = 1

        while index + count < len(string) and string[index + count] == digit:
            count += 1

        output += str(count) + digit
        index += count

    return output