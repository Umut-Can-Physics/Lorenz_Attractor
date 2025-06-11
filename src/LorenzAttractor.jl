module LorenzAttractor

export lorenz_derivative!, plot_lorenz_attractor

using DifferentialEquations
using Plots
using Interpolations

include("lorenz_system.jl")
include("plotting.jl")

end # module
