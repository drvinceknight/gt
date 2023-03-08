---
layout: topic
title:  "Best responses"
tag: best-responses
note_urls:
    - "https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#best-responses"
video_urls:
    - "Best way to respond in Game Theory: how to choose what to do when matching pennies. - [YouTube](https://youtu.be/n3vS1jLkMp0) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9ed52684-29a6-4884-97af-af93010fc1bc)"
    - "The definition of a Best Response in Game Theory - [YouTube](https://youtu.be/V0Gyq4OeNVw) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3dcc1ff7-aa24-4390-a1da-af93010fca4c)"
    - "Best responses in small games: exact calculations for 2 by 2 Normal Form Games. - [YouTube](https://youtu.be/SNiZIYCNE90) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e095a55f-7e11-48ee-8b0a-af93010fcfda)"
    - "A general condition for a strategy to be a best response in Game Theory - [YouTube](https://youtu.be/Ms49pMcjeSI) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4273ca0a-5f4d-4463-9308-af93010fd957)"
    - "When no player has a reason to change: Nash equilibrium - [YouTube](https://youtu.be/R0aZ_4vd4cM) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9c1b0cbe-8bde-4024-936e-af93010ff23a)"
    - "Using Python to check if strategies are best responses to each other - [YouTube](https://youtu.be/h6zSP8G1aQw) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4aaf679f-7bd7-4d00-8edc-af9301100d43)"
meeting_urls:
    - "https://github.com/drvinceknight/gt/blob/main/do/02-best-response-condition.md"
---

## Typical Programming Exercises

1. Create a variable `are_best_responses` which has value a tuple of booleans indicating if the following pairs of strategies are best responses to each other for the Normal Form Game when the row player is playing \\(\sigma_r=(.4, .6)\\) and the column player is playing \\(\sigma_c=(0, 1)\\):
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix} \qquad B = \begin{pmatrix}-1 & 1\\ 1 & -1\end{pmatrix}$$
2. Output a tuple of booleans indicating if the following pairs of strategies are best responses to each other for the Normal Form Game when the row player is playing \\(\sigma_r=(1 / 3, 2 / 3)\\) and the column player is playing \\(\sigma_c=(1 / 2, 1 / 2)\\):
   $$A = \begin{pmatrix}3 & 2\\ 3 & 1\end{pmatrix} \qquad B = \begin{pmatrix}4 & 9\\ 5 & 3\end{pmatrix}$$
3. Create a variable `are_best_responses` which has value a tuple of booleans indicating if the following pairs of strategies are best responses to each other for the Normal Form Game when the row player is playing \\(\sigma_r=(0, 1)\\) and the column player is playing \\(\sigma_c=(1/4, 3/4)\\):
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix}$$
4. Output a tuple of booleans indicating if the following pairs of strategies are best responses to each other for the zero sum Normal Form Game when the row player is playing \\(\sigma_r=(0, 1, 0)\\) and the column player is playing \\(\sigma_c=(1/4, 1/4, 1/2)\\):
   $$A = \begin{pmatrix}-3 & - 1 & 4\\ 2 & -1 &  1\\ 0 & 3 & -2\end{pmatrix}$$

[Solutions]({{ site.baseurl }}/assets/solutions/best-responses.ipynb)
