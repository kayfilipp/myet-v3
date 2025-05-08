import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

if not 'is_logged_in' in st.user:
    login_screen()
else:
    print(st.user.__dict__)
    st.header(f"Welcome, {st.user}!")
    st.button("Log out", on_click=st.logout)