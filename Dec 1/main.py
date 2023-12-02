import re

input_arr = []
digits = ['1','2','3','4','5','6','7','8','9','0']
number_names = ['one','two','three','four','five','six','seven','eight','nine','zero']

with open('input.txt','r') as input_doc:
    lines = input_doc.readlines()

for line in lines:
    input_arr.append(line)

def digit_first_and_last(list):
    keylist = []
    addItUp = 0
    for item in list:
        digitHolder = ''
        for letter in str(item):
            if letter in digits:
                digitHolder += letter
        digitHolder = digitHolder[0]+digitHolder[-1]
        keylist.append(digitHolder)

    for item in keylist:
        item = int(item)
        addItUp += item
    
    return addItUp

# print(first_and_last(input_arr))


def all_first_and_last(input_list):
    keylist = []
    addItUp = 0
    for item in input_list:
        matches = re.findall(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)', item)
        # print(matches[:4])
        for subitem in range(len(matches)):
            figure = matches[subitem]
            if figure in number_names:
                # print(f'{figure} at index {number_names.index(figure)}')
                # print(f'{figure} equals {digits[number_names.index(figure)]}')
                matches[subitem] = digits[number_names.index(figure)]
        keylist.append(str(matches[0]+matches[-1]))
    print(keylist)
    for item in keylist:
        addItUp += int(item)
    return addItUp

    
sample_list = (input_arr)
print(sample_list)
print(all_first_and_last(sample_list))

