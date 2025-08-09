import sqlite3
from app.config import DATABASE as db_name

class Database:
    #check if this is the right way to do singleton in python
    def __init__(self):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def get_connection(self):
        return self.connection
    
    def init_db():
        pass
