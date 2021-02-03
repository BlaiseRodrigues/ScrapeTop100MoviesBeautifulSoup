from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = soup.find_all(name="h3", class_ = "title")

top_100 = []
for movie in movies:
    top_100.append(movie.getText())

print(top_100[-1])
top_100[-1] = "1) " + top_100[-1]
print(top_100[-1])

with open('top100Movies.txt', 'w') as file:
    for movie in top_100:
        file.write("{}\n".format(movie.encode("utf-8")))