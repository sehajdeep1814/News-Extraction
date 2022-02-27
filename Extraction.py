
#News- Extractioin

# Step 0: Importing packages

import requests

from bs4 import BeautifulSoup

url = "https://www.inshorts.com/en/read"

# Step 1: GET HTML using requests

r = requests.get(url)

content = r.content

# Step 2: Parsing HTML using BeautifulSoup

soup = BeautifulSoup(content, 'html.parser')

# Step 3:  HTML Tree traversal

all_news = soup.find_all('div', {'class': 'news-card z-depth-1'})

news_headlines = []
news_author = []
news_body = []
news_images = []
news_url = []
news_keyword = []
common_words = []

# Adding 3000 common words in English in the common_words list
with open("words.txt") as file:
    for words in file.readlines():
        common_words.append(words[:-1])


for news in all_news:

    headline = news.find('span', {'itemprop': 'headline'}).text.strip()
    news_headlines.append(headline)  # Headline

    news_author.append(
        news.find('span', {'class': 'author'}).text.strip())  # Author

    body = news.find('div', {'itemprop': 'articleBody'}).text.strip()
    news_body.append(body)  # Body

    anchor = news.find('a', {'class': 'source'})
    if(anchor != None):
        news_url.append(anchor.get('href'))  # News Source
    else:
        news_url.append('')

    images = news.find('div', {'class': 'news-card-image'})
    news_images.append(images.get('style')[23:-3])  # Image url

    news_headlines_1 = headline.replace('.', '').replace(',', "").split(' ')

    news_body_1 = body.replace('.', ' ').replace(',', "").split(" ")

    max_occurance = []
    for i in news_headlines_1:
        # if i not in ['a', 'an', 'the', 'in', 'is', 'of', 'my', 'no', 'yes', 'on', 'to', 'for', 'it', 'after', 'I', "I'm", 'be', 'he', 'she', 'are', 'they', 'him', 'her']:
        if i not in common_words:
            max_occurance.append(news_body_1.count(i))
        else:
            max_occurance.append(0)

    news_keyword.append(news_headlines_1[max_occurance.index(
        max(max_occurance))])  # News Keyword


data = [news_headlines, news_author, news_body,
        news_url, news_images, news_keyword]
news_length = len(data[0])
