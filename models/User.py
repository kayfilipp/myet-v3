from . import DB

class User:

    def __init__(self, auth_id, firstname, lastname, email):
        self.auth_id = auth_id
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 
        self.db = DB

    def sync(self):
        DB.run_query(
            query="""insert or ignore into user(auth_id, firstname, lastname, email) values (?, ?, ?, ?)""", 
            params=(self.auth_id, self.firstname, self.lastname, self.email),
            commit=True,
            return_=False
        )

        id = DB.run_query(
            query="select id from user where auth_id = ?", 
            params=(self.auth_id), 
            return_=True, 
            as_dict=True
        )

        print(id)
