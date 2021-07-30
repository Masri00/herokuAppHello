import streamlit as st
import pickle
import pandas as pd
st.write("""
## My first App
""")
#from xRME get 1RME
def Get_One_RME(reps,reps_RME):
  return (reps_RME*100)/(-3.1631e-05*reps**5 + 0.0022551*reps**4 - 0.058792*reps**3 + 0.66911*reps**2 -5.6984*reps + 104.7705)

#Get xRME from oneRME
def Get_X_RME(reps,oneRME):
  return oneRME*(-3.1631e-05*reps**5 + 0.0022551*reps**4 - 0.058792*reps**3 + 0.66911*reps**2 -5.6984*reps + 104.7705)/100

#get yRME from xRME
def Switch_RME(given_reps,desired_reps,given_RME):
  if desired_reps==given_reps:
    return given_RME
  elif given_reps==1:
    return Get_X_RME(desired_reps,given_RME)
  elif desired_reps==1:
    return Get_One_RME(given_reps,given_RME)
  else:
    one_rme=Get_One_RME(given_reps,given_RME)
    return Get_X_RME(desired_reps,one_rme)

#get decaying weight
def reps_weight(goal_reps,used_reps):
  diff=abs(goal_reps-used_reps)
  if diff>5:
    return 0
  else:
    return int(32/(2**(diff)))

def Allometric_scaling(target_bw,set_bw,set_strength):#This function will return the strength for the target body weight
  mult=(target_bw/set_bw)**(2/3)
  return set_strength*mult


#Get the look_up look_up_dictionary from pickle file
@st.cache(allow_output_mutation=True)
def get_look_up():
    with open('look_up.pkl', 'rb') as pkl_file:
        look_up_dictionary=pickle.load(pkl_file)
    return look_up_dictionary
look_up_dictionary=get_look_up()

#create a form
form = st.form(key='my_form')

exercise=form.selectbox('select exrcise', ['Barbell bench press', 'Barbell back squat',
'Barbell front squat','Barbell deadlift','Overhead press - standing barbell',
'Barbell pendlay row'], key='exercise')
gender=form.selectbox('select gender', ['male', 'female'], key='gender')
age=form.number_input('enter your age', min_value=10, max_value=70, value=20, step=1,key='age')
age_group=(age//10)*10
body_weight=form.number_input('enter your  body weight', min_value=20., max_value=300., value=80., step=1.,format="%.2f",key='body_weight')
reps_done=form.number_input('enter number of reps', min_value=1, max_value=200, value=5, step=1,key='reps_done')
weight_lifted=form.number_input('enter weight lifted', min_value=1., max_value=300., value=30., step=1.,format="%.2f",key='weight_lifted')
df=pd.DataFrame(look_up_dictionary[exercise][gender][age_group])
condition=abs(df['resultReps']-reps_done)<=5
df=df[condition]

submit_button = form.form_submit_button(label='Submit')
if submit_button:
    temp_list=[]
    for i in df['resultReps'].unique():
        weight_values=df[df['resultReps']==i]['resultWeight'].values
        weight_values_truebw=Allometric_scaling(body_weight,100,weight_values)
        converted_weights=Switch_RME(i,reps_done,weight_values_truebw)
        converted_weights_list=converted_weights.tolist()
        temp_list+=converted_weights_list*reps_weight(reps_done,i)
    if len(temp_list)==0:
        st.write("""# No previous history""")
    else:
        percentile=100*len([i for i in temp_list if i<weight_lifted])/len(temp_list)
        st.write(f"""# You are in the {float("{0:.2f}".format(percentile))} percentile""")
