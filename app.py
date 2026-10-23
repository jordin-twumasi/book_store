from flask import Flask, render_template, request, redirect, session
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user_repository import UserRepository
from user import User
from login_required import login_required
from film_repository import FilmRepository
from film import Film

# Instantiate Flask app object
app = Flask(__name__)

#Session config - key preventing tampering (irl long string stored in env)
app.secret_key = "some_really_secret_key"

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
@login_required
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

#Route for serving login form

@app.route('/sessions/new', methods = ["GET"])
def get_user_login_form():
    return render_template("login_form.html")

@app.route("/sessions", methods=["POST"])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    username = request.form["username"]
    password = request.form["password"]
    
    user = user_repository.find_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")



#Film 
@app.route('/films', methods = ["GET"])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    print(films)
    
    return render_template("films.html", films = films) 

@app.route('/films', methods = ["POST"])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form
    film = Film(film_details["title"], film_details["release_year"])
    film_repository.create(film)
    return redirect("/films")

# Make server run in response to app.py on port 5001
# And use debuf mode so changing code restarts app

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)

