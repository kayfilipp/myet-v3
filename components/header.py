from .buttons import href_button
import streamlit

def _logout(st):
    st.session_state['user_session'].delete()
    st.session_state['auth'].logout()

def header(st: streamlit):
    fname = st.session_state['user'].firstname
    root = st.session_state['root_url']

    with st.sidebar:

        st.title("MYET")
        st.write(f"Hi, {fname}!")
        if st.button("Logout", type="secondary"):
            st.logout()

        st.divider()
        href_button(st, f"{root}/?page=assessment", text="Take Assessment", fill_container=True)
        href_button(st, f"{root}/?page=scores", text="My Scores", fill_container=True)
        href_button(st, f"{root}/?page=invite", text="Invite", fill_container=True) 
        href_button(st, f"{root}/?page=about", text="About Us", fill_container=True) 