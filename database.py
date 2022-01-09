import sqlite3


class Db:
    def __init__(self, path):
        self.path = path

    def load(self, tab):
        conn = None
        sp = []
        try:
            conn = sqlite3.connect(self.path)
            cur = conn.cursor()
            data = cur.execute("SELECT * FROM '{}' ORDER BY rowid".format(tab)).fetchall()

            for i in data:
                row = []
                for j in i:
                    row.append(j)
                sp.append(row)
            return sp
        except Exception as e:
            print(e)
            return []
        finally:
            if conn:
                conn.close()
