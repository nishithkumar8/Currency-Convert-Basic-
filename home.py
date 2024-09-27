import streamlit as st

st.title("Currency Converter")


exchange_rates = {"USD": 1, "EUR": 0.85, "GBP": 0.75, "INR": 80}

amount = st.number_input("Enter amount in USD:")
target_currency = st.selectbox("Choose currency:", exchange_rates.keys())


converted_amount = amount * exchange_rates[target_currency]
st.success(f"{amount} USD is equal to {converted_amount:.2f} {target_currency}")

