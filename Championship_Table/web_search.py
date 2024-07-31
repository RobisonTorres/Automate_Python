import requests, bs4

def web_search():

    # This function accesses the page and takes the html. 
    url = 'https://fbref.com/pt/comps/24/Serie-A-Estatisticas'
    source = requests.get(url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    return soup

def extract_search_championship_table(soup):

    # This function extracts the championship table from the html.
    table = soup.find('table', {'id': 'results2024241_overall'})
    rows = table.find_all('tr')
    table = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        table.append([ele for ele in cols if ele])  
    dictionary = {}
    for x in range(1, 21):
        dictionary[table[x][0]] = [table[x][1], table[x][2], table[x][3], table[x][4], table[x][5], table[x][6], table[x][7], table[x][8]]
    dictionary = dict(sorted(dictionary.items(),key=lambda x: x[0])) 
    return dictionary

def extract_search_shoot_defense(soup):

    # This function extracts the shoots and defenses info from the html.
    try:
        table = soup.find('table', {'id': 'stats_squads_shooting_for'})
        rows = table.find_all('tr')
        shoots = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            shoots.append([ele for ele in cols if ele])  
        shoots = [ele[4] for ele in shoots[2:]]

        table = soup.find('table', {'id': 'stats_squads_defense_for'})
        rows = table.find_all('tr')
        defenses = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            defenses.append([ele for ele in cols if ele])  
        defenses = [ele[3] for ele in defenses[2:]]
        return [shoots, defenses]
    except:
        return 'Something went wrong. Try again.'
