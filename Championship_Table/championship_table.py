import csv, pandas as pd
from web_search import*
from datetime import date

def create_file_csv():
   
    # This function creates a csv file based on the information extracted.
    try:
        with open('championship_table.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ['Club', 'Pts', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Shoots on Target', 'Won Defenses', 'P. - Pts']
            writer.writerow(field)
            soup = web_search()
            result_dict = extract_search_championship_table(soup)
            teams, scores = list(result_dict.keys()), list(result_dict.values())
            shoots, defenses = extract_search_shoot_defense(soup)

            for x in range(0, 20):
                projection_pts = int(scores[x][7])/(int(scores[x][0]) * 3) * (38 - int(scores[x][0])) * 3 + int(scores[x][7])
                writer.writerow([teams[x], scores[x][7], scores[x][0], scores[x][1], scores[x][2], scores[x][3], scores[x][4], scores[x][5], scores[x][6], shoots[x], defenses[x], int(projection_pts)])
    except:
        return 'Something went wrong. Try again.'

def create_file_excel():
    
    # This function converts the csv file to excel.
    create_file_csv()
    today = date.today().strftime("%d-%m")
    df = pd.read_csv('championship_table.csv', encoding='latin-1')
    writer = pd.ExcelWriter(f'championship table {today}.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Table', startrow=1, header=False, index=False)
    workbook = writer.book
    worksheet = writer.sheets['Table']
    (max_row, max_col) = df.shape
    column_settings = []
    for header in df.columns: 
        column_settings.append({'header': header})  
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
    worksheet.set_column(0, max_col - 1, 12)
    writer.close()
    return 'File created with success.'
 
if __name__ == "__main__":
    
    print(create_file_excel())