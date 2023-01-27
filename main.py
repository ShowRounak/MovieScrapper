from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

boxes = soup.find_all(class_ = "article-title-description__text")

movie_list = []
for box in boxes:
    #print(box.find(class_ = "title").getText())
    movie_list.append(box.find(class_ = "title").getText())

#print(movie_list)

with open("movies.txt", 'w', encoding='utf8') as f:
    for movie in movie_list[::-1]:
        f.write(movie)
        f.write('\n')



