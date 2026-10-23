from film import Film

def test_constructs_film_with_fields():
    film = Film('Doomsday', "2026", 5)
    assert film.id == 5
    assert film.title == "Doomsday"
    assert film.release_year == "2026"

def test_equality():
    film_1 = Film('Doomsday', "2026", 5)
    film_2 = Film('Doomsday', "2026", 5)
    assert film_1 == film_2

def test_prints_nicely():
    film = Film('Doomsday', "2026", 5)
    assert str(film) == "Film(5, Doomsday, 2026)"