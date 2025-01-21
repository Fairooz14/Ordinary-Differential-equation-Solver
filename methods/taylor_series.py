import numpy as np

def taylor_series_method(eq, y0, t0, t_end, h):
    def f(t, y):
        return eval(eq)

    def f_prime(t, y):
        return eval(eq.replace("y", f"({f(t, y)})"))

    t_values = np.arange(t0, t_end + h, h)
    y_values = [y0]

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[-1]

        y_next = y + h * f(t, y) + (h ** 2 / 2) * f_prime(t, y)
        y_values.append(y_next)

    return t_values, y_values

