from .DbConnector import SnowFlakeSql
import streamlit as st 
SNOWFLAKE = SnowFlakeSql(st.secrets['snowflake'])
SNOWFLAKE.get_con()