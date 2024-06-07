import json
import requests
from .istorage import IStorage
from dotenv import load_dotenv
import os


class StorageJson(IStorage):
    """
    A class for managing movie data stored in a JSON file.

    Attributes:
        file_path (str): The path to the JSON file containing movie data.

    Methods:
        - load_movies(): Loads movie data from the JSON file.
        - save_movies(movies): Saves updated movie data to the JSON file.
        - list_movies(): Returns a dictionary of movie information.
        - add_movie(): Adds a new movie to the database.
        - delete_movie(): Deletes a movie from the database.
        - update_movie(): Updates the rating of an existing movie.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageJson instance with the provided file path.

        Args:
            file_path (str): Path to the JSON file.
        """
        self.file_path = file_path

    def load_movies(self):
        """
        Loads movie data from the JSON file and returns it as a list of
        dictionaries.

        Returns:
            list: List of movie dictionaries.
        """
        try:
            with (open(self.file_path, "r", encoding="utf-8") as
                  movie_obj):
                return json.load(movie_obj)
        except FileNotFoundError:
            print("Error: The storage file was not found.")

    def save_movies(self, movies):
        """
        Saves the updated movie data to the JSON file.

        Args:
            movies (list): List of movie dictionaries.
        """
        try:
            with open(self.file_path, "w") as movie_obj:
                json.dump(movies, movie_obj, indent=4)
        except FileNotFoundError:
            print("Error: File was not found.")

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON
        file and returns the data.

        For example, the function may return:
        {
        "Titanic": {
            "rating": 9,
            "year": 1999
        },
        "..." {
            ...
        },
        }
        """
        movies_list = self.load_movies()
        if not movies_list:
            print("No movies found")
            return
        print()
        print(f"{len(movies_list)} movies in total")
        for movie in movies_list:
            print(f"{movie["title"]}, ({movie['year']}): {movie['rating']}")
        return movies_list

    def add_movie(self):  # title, year, rating, poster
        """
        Adds a movie to the movies' database.

        Retrieves additional movie information (year, rating, and poster) from
        the OMDB API.
        Appends the movie data to the list and saves it.
        """

        while True:
            title = input("Enter new movie name: ").strip()
            if title:
                break
            print("Error: Movie name cannot be empty.")

        movies_list = self.load_movies()

        if not movies_list:
            print("No movies found")
            return

        for movie in movies_list:
            if movie["title"].lower() == title.lower():
                print(f"Movie '{title}' already exists!")
                return

        try:
            load_dotenv()
            api_key = os.getenv("API_KEY")
            url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
            response = requests.get(url, timeout=5)
            data = response.json()
            print(f"API response: {data}")
        except ConnectionError as connection_error:
            print(connection_error)
            return

        movies_list.append({"title": data["Title"], "year": data["Year"],
                            "rating": data["imdbRating"],
                            "poster": data["Poster"], })
        self.save_movies(movies_list)
        print(f"Movie '{title}' successfully added")

    def delete_movie(self):  # title
        """
        Deletes a movie from the movies' database.

        Removes the specified movie (if found) and saves the updated list.
        """
        while True:
            title = input("Enter new movie name: ").strip()
            if title:
                break
            print("Error: Movie name cannot be empty.")

        movies_list = self.load_movies()

        if not movies_list:
            print("No movies found")
            return

        for movie in movies_list:
            if movie["title"].lower() == title.lower():
                movies_list.remove(movie)
                self.save_movies(movies_list)
                print(f"Movie {title} successfully deleted")
                return
        print(f"Movie {title} doesn't exist!")

    def update_movie(self):  # title, rating
        """
        Updates a movie's rating in the movies' database.

        Updates the rating for the specified movie (if found) and saves the
        updated list.
        """
        while True:
            title = input("Enter new movie name: ").strip()
            if title:
                break
            print("Error: Movie name cannot be empty.")

        movies_list = self.load_movies()

        if not movies_list:
            print("No movies found")
            return

        for movie in movies_list:
            if movie["title"].lower() == title.lower():
                while True:
                    rating = input("Enter new movie rating: ")
                    if rating.isdigit():
                        break
                    print("Error: Rating must be a integer.")
                movie["rating"] = float(rating)
                self.save_movies(movies_list)
                print(f"Movie {title} successfully updated")
                return
        print(f"Movie {title} doesn't exist!")
