# example/st_app.py

import streamlit as st
from io import BytesIO
import requests
from PyPDF2 import PdfReader
import base64
from pathlib import Path

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

headers = {'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}

url = 'https://jnnprogress.com/Site/Hitachi/ann/DepotControl.pdf'
#response = requests.get(url=url, headers=headers, timeout=120)
#on_fly_mem_obj = io.BytesIO(response.content)
#pdf_file = PdfReader(on_fly_mem_obj)

pdf_bytes = open_pdf_from_url(url)
if pdf_bytes :
                st.write(pdf_bytes.getvalue())
                st.markdown(f'<embed src="data:application/pdf;base64,{pdf_bytes.getvalue().decode("utf-8")}" width="700" height="1000" type="application/pdf">', unsafe_allow_html=True)
else:
            st.warning("Please enter a valid URL.")


st.markdown("# Train Testing / Energization Plan")

st.markdown(" # Shutdown  Plan ")


