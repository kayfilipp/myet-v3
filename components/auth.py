from models.User import User
from streamlit_google_auth import Authenticate
from models.UserSession import UserSession


def check_cached_sessions(st):
    anonymous_session_id = st.session_state.get("init", None)

    if not anonymous_session_id:
        return 
    
    anonymous_session_id = anonymous_session_id.get("ajs_anonymous_id", None)

    sesh = UserSession(anonymous_session_id)

    # try to find a user based on the session.
    sesh_user = sesh.retreive()
    
    if not sesh_user:
        return
    
    print("found user session!")
    # touch the session to keep it alive.
    sesh.touch()

    # alter session state by creating a user and checking the connected box.
    st.session_state['connected'] = True 
    st.session_state['user'] = sesh_user
    st.session_state['user_session'] = sesh

def auth(st):

    st.session_state['auth'] = Authenticate(
        secret_credentials_path='./google_credentials.json',
        cookie_name='google_auth_cookie',
        cookie_key='google_auth_secret',
        redirect_uri=st.session_state['root_url'],
    )

    # Catch the login event
    st.session_state['auth'].check_authentification()

    # Create the login button and stop the flow.
    if not st.session_state.get('connected', False):
        st.subheader("Welcome to MYET!")
        st.caption("Please log in to your Google account to continue.")
        st.session_state['auth'].login(justify_content="left")

def save_user_and_session(st):

    # update user in db or crate if we have user info.
    if 'user_info' not in st.session_state:
        return

    user_info = st.session_state['user_info']

    if not st.session_state.get('user'):

        st.session_state['user'] = User(
            auth_id=user_info['id'],
            email=user_info['email'],
            firstname=user_info['given_name'],
            lastname=user_info['family_name']
        )
        st.session_state['user'].save()


    # save the user session for future reference.
    anonymous_session_id = st.session_state.get("init",{}).get("ajs_anonymous_id", None)

    if anonymous_session_id and not st.session_state.get('user_session'):
        print('saving user session...')
        st.session_state['user_session'] = UserSession(anonymous_session_id)
        st.session_state['user_session'].save(
            user_id=user_info['id'],
            email=user_info['email'],
            firstname=user_info['given_name'],
            lastname=user_info['family_name']
        )          