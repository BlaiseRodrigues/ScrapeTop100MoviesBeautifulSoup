from bs4 import BeautifulSoup
import requests
import numpy as np

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)

    article_link = article.get("href")
    article_links.append(article_link)

article_votes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_votes)

highest_votes_index = np.argmax(article_votes)

print(f'Article with Highest up votes is "{article_texts[highest_votes_index]}" with "{article_votes[highest_votes_index]}"')



