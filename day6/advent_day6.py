# t0 = tiempo
# Distancia(t) = v * (t)
# total = t0(t_total - t0)
# Dist_max -> d_total' = 0
# Dist_max -> t_total - 2
# t0 = 0
# Tiempo_pulsando = t_0 / 2

# Dada la distancia X
# Entonces X = t_total * t0 - t0 ** 2
# Por lo que t0 ** 2 - t_total * t0 + X
# T0 = (t_total - + √(t_total) ** 2 - 4 x) / 2

import re
from math import sqrt, floor

input_string = """Time:        38     94     79     70
Distance:   241   1549   1074   1091"""

main_input = input_string.split('\n')

# print(re.findall(r"[a-zA-Z]+", input_string))

time_list, distance_list = [re.split(r"[a-zA-Z]*:?\s+", i) for i in main_input]

time_list.pop(0)
distance_list.pop(0)

time_list.append(''.join(time_list))
distance_list.append(''.join(distance_list))

print(time_list)
print(distance_list)


def get_min_max_distance(distance, ttotal):
    min_time = (ttotal - sqrt(ttotal ** 2 - 4 * distance)) / 2
    max_time = (ttotal + sqrt(ttotal ** 2 - 4 * distance)) / 2
    return min_time, max_time


prod = 1

for i in range(len(time_list) - 1, len(time_list)):
    mint, maxt = get_min_max_distance(int(distance_list[i]), int(time_list[i]))
    prod *= floor(maxt) - floor(mint)

print(prod)
