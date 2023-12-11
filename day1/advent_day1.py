import re


def solve_code(input_file='input.txt'):
    with open(input_file, 'r') as f:
        s = f.readlines()

    value_list = []
    for i in s:

        regex_nums = re.sub("[a-zA-Z\n]", "", i)
        value_list.append(int(regex_nums[0] + regex_nums[-1]))
    return sum(value_list)


def solve_part2(input_file='input.txt'):
    string_to_number = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]
    with open(input_file, 'r') as f:
        s = f.readlines()

    # s = ['two1nine', '7ckxjmlpkqqqjtfiveeightbmmdoneighttnv', 'eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    value_list = []

    for i in s:
        digits = re.finditer(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", i)
        digits =[match.group(1) for match in digits]
        first = digits[0]
        last = digits[-1]

        for word, number in string_to_number:
            first = first.replace(word, str(number))
            last = last.replace(word, str(number))
        value_list.append(int(first + last))
    return sum(value_list)


if __name__ == '__main__':
    print(solve_part2())

