from . import SNOWFLAKE
from models.AssessmentScore import AssessmentScore
import json 
from datetime import datetime 

class User:

    def __repr__(self):
        return f"User(id={self.id}, {self.email})"

    def __init__(self, firstname, lastname, email):
        self.id = None 
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 

        self.assessment_scores: list[AssessmentScore] = []
        self.shared_scores: list[AssessmentScore] = []

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

    def get_scores(self):

        scores = SNOWFLAKE.run_query(
            query="select ksuid as id, json_results, created_date, is_public from assessment where user_id = %s",
            params = [self.id],
            as_dict=True,
            return_=True,
            close_after_operation=False
        )

        if len(scores) == 0:
            return 

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

    async def get_scores_async(self):
        self.get_scores()

    def get_shared_scores(self):
        #to-do: a method that lets a user see scores people have shared with them.
        scores = SNOWFLAKE.run_query(
            query=f"""
            select 
                a.ksuid as id, a.json_results, a.created_date, a.is_public,
                u.email, u.firstname, u.lastname
            from assessment a 
            inner join user u on user_id = a.user_id
            inner join assessment_viewers av on av.assessment_ksuid = a.ksuid 
            where av.email = %s
            """,
            params=[self.email],
            return_=True,
            as_dict=True,
            close_after_operation=False
        )

        if len(scores) == 0:
            return

        self.shared_scores = [
            AssessmentScore(
                user=User(score['firstname'], score['lastname'], score['email']),
                id=score['id'],
                results=json.loads(score['json_results']),
                created_date=score['created_date'],
                is_public=score['is_public'],
                saved=True
            )
            for score in scores
        ]


