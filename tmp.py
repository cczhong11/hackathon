from io import StringIO
import streamlit as st
import json
from util import give_me_text_from_graph

# Title of the app
st.title("My To-Do List")

# To-do list items
# tasks = ["Write project", "Design", "Write Code"]
uploaded_file = st.file_uploader("Choose a file")


def create_bullet_journal_container(date, tasks):
    with st.container():
        # Create two columns, one small for the date, one larger for the tasks
        col1, col2 = st.columns([1, 4])
        with col1:
            # Display the date in the first column
            st.markdown(f"#### {date}")
        with col2:
            # Create a box-like container for tasks
            st.markdown("##### Tasks")
            for task in tasks:
                # Create a checkbox for each task
                st.checkbox(task)


if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write("Uploaded file is now stored as bytes.")

    # Can use any file handling or processing here
    # For example, saving the file
    with open("myfile.jpeg", "wb") as f:
        f.write(bytes_data)
    st.success("File saved!")
    output = give_me_text_from_graph("myfile.jpeg")
    print(output)
    output_json = json.loads(output)
    create_bullet_journal_container(output_json.get("date"), output_json.get("tasks"))