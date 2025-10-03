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
    st.title("Monte Carlo π Approximation")
    st.write(
        "This app uses the Monte Carlo method to approximate π by randomly "
        "sampling points and calculating what fraction fall inside a unit "
        "circle."
    )
    st.subheader("How it Works:")
    st.write(
        "We randomly place points in a square and check if they're in the "
        "circle:"
    )
    st.latex(r"x^2 + y^2 \leq 1")
    st.write("Then we calculate π using:")
    st.latex(
        r"\pi \approx 4 \cdot \frac{\text{Points inside circle}}"
        r"{\text{Total points}}"
    )
    st.write("More points = better approximation.")


def plot_points(
    x_in: list[float],
    y_in: list[float],
    x_out: list[float],
    y_out: list[float],
    pi_approx: float,
    total: int,
) -> plt.Figure:
    """Plots the points and the current approximation of π."""
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=(5, 5))
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
    num_points: int = 10_000

    # Initialize session state for simulation data
    if "inside" not in st.session_state:
        st.session_state.inside = 0
        st.session_state.total = 0
        st.session_state.x_in = []
        st.session_state.y_in = []
        st.session_state.x_out = []
        st.session_state.y_out = []
        st.session_state.simulation_complete = False

    # Button to start or rerun simulation
    button_label = "Run Simulation" if st.session_state.total == 0 else "Rerun"
    if st.button(button_label, key="run_button"):
        # Reset state
        st.session_state.inside = 0
        st.session_state.total = 0
        st.session_state.x_in = []
        st.session_state.y_in = []
        st.session_state.x_out = []
        st.session_state.y_out = []
        st.session_state.simulation_complete = False

        # Generate num_points with a progress bar
        progress = st.progress(0)
        i: int
        for i in range(num_points):
            x: float
            y: float
            x, y = random.uniform(-1, 1), random.uniform(-1, 1)
            st.session_state.total += 1

            if x**2 + y**2 <= 1:
                st.session_state.inside += 1
                st.session_state.x_in.append(x)
                st.session_state.y_in.append(y)
            else:
                st.session_state.x_out.append(x)
                st.session_state.y_out.append(y)

            # Update progress bar
            progress.progress((i + 1) / num_points)

        st.session_state.simulation_complete = True

    # Display the current plot if we have points
    if st.session_state.total > 0:
        pi_approx: float = 4 * st.session_state.inside / st.session_state.total
        fig: Figure = plot_points(
            st.session_state.x_in,
            st.session_state.y_in,
            st.session_state.x_out,
            st.session_state.y_out,
            pi_approx,
            st.session_state.total,
        )
        st.pyplot(fig)

        # Show final approximation in text box if simulation is complete
        if st.session_state.simulation_complete:
            st.text_area(
                "Final Result",
                f"π approximation: {pi_approx:.4f}",
                height=70,
                disabled=True,
            )


if __name__ == "__main__":
    main()
