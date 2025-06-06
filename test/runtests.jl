using Test
using LorenzAttractor
using Plots

@testset "LorenzAttractor" begin
    du = zeros(3)
    u = [1.0, 0.0, 0.0]
    p = [10.0, 28.0, 8/3]
    LorenzAttractor.parameterized_lorenz!(du, u, p, 0.0)
    @test du ≈ [-10.0, 28.0, 0.0]

    plt = LorenzAttractor.plot_Lorenz_attractor_interpolated(u, (0.0, 1.0), p; N=10)
    @test plt isa Plots.Plot
end
