import streamlit as st
import cv2
import pandas as pd
import datetime
from jadeframework import *
from streamlit_gsheets import GSheetsConnection


## Method#1, Retrive database
#gsheetid = "1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc"    
#sheet_name = "Possession"
#gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
#Maindf = pd.read_csv(gsheet_url)

## Method#2, firewall proof
url = "https://docs.google.com/spreadsheets/d/1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
Maindf = conn.read(spreadsheet=url)
##Highlight

#Header
#st.write("Depot Possession : 你好" )
st.markdown("# Depot Possesion ")
st.markdown("| abc | defghi |")
st.markdown("### Approved Possession as date ##-Jan-24")
#Date Picker
today = datetime.date.today()


#with Col2:
#    st.write('Today :', today)

Col1,Col2,Col3,Col4 = st.columns(4)

with Col2:
    workingshift = st.select_slider('Select Working Shift', options = ['Morning','Afternoon','Night'], value = ('Morning'))
with Col1:
    #st.write('Selected date :', select_date)
    select_date  = Col1.date_input('Start Date',value=today,min_value=today)

#to work on min/max day
#onchange of date select

#Filtering
#df2 = df[df['Cat1'] == filterdata]
ProcessedDF = Maindf
for row_name, i in ProcessedDF.iterrows():
    #st.write(i.Subsystem)    
    row_startdate = i['Start(Date)']
    row_enddate = i['Finish(Date)']
    robj_startdate = datetime.datetime.strptime(row_startdate,'%d-%b-%y')    
    robj_startdate = robj_startdate.date()
    robj_enddate = datetime.datetime.strptime(row_enddate,'%d-%b-%y')
    robj_enddate = robj_enddate.date()
    #st.write(robj_startdate, robj_enddate)
    if select_date >= robj_startdate and select_date <= robj_enddate :
        #st.write("Selected : ", row_name)
        ProcessedDF = ProcessedDF.drop(row_name)

#Main layout
Layout = cv2.imread("images\\Depot.PNG")
Layout = Highlight(Layout,"TK201")
st.image(Layout)


#Main Table shift #1
#st.dataframe(Maindf,hide_index=True)
testfunction()
st.dataframe(ProcessedDF,hide_index=True)

#Main table shift #2

#main Table shift #3