import sys
import subprocess
import conda.cli.python_api as Conda
package_name = "streamlit_player"
try:

    subprocess.check_call([sys.executable, '-m', 'conda', 'install', package_name])

except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])  

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_player import st_player

page = st.selectbox("Choose your page", ["Introduction", "NFT Store"]) 

if page == "Introduction":
    st.sidebar.title("Group 2 Capstone Project")
    st.sidebar.markdown("""
    * **Python Libraries:** pandas, streamlit
    """)
    
    st.sidebar.title("NFT Store")
    st.sidebar.text("GROUP MEMBERS")
    st.sidebar.text("Carl Buchholz")
    st.sidebar.text("Chris Kwiatkowski")
    st.sidebar.text("Edward Schryver")
    st.sidebar.text("Troy Albany")

    from PIL import Image
    image = Image.open('streamlit_code_1.jpg')   
    st.image(image, caption='NFT Purchase code')

    st.markdown(
        """
        <style>
        .reportview-container{
        background-image: url("https://th.bing.com/th/id/OIP.KZTDIgchaAhxJ-AHYwawagHaEK?w=309&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7");
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

elif page == "NFT Store":
    st.title("Top 10 NFL Plays of All Time")
    st.markdown("""
    This app shows the top 10 NFL plays of All Time as NFT's!
    """)

    st.markdown(
        """
        <style>
        .reportview-container{
        background-image: url("https://th.bing.com/th/id/OIP.zAy9ElFT0X74jBIm8lDq2wHaE7?w=236&h=180&c=7&r=0&o=5&pid=1.7");
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    st.sidebar.header('Purchase NFT')
    st.sidebar.selectbox('Play', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

    offer_price = st.sidebar.slider('Offer Price - Eth', 0, 100,)
    if offer_price > 70: 
        if st.sidebar.button("Purchase"):
            st.balloons()
    else: 
        if st.sidebar.button("Purchase"):
            st.sidebar.error("Offer Price Too Low")



    st_player("https://soundcloud.com/imaginedragons/whatever-it-takes-1")
    st.title("Play 10 - Philly Special - Eagles vs Patriots")
    st_player("https://www.youtube.com/watch?v=y3Jqif1TUwQ")

    st.title("Play 9 - The Minneapolis Miracle - Vikings vs Saints")
    st.image("https://th.bing.com/th/id/OIP._gNH0hiXPzuzAEm027b4OwHaFP?w=213&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    st.title("Play 8 - Bart Stars QB Sneak - Packers vs Cowboys")
    st_player("https://www.youtube.com/watch?v=1WXCKG55tlM")

    st.title("Play 7 - Immaculate Interception – Steelers v Cardinals XLIII")
    st_player("https://www.youtube.com/watch?v=50M0MOgAAbw")

    st.title("Play 6 - Santonio Holmes game winning TD – Steelers v Cardinals XLIII")
    st_player("https://www.youtube.com/watch?v=rlqipGHuk-4")

    st.title("Play 5 - Butler picks off Wilson – Patriots v Seahawks XLIX")
    st.image("https://th.bing.com/th/id/OIP.Wd4AvmBwtnwT0uDrf6r_mAHaDv?w=327&h=177&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    st.title("Play 4 - Music City Miracle – Titans v Bills")
    st_player("https://www.youtube.com/watch?v=Pfz4JViRkoA")

    st.title("Play 3 - David Tyree Helmet Catch – Giants v Patriots XLII")
    st.image("https://th.bing.com/th/id/OIP.bT29UEGMCg_RBtvekfIsPQHaFD?w=237&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    st.title("Play 2 - The Catch Joe Montana – 49ers v Cowboys NFC Championship")
    st.image("https://th.bing.com/th/id/OIP.safFKQlWCAG-NinfB35hWgHaG0?w=168&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    st.title("Play 1 - Immaculate Reception – Steelers v Raiders")
    st.image("https://th.bing.com/th/id/OIP.Tj18qDCd1tM__8cbl7xvWQHaFx?w=230&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

