import sqlite3 
import snowflake.connector


class SQLite:

    def __init__(self, db_path):
        self.db_path = db_path

    def get_con(self):
        self.con = sqlite3.connect(self.db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def run_query(self, query, commit=False, return_=True, as_dict=True, params=(), close_after_operation=True):

        self.cur.execute(query,params)

        if commit:
            self.con.commit()

        if return_:
            data = self.data_as_dict(self.con,self.cur) if as_dict else self.cur.fetchall()
        else:
            data = None
        
        if close_after_operation:
            self.con.close()

        return data 

    def data_as_dict(self):
        return [dict(row) for row in self.cur.fetchall()]
    
class SnowFlakeSql(SQLite):

    def __init__(self, snowflake_config):
        self.config = snowflake_config 

    def get_con(self):
        self.con = snowflake.connector.connect(**self.config)
        self.cur = self.con.cursor()
    
    def data_as_dict(self):
        rows = self.cur.fetchall()
        columns = [desc[0].lower() for desc in self.cur.description]
        return [dict(zip(columns, row)) for row in rows]