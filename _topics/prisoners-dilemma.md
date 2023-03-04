---
layout: topic
title:  "Prisoners Dilemma"
tag: prisoners-dilemma
note_urls:
    - "https://nashpy.readthedocs.io/en/stable/text-book/cooperation.html"
video_urls:
    - "Repeating the coordination game: repeated games as extensive form games. - [YouTube](https://youtu.be/RTxIw_M4XEY) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=1cd4a3e4-6054-4e34-b104-af930110f136)"
    - "The definition of a Repeated Game - [YouTube](https://youtu.be/0mV43J8MR64) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8323c235-e54d-40c6-bdea-af9301110fb1)"
    - "Mapping histories to actions: strategies in repeated games. - [YouTube](https://youtu.be/2yIt8m9KraE) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b2ee62dc-7d0a-4a55-9d0b-af9301112cb4)"
    - "The impact of reputation: Nash Equilibria in Repeated Games - [YouTube](https://youtu.be/F3TpV77V6xI) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=961c25a2-f98d-4fcd-9f0f-af9301114484)"
    - "Using Python to study Repeated Game with Nashpy - [YouTube](https://youtu.be/s4jF9X86pTg) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=78fed781-91b5-4746-8639-af9301115c24)"
meeting_urls:
    - "https://github.com/drvinceknight/gt/blob/main/do/05-extensive-form-games.rst"
---

## Typical Programming Exercises

1. Output the row player payoff matrix corresponding to an Iterated Prisoners
   Dilemma Tournament (with 200 turns) with the following strategies from the Axelrod library:
   - [`axelrod.TitForTat`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.titfortat.TitForTat)
   - [`axelrod.Random`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.rand.Random)
   - [`axelrod.Grudger`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.grudger.Grudger)
2. Create a variable `A` which has value the row player payoff matrix
corresponding to an Iterated Prisoners Dilemma Tournament (with 200 turns) with
the following strategies from the Axelrod library:
   - [`axelrod.EvolvedFSM16`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.finite_state_machines.EvolvedFSM16)
   - [`axelrod.Adaptive`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.adaptive.Adaptive)
   - [`axelrod.GoByMajority`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.gobymajority.GoByMajority)
3. Output the Nash equilibria that corresponds to the Normal Form Game for the
   following strategies of an Iterated Prisoners Dilemma Tournament (with 200
   turns) from the Axelrod library:
   - [`axelrod.TitForTat`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.titfortat.TitForTat)
   - [`axelrod.Random`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.rand.Random)
   - [`axelrod.Grudger`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.grudger.Grudger)
   - [`axelrod.EvolvedFSM16`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.finite_state_machines.EvolvedFSM16)
   - [`axelrod.Adaptive`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.adaptive.Adaptive)
   - [`axelrod.GoByMajority`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.gobymajority.GoByMajority)
