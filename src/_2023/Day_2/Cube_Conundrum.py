RED = 12
GREEN = 13
BLUE = 14

def sum_up_ids_of_possible_games(game_results: str) -> int:
    sum: int = 0

    for game in game_results.split('\n'):
        (title, results) = game.split(':')

        game_id: int = int(title[5:])

        if game_is_possible(results):
            sum += game_id

    return sum

def game_is_possible(game: str) -> bool:
    for set in game.split(';'):
        for partition in set.split(','):
            (amount, color) = partition[1:].split(' ')

            if int(amount) < 0:
                return False
            
            if color == 'red' and int(amount) > RED:
                return False
            if color == 'green' and int(amount) > GREEN:
                return False
            if color == 'blue' and int(amount) > BLUE:
                return False
            
    return True

def sum_up_powers(game_results: str) -> int:
    sum: int = 0

    for game in game_results.split('\n'):
        (title, results) = game.split(':')
        sum += calculate_game_power(results)

    return sum

def calculate_game_power(game: str) -> int:
    red: int = 0
    green: int = 0
    blue: int = 0

    for set in game.split(';'):
        for partition in set.split(','):
            (amount, color) = partition[1:].split(' ')
            
            if color == 'red':
                red = max(red, int(amount))
            if color == 'green':
                green = max(green, int(amount))
            if color == 'blue':
                blue = max(blue, int(amount))
            
    return red * green * blue