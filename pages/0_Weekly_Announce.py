# example/st_app.py

import streamlit as st
from io import BytesIO
import requests
import base64
from pathlib import Path
import io


def open_pdf_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        st.write(response.status_code)
        st.error(f"Failed to fetch PDF from URL: {url}")
        return None


st.set_page_config(
    page_title="Announcement",
    layout="wide",
    page_icon = "🧊"
    # page_icon=Hitachi_logo    
)

init_page =     """
    <style>
    .block-container { padding-top: 0rem;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .stToolbar {visibility: hidden;}
    .st-emotion-cache-zq5wmm.ezrtsby0 { visibility: hidden;}
    [data-testid="manage-app-button"] { visibility: hidden;}
    </style>    
    """

init_sidebar = """
    <style>    
    [data-testid='stSidebarNavItems'] {                 
        margin-top: -50px;
        min-height: 60vh; 
    }
    </style>
"""

st.markdown(init_sidebar, unsafe_allow_html=True)
st.markdown(init_page, unsafe_allow_html=True)
st.sidebar.title("Hitachi TCO &copy;")
st.sidebar.image("./images/hitachi.png")

st.markdown("# Weekly Announce for week xxx")
st.markdown("Date : xxx to xxx")
st.markdown("# Controlled Area ")

headerx = {  'Accept': '*/*'}

urla = 'https://www.jnnprogress.com/Site/Hitachi/images/ann1.PNG'
#urla = 'https://www.jnnprogress.com/Site/Hitachi/ann/DepotControl.pdf'
#urla = 'https://www.ti.com/lit/ds/symlink/lm741.pdf'
response = requests.get(urla)

#on_fly_mem_obj = io.BytesIO(response.content)

st.write(response)
st.write(response.headers)
st.write(response.status_code)
#st.write(response.content)
#st.image(io.BytesIO(response.content))
#st.markdown(f'<iframe src="{urla}" width="700" height="1000"></iframe>', unsafe_allow_html=True)
#st.write('https://www.jnnprogress.com/Site/Hitachi/images/ann1.PNG')
st.markdown("# Train Testing / Energization Plan")

st.markdown(" # Shutdown  Plan ")


