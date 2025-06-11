"""Plotting utilities for the Lorenz attractor."""

from typing import Iterable, Tuple


def plot_lorenz(
    u0: Iterable[float],
    tspan: Tuple[float, float],
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    dt: float = 0.01,
):
    """Return a matplotlib figure of the Lorenz attractor."""
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise RuntimeError("matplotlib is required for plotting") from exc
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    from .system import solve_lorenz

    _t, sol = solve_lorenz(u0, tspan, sigma, rho, beta, dt)
    xs = [s[0] for s in sol]
    ys = [s[1] for s in sol]
    zs = [s[2] for s in sol]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    return fig
