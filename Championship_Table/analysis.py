import pandas as pd
from tabulate import tabulate
from championship_table import create_file_csv
create_file_csv()

def filter_data(category, ascending=False):

    # This function filter and sort the data based on the category passed.
    my_csv = pd.read_csv('championship_table.csv', encoding='latin-1')
    filter_result = my_csv.sort_values(by=[category], ascending=ascending)
    filter_result = filter_result[['Club',category]][:5].to_string(index=False)
    if ascending == False:
        return f'More {category}\n' + filter_result 
    else:
        return f'Less {category}\n' + filter_result 

print(tabulate([[filter_data('W'), filter_data('W', True)]]))
print(tabulate([[filter_data('L'), filter_data('L', True)]]))
print(tabulate([[filter_data('GF'), filter_data('GF', True)]]))
print(tabulate([[filter_data('GA'), filter_data('GA', True)]]))
print(tabulate([[filter_data('Shoots on Target'), filter_data('Shoots on Target', True)]]))
print(tabulate([[filter_data('Won Defenses'), filter_data('Won Defenses', True)]]))