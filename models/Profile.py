from models.User import User 
from models.Assessment import Assessment
from . import SNOWFLAKE

# used to pull assessments and stuff I guess 

class Profile:

    def __init__(self, user: User):
        self.user = user 
        self.assessments: list[dict] = []

    def get_assessment_history(self):

        query="select id, created_date, json_results, is_public from assessment where user_id = %s"
        params = [self.user.id]
        self.assessments = SNOWFLAKE.run_query(query=query, params=params, return_=True, commit=False, as_dict=True)
        return 

    def get_assessment(self, id):

        # check locally 
        if self.assessments != []:
            search = next((assessment for assessment in self.assessments if assessment['id'] == id))
            if search:
                return search 
            
        # then cloud 
        query="select id, created_date, json_results, is_public from assessment where user_id = %s and id = %s"
        params = [self.user.id, id]
        assessment =  SNOWFLAKE.run_query(query=query, params=params, return_=True, commit=False, as_dict=True)

        # add assessment to profile 
        self.assessments += assessment 

        return assessment[0]