from flask import Flask, render_template
import main
from index_utils import IndexUtils

app = Flask(__name__)

index = IndexUtils()
expression = main.get_kanji_list()[index.get_today_index()].expression
meaning = main.get_kanji_list()[index.get_today_index()].meaning
reading = main.get_kanji_list()[index.get_today_index()].reading

@app.route('/')
def main_page():
    return render_template('index.html', expression=expression, meaning=meaning, reading=reading)


if __name__ == '__main__':
    app.run(debug=True)