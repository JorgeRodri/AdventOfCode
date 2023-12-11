# In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have
# (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers!
# That means card 1 is worth 8 points (1 for the first match, then doubled three times
# for each of the three matches after the first).
import re


def read_file(filename) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

first_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def get_winning_points(input_file='input.txt'):

    scratched_cards = read_file(input_file)
    cleaned_scratched_cards = [re.sub(r"\s+", ' ', i.strip()) for i in scratched_cards]
    cards = dict()
    for line in cleaned_scratched_cards:
        # print(re.match(r"Card\s\d+:\s", line).group())
        this_numbers = re.sub(r"Card\s\d+:\s", '', line).split('|')
        winning_numbers = this_numbers[0].strip().split(' ')
        my_numbers = this_numbers[1].strip().split(' ')

        my_winning_numbers = [i for i in my_numbers if i in winning_numbers]

        cards[re.match(r"Card\s\d+:\s", line).group()] = my_winning_numbers

    score = sum([2 ** (len(i) - 1) for i in cards.values() if len(i) != 0])
    return cards, score


def get_number_of_cards(input_file='input.txt'):
    winning_cards, total_score = get_winning_points(input_file)

    print("part 1 total score is : %d" % total_score)

    winning_numbers_and_copies = [[len(value), 1] for key, value in winning_cards.items()]

    for i in range(len(winning_numbers_and_copies)):
        this_number_of_copies = winning_numbers_and_copies[i][0]
        for j in range(1, this_number_of_copies + 1):
            if i + j < len(winning_numbers_and_copies):
                winning_numbers_and_copies[i + j][1] += winning_numbers_and_copies[i][1]

    return winning_numbers_and_copies, sum([i[1] for i in winning_numbers_and_copies])


if __name__ == '__main__':
    # winning_cards, total_score = get_winning_points()
    winning_cards_copies, total_score = get_number_of_cards()

    print("Part 2 total score is : %d" % total_score)
