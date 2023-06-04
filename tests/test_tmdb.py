import pytest
import tmdb_client
from unittest.mock import Mock
from main import app


def test_get_single_movie(monkeypatch):
   movie_id = 603692
   mock_response = {'id': movie_id, 'title': 'John Wick: Chapter 4'}

   mock_get = Mock(return_value=Mock(json=Mock(return_value=mock_response)))
   monkeypatch.setattr("requests.get", mock_get)

   movie = tmdb_client.get_single_movie(movie_id)

   assert movie['id'] == movie_id
   assert movie['title'] == 'John Wick: Chapter 4'
   mock_get.assert_called_once_with(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_client.API_TOKEN}")


def test_get_movie_images(monkeypatch):
   movie_id = 603692
   mock_response = {
      'id': movie_id,
      'backdrops': [{'file_path': '/h8gHn0OzBoaefsYseUByqsmEDMY.jpg'}]
   }

   mock_get = Mock(return_value=Mock(json=Mock(return_value=mock_response)))
   monkeypatch.setattr("requests.get", mock_get)

   images = tmdb_client.get_movie_images(movie_id)

   assert images['id'] == movie_id
   assert len(images['backdrops']) == 1
   assert images['backdrops'][0]['file_path'] == '/h8gHn0OzBoaefsYseUByqsmEDMY.jpg'

def test_get_single_movie_cast(monkeypatch):
   movie_id = 603692
   mock_response = {
      'id': movie_id,
      'cast': [{'name': 'Keanu Reeves'}]
   }

   mock_get = Mock(return_value=Mock(json=Mock(return_value=mock_response)))
   monkeypatch.setattr("requests.get", mock_get)

   cast = tmdb_client.get_single_movie_cast(movie_id)

   assert cast['cast'][0]['name'] == 'Keanu Reeves'

def test_get_single_movie_invalid_data(monkeypatch):
   movie_id = 603692
   mock_response = {'id': movie_id, 'name': 'John Wick: Chapter 4'}  # Zmienione pole 'title' na 'name'

   mock_get = Mock(return_value=Mock(json=Mock(return_value=mock_response)))
   monkeypatch.setattr("requests.get", mock_get)

   with pytest.raises(KeyError, match="Invalid response format: missing 'title' field"):
       tmdb_client.get_single_movie(movie_id)


@pytest.mark.parametrize("list_type", ["popular", "top_rated", "now_playing", "upcoming"])
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.get_popular_movies", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)


