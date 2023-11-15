from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ghibli_app.views import MovieListView

class TestUrls(SimpleTestCase):
    """
    This class tests the respective urls lead to their corresponding views functions
    """

    def test_index_url_is_resolved(self):
        """
        Tests that the index url does lead to index function
        """
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, MovieListView)
