from . import DB

class User:

    def __init__(self, auth_id, firstname, lastname, email):
        self.auth_id = auth_id
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 
        self.db = DB

    def save(self):
        DB.run_query(
            query="""insert or replace into user(auth_id, firstname, lastname, email) values (?, ?, ?, ?)""", 
            params=(self.auth_id, self.firstname, self.lastname, self.email),
            commit=True,
            return_=False
        )