from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    # Selecting all records
    # No arguments

    def all(self):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;
        rows = self._connection.execute('SELECT * FROM users')
        # Returns an array of Users objects.
        users = []
        for row in rows:
            item = User(row["username"], row["account"], row["email_address"])
            users.append(item)
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
        return User(row["username"], row["account"], row["email_address"])

    def create(self, user):
        self._connection.execute('INSERT INTO users (username, account, email_address) VALUES (%s,%s,%s)',[user.username, user.account, user.email_address])
        return None