# Book Scraper and Database Saver

## Overview

The **Book Scraper and Database Saver** is a Python application that scrapes book data from a webpage and stores it in an SQLite database. It extracts information such as the title, price, and rating of books from the webpage.

## How It Works

1. The program sends a request to a webpage containing a list of books.
2. It uses BeautifulSoup to parse the HTML and extract the book data.
3. The data (title, price, rating) is stored in an SQLite database called `books.db`.

## Requirements

- Python 3.x
- `requests` module (can be installed using `pip install requests`)
- `BeautifulSoup` from the `bs4` library (can be installed using `pip install beautifulsoup4`)
- `sqlite3` (included with Python)

## Installation

1. Clone this repository or download the code files.
2. Install the required dependencies:

```
bash
   pip install requests beautifulsoup4
```

3. Run the `book_scraper.py` file in your terminal:

## How to Use
1. Run the Program: The program will start by sending a request to the URL specified in the scrape_books function.
2. Scrape Data: It scrapes the title, price, and rating of each book on the webpage.
3. Save to SQLite Database: The program saves the scraped data to an SQLite database (books.db) in a table named books.

## Example Output
The table books in the books.db database will have the following structure:
```
title (TEXT): The title of the book.
price (REAL): The price of the book in GBP.
rating (INTEGER): The rating of the book (0-5).
```

## Error Handling
The program is designed to handle typical webpage parsing scenarios. If the webpage structure changes or the required data cannot be found, an error may occur.

## Example Usage
* After running the program, you can view the contents of the books.db database using a tool like sqlite3: `sqlite3 books.db`
* To query the database: `SELECT * FROM books;`

## License
This project is open-source and available under the MIT License.
