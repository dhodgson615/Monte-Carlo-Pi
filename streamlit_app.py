import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import time

# Streamlit app configuration
st.set_page_config(page_title="Monte Carlo π Approximation", layout="centered")

# Title of the app
st.title("Monte Carlo π Approximation")
st.write("This app uses a Monte Carlo method to approximate π by randomly sampling points within a unit square.")

# Streamlit elements
placeholder = st.empty()
inside_circle = 0
total_samples = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Infinite loop for sampling and updating visualization
while True:
    # Generate random points and calculate whether they are inside the circle
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    total_samples += 1

    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

    # Update the approximation of π
    pi_approximation = 4 * inside_circle / total_samples

    # Plot the results
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Draw the unit circle
    ax.add_patch(Circle((0, 0), 1, color='lightblue', fill=False))

    # Scatter plot points
    ax.scatter(x_inside, y_inside, color='green', s=1, label='Inside Circle')
    ax.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')

    # Title and legend
    ax.set_title(f"Monte Carlo π Approximation\nπ ≈ {pi_approximation:.6f} (Samples: {total_samples})")
    ax.legend(loc='upper right')

    # Display the plot in Streamlit
    placeholder.pyplot(fig)

    # Add a small delay for visualization
    time.sleep(0.01)
