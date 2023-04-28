import streamlit as st
import pandas as pd
import lxml
from PIL import Image
from urllib.request import Request,urlopen
from streamlit_option_menu import option_menu



st.set_page_config(page_title="ICC",layout="wide")

#ackgroundColor

page_bg_img ="""
 <style>
 [data-testid="stAppViewContainer"]{

 }
 [data-testid="stHeader"]{

 }
 </style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

req = Request('https://sports.ndtv.com/cricket/icc-rankings',headers={'User-Agent':'Mozilla/5.0'})
webpage=urlopen(req)
data=pd.read_html(webpage,header=0)


req2= Request('https://www.icc-cricket.com/rankings/womens/team-rankings/odi',headers={'User-Agent':'Mozilla/5.0'})
webpage=urlopen(req2)
data1=pd.read_html(webpage,header=0)

req3= Request('https://www.icc-cricket.com/rankings/womens/team-rankings/t20i',headers={'User-Agent':'Mozilla/5.0'})
webpage2=urlopen(req3)
data2=pd.read_html(webpage2,header=0)









req4= Request('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting',headers={'User-Agent':'Mozilla/5.0'})
webpage3=urlopen(req4)
data3=pd.read_html(webpage3,header=0)

req5= Request('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling',headers={'User-Agent':'Mozilla/5.0'})
webpage4=urlopen(req5)
data4=pd.read_html(webpage4,header=0)

req6= Request('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder',headers={'User-Agent':'Mozilla/5.0'})
webpage5=urlopen(req6)
data5=pd.read_html(webpage5,header=0)


        #Iam scrapping the for T20 womens here from ICC cricket

req7= Request('https://www.icc-cricket.com/rankings/womens/player-rankings/t20i/batting',headers={'User-Agent':'Mozilla/5.0'})
webpage6=urlopen(req7)
data6=pd.read_html(webpage6,header=0)

req8= Request('https://www.icc-cricket.com/rankings/womens/player-rankings/t20i/bowling',headers={'User-Agent':'Mozilla/5.0'})
webpage7=urlopen(req8)
data7=pd.read_html(webpage7,header=0)

req9= Request('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder',headers={'User-Agent':'Mozilla/5.0'})
webpage8=urlopen(req9)
data8=pd.read_html(webpage8,header=0)


# Nav bar creation 

selectedNavbar=option_menu(menu_title=None,options=["Home","Awards","Results","Contact-Us","Hall of Fame"],orientation="horizontal",default_index=0,styles={
        "container": {"padding": "5!important","width":"100vw"},
        "icon": {"color": "orange", "font-size": "10px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#E9DCCF"}},)













st.title('ICC Ranking')
st.markdown('This app Shows the Ranking of ICC ')



# About
expander_bar = st.expander('About')
expander_bar.markdown("""
* **Made By:** <MD Uday Kiran , Vasihnavi,Vamshi,Nandhini>
* **Data source:** [NDTv , Icc Cricket](https://sports.ndtv.com/cricket/icc-rankings).
""")
if selectedNavbar =="Home":
    st.sidebar.title("Use These Below Options To View Your Data")
    menu0=["Male Team","Female Team"]
    d=st.sidebar.selectbox("Select ",menu0)
    if d=="Male Team":
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
                image = Image.open('test.png')
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
                image = Image.open('odi.png')
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
    
    if d=="Female Team":
        menugirls=["Player","Team"]
        e=st.sidebar.selectbox("Select ",menugirls)
        if e=="Team":
            menugirls2=["ODI","T20"]
            f=st.sidebar.selectbox("Match Type",menugirls2)
            st.markdown('Select the Match Type From The Select Box')
            st.markdown('___________________________________________________________________________')
            if f=="T20":
                st.markdown('Here is The data for You about The T20 Matches That went On ')
                df=data2[0]
                st.dataframe(df)
            if f=="ODI":
                st.markdown('Here is The data for You about The ODI Matches That went On ')
                df=data1[0]
                st.dataframe(df,width=900)
        if e=="Player":
            menugirls3=["ODI","T20"]
            f=st.sidebar.selectbox("Select Match Type",menugirls3)
            if f=="ODI":
                image = Image.open('odi.png')
                st.image(image, width=80)
                st.markdown('Here is your  Players list in ODI')
                menugirls4=["Batting","Bowling","All Rounder"]
                g=st.selectbox("Select The Player Type",menugirls4)
                st.markdown('___________________________________________________________________________')
                if g=="Batting":
                    df=data3[0]
                    st.dataframe(df)
                if g=="All Rounder":
                    df=data5[0]
                    st.dataframe(df)
                if g=="Bowling":
                    df=data4[0]
                    st.dataframe(df)
            if f=="T20":
                image = Image.open('T20.png')
                st.image(image, width=80)
                st.markdown('Here is your Players list in T20')
                menugirls4=["Batting","Bowling","All Rounder"]
                g=st.selectbox("Select The Player Type",menugirls4)
                if g=="Batting":
                    df=data6[0]
                    st.dataframe(df)
                if g=="All Rounder":
                    df=data8[0]
                    st.dataframe(df)
                if g=="Bowling":
                    df=data7[0]
                    st.dataframe(df)
















#navbar vertical in side bar
with st.sidebar:
        selected=option_menu(menu_title=None,options=["Store","Faqs","News","Donate","Match Highlights"],orientation="vertical",default_index=0,styles={
            "container": {"padding": "0!important","width":"100vw"},
            "icon": {"color": "orange", "font-size": "10px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"}},) 
        
    

if selectedNavbar == "Contact-Us":
    st.write()
    
    st.header(":mailbox: Customer Support")
    contact_form="""
    <form action="https://formsubmit.co/udaykirandhage@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name"  placeholder="Your Name"required>
        <input type="email" name="email" placeholder="Your Gmail" required>
        <input type="text" name="number" placeholder="Your Number" required>
        <textarea name="Address" placeholder=" Enter Your Address"></textarea>
        <button type="submit">Send</button>
    </form> """
    st.markdown(contact_form,unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    local_css("style.css")


