import streamlit as st

api_key = st.secrets["api_key"]
lmt = 8

st.write('This is page 2')
st.write(api_key)
