import streamlit as st
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

start = dt.datetime(2020,1,1)
end = dt.datetime.now()


st.title("Cryptocurrency Price Visualizer")
st.write(""" ## Created By: Shivam Bhosale """)

st.sidebar.write(""" ## Cryptocurrency Price Visualizer """)

crypto_name = st.sidebar.selectbox("Select Cryptcurrency",("BTC","ETH","ETC","DOGE","ADA","XRP","TRX","LINK",))
currency_name = st.sidebar.selectbox("Select Local Currency",("USD","EUR","INR","CAD","AUD","GBP"))

if st.sidebar.button("Visualize"):
    data = web.DataReader(f"{crypto_name}-{currency_name}", "yahoo")
    st.write(f"Ploting the graph between {crypto_name} and {currency_name}.")

    fig = plt.figure(figsize=(8,6))
    plt.title(f"{crypto_name} Coin Price Visualizer")
    plt.xlabel("Year")
    plt.ylabel(f"Price in {currency_name}")
    plt.plot(data['Close'],color='green')
    st.pyplot(fig)
    s = data['Close'].tail(1) 
    st.write(f"The closing price for the {crypto_name} is {s} ")