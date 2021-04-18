from operations.users_ops import UsersOps


def test_get_geo(t_user1, t_user2):
    """Test getting user geo coordinates from user's data"""
    geo1 = UsersOps().get_user_geo(t_user1)
    geo2 = UsersOps().get_user_geo(t_user2)
    assert geo1 == (1.58, -2.33)
    assert geo2 == (10.5, 20)


def test_calc_distance():
    """Test calculating distance between two users"""
    geo1 = (1, 2)
    geo2 = (5, 5)
    geo3 = (-2, -4)
    dist1 = UsersOps().calc_distance(geo1, geo2)
    dist2 = UsersOps().calc_distance(geo2, geo3)
    dist3 = UsersOps().calc_distance(geo1, geo3)
    assert dist1 == 5
    assert round(dist2, 2) == 11.40
    assert round(dist3, 2) == 6.71


def test_nearest_users(t_users):
    """Test finding the nearest neighbors for all users"""
    u = UsersOps().nearest_users(t_users)
    expected = ['For user User1 the nearest user is User3',
                'For user User2 the nearest user is User3',
                'For user User3 the nearest user is User1']
    assert u == expected
