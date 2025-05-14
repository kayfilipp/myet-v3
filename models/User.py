from . import SNOWFLAKE
from models.AssessmentScore import AssessmentScore
import json 

class User:

    def __repr__(self):
        return f"User(id={self.id}, {self.email})"

    def __init__(self, firstname, lastname, email):
        self.id = None 
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 

        self.assessment_scores: list[AssessmentScore] = []

    @property
    def name(self):
        return self.firstname + ' ' + self.lastname
    
    async def get_user_id(self):

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
            close_after_operation=False
        )

        self.id = id[0]['id']

    async def get_scores(self):

        scores = SNOWFLAKE.run_query(
            query="select ksuid as id, json_results, created_date, is_public from assessment where user_id = %s",
            params = [self.id],
            as_dict=True,
            return_=True,
            close_after_operation=False
        )

        self.assessment_scores = [
            AssessmentScore(
                user=self, 
                id=score['id'], 
                results=json.loads(score['json_results']),
                created_date=score['created_date'],
                is_public=score['is_public'],
                saved=True
            )
            for score in scores 
        ]

    async def get_shared_scores(self):
        #to-do: a method that lets a user see scores people have shared with them.
        pass 

