import requests, bs4, re

def web_search(round):

    # This function accesses the lottery's page and takes the html.
    url = f'https://www.intersena.com.br/lotofacil/resultados/{round}'
    source = requests.get(url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    return soup

def extract_search(round=False):

    # This function extracts only the lottery result from 
    # the web_search, and gives a proper format to the result.
    if round == False: round = input('What round do you want to check: ')
    
    target = web_search(round)
    round_found = target.find('h1', class_='col-md-6 col-sm-6 col-xs-12')  
    lottery_numbers = target.find('div', class_='resultado-individual-sorteio')  
    
    # Only numbers.
    round_found = re.sub('[^0-9]', '', round_found.text)
    lottery_numbers = re.sub('[^0-9]', '', lottery_numbers.text)
      
    if str(round) != round_found: 
        return f'\nRound: {round} - Result not found.\n'

    else:
        lottery_result = [int(lottery_numbers[x:x+2]) for x in range(0, len(lottery_numbers), 2)]
        return [lottery_result, round]