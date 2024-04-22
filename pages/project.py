
import streamlit as st
from PIL import Image
import cv2
import pandas as pd

st.title("project")

st.write("Hello second")
my_input = st.text_input("Input a text here","default text")

submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write ("you have enter :", my_input)

#image = Image.open('\\D\\testimage.PNG')
image = cv2.imread('images\\Depot.PNG')
#image = Image.open('testimage.PNG')
startpoint = (20,207)
endpoint = (210,207)
color = (0,255,0)
thickness = 2
cv2.line(image, startpoint , endpoint  , color , thickness )

df = pd.DataFrame({"Par":["Apple","Strawberry","Banana"],"Cat1":["good","good","bad"],"Cat2":["healthy","no","unhealthy"]})

st.dataframe(df,hide_index=1)

filterdata = "good"

st.dataframe(df[df['Cat1'] == filterdata])

df2 = df[df['Cat1'] == filterdata]

for i, row in df2.iterrows():
    if row['Cat2'] == 'healthy':
        st.write ('it is healthy')

gsheetid = "1J8RjbrDw86ubi6BDnE_t2-XgxkpmgI8I1U4bN3GmEgc"    
sheet_name = "Possession"
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df3 = pd.read_csv(gsheet_url)
#df3.head()
#df3

st.dataframe(df3[df3['Descritpion'] == "Duby"])


#def (image, Z1)
# array of string ("z1","z2") foreach and def(image,Z1)


st.image(image, caption='Test image')