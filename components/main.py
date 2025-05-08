import streamlit
from .buttons import href_button

def render(st: streamlit):
    st.subheader("Welcome to your MYET page.")
    st.caption("What would you like to do today?")

    st.divider()

    cols = st.columns([1.5,1.5,1.5,5.5])
    
    with cols[0]:
        href_button(st, f"{st.session_state['root_url']}/?page=assessment", text="Take Assessment", fill_container=True)
    with cols[1]:
        href_button(st, f"{st.session_state['root_url']}/?page=scores", text="See Scores", fill_container=True)
    with cols[2]:
        href_button(st, f"{st.session_state['root_url']}/?page=invite", text="Invite Others", fill_container=True)
    