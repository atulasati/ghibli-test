from ..api_request import HTTPHelper
from django.test import SimpleTestCase

class TestHelperFunctions(SimpleTestCase):
    """
    This class tests the helper functions.
    """

    movies_api_url = "https://ghibli.rest/films"
    error_url_404 = "https://ghibli.rest/404"

    def test_check_error_response(self):
        """
        Tests if a wrong API returns an error status.
        """
        response = HTTPHelper.make_request(self.error_url_404)
        self.assertEqual(response.status_code, 404)

    def test_check_successful_call(self):
        """
        Tests if a page is found and returns a 200 status code.
        """
        response = HTTPHelper.make_request(self.movies_api_url)
        self.assertEqual(response.status_code, 200)
        response = HTTPHelper.make_request(self.movies_api_url + "?ghiblikey=ghiblivalue")
        json_data = response.json()
        movie_keys_set: set[str] = {
            'id', 'title', 'original_title', 'original_title_romanised', 'image', 'movie_banner', 
            'description', 'director', 'producer', 'release_date', 'running_time', 'rt_score', 
            'people', 'species', 'locations', 'vehicles', 'url'
        }
        self.assertEqual(json_data[0].keys(), movie_keys_set)

