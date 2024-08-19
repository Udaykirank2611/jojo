import streamlit as st
import requests

st.title("Download Zip File")

zip_url = "https://github.com/udaykirank2611/jojo/raw/main/cse attendence.zip"

# Provide a download button
#st.markdown(f"[Download zip file]")
# Optional: If you want to fetch the file and provide it directly via Streamlit
response = requests.get(zip_url)
zip_content = response.content

st.download_button(
    label="Download zip file",
    data=zip_content,
    file_name="245122737005.zip",
    mime="application/zip"
)
