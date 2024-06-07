from movie_app import MovieApp
import storage_csv
import storage_json


# storage = storage_json.StorageJson("movies.json")
storage = storage_csv.StorageCsv("movies.csv")
movie_app = MovieApp(storage)
print(storage.load_movies)
movie_app.run()


def main():
    movie_app.run()


if __name__ == "__main__":
    main()
