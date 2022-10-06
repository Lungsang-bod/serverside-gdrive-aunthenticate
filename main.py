import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    path = "/home/ubuntu/serverside-gdrive-authenticate/content/"
    folder = "KrW8LGuIELpsBqvaVfLAmHiuLz7uJ5T_"

    file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()
    if st.checkbox("Show file list?", True):
        for index, file in enumerate(file_list):
            st.write(index + 1, file['title'])
            file.GetContentFile(path + file['title'])


st.button("click here", on_click=authenticate)
