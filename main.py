import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

@st.cache_data
def load_data():
    data = pd.read_excel("NIFTY BANK.xlsx")
    data['Expiry'] = data['Date'].dt.dayofweek == 3
    data = data.drop(columns=['Date'])  # Drop non-numeric columns
    return data

def main():
    st.title("NIFTY BANK Close Price Predictor")
    
    data = load_data()
    X = data.drop(columns=['Close'])  # Feature columns (all numeric)
    y = data['Close']  # Target column

    # Ensure all data in X is numeric
    X = X.apply(pd.to_numeric, errors='coerce')
    X = X.fillna(0)  # Fill NaN values with 0 or any other suitable value

    # Standardize features and split data
    scaler = StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(scaler.fit_transform(X), y, test_size=0.2, random_state=42)
    
    # Train and evaluate model
    model = LinearRegression().fit(X_train, y_train)
    mse = mean_squared_error(y_test, model.predict(X_test))
    st.write(f"Mean Squared Error: {mse}")

    # Prediction inputs
    inputs = [st.number_input(col) for col in X.columns[:-1]]
    inputs.append(st.selectbox("Expiry Day", ['Yes', 'No']) == 'Yes')

    if st.button("Predict"):
        prediction = model.predict(scaler.transform([inputs]))
        st.write('Close Price Prediction:', prediction[0])

if __name__ == "__main__":
    main()
