import streamlit as st

st.set_page_config(
    page_title="MYET",
    page_icon="./assets/favicon-32x32.png",
    initial_sidebar_state="expanded",
    layout="wide"
)

# Define app pages
landing_page = st.Page("./app/landing.py", title="Welcome", icon=":material/menu:")
app_page = st.Page("./app/app.py", title="Home", icon=":material/home:")
admin_page = st.Page("./app/admin.py", title="Admin", icon=":material/admin_panel_settings:")

# Enables switch_page behaviour
if not st.experimental_user.is_logged_in:
    pg = st.navigation(
        [landing_page],
        position="hidden",
    )
elif st.experimental_user.email == st.secrets["admin_email"]:
    pg = st.navigation(
        [app_page, admin_page],
    )
else:
    pg = st.navigation(
        [app_page],
        position="hidden",
    )

# Head to first page of navigation
pg.run()
