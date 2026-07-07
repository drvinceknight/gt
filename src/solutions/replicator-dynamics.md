---
layout: solution
title: "Replicator Dynamics"
tag: "replicator-dynamics"
---

# Replicator Dynamics: worked solutions

Solutions to the example questions on the
[Replicator Dynamics](/topics/replicator-dynamics.html) page. Each question is
worth 25 marks.

## Question 1 [25 marks]

**(a) Fitnesses.** [3]

\[
f_D = 3x + 2(1 - x) = x + 2, \qquad f_S = 4x + 0(1 - x) = 4x.
\]

**(b) Replicator equation.** [7]

\[
\dot{x} = x(f_D - \phi) = x(1 - x)(f_D - f_S) = x(1 - x)\bigl((x + 2) - 4x\bigr)
= x(1 - x)(2 - 3x).
\]

**(c) Stable populations.** [3]

Setting \(\dot{x} = 0\) gives the stable populations \(x = 0\), \(x = 1\) and
\(x = \tfrac{2}{3}\).

**(d) Which is approached.** [6]

For \(0 < x < \tfrac{2}{3}\) the factor \((2 - 3x) > 0\), so \(\dot{x} > 0\); for
\(\tfrac{2}{3} < x < 1\) it is negative, so \(\dot{x} < 0\). From any interior
start the dynamics therefore approach \(x = \tfrac{2}{3}\), while \(x = 0\) and
\(x = 1\) are repelling. This is exactly where the class settled: about
two-thirds of the room playing Dig.

**(e) ESS.** [6]

Yes, \(x = \tfrac{2}{3}\) is an ESS. It is an interior stable population to which
the dynamics return: from part (d), \(\dot{x} > 0\) for \(x < \tfrac{2}{3}\) and
\(\dot{x} < 0\) for \(x > \tfrac{2}{3}\), so the population returns to it after any
small perturbation. Equivalently, by the invasion condition, at \(x = \tfrac{2}{3}\)
the two strategies are equally fit (\(f_D = f_S\)). A small invasion that raises
\(x\) above \(\tfrac{2}{3}\) makes \(f_D - f_S = 2 - 3x < 0\), so the now more
numerous Dig type earns less and is selected against; an invasion that lowers
\(x\) makes \(f_D > f_S\) and Dig recovers. Either way the invading mix earns a
lower fitness than the resident, so it cannot spread: \(x = \tfrac{2}{3}\) is
evolutionarily stable.

## Question 2 [25 marks]

**(a) Replicator equation.** (Bookwork.) [3]

\[
\dot{x}_1 = x_1(f_1(x) - \phi), \qquad \phi = x_1 f_1(x) + x_2 f_2(x).
\]

**(b)(i) Interpretation.** [2]

Each fitness is a base value of \(1\) (the payoff to not crashing) plus a term
increasing in the proportion of others using the same side, since matching the
majority lowers the chance of a collision.

**(b)(ii) Replicator equation.** [6]

\[
\dot{x} = x(1 - x)(f_L - f_R) = x(1 - x)\bigl((1 + x) - (2 - x)\bigr) = x(1 - x)(2x - 1).
\]

**(b)(iii) Stable populations.** [4]

Setting \(\dot{x} = 0\) gives the stable populations \(x = 0\), \(x = 1\) and
\(x = \tfrac{1}{2}\).

**(b)(iv) Stability and ESS.** [8]

Examining the sign of \(\dot{x} = x(1 - x)(2x - 1)\):

- Near \(x = \tfrac{1}{2}\): for \(x < \tfrac{1}{2}\), \((2x - 1) < 0\) so
  \(\dot{x} < 0\); for \(x > \tfrac{1}{2}\), \(\dot{x} > 0\). The dynamics move
  **away** from \(x = \tfrac{1}{2}\), so it is repelling and not an ESS.
- Near \(x = 0\): \(\dot{x} < 0\) for small \(x > 0\), so the population returns
  to \(0\); it is approached.
- Near \(x = 1\): \(\dot{x} > 0\) for \(x\) just below \(1\), so the population
  returns to \(1\); it is approached.

The stable populations \(x = 0\) (everyone drives right) and \(x = 1\) (everyone
drives left) are approached and are the evolutionarily stable strategies; the
mixed population \(x = \tfrac{1}{2}\) is a stable population in the sense
\(\dot{x} = 0\) but is repelling, so it is not an ESS.

**(b)(v) Two stable populations.** [2]

The game has two stable populations the dynamics can settle on, \(x = 0\) and
\(x = 1\), separated by the unstable population \(x = \tfrac{1}{2}\). Which side
everyone ends up on is determined by history: whichever side starts in the
majority is reinforced and takes over. Because \(x = \tfrac{1}{2}\) is unstable,
any tiny imbalance grows, so the symmetric mixed population is never observed: a
population settles on a single convention, all driving left or all driving
right.

## Question 3 [25 marks]

**(a) Fitnesses and average fitness.** [5]

Each fitness is the corresponding row of \(A x\):

\[
f_R = x_S - x_P, \qquad f_P = x_R - x_S, \qquad f_S = x_P - x_R.
\]

The average fitness is

\[
\phi = x_R f_R + x_P f_P + x_S f_S
= x_R(x_S - x_P) + x_P(x_R - x_S) + x_S(x_P - x_R) = 0,
\]

since \(A\) is antisymmetric and every term cancels in pairs.

**(b) Replicator equations.** [4]

With \(\phi = 0\), the replicator equation \(\dot{x}_i = x_i(f_i - \phi)\)
reduces to

\[
\dot{x}_R = x_R(x_S - x_P), \qquad
\dot{x}_P = x_P(x_R - x_S), \qquad
\dot{x}_S = x_S(x_P - x_R).
\]

**(c) Interior stable population.** [5]

At an interior stable population every proportion is positive and each
\(\dot{x}_i = 0\), so we need \(f_R = f_P = f_S = 0\). From \(f_R = 0\) we get
\(x_S = x_P\), and from \(f_P = 0\) we get \(x_R = x_S\). Hence
\(x_R = x_P = x_S\), and with \(x_R + x_P + x_S = 1\) this gives the unique
interior stable population \(x_R = x_P = x_S = \tfrac{1}{3}\).

**(d) A constant of motion.** [7]

Along any interior trajectory,

\[
\begin{aligned}
\frac{d}{dt} \ln H
&= \frac{d}{dt}\bigl(\ln x_R + \ln x_P + \ln x_S\bigr) \\
&= \frac{\dot{x}_R}{x_R} + \frac{\dot{x}_P}{x_P} + \frac{\dot{x}_S}{x_S} \\
&= \frac{x_R f_R}{x_R} + \frac{x_P f_P}{x_P} + \frac{x_S f_S}{x_S} \\
&= f_R + f_P + f_S \\
&= (x_S - x_P) + (x_R - x_S) + (x_P - x_R) = 0.
\end{aligned}
\]

Hence \(\ln H\), and so \(H = x_R x_P x_S\) itself, keeps the same value all the
way along a trajectory. We can use this to see how the dynamics behave. Suppose
we start in the interior, so all three proportions are positive and \(H > 0\). If
one of the proportions ever dropped to zero, the product \(H = x_R x_P x_S\)
would be zero too; but \(H\) cannot change, so this never happens and the
trajectory stays away from the edges of the simplex. Equally, the dynamics cannot
drift in to the centre and stop there, because the centre is the only fixed
point and any other starting value of \(H\) is different from its value there.

The trajectory is therefore boxed in: it can never settle down (the only
resting point is the centre, which it does not start at) and it can never reach
the edges. With nowhere to go, it simply loops back on itself, tracing a closed
curve around the centre \(\left(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\right)\)
and repeating the same cycle forever. A small perturbation away from the centre
neither grows nor shrinks; it just circulates. The interior population is
therefore stable, in that nearby populations stay nearby, but not asymptotically
stable, since the dynamics never return to it.

**(e) Not an ESS.** [4]

An evolutionarily stable strategy must be asymptotically stable under the
replicator dynamics. From part (d) the interior population is only stable, not
asymptotically stable, so \(\left(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\right)\)
is not an ESS. This reflects the cyclic structure of the game: Rock beats
Scissors, Scissors beats Paper, and Paper beats Rock. Whenever one strategy
becomes common the strategy that beats it gains, so the population chases its
own tail through Rock, Paper and Scissors without ever settling.

## Question 4 [25 marks]

**(a) The function is non-negative.** [5]

Write \(V(x) = -\sum_i x^{*}_i \ln\!\dfrac{x_i}{x^{*}_i}\). Since \(\ln\) is
concave and the weights \(x^{*}_i\) sum to one, Jensen's inequality gives

\[
\sum_i x^{*}_i \ln\!\frac{x_i}{x^{*}_i}
\le \ln\!\left(\sum_i x^{*}_i \frac{x_i}{x^{*}_i}\right)
= \ln\!\left(\sum_i x_i\right) = \ln 1 = 0.
\]

Hence \(V(x) \ge 0\). Equality in Jensen's inequality holds only when the ratios
\(x_i/x^{*}_i\) are all equal; since both \(x\) and \(x^{*}\) sum to one this
forces \(x = x^{*}\).

**(b) Its rate of change.** [9]

Differentiating along a trajectory, and using \(\sum_i x^{*}_i = 1\),

\[
\frac{d}{dt} V
= -\sum_i x^{*}_i \frac{\dot{x}_i}{x_i}.
\]

The replicator dynamics give \(\dot{x}_i = x_i\bigl(f_i - \phi\bigr)\), with
\(f_i = (A x)_i\) the fitness of strategy \(i\) and \(\phi = x A x\) the average
fitness, so \(\dot{x}_i / x_i = f_i - \phi\). Therefore

\[
\frac{d}{dt} V
= -\sum_i x^{*}_i\bigl(f_i - \phi\bigr)
= -\left(\sum_i x^{*}_i f_i - \phi\right)
= -\bigl(x^{*} A x - x A x\bigr),
\]

since \(\sum_i x^{*}_i f_i = x^{*} A x\) and \(\phi = x A x\).

**(c) Asymptotic stability.** [6]

For \(x \neq x^{*}\) near \(x^{*}\) the evolutionarily stable strategy condition
gives \(x^{*} A x > x A x\), so \(x^{*} A x - x A x > 0\) and hence
\(\tfrac{d}{dt} V < 0\). Together with part (a), \(V\) is positive away from
\(x^{*}\), zero at \(x^{*}\), and strictly decreasing along every nearby
trajectory. It is therefore a Lyapunov function, and \(x^{*}\) is asymptotically
stable: nearby populations not only stay close but converge to \(x^{*}\).

**(d) Contrast with Rock-Paper-Scissors.** [5]

In the Rock-Paper-Scissors game of Question 3 the interior population is only
neutrally stable, not an evolutionarily stable strategy, so the inequality
\(x^{*} A x > x A x\) fails: the antisymmetry of the payoff matrix makes
\(x^{*} A x = x A x\) for every \(x\). The same calculation then gives
\(\tfrac{d}{dt} V = 0\), so the cross-entropy neither decreases nor increases. The
natural conserved quantity there is \(H = x_R x_P x_S\), with
\(\tfrac{d}{dt}\ln H = 0\). Because a constant of motion is preserved rather than a
Lyapunov function decreasing, the trajectories cannot approach the centre; they
trace closed orbits around it. The decreasing \(V\) of an evolutionarily stable
strategy gives convergence, whereas the conserved \(H\) of Rock-Paper-Scissors
gives perpetual cycling.
