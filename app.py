from flask import Flask, render_template, request, redirect
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user_repository import UserRepository
from user import User

# Instantiate Flask app object
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route('/team', methods=["GET"])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/books', methods = ['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)

    return render_template("books.html", books = books)

@app.route('/books', methods = ["POST"])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title = book_details["title"], author = book_details["author"])
    book_repository.create(book)
    return redirect("/books")


@app.route('/authors', methods =['GET'])
def list_authors():
    return [
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


#User routes

@app.route('/users/new', methods = ["GET"])
def get_user_signup_form():
    return render_template("signup_form.html")


@app.route("/users", methods = ["POST"])
def create_a_new_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username = user_details["username"], password= user_details["password"])
    user_repository.save(user)
        
    return redirect("/users/new")


# Make server run in response to app.py on port 5001
# And use debuf mode so changing code restarts app

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)

