import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# text şeklinde site verisi
response = requests.get(URL)
web_page = response.text

# html parse işlemi

soup = BeautifulSoup(web_page, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movies = [each.getText() for each in movie_tags]

# elemanları ters çevir
# kısa versiyonu//  movies[::-1]
ordered_movies = []
len_l = len(movies)-1
for i in range(len_l):
    ordered_movies.append(movies[len_l-i])
print(ordered_movies)
# listeyi txt ye yazma
# file.write() + file.write("\n") da olur yada file.writelines() da
with open("movies.txt", "w") as file:
    for movie in ordered_movies:
        file.write(movie)
        file.write("\n")



