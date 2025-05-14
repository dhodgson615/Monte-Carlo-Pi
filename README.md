# [Monte-Carlo-Pi](https://monte-carlo-pi-efxp3lntxpzv8g8wm6ejbv.streamlit.app)

This program uses the Monte Carlo method to approximate the value of $π$.
The method works by randomly sampling points in a square and calculating 
the ratio of points that fall inside a unit circle to the total number of points.

How it Works:
1. Randomly generate points $(x, y)$ in a square of side length 2, centered at the origin.
2. Check if each point lies inside the unit circle by testing the condition:
   $x^2 + y^2 ≤ 1$
3. The ratio of points inside the circle to the total number of points approximates $π$: $π ≈ 4 * \frac{N_{inside}}{T_{points}}$
