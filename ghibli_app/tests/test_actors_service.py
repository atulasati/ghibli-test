from django.test import SimpleTestCase
from ..actors_service import ActorsService


class TestPeopleService(SimpleTestCase):
    """
    This class tests the Movies Service Class functions
    """

    def test_get_people(self):
        """
        Tests that get_people returns a valid people object
        """
        people = ActorsService().fetch_actors_data()
        people_keys: set[str] = {'id', 'name',
                                 'gender', 'age',
                                 'eye_color', 'hair_color',
                                 'films', 'species', 'url'}
        self.assertEqual(people[0].keys(), people_keys)
