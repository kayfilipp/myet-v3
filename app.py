import streamlit as st
from components import header
from components import auth
from components import style
from router import route
import os 
import json 

st.set_page_config(layout="wide")
_CONFIG = json.load(open('config.json'))

st.session_state['root_path'] = os.path.dirname(os.path.abspath(__file__))
st.session_state['root_url'] = _CONFIG['root']
st.session_state['questions_chunk_size'] = _CONFIG['questions_chunk_size']

if not st.session_state.get('connected'):
    print("checking cache..")
    auth.check_cached_sessions(st)

if not st.session_state.get('connected'):
    auth.auth(st)

else:
    auth.save_user_and_session(st)

    style.render(st)
    header.header(st)
    route(st)

    print(st.session_state)