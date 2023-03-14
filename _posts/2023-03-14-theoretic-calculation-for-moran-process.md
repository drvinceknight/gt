---
layout: post
title:  "Theoretic calculation for fixation"
tags:
    - moran-process
---

In class today we revisited the [Moran
Process](https://vknight.org/gt/topics/moran-processes.html) and specifically we
looked at calculating so called fixation probabilities analytically.

You can see a recording of this here:
[cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=09358805-0821-4a71-b50d-afc000a5ac93](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=09358805-0821-4a71-b50d-afc000a5ac93)

The notions considered follow the class text closely which you can read here:
[nashpy.readthedocs.io/en/stable/text-book/moran-process.html](https://nashpy.readthedocs.io/en/stable/text-book/moran-process.html).

The formula for the respective fitness values used is:

$$
\begin{aligned}
   f_{1i} &= \frac{3(N-i)}{N - 1}=3\frac{N-i}{N-1}\\
   f_{2i} &= \frac{i+2(N - i -1)}{N - 1}=\frac{2N-2-i}{N - 1}\\
\end{aligned}
$$

For \\(N=3\\) this gives (recall we're using the [Hawk Dove game](https://nashpy.readthedocs.io/en/stable/text-book/normal-form-games.html#hawk-dove-game))


$$f_{1}(1)=3\qquad f_{1}(2)=\frac{3}{2}$$

and:

$$f_{2}(1)=\frac{3}{2}\qquad f_{2}(2)=1$$

Which leads to:

$$\gamma_1=\frac{1}{2}\qquad \gamma_2=\frac{2}{3}$$

Thus, applying [the
formula](https://nashpy.readthedocs.io/en/stable/text-book/moran-process.html#fixation-probability)
we get:

$$
x_1 = \frac{1}{1 + 1/2 + 1/2\times2/3}=\frac{1}{11/6}\approx.545455
$$

This is not far from [the approximations we simulated](
{{site.baseurl}}/2023/03/10/moran-process.html).

This was/is our last so called "content" based class, everything from here will
be preparing for your assessment: both the individual and the group.
