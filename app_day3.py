import streamlit as st
import time
import json 
from pathlib import Path

st.set_page_config(
    page_title="Course Manager",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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
json_path = Path("Assignment.json")
