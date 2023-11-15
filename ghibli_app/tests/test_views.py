from django.test import SimpleTestCase
from django.urls import reverse
from django.core.cache import cache
from ..movies_service import MoviesService
from ..views import MovieListView
from django.test import  RequestFactory
from django.test import TestCase, RequestFactory, override_settings
from django.core.cache import cache
from unittest.mock import patch


class TestViews(SimpleTestCase):
    """
    This class tests the index view
    """

    def setUp(self):
        self.factory = RequestFactory()

        self.response = self.client.get(reverse('index'))
        self.movies = MoviesService().get_movies_actors()

    def test_index_page(self):
        """
        Tests the html page used for the associated url
        Tests the page contains the word Movies
        """
        self.assertTemplateUsed(self.response, 'movies/error.html')

    def test_valid_ghibli_key(self):
        # Prepare a GET request with valid ghiblikey
        request = self.factory.get('/movies/', {'ghiblikey': 'ghiblivalue', 'format' : 'json'})
        response = MovieListView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertIn('movies_actors_list', response.data)

    def test_invalid_ghibli_key(self):
        # Prepare a GET request with an invalid ghiblikey
        request = self.factory.get('/movies/', {'ghiblikey': 'invalidkey', 'format' : 'json'})
        response = MovieListView.as_view()(request)

        # Check if the response status code is 403
        self.assertEqual(response.status_code, 403)
        self.assertIn('error', response.data)
