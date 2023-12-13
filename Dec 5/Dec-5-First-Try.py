with open('Dec 5/input.txt','r',newline='') as doc:
    lines = doc.readlines()

sample_input = lines

# print(sample_input)
data = []
for line in sample_input[2:]:
    data.append(line.strip())

#print(f'Data length: {len(data)}; supplies length: {len(supplies)}')

print('*****===================NEW RUN====================*****')

seeds = []
for line in sample_input[0:1]:
    seeds.extend(line.strip().split(':')[1].split())

# print(seeds)

def is_between(number_input,lower_bound,upper_bound):
    return lower_bound<=number_input<=upper_bound

def min_seed_in_range(range_min,range_max):
    return min([parse_map_string(seed) for seed in range(range_min,range_max)])

def make_dict():
    result_dict = {}
    last_map = ''
    for item in data:
        if item == '':
            pass
        elif item.endswith(':'):
            last_map = item[:len(item)-1]
            result_dict[last_map] = []
        else:
            result_dict[last_map].append(item)

    
    return result_dict

def parse_one_map(map,input_id):
    for conversion in map:
        split_conversion = [int(i) for i in conversion.split()]
        # print(split_conversion)
        if input_id in range(split_conversion[1],split_conversion[1]+split_conversion[2]):
            difference = input_id-split_conversion[1]
            converted_id = split_conversion[0]+difference
            #print(f'PARSE_ONE_MAP() --- Input ID {input_id} found between {split_conversion[1]} and {split_conversion[1]+split_conversion[2]}! Difference is {difference}, converted ID is {converted_id}')
            return converted_id
    converted_id = input_id
    #print(f'PARSE_ONE_MAP() --- ID not mapped. Returning same ID: {converted_id}')
    return converted_id

def parse_map_string(seed_id):
    supply_dict = make_dict()
    supplies = ['seed-to-soil map','soil-to-fertilizer map','fertilizer-to-water map','water-to-light map','light-to-temperature map','temperature-to-humidity map','humidity-to-location map']
    # debug_old_id = 0
    current_id = seed_id
    for supply in supplies:
        debug_old_id = current_id
        current_id = parse_one_map(supply_dict[supply],current_id)
        #print(f'PARSE_MAP_STRING() --- Parsed {supply}. ID {debug_old_id} converted to {current_id}')
    return current_id

seeds = [int(i) for i in seeds]
print(seeds[0])


parse_map_string(seeds[0])

# debug_dict = make_dict()
# parse_one_map(debug_dict['seed-to-soil map'],858905075)

print(f'Seeds: {seeds}')

locations = [parse_map_string(seed) for seed in seeds]
print(min(locations))

seed_ranges = {}
for seed in range(0,len(seeds),2):
    seed_ranges[seeds[seed]] = [seeds[seed], seeds[seed+1]]

def compare_seed_range_to_soil_maps(seed,map_to_use):
    seed_start = seed_ranges[seed][0]
    seed_end = seed_ranges[seed][1]
    map_dicts = make_dict()
    lowest_range_location = 0
    for mappy_thing in map_dicts[map_to_use]:
        mappy_thing = mappy_thing.split()
        map_start = mappy_thing[1]
        map_end = mappy_thing[1]+mappy_thing[2]-1
        if is_between(seed_start,map_start,map_end) and is_between(seed_end,map_start,map_end):
            lowest_range_location = min_seed_in_range(seed_start,seed_end)
        elif is_between(seed_start,map_start,map_end):
            lowest_range_location = min_seed_in_range(seed_start,map_end)
        elif is_between(seed_end,map_start,map_end):
            lowest_range_location = min_seed_in_range(map_start,seed_end)
        else:
            return seed_start
    return lowest_range_location

