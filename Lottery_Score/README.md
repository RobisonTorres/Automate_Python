# Lottery Score Checker

This python script automates the process of getting the score based on the lottery result.

## Intro

From time to time, my father asks me to check his score in the Lotofácil, a Brazilian lottery. This process was tedious because I had to visit the lottery website, compare the results with each game, and mark points and errors manually, sometimes double-checking for accuracy.

I decided to create a Python script to automate this process. My initial idea was to use the pytesseract package to read the games from the ticket and retrieve the results using web scraping with the bs4 module. However, pytesseract isn't 100% accurate in reading numbers from lottery tickets.

To address this, I implemented alternative options:

* Users can manually input each game as a 15-number array.
* Users can create games in MS Word, take screenshots (like in the games.png file), and use the script to process those images.

## Features 

 - ```checking_score.py``` - This function checks the total score hit in each lottery ticket.
 - ```games_image.py``` - This function retrieves numbers from image and processes them to form lottery games. 
 - ```web_scraper.py``` - This function accesses the lottery's site and retrieve the result.
 
## Prerequisites

- Python
- Required Python packages: `requests`, `bs4`
- Image_Reader project.

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/RobisonTorres/Automate_Python.git

2. Install the library requests bs4e.

   ```bash
   pip install requests bs4

3. Navigate to the directory:

   ```bash
   cd Automate_Python/Lottery_Score

4. Choose a function:

    * To check the your score:
    ```bash
   python checking_score.py
    ```
    * To make sure the program read the numbers correctly:
    ```bash
   python games_image.py

5. Follow the instructions prompted into your screen to download.