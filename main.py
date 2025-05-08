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



# st.set_page_config(layout="wide")
# _CONFIG = json.load(open('config.json'))

# st.session_state['root_path'] = os.path.dirname(os.path.abspath(__file__))
# st.session_state['root_url'] = _CONFIG['root']
# st.session_state['questions_chunk_size'] = _CONFIG['questions_chunk_size']

# if not st.session_state.get('connected'):
#     print("checking cache..")
#     auth.check_cached_sessions(st)
#     auth.auth(st)

# else:
#     auth.save_user_and_session(st)

#     style.render(st)
#     header.header(st)
#     route(st)

#     print(st.session_state)