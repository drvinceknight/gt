import axelrod as axl

first_tournament_participants_ordered_by_reported_rank = [s() for s in axl.axelrod_first_strategies]
tournament = axl.Tournament(
     players=first_tournament_participants_ordered_by_reported_rank,
     turns=200,
     repetitions=500,
     seed=1,
)
results = tournament.play()

plot = axl.Plot(results)
p = plot.boxplot()
p.savefig("main.pdf", transparent=True)
