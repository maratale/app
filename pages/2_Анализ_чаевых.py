import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import altair as alt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import seaborn as sns

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

start = pd.to_datetime('2023-01-01')
end = pd.to_datetime('2023-01-31')
tips['time_order'] = pd.to_datetime(
    np.random.randint(start.value, end.value, size=len(tips))
).normalize()

st.title('Анализ чаевых')

st.dataframe(tips.head())
tips_dynamic = tips.groupby('time_order')['tip'].sum()

fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.plot(tips_dynamic.index, tips_dynamic.values, marker='o')
ax2.set_title('Динамика чаевых во времени')
ax2.set_xlabel('Дата')
ax2.set_ylabel('Сумма чаевых')
ax2.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig2)
buf = io.BytesIO()
fig2.savefig(buf, format="png")
buf.seek(0)

st.download_button(
        label="Скачать график 'Динамика чаевых во времени' (PNG)",
        data=buf,
        file_name="chart.png",
        mime="image/png",
        icon=":material/download:"
    )

fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.kdeplot(data=tips, x='total_bill', color='red', ax=ax3, fill=True)
ax3.set_title('Распределение общего счета')
st.pyplot(fig3)
buf = io.BytesIO()
fig3.savefig(buf, format="png")
buf.seek(0)

st.download_button(
        label="Скачать график 'Распределение общего счета' (PNG)",
        data=buf,
        file_name="chart.png",
        mime="image/png",
        icon=":material/download:"
    )


fig, ax = plt.subplots(figsize=(15, 10))
ax.scatter(tips["total_bill"], tips["tip"], alpha=0.7)
ax.set_title("Общий счет vs Чаевые")
ax.set_xlabel("Общий счет")
ax.set_ylabel("Чаевые")
ax.grid(True)

st.pyplot(fig)
buf = io.BytesIO()
fig.savefig(buf, format="png")
buf.seek(0)

st.download_button(
        label="Скачать график 'Общий счет vs Чаевые' (PNG)",
        data=buf,
        file_name="chart.png",
        mime="image/png",
        icon=":material/download:"
    )

fig, ax = plt.subplots(figsize=(12, 8))

sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    size='size',
    sizes=(20, 200),
    alpha=0.7,
    legend='brief',
    color='b',
    ax=ax 
)

ax.set_title('Связь общего счёта, чаевых и размера (размер точки)')
ax.set_xlabel('Общий счет')
ax.set_ylabel('Чаевые')
ax.grid(True)

st.pyplot(fig)
buf = io.BytesIO()
fig.savefig(buf, format="png")
buf.seek(0)

st.download_button(
        label="Скачать график 'Связь общего счёта, чаевых и размера' (PNG)",
        data=buf,
        file_name="chart.png",
        mime="image/png",
        icon=":material/download:"
    )


fig, ax = plt.subplots(figsize=(20, 10))

days_bills = tips.groupby('day')['total_bill'].sum()

ax.plot(days_bills.index, days_bills.values, marker='o')
ax.set_title('Суммарные счета по дням недели')
ax.set_xlabel('День недели')
ax.set_ylabel('Сумма счета')
ax.grid(True)
plt.xticks(rotation=45)
with st.expander("kuku"):
    st.write("👻")

st.pyplot(fig)
buf = io.BytesIO()
fig.savefig(buf, format="png")
buf.seek(0)

st.download_button(
        label="Скачать график 'Суммарные счета по дням недели' (PNG)",
        data=buf,
        file_name="chart.png",
        mime="image/png",
        icon=":material/download:"
    )


st.title("Загрузка и скачивание файла")

uploaded_file = st.file_uploader("Загрузите CSV файл", type=None)
if uploaded_file is not None:
    st.success(f"Файл '{uploaded_file.name}' успешно загружен!")
    

st.badge("HELP ME", color="red", icon=":material/sentiment_dissatisfied:")