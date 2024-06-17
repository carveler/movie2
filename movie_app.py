import random
import statistics
import os

APP_TITLE = "Movie App"

# Get the absolute path to the directory where movie_app.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths relative to the base_dir
TEMPLATE_HTML = os.path.join(base_dir, 'templates', 'index_template.html')
OUTPUT_HTML = os.path.join(base_dir, 'templates', 'index.html')


class MovieApp:
    def __init__(self, storage):
        """
        Initialize the MovieApp with a storage backend.

        Args:
            storage (IStorage): The storage backend to use for movie data.
        """
        self._storage = storage

    def _command_list_movies(self):
        """
        Load and return the list of movies from the storage.

        Returns:
            list: A list of movie dictionaries.
        """
        try:
            movies = self._storage.load_movies()
            return movies
        except FileNotFoundError:
            print("Error: The storage file was not found.")

    def _command_movie_stats(self):
        """
        Prints statistics about the movies in the database, including
        average rating, median rating,
        best and worst-rated movies.
        """
        movies_list = self._command_list_movies()
        if not movies_list:
            print("No movies found.")
            return

        ratings = sorted([float(movie["rating"]) for movie in movies_list])
        length_ratings = len(ratings)
        best_rating = max(ratings)
        worst_rating = min(ratings)

        average = sum(ratings) / length_ratings

        median = statistics.median(ratings)

        best_titles = [movie["title"] + ", " + movie["rating"] for movie in
                       movies_list if float(movie["rating"]) == best_rating]
        worst_titles = [movie["title"] + ", " + movie["rating"] for movie in
                        movies_list if float(movie["rating"]) == worst_rating]

        print(f"Average rating: {average:.1f}")
        print(f"Median rating:  {median:.1f}")
        print("Best movie: " + ", ".join(best_titles))
        print("Worst movie: " + ", ".join(worst_titles))

    def _generate_website(self):
        """
        Write the movie data to an HTML file based on a template.
        """
        content = ""
        movies_list = self._storage.load_movies()
        if not movies_list:
            print("No movies found.")
            return
        for movie_data in movies_list:
            content += '<li>'
            movie_grid = (f'<div class="movie">'
                          f'<img class="movie-poster" '
                          f'src={movie_data['poster']} title="" />'
                          f'<div class="movie-title">'
                          f'{movie_data['title']}</div>'
                          f'<div class="movie-year">{movie_data['year']}</div>'
                          '</div>')
            content += movie_grid
            content += '</li>'
        try:
            with open(TEMPLATE_HTML, "r", encoding="utf-8") as handle:
                template = handle.read()
            with open(OUTPUT_HTML, "w", encoding="utf-8") as handle:
                replaced_template = template.replace("__TEMPLATE_TITLE__",
                                                     APP_TITLE)
                replaced_template = replaced_template.replace(
                    "__TEMPLATE_MOVIE_GRID__", content)
                handle.write(replaced_template)
            print("Website was generated successfully.")
        except FileNotFoundError:
            print(f"The template file {TEMPLATE_HTML} does not exist.")
        except Exception as gen_error:
            print(f"An error occurred: {gen_error}")

    @staticmethod
    def _print_movies(movies_list):
        """
        Prints the list of movies.

        Args:
            movies_list (list): List of movie dictionaries.
        """
        if not movies_list:
            print("No movies to print.")
            return
        for movie in movies_list:
            title, year, rating, _ = movie.values()
            print(f"{title} ({year}): {rating}")

    def _print_random_movie(self):
        """
        Prints a randomly selected movie from the database.
        """
        movies_list = self._storage.load_movies()
        if not movies_list:
            print("No movies found.")
            return
        movie = random.choice(movies_list)
        print(f"Your movie for tonight: {movie['title']}, it's rated "
              f"{movie['rating']}")

    def _search_movie(self):
        """
        Searches for movies in the database based on a partial match of the
        movie title.
        """
        search_word = input("Enter part of movie name: ").strip().lower()
        movies_list = self._storage.load_movies()
        if not movies_list:
            print("No movies found.")
            return
        matched_movies = [movie for movie in movies_list if
                          search_word in movie["title"].lower()]
        if matched_movies:
            self._print_movies(matched_movies)
        else:
            print("Nothing found")

    def _sort_by_rating(self):
        """
        Sorts and prints the movies in the database based on their rating in
        descending order.
        """
        movies_list = self._storage.load_movies()
        if not movies_list:
            print("No movies found.")
            return
        sorted_movies = sorted(movies_list, key=lambda x: x["rating"],
                               reverse=True)
        self._print_movies(sorted_movies)

    @staticmethod
    def _sort_order():
        """
        Asks the user for the sort order preference (latest movies first or
        not).
        Returns:
            str: 'y' for latest movies first, 'n' otherwise.
        """
        while True:
            answer = input(
                "Do you want the latest movies first? (Y/N) ").strip().lower()
            if answer in ["y", "n"]:
                return answer
            print('Please enter "Y" or "N"')

    def _sort_by_year(self):
        """
        Sorts and prints the movies in the database based on their release
        year,
        either in descending or ascending order based on user preference.
        """
        answer = self._sort_order()
        movies_list = self._storage.load_movies()
        if not movies_list:
            print("No movies found.")
            return
        if answer == "y":
            sorted_movies = sorted(movies_list, key=lambda x: x["year"],
                                   reverse=True)
            self._print_movies(sorted_movies)
        elif answer == "n":
            sorted_movies = sorted(movies_list, key=lambda x: x["year"])
            self._print_movies(sorted_movies)

    def _filter_movies(self):
        """
        Filters and prints movies from the database based on user-defined
        criteria such as
        minimum rating and release year range.
        """
        minimum_rating = float(input(
            "Enter minimum rating (leave blank for no minimum rating): ") or 0)
        start_year = int(
            input("Enter start year (leave blank for no start year): ") or 0)
        end_year = int(
            input("Enter end year (leave blank for no end year): ") or 99999)
        movies_list = self._storage.load_movies()
        filtered_movies = list(filter(
            lambda movie: movie.get("rating") and float(
                movie["rating"]) > minimum_rating and movie.get(
                "year") and end_year >= int(movie["year"]) >= start_year,
            movies_list, ))
        if filtered_movies:
            self._print_movies(filtered_movies)
        else:
            print("Nothing found")

    def process_input(self, user_input):
        """
        Process the user's input and perform the corresponding action.

        Args:
            user_input (str): The user's menu choice.
        """
        actions = {"0": exit, 
                   "1": self._storage.list_movies,
                   "2": self._storage.add_movie,
                   "3": self._storage.delete_movie,
                   "4": self._storage.update_movie,
                   "5": self._command_movie_stats,
                   "6": self._print_random_movie,
                   "7": self._search_movie,
                   "8": self._sort_by_rating,
                   "9": self._sort_by_year,
                   "10": self._filter_movies,
                   "11": self._generate_website, }

        action = actions.get(user_input)
        if action:
            action()
        else:
            print("Invalid choice")

    def run(self):
        """
        Displays the menu options and asks the user for input, processing
        the input to perform the corresponding actions.
        """
        menus = (
            "Exit", "List Movies", "Add Movie", "Delete Movie", "Update Movie",
            "Stats", "Random Movie", "Search Movie", "Movies Sorted by Rating",
            "Movies Sorted by Year", "Filter movies", "Generate website",)

        print("Menu:")
        index_menu = list(enumerate(menus))
        for index, option in index_menu:
            print(f"{index}. {option}")
        print()

        # Get user command
        while True:
            choice = input(f"Enter choice (0-{len(menus) - 1}): ").strip()
            if not choice.isdigit() or int(choice) not in range(len(menus)):
                print("Invalid choice")
                continue
            self.process_input(choice)
            print()
            enter = input("Press enter to continue ")
            if enter == "":
                continue
