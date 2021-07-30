import streamlit as st
import pickle
import pandas as pd
st.write("""
## My first App
""")
@st.cache(allow_output_mutation=True)
def get_look_up():
    with open('look_up.pkl', 'rb') as pkl_file:
        look_up_dictionary=pickle.load(pkl_file)
    return look_up_dictionary
look_up_dictionary=get_look_up()
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
df=pd.DataFrame(dict)
submit_button = form.form_submit_button(label='Submit')
if submit_button:

    st.write(df.iloc[:10,:])
