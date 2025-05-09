import streamlit as st

st.title("Welcome to your MYET Account!")
user = st.experimental_user

if not st.user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

with st.sidebar:
    st.header(f"Logged in with {user.email}")
    if st.button("🔓 Logout"):
        st.logout()

st.divider()

_c = st.columns([1,1,8])

with _c[0]:
    st.caption(user.name)
    st.image(user.get("picture", ".\assets\default_profile.jpg"))

st.write(user)