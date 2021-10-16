class IndexUtils:

    def __init__(self):
        self.index = self.get_today_index()

    @staticmethod
    def get_today_index() -> int:
        with open('kanji_data.txt', 'r') as kanji_data:
            return int(kanji_data.readline())

    def update_index(self):
        with open('kanji_data.txt', 'w') as kanji_data:
            kanji_data.write(f'{self.index + 1}')