import sqlite3


class Config:
    def __init__(self, path):
        con = sqlite3.connect(path)
        self.cur = con.cursor()

    def create_tables(self):
        with open("Requests/create_table_genres.sql", "r") as f_o:
            self.cur.execute(f_o.read())

    def selected(self): ...

    def inserts(self): ...
