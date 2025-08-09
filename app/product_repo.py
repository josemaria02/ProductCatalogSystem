from app.database import Database


class ProductRepo:
    def __init__(self):
        self.db = Database.get_connection

