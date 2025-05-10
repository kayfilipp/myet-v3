from models.User import User

def render(st):

    user: User = st.session_state['User']

    # add a logout button to the sidebar
    with st.sidebar:
        st.caption(f"Logged in with {user.email}")
        if st.button("🔓 Logout"):
            st.logout()