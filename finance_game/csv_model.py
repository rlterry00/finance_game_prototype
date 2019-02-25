import csv
from flashcards import flashTerm 
csv_columns = ['Term','Definition']
dict_data = flashTerm.flashcards
csv_file = "finance_terms.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        data = [dict(zip(csv_columns, [k, v])) for k, v in dict_data.items()]
        writer.writerows(data)
except IOError:
    print("I/O error") 