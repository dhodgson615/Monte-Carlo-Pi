from time import time

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.pyplot import ion, pause, subplots
from numpy import column_stack, empty
from numpy.random import uniform


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


def monte_carlo_pi(batch: int = 1000, redraw_every: int = 1) -> None:
    """Approximates π using the Monte Carlo method with real-time
    plotting.
    """
    inside, total = 0, 0
    x_in, y_in, x_out, y_out = [], [], [], []
    fig, ax, circle = setup_plot()
    scatter_in = ax.scatter([], [], color="green", s=1, label="Inside Circle")
    scatter_out = ax.scatter([], [], color="red", s=1, label="Outside Circle")
    title = ax.set_title("Monte Carlo π Approximation\nπ ≈ 0.0 (Samples: 0)")
    ax.legend(loc="upper right")
    batch_count = 0
    t0 = time()

    try:
        while True:
            x, y = uniform(-1.0, 1.0, size=batch), uniform(
                -1.0, 1.0, size=batch
            )

            mask = (x * x + y * y) <= 1.0
            n_in = int(mask.sum())
            inside += n_in
            total += batch

            if n_in:
                xi = x[mask].tolist()
                yi = y[mask].tolist()
                x_in.extend(xi)
                y_in.extend(yi)

            n_out = batch - n_in

            if n_out:
                xo = x[~mask].tolist()
                yo = y[~mask].tolist()
                x_out.extend(xo)
                y_out.extend(yo)

            batch_count += 1

            if batch_count >= redraw_every:
                batch_count = 0
                pi_approx = 4.0 * inside / total

                scatter_in.set_offsets(
                    column_stack((x_in, y_in)) if x_in else empty((0, 2))
                )

                scatter_out.set_offsets(
                    column_stack((x_out, y_out)) if x_out else empty((0, 2))
                )

                title.set_text(
                    f"Monte Carlo π Approximation\nπ ≈ {pi_approx:.6f} "
                    f"(Samples: {total})"
                )

                fig.canvas.draw_idle()
                pause(0.001)

    except KeyboardInterrupt:
        elapsed = time() - t0
        print(
            f"\nStopped after {total} samples, π ≈ "
            f"{4.0 * inside / total:.6f}, {total/elapsed:.0f} samples/s"
        )


if __name__ == "__main__":
    print_intro()
    monte_carlo_pi(batch=2000, redraw_every=1)
