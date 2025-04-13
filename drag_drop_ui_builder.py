import streamlit as st
from streamlit_sortables import sort_items

def render_ui_builder():
    st.markdown("### 🧩 Drag & Drop UI Builder")
    layout = sort_items(["Header", "Text Input", "Submit Button", "Chart Placeholder"])
    st.write("🧱 Your layout:", layout)
