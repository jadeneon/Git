import cv2
import streamlit as st
import requests
import numpy as np
from io import BytesIO

class EngZone:
    def __init__(self,name, startpoint, endpoint, color, thickness ):
        self.name = name
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.color = color
        self.thickness = thickness

#Color

class Park:
    def __init__(self, name='', track=0, pos=0,train = 0, occupied = False):
        self.name = name
        self.track = track
        self.pos = pos
        self.train = train
        self.occupied = occupied

    def __repr__(self):
        return f"Park(name='{self.name}', track={self.track}, pos={self.pos}, train={self.train}, occupied={self.occupied} )"

class Parks:
    def __init__(self):
        self.Parks = {}

    def __getitem__(self, key):
        # Allow dictionary-like access to student instances
        if key not in self.Parks:
            self.Parks[key] = Park()  # Create a new Student instance if it doesn't exist
        return self.Parks[key]

    def __setitem__(self, key, value):
        # Allow dictionary-like setting of student instances
        self.Parks[key] = value

    def __delitem__(self, key):
        # Allow dictionary-like deletion of student instances
        if key in self.Parks:
            del self.Parks[key]

    def __contains__(self, key):
        # Allow usage of 'in' keyword to check if a student exists
        return key in self.Parks

#Const
DPTK201 = EngZone('DPTK201', (80,159) , (616,158) , (255,0,0) , 10)
DPTK2012 = EngZone('DPTK201', (80,209) , (649,209) , (255,0,0) , 10)
DPTK2013 = EngZone('DPTK201', (80,251) , (600,251) , (255,0,0) , 10)
DPTK2014 = EngZone('DPTK201', (616,158) , (715,303) , (255,0,0) , 10)
DPTK2015 = EngZone('DPTK201', (600,251) , (623,302) , (255,0,0) , 10)

#Section 2
DPTK204 = EngZone('DPTK204', (80,302) , (715,302) , (255,0,0) , 10)
DPTK2042 = EngZone('DPTK204', (80,351) , (690,351) , (255,0,0) , 10)
DPTK2043 = EngZone('DPTK204', (690,351) , (715,399) , (255,0,0) , 10)
DPTK2044 = EngZone('DPTK204', (80,399) , (715,399) , (255,0,0) , 10)

#Section 3
DPTK207 = EngZone('DPTK207', (80,448) , (600,448) , (255,0,0) , 10)
DPTK2072 = EngZone('DPTK207', (600,448) , (629,495) , (255,0,0) , 10)
DPTK2073 = EngZone('DPTK207', (80,495) , (629,495) , (255,0,0) , 10)

#Section 4 Test track
DPTT = EngZone('DPTT', (15,58), (1775,58) , (255,0,0) ,10)
DPTT1 = EngZone('DPTT', (1226,301), (1348,58), (255,0,0) ,10)
#DPTK

#Section 5 Fan Area
Fan1 = EngZone('Fan', (601,105) , (1950,105) , (255,0,0) , 10)
Fan2 = EngZone('Fan', (1950,105) , (1950,965) , (255,0,0) , 10)
Fan3 = EngZone('Fan', (1950,965) , (601,965) , (255,0,0) , 10)
Fan4 = EngZone('Fan', (601,965) , (601,105) , (255,0,0) , 10)

def testfunction():
        st.markdown("# Call test function ")



def Highlight(image, zone):
    
    if zone==DPTK201.name :      
        cv2.line(image,DPTK201.startpoint,DPTK201.endpoint,DPTK201.color, DPTK201.thickness)    
        cv2.line(image,DPTK2012.startpoint,DPTK2012.endpoint,DPTK2012.color, DPTK2012.thickness) 
        cv2.line(image,DPTK2013.startpoint,DPTK2013.endpoint,DPTK2013.color, DPTK2013.thickness) 
        cv2.line(image,DPTK2014.startpoint,DPTK2014.endpoint,DPTK2014.color, DPTK2014.thickness) 
        cv2.line(image,DPTK2015.startpoint,DPTK2015.endpoint,DPTK2015.color, DPTK2015.thickness) 
    if zone==DPTK204.name :      
        cv2.line(image,DPTK204.startpoint,DPTK204.endpoint,DPTK204.color, DPTK204.thickness)    
        cv2.line(image,DPTK2042.startpoint,DPTK2042.endpoint,DPTK2042.color, DPTK2042.thickness) 
        cv2.line(image,DPTK2043.startpoint,DPTK2043.endpoint,DPTK2043.color, DPTK2043.thickness) 
        cv2.line(image,DPTK2044.startpoint,DPTK2044.endpoint,DPTK2044.color, DPTK2044.thickness)
    if zone==DPTK207.name :      
        cv2.line(image,DPTK207.startpoint,DPTK207.endpoint,DPTK207.color, DPTK207.thickness)    
        cv2.line(image,DPTK2072.startpoint,DPTK2072.endpoint,DPTK2072.color, DPTK2072.thickness) 
        cv2.line(image,DPTK2073.startpoint,DPTK2073.endpoint,DPTK2073.color, DPTK2073.thickness) 
    if zone==DPTT.name :      
        cv2.line(image,DPTT.startpoint,DPTT.endpoint,DPTT.color, DPTT.thickness)    
        cv2.line(image,DPTT1.startpoint,DPTT1.endpoint,DPTT1.color, DPTT1.thickness) 
    if zone==Fan1.name :
        cv2.line(image,Fan1.startpoint,Fan1.endpoint,Fan1.color, Fan1.thickness)    
        cv2.line(image,Fan2.startpoint,Fan2.endpoint,Fan2.color, Fan2.thickness) 
        cv2.line(image,Fan3.startpoint,Fan3.endpoint,Fan3.color, Fan3.thickness) 
        cv2.line(image,Fan4.startpoint,Fan4.endpoint,Fan4.color, Fan4.thickness)
        
    #cv2.line(image, startpoint , endpoint  , color , thickness )
    return image

def resize_image(image, scale_percent):
    # Calculate the new dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)
    # Resize the image
    resized_image = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)
    return resized_image

def add_text_to_image(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, 
                      font_scale=1, color=(0,0,0) , thickness=6):

    if image is None:
        st.error("Image is None. Cannot add text to a NoneType object.")
        return None

    if image.shape[2] == 4:  # Check if image has an alpha channel
        # Split the image into RGB and Alpha channels
        bgr_image = image[:, :, :3]
        alpha_channel = image[:, :, 3]
        # Add text to the BGR image
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
        cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        #cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        # Merge the BGR image and alpha channel back together
        #result_image = cv2.merge((bgr_image, alpha_channel))
        result_image = image
    else:
        # Add text directly if there is no alpha channel
        cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        result_image = image

    return result_image


def filltrain(layout,icon, x,y):
     
     return layout

def IDadd(icon,id):
    #icon = np.zeros((512,512,3), np.uint8)
    # Write some Text
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (0,0)
    fontScale              = 1
    fontColor              = (0,0,0)
    thickness              = 2
    lineType               = 2

    cv2.putText(icon,str(id), 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        thickness,
        cv2.LINE_AA)
    return icon
