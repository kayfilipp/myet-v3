from . import SNOWFLAKE
import json 
import ksuid 
from datetime import datetime 
"""
Assessment Scores can originate in one of two ways:
1. generated during a quiz completed by the user.
2. loaded from db.

in the former, there is no id for the assessment until the result is saved.
in the latter, the id is provided by the db.
"""
def gen_id():
    return ksuid.ksuid().__str__()

class AssessmentScore:

    def __init__(self, user, id: str = None, results: dict={}, created_date: datetime = datetime.now(), is_public:bool=False, saved:bool=False):
        self.user = user 
        self.id = id or gen_id() # if no id is provided, make one up
        self.results = results
        self.created_date = created_date
        self.is_public = is_public
        self.saved = saved 

    def load_from_db(self):
        query = "select * from assessment where user_id = %s and id = %s limit 1"
        params = (self.user.id, self.id)

        _ = SNOWFLAKE.run_query(
            query=query,
            params=params,
            return_=True,
            as_dict=True,
            close_after_operation=False
        )

        assert len(_) == 1, "Cannot load result from DB."

        self.results = json.loads(_[0]['json_results']) 
        self.created_date = _[0]['created_date']
        self.is_public = _[0]['is_public']
        self.saved = True 


    async def save(self):
        query = "insert into assessment(ksuid, user_id,json_results) select %s, %s, PARSE_JSON(%s)"
        params = (self.id, self.user.id, json.dumps(self.results))

        SNOWFLAKE.run_query(
            query=query,
            params=params,
            return_=False,
            commit=True
        )

        self.saved = True 
        self.user.assessment_scores.append(self)


    async def delete(self):

        params = [self.id]

        queries = [
            "delete from assessment_viewers where assessment_ksuid = %s",
            "delete from assessment where ksuid = %s"
        ]

        for query in queries:
            SNOWFLAKE.run_query(
                query=query,
                params=params,
                return_=False,
                commit=True
            )

        self.saved = False 
        self.user.assessment_scores.remove(self)

    async def share(self, emails: str):
        assert self.saved, "Must save assessment score before sharing."
        email_list = emails.split(",")

        viewers = [{"email": email, "assessment_ksuid": self.id} for email in email_list]

        SNOWFLAKE.run_query(
            query=f"create temporary table viewers_{self.id} (email varchar(255), assessment_ksuid varchar(255))",
            return_=False,
            commit=False,
            close_after_operation=False 
        )

        SNOWFLAKE.run_query(
            query="insert into viewers_{self.id} (email, assessment_ksuid) values (%s, %s)",
            params=viewers,
            return_=False,
            execute_many=True,
            commit=False,
            close_after_operation=False
        )

        SNOWFLAKE.run_query(
            query=f"""
            merge into assessment_viewers AS target
            using viewers_{self.id} AS source
                on target.assessment_ksuid = source.assessment_ksuid 
                and target.email = source.email 
            WHEN NOT MATCHED THEN 
                INSERT (assessment_ksuid, email) VALUES (source.assessment_ksuid, source.email);
            """,
            return_=False,
            commit=True,
            close_after_operation=True
        )
