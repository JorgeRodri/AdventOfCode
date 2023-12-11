import re
from functools import reduce  # Required in Python 3
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def read_file(filename) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def get_numbers_and_symbols(lines):
    numbers = []
    symbols = []
    for i, line in enumerate(lines):
        numbers.append([])
        for numb in re.finditer(r"\d+", line):
            numbers[i].append((numb.group(), i, numb.start(), numb.end()))

        for symbol in re.finditer(r"[^\.\d]", line):
            symbols.append((i, symbol.start()))

    return numbers, symbols


def get_matched_numbers(symbols, numbers):
    valid_numbers = set()
    for symb in symbols:
        for i in range(symb[0] - 1, symb[0] + 2):
            for j in range(symb[1] - 1, symb[1] + 2):
                if i >= 0:
                    for numb in numbers[i]:
                        if numb[2] <= j < numb[3]:
                            valid_numbers.add(numb)
    return list(map(lambda x: int(x[0]), valid_numbers))


def get_numbers_and_gears(lines):
    numbers = []
    symbols = []
    for i, line in enumerate(lines):
        numbers.append([])
        for numb in re.finditer(r"\d+", line):
            numbers[i].append((numb.group(), i, numb.start(), numb.end()))

        for symbol in re.finditer(r"[*]", line):
            symbols.append((i, symbol.start()))

    return numbers, symbols


def get_matched_numbers_to_gears(symbols, numbers):
    valid_products = set()
    for symb in symbols:
        this_gear_numbers = set()
        for i in range(symb[0] - 1, symb[0] + 2):
            for j in range(symb[1] - 1, symb[1] + 2):
                if i >= 0:
                    for numb in numbers[i]:
                        if numb[2] <= j < numb[3]:
                            this_gear_numbers.add(numb)

        if len(this_gear_numbers) > 1:
            valid_products.add(prod(list(map(lambda x: int(x[0]), this_gear_numbers))))
    return valid_products


def solve_part_1():
    found_numbers, found_symbols = get_numbers_and_symbols(read_file('input.txt'))
    print(found_symbols)
    good_numbers = get_matched_numbers(found_symbols, found_numbers)
    return good_numbers


def solve_part_2():
    found_numbers_gears, found_gears = get_numbers_and_gears(read_file('input.txt'))
    gears_products = get_matched_numbers_to_gears(found_gears, found_numbers_gears)
    return gears_products


if __name__ == '__main__':
    basic_schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    splitted_lines = basic_schematic.split('\n')

    # print(sum(solve_part_1()))
    print(sum(solve_part_2()))
