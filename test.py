from flask import Flask, render_template, url_for
from Extraction import data, news_length

app = Flask('__name__')


@app.route('/')
def homepage():
    return render_template('homepage.html', data=data, news_length=news_length)


if __name__ == '__main__':
    app.run(debug=True)
