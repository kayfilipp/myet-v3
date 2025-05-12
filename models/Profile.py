from models.User import User 
from models.Assessment import Assessment
from . import SNOWFLAKE

# used to pull assessments and stuff I guess 

class Profile:

    def __init__(self, user: User):
        self.user = user 
        self.assessments: list[dict] = None

    def get_assessment_history(self):
        query="select id, created_date, json_results, is_public from assessment where user_id = %s"
        params = [self.user.id]
        self.assessments = SNOWFLAKE.run_query(query=query, params=params, return_=True, commit=False, as_dict=True)