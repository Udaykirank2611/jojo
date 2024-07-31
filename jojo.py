import streamlit as st
import requests

st.title("Download Zip File from GitHub")

zip_url = "https://github.com/udaykirank2611/jojo/raw/main/CN LAB.zip"

# Provide a download button
st.markdown(f"[Download zip file]({})")

# Optional: If you want to fetch the file and provide it directly via Streamlit
response = requests.get(zip_url)
zip_content = response.content

st.download_button(
    label="Download zip file",
    data=zip_content,
    file_name="yourfile.zip",
    mime="application/zip"
)
