# themovie.org film API
# e8a9d5f82d78ca210c8076d648685c12
# https://api.themoviedb.org/3/movie/550?api_key=e8a9d5f82d78ca210c8076d648685c12

import requests

class TheMovieDb:
    def __init__(self) -> None:
        self.apiUrl = "https://api.themoviedb.org/3"
        self.apiKey = "e8a9d5f82d78ca210c8076d648685c12"

    def getPopulars(self):
        response = requests.get(f"{self.apiUrl}/movie/popular?api_key={self.apiKey}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword):
        response = requests.get(f"{self.apiUrl}/search/keyword?api_key={self.apiKey}&query={keyword}&page=1")
        return response.json()

movieApi = TheMovieDb()

while True:
    secim = int(input("1 - Popüler Filmler\n2 - Film Ara\n3 - Çıkış\n"))
    match secim:
        case 1:
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"].center(50,"*"))
        case 2 :
            keyword = input("Aranacak film adını giriniz\n")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie["name"].center(50,"*"))
        case 3:
            break
        case _:
            print("Hatalı giriş")
