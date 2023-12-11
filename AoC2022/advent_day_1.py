with open('day1_input.txt', 'r') as f:
    # while
    s = f.readlines()

l = []
all_elves_calories = []
max_sum = 0

for i in s:
    if i == '\n':
        total_sum = sum(l)
        all_elves_calories.append(total_sum)
        if total_sum > max_sum:
            max_sum = total_sum
        l = []
    else:
        l.append(int(i.replace('\n', '')))

total_sum = sum(l)
if total_sum > max_sum:
    max_sum = total_sum

print(max_sum)
all_elves_calories.sort()
print('The maximum value is: %d' % max_sum)
print('The sum of top 3 is: %d' % sum(all_elves_calories[-3:]))
