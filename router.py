import streamlit 
from components import main
from components import assesment
from components import _404
import json 

_CONFIG = json.load(open('config.json'))
ROOT = _CONFIG['root']

routes = {
    'main': main,
    'assessment': assesment
}

def route(st: streamlit):
    params = st.query_params
    page = params.get('page', 'main')
    
    if not page in routes:
        _404.render(st)
        return 
    
    routes[page].render(st)
