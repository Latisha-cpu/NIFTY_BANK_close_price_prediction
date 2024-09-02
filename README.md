# NIFTY_BANK_close_price_prediction
## Overview

This project is focused on predicting the closing price of the NIFTY BANK index using various financial metrics and indicators. The prediction model is built using machine learning techniques, and a web app interface is provided for users to input data and get predictions.

## Project Structure:

main.py: Main script that contains the Streamlit app code for user interaction and prediction.

requirements.txt: List of Python libraries required to run the project.

README.md: Project documentation file.

## Features:

Predict the closing price of the NIFTY BANK index based on user inputs.

Intuitive web interface built with Streamlit.

Real-time prediction based on key market metrics.

Option to include expiry day as a factor in prediction.

## Inputs for Prediction:

The app takes the following input fields to make a prediction:

Open: Opening price of the NIFTY BANK index.

High: Highest price of the NIFTY BANK index during the day.

Low: Lowest price of the NIFTY BANK index during the day.

INDIAVIX Open: Opening value of the India VIX (Volatility Index).

INDIAVIX High: Highest value of India VIX during the day.

INDIAVIX Low: Lowest value of India VIX during the day.


Expiry Day (Yes/No): A boolean value indicating whether the date is an expiry day (Thursday) for NIFTY BANK futures and options.

These inputs are used by the Linear Regression model to predict the closing price of NIFTY BANK.

## Significance:

Open, High, Low prices are essential to gauge market sentiment and fluctuations within the day.

INDIAVIX metrics provide insights into market volatility and potential risk factors.

Expiry Day accounts for possible anomalies due to options settlement, which can cause sharp market movements.

# Installation
## Prerequisites

Python 3.x installed on your machine.

Streamlit and other required libraries listed in requirements.txt.

## Steps

Clone the repository to your local machine:
git clone https://github.com/yourusername/nifty-bank-prediction.git

Navigate to the project directory:
cd nifty-bank-prediction

Install the required Python libraries:
pip install -r requirements.txt

## Usage
Run the Streamlit app:
streamlit run app.py

The app will open in your web browser. Input the required values in the provided fields.

Click on the "Predict" button to get the predicted "Close" price.

## Notes:
This project does not require a saved model file (model.pkl) as the model is trained each time the application runs.

