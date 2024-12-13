import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyser")

ticker_data = yf.Ticker("MSFT")

ticker_df = ticker_data.history(period = '1d', start = '2023-01-01', end = '2023-12-31')
st.dataframe(ticker_df.head())

st.subheader('Closing price movement in 2023')
st.line_chart(ticker_df['Close'])

st.subheader('Volume movement in 2023')
st.line_chart(ticker_df['Volume'])

# Q2. Which stock u wnat to analyze?

st.radio("Which stock you want to analyze?",['MSFT', 'APPL', 'GOOG'])

start_date = st.date_input("Please enter starting date", datetime.date(2023,1,1))

end_date = st.date_input("Please enter ending date", datetime.date(2023,12,12))

# Q2. Which stock u wnat to analyze? COlumn wise

st.title("Stock Price Analyzer.")
col1, col2, col3 = st.columns(3)
with col1:
    stock_name = st.text_input("Which stock you want to analyse", "MSFT")

ticker_data = yf.Ticker(stock_name)


with col2:
    start_date = st.date_input("Please enter Starting Date",
              datetime.date(2023,12,1))
with col3:
    end_date = st.date_input("Please enter Ending Date",
              datetime.date(2024,12,1))
