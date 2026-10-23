from film_repository import FilmRepository
from film import Film
from database_connection import DatabaseConnection

# def test_lists_all_films():
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("seeds/films.sql")
#     repository = FilmRepository(connection)

#     result = repository.all()
#     assert result == [
#         Film(1, 'Spiderman', '2003'),
#         Film(2, 'Birdbox', '2018'),
#         Film(3, 'Snow White', '1936'),
#         Film(4,'Avengers', '2012')
#     ]

# def test_adds_film_to_list():
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("seeds/films.sql")
#     repository = FilmRepository(connection)

#     film = Film(5, 'Doomsday', 2026)
#     repository.create(film)

#     assert repository.all() == [
#         Film(1, 'Spiderman', '2003'),
#         Film(2, 'Birdbox', '2018'),
#         Film(3, 'Snow White', '1936'),
#         Film(4,'Avengers', '2012'),
#         Film(5, 'Doomsday', '2026')
#     ]