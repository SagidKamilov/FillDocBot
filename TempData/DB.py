from typing import List

import sqlite3


class DataBaseConnection:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()


class DataBaseOperations(DataBaseConnection):
    def create_table(self) -> bool:
        sql = """
        CREATE TABLE IF NOT EXISTS document(
        address_up text,
        address_down text,
        type_auto text,
        cargo text, 
        type_up text,
        type_down text,
        contact_manager text,
        info_customer text,
        name_customer text,
        short_name_customer text,
        info_carrier text,
        name_carrier text,
        short_name_carrier text,
        car_brand text
        );
        """
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return True
        except:
            return False

    def insert_data(self, data_dict: dict) -> bool:
        placeholders = ', '.join('?' * len(data_dict))
        columns = ', '.join(data_dict.keys())
        sql = f"INSERT INTO document ({columns}) VALUES ({placeholders})"
        try:
            self.cur.execute(sql, list(data_dict.values()))
            self.conn.commit()
            return True
        except:
            return False

    def get_data_by_column(self, column_name: str) -> List[str] | bool:
        try:
            self.cur.execute(f"SELECT {column_name} FROM document")
            result: list = self.cur.fetchall()
            print(result)
            if result[-1][0]:
                result = result[:-6:-1]
                return [row[0] for row in result if row[0] is not None]
            else:
                return False
        except:
            return False


db = DataBaseOperations("temp_data.db")
print(db.get_data_by_column("type_auto"))
