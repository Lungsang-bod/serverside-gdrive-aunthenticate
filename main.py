import streamlit as st
from google.oauth2 import service_account


def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
    SERVICE_ACCOUNT_FILE = 'lustrous-bond-364709-c757fbc3c905.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


st.button("click here", on_click=authenticate)
