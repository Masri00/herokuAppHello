import streamlit as st
import pickle
import pandas as pd
st.write("""
## My first App
""")

number1=st.slider('Choose a number:', 1, 50,key='1')
number2=st.slider('Choose a number:', 1, 50,key='2')
number3=st.slider('Choose a number:', 1, 50,key='3')

st.write(f"""# You chose {number1+number2+number3}""")

with open('look_up.pkl', 'rb') as pkl_file:
    look_up_dictionary=pickle.load(pkl_file)
df=pd.DataFrame(look_up_dictionary['Barbell bench press']['male'][20])
st.write('hello')
