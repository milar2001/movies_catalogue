import tmdb_client
from unittest.mock import Mock


def test_get_single_movie(monkeypatch):
   # Przygotowanie danych testowych
   movie_id = 603692
   mock_response = {'id': movie_id, 'title': 'John Wick: Chapter 4'}

   # Symulowanie żądania API za pomocą Mock() i monkeypatch
   mock_get = Mock(return_value=Mock(json=Mock(return_value=mock_response)))
   monkeypatch.setattr("requests.get", mock_get)

   # Wywołanie funkcji testowanej
   movie = tmdb_client.get_single_movie(movie_id)

   # Sprawdzenie wyników
   assert movie['id'] == movie_id
   assert movie['title'] == 'John Wick: Chapter 4'


def test_get_movie_images(monkeypatch):
   # Przygotowanie danych testowych
   movie_id = 603692
   mock_response = {
      'id': movie_id,
      'backdrops': [{'file_path': '/h8gHn0OzBoaefsYseUByqsmEDMY.jpg'}]
   }

   # Symulowanie żądania API za pomocą Mock() i monkeypatch
   mock_get = Mock(return_value=Mock(json=Mock(return_value=mock_response)))
   monkeypatch.setattr("requests.get", mock_get)

   # Wywołanie funkcji testowanej
   images = tmdb_client.get_movie_images(movie_id)

   # Sprawdzenie wyników
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