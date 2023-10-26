import streamlit as st
from PIL import Image

st.title("My web")
st.write("hello kunaaal")
num = st.number_input("Enter number")
if st.button("Click me"):
    st.write("clicked")
audio = open("Dosti From Rrr Amit Trivedi 128 Kbps.mp3","rb")
st.audio(audio,format="audio/mp3")

video = open("LEO - Badass Glimpse 1080p-(Teluguvideos.in).mp4","rb")
st.video(video,format="video/mp4")

img = Image.open("virat.png")
st.image(img,caption="Virat Kohli",use_column_width="10px")
a = st.markdown("[link](/?param=value)")
