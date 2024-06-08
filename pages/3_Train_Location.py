import streamlit as st
import cv2
import numpy as np
from jadeframework import *
import pandas as pd
import re

TRAINICON = cv2.imread("./images/trainIcon2.png",cv2.IMREAD_UNCHANGED)

st.set_page_config(
    page_title="TCO Train Location",
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


col1, col2 = st.columns(2)

with col1 :
    st.markdown("# Sanying TCO Train Location")

with col2 :
    C1,C2 = st.columns(2)

    if "login" in st.session_state :
        if st.session_state.login:
            st.write("Edit Mode")
        else :
            st.write("Login Failed")        

    else :
        with C1:
            st.session_state.user = st.text_input("user",value="admin",label_visibility="hidden")
        with C2:
            st.write("")
            st.write("")
            if st.button("Submit") :    
                if st.session_state.user == 'jade':            
                    st.write("Login Successful")
                    st.session_state.login = True
                else :
                    st.session_state.login = False


# Option in form
with st.form("Modify train loc",clear_on_submit=True):
    if st.session_state.user == 'jade':    
        c11,c12,c13 = st.columns(3)
        with c11:
            TrainSelect = st.selectbox("Train ID",("EMU101","EMU102","EMU103"))
        with c12:
            ParkingLoc = st.selectbox("Parking",("201_1","201_0"))
        with c13:
            st.write("")
            st.write("")
            from_sub = st.form_submit_button("Modtrain")

## Method#1, Retrive database
gsheetid = "1BevBgtAvlLvOqmHOBdH2Z1b0XdXmoYTx"    
sheet_name = "TrainLocation"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
Maindf = pd.read_csv(gsheet_url)

Parking = ParkCol()
Maindf = Maindf.reset_index()

#read data
for index,tid in Maindf.iterrows():     
    #st.write(tid['Train ID'], tid['Parking Location'] )
    Emu = tid['Train ID']
    parkLoc = tid['Parking Location']

#regex
    pattern = r"TK(\d+)_([0-9]+)"
    match = re.search(pattern, str(parkLoc))
    if match:
        Tr = match.group(1)
        Pos = match.group(2)
        Parking.add(Park(parkLoc,int(Tr),int(Pos),int(Emu),True))


#Parx = Park('TK201_1',201, 1, 101, True)
#Parking.add(Park('TK201_1',201, 1, 101, True))
#Parking.add(Park('TK201_2',201, 2, 102, True))

# Image run
Layout = cv2.imread("./images/TrainLoc.PNG")



#add train to gsheet and layout
TRAINICON = cv2.imread("./images/trainIcon2.png",cv2.IMREAD_UNCHANGED)

for pid in Parking:
    #Add train ID
    trainicon = None
    trainicon = add_text_to_image(TRAINICON,str(pid.train),(60,90))
    st.write(pid)
    trainicon = resize_image(trainicon,40)
    #fill data in
    Layout = filltrain(Layout,trainicon,pid.track,pid.pos)

st.image(Layout,use_column_width=True)
