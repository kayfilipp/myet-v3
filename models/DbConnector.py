import sqlite3 
import snowflake.connector


class SQLite:

    def __init__(self, db_path):
        self.db_path = db_path

    def get_con(self):
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        return con, cur 

    def run_query(self, query, commit=False, return_=True, as_dict=True, params=()):

        con, cur = self.get_con()

        cur.execute(query,params)

        if commit:
            con.commit()

        if not return_:
            con.close()
            return 

        data = self.data_as_dict(con,cur) if as_dict else cur.fetchall()
        con.close()
        return data 


    @staticmethod
    def data_as_dict(con, cur):
        return [dict(row) for row in cur.fetchall()]
    
class SnowFlakeSql(SQLite):

    def __init__(self, snowflake_config):
        self.config = snowflake_config 

    def get_con(self):
        con = snowflake.connector.connect(**self.config)
        cur = con.cursor()
        return con,cur 
    
    @staticmethod
    def data_as_dict(con, cur):
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return [dict(zip(columns, row)) for row in rows]