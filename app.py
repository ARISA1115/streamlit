import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Streamlit app")

st.write("Hello, this is a Streamlit app!")

st.header("Add Components")

st.markdown("This is **boldtext** and this is *italic text*.")

st.latex(r"\sqrt{x^2 + y^2} = z")

st.info("データの読み込みが完了しました。")

st.warning("ファイルのサイズが大きいため、処理に時間がかかる可能性があります。")

st.error("ファイルの形式が正しくありません。CSVファイルをアップロードしてください。")

st.success("グラフの作成が完了しました。")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.header("Data entry and display")

name = st.text_input("Enter your name")
if name:
    st.write(f'Hello. {name}!')

age = st.number_input("Enter your age", min_value=0, max_value=120, value=20)
st.write(f'You are {age} years old.')

date = st.date_input("Select a date")
st.write(f'Selected date: {date}')

st.header("Display DataFrame")

data = {
    "Name": ["Alice", "Bob", "Charline"],
    "Age":[20, 30, 35],
    "City": ["Tokyo", "Osaka", "Fukuoka"]
}

df = pd.DataFrame(data)

st.subheader("DataFrame")
st.dataframe(df)

st.subheader("Display DataFrame as Table")
st.table(df)

st.header("Create Plotly Graph")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "jun"],
    "Sales": [100, 120, 140, 180, 200, 210],
    "Profit": [20, 25, 30, 40, 50, 55]
}

df = pd.DataFrame(data)

st.write("Sample Data")
st.dataframe(df) 

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df["Month"], y=df["Sales"], mode="lines+markers", name="Sales", line=dict(color="blue", width=2)))
fig.add_trace(go.Scatter(x=df["Month"], y=df["Profit"], mode="lines+markers", name="Profit", line=dict(color="red", width=2)))

fig.update_layout(
    title="Sales and Profit Over Months",
    xaxis_title="Month",
    yaxis_title="Amount",
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", 
    yanchor="bottom", y=1.02, 
    xanchor="right", x=1),
    hovermode="x unified"
)

fig.update_xaxes(tickangle=45)
fig.update_yaxes(
    zeroline=True,
    zerolinewidth=2,
    zerolinecolor="lightgrey")

st.plotly_chart(fig)