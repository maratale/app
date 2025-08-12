import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import altair as alt
import numpy as np
import io

st.set_page_config(page_title="Анализ Apple", layout="wide")

st.title("Анализ котировок Apple")

st.sidebar.header("Настройки")

period = st.sidebar.selectbox("Период данных Apple", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

@st.cache_data
def load_apple_data(period):
    data = yf.download("AAPL", period=period, progress=False)
    data.reset_index(inplace=True)
    return data

apple_data = load_apple_data(period)
st.subheader(f"Котировки Apple за период: {period}")
st.dataframe(apple_data.tail())

fig, ax = plt.subplots()
ax.plot(apple_data["Date"], apple_data["Close"], label="AAPL")
ax.set_title("Закрытие акций Apple")
ax.set_xlabel("Дата")
ax.set_ylabel("Цена закрытия")
ax.legend()
st.pyplot(fig)

