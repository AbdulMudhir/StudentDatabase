import sqlite3





class StudentDatabase(sqlite3.Connection):

    def __init__(self, database_path):
        sqlite3.Connection.__init__(self, database_path)
        self.cursor = self.cursor()


    def set_database(self):

        self.cursor.execute('''CREATE TABLE database (
       StudentID TEXT UNIQUE,
       Firstname TEXT,
       Lastname TEXT,
       Gender TEXT,
       Age INTEGER,
       Address TEXT,
       Postcode TEXT, 
       Mobile INTEGER,
       Chemistry INTEGER,
       Computing INTEGER,
       English INTEGER,
       Physics INTEGER,
       Biology INTEGER,
       Business INTEGER,
       Maths INTEGER,
       Additional_math INTEGER
        )''')

    def get_columns(self):

        self.cursor.execute("PRAGMA table_info(database)")

        return self.cursor.fetchall()




