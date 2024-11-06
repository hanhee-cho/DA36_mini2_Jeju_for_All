import streamlit as st
st.write('hello')
checked=st.checkbox('Agree?')
st.write(f'Agree_status:{'agree' if checked else 'disagree'}')