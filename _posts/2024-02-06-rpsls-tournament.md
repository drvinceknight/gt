---
layout: post
title: "A rock paper scissors lizard spock tournament"
tags:
  - about
  - support-enumeration
---

In class today we bore witness to Tim's talent at Rock Paper Scissors Lizard
Spock and also: not everyone got chocolate.

A recording of the class is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=72a8688a-c9bf-4d2c-84ba-b10900c67881).

### Using Nashpy to check if strategies are best responses to each other

I started the class by showing how to use `nashpy` to check if strategies are
best responses to each other.

You can see the Nashpy documentation for this here: [https://nashpy.readthedocs.io/en/stable/how-to/check-best-responses.html](https://nashpy.readthedocs.io/en/stable/how-to/check-best-responses.html)

You can find a link to a video demonstrating this here: [https://vknight.org/gt/topics/best-responses.html](https://vknight.org/gt/topics/best-responses.html)

You can find the notebook I used in class [here]({{site.baseurl}}/assets/2023-2024/nbs/2024-02-06.ipynb)

### A rock paper scissors lizard tournament

After this we moved on to class rock paper scissors tournament.

The first time I heard of this game (a variation of rock paper scissors) was in
an episode of the Big Bang Theory. You can find a clip of it here:
[YouTube](https://youtu.be/x5Q6-wMx-K8) and a summary of the rules are available
[here](https://github.com/drvinceknight/gt/blob/main/do/static/rpsls/main.pdf).

After everyone played their tournaments (a knock out with a final)
following that there was a "last player standing" session which lead to the
grand final. **Tim** was victorious here (hail Tim) and we then started having a
conversation about what made someone be good at Rock Paper Scissors Lizard
Spock.

Interestingly all the ideas revolved around playing a best response to what you
thought your opponent would do.

One thing I spoke about at the end was how to make that hard to do: being
unpredictable.

Indeed, in this setting the only pair of strategies that are best responses to
each other are:

$$\sigma_r=(1/5, 1/5, 1/5, 1/5, 1/5)$$

and

$$\sigma_c=(1/5, 1/5, 1/5, 1/5, 1/5)$$
