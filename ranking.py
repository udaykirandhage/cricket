import streamlit as st
import pandas as pd
from PIL import Image
from urllib.request import Request,urlopen

req = Request('https://sports.ndtv.com/cricket/icc-rankings',headers={'User-Agent':'Chrome/5.0'})
webpage=urlopen(req)
data=pd.read_html(webpage,header=0)


image = Image.open('ICC.jpg')
st.image(image, width=300)
st.title('ICC Ranking')
st.markdown('This app Shows the Ranking of ICC ')



# About
expander_bar = st.expander('About')
expander_bar.markdown("""
* **Made By:** <MD Uday Kiran , Vasihnavi,Vamshi,Nandhini>
* **Data source:** [NDTv](https://sports.ndtv.com/cricket/icc-rankings).
""")

menu1=["Player","Team"]
a=st.sidebar.selectbox("Select ",menu1)
if a=="Team":
    menu2=["Test","ODI","T20"]
    b=st.sidebar.selectbox("Match Type",menu2)
    st.markdown('Select the Match Type From The Select Box')
    st.markdown('___________________________________________________________________________')
    if b=="Test":
        st.markdown('Here is The data for You about The Test Matches That went On ')
        df=data[0]
        st.dataframe(df)
    #style.set_properties(**{'background-color':'black','color':'white'})
    if b=="ODI":
        st.markdown('Here is The data for You about The ODI Matches That went On ')
        df=data[4]
        st.dataframe(df)
    if b=="T20":
        st.markdown('Here is The data for You about The T20 Matches That went On ')
        df=data[8]
        st.dataframe(df)
if a=="Player":
    menu3=["Test","ODI","T20"]
    b=st.sidebar.selectbox("Select Match Type",menu3)
    
    if b=="Test":
        image = Image.open('test.jpg')
        st.image(image, width=80)
        st.markdown('Here is your Top 10 Players list in T20')
        menu4=["Batting","Bowling","All Rounder"]
        c=st.selectbox("Select The Player Type",menu4)
        if c=="Batting":
            df=data[1]
            st.dataframe(df)
        if c=="All Rounder":
            df=data[3]
            st.dataframe(df)
        if c=="Bowling":
            df=data[2]
            st.dataframe(df)
    if b=="ODI":
        menu5=["Batting","Bowling","All Rounder"]
        c=st.selectbox("Select The Player Type",menu5)
        image = Image.open('odi.jpg')
        st.image(image, width=80)
        st.markdown('Here is your Top 10 Players list in T20')
        if c=="Batting":
            df=data[5]
            st.dataframe(df)
        if c=="All Rounder":
            df=data[7]
            st.dataframe(df)
        if c=="Bowling":
            df=data[6]
            st.dataframe(df)
    if b=="T20":
        menu5=["Batting","Bowling","All Rounder"]
        c=st.selectbox("Select",menu5)
        image = Image.open('T20.png')
        st.image(image, width=80)
        st.markdown('Here is your Top 10 Players list in T20')
        if c=="Batting":
            df=data[9]
            st.dataframe(df)
        if c=="All Rounder":
            df=data[10]
            st.dataframe(df)
        if c=="Bowling":
            df=data[11]
            st.dataframe(df)
