import streamlit as st

st.title("Course Manager App")
st.header("Assignment")
st.subheader("Assignment Manager")

st.divider()

assignment= [
    {
        "id": "HW1",
       "title": "Introduction to database",
       "description": "basis of database design",
       "points": 100,
       "type":"homework"
    },
    {
        "id":"HW2",
        "title": "Normalization",
        "description": "Normalize the table design",
        "point": 100,
        "type": "lab"
    }
]

# Add new assignment 

st.markdown("### Add new assignment")

#input
title = st.text_input("Title",placeholder="ex. Homework 1",
                      help= "This is the name of the assignment")

description= st.text_area("Description",placeholder="ex. database design...")

due_date= st.date_input("Due Date")
assignment_type= st.radio("Type",["Homework","Lab"])
#assignment_type2= st.selectbox("Type",["Homework","Lab","other"])
#if assignment_type2 == "other":
  #  assignment_type2 = st.text_input("Assignment Type")

#lab= st.checkbox("Lab")

with st.expander("Assignment Preview",expander=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title:{title}")

btn_save= st.button("Save",width= "stretch")
if btn_save:
    st.warning("Working on it!")
