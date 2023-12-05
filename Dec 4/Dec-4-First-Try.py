with open('Dec 4/input.txt','r',newline='') as doc:
    lines = doc.readlines()

sample_input = lines
scratch_cards = []

def parse_lines(lines):
    winner_set = []
    card_set = []
    for line in lines:
        cut_card_name = line.strip().split(':')
        winner_str = (cut_card_name[1].strip().split('|')[0].split())
        card_set_str = (cut_card_name[1].strip().split('|')[1].split())
    
        winner_int = list(map(int, winner_str))
        card_set_int = list(map(int, card_set_str))
    
        winner_set.append(winner_int)
        card_set.append(card_set_int)

    print(winner_set)
    print(card_set)    
    return winner_set,card_set

def card_scorer(matches):
    if matches == 0:
        score = 0
    else:
        score = 2**(matches-1)
    print(f'Applying score of {score}')
    return score

print(parse_lines(sample_input))

def read_cards(input):
    print('=========NEW OUTPUT=========')
    winning_numbers, numbers_you_have = parse_lines(input)
    running_total = 0

    if len(winning_numbers)!=len(numbers_you_have):
        return "uneven sets"
    
    for card_num, card in enumerate(winning_numbers):
        print(f'Evaluating card number {card_num+1}\n Winning numbers: {winning_numbers[card_num]} \n Numbers you have: {numbers_you_have[card_num]}')
        card_matches = 0
        match_list = []
        for winning_num in set(card):
            print(f'Checking Winning Number: {winning_num}')
            if winning_num in numbers_you_have[card_num]:
                print(f'Found winning number!')
                match_list.append(winning_num)
                #card_matches +=1
        card_matches += len(set(match_list))
        print(f'Card matches: {card_matches}')
        print(f'Matching numbers: {match_list}')
        running_total += card_scorer(card_matches)
    return running_total

print(read_cards(sample_input))