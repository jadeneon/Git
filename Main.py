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

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {    
    background-image: url('images/ann3.PNG');
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
    opacity:0.5;
}
[data-testid="stHeader"]{
    background-color : rgba(0,0,0,0);

}

</style>
"""

init_page =     """
    <style>
    .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
    .stApp [data-testid="stSidebarNavLink"] { padding-top: 0rem;}
    .reportview-container {margin-top: -2em;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    </style>    
    """

init_sidebar = """
    <style>
    .st-emotion-cache-1oe5cao.eczjsme9 {
      margin-top: -50px;      
    }
    </style>
"""


st.markdown(init_sidebar, unsafe_allow_html=True)
st.markdown(init_page, unsafe_allow_html=True)
st.markdown(background_image, unsafe_allow_html=True)
st.sidebar.title("Hitachi TCO &copy;")

opacity = """
<style>
[data-testid="stAppViewContainer"] > .main {        
    opacity:1;
}
</style>
"""

#st.markdown(opacity, unsafe_allow_html=True)
st.markdown("# Welcome to Sanying Possession Plan")
#ann3 =  Image.open("./images/ann3.PNG")
#set_background("./images/ann3.PNG")
#set_background("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")

#with st.container():
    #st.image("https://jnnprogress.com/Site/Home_files/banner.jpg")
    #st.image("https://www.jnnprogress.com/Site/Hitachi/images/Depot.PNG")    
    

