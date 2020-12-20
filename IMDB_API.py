from imdb import IMDb
import os

ia = IMDb()

top_250 = ia.get_top250_movies()

movies = {}
persons = {}

for mov in top_250:
    movieObj = ia.get_movie(mov.movieID)
    movies.update({mov.movieID: movieObj})
    for person in movieObj['cast']:
        person.update({person.personID : ia.get_person(person.personID)})

for movie in movies:
    print("test")
    print("test" + movies[movie].data['original title'])