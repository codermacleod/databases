from lib.user_repository import UserRepository
from lib.user import User

'''
When we call UserRepository#all
We get a list of User objects reflecting the seed data
'''

def test_get_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    users = repository.all()

    assert users == [
        User('Steve Jobs', 77, 'sj@apple.com'),
        User('Bill Gates', 88, 'bg@microsoft.com'),
        User('Joe Bloggs', 99, 'jb@chill.com'),
        User('Jean Claude Van Damme', 111, 'jcvd@stillkicking.com'),
    ]

'''
When we call UserRepository#find method
We retrieve a record from the UserRepository:
'''
def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.find(2)
    assert result == User('Bill Gates', 88, 'bg@microsoft.com')

'''
When we call UserRepository#create method
We create a record in the UserRepository:
'''
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User('Yoyo', 107, 'yy@yoyo.com')
    repository.create(user)
    assert user.create(user) == User('Yoyo', 107, 'yy@yoyo.com')
    assert repository.all() == [
        User('Steve Jobs', 77, 'sj@apple.com'),
        User('Bill Gates', 88, 'bg@microsoft.com'),
        User('Joe Bloggs', 99, 'jb@chill.com'),
        User('Jean Claude Van Damme', 111, 'jcvd@stillkicking.com'),
        User('Yoyo', 107, 'yy@yoyo.com'),

    ]