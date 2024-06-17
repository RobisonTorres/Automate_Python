import web_scraper, games_image
print('Checking Score.\n')

def takeGame():

    nums = input("Enter the Lottery games separated by commas, each with 15 numbers: ").strip().split(',')
    your_games = [list(map(int, game)) for game in nums]
    choseNumbers = []   
    for game in your_games:
        new_game = [game.pop(0)]
        while len(game) > 1:
            new_game.append(game.pop(0) if (game[0]) > new_game[-1]
                                       else int(str(game.pop(0)) + str(game.pop(0))))   
        choseNumbers.append(new_game) 
    return choseNumbers

# Not working.
def score(your_games, round=False):
    
    # This function checks the total score hit in each lottery ticket.
    lottery_result = web_scraper.extract_search(round)
    if type(lottery_result) == str:
        return lottery_result
    else:
        numbers_result = lottery_result[0]            
        round = lottery_result[1]
        print(f'\nRound: {round} - Result: {("-".join(map(str, numbers_result)))}\n')

        # Comparing the lottery's result with your games.
        score_result = []
        for num, game in enumerate(your_games, 1):
            if len(game) != 15:
                score_result.append("Error, games must have 15 numbers.")
            else:    
                score_result.append(str(num) + '° Game - Score: ' 
                                   +  str(15 - len(set(numbers_result) - set(game))))
        return '\n'.join(score_result)

print(score(takeGame()))
print(score(*games_image.get_numbers(f'games.png')))  # Don't forget to change the file.png