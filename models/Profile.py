from models.User import User 
from models.Assessment import Assessment
from . import DB

# used to pull assessments and stuff I guess 

class Profile:

    def __init__(self, user: User):
        self.user = user 

    def get_assessment_history(self):
        query="select id, created_date, json_results, is_public from assessment where user_id = ?"
        params = [self.user.id]
        self.assessments = DB.run_query(query=query, params=params, return_=True, commit=False, as_dict=True)