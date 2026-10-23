DROP TABLE IF EXISTS films;

CREATE TABLE IF NOT EXISTS films(
    id SERIAL PRIMARY KEY,
    title text,
    release_year text
);


INSERT INTO films (title, release_year) VALUES ('Spiderman', '2003');
INSERT INTO films (title, release_year) VALUES ('Birdbox', '2018');
INSERT INTO films (title, release_year) VALUES ('Snow White', '1936');
INSERT INTO films (title, release_year) VALUES ('Avengers', '2012');