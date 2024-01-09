import sys, re
sys.path.append(r'C:\Users\rcssi\Code\Automate_Python\Image_Reader')
import reader_numbers

def get_numbers():

    # This function retrieves numbers from image and processes them to form lottery games. 
    your_games = []   
    numbers_retrieved = reader_numbers.read_nums(f'games.png')
    games_retrieved =  re.sub(r'(#\d)|(\@\d+)', ' ', numbers_retrieved).split()
    round_retrieved = re.sub(r'(#\d+)|(\@)', '', numbers_retrieved)
   
    for x in range(0, len(games_retrieved)):
        nums = [int(n) for n in games_retrieved[x]]   
        numbers = [nums.pop(0)]

        while len(numbers) < 15:
            numbers.append(nums.pop(0) if (nums[0]) > numbers[-1]
                                       else int(str(nums.pop(0)) + str(nums.pop(0))))
        your_games.append(numbers)   

    return [your_games, round_retrieved]

def show_games():

    # This function shows the games retrieved from the image.
    image_result = get_numbers()
    your_games = image_result[0]
    show = []

    for n, game in enumerate(your_games, 1):
        show.append(f'{str(n)}° Game - {("-".join(map(str, game)))}')

    return '\n'.join(show)

if __name__ == "__main__":
    
    print(show_games())