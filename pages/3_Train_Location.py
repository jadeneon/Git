import streamlit as st
import cv2
import numpy as np
from jadeframework import *
import gspread
#from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import re

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
            from_sub = st.form_submit_button("Modtrain")

## Method#1, Retrive database
gsheetid = "1BevBgtAvlLvOqmHOBdH2Z1b0XdXmoYTx"    
sheet_name = "TrainLocation"
#key_file_path = "./cre/servicekey.json"
#scope = [
#    'https://www.googleapis.com/auth/drive'
#]
#credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_path, scope)
#client = gspread.authorize(credentials)

# Open the Google Sheet by its name
#sheet = client.open(sheet_name).sheet1  # Open the first sheet

# Read data from the sheet into a pandas DataFrame
#data = sheet.get_all_records()

gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
connFailed = False

try:
    Maindf = pd.read_csv(gsheet_url)
    #Maindf = pd.DataFrame(data)
except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
        connFailed = True
except pd.errors.ParserError:
        print("Error parsing the CSV file.")
        connFailed = True
except Exception as e:
        print(f"An error occurred: {e}")
        connFailed = True

#Connection Check
if connFailed == False:

    Parking = ParkCol()
    Maindf = Maindf.reset_index()

    #read data
    for index,tid in Maindf.iterrows():     
        #st.write(tid['Train ID'], tid['Parking Location'] )
        Emu = tid['Train ID']
        parkLoc = tid['Parking Location']

    #regex
        pattern = r"T(\d{2})"
        match = re.search(pattern, str(Emu))
        if match:
            EmuId = match.group(1)        
    
    #regex
        pattern = r"TK(\d+)_([0-9]+)"
        match = re.search(pattern, str(parkLoc))
        if match:
            Tr = match.group(1)
            Pos = match.group(2)
            Parking.add(Park(parkLoc,int(Tr),int(Pos),int(EmuId),True))          
    # TTK Location identification
        pattern = r"TT_PLAT(\d)"
        match = re.search(pattern, str(parkLoc))
        if match:
            Tr = 0
            Pos = match.group(1)
            Parking.add(Park(parkLoc,int(Tr),int(Pos),int(EmuId),True))          

    #Image run
    Layout = cv2.imread("./images/TrainLoc.PNG")

    #add train to gsheet and layout
    for pid in Parking:
        #Add train ID
        trainicon = cv2.imread("./images/trainIcon3.png",cv2.IMREAD_UNCHANGED)
        tprefix = "T"
        if pid.train < 10:
             tprefix = "T0"
        trainicon = add_text_to_image(trainicon,tprefix+str(pid.train),(30,65))
        trainicon = resize_image(trainicon,40)
        #fill data in
        Layout = filltrain(Layout,trainicon,pid.track,pid.pos)

    st.image(Layout)
else:
     st.write("No google drive connection, Check your internet connection")