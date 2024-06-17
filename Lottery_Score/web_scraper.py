from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def web_search(round):

    # This function accesses the lottery's page and takes the result.
    driver = webdriver.Chrome()
    driver.get("https://www.intersena.com.br/lotofacil/resultados")

    # Input the round, clink the button and get the result.
    search = driver.find_element(By.ID, "inputNumeroConcurso")
    search.send_keys(round)
    click_button = driver.find_element(By.XPATH, "//*[contains(text(), 'PESQUISAR')]").click()
    result = driver.find_element(By.CLASS_NAME, "table-responsive").text

    # Close the browser.
    driver.close()
    
    return result

def extract_search(round=False):

    # This function extracts only the lottery result from 
    # the web_search, and gives a proper format to the result.
    if round == False: round = input('What round do you want to check: ')

    # Perform the web search.
    lottery_numbers = web_search(round)

    # Convert the formatted string into a list of integers (each representing a lottery number)
    lottery_numbers = re.findall(r'(\d{2}(?:-\d{2}){14})', lottery_numbers)   
    lottery_numbers = re.sub('[^0-9]', '', lottery_numbers[0])
    lottery_result = [int(lottery_numbers[x:x+2]) for x in range(0, len(lottery_numbers), 2)]
    
    return [lottery_result, round]