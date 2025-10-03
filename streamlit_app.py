from random import uniform

from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.pyplot import subplots
from streamlit import (button, latex, progress, pyplot, session_state,
                       subheader, text_area, title, write)

s = session_state


def show_intro() -> None:
    """Displays the introduction and explanation of the Monte Carlo π
    approximation.
    """
    title("Monte Carlo π Approximation")

    write(
        "This app uses the Monte Carlo method to approximate π by randomly "
        "sampling points and calculating what fraction fall inside a unit "
        "circle."
    )

    subheader("How it Works:")

    write(
        "We randomly place points in a square and check if they're in the "
        "circle:"
    )

    latex(r"x^2 + y^2 \leq 1")
    write("Then we calculate π using:")

    latex(
        r"\pi \approx 4 \cdot \frac{\text{Points inside circle}}"
        r"{\text{Total points}}"
    )

    write("More points = better approximation.")


def plot_points(
    x_in: list[float],
    y_in: list[float],
    x_out: list[float],
    y_out: list[float],
    pi_approx: float,
    total: int,
) -> Figure:
    """Plots the points and the current approximation of π."""
    fig, ax = subplots(figsize=(5, 5))
    ax.set_aspect("equal")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.add_patch(Circle((0, 0), 1, color="lightblue", fill=False))
    ax.scatter(x_in, y_in, color="green", s=1, label="Inside Circle")
    ax.scatter(x_out, y_out, color="red", s=1, label="Outside Circle")
    ax.set_title(f"π ≈ {pi_approx:.6f} (Samples: {total})")
    ax.legend(loc="upper right")
    return fig


def main() -> None:
    """Main function to run the Monte Carlo simulation."""
    show_intro()
    num_points = 10_000

    if "inside" not in s:
        s.inside, s.total = 0, 0
        s.x_in, s.y_in, s.x_out, s.y_out = [], [], [], []
        s.simulation_complete = False

    button_label = "Run Simulation" if s.total == 0 else "Rerun"

    if button(button_label, key="run_button"):
        s.inside, s.total = 0, 0
        s.x_in, s.y_in, s.x_out, s.y_out = [], [], [], []
        s.simulation_complete = False
        p = progress(0)

        for i in range(num_points):
            x, y = uniform(-1, 1), uniform(-1, 1)
            s.total += 1

            if x**2 + y**2 <= 1:
                s.inside += 1
                s.x_in.append(x)
                s.y_in.append(y)

            else:
                s.x_out.append(x)
                s.y_out.append(y)

            p.progress((i + 1) / num_points)

        s.simulation_complete = True

    # Display the current plot if we have points
    if s.total > 0:
        pi_approx = 4 * s.inside / s.total

        fig = plot_points(
            s.x_in,
            s.y_in,
            s.x_out,
            s.y_out,
            pi_approx,
            s.total,
        )

        pyplot(fig)

        if s.simulation_complete:
            text_area(
                "Final Result",
                f"π approximation: {pi_approx:.4f}",
                height=70,
                disabled=True,
            )


if __name__ == "__main__":
    main()
