import streamlit as st

st.write("""
# My first App
""")
number=st.slider('Choose a number:', 1, 100)
st.write("You chose: ", number)
