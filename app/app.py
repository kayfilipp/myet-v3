import streamlit as st

st.title("Welcome to your MYET Account!")

if not st.experimental_user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

with st.sidebar:
    st.header(f"Logged in with {st.experimental_user.email}")
    if st.button("🔓 Logout"):
        st.logout()

st.divider()

_c = st.columns([1,1,8])

with _c[0]:
    st.image(st.experimental_user.get("picture", ".\assets\default_profile.jpg"))

st.write(st.experimental_user)