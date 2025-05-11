from . import DB

class User:

    def __repr__(self):
        return f"User(id={self.id}, {self.email})"

    def __init__(self, firstname, lastname, email):
        self.id = None 
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 
        self.db = DB

    def sync(self):
        DB.run_query(
            query="""insert or ignore into user(firstname, lastname, email) values (?, ?, ?)""", 
            params=(self.firstname, self.lastname, self.email),
            commit=True,
            return_=False
        )

        id = DB.run_query(
            query="select id from user where email = ? limit 1", 
            params=[self.email], 
            return_=True, 
            as_dict=True
        )

        self.id = id[0]['id']
