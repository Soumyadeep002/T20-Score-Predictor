import streamlit as st
import pickle
import pandas as pd

file = open("model_pipeline.pkl", "rb")
pipeline = pickle.load(file)


st.set_page_config(
   page_title="T20 Score Predicto"
)


st.title("T20 Score Predictor")

col1, col2 = st.columns(2)

team = ['Australia', 'New Zealand', 'South Africa', 'England', 'India',
       'West Indies', 'Pakistan', 'Bangladesh', 'Afghanistan',
       'Sri Lanka']

city = ['Melbourne', 'Adelaide', 'Mount Maunganui', 'Auckland',
       'Southampton', 'Cardiff', 'Nagpur', 'Bangalore', 'Lauderhill',
       'Dubai', 'Abu Dhabi', 'Sydney', 'Wellington', 'Hamilton',
       'Barbados', 'Trinidad', 'Colombo', 'St Kitts', 'Manchester',
       'Delhi', 'Lahore', 'Johannesburg', 'Centurion', 'Cape Town',
       'Mumbai', 'Kolkata', 'Durban', 'Chandigarh', 'Christchurch',
       'London', 'Nottingham', 'St Lucia', 'Pallekele', 'Mirpur',
       'Chittagong']


with col1:
    batting_team = st.selectbox(
        "Batting Team",
        team, index=None, placeholder="Select batting team...")
with col2:
    bowling_team = st.selectbox(
        "Bowling Team",
        team, index=None, placeholder="Select bowling team...")
    
city = st.selectbox(
        "City",
        city, index=None, placeholder="Select city...",)

col3, col4, col5  = st.columns(3)

with col3:
    current_score = st.number_input("Enter Current Score")
    
with col4:
    over_done = st.number_input("Overs Done")

with col5:
    wickets_out = st.number_input("Wickets out")


last_five = st.number_input("Enter Score in last 5 overs")

s_state = st.button("Predict")

if s_state:
    if batting_team == None or bowling_team == None or city == None or float(current_score) < 0.0 or float(over_done) <= 0.0 or int(wickets_out) < 0 or float(last_five) < 0.0 or batting_team == bowling_team :
        st.warning("Please fill valid values !")
    else:
        wickets_left = 10 - wickets_out
        balls_left = 120 - (over_done*6)
        crr = current_score/over_done

        data = pd.DataFrame({ 'batting_team':[batting_team], 'bowling_team':[bowling_team], 'city':city, 'current_score':[current_score], 'balls_left':[balls_left], 'wickets_left':[wickets_left] ,'crr':[crr], 'last_five':[last_five]})
        predicted_result = pipeline.predict(data)

        st.header(f'Predicted Runs for team {batting_team} is: ')
        st.subheader(f' {int(predicted_result[0])}')

