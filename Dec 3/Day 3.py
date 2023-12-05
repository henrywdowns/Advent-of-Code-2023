from collections import defaultdict

final_ans = 0

with open('input.txt','r',newline='') as input_doc:
    input_arr = [line.strip('\n') for line in input_doc.readlines()]

sample_arr = input_arr
print(f'Sample Array: {len(sample_arr)} items long')

symbols_list = ['#','$', '%', '&', '*', '+', '-', '/']

def num_and_symbol_coords(list):
    nums = defaultdict(int) #dictionary that returns a default value instead of throwing an error if searching for something not in there
    symbols = defaultdict(str)
    for y, line in enumerate(list): #iterate through the lines
        num = '' #empty variable that resets each line
        for x, c in enumerate(line): #iterate through characters in line
            if c.isdigit(): #if c is a digit...
                num += c #add c to the empty variable as a string
            elif num: #if c isnt a digit but num is no longer empty (ie we have hit the end of a number)...
                nums[(x-len(num),y)] = int(num) #add to nums dict; (x-len(num)) is the position of the leftmost digit if num; y is y
                num = '' #reset num

            if c != '.' and not c.isdigit(): #if c is a non-number character other than '.'...
                symbols[(x,y)] = str(c) #create a symbols entry at that location with value of character
        if num: #after all this, if num is not empty at end of line...
            nums[(len(line)-len(num),y)] = int(num) #create dict key that looks back to coords of first char of num, value of num
            num = '' #reset num
    # print(nums)
    # print(symbols)
    return (nums, symbols) #return two dict objects

gear_counter = defaultdict(int)

def check_surroundings(nums,symbols):
    target = [] #empty list
    for x,y in nums: #iterate through nums, list of coordinates that contain first digit of numbers
        value = nums[(x,y)] #variable containing value attached to coordinate key. resets for each coordinate
        for i in range(-1, len(str(value)) + 1): #iterates from -1 to length of value+1
            if symbols[(x + i, y - 1)]: #add i to x in order to search 1 back and 1 past end of num, looking one line back
                target.append(value) #if we find a symbol in above iteration, add value to target list
            elif symbols[(x + i, y)]: #same here, but on same line as value
                target.append(value)
            elif symbols[(x + i, y + 1)]:#once more but one line ahead
                target.append(value)
    return target #return list of values adjacent to symbols

nums, symbols = num_and_symbol_coords(sample_arr)
for item in check_surroundings(nums,symbols):
    final_ans+= item

print(f'part 1: {final_ans}')


# part 2 plan: create two new dicts of coordinates. one that contains engines with symbols around them
# and one that contains symbols == *
# iterate through symbol coordinates. create empty list to contain surrounding num values
# iterate through num coordinates, adding any nums next to * using catch_surrounding_parts
# if that list has more than 1 value at the end of the loop, multiply values together and add to a running total
# return that total at the end

def catch_surrounding_parts(coords_to_reference,engine_boundaries,eng_val): #take gear coords, engine coords, and engine value as args
    min_coords = (engine_boundaries[0]-1,engine_boundaries[1]-1) #find top left coords for surrounding space
    max_coords = (engine_boundaries[0]+len(str(eng_val)),engine_boundaries[1]+1) #find bottom right for surrounding space
    return min_coords[0] <= coords_to_reference[0] <= max_coords[0] and min_coords[1] <= coords_to_reference[1] <=max_coords[1] #return true or false based on if gear coords adj to engine coords

def gear_ratio(array):
    nums, symbols = num_and_symbol_coords(array) #generate dicts of nums & symbols
    numbers = check_surroundings(nums, symbols) #generate list of nums adjacent to symbols
    engines = {k:v for k, v in nums.items() if v in numbers} #generate dict of nums adjacent to symbols with k = coordinates
    gears = {k:v for k, v in symbols.items() if v == '*'} #generate dict of symbols where symbols are *
    running_total = 0
    for gear_coords in gears: #iterate through *s
        adjacent = [] #empty list to hold engine values adjacent to *s
        for eng_coords in engines: #iterate through numbers adjacent to symbols
            eng_value = engines[eng_coords] #set variable equal to engines.values()
            if catch_surrounding_parts(gear_coords,eng_coords,eng_value): #invoke helper function
                adjacent.append(eng_value) #if true, add to adjacent
        if len(adjacent) == 2: #if there are two values, multiply them together and add to running total
            running_total += adjacent[0]*adjacent[1]
    return running_total

print(f'part 2: {gear_ratio(input_arr)}')