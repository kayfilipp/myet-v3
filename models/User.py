import sqlite3

class User:

    def __init__(self, auth_id, firstname, lastname, email):
        self.auth_id = auth_id
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 

    def save(self):
        con = sqlite3.connect("myet.db")
        cur = con.cursor()
        cur.execute("""
        insert or replace into user(auth_id, firstname, lastname, email) values (?, ?, ?, ?)
        """, (self.auth_id, self.firstname, self.lastname, self.email))
        con.commit()