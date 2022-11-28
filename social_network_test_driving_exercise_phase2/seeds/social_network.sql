DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;



CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  account INTEGER,
  email_address VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
-- Then the table with the foreign key first.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  content VARCHAR(255),
  views INTEGER,
-- The foreign key name is always {other_table_singular}_id
  user_id INT,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (username, account, email_address) VALUES ('Steve Jobs', 77, 'sj@apple.com');
INSERT INTO users (username, account, email_address) VALUES ('Bill Gates', 88, 'bg@microsoft.com');
INSERT INTO users (username, account, email_address) VALUES ('Joe Bloggs', 99, 'jb@chill.com');
INSERT INTO users (username, account, email_address) VALUES ('Jean Claude Van Damme', 111, 'jcvd@stillkicking.com');

INSERT INTO posts (title, content, views, user_id) VALUES ('How to take mushrooms...', 'Lie down on a nice patch of grass...', 1000, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('How to punch snakes...', 'Position your feet nicely...', 12000, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('How to take it easy...', 'Get a sofa...', 24, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('How to make billions from windows...', 'Put on your glasses...', 10000, 2);
