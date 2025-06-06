```@meta
CurrentModule = LorenzAttractor
```

# LorenzAttractor.jl

`LorenzAttractor.jl` provides a simple implementation of the classic
Lorenz system together with a convenience function for plotting the
resulting attractor.

## Installation

```julia
using Pkg
Pkg.add(url="https://github.com/your/repo")
```

## Usage

```julia
using LorenzAttractor

u0 = [1.0, 0.0, 0.0]
tspan = (0.0, 20.0)
p = [10.0, 28.0, 8/3]

plot_Lorenz_attractor_interpolated(u0, tspan, p)
```

## API

```@autodocs
Modules = [LorenzAttractor]
```
