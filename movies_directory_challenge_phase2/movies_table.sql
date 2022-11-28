CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int
);


INSERT INTO movies (title, release_year)
VALUES ('Braveheart', 1995);