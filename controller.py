from data_retriever import DataRetriever
from operations.posts_ops import PostsOps
from operations.users_ops import UsersOps


class Controller:

    def control_loop(self):
        """
        The function gets posts and users from server and match them.
        Next it prints available options and read input from user.
        Accordingly with chosen option it performs suitable action.
        """
        posts = DataRetriever().get_posts()
        users = DataRetriever().get_users()
        u_posts = PostsOps().match_posts_users(posts, users)
        option = -1
        while option != 5:
            s = "Available options: \n1 - print users with assigned posts \n"\
                "2 - print multiplied titles \n3 - print amount of users' " \
                "posts \n4 - print nearest neighbors for users\n5 - exit\n"
            option = input(s)
            if option == '1':
                print(u_posts)
            elif option == '2':
                print(f'Multiplied titles: '
                      f'{PostsOps().check_title_uniqueness(posts)}')
            elif option == '3':
                print(PostsOps().count_users_posts(u_posts))
            elif option == '4':
                print(UsersOps().nearest_users(users))
            elif option == '5':
                print('Program ended.')
                break
            else:
                print(f'There is no such option as {option}.')
