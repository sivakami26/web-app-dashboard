import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Sivakami")
    content = """Highly motivated individual with 7+ years of experience in developing and
     implementing embedded software solutions. Strong skills in embedded C programming and 
     WLAN protocols. Possess deep passion for learning new tools and technologies. currently 
     learning and building apps in Python"""
    st.info(content)

st.info("Below you can find some of the apps I have built in Python")