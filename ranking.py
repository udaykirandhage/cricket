import streamlit as st
import pandas as pd
import lxml
from PIL import Image
from urllib.request import Request,urlopen
from streamlit_option_menu import option_menu
import json
from streamlit_lottie import st_lottie
import requests


st.set_page_config(page_title="ICC",layout="wide")

#backgroundColor

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

selectedNavbar=option_menu(menu_title=None,options=["Home","Highlights","About ICC","Contact-Us","Hall of Fame","Faqs"],orientation="horizontal",default_index=0,styles={
        "container": {"padding": "5!important","width":"100vw"},
        "icon": {"color": "orange", "font-size": "10px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#E9DCCF"}},)


#loading lottie files
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
lottie_hey=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_pVTLqHPbds.json")


st.header('ICC Ranking')
st.markdown('This app Shows the Ranking of ICC ')



# About
expander_bar = st.expander('About')
expander_bar.markdown("""
* **Made By:** <MD Uday Kiran , Vasihnavi,Vamshi,Nandhini>
* **Data source:** [NDTv , Icc Cricket](https://sports.ndtv.com/cricket/icc-rankings).
""")



if selectedNavbar =="Home":
    with st.sidebar:
        st.sidebar.title("Use These Below Options To View Your Data")
        st_lottie(lottie_hey,key="Hello")
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

if selectedNavbar =="Faqs":
    with st.sidebar:
        st.header("Faqs!")
        st.write("_____________________")
        st.write("Lets discuss the frequently asked questions!")
        
        lottie_faqs=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_zrw0ybu1.json")
        st_lottie(lottie_faqs,key="faq")
        st.write("_____________________")

    
    st.header ("Frequently Asked Questions about Player Rankings?")
    st.write("_________________________________________________________")
    expander_bar1 = st.expander('What do the rankings measure?')
    expander_bar1.markdown("""
        Think of the MRF Tyres ICC Rankings as a system for identifying the players who 
        could be selected for an ICC World XI if it was picked today. Take a look at the latest top tens, and you
          should find that most of the players at the top would be candidates for your current World XI. The rankings have often 
          been described as a measure of form, but this is a simplification. A form ranking would only look at what a player has done in 
          (say) the last year, whereas our rankings take into account a player's entire career - though they put more emphasis on what he or 
          she has done recently.
        """)
    expander_bar2 = st.expander('Whats the difference between rankings and ratings?')
    expander_bar2.markdown("""
        We use ‘rankings’ to refer to the positions of players in the tables, and ‘ratings’ to refer to their points.
        """)
    expander_bar3 = st.expander('How do you decide who is or is not included in the list?')
    expander_bar3.markdown("""
        Players have to have appeared in a match within the qualifying period to appear in the lists (normally 12-15 months for Tests, 9 -12 months 
        for T20s and ODIs). For example, Parthiv Patel lost his place in the Indian Test side in 2008 and disappeared from the lists in 2009. But 
        he retained a rating which slowly diminished as he missed matches. He was then picked again 2016 and returned to the rankings. If a player 
        confirms his retirement he is also removed from the list. So, for example, MS Dhoni retired from Tests in 2014 and was removed from the Test
          rankings - but he remained in the ODI tables. Players are in the rankings as soon as they complete 
        a match. However, we only publish the top 100 players (at most), so it can take several matches for a player to break into that
        """)
    expander_bar4 = st.expander('What happens to a players rating if he plays but does not bat/bowl?')
    expander_bar4.markdown("""
        If a batsman does not bat, his rating is unchanged. We don't want the ratings to punish a player when he
          hasn't done anything wrong (and it would be tough if, for example, rain wiped out an innings causing all the
            team to lose points). The situation with bowlers is slightly different. If the opposition are bowled out for 
            less than 150, then a bowler who has not bowled is not penalised (conditions obviously suited the other bowlers, and 
            his services weren't needed).
          But if the opposition makes a big total, then bowlers who don’t bowl in the innings lose points.
        """)
    expander_bar5= st.expander('What does it mean to have, say, 500 points?')
    expander_bar5.markdown("""
      Ratings points have a meaning in the same way as traditional averages do. Over 900
        points is a supreme achievement. Few players get there, and even fewer stay there for long.
        750 plus is normally enough to put a player in the world top ten. 500 plus is a good, solid rating.
        """)
    expander_bar5= st.expander('What about ratings for wicket-keepers?')
    expander_bar5.markdown("""
                               The challenge is to find a fair way of rating a keeper. You can't 
                               just rate him on catches and stumpings taken, since these are highly dependent on the bowler creating these chances
                                 (how many chances did Warne create for Healy, for example?) No accurate details are kept historically on missed chances, and in any case what 
                                 is a missed chance? So, as
                                 with other fielding skills, we won't attempt to produce a rating since we aren't convinced it would be credible.
        """)
    expander_bar6= st.expander('Who decides how good the pitch is?')
    expander_bar6.markdown("""Nobody does. There is a common misconception that there is an expert panel that sits down to assess
      the pitch in each match. In fact, all the Ratings calculations are based purely on the information in the scorecard (as you would find published
        online or in a newspaper). If both teams score 500 in each innings, the computer rates this as a high-scoring match in which run-making was relatively 
        easy, and therefore downgrades the value of runs scored. If both teams score 150, this indicates that runs were at a premium and a 
    player gets greater credit for scoring well in this game.
     
        """)
    expander_bar7= st.expander('How do you rate all-rounders?')
    expander_bar7.markdown("""
     We have devised an all-rounder index that gives a good indication of who the best all-rounders in the world are in Test and One Day cricket. 
     To obtain the index, simply take the player's batting and bowling points, multiply them together and divide by 1000. So a player with 800 batting and 0
       bowling gets an index of zero (because he can't bowl and therefore isn't an all-rounder!), 600 batting/200 bowling gets a rating of 120, and 400 batting/400
         bowling points gets a rating of 160. An index of 300 plus is world class. There are far more all-rounders in T20s and ODIs than Tests, but the same names 
         tend to appear high in both lists. Incidentally, this index does omit one important all-rounder skill, namely fielding. There is no satisfactory way of
           rating fielding skills statistically at present.
        """)
    expander_bar8= st.expander('Is it harder to score points against some of the lower ranked teams than it might be to score points against the higher teams?')
    expander_bar8.markdown("""Because the ratings take account of the opposition strength, there shouldn't be any obvious advantage to playing against any particular team. Of course that's not to say that certain individuals do seem to play better against certain opposition or on certain types of pitch.

        """)
    




        
    

if selectedNavbar == "Contact-Us":
    with st.sidebar:
        lottie_contactus=load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_qmaetdpn.json")
        st.write("____________________________________________")
        st.write("Any Queries or suggestions fill out this mail we would contact you as soon as possible !!!")
        st_lottie(lottie_contactus)
        st.write("____________________________________________")
        
        

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


if selectedNavbar =="Highlights":
    
    st.header("Highlights of the Match")
    st.write("Match Highlights")




    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_hello=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_pleodkag.json")
    lottie_match_highlights2=load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_l2focifi.json")
    

    

    col1,col2=st.columns(2)
    with st.sidebar:
        st.header("Watch The Highlights Here")
        st.markdown("________________________________________________________________________________________________________")

        st.write("""Watch all the latest match highlights Here and
                       For More Videos Click Here below............ """)
        st_lottie(lottie_match_highlights2,key="Match2")
      
        st.write("[Watch More >](https://www.youtube.com/@ICC)")

        st.markdown("________________________________________________________________________________________________________")
       
    with col1:
        st.video("https://www.youtube.com/watch?v=Kwu1yIC-ssg&list=PLtWkiFWAD1czNxQYv-ehzMxvO1V_hoHwe",start_time=1)
        st.video("https://www.youtube.com/watch?v=HOG6BV_neH0")
        st.video("https://www.youtube.com/watch?v=s8OJgjKlxnk")
        st.video("https://www.youtube.com/watch?v=aMBYUKJ8bug")
        st.video("https://www.youtube.com/watch?v=qUXsLbEcOqo")
        st.video("https://www.youtube.com/watch?v=JFwSKxGTpA4")

    with col2:
        st.video("https://www.youtube.com/watch?v=3TMjFJEE7cY",start_time=1)
        st.video("https://www.youtube.com/watch?v=S3FVVv-HkcU")
        st.video("https://www.youtube.com/watch?v=o4qnuo2Z8dQ")
        st.video("https://www.youtube.com/watch?v=XbeZIOBNn7Q")
        st.video("https://www.youtube.com/watch?v=DpuGzdb9VAI")
        st.video("https://www.youtube.com/watch?v=bpNMdtkspAE")

#
if selectedNavbar == "About ICC":
    with st.sidebar:
        st.header("About ICC")
        st.write("_______________________________________")
        st.write("Lets Know about ICC")
        lottie_aboutIcc=load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ve2idx3p.json")
        st_lottie(lottie_aboutIcc)
        st.write("_______________________________________")

     


    
    st.header('Introduction The ICC')
    image = Image.open('about ICC.jpg')
    st.write("_______________________________________")
    st.image(image, width=500)

    st.write("""

            The ICC is the global governing body for cricket. Representing 108 members, the ICC governs and administrates 
            the game and works with our members to grow the sport. The ICC is also responsible for the staging of all ICC Events.
            The ICC presides over the ICC Code of Conduct, playing conditions, the Decision Review System and other ICC regulations. The ICC also appoints all match officials that officiate at all sanctioned international matches.
            Through the Anti-Corruption Unit it coordinates action against corruption and match fixing.
    """)

    st.header('Our Vision ')
    st.write("_______________________________________")
    
    vision_image=Image.open('Vision.jpg')
    st.image(vision_image,width=500)
    st.write('The ICC has a long-term ambition for cricket to become the world’s favourite sport. We will lead the continued drive towards more competitive, entertaining, and meaningful cricket for players and fans. We will grow the sport by creating more opportunities for more people and nations to enjoy it and increase the competitiveness of international cricket at all levels. We will promote cricket by delivering exciting and engaging global events, attracting new and diverse fans, and building long-term successful commercial partnerships. And finally, we will continue to make considerable efforts to protect the integrity of the sport.')
    st.write("_______________________________________")


    st.header('ICC Development')
    st.write("_______________________________________")
    
    vision_image=Image.open('iccdevelopement.jpg')
    st.image(vision_image,width=500)
    st.write('There are 104 Member countries of the International Cricket Council (ICC). This includes 12 Full Members and 92 Associate Members.There are 104 Member countries of the International Cricket Council (ICC). This includes 12 Full Members and 92 Associate Members.The team are also responsible for implementing and administering the qualifying event structures and investment provided to the 92 Associate Member (AMs) countries by the ICC to assist the development of cricket across the globe through the ICC Development Funding Model.')
    st.write("_______________________________________")

    st.header('Our Partners')
    st.write("_______________________________________")
    
    vision_image=Image.open('iccpatners.jpg')
    st.image(vision_image,width=500)
    st.write('''The ICC Commercial programme aims to optimize revenues for the benefit of the game by delivering exciting, engaging global events that attract new and diverse fans and by building long-term successful commercial partnerships.
           The programme provides media owners and brands with powerful products and platforms to meaningfully engage a global audience (estimated currently at 2.5 billion with a projected 4.85 billion cumulative broadcast audience across 18 events from 2016-2023) – representing an unrivalled commercial product and platform delivering fan engagement, significant viewership reach, brand profile, increased sales and brand affinity opportunities
          The stories, values and emotive connections generated by cricket and delivered via broadcast, digital and social media in over 220 territories has led to 97% ‘recommendation’ and ‘preference’ for brands to sponsor and engage with cricket.
          The programme is managed in-house by an experienced team that oversees event delivery, sponsorships, brand licenses, broadcast production, media and digital rights, digital content and channels, marketing and overall commercial sales.''')
    st.write("_______________________________________")

if selectedNavbar =="Hall of Fame":
    col1,col2=st.columns(2)
    with col1:
        st.header("           Hall of Fame                      ")
        st.write('______________________________________________')
        highligh_image1=Image.open("h1.jpg")
        st.image(highligh_image1,width=400)
       
        st.write('______________________________________________')
        highligh_image2=Image.open("h2.jpg")
        st.image(highligh_image2,width=400)
        st.write('______________________________________________')
        highligh_image3=Image.open("h3.jpg")
        st.image(highligh_image3,width=400)
        st.write('______________________________________________')
        highligh_image4=Image.open("h4.jpg")
        st.image(highligh_image4,width=400)
        st.write('______________________________________________')
        highligh_image5=Image.open("h5.jpg")
        st.image(highligh_image5,width=400)
        st.write('______________________________________________')

    with col2:
        st.header("    ")
        
        st.header("")
        st.write('______________________________________________')
        highligh_image6=Image.open("h6.jpg")
        st.image(highligh_image6,width=400)
       
        st.write('______________________________________________')
        highligh_image7=Image.open("h7.jpg")
        st.image(highligh_image7,width=400)
        st.write('______________________________________________')
        highligh_image8=Image.open("h8.jpg")
        st.image(highligh_image8,width=400)
        st.write('______________________________________________')
        highligh_image9=Image.open("h9.jpg")
        st.image(highligh_image9,width=400)
        st.write('______________________________________________')
        highligh_image10=Image.open("h10.jpg")
        st.image(highligh_image10,width=400)
        st.write('______________________________________________')

        
    
        




    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    
    lottie_hallof_fame=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_P9BonoOnCi.json")
    
    

    

    
    with st.sidebar:
        st.header("Hall of Fame")
        st.markdown("________________________________________________________________________________________________________")

        
        st_lottie(lottie_hallof_fame,key="Match2")
      
