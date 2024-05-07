import streamlit as st
import base64
from PIL import Image
import pandas as pd
import cv2
import urllib
import numpy

st.set_page_config(
    page_title="TCO Dashboard",
    layout="wide",
    page_icon = "🧊"
    # page_icon=Hitachi_logo    
)



def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    [data-testid="Portal"] {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity: 0.5    
    background-repeat: no-repeat;

    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
#background-image: url('https://images.unsplash.com/photo-1714756034183-42581eacfb05?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {    
    background-image: url('../image/ann3.PNG');
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
[data-testid="stAppViewContainer"] > .main::after {    opacity:1;
}
[data-testid="stHeader"]{ background-color : rgba(0,0,0,0);}
}

</style>
"""

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
st.markdown(background_image, unsafe_allow_html=True)
st.sidebar.title("Hitachi TCO &copy;")
st.sidebar.image("./images/hitachi.png")

#st.markdown(opacity, unsafe_allow_html=True)
st.markdown("# Welcome to Sanying Possession Plan")

st.error("TCO contact number : ")

st.warning("Becareful of earthquake in taipei enjoy; find update image below")

#ann3 =  Image.open("./images/ann3.PNG")
#set_background("./images/ann3.PNG")
#set_background("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")

#with st.container():
    #st.image("https://jnnprogress.com/Site/Home_files/banner.jpg")
    #st.image("https://www.jnnprogress.com/Site/Hitachi/images/Depot.PNG")    
    

