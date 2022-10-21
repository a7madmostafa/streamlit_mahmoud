import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st



st.title("olympics Data")

olympics = pd.read_csv('sources/olympics_1.csv')

st.dataframe(olympics)
