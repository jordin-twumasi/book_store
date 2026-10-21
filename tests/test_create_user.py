import sys
import os

from app import app
from database_connection import DatabaseConnection

def test_create_user_is_saved_to_db():
    #Create the test client
    client = app.test_client()

    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/users.sql") #instead of manually truncaring, call seed


    #Send request 
    response = client.post('/users', data = {
        'username' : 'testuser',
        'password': 'password123'
    })

    #assert that the redirect took place
    assert response.status_code == 302

    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    #assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'