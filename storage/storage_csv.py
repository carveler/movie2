from .istorage import IStorage
import csv


class StorageCsv(IStorage):
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
            with (open(self.file_path, "r", encoding="utf-8",
                       newline="") as csvfile):
                reader = csv.DictReader(csvfile)
                return list(reader)
        except FileNotFoundError:
            print(f"Error: The storage file was not found.: {self.file_path}")

    def save_movies(self, movies):
        """
        Saves the updated movie data to the JSON file.

        Args:
            movies (list): List of movie dictionaries.
        """
        try:
            with (open(self.file_path, 'w', encoding="utf-8",
                       newline='') as csvfile):
                fieldnames = ['title', 'year', 'rating', 'poster']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for movie in movies:
                    writer.writerow(movie)
        except FileNotFoundError:
            print(f"Error: File was not found.: {self.file_path}")

    def list_movies(self):
        """
        print list of movies         
        Returns:
            list: List of movie dictionaries or None if the file is not found.
        """
        movies_list = self.load_movies()
        if movies_list is None or not movies_list:
            print(f"Movies data does not exist or empty!")
            return None
        print()
        print(f"{len(movies_list)} movies in total")
        for movie in movies_list:
            print(f"{movie["title"]}, ({movie['year']}): {movie['rating']}")
        return movies_list

    def add_movie(self, title="", year="", rating="", poster=""):
        """
        Adds a movie to the movies' database.

        Args:
            title (str): Title of the movie to add.
            year (int): Year the movie was released.
            rating (float): Rating of the movie.
            poster (str): URL of the movie poster.
        """
        movies_list = self.load_movies()

        if movies_list is None or not movies_list:
            print(f"Movies data does not exist or empty!")
            return

        for movie in movies_list:
            if movie["title"].lower() == title.lower():
                print(f"Movie '{title}' already exists!")
                return

        try:
            movies_list.append({"title": title, "year": year, "rating": rating,
                                "poster": poster, })
            self.save_movies(movies_list)
            print(f"Movie '{title}' successfully added")
        except Exception as e:
            print(f"An error occurred while adding the movie: {e}")

    def delete_movie(self, title): 
        """
        Removes the specified movie (if found) and saves the updated list.      
        Args:
            title (str): Title of the movie to delete.
        """
        movies_list = self.load_movies()

        if movies_list is None or not movies_list:
            print(f"Movies data does not exist or empty!")
            return

        for movie in movies_list:
            if movie["title"].lower() == title.lower():
                try:
                    movies_list.remove(movie)
                    self.save_movies(movies_list)
                    print(f"Movie {title} successfully deleted")
                except Exception as e:
                    print(
                        f"Error: Movie deleted but failed to save changes! ("
                        f"{e})")
                return

        print(f"Movie {title} doesn't exist!")

    def update_movie(self, title, rating): 
        """
        Updates a movie's rating in the movies' database.

        Updates the rating for the specified movie (if found) and saves the
        updated list.

        Args:
            title (str): Title of the movie to update.
            rating (float): The new rating for the movie.
        """

        movies_list = self.load_movies()

        if movies_list is None or not movies_list:
            print(f"Movies data does not exist or empty!")
            return

        for movie in movies_list:
            if movie["title"].lower() == title.lower():
                movie["rating"] = float(rating)
                self.save_movies(movies_list)
                print(f"Movie {title} successfully updated")
                return
        print(f"Movie {title} doesn't exist!")
