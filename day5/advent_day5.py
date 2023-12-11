import re
import time

short_almanac = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def get_mapping(destination_range, source_range, range_length):
    return {int(source_range) + k: int(destination_range) + k for k in range(int(range_length))}


def get_full_mappings(mapping_dict, key):
    aux = {}
    for i in mapping_dict[key]:
        aux.update(get_mapping(*i))
    return aux


def get_full_list_mappings(mapping_dict, key):
    start = []
    end = []
    for i in mapping_dict[key]:
        aux.update(get_mapping(*i))
    return aux


def get_all_locations_small(input_file='input.txt'):

    with open(input_file) as file:
        almanac_info = file.read()

    process_steps = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

    almanac_splitted = [re.split(r'\s*[map]*\s*:\n?\s*', i) for i in almanac_info.split('\n\n')]
    seeds = almanac_splitted[0]
    mappings = {i[0]: [j.split(' ') for j in i[1].split('\n')] for i in almanac_splitted[1:]}
    seeds = seeds[1].split(' ')

    simplified_mappings = dict()
    for key in mappings.keys():
        simplified_mappings[key] = get_full_mappings(mappings, key)

    print('lets get the locations')
    locations = []
    for s in seeds:
        seed_chain = [int(s)]
        for i in range(len(process_steps) - 1):
            map_name = process_steps[i] + '-to-' + process_steps[i + 1]
            seed_chain.append(simplified_mappings[map_name].get(seed_chain[-1], seed_chain[-1]))
        locations.append(seed_chain[-1])

    return locations


def get_all_locations_fast(input_file='input.txt'):

    with open(input_file) as file:
        almanac_info = file.read()

    process_steps = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

    almanac_splitted = [re.split(r'\s*[map]*\s*:\n?\s*', i) for i in almanac_info.split('\n\n')]
    seeds = almanac_splitted[0]
    mappings = {i[0]: [[int(k) for k in j.split(' ')] for j in i[1].split('\n')] for i in almanac_splitted[1:]}

    seeds = seeds[1].split(' ')

    locations = []
    for s in seeds:
        seed_chain = [int(s)]
        for i in range(len(process_steps) - 1):
            map_name = process_steps[i] + '-to-' + process_steps[i + 1]
            found_aux = False
            for destination, source, range_length in mappings[map_name]:
                if source <= seed_chain[-1] <= source + range_length:
                    seed_chain.append(destination + seed_chain[-1] - source)
                    found_aux = True
                    break
            if not found_aux:
                seed_chain.append(seed_chain[-1])
        locations.append(seed_chain[-1])

    return locations


def get_all_locations_part2(input_file='input.txt'):

    with open(input_file) as file:
        almanac_info = file.read()

    process_steps = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

    almanac_splitted = [re.split(r'\s*[map]*\s*:\n?\s*', i) for i in almanac_info.split('\n\n')]
    seeds = almanac_splitted[0]
    mappings = {i[0]: [[int(k) for k in j.split(' ')] for j in i[1].split('\n')] for i in almanac_splitted[1:]}

    seeds = seeds[1].split(' ')
    seed_pairs = [(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)]

    min_location = 999827832388 # random super high number

    print('Starting the search')
    seed_cnt = 0
    total_seed_cnt = 0
    t1 = time.time()
    for base_seed, seed_range in seed_pairs:
        t2 = time.time()
        seed_cnt += 1
        print('Going with seed %d out number %d out of the total %d.' % (base_seed, seed_cnt, len(seed_pairs)))
        print('Time for the last run: %f' % (t2 - t1))
        print('Current Minimum found: %d' % min_location)
        t1 = time.time()
        for i in range(seed_range):
            seed_chain = [base_seed + i]
            total_seed_cnt += 1
            for i in range(len(process_steps) - 1):
                map_name = process_steps[i] + '-to-' + process_steps[i + 1]
                found_aux = False
                for destination, source, range_length in mappings[map_name]:
                    if source <= seed_chain[-1] <= source + range_length:
                        seed_chain.append(destination + seed_chain[-1] - source)
                        found_aux = True
                        break
                if not found_aux:
                    seed_chain.append(seed_chain[-1])
            if seed_chain[-1] < min_location:
                min_location = seed_chain[-1]

    return min_location, total_seed_cnt


if __name__ == '__main__':

    print(get_all_locations_part2())

    # with open('input.txt') as file:
    #     almanac_info = file.read()
    #
    # process_steps = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    #
    # almanac_splitted = [re.split(r'\s*[map]*\s*:\n?\s*', i) for i in almanac_info.split('\n\n')]
    # seeds = almanac_splitted[0]
    # mappings = {i[0]: [[int(k) for k in j.split(' ')] for j in i[1].split('\n')] for i in almanac_splitted[1:]}
    #
    # seeds = seeds[1].split(' ')
    # # print(seeds)
    # seed_pairs = [(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)]
    # all_the_seeds = []
    # for base_seed, seed_range in seed_pairs:
    #     for i in range(seed_range):
    #         all_the_seeds.append(base_seed + i)
    #
    # print(len(all_the_seeds))

