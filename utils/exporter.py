import numpy as np

def export_results(t_values, y_values, filename="results.csv"):
    data = np.column_stack((t_values, y_values))
    np.savetxt(filename, data, delimiter=",", header="Time, y(t)", comments="")
