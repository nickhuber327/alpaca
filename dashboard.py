import streamlit as st
import pandas as pd
import numpy as np


option = st.sidebar.selectbox("Dashboard", ('Home', 'Charts', 'Alpaca'))
st.title(option)
