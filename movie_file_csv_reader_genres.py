import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReaderGenre:

    def __init__(self, file_name, genre_type):
        self.__file_name = file_name
        self.__genre_type = genre_type
        self.__dataset_of_movies = [Movie('ZZZZZZZZZZZZZZZZZZZZZZZZZZZ', 200000)]

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader_genre = csv.DictReader(csvfile)

            for row in movie_file_reader_genre:
                movie = row['Title']
                actors = sorted(row['Actors'].strip().split(','))
                for i in range(len(actors)):
                    actors[i] = actors[i].strip()
                director = row['Director']
                genres = sorted(row['Genre'].strip().split(','))
                for i in range(len(genres)):
                    genres[i] = genres[i].strip()
                year = int(row['Year'].strip())
                description = row['Description'].strip()
                runtime = int(row['Runtime (Minutes)'].strip())



                if self.__genre_type in genres:
                    the_movie = Movie(movie, year)

                    the_director = Director(director)
                    the_movie.director = the_director

                    for i in range(len(actors)):
                        the_actor = Actor(actors[i])
                        the_movie.actors.append(the_actor)

                    the_movie.description = description
                    the_movie.runtime_minutes = runtime
                    the_movie.director = the_director

                    for i in range(len(genres)):
                        the_genre = Genre(genres[i])
                        the_movie.genres.append(the_genre)

                    if the_movie not in self.__dataset_of_movies:
                        flag = True
                        for i in range(len(self.__dataset_of_movies)):
                            if the_movie < self.__dataset_of_movies[i]:
                                self.__dataset_of_movies.insert(i, the_movie)
                                flag = False
                                break
                        if flag:
                            self.__dataset_of_movies.insert(i, the_movie)



            self.__dataset_of_movies.pop()

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    def __repr__(self):
        return(self.__genre_type)



