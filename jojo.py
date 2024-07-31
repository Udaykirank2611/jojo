import streamlit as st
import zipfile
from io import BytesIO

st.title("Zip File Upload and Download Example")

# File uploader
uploaded_file = st.file_uploader("Choose a zip file", type=["zip"])

if uploaded_file is not None:
    # Display the name of the uploaded file
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Extract the zip file
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        # List all files in the zip
        file_list = zip_ref.namelist()
        st.write("Files in the zip:")
        st.write(file_list)

        # Read and display the content of each file
        for file_name in file_list:
            with zip_ref.open(file_name) as file:
                file_content = file.read()
                st.write(f"Content of {file_name}:")
                st.text(file_content.decode("utf-8"))

    # Create a download button for the uploaded zip file
    st.download_button(
        label="Download zip file",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime="application/zip"
    )
