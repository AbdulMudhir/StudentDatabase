import sqlite3


class StudentDatabase(sqlite3.Connection):

    def __init__(self, database_path):
        sqlite3.Connection.__init__(self, database_path, check_same_thread=False)
        self.cursor = self.cursor()

    def create_database(self):
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
       Additional_Math INTEGER
        )''')

    def get_columns(self):
        self.cursor.execute("PRAGMA table_info(database)")

        return self.cursor.fetchall()

    def add_student(self, student_info):
        self.cursor.execute('''INSERT OR IGNORE INTO database
         VALUES( 
        :student_id,
        :first_name,
         :last_name,
        :gender,
        :age,
        :address,
        :postcode,
        :mobile,
        :chemistry,
        :computing,
        :english,
        :physics,
        :biology,
        :business,
         :maths,
        :add_math)''', student_info)


    def get_database(self):
        self.cursor.execute("SELECT * FROM database")

        return self.cursor.fetchall()

    def get_student_data(self, student_id):
        self.cursor.execute("SELECT * FROM database WHERE StudentID = :student_id", {'student_id': student_id})
        return self.cursor.fetchone()

    def remove_student(self, student_id):
        self.cursor.execute("DELETE FROM  database WHERE StudentID = :student_id", {'student_id': student_id})
        self.commit()

    def update_student(self, student_id, column_name, updated_value):
        self.cursor.execute(f"UPDATE database SET {column_name}= :updated_value WHERE StudentID = :student_id",
                            {'student_id': student_id,
                             'updated_value':updated_value})
        self.commit()

    def filter_student_by_id(self, student_id):
        self.cursor.execute(f"SELECT * FROM database WHERE StudentID LIKE '%{student_id}%';")

        return self.cursor.fetchall()