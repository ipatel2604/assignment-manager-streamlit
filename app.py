import streamlit as st

st.title("Course Manager")

st.header("Course Managemnt Dashboard")
st.caption("MISY350")
st.divider()


assignment=[
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
        "type": "homework"
    }
]

#3. step 3: Add new assignemnt section (Input & layout)
st.subheader("Add New assignment")
with st.container(border=True):
    col1,col2 = st.columns([2,1])

    with col1:
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input("Assignment title",placeholder="homework")
            description= st.text_input("Assignment description")
            point= st.number_input("Points")
    with col2:
        st.markdown("**Time and Type**")
        due_date = st.date_input("Due date")
        type = st.radio("type",["Homework","lab"])
