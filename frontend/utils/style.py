import streamlit as st

def set_background():
    st.markdown("""
    <style>
    .stApp {
        background-color: #fffee1;
    }
    </style>
    """, unsafe_allow_html=True)