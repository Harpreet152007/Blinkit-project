import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
 df = pd.read_csv("blinkit_orders.csv") 
 df = load_data()