import streamlit as st

def configure_sidebar():
    st.sidebar.header("⚙️ Configure Parameters")

    # Input fields
    equation = st.sidebar.text_input("Enter ODE (e.g., -2*y + t):", value="-2*y")
    init_val = st.sidebar.number_input("Initial Value y(0):", value=1.0)
    t_start = st.sidebar.number_input("Start Time:", value=0.0)
    t_end = st.sidebar.number_input("End Time:", value=10.0)
    step_size = st.sidebar.number_input("Step Size:", value=0.1)

    # Method selection
    method = st.sidebar.selectbox(
        "Select Method:",
        [
            "Euler's Method",
            "Heun's Method",
            "Runge-Kutta Method (4th Order)",
            "Taylor's Series Method",
        ],
    )

    # Export options
    export = st.sidebar.checkbox("Export results as CSV")
    filename = ""
    if export:
        filename = st.sidebar.text_input("Export Filename:", value="results.csv")

    return {
        "equation": equation,
        "init_val": init_val,
        "t_start": t_start,
        "t_end": t_end,
        "step_size": step_size,
        "method": method,
        "export": export,
        "filename": filename,
    }
