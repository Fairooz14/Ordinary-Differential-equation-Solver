# import matplotlib.pyplot as plt
# import streamlit as st

# def display_plot(t_values, y_values, method):
#     st.subheader("📈 Solution Visualization")
#     fig, ax = plt.subplots()
#     ax.plot(t_values, y_values, label=method, color="blue", linewidth=2)
#     ax.set_xlabel("Time (t)")
#     ax.set_ylabel("y(t)")
#     ax.set_title(f"ODE Solution using {method}")
#     ax.legend()
#     ax.grid(True)
#     st.pyplot(fig)
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def display_plot(t_values, y_values, method, params=None, error=None, comparison_data=None):
    """
    Enhanced visualization of ODE solutions with features like parameter influence, error estimation, and comparisons.
    Additionally, displays numerical results below the plot.
    """
    st.subheader("📈 Solution Visualization")

    # Initialize plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Main solution plot
    ax.plot(t_values, y_values, label=f"Solution ({method})", color="blue", linewidth=2)

    # Add parameter influence visualization
    if params:
        for param_label, param_solution in params.items():
            ax.plot(t_values, param_solution, label=f"Solution ({param_label})", linestyle="--")

    # Add error estimation visualization
    if error is not None:
        ax.fill_between(
            t_values, y_values - error, y_values + error,
            color="orange", alpha=0.3, label="Error Estimation"
        )

    # Add comparisons with other methods or exact solutions
    if comparison_data:
        for method_label, (comp_t, comp_y) in comparison_data.items():
            ax.plot(comp_t, comp_y, label=f"Comparison ({method_label})", linestyle=":")

    # Customize plot
    ax.set_xlabel("Time (t)", fontsize=12)
    ax.set_ylabel("y(t)", fontsize=12)
    ax.set_title(f"ODE Solution Visualization", fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True)

    # Render plot in Streamlit
    st.pyplot(fig)

    # Display numerical results below the plot
    st.subheader("📋 Numerical Results")

    # Prepare data for the main method
    results_data = {"Time (t)": t_values, f"Solution ({method})": y_values}

    # Add parameter influence data
    if params:
        for param_label, param_solution in params.items():
            results_data[f"Solution ({param_label})"] = param_solution

    # Add comparison data
    if comparison_data:
        for method_label, (comp_t, comp_y) in comparison_data.items():
            results_data[f"Comparison ({method_label})"] = comp_y

    # Convert to DataFrame and display
    results_df = pd.DataFrame(results_data)
    st.dataframe(results_df, use_container_width=True)

