import streamlit as st
import cv2
import numpy as np

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

col1, col2, col3 = st.columns(3)

with col1 :
    st.markdown("# Train Location")

with col3 :
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


# Image run
Layout = cv2.imread("./images/Depot.PNG")
trainicon = cv2.imread("./images/trainnobg.png",cv2.IMREAD_UNCHANGED)

if trainicon.shape[2] == 4:
    # Split the foreground image into color and alpha channels
    fg_color = trainicon[:, :, :3]
    alpha = trainicon[:, :, 3] / 255.0
else:
    # If no alpha channel, create a mask with full opacity
    fg_color = trainicon
    alpha = np.ones(trainicon.shape[:2], dtype=float)

x_offset=y_offset=150

y1, y2 = y_offset, y_offset + fg_color.shape[0]
x1, x2 = x_offset, x_offset + fg_color.shape[1]

for c in range(0, 3):
        Layout[y1:y2, x1:x2, c] = (alpha[:y2-y1, :x2-x1] * fg_color[:y2-y1, :x2-x1, c] +
                                       (1 - alpha[:y2-y1, :x2-x1]) * Layout[y1:y2, x1:x2, c])


#Layout[y_offset:y_offset + trainicon.shape[0], x_offset:x_offset+trainicon.shape[1]] = trainicon

st.image(Layout)

#import cv2
#s_img = cv2.imread("smaller_image.png")/
#l_img = cv2.imread("larger_image.jpg")
#x_offset=y_offset=50
#l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img