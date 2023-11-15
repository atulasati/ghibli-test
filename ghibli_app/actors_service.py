from .api_request import HTTPHelper


class ActorsService:
    """
    A class containing functions related to managing actors data.
    """

    actors_api_url = "https://ghibli.rest/people"

    actors_data: list

    def fetch_actors_data(self) -> list:
        """
        Fetches actors data from a specified API endpoint.
        :return: A list containing the retrieved actors data.
        @rtype: list
        """
        self.actors_data = HTTPHelper.make_request(self.actors_api_url).json()
        return self.actors_data
