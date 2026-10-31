
import streamlit as st

st.title("OS Simulation Starter")

processes = st.number_input(
    "Choose the number of processes:",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

st.write(f"Simulation will include {processes} processes.")
