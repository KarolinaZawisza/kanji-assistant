import csv
from kanji import Kanji
from index_utils import IndexUtils

index = IndexUtils()

with open('n5_data.csv', encoding="utf8") as n5_data_file:
    n5_data = csv.reader(n5_data_file, delimiter=',')
    n5_list = [row for row in n5_data]
    kanji = Kanji(n5_list[index.get_today_index() - 1][0],
                  n5_list[index.get_today_index() - 1][1],
                  n5_list[index.get_today_index() - 1][2])


index.update_index()