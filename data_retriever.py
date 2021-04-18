from config import POSTS_URL, USERS_URL

import requests


class DataRetriever:

    def get_data_from_server(self, url):
        """
        Function sends request to server and if it is successful it returns
        received data as json. Otherwise it raises Request Exception.
        :param url: address to data resource
        :return: response data in json format
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise requests.exceptions.RequestException

    def get_posts(self):
        """
        Function gets posts from the server and returns them in a list.
        :return: list of post objects
        """
        posts = DataRetriever().get_data_from_server(POSTS_URL)
        return posts

    def get_users(self):
        """
        Function gets users from the server adn return them in a list.
        :return: list of user objects
        """
        users = DataRetriever().get_data_from_server(USERS_URL)
        return users
