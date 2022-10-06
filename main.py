import streamlit as st
from pydrive.auth import GoogleAuth


def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()


st.button("click here", on_click=authenticate)
