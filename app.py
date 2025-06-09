import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('random_forest_taxi_model.pkl')

st.set_page_config(page_title="Taxi Price Predictor", page_icon="🚖")
st.title("🚖 Taxi Trip Price Predictor")
st.markdown("Use this app to estimate the **trip price** based on ride details using a Random Forest regression model.")

# --- Input Section: Numeric Features ---
st.header("🔢 Enter Trip Details")

trip_distance = st.number_input("Trip Distance (km)", min_value=1.23, max_value=146.07, value=10.0)
passenger_count = st.slider("Passenger Count", min_value=1, max_value=4, value=1)
base_fare = st.number_input("Base Fare ($)", min_value=2.01, max_value=5.0, value=3.0)
per_km_rate = st.number_input("Per KM Rate ($)", min_value=0.5, max_value=2.0, value=1.2)
per_minute_rate = st.number_input("Per Minute Rate ($)", min_value=0.1, max_value=0.5, value=0.3)
trip_duration = st.number_input("Trip Duration (minutes)", min_value=5.01, max_value=119.84, value=20.0)

# --- Input Section: Categorical Features ---
st.header("🗓️ Select Ride Context")

time_of_day = st.selectbox("Time of Day", ['Morning', 'Afternoon', 'Evening', 'Night'])
day_of_week = st.selectbox("Day of Week", ['Weekday', 'Weekend'])
traffic = st.selectbox("Traffic Conditions", ['Low', 'Medium', 'High'])
weather = st.selectbox("Weather", ['Clear', 'Rain', 'Snow'])

# --- Encoding Categorical Variables ---
def encode_inputs(time, day, traffic, weather):
    # One-hot encoding in fixed order
    time_vals = ['Morning', 'Afternoon', 'Evening', 'Night']
    day_vals = ['Weekday', 'Weekend']
    traffic_vals = ['Low', 'Medium', 'High']
    weather_vals = ['Clear', 'Rain', 'Snow']

    encoded = []
    encoded += [1 if time == val else 0 for val in time_vals]
    encoded += [1 if day == val else 0 for val in day_vals]
    encoded += [1 if traffic == val else 0 for val in traffic_vals]
    encoded += [1 if weather == val else 0 for val in weather_vals]

    return encoded

# --- Prediction ---
if st.button("🔍 Predict Trip Price"):
    # Combine numerical and encoded categorical inputs
    numerical_features = [
        trip_distance,
        passenger_count,
        base_fare,
        per_km_rate,
        per_minute_rate,
        trip_duration
    ]
    categorical_features = encode_inputs(time_of_day, day_of_week, traffic, weather)

    input_vector = np.array([numerical_features + categorical_features])
    print("Input Vector:", input_vector)

    # Predict (assuming log transformation was applied during training)
    log_price = model.predict(input_vector)[0]
    #predicted_price = np.exp(log_price)

    st.success(f"💰 Estimated Trip Price: **${log_price:.2f}**")

