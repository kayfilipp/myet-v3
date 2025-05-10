def render(st):
    # add a logout button to the sidebar
    with st.sidebar:
        st.caption(f"Logged in with {user['email']}")
        if st.button("🔓 Logout"):
            st.logout()