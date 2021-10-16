import csv
from kanji import Kanji

def get_kanji_list():
    with open('n5_data.csv', encoding="utf8") as n5_data_file:
        n5_data = csv.reader(n5_data_file, delimiter=',')
        n5_list = [row for row in n5_data]
        kanji_list = []
        for data_set in range(0, len(n5_list)):
            kanji = Kanji(n5_list[data_set][0],
                          n5_list[data_set][1],
                          n5_list[data_set][2])
            kanji_list.append(kanji)
        return kanji_list
