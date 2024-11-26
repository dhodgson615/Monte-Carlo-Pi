import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import time

# Explanation and Initialization
print("Monte Carlo π Approximation")
print("""
This program uses the Monte Carlo method to approximate the value of π.
The method works by randomly sampling points in a square and calculating 
the ratio of points that fall inside a unit circle to the total number of points.

How it Works:
1. Randomly generate points (x, y) in a square of side length 2, centered at the origin.
2. Check if each point lies inside the unit circle by testing the condition:
   x^2 + y^2 <= 1
3. The ratio of points inside the circle to the total number of points approximates π:
   π ≈ 4 * (Number of points inside the circle) / (Total number of points)
""")

# Initialize variables
inside_circle = 0
total_samples = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Create the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Draw the unit circle
circle = Circle((0, 0), 1, color='lightblue', fill=False)
ax.add_patch(circle)

# Infinite loop for sampling and updating visualization
while True:
    # Generate random points
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    total_samples += 1

    # Check if the point is inside the circle
    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

    # Approximate π
    pi_approximation = 4 * inside_circle / total_samples

    # Update the plot
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.add_patch(circle)
    ax.scatter(x_inside, y_inside, color='green', s=1, label='Inside Circle')
    ax.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')

    # Add a title with π approximation
    ax.set_title(f"Monte Carlo π Approximation\nπ ≈ {pi_approximation:.6f} (Samples: {total_samples})")
    ax.legend(loc='upper right')

    # Display the updated plot
    plt.pause(0.01)  # Pause briefly to allow the plot to update

    # Add a small delay for the loop to run smoothly
    time.sleep(0.01)
