from django.test import SimpleTestCase
from ..movies_service import MoviesService


class TestMoviesService(SimpleTestCase):
    """
    This class tests the Movies Service Class functions
    """

    def setUp(self):
        self.movies = MoviesService().get_movies()

    def test_get_movies(self):
        """
        Tests that get_movies returns a valid Movie object
        """
        movie_keys: set[str] = {'id', 'title', 'original_title', 
                                'original_title_romanised', 'image', 
                                'movie_banner', 'description', 'director',
                                'producer', 'release_date', 'running_time',
                                'rt_score', 'people', 'species', 'locations', 
                                'vehicles', 'url'}
        
        self.assertEqual(self.movies[0].keys(), movie_keys)

    def test_map_people_to_movies(self):
        """
        Tests that map_people_to_movies returns a valid Movie object
        with a valid people object in it
        """
        movies = MoviesService().get_movies_actors()
        movie_keys: set[str] = {'id', 'title', 'original_title', 'original_title_romanised', 'image', 'movie_banner', 'description', 'director', 'producer', 'release_date', 'running_time', 'rt_score', 'people', 'species', 'locations', 'vehicles', 'url', 'actors'}
        people_keys: set[str] = {'id', 'name',
                                 'gender', 'age',
                                 'eye_color', 'hair_color',
                                 'films', 'species', 'url'}
        people_object_is_valid: bool = False
        self.assertEqual(movies[0].keys(), movie_keys)

        for movie in movies:
            if len(movie['actors']) > 0:
                people_object_is_valid = True
                self.assertEqual(movie['actors'][0].keys(), people_keys)
                break

        self.assertEqual(people_object_is_valid, True)
