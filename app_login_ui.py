import streamlit as st
import time
import json
from pathlib import Path
from datetime import datetime
import uuid

st.set_page_config(
    page_title="Course Manager",
    layout="centered",
)
users = [
        {
            "id": "1",
            "email": "admin@school.edu",
            "full_name": "System Admin",
            "password": "123ssag@43AE",
            "role": "Admin",
            "registered_at": "..."
        }
    ]
# --- Step 2: data‑loading logic --------------------------------------

json_path = Path("users.json")

if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        users = json.load(f)

tab1 , tab2 = st.tabs(["Login", "Register"])
with tab1:
    with st.container(border=True):
     st.markdown("Login")
    user_name= st.text_input("Email")
    password = st.text_input("Password")

if st.button("Login",type="primary" ,key="loginbutton",use_container_width=True):
    with st.spinner("Checking the login .."):
        time.sleep(5)

