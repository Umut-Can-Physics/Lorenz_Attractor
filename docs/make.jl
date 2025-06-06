using Documenter
using LorenzAttractor

makedocs(
    sitename = "LorenzAttractor.jl",
    modules = [LorenzAttractor],
    format = Documenter.HTML(),
    pages = [
        "Home" => "index.md",
    ],
)

deploydocs(devbranch = "main")

