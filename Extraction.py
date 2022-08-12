
#News- Extraction

# Step 0: Importing packages

import requests

from bs4 import BeautifulSoup

categories = {
    "all News": "",
    "india": "national",
    "business": "business",
    "sports": "sports",
    "world": "world",
    "politics": "politics",
    "technology": "technology",
    "entertainment": "entertainment",
    "science": "science",
}

common_words = []
# Adding 3000 common words in English in the common_words list
with open("words.txt") as file:
    for words in file.readlines():
        common_words.append(words[:-1])

class News:
    def __init__(self, tag, attribute):
        self.items = []
        self.tag = tag
        self.attribute = attribute

    def add(self, news):
        for single_news in news:
            self.items.append(single_news.find(self.tag, self.attribute).text.strip())

    def addURLs(self, news):
        for single_news in news:
            anchor = single_news.find(self.tag, self.attribute)
            if (anchor == None):
                self.items.append('')
            else:
                self.items.append(anchor.get('href'))

    def addImages(self, news):
        for single_news in news:
            image = single_news.find(self.tag, self.attribute)
            self.items.append(image.get('style')[23:-3])

url = ""
news_categories = {}
for label, link in categories.items():
    url = f"https://www.inshorts.com/en/read/{link}"

    # Step 1: GET HTML using requests

    r = requests.get(url)

    content = r.content

    # Step 2: Parsing HTML using BeautifulSoup

    soup = BeautifulSoup(content, 'html.parser')

    # Step 3:  HTML Tree traversal

    all_news = soup.find_all('div', {'class': 'news-card z-depth-1'})




    headlines = News('span', {'itemprop': 'headline'})
    headlines.add(all_news)

    authors = News('span', {'class': 'author'})
    authors.add(all_news)

    bodies = News('div', {'itemprop': 'articleBody'})
    bodies.add(all_news)

    urls = News('a', {'class': 'source'})
    urls.addURLs(all_news)

    images = News('div', {'class': 'news-card-image'})
    images.addImages(all_news)

    news_keyword = []



    for i in range(len(headlines.items)):
        max_occurrence = []
        headlines_words = headlines.items[i].replace('.', '').replace(',', '').split(' ')
        bodies_words = bodies.items[i].replace('.', '').replace(',', '').split(' ')

        for word in headlines_words:
            if word not in common_words:
                max_occurrence.append(bodies.items.count(word))
            else:
                max_occurrence.append(0)

        news_keyword.append(headlines_words[max_occurrence.index(max(max_occurrence))])

    data = [headlines.items, authors.items, bodies.items,
            urls.items, images.items, news_keyword]
    news_categories[link] = data;
