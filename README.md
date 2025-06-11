# LorenzAttractor.jl

This package implements the Lorenz system and provides utilities for plotting
the well known attractor. It is intended as a minimal example for exploring
the dynamics of chaotic systems in Julia.

## Features

- In-place equation definition `lorenz_derivative!`.
- Helper function `plot_lorenz_attractor` that solves and draws
  a smooth trajectory.
- Documentation built with [Documenter.jl](https://juliadocs.github.io/Documenter.jl/).

## Building the Documentation

```bash
julia --project=docs docs/make.jl
```

The generated site will be available in `docs/build`.
