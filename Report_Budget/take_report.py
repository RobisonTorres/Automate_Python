import openpyxl, warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category = UserWarning)
    wb = openpyxl.load_workbook('Personal_Budget.xlsx', data_only = True)
    wb = wb['Balance & Tracking']

def get_balance():

    # This function extract data from Personal_Budget.xlsx.
    current_balance = wb['C3'].value
    annual_balance = wb['C12'].value
    return f'The current balance is $ {current_balance}.'\
           f'The annual balance is $ {annual_balance}.' 
