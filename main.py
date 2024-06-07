from movie_app import MovieApp
from storage import StorageCsv
# from storage import StorageJson


def main():
    # storage = storage_json.StorageJson("./movies.json")
    storage = StorageCsv("./data/movies.csv")
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
