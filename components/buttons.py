def href_button(st, url, text, fill_container=False):
    _class = "button" if not fill_container else "button fill-container"
    st.markdown(f'<a href="{url}" class="{_class}" target="_self">{text}</a>', unsafe_allow_html=True)