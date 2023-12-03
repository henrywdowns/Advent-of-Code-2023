#three cubes: red, green, blue
#each game, an unkown number of cubes of each color put in bag
#a few cubes revealed, record info, then this repeats a few times per game
#play several games
#recorded info is my input
#each game has ID number, like game 11 ID is 11
#then, a semicolor separated list of subsets of cubes: ie, 3 red, 5 green, 4 blue
# record of a game might look like this:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#determine in which games its possible if the bag contained only 12 red, 13 green, and 14 blue
#basically, if you see more than any of these numbers in any reveal, you know it's impossible.
#then, sum the IDs

print('\n\n\n============RUN CODE============\n\n\n')



with open('Dec 2/input.txt','r',newline='\n') as input_doc:
    input_arr = [line.strip() for line in input_doc.readlines()]

sample_arr = input_arr[10:11]
# print(sample_arr)

# for i in sample_arr:
#     print(i)
colors = ['red','blue','green']
color_dict = {
    'red':12,
    'green':13,
    'blue':14
}

def cleanup(item): #turn a line of raw text (which represents 1 game) into a list of the results for that game
    dice_reveal_lst = []
    game_split = [i for i in item[item.index(':')+2:].split(';')]
    for reveal in game_split:
        dice_reveal_lst.append(reveal.split(','))
    return dice_reveal_lst #returns a list of lists. superlist is the game, sublists are reveals


# for game in sample_arr:
#     print(cleanup(game))

def eval_games(game_lst): #read each cleanup game_split to find the highest number of each color
    total = 0
    for game in game_lst:
        truthy_dict = {
            'red': False, #set each color to False. if at any point in the game a number exceeding the limit is revealed, set these to True
            'blue': False,
            'green': False}
        game_id = int(game[4:game.index(':')]) #isolate the number for the game ID. if the eval returns True this gets added to total
        cleaned = cleanup(game)
        for reveal in cleaned: #reveal is a subsection of a game
            for dice_category in reveal: #dice_category represents the colors
                for color in colors: #iterate through the three possible colors
                    if color in dice_category and truthy_dict[color] == False: #if the color is revealed and we haven't already switched it to True this game...
                        number = int(dice_category[:dice_category.index(color)-1]) #extract the number of cubes shown
                        if number > color_dict[color]: truthy_dict[color] = True #compare to the limit and switch to True if exceeding
        if not any(truthy_dict.values()): #if nothing has exceeded, increment total by game_id
            total += game_id
        print(f'Game: {game_id}\n{truthy_dict}\nNew total: {total}')
    return total
                        

print(eval_games(input_arr))
