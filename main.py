from movie_app import MovieApp
from storage import StorageCsv
from storage import StorageJson
import argparse

def main():
    parser = argparse.ArgumentParser(description="movie file name")
    parser.add_argument("file_name", help="movie file name csv or json")
    args = parser.parse_args() 

    storage = None
    
    if "csv" in args.file_name:
        storage = StorageCsv(f"./data/{args.file_name}")
    elif "json" in args.file_name:
        storage = StorageJson(f"./data/{args.file_name}")

    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
