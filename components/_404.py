import streamlit
from .buttons import href_button
def render(st: streamlit):

    st.header("Sorry. 😔")
    st.caption("The page you're looking for doesn't exist!")
    home = st.session_state['root_url']
    href_button(st, url=home, text="Home", fill_container=False)
