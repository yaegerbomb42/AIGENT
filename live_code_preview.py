import streamlit as st
import os

def display_code_preview(directory):
    st.markdown("### 🧠 Code Preview")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                st.subheader(file)
                with open(os.path.join(root, file)) as f:
                    st.code(f.read(), language="python")
