class PostsOps:

    def match_posts_users(self, posts, users):
        """
        Function assigns post ids to each user.
        :param posts: list of posts
        :param users: lists of users
        :return: list of users including list of post ids for each user.
        """
        for u in users:
            u['posts_ids'] = [p['id'] for p in posts if p['userId'] == u['id']]
        return users

    def count_users_posts(self, u_posts):
        """
        :param u_posts: list of users including their post ids
        :return: list of strings saying how many posts have been written by
                 each user.
        """
        posts_counts = []
        for u in u_posts:
            s = f'{u["username"]} napisał(a) {len(u["posts_ids"])} postów'
            posts_counts.append(s)
        return posts_counts

    def check_title_uniqueness(self, posts):
        """
        Functions counts how many times each title appears in data and returns
        list of titles that appear more than once.
        :param posts: list of posts
        :return: list of title strings or single string
        """
        posts_titles = [p['title'] for p in posts]
        not_unique = []
        for t in posts_titles:
            if posts_titles.count(t) > 1 and t not in not_unique:
                not_unique.append(t)
        if len(not_unique) == 0:
            return 'There are no multiplied titles.'
        else:
            return not_unique
