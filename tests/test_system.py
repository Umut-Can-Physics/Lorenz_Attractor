import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lorenz_attractor import lorenz_derivative, solve_lorenz


def test_derivative():
    du = lorenz_derivative([1.0, 0.0, 0.0], 10.0, 28.0, 8/3)
    assert all(abs(a - b) < 1e-6 for a, b in zip(du, [-10.0, 28.0, 0.0]))


def test_integration_length():
    t, sol = solve_lorenz([1.0, 0.0, 0.0], (0.0, 0.1), dt=0.01)
    assert len(t) == len(sol)
    assert len(t) == 11
