from lib.album import Album

"""
Constructs with title, release_year and artist_id:
"""

def test_constructs_with_title_release_year_artist_id():
    album = Album('Hackers', 1995, 1)
    assert album.title == 'Hackers'
    assert album.release_year == 1995
    assert album.artist_id == 1