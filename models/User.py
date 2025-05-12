from . import SNOWFLAKE

class User:

    def __repr__(self):
        return f"User(id={self.id}, {self.email})"

    def __init__(self, firstname, lastname, email):
        self.id = None 
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 

    async def get_user_id(self):

        SNOWFLAKE.get_con()

        SNOWFLAKE.run_query(
            query="insert into user(firstname, lastname, email) select %s, %s, %s where not exists (select 1 from user where email = %s)", 
            params=(self.firstname, self.lastname, self.email, self.email),
            commit=True,
            return_=False,
            close_after_operation=False
        )

        id = SNOWFLAKE.run_query(
            query="select id from user where email = %s limit 1", 
            params=(self.email,), 
            return_=True, 
            as_dict=True,
            close_after_operation=True
        )

        self.id = id[0]['id']

    @property
    def name(self):
        return self.firstname + ' ' + self.lastname