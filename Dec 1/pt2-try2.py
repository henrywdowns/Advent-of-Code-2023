from collections import OrderedDict

final_sum = 0
digits = ['1','2','3','4','5','6','7','8','9','0']
number_names = ['one','two','three','four','five','six','seven','eight','nine','zero']
first_and_len = [[i[0] for i in number_names],[len(i) for i in number_names]]

with open('Dec 1/input.txt','r',newline='\n') as input_doc:
    input_arr = [line.strip() for line in input_doc.readlines()]

def convert_word_to_digit(word):
    if word in number_names:
        ind = number_names.index(word)
        return int(digits[ind])
    else:
        return ''
    
def find_nums(item):
    numString = ''
    for iInd, i in enumerate(item):
        if i in digits:
            numString += i
        else:
            for xInd, x in enumerate(first_and_len[0]):
                xLen = first_and_len[1][xInd]
                if x == i:
                    wordNum = item[iInd:iInd + xLen]
                    newDigit = convert_word_to_digit(wordNum)
                    if str(newDigit) in digits:
                        numString += str(newDigit)
    numString = int(numString[0]+numString[-1])
    return numString

first_last_lst = [find_nums(item) for item in input_arr]
for i in first_last_lst:
    final_sum+= i

print(final_sum)