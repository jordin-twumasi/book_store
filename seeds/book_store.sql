
CREATE TABLE IF NOT EXISTS books(
    id SERIAL PRIMARY KEY,
    title text,
    author text
);

TRUNCATE TABLE books RESTART IDENTITY; --Removes all rows without dropping table


INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');