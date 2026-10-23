import sys
import os

from playwright.sync_api import Page, expect


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from database_connection import DatabaseConnection



def test_get_films_returns_200(): 
    #Simulate request - make test client, make request, assert response
    client = app.test_client()

    response = client.get('/films')

    assert response.status_code == 200

def test_get_film_contains_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/films.sql")

    page.goto("http://127.0.0.1:5001/films")
    films = page.locator('li')
    expected_films = [
        "Spiderman - 2003",
        "Birdbox - 2018",
        "Snow White - 1936",
        "Avengers - 2012"
    ]
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films

# def test_create_a_film(page: Page):
#     #Authentication - unrelated 
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("seeds/films.sql")
#     # connection.execute("TRUNCATE TABLE films;")
#     # connection.execute("INSERT INTO films (title, release_year) values ('test_title', 'test_year');")

#     page.goto("http://127.0.0.1:5001/films")
#     page.get_by_placeholder("Title").fill("test_title")
#     page.get_by_placeholder("Release Year").fill("test_year")
#     page.get_by_role("button", name = "Submit").click()

#     films = page.locator('li')
#     print(films.all_inner_texts())
#     new_film = films.all_inner_texts()[-1] #final item in list
#     assert new_film == "test_title - test_year"