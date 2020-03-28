import sqlite3





class StudentDatabase(sqlite3.Connection):

    def __init__(self):
        sqlite3.