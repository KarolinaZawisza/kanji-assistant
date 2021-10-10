import csv

with open('n5_data.csv', encoding="utf8") as n5_data_file:
    n5_data = csv.reader(n5_data_file, delimiter=',')
    n5_list = [row for row in n5_data]

