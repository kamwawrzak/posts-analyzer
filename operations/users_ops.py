import math
from operator import itemgetter


class UsersOps:

    def get_user_geo(self, user):
        """
        Function gets user's coordinates and returns them in tuple.
        :param user: single user object
        :return: tuple showing user's geo coordinates
        """
        user_lat = float(user['address']['geo']['lat'])
        user_long = float(user['address']['geo']['lng'])
        return user_lat, user_long

    def calc_distance(self, geo1, geo2):
        """
        Function accepts two points and calculates distance between them basing
        on Pythagorean theorem
        :param geo1: tuple of first user coordinates
        :param geo2: tuple of second user coordinates
        :return: float representing distance between users
        """
        dist = math.sqrt((geo1[0] - geo2[0])**2 + (geo1[1] - geo2[1])**2)
        return dist

    def nearest_users(self, users):
        """
        Function calculates distances between all users and finds the nearest
        neighbor for each of them.
        :param users: list of users
        :return: list of  strings showing the nearest neighbor for each user
        """
        nearest_users = []
        for u in users:
            u_geo = UsersOps().get_user_geo(u)
            distances = []
            for j in users:
                if j != u:
                    j_geo = UsersOps().get_user_geo(j)
                    d = UsersOps().calc_distance(u_geo, j_geo)
                    distances.append({'username': j['username'],
                                      'distance': d})
            sorted_dist = sorted(distances, key=itemgetter('distance'))
            nearest_name = sorted_dist[0]['username']
            s = f'For user {u["username"]} the nearest user is {nearest_name}'
            nearest_users.append(s)
        return nearest_users
