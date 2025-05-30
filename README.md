# Monte Carlo $\pi$ Approximation

[Live Demo on
Streamlit](https://monte-carlo-pi-efxp3lntxpzv8g8wm6ejbv.streamlit.app)

This project demonstrates how to approximate the value of $\pi$ using the [Monte
Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method). The algorithm
randomly samples points in a square and estimates $\pi$ based on the proportion
of points that fall inside a unit circle.

## How It Works

1. Randomly generate points $(x, y)$ within a square of side length 2, centered
   at the origin.

2. Check if each point lies inside the unit circle using the condition: $x^2 +
   y^2 \leq 1$.

3. Approximate $\pi$ using the formula $\pi \approx \frac{4n}{T}$, where $n$ is
   the number of points inside the circle, and $T$ is the total number of points.

## Features

- Interactive visualization of the Monte Carlo process

- Streamlit web app for instant browser-based exploration

- Local Matplotlib animation for desktop use

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/dhodgson615/Monte-Carlo-Pi
cd Monte-Carlo-Pi
pip3 install -r requirements.txt
```

## Running Locally

**Matplotlib Animation:** Run `python3 local_monte.py` to see the process in a
desktop window.

**Streamlit Web App:** Run `streamlit run streamlit_app.py` to launch the
interactive web app.

## Project Structure

- `local_monte.py` - Local visualization using Matplotlib
- `streamlit_app.py` - Interactive web app using Streamlit
