import streamlit as st
import numpy as np
import pandas as pd


# 8_selectbox.py


df = pd.DataFrame({
    'first column':[1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


option = st.selectbox(
    'which number do you like best',
    df['first column']
)

'you selected', option