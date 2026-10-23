import sys
import os

from app import app
from playwright.sync_api import Page
from database_connection import DatabaseConnection

def test_auth_integration_passes():
    #Create the test client
    client = app.test_client()

    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/users.sql") #instead of manually truncaring, call seed
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    #Send request 
    response = client.post('/sessions', data = {
        'username' : 'test',
        'password': '1234'
    })

    #assert that the redirect took place
    assert response.status_code == 302

    #new assertion - ensures redirected to correct page
    assert response.headers['Location'].endswith('/books')


#Incomplete
def test_auth_integration_fails():
     #Create the test client
        client = app.test_client()
    
        connection = DatabaseConnection()
        connection.connect()
        connection.seed("seeds/users.sql") #instead of manually truncaring, call seed
        connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    
        #Send request 
        response = client.post('/sessions', data = {
            'username' : 'incorrect_test',
            'password': 'incorrect_password'
        })

        assert response.status_code == 302

        

    

def test_auth(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/users.sql") #instead of manually truncaring, call seed
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    
    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("1234")
    page.get_by_role("button").click()

    assert page.url == "http://localhost:5001/books"


# #Incomplete
# def test_auth_fails(page: Page):
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("seeds/users.sql") #instead of manually truncaring, call seed
#     connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    
#     page.goto("http://localhost:5001/sessions/new")
#     page.get_by_placeholder("username").fill("test")
#     page.get_by_placeholder("password").fill("1234")
#     page.get_by_role("button").click()

