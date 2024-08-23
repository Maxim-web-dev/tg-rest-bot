from typing import Any
import sqlite3 as sql

class DataBase(object):
    def __init__(self, db_path: str, table_name: str) -> None:
        self.db = sql.connect(db_path)
        self.c = self.db.cursor()
        
    def find(self, ) -> Any:
        pass