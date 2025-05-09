import json 
import sys, os 
from .DbConnector import DbConnector

_CONFIG_PATH = os.path.abspath("config.json")
_CONFIG = json.load(open(_CONFIG_PATH))
DB_PATH = _CONFIG['db-name']

DB = DbConnector(DB_PATH)