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
        self.SNOWFLAKE = SNOWFLAKE

    def load_from_db(self):
        query = "select * from assessment where user_id = %s and id = %s limit 1"
        params = (self.user.id, self.id)

        _ = self.SNOWFLAKE.run_query(
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

        self.SNOWFLAKE.run_query(
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
            self.SNOWFLAKE.run_query(
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

        viewers = [(email, self.id) for email in email_list if email != self.user.email]
        table_name = f"viewers_{self.id}"

        if len(viewers) == 0:
            return

        # Step 1: Create Temporary Table
        self.SNOWFLAKE.run_query(
            query=f"CREATE OR REPLACE TEMPORARY TABLE {table_name} (email VARCHAR(255), assessment_ksuid VARCHAR(255))",
            return_=False,
            commit=True,
            close_after_operation=False
        )

        # Step 2: Insert Data
        self.SNOWFLAKE.run_query(
            query=f"INSERT INTO {table_name} (email, assessment_ksuid) VALUES (%s, %s)",
            params=viewers,
            return_=False,
            execute_many=True,
            commit=True,
            close_after_operation=False
        )

        # Step 3: Merge Data
        self.SNOWFLAKE.run_query(
            query=f"""
            MERGE INTO assessment_viewers AS target
            USING {table_name} AS source
                ON target.assessment_ksuid = source.assessment_ksuid 
                AND target.email = source.email 
            WHEN NOT MATCHED THEN 
                INSERT (assessment_ksuid, email) VALUES (source.assessment_ksuid, source.email)
            """,
            return_=False,
            commit=True,
            close_after_operation=True
        )
