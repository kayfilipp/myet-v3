import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    if st.button("Log in with Google"):
        st.login()

if not st.user.get('is_logged_in'):
    login_screen()
else:
    print(st.user.to_dict())
    st.header(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)