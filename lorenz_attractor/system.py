"""Numerical integration and derivative functions for the Lorenz system."""

from typing import Iterable, Tuple, List


def lorenz_derivative(state: Iterable[float], sigma: float, rho: float, beta: float) -> List[float]:
    """Return the derivatives for a given state."""
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


def solve_lorenz(
    u0: Iterable[float],
    tspan: Tuple[float, float],
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    dt: float = 0.01,
) -> Tuple[List[float], List[List[float]]]:
    """Solve the Lorenz system using a 4th order Runge-Kutta method."""
    t0, t1 = tspan
    n = int((t1 - t0) / dt)
    times = [t0 + i * dt for i in range(n + 1)]
    state = list(u0)
    sol = [state.copy()]
    for _ in range(n):
        x, y, z = state
        # k1
        k1x = sigma * (y - x)
        k1y = x * (rho - z) - y
        k1z = x * y - beta * z

        # k2
        x2 = x + dt * k1x / 2
        y2 = y + dt * k1y / 2
        z2 = z + dt * k1z / 2
        k2x = sigma * (y2 - x2)
        k2y = x2 * (rho - z2) - y2
        k2z = x2 * y2 - beta * z2

        # k3
        x3 = x + dt * k2x / 2
        y3 = y + dt * k2y / 2
        z3 = z + dt * k2z / 2
        k3x = sigma * (y3 - x3)
        k3y = x3 * (rho - z3) - y3
        k3z = x3 * y3 - beta * z3

        # k4
        x4 = x + dt * k3x
        y4 = y + dt * k3y
        z4 = z + dt * k3z
        k4x = sigma * (y4 - x4)
        k4y = x4 * (rho - z4) - y4
        k4z = x4 * y4 - beta * z4

        state = [
            x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6,
            y + dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6,
            z + dt * (k1z + 2 * k2z + 2 * k3z + k4z) / 6,
        ]
        sol.append(state.copy())
    return times, sol
