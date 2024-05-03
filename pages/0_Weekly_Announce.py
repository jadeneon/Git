# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Announcement",
    layout="wide",
    page_icon = "🧊"
    # page_icon=Hitachi_logo    
)


st.markdown("# Weekly Announce")
st.markdown("### Train testing and Energization Plan for week xxx ")
st.markdown("Date : xxx to xxx")

url = "https://docs.google.com/spreadsheets/d/1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc/edit?usp=sharing" 

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
st.dataframe(data)