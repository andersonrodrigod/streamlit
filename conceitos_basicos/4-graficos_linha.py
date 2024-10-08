import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 4),
     columns=['a', 'b', 'c', 'd'])

st.line_chart(chart_data)