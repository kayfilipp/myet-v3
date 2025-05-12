from . import SNOWFLAKE

class User:

    def __repr__(self):
        return f"User(id={self.id}, {self.email})"

    def __init__(self, firstname, lastname, email):
        self.id = None 
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 

    def sync(self):
        SNOWFLAKE.run_query(
            query="""insert into user(firstname, lastname, email) values (%s, %s, %s)""", 
            params=(self.firstname, self.lastname, self.email),
            commit=True,
            return_=False
        )

        id = SNOWFLAKE.run_query(
            query="select id from user where email = %s limit 1", 
            params=(self.email,), 
            return_=True, 
            as_dict=True
        )

        self.id = id[0]['id']

    @property
    def name(self):
        return self.firstname + ' ' + self.lastname