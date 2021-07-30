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
st.write('hello1')
with open('look_up.pkl', 'rb') as pkl_file:
    look_up_dictionary=pickle.load(pkl_file)
oo='initial'
form = st.form(key='my_form')
exercise=form.selectbox('select exrcise', ['Barbell bench press', 'Barbell back squat',
'Barbell front squat','Barbell deadlift','Overhead press - standing barbell',
'Barbell pendlay row'], key='exercise')
gender=form.selectbox('select gender', ['male', 'female'], key='age')
age=form.number_input('select age', min_value=1, max_value=10, value=5, step=1)
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    df=pd.DataFrame(look_up_dictionary[exercise][gender][age])
    st.write(df.iloc[:10,:])
