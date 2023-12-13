with open('Dec 6/input.txt') as input_doc:
    lines = [line.strip() for line in input_doc.readlines()]

race_dict = {}


race_dict['time'] = lines[0].split(":")[1:][0].split()
race_dict['distance'] = lines[1].split(":")[1:][0].split()

races = [(time, dist) for time, dist in zip(race_dict['time'],race_dict['distance'])]

# PART 1

def calc_press_times(race_time,rec_dist):
    time = int(race_time)
    wins = 0
    for ms in range(time+1):
        if ms*(time-ms) > int(rec_dist):
            wins += 1
    return wins

ans_list = []

for race in races:
    ans_list.append(calc_press_times(race[0],race[1]))

print(ans_list)
time_product = 1
for x in ans_list:
    time_product *= x

print(time_product)
#1195150


# PART 2

one_time = ''
for char in lines[0]:
    if char.isdigit():
        one_time += char
one_time = int(one_time)

one_dist = ''
for char in lines[1]:
    if char.isdigit():
        one_dist += char
one_dist = int(one_dist)

print(one_time,one_dist)

print(calc_press_times(one_time,one_dist))
#42550411