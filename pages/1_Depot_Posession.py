import PIL.Image
import streamlit as st
import pandas as pd
import datetime
import cv2
import requests
import numpy as np
import urllib.request
import urllib
from io import BytesIO
from jadeframework import *
from PIL import Image

st.set_page_config(
    page_title="Depot Possesion",
    layout="wide",
    page_icon = "🧊"
    # page_icon=Hitachi_logo    
)

## Method#1, Retrive database
gsheetid = "1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc"    
sheet_name = "Possession"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
Maindf = pd.read_csv(gsheet_url)

## Method#2, firewall proof
#url = "https://docs.google.com/spreadsheets/d/1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc/edit?usp=sharing"
#conn = st.connection("gsheets", type=GSheetsConnection)
#Maindf = conn.read(spreadsheet=url)
##Highlight

#Header
today = datetime.date.today()
#st.write("Depot Possession : 你好" )
st.markdown("# Depot Possesion ")
st.markdown(f"""## Approved Possession as date {today} for Week  {today.isocalendar().week}""", unsafe_allow_html=True)
#Date Picker

#with Col2:
#    st.write('Today :', today)

Col1,Col2,Col3,Col4 = st.columns(4)

with Col2:
    selectedworkingshift = st.select_slider('Select Working Shift', options = ['Morning','Afternoon','Night'], value = ('Morning'))
with Col1:
    #st.write('Selected date :', select_date)
    #select_date  = Col1.date_input('Start Date',value=today,min_value=today)    
    select_date  = Col1.date_input('Start Date',value=today)    
match selectedworkingshift:
    case    'Morning':
        translatedworkingshift = 'SH1'
    case    'Afternoon':
        translatedworkingshift = 'SH2'
    case    'Night':
        translatedworkingshift = 'SH3'

#to work on min/max day
#onchange of date select

#Filtering
#df2 = df[df['Cat1'] == filterdata]

ProcessedDF = Maindf
for row_name, i in ProcessedDF.iterrows():
    #date filtering     
    row_startdate = i['Start(Date)']
    row_enddate = i['Finish(Date)']
    robj_startdate = datetime.datetime.strptime(row_startdate,'%d-%b-%y')    
    robj_startdate = robj_startdate.date()
    robj_enddate = datetime.datetime.strptime(row_enddate,'%d-%b-%y')
    robj_enddate = robj_enddate.date()

    row_workingshift = i['Working.Shift']
    workingShiftFilter = row_workingshift.split(",")

    if select_date < robj_startdate or select_date > robj_enddate :        
        ProcessedDF = ProcessedDF.drop(row_name)
    else : 
        if translatedworkingshift not in workingShiftFilter :
            ProcessedDF = ProcessedDF.drop(row_name)
        
    #shiftfitering

#Main layout

#url = 'https://www.jnnprogress.com/Site/gtest.png'
#url = 'https://img.creative.com/images/products/large/pdt_23968.png'
#url = 'https://www.google.co.th/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
#resp = requests.get(url)
#img = BytesIO(resp.content)
#img2 = Image.open(img)
#img = Image.open('images\Ann2.PNG')
#img2 = img.copy()
#resp = urllib.urlopen(url)
#image = np.asarray(bytearray(resp.read()), dtype="uint8")
#Layout = cv2.imdecode(image, cv2.IMREAD_COLOR)
#Layout = cv2.cvtColor(Layout, cv2.COLOR_BGR2RGB)
#Layout = Image.open(resp)
Layout = cv2.imread("./images/Depot.PNG")

for row_name, i in ProcessedDF.iterrows():
 row_PowerZone = i['PowerZone']
 workingPowerZoneFilter = row_PowerZone.split(",")
 for pow in workingPowerZoneFilter:
    if pow not in ('Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8') :        
        Layout = Highlight(Layout,pow)

st.image(Layout)

#Main Table shift #1
#st.dataframe(Maindf,hide_index=True)
#testfunction()
st.markdown(" ### Approved Works List")
#st.dataframe(ProcessedDF,hide_index=True)
st.dataframe(ProcessedDF,hide_index=True,column_order=("Date", "Start(Area)","Start(Date)","Energization","PowerZone"))

#Main table shift #2

#main Table shift #3