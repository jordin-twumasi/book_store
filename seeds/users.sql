-- TRUNCATE table users;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

TRUNCATE TABLE users RESTART IDENTITY; --Resets id so each test has clean slate
