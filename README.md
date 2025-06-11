# Lorenz Attractor

A small Python package for simulating the Lorenz system and plotting its chaotic attractor.

## Installation

```bash
pip install -e .[plot]
```

## Usage

```python
from lorenz_attractor import solve_lorenz, plot_lorenz

u0 = [1.0, 0.0, 0.0]
tspan = (0.0, 20.0)

# Integrate the system
_, sol = solve_lorenz(u0, tspan)

# Create a plot (requires matplotlib)
fig = plot_lorenz(u0, tspan)
fig.show()
```

## Testing

Run the tests with `pytest`:

```bash
pytest
```
