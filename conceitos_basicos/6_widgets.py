import streamlit as st

'''x = st.slider('x')
st.write(x, 'squared is', x * x)'''


st.text_input("Your name", key="name")
st.session_state.name