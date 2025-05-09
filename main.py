# app.py
import streamlit as st
import squadbase.streamlit as sq

user_info = sq.auth.get_user()
st.write(user_info)
# st.write(f"Hello, {user_info['firstName']} {user_info['lastName']}")

if "admin" in user_info['roles']:
  st.write("You are an admin")
else:
  st.write("You are not an admin")
