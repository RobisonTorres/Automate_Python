# Monthly Personal Budget Report Automation

This Python script automates the process of generating and sending a monthly Personal Budget Report via email.

## Intro

The goal of this project is to show an example of automation and serves as quick reference.

## Features

1. `send_email.py`: This script uses the `take_report` module to gather financial data and sends an email with the monthly Personal Budget Report attached.

2. `take_report.py`: This module utilizes the `openpyxl` library to extract financial data from the 'Personal_Budget.xlsx' file.

## Prerequisites

- Python 3.x
- Required Python packages: `win32com`, `openpyxl`
- Outlook

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RobisonTorres/Automate_Python.git
    ```

2. Install the required packages:

    ```bash
    pip install pywin32 openpyxl
    ```

## Usage

1. Run the `send_email.py` script:

    ```bash
    python send_email.py
    ```

2. Follow the prompts to input the recipient's email address.

3. The script will generate a detailed budget report and send it via email.

## Notes

- Ensure that 'Personal_Budget.xlsx' is present in the project directory.

- The email is sent using the Outlook application. Make sure Outlook is installed and configured on your machine.