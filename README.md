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

When hosted on GitHub, the documentation is automatically deployed to the
`gh-pages` branch using GitHub Actions. You can view the rendered pages at
`https://<USERNAME>.github.io/Lorenz_Attractor` (replace `<USERNAME>` with your
GitHub handle).
