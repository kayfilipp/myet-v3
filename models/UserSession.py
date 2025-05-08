from . import _CONFIG, DB_PATH
from .User import User 
import sqlite3
from datetime import datetime 

SESSION_LOOKUP_FIELD = _CONFIG['session_lookup_on']
SESSION_TIMEOUT_MS = _CONFIG['session_timeout_ms']

class UserSession:
    def __init__(self, session_id):
        self.session_id = session_id 

    def retreive(self) -> User:
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        # 
        # SESSION_TIMEOUT_SECONDS

        cur.execute(
            "select * from user_session where session_id = ? and strftime('%s', 'now') - strftime('%s', touched_at) < ? ",
            [self.session_id, SESSION_TIMEOUT_MS]
        )

        sesh = cur.fetchone()
        con.close()

        if sesh:
            sesh = dict(sesh)
            return User(
                auth_id=sesh['user_id'],
                firstname=sesh['first_name'],
                lastname=sesh['last_name'],
                email=sesh['email']
            )
        return None

    
    def save(self, firstname, lastname, email, user_id, touched_at=datetime.now()):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(
            """
                insert into user_session (session_id, first_name, last_name, email, user_id, touched_at) VALUES (?, ? ,?, ?, ?, ?) 
                on conflict(session_id) do update set touched_at = ?
            """,
            (self.session_id, firstname, lastname, email, user_id, touched_at, touched_at)
        )
        con.commit()
        con.close()

    def touch(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(
            "update user_session set touched_at = ? where session_id = ?",
            (self.session_id, datetime.now())
        )
        con.commit()
        con.close()

    def delete(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(
            "delete from user_session where session_id = ?",
            [self.session_id]
        )
        con.commit()
        con.close()