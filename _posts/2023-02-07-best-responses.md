---
layout: post
title:  "Utility calculations and the start of best responses"
tags:
    - strategies
    - best-responses
---

Today was a fun class: thanks! We spoke about calculating utilities as well as
best responses.

A recording of today is available here: [cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3819dbcc-aeac-487b-baaa-af9d00a567ce](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3819dbcc-aeac-487b-baaa-af9d00a567ce).

In class we finished covering how to calculate the expected utility for each
player (the row and the column player) when we know what strategies they are
playing (\\(\sigma_r\\) and \\(\sigma_c\\)). The notes on this are available at:
[nashpy.readthedocs.io/en/stable/text-book/strategies.html#calculation-of-expected-utilities](https://nashpy.readthedocs.io/en/stable/text-book/strategies.html#calculation-of-expected-utilities).

I also showed how we could use Nashpy to directly compute expected utilities.
The up to date notebook is available [here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-02-03-gt.ipynb).

After this discussion we moved on to looking at what is called a "best
response". We did this by playing the modified matching pennies game against the
following 3 strategies:

- \\(\sigma_r=(.2, .8)\\)
- \\(\sigma_r=(.9, .1)\\)
- \\(\sigma_r=(1/3, 2/3)\\)

In the first two cases there was an intuitive way to play (and indeed a number
of students got the maximum possible score) however in the final
one it was not so clear.

Towards the end of the class we started looking at this a bit more formally
however it was clear there was some confusion. I plan to revisit this on Friday.

The notebook I used to start looking at best responses is available [here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-02-07-gt.ipynb) (at present this contains the code for the random sampling of the strategies -- I will update it with more on Friday).
