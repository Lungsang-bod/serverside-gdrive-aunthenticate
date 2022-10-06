import streamlit as st
from pydrive.auth import GoogleAuth


def authenticate():
    gauth = GoogleAuth()
    gauth.redirect_uri = 'http://13.232.4.181:8503'


st.button("click here", on_click=authenticate)
