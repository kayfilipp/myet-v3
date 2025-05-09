import streamlit as st

st.title("Welcome to MYET!")

st.markdown(
    "Welcome to MYET - a new frontier in risk assessment. Log in to get started!"
)


if st.button(
    "Log In",
    type="primary",
    key="checkout-button",
    use_container_width=True,
):
    # st.login("google")
    st.login("auth0")

st.html("./styles.html")
