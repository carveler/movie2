# Movie App

This is a Python application for managing movie data.  
It provides functionality to load movies from a csv json file, display statistics about the movies, generate a html with movie information, and perform various operations like adding, deleting, and updating movies.

## Setup

To set up Movie App on your local machine, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/movie2.git
    ```

2. Navigate to the project directory:
    ```bash
    cd movie2
    ```

3. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

# Setting Up API Key for Movie App

To access additional movie information, Movie App requires an API key for the [OMDB API](https://www.omdbapi.com/). Follow these steps to set up the API key:

1. **Create .env file:** 
   - In your project directory, create a new file named `.env`.

2. **Add API Key to .env file:** 
   - Open the `.env` file in a text editor.
   - Add the following line to the file, replacing `"YOUR_API_KEY"` with your actual API key:
     ```
     API_KEY=YOUR_API_KEY
     ```

3. **Save the .env file:** 
   - Save the changes made to the `.env` file.

4. **Configure .gitignore:** 
   - Open or create a file named `.gitignore` in your project directory.
   - Add the following line to the `.gitignore` file to ensure that the `.env` file is not committed to your version control system:
     ```
     .env
     ```

5. **Verify .env is Ignored:** 
   - Ensure that `.env` is listed in your `.gitignore` file to prevent accidental commits of sensitive information.

By following these steps, you'll have securely set up your API key for Movie App, allowing it to access the OMDB API and retrieve additional movie information.

 

## Usage

To use Movie App, follow these steps:

1. Run the main script:
    ```bash
    python3 main.py
    ```

2. Follow the on-screen menu options to interact with the application. You can list movies, add new movies, delete existing movies, update movie ratings, display movie statistics, generate a website with movie information, and more.
