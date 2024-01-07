import take_report, win32com.client as win32, os
print('Sending Email.')

outlook = win32.Dispatch('outlook.application') # Python-Outlook integration.
mail = outlook.CreateItem(0)

def send_email():

    # This function sends the email with the monthly Personal Budget.
    balance = take_report.get_balance()
    mail.to = input('Please type in the recipient: ')
    mail.Subject = 'Monthly Personal Budget Report.'
    email_content = f'''

    Dear Mr. ,

    I hope this message finds you well.
    {balance}
    Attached, please find the detailed budget. This report encompasses a comprehensive \n
    overview of our financial activities, including income, expenditures, savings, and \n
    any other pertinent financial updates.

    '''
    mail.HTMLBody = email_content
    try:
        mail.Attachments.Add(os.path.join(os.getcwd(), "Personal_Budget.xlsx"))
        mail.Send()        
        return '\nThe email has sent with success.'
    except:
        return '\nSorry, something went wrong.' 
        
print(send_email())
