import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config("order application", layout="wide",initial_sidebar_state="expanded")

inventory = [
    {"id": 1, "name": "Espresso", "price": 2.50, "stock": 40},
    {"id": 2, "name": "Latte", "price": 4.25, "stock": 25},
    {"id": 3, "name": "Cold Brew", "price": 3.75, "stock": 30},
    {"id": 4, "name": "Mocha", "price": 4.50, "stock": 20},
    {"id": 5, "name": "Blueberry Muffin", "price": 2.95, "stock": 18}
]
if "page" not in st.session_state:
    st.session_state["page"] = "home"

if "message" not in st.session_state:
    st.session_state["message"] = [
        {
            "role": "assistant",
            "content": "Hi how can I help you today?"
        }
    ]
with st.sidebar:
    if st.button("Home",key="home_btn",type="primary",use_container_width=True):
        st.session_state["page"]="home"
        st.rerun()


    if st.button("Orders",key="Order_btn",type="primary",use_container_width=True):
        st.session_state["page"]="Orders"
        st.rerun()

json_path_inventory = Path("inventory.json")
if json_path_inventory.exists():
    with open(json_path_inventory,"r") as f:
        inventory= json.load(f)

json_path_orders = Path("orders.json")
if json_path_orders.exists():
    with open(json_path_orders,"r") as f:
        orders= json.load(f)
else:
    orders =[]

if st.session_state["page"]=="home":
    col1, col2 = st.columns([4,2])
    with col1:
        selected_category= st.radio("Select a Categroy",["Orders","inventory"],horizontal=True)

        if selected_category == "Inventory":
            st.markdown("## Inventory")
            if len(inventory)> 0:
                st.dataframe(inventory)
            else:
                st.warning("no item found")
        else :
            st.markdown("## Orders")
            if len(orders)>0:
                 st.dataframe(orders)
            else:
                st.warning("no order are recoded yet")
    with col2:
        if selected_category =="Inventory":
            st.metric("Total Inventory", f"{len(inventory)}")
        else:
            st.metric("Total Order", f"{len(orders)}")





elif st.session_state["page"]== "orders":
    st.markdown("Under Construction...")

tab1, tab2 = st.tabs(["Add New Order", "Cancel an order"])

with tab1:
    col1, col2 = st.columns([3,3])
    with col1:
        selected_item = st.selectbox("Items",options = inventory, key="inventory_selector",
                                    format_func= lambda x: f"{x['name']}")
        quantity = st.number_input("Enter the Quantity",min_value=1, step=1)

        if st.button("Create New Order",key = "create_order_btn",type="primary",use_container_width=True):
            with st.spinner("Recording the new order..."):
                total = quantity* selected_item['price']

                for item in inventory:
                    if item["id"] == selected_item["id"]:
                        item["stock"]= item["stock"]- quantity
                        break
            
                orders.append({
                "id": str(uuid.uuid4()),
                "item_id": selected_item["id"],
                "item_name": selected_item["name"],
                "quantity": quantity,
                "status": "placed",
                "total_price": total,
                
            })
                time.sleep(4)
                with open(json_path_inventory,"w") as f:
                    json.dump(inventory,f)

                with open(json_path_orders,"w") as f:
                    json.dump(orders,f)
                
                st.balloons()
                time.sleep(8)

                st.session_state["page"]="home"
                st.rerun()
            
    with col2:
        st.subheader("AI Assistant")
        col11 ,col22 = st.columns([3,1])
        with col11:
            st.caption("Try asking : How to place an order")
        
        with col22:
            if st.button("Clear Conversation"):
                pass
        
        with st.container(border= True, height= 250):
            for message in st.session_state["message"]:
                with st.chat_message(message["role"]):
                    st.write(message["content"])


        user_input = st.chat_input("Ask a question...")
        if user_input:
            with st.spinner("Thinking..."):
                st.session_state["message"].append({
                    "role": "user",
                    "content": user_input
                })
                
                ai_response = "I am working on it ..."
                    
                st.session_state["message"].append({
                            "role": "user",
                            "content": user_input
                        }
                )
                        
                ai_response = "I am working on it ..."
                    
                st.session_state["message"].append(
                    {
                            "role": "user",
                            "content": user_input
                        })
