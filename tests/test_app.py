from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post("/albums", data={
        'title': 'In Ear Park',
        'release_year': '2008',
        'artist_id': '1'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') ==  (
        'Album(1, The Cold Nose, 2008, 1)\n'
        'Album(2, In Ear Park, 2008, 1)'
    )


def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post("/albums")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You need to submit a title, release_year and artist_id'
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Album(1, The Cold Nose, 2008, 1)'


################



def test_post_artist(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post("/artists", data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') ==  (
        'Artist(1, Pixies, Rock)\n'
        'Artist(2, ABBA, Pop)\n'
        'Artist(3, Taylor Swift, Pop)\n'
        'Artist(4, Nina Simone, Jazz)\n'
        'Artist(5, Wild nothing, Indie)'
    )


def test_post_artist_with_no_data(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post("/artists")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You need to submit a name and genre'
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
        'Artist(1, Pixies, Rock)\n'
        'Artist(2, ABBA, Pop)\n'
        'Artist(3, Taylor Swift, Pop)\n'
        'Artist(4, Nina Simone, Jazz)'
    )