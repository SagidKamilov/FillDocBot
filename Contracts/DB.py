import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect(database="docxTemp.db")
        self.cur = self.conn.cursor()

    def create_file_meta(self, short_name: str, name: str, path: str):
        sql = """
        INSERT INTO file(short_name, name, path) VALUES (?, ?, ?)
        """
        self.cur.execute(sql, (short_name, name, path))
        self.conn.commit()

    def delete_file_meta(self, short_name: str):
        sql = """
        DELETE FROM file WHERE short_name=?
        """
        self.cur.execute(sql, (short_name,))
        self.conn.commit()


# DB().create_file_meta("ok", "ok", "ok")
# DB().delete_file_meta("ok")