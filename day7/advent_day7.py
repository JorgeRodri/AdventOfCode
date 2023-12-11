import re
from functools import cmp_to_key
from collections import Counter


def read_file(filename) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def get_hand_value(card_hand):

    hand_counter = Counter(card_hand).most_common()
    if hand_counter[0][1] == 5:
        # repoquer
        return 7
    if hand_counter[0][1] == 4:
        # poquer
        return 6
    if hand_counter[0][1] == 3 and hand_counter[1][1] == 2:
        # full house
        return 5
    if hand_counter[0][1] == 3:
        # triples
        return 4
    if hand_counter[0][1] == 2 and hand_counter[1][1] == 2:
        # dobles parejas
        return 3
    if hand_counter[0][1] == 2:
        # pareja
        return 2
    else:
        # Carta alta
        return 1


def is_greater_than(hand_bet1, hand_bet2):

    hand1 = hand_bet1[0]
    hand2 = hand_bet2[0]

    value_hand1 = get_hand_value(hand1)
    value_hand2 = get_hand_value(hand2)
    if value_hand1 > value_hand2:
        return 1
#    elif value_hand2 > value_hand1:
#        return hand2
    elif value_hand1 == value_hand2:
        cards_ordered = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

        for i in range(len(hand1)):
            if cards_ordered.index(hand1[i]) < cards_ordered.index(hand2[i]):
                return 1
            elif cards_ordered.index(hand1[i]) > cards_ordered.index(hand2[i]):
                return -1
    return -1



small_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

hand_list = [i.split(' ') for i in read_file('input.txt')] #[i.split(' ') for i in small_input.split('\n')]

# hand_list = [i.split(' ')[0] for i in small_input.split('\n')]
# bet_list = [int(i.split(' ')[1]) for i in small_input.split('\n')]

sorted_hands = sorted(hand_list, key=cmp_to_key(is_greater_than))
total_bets = 0

print(sorted_hands)

rank_i = 1
for cards, bet in sorted_hands:
    total_bets += rank_i * int(bet)
    rank_i += 1

print(total_bets)

