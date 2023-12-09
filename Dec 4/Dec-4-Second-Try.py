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
 
    return winner_set,card_set

win, play = (parse_lines(sample_input))

def create_card_dict(winning,playing):
    output_dict = {}
    for card_num, winners in enumerate(winning):
        output_dict[card_num] = [set(winners),set(playing[card_num])]
    return output_dict

card_dict = create_card_dict(win,play)

def count_winners (winning, playing):
    total_score = 0
    for card_num, winners in enumerate(winning):
        win_set = set(winners)
        play_set = set(playing[card_num])
        winning_numbers = win_set.intersection(play_set)
        score = 0
        if len(winning_numbers)>0:
            score = 2**(len(winning_numbers)-1)
        total_score+=score
    return total_score

def part_2_winners(dictionary,input,winning,playing):
    total_cards = 0
    card_list = [i for i in range(len(input))]
    card_counts = {} #my inventory of cards as a dict
    try:
        for ind in range(len(input)):
            card_counts[ind] = 1 #i have one of each original to start
        for i in card_list: #iterate through card numbers
            for amount in range(card_counts[i]): #reiterate through card numbers for each copy we have
                total_cards += 1
                card_counts[i] -= 1 #this card has been played, so we lower its count in the dict
                win_set = set(winning[i]) #isolate winning numbers
                play_set = set(playing[i]) #isolate numbers played
                winning_numbers = win_set.intersection(play_set) #find the intersection
                print(f'Card {i} has {len(winning_numbers)} winning_numbers ({winning_numbers})')
                new_cards = [] #hold the new cards
                for card_no in range(i + 1, i + len(winning_numbers) + 1):
                    new_cards.append(card_no)
                #print(f'New cards: {new_cards}')
                for x in new_cards:
                    if card_counts[x]:
                        card_counts[x] += 1
        return card_counts, total_cards
    except:
        print('Error occurred')
        return card_counts, total_cards

    

print('\n\n\n========================= RUN CODE =========================\n\n\n')
print(f'card dict: {card_dict}')
final_score = count_winners(win,play)
print(final_score)
print(f'{part_2_winners(card_dict,sample_input,win,play)}')