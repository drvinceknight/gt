---
layout: topic
title:  "Support enumeration"
tag: support-enumeration
note_urls:
    - "https://nashpy.readthedocs.io/en/stable/text-book/support-enumeration.html#"
video_urls:
    - "How do we find Nash equilibria in the coordination game? - [YouTube](https://youtu.be/zfcS3jrMjlY) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ce0d19ce-245b-4d77-85cf-af930110238d)"
    - "The support enumeration algorithm. - [YouTube](https://youtu.be/6gx5gSMDav4) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c37a8a28-1136-458b-a6dd-af9301104491)"
    - "Using Python to find Nash Equilibria with Nashpy - [YouTube](https://youtu.be/ggUp9EfkEo8) [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a8d76a65-8772-44f8-b3bf-af9301104ebd)"
meeting_urls:
    - "https://github.com/drvinceknight/gt/blob/main/do/03-support-enumeration.md"
---

## Typical Programming Exercises

1. Create a variable `equilibria` which has value a list containing all equilibria for the Normal Form Game defined by:
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix} \qquad B = \begin{pmatrix}-1 & 1\\ 1 & -1\end{pmatrix}$$
2. Output a list containing all equilibria for the Normal Form Game defined by:
   $$A = \begin{pmatrix}3 & 2\\ 3 & 1\end{pmatrix} \qquad B = \begin{pmatrix}4 & 9\\ 5 & 3\end{pmatrix}$$
3. Create a variable `equilibria` which has value a list containing all equilibria for the Normal Form Game defined by:
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix}$$
4. Output a list containing all equilibria for the Zero sum Normal Form Game defined by:
   $$A = \begin{pmatrix}-3 & - 1 & 4\\ 2 & -1 &  1\\ 0 & 3 & -2\end{pmatrix}$$

[Solutions]({{ site.baseurl }}/assets/solutions/support-enumeration.ipynb)
