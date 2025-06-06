# LorenzAttractor.jl

This package implements the Lorenz system and provides utilities for plotting
the well known attractor. It is intended as a minimal example for exploring
the dynamics of chaotic systems in Julia.

## Features

- In-place equation definition `parameterized_lorenz!`.
- Helper function `plot_Lorenz_attractor_interpolated` that solves and draws
  a smooth trajectory.
- Documentation built with [Documenter.jl](https://juliadocs.github.io/Documenter.jl/).

## Building the Documentation

```bash
julia --project=docs docs/make.jl
```

The generated site will be available in `docs/build`.
