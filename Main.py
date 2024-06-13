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
    position: relative; /* Ensure the container is positioned */
    z-index: 0; /* Ensure the stacking context is correct */
}
[data-testid="stAppViewContainer"] > .main::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('https://www.jnnprogress.com/Site/Hitachi/images/interior2.png');
    background-size: 100vw 100vh;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.1; /* Set the opacity of the background image */
    z-index: -1; /* Place the pseudo-element behind the main content */
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

st.markdown("# Welcome to Sanying Possession Plan")

#Google connect
gsheetid = "1BevBgtAvlLvOqmHOBdH2Z1b0XdXmoYTx"    
sheet_name = "WeeklyInfo"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

connFailed = False
try:
    Maindf = pd.read_csv(gsheet_url)
except pd.errors.EmptyDataError:
        #print("The CSV file is empty.")
        connFailed = True
except pd.errors.ParserError:
        #print("Error parsing the CSV file.")
        connFailed = True
except Exception as e:
        #print(f"An error occurred: {e}")
        connFailed = True


#get max data
if connFailed == False:
    Annmessage =""
    TCOnumber =""
    warningmsg =""
    for index, row in Maindf.iterrows():
        if (index>1) and (str(row['Info1']) != "nan") and (index<8):
            Annmessage = Annmessage + str(row['Info1']) + "\n\n"
        if index == 8:
            TCOnumber = str(row['Info1'])
        if index == 9:
            warningmsg = str(row['Info1'])
    st.info(Annmessage)
    st.error(TCOnumber)

    st.warning(warningmsg)
else:
     st.error("Google drive connection failed")
#ann3 =  Image.open("./images/ann3.PNG")
#set_background("./images/ann3.PNG")
#set_background("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")

#with st.container():
    #st.image("https://jnnprogress.com/Site/Home_files/banner.jpg")
    #st.image("https://www.jnnprogress.com/Site/Hitachi/images/Depot.PNG")    
    

