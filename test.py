from flask import Flask, render_template, url_for
from Extraction import data, news_categories, categories

app = Flask('__name__')


# for link, data in news_categories.items():
#     url = f"/{link}"
#     @app.route(url)
#     def render_page():
#         return render_template('homepage.html', data=data, news_length=len(data[0]))

@app.route('/')
def allNews():
    data = news_categories[""]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route('/national')
def national():
    data = news_categories["national"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route('/business')
def business():
    data = news_categories["business"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route("/sports")
def sports():
    data = news_categories["sports"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route("/world")
def world():
    data = news_categories["world"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route("/politics")
def politics():
    data = news_categories["politics"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route("/technology")
def technology():
    data = news_categories["technology"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route("/entertainment")
def entertainment():
    data = news_categories["entertainment"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)

@app.route("/science")
def science():
    data = news_categories["science"]
    return render_template('homepage.html', data=data, news_length=len(data[0]), categories=categories, news_categories=news_categories)


if __name__ == '__main__':
    app.run(debug=True)
