# Determine which games would have been possible if the bag had been loaded
# with only 12 red cubes, 13 green cubes, and 14 blue cubes.
# What is the sum of the IDs of those games?
import re


def solve_game(input_file='input.txt'):

    with open(input_file, 'r') as f:
        s = f.readlines()

    games = {}
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []

    for i in s:
        game = i.split(': ')[0]
        rounds = i.split(': ')[-1].replace('\n', '')
        rounds = rounds.split('; ')
        dict_rounds = []
        is_possible = True

        for i_round in rounds:
            # red = re.match(r".*(\d+)( red)", i_round)
            # blue = re.match(r".*(\d+)( blue)", i_round)
            # green = re.match(r".*(\d+)( green)", i_round)
            # this_round = {'red': 0 if red is None else int(red.group(1)),
            #               'blue': 0 if blue is None else int(blue.group(1)),
            #               'green': 0 if green is None else int(green.group(1))}
            this_round = {colour.split(' ')[-1]: int(colour.split(' ')[0]) for colour in i_round.split(', ')}
            if this_round.get('red', 0) > max_cubes['red'] or this_round.get('blue', 0) > max_cubes['blue'] or this_round.get('green', 0) > max_cubes['green']:
                is_possible = False
                # print('Found', game)
            dict_rounds.append(this_round)

        games[game] = dict_rounds
        if is_possible:
            possible_games.append(int(re.match(r"Game (\d+)", game).group(1)))

    return sum(possible_games)


def solve_game_2(input_file='input.txt'):

    with open(input_file, 'r') as f:
        s = f.readlines()

    games = {}
    game_power_list = []

    for i in s:
        game = i.split(': ')[0]
        rounds = i.split(': ')[-1].replace('\n', '')
        rounds = rounds.split('; ')
        dict_rounds = []
        min_red = 1
        min_blue = 1
        min_green = 1
        for i_round in rounds:
            this_round = {colour.split(' ')[-1]: int(colour.split(' ')[0]) for colour in i_round.split(', ')}
            dict_rounds.append(this_round)

            min_red = max(this_round.get('red', 1), min_red)
            min_blue = max(this_round.get('blue', 1), min_blue)
            min_green = max(this_round.get('green', 1), min_green)

        game_power = min_red * min_blue * min_green
        games[game] = dict_rounds
        game_power_list.append(game_power)

    return sum(game_power_list)


if __name__ == '__main__':
    print(solve_game_2())
