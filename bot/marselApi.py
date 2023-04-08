import requests
import random


class User:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def check_age(self, anime):
        anime_age_rating = anime["data"]["attributes"]["ageRating"]
        print(anime_age_rating)


# https://kitsu.io/api/edge/anime?filter[text]=tokio

def random_anime():
    maximum = 13000
    rand = random.randint(1, maximum)
    link = "https://kitsu.io/api/edge/anime/"  # get-запрос на определенный api
    link += str(rand)
    response = requests.get(link)
    if response.ok:
        return response.json()
    else:
        return random_anime()


anime = random_anime()
nikita = User("Никита", "male", 12)
nikita.check_age(anime)
