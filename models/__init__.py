import json 
import sys, os 
from .DbConnector import SQLite, SnowFlakeSql

_CONFIG_PATH = os.path.abspath("config.json")
_CONFIG = json.load(open(_CONFIG_PATH))
DB_PATH = _CONFIG['db-name']

DB = SQLite(DB_PATH)

import streamlit as st 
SNOWFLAKE = SnowFlakeSql(st.secrets['snowflake'])
SNOWFLAKE.get_con()