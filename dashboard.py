import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.title("Stock Dashboard")
st.set_page_config(layout="centered")

tickers = st.text_input("Ticker input (separated by comma):",placeholder="AAPL,MSFT,TSLA")
tickers = [t.strip() for t in tickers.split(",")]

df = yf.download(tickers, period="1y", auto_adjust=True)
df_5y = yf.download(tickers, period="10y", auto_adjust=True)
prices = df["Close"]
prices_5y = df_5y["Close"]

if isinstance(prices, pd.Series):
    prices = prices.to_frame(name=tickers[0])

if isinstance(prices_5y, pd.Series):
    prices_5y = prices_5y.to_frame(name=tickers[0])


fig = px.line(prices, title="Stock prices comparison (1 year)")
st.plotly_chart(fig, use_container_width=True)

fig_5y = px.line(prices_5y, title="Stock prices comparison (5 years)")
st.plotly_chart(fig_5y, use_container_width=True)