from film import Film
from database_connection import DatabaseConnection

class FilmRepository:
   def __init__(self, connection):
      self.connection = connection

   def all(self):
      rows = self.connection.execute("SELECT * from films")
      films = []
      for row in rows:
         film = Film(row['title'], row['release_year'], row['id'])
         films.append(film)
      return films

   def create(self, film):
      self.connection.execute("INSERT INTO films VALUES (%s, %s, %s)", [film.title, film.release_year, film.id])
      return None

      