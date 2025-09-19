import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.title("Stock Dashboard")

tickers = st.text_input("Ticker input (separated by comma):",placeholder="AAPL,MSFT,TSLA")
tickers = [t.strip() for t in tickers.split(",")]