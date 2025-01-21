import streamlit as st
from components.sidebar import configure_sidebar
from components.plot import display_plot
from methods.euler import euler_method
from methods.heun import heuns_method
from methods.runge_kutta import runge_kutta_4th_method
from methods.taylor_series import taylor_series_method
from utils.exporter import export_results

# Main Streamlit App
def main():
    st.title("🌟 Advanced ODE Solver Tool")
    st.markdown(
        """
        Welcome to the **ODE Solver Tool**. Use the sidebar to configure parameters, 
        select a numerical method, and view solutions interactively.
        """
    )
              
    # Configure parameters in the sidebar
    params = configure_sidebar()

    if st.button("🔍 Solve ODE"):
        try:
            # Select method and solve
            if params["method"] == "Euler's Method":
                t_values, y_values = euler_method(
                    params["equation"], params["init_val"], params["t_start"], params["t_end"], params["step_size"]
                )
            elif params["method"] == "Heun's Method":
                t_values, y_values = heuns_method(
                    params["equation"], params["init_val"], params["t_start"], params["t_end"], params["step_size"]
                )
            elif params["method"] == "Runge-Kutta Method (4th Order)":
                t_values, y_values = runge_kutta_4th_method(
                    params["equation"], params["init_val"], params["t_start"], params["t_end"], params["step_size"]
                )
            elif params["method"] == "Taylor's Series Method":
                t_values, y_values = taylor_series_method(
                    params["equation"], params["init_val"], params["t_start"], params["t_end"], params["step_size"]
                )
            else:
                st.error("Unsupported method selected.")
                return

            # Display plot
            display_plot(t_values, y_values, params["method"])

            # Export option
            if params["export"]:
                export_results(t_values, y_values, params["filename"])
                st.success(f"Results exported to `{params['filename']}`.")

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
