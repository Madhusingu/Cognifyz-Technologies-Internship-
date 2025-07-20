import streamlit as st
import pandas as pd
import plotly.express as px

# Upload dataset
uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "json"])
if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)
    st.write("Data Preview:", df.head())

    # Chart selection
    chart_type = st.selectbox("Select chart type", ["Scatter", "Line", "Bar"])
    x_axis = st.selectbox("X-axis", df.columns)
    y_axis = st.selectbox("Y-axis", df.columns)

    # Generate chart
    if chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    else:
        fig = px.bar(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)
