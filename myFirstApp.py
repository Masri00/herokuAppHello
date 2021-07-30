import streamlit as st
import pickle
import pandas as pd
st.write("""
## My first App
""")

with open('look_up.pkl', 'rb') as pkl_file:
    look_up_dictionary=pickle.load(pkl_file)
oo='initial'
form = st.form(key='my_form')
exercise=form.selectbox('select exrcise', ['Barbell bench press', 'Barbell back squat',
'Barbell front squat','Barbell deadlift','Overhead press - standing barbell',
'Barbell pendlay row'], key='exercise')
dict=look_up_dictionary[exercise]
gender=form.selectbox('select gender', ['male', 'female'], key='age')
dict=dict[gender]
age=form.number_input('select age', min_value=1, max_value=50, value=20, step=1)
dict=dict[age]
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    df=pd.DataFrame(dict)
    st.write(df.iloc[:10,:])
