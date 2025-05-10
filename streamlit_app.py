import streamlit as st
from models.User import User

st.set_page_config(
    page_title="MYET",
    page_icon="./assets/favicon-32x32.png",
    initial_sidebar_state="expanded",
    layout="wide"
)

# styles
st.components.v1.html("styles.html")

# Define app pages
landing_page = st.Page("./app/landing.py", title="Welcome", icon=":material/menu:")
app_page = st.Page("./app/app.py", title="Home", icon=":material/home:")
admin_page = st.Page("./app/admin.py", title="Admin", icon=":material/admin_panel_settings:")
assessment_page = st.Page("./app/quiz.py", title="Assessment", icon=":material/edit:")
about_page = st.Page("./app/about.py", title="About", icon=":material/info:")

# Enables switch_page behaviour
if not st.experimental_user.is_logged_in:

    pg = st.navigation(
        [landing_page],
        position="hidden",
    )

else:

    pages = [app_page, assessment_page, about_page]
    if st.experimental_user.email == st.secrets["admin_email"]:
        pages += [admin_page]

    pg = st.navigation(
        pages,
        position="sidebar",
    )

    # save the user as a User object if they don't already exist.
    user = st.experimental_user

    if not st.session_state.get('User'):

        firstname = user.get('given_name') if user.get('given_name') else user.get('name')
        lastname = user.get('family_name')

        _user = User(
            auth_id=user['email'],
            firstname=firstname,
            lastname=lastname,
            email=user['email']
        )
        _user.save()

        st.session_state['User'] = _user

    # add a logout button to the sidebar
    with st.sidebar:
        st.caption(f"Logged in with {user['email']}")
        if st.button("🔓 Logout"):
            st.logout()

# Head to first page of navigation
pg.run()

