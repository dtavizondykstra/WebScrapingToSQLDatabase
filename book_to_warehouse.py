import sqlite3
import requests
from bs4 import BeautifulSoup
# Request URL


def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)


def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE books
        (title TEXT, price REAL, rating INTEGER)''')
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    ratings_dict = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    rating_paragraph = book.select(".star-rating")[0]
    text_rating = rating_paragraph.get_attribute_list("class")[-1]
    int_rating = ratings_dict[text_rating]


scrape_books("https://books.toscrape.com/catalogue/category/books/history_32/index.html")
# print(books)
# Initialize BeautifulSoup
# Extract the data we want
# Save data to database
