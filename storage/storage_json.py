import json

from .istorage import IStorage


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
        super().__init__(file_path)

    def load_movies(self):
        """
        Loads movie data from the JSON file and returns it as a list of
        dictionaries.

        Returns:
            list: List of movie dictionaries.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as movie_obj:
                return json.load(movie_obj)
        except FileNotFoundError:
            print("Error: The storage file was not found.")
        except json.JSONDecodeError as e:
            print(f"Error: An error occurred while parsing the JSON data: {e}")
            return

    def save_movies(self, movies):
        """
        Saves the updated movie data to the JSON file.

        Args:
            movies (list): List of movie dictionaries.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as movie_obj:
                json.dump(movies, movie_obj, indent=4)
        except FileNotFoundError:
            print("Error: File was not found.")
            return

    def add_movie(self, title="", year="", rating="", poster=""):
        """
        Adds a movie to the movies' database.

        Args:
            title (str): Title of the movie to add.
            year (int): Year the movie was released.
            rating (float): Rating of the movie.
            poster (str): URL of the movie poster.
        """
        super().add_movie(title, year, rating, poster)

    def delete_movie(self, title):
        """
        Removes the specified movie (if found) and saves the updated list.

        Args:
            title (str): Title of the movie to delete.
        """
        super().delete_movie(title)

    def update_movie(self, title, rating):
        """
        Updates a movie's rating in the movies' database.

        Updates the rating for the specified movie (if found) and saves the
        updated list.

        Args:
            title (str): Title of the movie to update.
            rating (float): The new rating for the movie.
        """

        super().update_movie(title, rating)
