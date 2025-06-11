"""
    lorenz_derivative!(du, state, params, t)

Compute the derivatives of the Lorenz system in-place. The state vector
`state = (x, y, z)` evolves according to the parameters `params = (σ, ρ, β)`.
The result is written to `du`.
"""
function lorenz_derivative!(du, state, params, t)
    x, y, z = state
    sigma, rho, beta = params
    du[1] = sigma * (y - x)
    du[2] = x * (rho - z) - y
    du[3] = x * y - beta * z
    return nothing
end
