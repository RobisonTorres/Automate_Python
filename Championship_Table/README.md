# Championship Table

This repository stores functions to download the table and perform data analysis for the main soccer championship of Brazil.

## Intro

The main goal of this project is to retrieve the championship table of Brazil, save it as an Excel file, and analyze some data to help choose the best bet.

## Features 

- Championship table as an Excel file.
- Data analysis.

## Prerequisites

You must have Python installed on your computer, as well as the necessary packages.

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/RobisonTorres/Automate_Python.git

2. Install the required packages:

   ```bash
   pip install requests beautifulsoup4 pandas

3. Navigate to the directory:

   ```bash
   cd Automate_Python/Championship_Table

4. Choose a function:

    * To download the championship table or get some analyzes, use respectively:
    ```bash
   python championship_table.py
   python analysis.py

## Example
Example of info retrieved after using the analysis.py:
```
----------------  -----------------
More W            Less W
         Club  W            Club  W
Botafogo (RJ) 12  Atl Goianiense  2
     Flamengo 12     Corinthians  4
     Cruzeiro 11          Cuiabá  4
    Palmeiras 11      Fluminense  4
    Fortaleza 10         Vitória  5
----------------  -----------------
```
## Issues

Sometimes the web scraping doesn't work properly, resulting in a blank Excel file. If this happens, simply retry until you get all the information.