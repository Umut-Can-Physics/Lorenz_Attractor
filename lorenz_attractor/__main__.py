from .plotting import plot_lorenz
from .system import solve_lorenz


def main():
    fig = plot_lorenz([1.0, 0.0, 0.0], (0.0, 40.0))
    fig.show()


if __name__ == "__main__":
    main()
