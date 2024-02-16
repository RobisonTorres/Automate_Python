import web_scraper, games_image
print('Checking Score.')
print()

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
            score_result.append(str(num) + '° Game - Score: ' 
                                   +  str(15 - len(set(numbers_result) - set(game))))
        return '\n'.join(score_result)

print(score([[],
           [],
           [],
           [],
           [],
           []]))

def auto_checking(file):

    # This function checks the score automatically.
    return score(*games_image.get_numbers(file))

print(auto_checking(f'games.png'))  # Don't forget to change the file.png