# ODE Solution Visualization Tool

📈 A Streamlit-based application to visualize and analyze solutions to Ordinary Differential Equations (ODEs). This tool offers enhanced features like parameter influence visualization, error estimation, and comparisons with other numerical methods or exact solutions.


## 🌟 Features
- **Interactive Plotting**:
  - Visualize ODE solutions with enhanced clarity.
  - Include parameter influences, error estimations, and method comparisons in a single graph.
- **Numerical Results Table**:
  - Display solution values directly below the plot for easy reference.
  - Support for additional solutions and comparison methods.
- **Streamlit Integration**:
  - Lightweight and easy-to-use interface.
  - Interactive capabilities for enhanced user experience.


## 🛠️ How It Works
1. **Main ODE Solution**: The solution for a given ODE is plotted using the specified numerical method (e.g., Euler, Runge-Kutta, etc.).
2. **Parameter Influence**: Visualize how changing parameters affects the solution.
3. **Result Exporting**: Result can be exported in csv file.


## 📂 Project Stucture
   ```
Ordinary-Differential-equation-Solver/
├── app.py                # Main Streamlit file
├── components/
│   ├── sidebar.py        # Streamlit sidebar component
│   ├── plot.py           # Plotting component
├── methods/
│   ├── euler.py
│   ├── heun.py
│   ├── runge_kutta.py
│   ├── taylor_series.py
├── utils/
│   ├── exporter.py       # CSV exporting logic
```

## 🔧 Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/fairooz14/Ordinary-Differential-equation-Solver.git
   cd Ordinary-Differential-equation-Solver
   ```
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## 📋 Usage Instructions

1. **Input Data**:
   - Provide `t_values` (time points) and `y_values` (solution points).
   - Optional: Pass additional parameters (`params`) or comparison data.

2. **Enhanced Visualization**:
   - View the main solution curve along with optional error regions and parameter-influenced solutions.

3. **Numerical Results Table**:
   - Scrollable and interactive table displayed below the plot for easy analysis.

---
