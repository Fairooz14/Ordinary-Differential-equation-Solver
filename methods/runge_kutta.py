import numpy as np

def runge_kutta_4th_method(eq, y0, t0, t_end, h):
    def f(t, y):
        return eval(eq)

    t_values = np.arange(t0, t_end + h, h)
    y_values = [y0]

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[-1]

        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)

        y_values.append(y + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    return t_values, y_values

