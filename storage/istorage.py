from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Abstract class for storage
    """

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def load_movies(self):
        pass

    @abstractmethod
    def save_movies(self, movies):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
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


    @abstractmethod
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
                    print(f"Error: Movie deleted but failed to save changes! (" f"{e})")
                return

        print(f"Movie {title} doesn't exist!")       

    @abstractmethod
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
                movie["rating"] = str(float(rating))
                self.save_movies(movies_list)
                print(f"Movie {title} successfully updated")
                return
        print(f"Movie {title} doesn't exist!")