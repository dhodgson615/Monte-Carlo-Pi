from random import uniform
from time import sleep

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.pyplot import ion, pause, subplots


def print_intro() -> None:
    """Prints the introduction and explanation of the Monte Carlo π
    approximation.
    """
    print(
        "Monte Carlo π Approximation"
        "\n"
        "\n"
        "This program approximates π using the Monte Carlo method by sampling"
        " random points and finding what fraction fall inside a unit circle."
        "\n"
        "\n"
        "How it Works:"
        "\n"
        "1. Generate random points in a 2×2 square centered at origin"
        "\n"
        "2. Count points where x² + y² ≤ 1 (inside the unit circle)"
        "\n"
        "3. Calculate: π ≈ 4 × (points inside) ÷ (total points)"
    )


def setup_plot() -> tuple[Figure, Axes, Circle]:
    """Sets up the initial plot for the Monte Carlo simulation."""
    ion()
    fig, ax = subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    circle = Circle((0, 0), 1, color="lightblue", fill=False)
    ax.add_patch(circle)
    return fig, ax, circle


def update_plot(
    ax: Axes,
    circle: Circle,
    x_in: list[float],
    y_in: list[float],
    x_out: list[float],
    y_out: list[float],
    pi_approx: float,
    total: int,
) -> None:
    """Updates the plot with the current points and π approximation."""
    ax.clear()
    ax.set_aspect("equal")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.add_patch(circle)
    ax.scatter(x_in, y_in, color="green", s=1, label="Inside Circle")
    ax.scatter(x_out, y_out, color="red", s=1, label="Outside Circle")

    ax.set_title(
        f"Monte Carlo π Approximation\nπ ≈ {pi_approx:.6f} (Samples: {total})"
    )

    ax.legend(loc="upper right")
    pause(0.01)


def monte_carlo_pi() -> None:
    """Runs the Monte Carlo simulation to approximate π."""
    inside, total = 0, 0
    x_in, y_in, x_out, y_out = [], [], [], []
    fig, ax, circle = setup_plot()

    while True:
        x, y = uniform(-1, 1), uniform(-1, 1)
        total += 1

        if x**2 + y**2 <= 1:
            inside += 1
            x_in.append(x)
            y_in.append(y)

        else:
            x_out.append(x)
            y_out.append(y)

        pi_approx = 4 * inside / total
        update_plot(ax, circle, x_in, y_in, x_out, y_out, pi_approx, total)
        time.sleep(0.01)


if __name__ == "__main__":
    print_intro()
    monte_carlo_pi()
