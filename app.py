import streamlit as st
from components import header
from components import auth
from components import style
from router import route
import os 
import json 

import streamlit as st
from streamlit_google_auth import Authenticate

authenticator = Authenticate(
    secret_credentials_path='google_credentials.json',
    cookie_name='my_cookie_name',
    cookie_key='this_is_secret',
    redirect_uri='http://localhost:8501',
)

# Check if the user is already authenticated
authenticator.check_authentification()

# Display the login button if the user is not authenticated
if not st.session_state.get('connected', False):
    authorization_url = authenticator.get_authorization_url()
    st.markdown(f'[Login]({authorization_url})')
    st.link_button('Login', authorization_url)
# Display the user information and logout button if the user is authenticated
else:
    st.image(st.session_state['user_info'].get('picture'))
    st.write(f"Hello, {st.session_state['user_info'].get('name')}")
    st.write(f"Your email is {st.session_state['user_info'].get('email')}")
    if st.button('Log out'):
        authenticator.logout()


# st.set_page_config(layout="wide")
# _CONFIG = json.load(open('config.json'))

# st.session_state['root_path'] = os.path.dirname(os.path.abspath(__file__))
# st.session_state['root_url'] = _CONFIG['root']
# st.session_state['questions_chunk_size'] = _CONFIG['questions_chunk_size']

# if not st.session_state.get('connected'):
#     print("checking cache..")
#     auth.check_cached_sessions(st)
#     auth.auth(st)

# else:
#     auth.save_user_and_session(st)

#     style.render(st)
#     header.header(st)
#     route(st)

#     print(st.session_state)