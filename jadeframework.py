import cv2
import streamlit as st


class EngZone:
    def __init__(self,name, startpoint, endpoint, color, thickness ):
        self.name = name
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.color = color
        self.thickness = thickness

#Color

#Const
DPTK201 = EngZone('TK201', (80,159) , (616,158) , (0,255,0) , 10)
DPTK2012 = EngZone('TK201', (80,209) , (649,209) , (0,255,0) , 10)
DPTK2013 = EngZone('TK201', (80,251) , (600,251) , (0,255,0) , 10)
DPTK2014 = EngZone('TK201', (616,158) , (715,303) , (0,255,0) , 10)
DPTK2015 = EngZone('TK201', (600,251) , (623,302) , (0,255,0) , 10)

#Section 2
DPTK204 = EngZone('TK204', (80,302) , (715,302) , (255,0,0) , 10)
DPTK2042 = EngZone('TK204', (80,351) , (690,351) , (255,0,0) , 10)
DPTK2043 = EngZone('TK204', (690,351) , (715,399) , (255,0,0) , 10)
DPTK2044 = EngZone('TK204', (80,399) , (715,399) , (255,0,0) , 10)

#Section 3
DPTK207 = EngZone('TK207', (80,448) , (600,448) , (0,0,255) , 10)
DPTK2072 = EngZone('TK207', (600,448) , (629,495) , (0,0,255) , 10)
DPTK2073 = EngZone('TK207', (80,495) , (629,495) , (0,0,255) , 10)


#Section 4 Test track
DPTT1 = EngZone('TT', (15,58), (1775,58) , (0,255,0) ,10)
DPTT2 = EngZone('TT', (1226,301), (1348,58), (0,255,0) ,10)
#DPTK

def testfunction():
        st.markdown("# Call test function ")

def Highlight(image, zone):
    
    if zone==DPTK201.name :      
        cv2.line(image,DPTK201.startpoint,DPTK201.endpoint,DPTK201.color, DPTK201.thickness)    
        cv2.line(image,DPTK2012.startpoint,DPTK2012.endpoint,DPTK2012.color, DPTK2012.thickness) 
        cv2.line(image,DPTK2013.startpoint,DPTK2013.endpoint,DPTK2013.color, DPTK2013.thickness) 
        cv2.line(image,DPTK2014.startpoint,DPTK2014.endpoint,DPTK2014.color, DPTK2014.thickness) 
        cv2.line(image,DPTK2015.startpoint,DPTK2015.endpoint,DPTK2015.color, DPTK2015.thickness) 
    if zone==DPTK201.name :      
        cv2.line(image,DPTK204.startpoint,DPTK204.endpoint,DPTK204.color, DPTK204.thickness)    
        cv2.line(image,DPTK2042.startpoint,DPTK2042.endpoint,DPTK2042.color, DPTK2042.thickness) 
        cv2.line(image,DPTK2043.startpoint,DPTK2043.endpoint,DPTK2043.color, DPTK2043.thickness) 
        cv2.line(image,DPTK2044.startpoint,DPTK2044.endpoint,DPTK2044.color, DPTK2044.thickness)
    if zone==DPTK201.name :      
        cv2.line(image,DPTK207.startpoint,DPTK207.endpoint,DPTK207.color, DPTK207.thickness)    
        cv2.line(image,DPTK2072.startpoint,DPTK2072.endpoint,DPTK2072.color, DPTK2072.thickness) 
        cv2.line(image,DPTK2073.startpoint,DPTK2073.endpoint,DPTK2073.color, DPTK2073.thickness) 
    if zone==DPTK201.name :      
        cv2.line(image,DPTT1.startpoint,DPTT1.endpoint,DPTT1.color, DPTT1.thickness)    
        cv2.line(image,DPTT2.startpoint,DPTT2.endpoint,DPTT2.color, DPTT2.thickness) 
        
    #cv2.line(image, startpoint , endpoint  , color , thickness )
    return image

    
