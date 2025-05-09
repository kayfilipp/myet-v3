import sqlite3 

class DbConnector:

    def __init__(self, db_path):
        self.db_path = db_path

    def run_query(self, query, commit=False, return_=True, as_dict=True, params=()):

        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        cur.execute(query,params)

        if commit:
            con.commit()

        if not return_:
            con.close()
            return 

        data = cur.fetchall() if not as_dict else [dict(row) for row in cur.fetchall()]
        con.close()
        return data 
    