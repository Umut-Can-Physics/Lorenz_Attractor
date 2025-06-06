module LorenzAttractor

export parameterized_lorenz!, plot_Lorenz_attractor_interpolated

using DifferentialEquations
using Plots
using Interpolations

function parameterized_lorenz!(du, u, p, t)
    x, y, z = u
    σ, ρ, β = p
    du[1] = σ * (y - x)
    du[2] = x * (ρ - z) - y
    du[3] = x * y - β * z
    return nothing
end

function plot_Lorenz_attractor_interpolated(u0, tspan, p; N=1000)
    prob = ODEProblem(parameterized_lorenz!, u0, tspan, p)
    sol = solve(prob, Tsit5(), saveat=tspan[1] .+ (tspan[2] - tspan[1]) * (0:N) / N)

    x_interp = LinearInterpolation(sol.t, sol[1, :])
    y_interp = LinearInterpolation(sol.t, sol[2, :])
    z_interp = LinearInterpolation(sol.t, sol[3, :])

    t_interp = range(tspan[1], tspan[2], length=N)

    return plot(x_interp.(t_interp), y_interp.(t_interp), z_interp.(t_interp),
                dpi=400, background_color=:transparent, legend=false, grid=false,
                xaxis=false, yaxis=false, zaxis=false)
end

end # module
