import matplotlib.pyplot as plt

def dda_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x0, y0
    x_coords, y_coords = [], []

    for _ in range(steps):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc

    return x_coords, y_coords

# Draw line from (2, 3) to (15, 10)
x_coords, y_coords = dda_line(2, 3, 15, 10)
plt.plot(x_coords, y_coords, 'bo-')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("DDA Line Drawing Algorithm")
plt.show()