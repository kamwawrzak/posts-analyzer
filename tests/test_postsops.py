from operations.posts_ops import PostsOps


def test_match_posts(t_posts, t_users):
    """Test matching posts with users"""
    u = PostsOps().match_posts_users(t_posts, t_users)
    assert u[0]['posts_ids'][0] == 1
    assert u[0]['posts_ids'][1] == 2
    assert u[1]['posts_ids'][0] == 3


def test_count_users_posts(users_with_posts):
    """Test counting users' posts"""
    u = PostsOps().count_users_posts(users_with_posts)
    u1_expected = 'User1 napisał(a) 0 postów'
    u2_expected = 'User2 napisał(a) 3 postów'
    assert u[0] == u1_expected
    assert u[1] == u2_expected


def test_check_title_uniqueness(t_posts, t_posts2):
    """Test checking multiplied titles of posts"""
    titles1 = PostsOps().check_title_uniqueness(t_posts)
    titles2 = PostsOps().check_title_uniqueness(t_posts2)
    assert titles1 == ['Example title 2']
    assert titles2 == 'There are no multiplied titles.'
