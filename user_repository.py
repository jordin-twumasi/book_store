from user import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, user):
        self.connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [user.username, user.password])
        return None

    def find_by_username(self, username):
        user_details = self.connection.execute(
        'SELECT * FROM users WHERE username = %s', [username])[0]

        return User(
        user_details["username"],
        user_details["password"],
        user_details["id"])