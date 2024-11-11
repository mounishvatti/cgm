import numpy as np
import matplotlib.pyplot as plt

def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    return (translation_matrix @ points.T).T

def rotate(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad), 0], [np.sin(rad), np.cos(rad), 0], [0, 0, 1]])
    return (rotation_matrix @ points.T).T

def scale(points, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    return (scaling_matrix @ points.T).T

# Define a square
points = np.array([[1, 1, 1], [1, 3, 1], [3, 3, 1], [3, 1, 1], [1, 1, 1]])

# Apply transformations
translated_points = translate(points, 2, 2)
rotated_points = rotate(points, 45)
scaled_points = scale(points, 2, 2)

plt.plot(points[:, 0], points[:, 1], 'bo-', label="Original")
plt.plot(translated_points[:, 0], translated_points[:, 1], 'ro-', label="Translated")
plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'go-', label="Rotated")
plt.plot(scaled_points[:, 0], scaled_points[:, 1], 'mo-', label="Scaled")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Transformation (Translation, Rotation, Scaling)")
plt.legend()
plt.grid(True)
plt.show()