import sqlite3


con = sqlite3.connect("myet.db")
cur = con.cursor()
cur.execute("""
    create table if not exists question (
        id integer primary key,
        body text not null,
        facet text,
        subtrait text,
        weight float default 0
    )
""")

cur.execute("""
    create table if not exists user (
        id integer primary key,            
        auth_id text unique,
        firstname text,
        lastname text,
        email text unique
    )"""
)

cur.execute("""
    create table if not exists user_session (
        session_id text not null unique,
        first_name text not null,
        last_name text not null,
        email text not null,
        user_id text not null,
        touched_at datetime default CURRENT_TIMESTAMP
    )
""")

con.commit()

