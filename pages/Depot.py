import streamlit as st
import streamlit_drawable_canvas as st_canvas
import cv2
import pandas as pd
import datetime

## Retrive database
gsheetid = "1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc"    
sheet_name = "Possession"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
Maindf = pd.read_csv(gsheet_url)

##Highi
#foreach highlighter

#Header
st.write("Depot Possessione : 你好" )


#Date Picker
today = datetime.date.today()
st.write('Today :', today)
select_date  = st.date_input('Start Date',value=today,min_value=today)
st.write('Selected date :', select_date)
#to work on min/max day
#onchange of date select

#Filtering
#df2 = df[df['Cat1'] == filterdata]
ProcessedDF = Maindf
for row_name, i in ProcessedDF.iterrows():
    #st.write(i.Subsystem)    
    row_startdate = i['Start(date)']
    row_enddate = i['End(date)']
    robj_startdate = datetime.datetime.strptime(row_startdate,'%d-%b-%Y')    
    robj_startdate = robj_startdate.date()
    robj_enddate = datetime.datetime.strptime(row_enddate,'%d-%b-%Y')
    robj_enddate = robj_enddate.date()
    #st.write(robj_startdate, robj_enddate)
    if select_date >= robj_startdate and select_date <= robj_enddate :
        #st.write("Selected : ", row_name)
        ProcessedDF = ProcessedDF.drop(row_name)

#Main layout
Layout = cv2.imread("images\\Depot.PNG")
st.image(Layout)


#Main Table
#st.dataframe(Maindf,hide_index=True)
st.dataframe(ProcessedDF,hide_index=True)
