import requests
import json

response = requests.get("https://jsonmock.hackerrank.com/api/tvseries")


def bestInGenre(genre: str) -> str:
    """
    Finds the highest-rated TV series in the given genre.
    Parameters:
    genre (str): The genre to search for (e.g., 'Action', 'Comedy', 'Drama')
    Returns:
    str: The name of the highest-rated show in the genre. If there is a tie,
    returns the alphabetically lower name. Returns the name as a string.
    Notes:
    - Ties are broken by alphabetical order of the show name
    - Genre matching is case-insensitive
    - Shows can have multiple genres (comma-separated)
    """
# Your implementation here

    #Cargamos el JSON para obtener la información de las series
    series = response.json()
    data = series["data"]

    #Empezamos a recorrer el JSON
    show_ranking = []
    show_per_genre = []
    for serie in data:
        if genre.lower() in serie["genre"].lower():
            show_per_genre.append(serie)
    show_ranking = sorted(show_per_genre,
                        key=lambda serie: serie["imdb_rating"],
                        reverse=True)
    for i in range(len(show_ranking)):   #Retornar en modo String
        print(show_ranking[i]['name']," - ", show_ranking[i]['imdb_rating'])  
    return "a"


genre = "drama"

print(bestInGenre(genre))