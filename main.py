from movie_app import MovieApp
from storage import StorageCsv
from storage import StorageJson
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="movie file name")
    parser.add_argument("file_name", help="movie file name csv or json")
    args = parser.parse_args()
    
    # Determine the directory of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    file_path = os.path.join(base_dir, "data", args.file_name)

    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    storage = None

    if "csv" in args.file_name:
        storage = StorageCsv(file_path)
    elif "json" in args.file_name:
        storage = StorageJson(file_path)

    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
