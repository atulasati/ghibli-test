from .api_request import HTTPHelper
from .actors_service import ActorsService


class MoviesService:
    """
    Class Containing Movie related functions
    """
    movies_url = "https://ghibli.rest/films"
    actors: list
    movies: list
    actors_service: None

    def __init__(self):
        """
        Class constructor
        """
        self.actors_service = ActorsService()

    def get_movies(self) -> list:
        """
        Get movies through an api call
        @return: list
        @rtype: list
        """
        self.movies = HTTPHelper.make_request(self.movies_url).json()
        return self.movies

    def get_movies_actors(self) -> list:
        """
        Return movies with their actors.
        For each movie add its related actors
        :return: list of movies with their actors
        @rtype: list
        """
        movies = self.get_movies()
        actors = self.actors_service.fetch_actors_data()
        movie_actors = {}
        for person in actors:
            for movie in person['films']:
                movie_id = movie.rsplit('/', 1)[-1]
                if movie_id in movie_actors:
                    movie_actors[movie_id].append(person)
                else:
                    movie_actors[movie_id] = [person]
    
        for movie in movies:
            movie_id = "films?id="+movie.get('id')
            if movie_id in movie_actors:
                movie['actors'] = movie_actors[movie_id]
            else:
                movie['actors'] = []

            if movie.get("people"):
                del movie["people"]

        return movies
