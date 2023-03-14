---
layout: topic
title:  "Prisoners Dilemma"
tag: prisoners-dilemma
note_urls:
    - "https://nashpy.readthedocs.io/en/stable/text-book/cooperation.html"
video_urls:
    - "Repeating the Prisoners Dilemma twice: does cooperation emerge? - [YouTube](https://youtu.be/pE79-O7u-NA) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3cb85181-7030-4211-8487-afc500d19504)"
    - "The general form of the Prisoners Dilemma - [YouTube](https://youtu.be/gYlVCc1zbRw) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a3c69fb5-3085-4f9c-9dbe-afc500d19573)"
    - "Axelrod's tournaments: a first computational case of understanding the emergence of cooperation. - [YouTube](https://youtu.be/rrkMbKWMld0) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=64406472-1aab-45ec-ab4b-afc500d19547)"
    - "Using Python to study the Iterated Prisoners Dilemma with the Axelrod library. - [YouTube](https://youtu.be/xzgWIzDdlwk) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=32b8a70f-d619-49df-a4de-afc500d195c8)"
meeting_urls:
    - "https://github.com/drvinceknight/gt/blob/main/do/06-prisoners-dilemma.rst"
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
3. Output the Nash equilibria (as a list) that corresponds to the Normal Form Game for the
   following strategies of an Iterated Prisoners Dilemma Tournament (with 200
   turns) from the Axelrod library:
   - [`axelrod.TitForTat`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.titfortat.TitForTat)
   - [`axelrod.Random`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.rand.Random)
   - [`axelrod.Grudger`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.grudger.Grudger)
   - [`axelrod.EvolvedFSM16`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.finite_state_machines.EvolvedFSM16)
   - [`axelrod.Adaptive`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.adaptive.Adaptive)
   - [`axelrod.GoByMajority`](https://axelrod.readthedocs.io/en/stable/reference/strategy_index.html#axelrod.strategies.gobymajority.GoByMajority)

[Solutions]({{ site.baseurl }}/assets/solutions/prisoners-dilemma.ipynb)
