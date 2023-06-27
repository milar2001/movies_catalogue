import requests

API_TOKEN = "b5a2506b12de524a5b5b0f696c42c757"

def get_popular_movies(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?api_key={API_TOKEN}"
    response = requests.get(endpoint)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(list_type="popular", how_many=0):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_TOKEN}"
    response = requests.get(endpoint)
    data = response.json()

    if 'title' not in data:
        raise KeyError("Invalid response format: missing 'title' field")

    return data

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_TOKEN}"
    response = requests.get(endpoint)
    return response.json()

def get_movie_cast(movie_id, how_many):
    data = get_single_movie_cast(movie_id)
    return data["cast"][:how_many]

def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?api_key={API_TOKEN}"
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={API_TOKEN}"
    response = requests.get(endpoint)
    return response.json()

def search(search_query):
    endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}&api_key={API_TOKEN}"
    response = requests.get(endpoint)
    data = response.json()
    if 'results' not in data:
        return []
    movies = data['results']
    return movies
