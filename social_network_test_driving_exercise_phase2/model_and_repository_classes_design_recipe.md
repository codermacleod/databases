# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: students

Columns:
id | name | cohort_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE users RESTART IDENTITY; -- replace with your own table name.
TRUNCATE TABLE posts RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO users (username, account, email_address) VALUES ('Steve Jobs', 77, 'sj@apple.com');
INSERT INTO users (username, account, email_address) VALUES ('Bill Gates', 88, 'bg@microsoft.com');
INSERT INTO users (username, account, email_address) VALUES ('Joe Bloggs', 99, 'jb@chill.com');
INSERT INTO users (username, account, email_address) VALUES ('Jean Claude Van Damme', 111, 'jcvd@stillkicking.com');

INSERT INTO posts (title, content, views, id) VALUES ('How to take mushrooms...', 'Lie down on a nice patch of grass...', 1000, 1);
INSERT INTO posts (title, content, views, id) VALUES ('How to punch snakes...', 'Position your feet nicely...', 12000, 4);
INSERT INTO posts (title, content, views, id) VALUES ('How to take it easy...', 'Get a sofa...', 24, 3);
INSERT INTO posts (title, content, views, id) VALUES ('How to make billions from windows...', 'Put on your glasses...', 10000, 2);
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: users

# Model class
# (in lib/users.py)
class User


# Repository class
# (in lib/user_repository.py)
class UserRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: users

# Model class
# (in lib/users.py)

class User:
	def __init__(self):
		self.username = ""
		self.account = 0
		self.email_address = ""
 


  # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> user = User()
# >>> user.username = "Dan"
# >>> user.account = "89098788"
# >>> user.username
# 'Dan'
# >>> user.email_address 
# 'dan@gmail.com'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/user_repository.py)

class UserRepository():

	# Selecting all records
	# No arguments
	def all(self):
		# Executes the SQL query:
		# SELECT id, name, cohort_name FROM students;
		rows = self._connection.execute(SELECT * FROM users)
		# Returns an array of Users objects.
		users = []
		for row in rows:
			item = User(row=["username"], row=["account"], row=["email_address"])
			user.append(item)
		return users

		# Gets a single record by its ID
		# One argument: the id (number)
	def find(self, id):
		# Executes the SQL query:
		# SELECT username, account, email_address FROM students WHERE id = $1;
		rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])#sql injection security
		# Returns a single Student object.
		row = rows[0]
		# Add more methods below for each operation you'd like to implement.
		return User(row=["username"], row=["account"], row=["email_address"])

	# def create(User):
	

	# def update(user)
	# 

	# def delete(user)
	# 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

repo = StudentRepository()

students = repo.all()

len(students) # =>  2

students[0].id # =>  1
students[0].name # =>  'David'
students[0].cohort_name # =>  'April 2022'

students[1].id # =>  2
students[1].name # =>  'Anna'
students[1].cohort_name # =>  'May 2022'

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

student.id # =>  1
student.name # =>  'David'
student.cohort_name # =>  'April 2022'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->