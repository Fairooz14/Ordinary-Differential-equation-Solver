import numpy as np

def euler_method(eq, y0, t0, t_end, h):
    def f(t, y):
        return eval(eq)

    t_values = np.arange(t0, t_end + h, h)
    y_values = [y0]

    for i in range(1, len(t_values)):
        y_values.append(y_values[-1] + h * f(t_values[i - 1], y_values[-1]))

    return t_values, y_values

