import sys 
import os


from playwright.sync_api import Page, expect

# hack to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from database_connection import DatabaseConnection


def test_get_books_returns_a_200():
    # Simulate requests
    # 1. Make test client - plays role of browser/curl
    client = app.test_client()

    #Make request, grabbing response object
    response = client.get("/books")

    #Assert response status code is 200
    assert response.status_code == 200

def test_get_books_contains_all_books(page: Page):
  #Extra so tests are done only on seed data
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("li")
    expected_books = [
      'The Gruffalo by Julia Donaldson',
      'Ada Twist, Scientist by Andrea Beaty',
      'The Girl Who Drank the Moon by Kelly Barnhill',
      'Dragons in a Bag by Zetta Elliott'
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_get_authors_returns_a_200():
    client = app.test_client()
    response = client.get("/authors")

    assert response.status_code == 200


def test_get_authors_returns_all_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]

#POST tests

def test_creates_a_new_book(page: Page):

    #Authentication - must login first
    def test_create_new_book(page: Page):

      connection = DatabaseConnection()
      connection.connect()
      connection.execute("TRUNCATE TABLE users;")
      connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

      page.goto("http://localhost:5001/sessions/new")
      page.get_by_placeholder("username").fill("test")
      page.get_by_placeholder("password").fill("1234")
      page.get_by_role("button").click()

      page.goto("http://localhost:5001/books")
      page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
      page.get_by_placeholder("Author").fill("Geronimo")
      page.get_by_role("button", name="Submit").click()
      books = page.locator('li')
      new_book = books.all_inner_texts()[-1]
      assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"