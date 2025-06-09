# 🚖 Taxi Price Prediction App

This project is a machine learning regression app that predicts taxi ride prices based on trip-related features like distance, duration, time of day, traffic, and weather conditions. The app is built using Streamlit and trained using a Random Forest Regressor model. Check out taxi price predictor here*.

# Inspiration
This project was inspired by the need for transparent and data-driven taxi fare estimation. It serves as a practical example of applying regression techniques to real-world scenarios while demonstrating end-to-end machine learning skills, from data preprocessing to model deployment using Streamlit.

# 🛠️ Technical Details

## 📊 Exploratory Data Analysis (EDA)
        Visualized relationships between trip price and features such as distance, duration, and time of day.

        Identified feature importance and correlations.

        Detected outliers in price and distance distributions.

## 🤖 Model Building
       - Evaluated multiple regression models:

       - Linear Regression - RMSE = 13.8606, R2 = 0.7687

       - Ridge Regression - RMSE = 13.9412, R2 = 0.7660

       - Support Vector Regression - RMSE = 7.6359, R2 = 0.9298

       - Random Forest Regressor - RMSE = 7.2951, R2 = 0.9359

       - Gradient Boosting Regressor - RMSE = 14.7083, R2 = 0.7396

       - XGBoost Regressor -Score on train data =  0.9686; Score on test data =  0.8339; MAE on test data = 6.4888

 📌 Final model selected: Random Forest Regressor
 ✔ Best balance of performance and simplicity
 ✔ RMSE: 7.59 | R² Score: 0.93 (on log-transformed price)

## 📌 Features

- Predicts taxi trip prices based on:
  - Trip Distance (km)
  - Passenger Count
  - Base Fare
  - Per Km Rate
  - Per Minute Rate
  - Trip Duration (minutes)
  - Time of Day (`Morning`, `Afternoon`, `Evening`, `Night`)
  - Day of Week (`Weekday`, `Weekend`)
  - Traffic Conditions (`Low`, `Medium`, `High`)
  - Weather (`Clear`, `Rain`, `Snow`)
- Built with Python, Pandas, Scikit-Learn, Streamlit

# 🌐 App Deployment
  - Developed an interactive Streamlit app to allow user inputs and predict trip prices.

  - App takes both numeric (distance, duration, rates) and categorical (time, day, weather, traffic)  inputs.

  - Outputs predicted trip price based on trained model.

# Sure! Here's a version tailored to your **Taxi Price Regression** project, written in a clear and professional tone:

---

## 👥 Contributions

    Contributions are always welcome! Whether it's improving the model, enhancing the Streamlit app, optimizing performance, or suggesting new features, your input can help make the **Taxi Price Predictor** even better.

    Feel free to fork the repository, create a branch, and submit a pull request. For major changes, please open an issue first to discuss what you'd like to improve.












