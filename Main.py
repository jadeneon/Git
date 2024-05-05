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

#set_background('images\interior.PNG')

#print ("perfect") #console print
#st.title("MainPage")

#st.sidebar.success("select page above")
#testimage = cv2.imread(r'images\Ann2.PNG')
#imagi = Image.open(r'images/Ann2.PNG')
#numpydata = numpy.asarray(imagi)
#startpoint = (20,207)
#endpoint = (210,207)
#color = (255,255,0)
#thickness = 2
#photo = numpydata.copy()
#photo.setflags(write=1)
#cv2.line(photo, startpoint , endpoint  , color , thickness )
#st.image(photo)


st.markdown("# Announce date // 11-Dec-2023 test")
ann3 =  Image.open("./images/ann3.png")

with st.container():
    #st.image("https://jnnprogress.com/Site/Home_files/banner.jpg")
    st.image("https://www.jnnprogress.com/Site/Hitachi/images/Depot.PNG")
    st.image(ann3)
    

