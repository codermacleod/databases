from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository #all method
Return a list of Album objects reflecting the seed data:
"""

def test_all_method_returns_list_of_album_objects(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    album_repo = AlbumRepository(db_connection) # Create a new AlbumRepository
    albums = album_repo.all()
    assert albums == [
    Album('Doolittle', 1989, 1),
    Album('Surfer Rosa', 1988, 1),
    Album('Waterloo', 1974, 2),
    Album('Super Trouper', 1980, 2),
    Album('Bossanova', 1990, 1),
    Album('Lover', 2019, 3),
    Album('Folklore', 2020, 3),
    Album('I Put a Spell on You', 1965, 4),
    Album('Baltimore', 1978, 4),
    Album('Here Comes the Sun', 1971, 4),
    Album('Fodder on My Wings', 1982, 4),
    Album('Ring Ring', 1973, 2),
    ]

"""
When we call AlbumRepository #find method
Print the album data which has an id of 1:
"""
def test_find_method_prints_the_album_with_an_id_of_1(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    album_repo = AlbumRepository(db_connection) # Create a new AlbumRepository
    albums = album_repo.all()
    album_wanted = album_repo.find(1)
    assert album_wanted == Album('Doolittle', 1989, 1)

"""
When create method is called we would want a new record of an Album to be created
"""
def test_creation_of_album_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    album_repo = AlbumRepository(db_connection) # Create a new AlbumRepository
    album = Album('New album', 2022, 3)
    assert album_repo.create(album) == None
    albums_list = album_repo.all()
    assert albums_list == [
    Album('Doolittle', 1989, 1),
    Album('Surfer Rosa', 1988, 1),
    Album('Waterloo', 1974, 2),
    Album('Super Trouper', 1980, 2),
    Album('Bossanova', 1990, 1),
    Album('Lover', 2019, 3),
    Album('Folklore', 2020, 3),
    Album('I Put a Spell on You', 1965, 4),
    Album('Baltimore', 1978, 4),
    Album('Here Comes the Sun', 1971, 4),
    Album('Fodder on My Wings', 1982, 4),
    Album('Ring Ring', 1973, 2),
    Album('New album', 2022, 3)
    ]

"""
When delete method is called should remove record of specified album
"""
def test_delete_method_removes_album(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    album_repo = AlbumRepository(db_connection) # Create a new AlbumRepository
    assert album_repo.delete('Baltimore') == None
    albums_list = album_repo.all()
    assert albums_list == [
    Album('Doolittle', 1989, 1),
    Album('Surfer Rosa', 1988, 1),
    Album('Waterloo', 1974, 2),
    Album('Super Trouper', 1980, 2),
    Album('Bossanova', 1990, 1),
    Album('Lover', 2019, 3),
    Album('Folklore', 2020, 3),
    Album('I Put a Spell on You', 1965, 4),
    Album('Here Comes the Sun', 1971, 4),
    Album('Fodder on My Wings', 1982, 4),
    Album('Ring Ring', 1973, 2),
    ]
