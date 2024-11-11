import matplotlib.pyplot as plt

def midpoint_circle(radius):
    x, y = 0, radius
    p = 1 - radius
    x_coords, y_coords = [], []

    def plot_circle_points(xc, yc, x, y):
        x_coords.extend([xc + x, xc - x, xc + x, xc - x, xc + y, xc - y, xc + y, xc - y])
        y_coords.extend([yc + y, yc + y, yc - y, yc - y, yc + x, yc + x, yc - x, yc - x])

    xc, yc = 0, 0  # Center of circle at origin
    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

    return x_coords, y_coords

# Circle with radius 10
x_coords, y_coords = midpoint_circle(10)
plt.scatter(x_coords, y_coords)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Midpoint Circle Drawing Algorithm")
plt.axis("equal")
plt.show()