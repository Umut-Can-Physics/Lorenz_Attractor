"""
    plot_lorenz_attractor(u0, tspan, params; points=1000)

Solve the Lorenz equations starting at `u0` over `tspan` and return a 3-D plot
of the trajectory. The optional keyword `points` controls the number of
interpolation points used to smooth the plot.
"""
function plot_lorenz_attractor(u0, tspan, params; points=1000)
    prob = ODEProblem(lorenz_derivative!, u0, tspan, params)
    sol = solve(prob, Tsit5(), saveat=range(tspan[1], tspan[2], length=points+1))

    x_interp = LinearInterpolation(sol.t, sol[1, :])
    y_interp = LinearInterpolation(sol.t, sol[2, :])
    z_interp = LinearInterpolation(sol.t, sol[3, :])

    t_interp = range(tspan[1], tspan[2], length=points)

    return plot(x_interp.(t_interp), y_interp.(t_interp), z_interp.(t_interp),
                dpi=400, background_color=:transparent, legend=false, grid=false,
                xaxis=false, yaxis=false, zaxis=false)
end
