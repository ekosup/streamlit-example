import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
# Simple Stock Price App

Shown are the stock closing and volume of Google.

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)