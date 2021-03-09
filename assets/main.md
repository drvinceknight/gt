---
title: Game Theory
---
# Game Theory: Introduction to the course

[Video](https://youtu.be/T50RbGZv-gw)

This course will cover the following aspects of Game Theory:

- Normal form games and Nash equilibrium
- Evolutionary Game Theory
- Some contemporary research

All course materials are available online at [vknight.org/gt/](http://vknight.org/gt/). You can also find all the source files that create that website at [github.com/drvinceknight/gt/](https://github.com/drvinceknight/gt/).

## Course notes

The course notes are written using Jupyter notebooks, you will see mathematics but also Python code used to illustrate and confirm certain results.

For example here is some code verifying the simple identity:

$$
(a + b) ^ 2 = a^2 + 2ab + b ^2.
$$


```python
import sympy as sym  # A library used for symbolic computations
sym.init_printing()  # Use LaTeX to clean up the output
a, b = sym.symbols('a, b')
((a + b) ** 2).expand()
```




$$a^{2} + 2 a b + b^{2}$$



In class we will not follow the course notes: these are there for you to read on your own time. Instead we will use activities and other examples to illustrate the concepts. I have my own notes for those (which are also available to you): http://vkgt.readthedocs.io/en/latest/. 

If you would like some information about the pedagogic approach:

- You can find my "teaching philosophy" here: https://vknight.org/tch-phi/
- Here is a paper describing some of the pedagogic rational for this approach: https://journals.gre.ac.uk/index.php/msor/article/view/254/254

It is possible that the course notes will change: **for things like typos and clarifications**, all of the notes are hosted openly on github and if you're interested you can find a list of all changes here: https://github.com/drvinceknight/gt/commits/master

## Technology in class

Please use whatever resources you need to be successful in this class. Let me know if I can help with anything.

## Office hours

I will hold 2-3 hours a week for office hours during which you may come and get help. Specific hours will be determined collaboratively as a class during the first class meeting.

## Assessment

There are two piece of assessment in this course:

- Individual coursework (25%): **The individual coursework includes a programming component.**
- Exam (75%)
# Normal Form Games

[Video](https://youtu.be/VDZ4I4IoFss?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Game theory is the study of interactive decision making. Consider the following situation:

> Two friends must decide what movie to watch at the cinema. Alice would like to watch a sport movie and Bob would like to watch a comedy. Importantly they would both rather spend their evening together then apart.

To represent this mathematically we will associate **utilities** to the 4 possible outcomes:

1. Alice watches a sport movie, Bob watches a comedy: Alice receives a utility of $1$ and Bob a utility of $1$.
2. Alice watches a comedy, Bob watches a sport movice: Alice receives a utility of $0$ and Bob a utility of $0$.
3. Alice and Bob both watch a sport movie: Alice receives a utility of $3$ and Bob a utility of $2$.
4. Alice and Bob both watch a comedy: Alice receives a utility of $2$ and Bob a utility of $3$.

This is referred to as the "battle of the sexes" and we will represent it using two matrices, $A$ will represent the utilities of Alice:

$$
A = 
\begin{pmatrix}
3 & 1\\
0 & 2
\end{pmatrix}
$$

and matrix $B$ will represent the utilities of Bob:

$$
B = 
\begin{pmatrix}
2 & 1\\
0 & 3
\end{pmatrix}
$$

We refer to **Alice as the row player** and **Bob as the column player**: 

- The row player chooses which row of the matrices the players will gain their utilities;
- The column player chooses which column of the matrices the player will gain their utilities.

Thus if the row player (Alice) chooses the first row (this corresponds to a sport movie) and the column player (Bob) chooses the second column (this corresponds to a comedy):

- The row player receives a utility of $A_{12}=1$
- The column player receives a utility of $B_{12}=1$

This representation of the stategic interaction between Alice and Bob is called a **Normal Form Game**.

---

## Definition of Normal Form Game

[Video](https://youtu.be/tP2WE0FdI0w?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

An \\(N\\) player normal form game consists of:

- A finite set of $N$ players
- Strategy spaces for the players: $\{S_1,S_2,S_3,\dots,S_N\}$;
- Payoff functions for the players: $u_i:S_1\times S_2\dots\times S_N\to\mathbb{R}$

---

**In this course we will only consider the case of $N=2$.**

For the battle of the sexes:

- We have \\(N=2\\) players (Alice and Bob)
- The strategy spaces: $S_1=S_2=\{\text{comedy}, \text{sport movie}\}$ or equivalently $S_1=S_2=\{1, 2\}$
- The payoff functions mapping an element of $\tilde s \in S_1\times S_2=\{(1, 1), (1, 2), (2, 1), (2, 2)\}$ to $\mathbb{R}$:

   $$u_1(\tilde s)=A_{\tilde s},$$
   
   $$u_2(\tilde s)=B_{\tilde s}.$$
   
---

We can use Python to represent these games, we will use the `nashpy` library to do so and we start by building our two matrices:


```python
import nashpy as nash
A = [[3, 1], [0, 2]]
B = [[2, 1], [0, 3]]
```

We then create a `nash.Game` instance:


```python
battle_of_the_sexes = nash.Game(A, B)
battle_of_the_sexes
```




    Bi matrix game with payoff matrices:
    
    Row player:
    [[3 1]
     [0 2]]
    
    Column player:
    [[2 1]
     [0 3]]



In the next chapter we will start to see how to use that for further calculations.

# Examples of other common games

## Prisoners Dilemma

[Video](https://youtu.be/qcQMeiUnfVQ?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

> Assume two thieves have been caught by the police and separated for questioning. If both thieves cooperate and don’t divulge any information they will each get a short sentence. If one defects he/she is offered a deal while the other thief will get a long sentence. If they both defect they both get a medium length sentence.

This corresponds to:

$$
A =
\begin{pmatrix}
    3 & 0\\
    5 & 1
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    3 & 5\\
    0 & 1
\end{pmatrix}
$$


```python
A = [[3, 0], [5, 1]]
B = [[3, 5], [0, 1]]
prisoners_dilemma = nash.Game(A, B)
prisoners_dilemma
```




    Bi matrix game with payoff matrices:
    
    Row player:
    [[3 0]
     [5 1]]
    
    Column player:
    [[3 5]
     [0 1]]



## Hawk Dove game 

[Video](https://youtu.be/_7HtcsVB2uU?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

> Suppose two birds of prey must share a limited resource. The birds can act like a hawk or a dove. Hawks always fight over the resource to the point of exterminating a fellow hawk and/or take a majority of the resource from a dove. Two doves can share the resource.



This corresponds to:

$$
A =
\begin{pmatrix}
    0 & 3\\
    1 & 2
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    0 & 1\\
    3 & 2
\end{pmatrix}
$$


```python
A = [[0, 3], [1, 2]]
B = [[0, 1], [3, 2]]
hawk_dove = nash.Game(A, B)
hawk_dove
```




    Bi matrix game with payoff matrices:
    
    Row player:
    [[0 3]
     [1 2]]
    
    Column player:
    [[0 1]
     [3 2]]



## Pigs

[Video](https://youtu.be/ORGYJdqZkX0?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

> Consider two pigs. One dominant pig and one subservient pig. These pigs share a pen. There is a lever in the pen that delivers food but if either pig pushes the lever it will take them a little while to get to the food. If the dominant pig pushes the lever, the subservient pig has some time to eat most of the food before being pushed out of the way. If the subservient pig push the lever, the dominant pig will eat all the food. Finally if both pigs go to push the lever the subservient pig will be able to eat a third of the food.

This corresponds to:

$$
A =
\begin{pmatrix}
    4 & 2\\
    6 & 0
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    2 & 3\\
    -1 & 0
\end{pmatrix}
$$


```python
A = [[4, 2], [6, 0]]
B = [[2, 3], [-1, 0]]
pigs = nash.Game(A, B)
pigs
```




    Bi matrix game with payoff matrices:
    
    Row player:
    [[4 2]
     [6 0]]
    
    Column player:
    [[ 2  3]
     [-1  0]]



## Matching pennies

[Video](https://youtu.be/80ImlktaeeY?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

>Consider two players who can choose to display a coin either Heads facing up or Tails facing up. If both players show the same face then player 1 wins, if not then player 2 wins.

This corresponds to:

$$
A =
\begin{pmatrix}
    1 & -1\\
    -1 & 1
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    -1 & 1\\
    1 & -1
\end{pmatrix}
$$


```python
A = [[1, -1], [-1, 1]]
B = [[-1, 1], [1, -1]]
matching_pennies = nash.Game(A, B)
matching_pennies
```




    Zero sum game with payoff matrices:
    
    Row player:
    [[ 1 -1]
     [-1  1]]
    
    Column player:
    [[-1  1]
     [ 1 -1]]



As indicated by `nashpy`, this is a `Zero sum game`: 

$$
A + B = 0
$$

---

## Definition of a zero sum game

[Video](https://youtu.be/wUh1KFupLFI?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

A two player normal form game with payoff matrices $A, B$ is called **zero sum** iff:

$$
A = -B
$$

---

To define a zero sum game using `nashpy` we can pass a single payoff matrix (it infers what the other will be):


```python
A = [[1, -1], [-1, 1]]
matching_pennies = nash.Game(A)
matching_pennies
```




    Zero sum game with payoff matrices:
    
    Row player:
    [[ 1 -1]
     [-1  1]]
    
    Column player:
    [[-1  1]
     [ 1 -1]]


# Calculating utilities of strategies

# Player strategies

---

## Definition of mixed strategies

[Video](https://youtu.be/D_UID1t94UI?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

A mixed strategy for a player with strategy set $S$ is denoted by $\sigma \in [0,1]_{\mathbb{R}}^{|S|}$ and corresponds to a probability distribution over the pure strategies of player $i$. So:

$$
\sum_{i=1}^{|S|}\sigma_i = 1
$$

---

The expected score of a player can then be calculated as a measure over the probability distributions.

---

## Calculating utilities

Considering a game $(A, B)\in\mathbb{{R^{m \times n}}^2}$, if $\sigma_r$ and $\sigma_c$ are the mixed strategies for the row/column player (respectively). The utility to the row player is:

$$
u_r(\sigma_r, \sigma_c) = \sum_{i=1}^m\sum_{j=1}^nA_{ij}{\sigma_r}_i{\sigma_c}_j
$$

and the utility to the column player is:

$$
u_c(\sigma_r, \sigma_c) = \sum_{i=1}^m\sum_{j=1}^nB_{ij}{\sigma_r}_i{\sigma_c}_j
$$

This comes from:

- The probability of being in a given cell of $A$ or $B$: ${\sigma_r}_i{\sigma_c}_j$
- The value of the particular cell: $A_{ij}$ or $B_{ij}$

---

As an example consider the matching pennies game:

$$
A =
\begin{pmatrix}
    1 & -1\\
    -1 & 1
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    -1 & 1\\
    1 & -1
\end{pmatrix}
$$

with the following mixed strategies:

$$
\sigma_r = (.2, .8)
\qquad
\sigma_c = (.6, .4)
$$

We have:

$$
u_r(\sigma_r, \sigma_c) = 0.2 \times 0.6 \times 1 + 0.2 \times 0.4 \times (-1) + 0.8 \times 0.6 \times (-1) + 0.8 \times 0.4 \times 1=-0.12,
$$

$$
u_c(\sigma_r, \sigma_c) = 0.2 \times 0.6 \times (-1) + 0.2 \times 0.4 \times 1 + 0.8 \times 0.6 \times 1 + 0.8 \times 0.4 \times (-1)=0.12.
$$

---

## Linear algebraic calculation

[Video](https://youtu.be/X-n0e58vfYw?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Note that we can rearrange the expressions for the utilities:

$$
u_r(\sigma_r, \sigma_c) = \sum_{i=1}^m{\sigma_r}_i\sum_{j=1}^nA_{ij}{\sigma_c}_j
$$

$$
u_c(\sigma_r, \sigma_c) = \sum_{i=1}^m{\sigma_r}_i\sum_{j=1}^nB_{ij}{\sigma_c}_j
$$

in turn this corresponds to the matrix vector product:

$$
u_r(\sigma_r, \sigma_c) = {\sigma_r}A\sigma_c^T
$$

$$
u_c(\sigma_r, \sigma_c) = {\sigma_r}B\sigma_c^T
$$

We can use numpy to verify this calculation:


```python
import numpy as np
A = np.array([[1, -1], [-1, 1]])
B = np.array([[-1, 1], [1, -1]])
sigma_r = np.array([.2, .8])
sigma_c = np.array([.6, .4])
np.dot(sigma_r, np.dot(A, sigma_c)), np.dot(sigma_r, np.dot(B, sigma_c))
```




    (-0.11999999999999998, 0.11999999999999998)



Finally we can also directly calculate this using a `nashpy` game:


```python
import nashpy as nash
matching_pennies = nash.Game(A, B)
matching_pennies[sigma_r, sigma_c]
```




    array([-0.12,  0.12])


# Rationalisation

---

## Definition of a strictly dominated strategy

[Video](https://youtu.be/KOSSfH_Z3F0?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In a two player game $(A, B)\in\mathbb{{R^{m \times n}}^2}$ a strategy $s$ is _dominated_ by strategy $\bar s$ if for all strategies of the other player $t$:

$$
u(s, t) < u(\bar s, t)
$$

---

For example if we consider the Prisoner's Dilemma:

$$
A =
\begin{pmatrix}
    3 & 0\\
    5 & 1
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    3 & 5\\
    0 & 1
\end{pmatrix}
$$

- we see that $A_{2j} > A_{1j}$ for all $j$, so we can say that the row players' first strategy is dominated by its second strategy.
- we see that $B_{i2} > B_{i1}$ for all $i$, so we can say that the column players' first strategy is dominated by its second strategy.

---

## Definition of a weakly dominated strategy

[Video](https://youtu.be/uJPcXIDDO8M?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In a two player game $(A, B)\in\mathbb{{R^{m \times n}}^2}$ a strategy $s$ is _weakly dominated_ by strategy $\bar s$ if for all strategies of the other player $t$:

$$
u(s, t) \leq u(\bar s, t)
$$

**and there exists** a $t'$ such that:

$$
u(s, t') < u(\bar s, t')
$$

---

For example if we consider the modified version of the previous game:

$$
A =
\begin{pmatrix}
    3 & 0\\
    3 & 1
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    3 & 3\\
    0 & 1
\end{pmatrix}
$$

- we see that $A_{2j} \geq A_{1j}$ for all $j$ **and** $A_{22} > A_{12}$, so we can say that the row players' first strategy is weakly dominated by its second strategy.
- we see that $B_{i2} \geq B_{i1}$ for all $i$ **and** $B_{22} > B_{21}$, so we can say that the column players' first strategy is weakly dominated by its second strategy.

We can use `numpy` to verify if a strategy is weakly/strictly dominated:


```python
import numpy as np
A = np.array([[3, 0], [3, 1]])
B = np.array([[3, 3], [0, 1]])
```


```python
# Verify that first row is weakly dominated by second row
all(A[0,:] <= A[1,:]) and any(A[0,:] < A[1,:])
```




    True




```python
# Verify that first column is weakly dominated by second column
all(B[:,0] <= B[:,1]) and any(B[:,0] < B[:,1])
```




    True



---

## Definition  of common knowledge of rationality

[Video](https://youtu.be/7FZAWCI_q60?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

An important aspect of Game Theory and the tool that we have in fact been using so far is to assume that players are rational. However we can (and need) to go further:

- The players are rational;
- The players all know that the other players are rational;
- The players all know that the other players know that they are rationals;
...


This chain of assumptions is called Common Knowledge of Rationality (CKR). By applying the CKR assumption we can attempt to predict rational behaviour through the iterated elimination of weakly dominated strategies. This process is called **rationalisation**.

Let us consider the following game:

$$
A =
\begin{pmatrix}
    10 & 5 & 1\\
    10 & 5 & 4
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    1 & 1 & -2\\
    1 & 0 & 2
\end{pmatrix}
$$

We see that the rows players' first strategy is weakly dominated by its second.


```python
A = np.array([[10, 5, 1], [10, 5, 4]])
B = np.array([[1, 1, -2], [1, 0, 2]])
all(A[0,:] <= A[1,:]) and any(A[0,:] < A[1,:])
```




    True



Once we have removed that strategy the game reduces to:

$$
A =
\begin{pmatrix}
    10 & 5 & 4
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    1 & 0 & 2
\end{pmatrix}
$$

and now we see that the column players' third strategy would dominate the other two.

Thus a prediction of rational behaviour would be the strategy profile: $(r_2, c_3)$.

Not all games allow for prediction of rational behaviour through rationalisation **and** for some games the prediction will change depending on the order of the elimination.
# Best responses

---

## Definition of a best response

[Video](https://youtu.be/cJUZEmfhdcA?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In a two player game $(A,B)\in{\mathbb{R}^{m\times n}}^2$ a mixed strategy $\sigma_r^*$  of the row player is a best response to a column players' strategy $\sigma_c$ iff:

$$
\sigma_r^*=\text{argmax}_{\sigma_r\in S_r}\sigma_rA\sigma_c^T.
$$

Similarly a mixed strategy $\sigma_c^*$  of the column player is a best response to a row players' strategy $\sigma_r$ iff:

$$
\sigma_c^*=\text{argmax}_{\sigma_c\in S_c}\sigma_rB\sigma_c^T.
$$

---

In other words: a best response strategy maximise the utility of a player given a known strategy of the other player.

## Best responses in the Prisoners Dilemma

Consider the Prisoners Dilemma:

$$
A = \begin{pmatrix}
3 & 0\\
5 & 1
\end{pmatrix}\qquad
B = \begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
$$

We can easily identify the pure strategy best responses by underlying the corresponding utilities. For the row player, we will underline the best utility in each column:

$$
A = \begin{pmatrix}
3 & 0\\
\underline{5} & \underline{1}
\end{pmatrix}
$$

For the column player we underling the best utility in each row:

$$
B = \begin{pmatrix}
3 & \underline{5}\\
0 & \underline{1}
\end{pmatrix}
$$

We see that both players' best responses are their second strategy.

## Best responses in matching pennies

[Video](https://youtu.be/dLUWbKNxU44?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Consider matching pennies with the best responses underlined:

$$
A = \begin{pmatrix}
\underline{1} & -1\\
-1 & \underline{1}
\end{pmatrix}\qquad
B = \begin{pmatrix}
-1 & \underline{1}\\
\underline{1} & -1
\end{pmatrix}
$$

We see that the best response now depend on what the opponent does.

Let us consider the best responses against a mixed strategy (and apply the previous definition):

- Assume $\sigma_r=(x,1-x)$
- Assume $\sigma_c=(y,1-y)$

We have:

$$
A\sigma_c^T = \begin{pmatrix}
2y-1\\
1-2y
\end{pmatrix}\qquad
\sigma_rB = \begin{pmatrix}
1-2x & 2x-1
\end{pmatrix}
$$


```python
import sympy as sym
import numpy as np
sym.init_printing()

x, y = sym.symbols('x, y')
A = sym.Matrix([[1, -1], [-1, 1]])
B = - A
sigma_r = sym.Matrix([[x, 1-x]])
sigma_c = sym.Matrix([y, 1-y])
A * sigma_c, sigma_r * B
```




$$\left ( \left[\begin{matrix}2 y - 1\\- 2 y + 1\end{matrix}\right], \quad \left[\begin{matrix}- 2 x + 1 & 2 x - 1\end{matrix}\right]\right )$$



Those two vectors gives us the utilities to the row/column player when they play either of their pure strategies:

- $(A\sigma_c^T)_i$ is the utility of the row player when playing strategy $i$ against $\sigma_c=(y, 1-y)$
- $(\sigma_rB)_j$ is the utility of the column player when playing strategy $j$ against $\sigma_r=(x, 1-x)$

Let us plot these (using `matplotlib`):


```python
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
matplotlib.rc("savefig", dpi=100)  # Increase the quality of the images (not needed)

ys = [0, 1]
row_us = [[(A * sigma_c)[i].subs({y: val}) for val in ys] for i in range(2)]
plt.plot(ys, row_us[0], label="$(A\sigma_c^T)_1$")
plt.plot(ys, row_us[1], label="$(A\sigma_c^T)_2$")
plt.xlabel("$\sigma_c=(y, 1-y)$")
plt.title("Utility to player 1")
plt.legend();
```


![png](output_3_0.png)



```python
xs = [0, 1]
row_us = [[(sigma_r * B)[j].subs({x: val}) for val in xs] for j in range(2)]
plt.plot(ys, row_us[0], label="$(\sigma_rB)_1$")
plt.plot(ys, row_us[1], label="$(\sigma_rB)_2$")
plt.xlabel("$\sigma_r=(x, 1-x)$")
plt.title("Utility to column player")
plt.legend();
```


![png](output_4_0.png)


We see that the best responses to the mixed strategies are given as:

$$
\sigma_r^* = 
\begin{cases}
(1, 0),&\text{ if } y > 1/2\\
(0, 1),&\text{ if } y < 1/2\\
\text{indifferent},&\text{ if } y = 1/2
\end{cases}
\qquad
\sigma_c^* = 
\begin{cases}
(0, 1),&\text{ if } x > 1/2\\
(1, 0),&\text{ if } x < 1/2\\
\text{indifferent},&\text{ if } x = 1/2
\end{cases}
$$

In this particular case we see that for any given strategy, the opponents' best response is either a pure strategy or a mixed strategy in which case they are indifferent between the pure strategies.

For example:

- If $\sigma_c=(1/4, 3/4)$ ($y=1/4$) then the best response is $\sigma_r^*=(0,1)$
- If $\sigma_c=(1/2, 1/2)$ ($y=1/2$) then any mixed strategy is a best response **but** in fact both pure strategies would give the same utility (the lines intersect).

This observation generalises to our first theorem:

---

## Best response condition

[Video](https://youtu.be/UQWoNZBifs8?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In a two player game $(A,B)\in{\mathbb{R}^{m\times n}}^2$ a mixed strategy $\sigma_r^*$  of the row player is a best response to a column players' strategy $\sigma_c$ iff:

$${\sigma_r^*}_i > 0 \Rightarrow (A\sigma_c^T)_i = \max_{k}(A\sigma_c^T)_k\text{ for all }1\leq i\leq m$$

### Proof of best response condition

$(A\sigma_c^T)_i$ is the utility of the row player when they play their $i$th strategy. Thus:

$$\sigma_rA\sigma_c^T=\sum_{i=1}^{m}{\sigma_r}_i(A\sigma_c^T)_i$$

Let $u=\max_{k}(A\sigma_c^T)_k$. Thus:

$$
\begin{align}
\sigma_rA\sigma_c^T&=\sum_{i=1}^{m}{\sigma_r}_i(u - u + (A\sigma_c^T)_i)\\
                   &=\sum_{i=1}^{m}{\sigma_r}_iu - \sum_{i=1}^{m}{\sigma_r}_i(u - (A\sigma_c^T)_i)\\
                   &=u - \sum_{i=1}^{m}{\sigma_r}_i(u - (A\sigma_c^T)_i)
\end{align}$$

We know that $u - (A\sigma_c^T)_i\geq 0$, thus the largest $\sigma_rA\sigma_c^T$ can be is $u$ which occurs iff ${\sigma_r}_i > 0 \Rightarrow (A\sigma_c^T)_i = u$ as required.

---

Returning to our previous example. If $\sigma_c=(1/2, 1/2)$, $(A\sigma_c^T)=(0, 0)$, thus $(A\sigma_c^T)_i = 0$ for all $i$.

Note that while any strategy is a best response to $(1/2, 1/2)$ the pair of strategies $(\sigma_r, \sigma_c) = ((1/2, 1/2), (1/2, 1/2))$ are the only two strategies that are best responses to each other. This _coordinate_ is called a **Nash equilibrium**.

## Definition of Nash equilibrium

[Video](https://youtu.be/b1JBFU0wDyY?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In a two player game $(A,B)\in{\mathbb{R}^{m\times n}}^2$, $(\sigma_r, \sigma_c)$ is a Nash equilibrium if $\sigma_r$ is a best response to $\sigma_c$ and vice versa.
# Support enumeration

The definition implies that a Nash equilibrium is a pair of best responses.

We can use this and the best response condition of the previous chapter to find Nash equilibrium.

---

## Definition of support

[Video](https://youtu.be/AlBfCs5bxhk?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

For a given strategy $\sigma$, the support of $\sigma$: $\mathcal{S}(\sigma)$ is the set of strategies for which $\sigma_i>0$:

$$
i\in\mathcal{S}(\sigma)\Leftrightarrow \sigma_i > 0
$$

---

For example:

- If $\sigma=(1/3, 1/2, 0, 0, 1/6)$: $\mathcal{S}(\sigma)=\{1, 2, 5\}$
- If $\sigma=(0, 0, 1, 0)$: $\mathcal{S}(\sigma)=\{3\}$


```python
import numpy as np
sigma = np.array([1/3, 1/2, 0, 0, 1/6])
np.where(sigma > 0)  # Recall Python indexing starts at 0
```




    (array([0, 1, 4]),)




```python
sigma = np.array([0, 0, 1, 0])
np.where(sigma > 0)  # Recall Python indexing starts at 0
```




    (array([2]),)



---

## Definition of nondegenerate games


A two player game is called nondegenerate if no mixed strategy of support size $k$ has more than $k$ pure best responses.

---

For example, the following game is degenerate:

$$
A = 
\begin{pmatrix}
    1 & 1 & 0\\
    2 & 3 & 0
\end{pmatrix}\qquad
B = 
\begin{pmatrix}
    1/2 & -1 & -1/2\\
    -1 & -1 & 2
\end{pmatrix}
$$

Indeed, consider $\sigma_c=(0, 0, 1)$, we have $|\mathcal{S}(\sigma_c)|=1$ and:

$$
A\sigma_c^T = 
\begin{pmatrix}
    0\\
    0
\end{pmatrix}
$$

So the number of pure best responses to $\sigma_c$ is 2.

Thus the game considered is indeed degenerate.


```python
A = np.array([[1, 1, 0], [2, 3, 0]])
sigma_c = np.array([0, 0, 1])
(np.dot(A, sigma_c))
```




    array([0, 0])



This leads to the following algorithm for identifying Nash equilibria:

---

## Support enumeration algorithm

[Video](https://youtu.be/w5MDcvzNI_A?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

For a nondegenerate 2 player game $(A, B)\in{\mathbb{R}^{m\times n}}^2$ the following algorithm returns all nash equilibria:

1. For all $1\leq k\leq \min(m, n)$;
2. For all pairs of support $(I, J)$ with $|I|=|J|=k$
3. Solve the following equations (this ensures we have best responses):

   $$\sum_{i\in I}{\sigma_{r}}_iB_{ij}=v\text{ for all }j\in J$$
   
   $$\sum_{j\in J}A_{ij}{\sigma_{c}}_j=u\text{ for all }i\in I$$

4. Solve
   - $\sum_{i=1}^{m}{\sigma_{r}}_i=1$ and ${\sigma_{r}}_i\geq 0$ for all $i$
   - $\sum_{j=1}^{n}{\sigma_{c}}_j=1$ and ${\sigma_{c}}_j\geq 0$ for all $j$
5. Check the best response condition.

Repeat steps 3,4 and 5 for all potential support pairs.

---

## 2 by 2 example of support enumeration


As an example consider the matching pennies game.

$$
A=
\begin{pmatrix}
1 & -1\\
-1 & 1
\end{pmatrix}\qquad
B=
\begin{pmatrix}
-1 & 1\\
1 & -1
\end{pmatrix}
$$

1. Consider $k=1$: so here we are just considering supports of size 1, in other words pairs of pure best responses. The easiest way to identify these is by looking at the best responses:

   $$
   A=
   \begin{pmatrix}
   \underline{1} & -1\\
   -1 & \underline{1}
   \end{pmatrix}\qquad
   B=
   \begin{pmatrix}
   -1 & \underline{1}\\
   \underline{1} & -1
   \end{pmatrix}
   $$
   
So there are no pairs.
   
1. Thus we start again with $k=2$.
2. There is only one pair of best responses to be considered: $I=J=\{1, 2\}$.
3. The equations we need to solve are:

   $$-{\sigma_{r}}_1+{\sigma_{r}}_2=v$$
   $${\sigma_{r}}_1-{\sigma_{r}}_2=v$$
   
   and 
   
   $${\sigma_{c}}_1-{\sigma_{c}}_2=u$$
   $$-{\sigma_{c}}_1+{\sigma_{c}}_2=u$$
   
   We don't actually care (or know!) the values of $u, v$ so we in fact solve:
   
   $$-{\sigma_{r}}_1+{\sigma_{r}}_2={\sigma_{r}}_1-{\sigma_{r}}_2$$
   
   $${\sigma_{c}}_1-{\sigma_{c}}_2=-{\sigma_{c}}_1+{\sigma_{c}}_2$$
   
   which gives:
   
   $${\sigma_{r}}_1={\sigma_{r}}_2$$
   
   $${\sigma_{c}}_1={\sigma_{c}}_2$$
   
4. This gives: 

   $$\sigma_{r}=(1/2, 1/2)$$
   
   $$\sigma_{c}=(1/2, 1/2)$$

5. Finally we check the best response condition: (we already did this in the previous chapter).

Note that for 2 player games with $m=n=2$ step 5 is trivial so in fact to find best mix strategy Nash equilibrium for games of this size simply reduces to finding a solution to 2 linear equations (step 3).

Let us consider a large game:


   $$
   A=
   \begin{pmatrix}
   1 & 1 & -1\\
   2 & -1 & 0
   \end{pmatrix}\qquad
   B=
   \begin{pmatrix}
   1/2 & -1 & -1/2\\
   -1 & 3 & 2
   \end{pmatrix}
   $$
   
   
1. It is immediate to note that there are no pairs of pure best responses.
2. All possible support pairs are:

   - $I=(1, 2)$ and $J=(1,2)$
   - $I=(1, 2)$ and $J=(1,3)$
   - $I=(1, 2)$ and $J=(2,3)$
   
3. Let us solve the corresponding linear equations:

   - $I=(1, 2)$ and $J=(1, 2)$:
     
     $$1/2{\sigma_{r}}_1-{\sigma_{r}}_2=-{\sigma_{r}}_1+3{\sigma_{r}}_2$$
     $${\sigma_{r}}_1=8/3{\sigma_{r}}_2$$
     
     $${\sigma_{c}}_1+{\sigma_{c}}_2=2{\sigma_{c}}_1-{\sigma_{c}}_2$$
     $${\sigma_{c}}_1=2{\sigma_{c}}_2$$
     
   - $I=(1, 2)$ and $J=(1,3)$:
      
     $$1/2{\sigma_{r}}_1-{\sigma_{r}}_2=-1/2{\sigma_{r}}_1+2{\sigma_{r}}_2$$
     $${\sigma_{r}}_1=3{\sigma_{r}}_2$$
     
     $${\sigma_{c}}_1-{\sigma_{c}}_3=2{\sigma_{c}}_1+0{\sigma_{c}}_3$$
     $${\sigma_{c}}_1=-{\sigma_{c}}_3$$

   - $I=(1, 2)$ and $J=(2,3)$:
            
     $$-{\sigma_{r}}_1+3{\sigma_{r}}_2=-1/2{\sigma_{r}}_1+2{\sigma_{r}}_2$$
     $${\sigma_{r}}_1=2{\sigma_{r}}_2$$
     
     $${\sigma_{c}}_2-{\sigma_{c}}_3=-{\sigma_{c}}_2+0{\sigma_{c}}_3$$
     $$2{\sigma_{c}}_2={\sigma_{c}}_3$$
     
4. We check which supports give valid mixed strategies:

   - $I=(1, 2)$ and $J=(1, 2)$:
   
     $$\sigma_r=(8/11, 3/11)$$
     $$\sigma_c=(2/3, 1/3, 0)$$
       
   - $I=(1, 2)$ and $J=(1, 3)$:
   
     $$\sigma_r=(3/4, 1/4)$$
     $$\sigma_c=(k, 0, -k)$$
       
     **which is not a valid mixed strategy.**
     
   - $I=(1, 2)$ and $J=(2, 3)$:
   
     $$\sigma_r=(2/3, 1/3)$$
     $$\sigma_c=(0, 1/3, 2/3)$$
     
5. Let us verify the best response condition:

   - $I=(1, 2)$ and $J=(1, 2)$:
   
     $$\sigma_c=(2/3, 1/3, 0)$$
     
     $$A\sigma_c^T=
     \begin{pmatrix}
     1\\
     1
     \end{pmatrix}
     $$
     
     Thus $\sigma_r$ is a best response to $\sigma_c$
        
     $$\sigma_r=(8/11, 3/11)$$
     $$\sigma_r B=(1/11, 1/11, 2/11)$$
     
     **Thus $\sigma_c$ is not a best response to $\sigma_r$** (because there is a better response outside of the support of $\sigma_c$).
     
     
   - $I=(1, 2)$ and $J=(2, 3)$:
   
     $$\sigma_c=(0, 1/3, 2/3)$$
     
     $$A\sigma_c^T=
     \begin{pmatrix}
     -1/3\\
     -1/3
     \end{pmatrix}
     $$
     
     Thus $\sigma_r$ is a best response to $\sigma_c$
        
     $$\sigma_r=(2/3, 1/3)$$
     $$\sigma_r B=(0, 1/3, 1/3)$$
     
     Thus $\sigma_c$ is a best response to $\sigma_r$.
     
Thus the (unique) Nash equilibrium for this game is:

$$((2/3, 1/3), (0, 1/3, 2/3))$$

Note that we can confirm all of this using `nashpy`:


```python
import nashpy as nash
A = np.array([[1,-1], [-1, 1]])
game = nash.Game(A)
list(game.support_enumeration())
```




    [(array([0.5, 0.5]), array([0.5, 0.5]))]




```python
A = np.array([[1, 1, -1], [2, -1, 0]])
B = np.array([[1/2, -1, -1/2], [-1, 3, 2]])
game = nash.Game(A, B)
list(game.support_enumeration())
```




    [(array([0.66666667, 0.33333333]),
      array([-0.        ,  0.33333333,  0.66666667]))]



If you recall the degenerate game mentioned previously:


```python
A = np.array([[1, 1, 0], [2, -1, 0]])
B = np.array([[1/2, -1, -1/2], [-1, 3, 2]])
game = nash.Game(A, B)
list(game.support_enumeration())
```




    []



This result is given without proof:

---

## Nash's theorem

Any game with a finite set of players and finit set of strategies has a Nash equilibrium in mixed strategies.

---
# Best response polytopes

Another useful representation of games is to consider polytopes. A polytope $\mathcal{P}$ has the following definition:

---
## Definition of a Polytope as a convex hull

[Video](https://www.youtube.com/watch?v=6NaPQhJe2QM&list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb&index=20)

For a given set of vertices $V\subseteq\mathbb{R} ^ K$, a Polytope $\mathcal{P}$ can be defined as the following set of points:

$$
\mathcal{P} = \left\{\sum_{i=1}^{|V|} \lambda_i v_i \in\mathbb{R} ^ K \;\left|\; \sum_{i=1}^{|V|} \lambda_i = 1; \lambda_i\geq 0;v_i \in V \right.\right\}
$$

---

This is a higher dimensional generalization of polygons. Let us plot the polytope with vertices:

$$
V = \{(0, 0), (1/2, 0), (1/2, 1/4), (0, 1/3)\}
$$


```python
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial

V = [
    np.array([0, 0]), 
    np.array([1 / 2, 0]), 
    np.array([1 / 2, 1 / 4]), 
    np.array([0, 1 / 3])
]
P = scipy.spatial.ConvexHull(V)
scipy.spatial.convex_hull_plot_2d(P);
```


![png](output_1_0.png)



An equivalent definition of Polytope is as an intersection of boundaries that seperate the space in to two distinct areas.

---

## Definition of a Polytope as an intersection of halfspaces

[Video](https://youtu.be/_JJ2O6q_pEg?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

For a matrix $M\in\mathbb{R} ^ {m\times n}$ and a vector $b\in\mathbb{R}^m$ a Polytope $\mathcal{P}$ can be defined as the following set of points:

$$
\mathcal{P} = \left\{x \in\mathbb{R} ^ {n} \;\left|\; Mx\leq b \right.\right\}
$$

---

For example the previous polytope is equivalently described by the following inequalities:

$$
\begin{aligned}
- x_1       & \leq 0\\
-x_2        & \leq 0\\
2x_1        & \leq 1\\
3x_2        & \leq 1\\
x_1 + 6 x_2 & \leq 2
\end{aligned}
$$

---

## Definition of best response polytopes

[Video](https://youtu.be/yGGtYMpSSzY?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)


For a two player game $(A, B)\in{\mathbb{R}^{m\times n}_{>0}}^2$ the row/column player best response polytope $\mathcal{P}$/$\mathcal{Q}$ is defined by:

$$
\mathcal{P} = \left\{x\in\mathbb{R}^{m}\;|\;x\geq 0; xB\leq 1\right\}
$$

$$
\mathcal{Q} = \left\{y\in\mathbb{R}^{n}\;|\; Ay\leq 1; y\geq 0 \right\}
$$

---

The polytope $\mathcal{P}$, corresponds to the set of points with an upper bound on the utility of those points when considered as row strategies against which the column player plays.

The fact that these polytopes are defined for $A, B > 0$ is not restrictive as we can simply add a constant to our utilities. As an example, let us consider the matching pennies game:

$$
A = 
\begin{pmatrix}
    1 & -1\\
    -1&  1
\end{pmatrix}\qquad
B = 
\begin{pmatrix}
    -1 & 1\\
    1&  -1
\end{pmatrix}
$$

First let us add 2 to all utilities:

$$
A = 
\begin{pmatrix}
    3 & 1\\
    1 &  3
\end{pmatrix}\qquad
B = 
\begin{pmatrix}
    1 & 3\\
    3 &  1
\end{pmatrix}
$$

The inequalities for $\mathcal{P}$ are then given by:

$$
\begin{aligned}
-x_1        & \leq 0\\
-x_2        & \leq 0\\
x_1 + 3 x_2        & \leq 1\\
3 x_1 + x_2       & \leq 1\\
\end{aligned}
$$

which corresponds to:

$$
\begin{aligned}
x_1        & \geq 0\\
x_2        & \geq 0\\
x_2        & \leq 1/3 -x_1/3\\
x_2       & \leq 1 - 3x_1\\
\end{aligned}
$$

the intersection of the two non trivial constraints is at the point:

$$1/3 -x_1/3=1 - 3x_1$$

giving:

$$x_1=1/4$$ 

and

$$x_2=1/4$$


```python
import sympy as sym
x_1 = sym.symbols('x_1')
sym.solveset(1/3 - x_1 / 3 - 1 + 3 * x_1, x_1)
```




    {0.25}



This gives 4 vertices:

$$
V = \{(0, 0), (1/3, 0), (1/4, 1/4), (0, 1/3)\}
$$


```python
V = [
    np.array([0, 0]), 
    np.array([1 / 3, 0]), 
    np.array([1 / 4, 1 / 4]), 
    np.array([0, 1 / 3])
]
P = scipy.spatial.ConvexHull(V)
scipy.spatial.convex_hull_plot_2d(P);
```


![png](output_5_0.png)


## Vertex labelling

[Video](https://youtu.be/yeatZdnfFY4?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

These vertices are no longer probability vectors. Recall the four inequalities of this polytope:

1. $x_1 \geq 0$: if this inequality is "binding" (ie $x_1=0$) that implies that the row player does not play that strategy.
2. $x_2 \geq 0$: if this inequality is "binding" (ie $x_2=0$) that implies that the row player does not play that strategy.
3. $x_1 + 3 x_2 \leq 1$: if this inequality is binding (ie $x_1 + 3 x_2 = 1$) then that implies that the utility to the column player for that particular column is as big as it can be.
4. $3x_1 + x_2 \leq 1$: if this inequality is binding (ie $3x_1 + x_2 = 1$) then that implies that the utility to the column player for that particular column is as big as it can be.

We in fact use this notion to **label** our vertices:

1. $(0, 0)$ has labels $\{0, 1\}$ (we start our indexing at 0).
2. $(1/3, 0)$ has labels $\{1, 3\}$
3. $(1/4, 1/4)$ has labels $\{2, 3\}$
4. $(0, 1/3)$ has labels $\{0, 2\}$

Similarly the vertices and labels for $\mathcal{Q}$ are:

1. $(0, 0)$ has labels $\{2, 3\}$
2. $(1/3, 0)$ has labels $\{0, 3\}$
3. $(1/4, 1/4)$ has labels $\{0, 1\}$
4. $(0, 1/3)$ has labels $\{1, 2\}$

Note that for a given pair of vertices, if the pair is fully labeled (so that the union of the labels is $\{0, 1, 2, 3\}$) then either a strategy is not played or it is a best response to the other player's strategies.

This leads to a final observation:

---
## Fully labeled vertex pair

For a pair of vertices $(x, y)\in\mathcal{P}\times \mathcal{Q}$, if the union of the labels of $x$ and $y$ correspond to the set of all labels then $x, y$, when normalised (so that the sum is 1), correspond to a Nash equilibrum.

---

This leads to another algorithm for finding equilibria:

---
## Vertex enumeration algorithm

[Video](https://youtu.be/LX3zU2en8vc?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

For a nondegenerate 2 player game $(A, B)\in{\mathbb{R}^{m\times n}_{>0}}^2$ the following algorithm returns all nash equilibria:

1. For all pairs of vertices of the best response polytopes
2. Check if the vertices have full labels
3. Return the normalised probabilities

---

For our running example, the only pair of vertices that is fully labeled is:

$$((1/4, 1/4), (1/4, 1/4))$$

which, when normalised (so that the sum is 1) corresponds to:

$$((1/2, 1/2), (1/2, 1/2))$$

This algorithm is implemented in `Nashpy`:


```python
import nashpy as nash
A = np.array([[1, -1], [-1, 1]])
matching_pennies = nash.Game(A)
list(matching_pennies.vertex_enumeration())
```




    [(array([0.5, 0.5]), array([0.5, 0.5]))]


# The Lemke Howson algorithm

The vertex and support enumeration algorithms are all algorithms that use an exhaustive search. For large games, this can take a long time and/or have a high computational cost. The following algorithm gives an approach to create a path through vertices in both best response polytopes to find a pair that is fully labelled.

---

## The Lemke Howson algorithm

[Video](https://youtu.be/HekHAuWR_30?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)


For a nondegenerate 2 player game $(A, B)\in{\mathbb{R}^{m\times n}_{>0}}^2$ the following algorithm returns a nash equilibrium:

1. Start at the artificial equilibrium: $(0, 0)$
2. Choose a label to drop.
3. Remove this label from the corresponding vertex by traversing an edge of the corresponding polytope to another vertex. 
4. The new vertex will now have a duplicate label in the other polytope. Remove this label from the vertex of the other polytope and traverse an edge of that polytope to another vertex.
5. Repeat step 4 until the pair of vertices is fully labelled.

---

As an example let us consider the matching pennies game:

$$
A = 
\begin{pmatrix}
    1 & -1\\
    -1&  1
\end{pmatrix}\qquad
B = 
\begin{pmatrix}
    -1 & 1\\
    1&  -1
\end{pmatrix}
$$

First let us add 2 to all utilities:

$$
A = 
\begin{pmatrix}
    3 & 1\\
    1 &  3
\end{pmatrix}\qquad
B = 
\begin{pmatrix}
    1 & 3\\
    3 &  1
\end{pmatrix}
$$

The vertices for $\mathcal{P}$ are:

1. $a=(0, 0)$ has labels $\{0, 1\}$ 
2. $b=(1/3, 0)$ has labels $\{1, 3\}$
3. $c=(1/4, 1/4)$ has labels $\{2, 3\}$
4. $d=(0, 1/3)$ has labels $\{0, 2\}$

The vertics and labels for $\mathcal{Q}$ are:

1. $w=(0, 0)$ has labels $\{2, 3\}$
2. $x=(1/3, 0)$ has labels $\{0, 3\}$
3. $y=(1/4, 1/4)$ has labels $\{0, 1\}$
4. $z=(0, 1/3)$ has labels $\{1, 2\}$

Let us apply the algorithm:

- $(a, w)$ have labels: $\{0, 1\}, \{2, 3\}$. Drop 0 (arbitrary decision) in $\mathcal{P}$.
- $\to (b, w)$ have labels: $\{1, 3\}, \{2, 3\}$. In $\mathcal{Q}$ drop 3.
- $\to (b, z)$ have labels: $\{1, 3\}, \{1, 2\}$. In $\mathcal{P}$ drop 1.
- $\to (c, z)$ have labels: $\{2, 3\}, \{1, 2\}$. In $\mathcal{Q}$ drop 2.
- $\to (c, y)$ have labels: $\{2, 3\}, \{0, 1\}$. Fully labeled vertex pair.

We now return the strategy pair by normalising these vertices:

$$((1/2, 1/2), (1/2, 1/2))$$

This is also implemented in `Nashpy`:


```python
import numpy as np
import nashpy as nash
A = np.array([[1, -1], [-1, 1]])
matching_pennies = nash.Game(A)
matching_pennies.lemke_howson(initial_dropped_label=0)
```




    (array([0.5, 0.5]), array([0.5, 0.5]))



You can also iterate over all possible starting labels:


```python
for eq in matching_pennies.lemke_howson_enumeration():
    print(eq)
```

    (array([0.5, 0.5]), array([0.5, 0.5]))
    (array([0.5, 0.5]), array([0.5, 0.5]))
    (array([0.5, 0.5]), array([0.5, 0.5]))
    (array([0.5, 0.5]), array([0.5, 0.5]))


In this case they will always give the same result (this game indeed has a unique equilibria), however that's not always the case and also note that not all equilibria can be obtained from a given starting vertex pair.

---

## Tableaux

[Video](https://youtu.be/krXbHbVhVTM?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Carrying out the Lemke Howson algorithm in this way is straightforward when the polytope can be visualised and/or the vertices themselves can all be enumerated to begin with. This is not always the case: using tools from linear programming we can traverse our polytopes using a technique called "pivoting" or a tabular representation of the polytopes called "tableaux" (plural).

A tableau corresponds to the inequalities relating to the payoffs considered but as equalities.The inequalities for the row polytope for the matching pennies game can be rewritten as:

1. $x_1+3x_2 + s_1 = 1$
2. $3x_1+x_2 + s_2 = 1$

where $s_1, s_2$ are "slack" variables used to convert the inequality to an equality.

This can be represented in tableau form as:

$$
T_r =
\begin{pmatrix}
1 & 3 & 1 & 0 & 1\\
3 & 1 & 0 & 1 & 1
\end{pmatrix}
$$

Note that this corresponds to:

$$
T_r = 
\begin{pmatrix}
B^T&I &1\\
\end{pmatrix}
$$

---

## Basic variables and labelled vertices

[Video](https://youtu.be/6ujffslY318?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

A basic variable of a tableau is a column (ignoring the last column) that is linearly independent from the others. Any given vertex of a polytope corresponds to a tableau where the non basic variables are set to 0 and the basic variables are solved. Non basic variables corresponds to labels of a vertex.

---

For example setting the non basic variables in $T_r$ to 0 we get:

$$x_1=x_2=0$$ which corresponds to the origin of the polytope (which is the starting point for the Lemke Howson algorithm). Thus the labels of vertex corresponds to the non basic variables.


---

## Pivoting and the Lemke Howson Algorithm

[Video](https://youtu.be/aJq73gJwd24?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In the Lemke Howson algorithm we need to drop a label and move along an edge of the Polytope to arrive at another vertex where a new label will replace the dropped label. This is equivalent to making a non basic variable basic (and vice versa). We do this by carrying out row operations on the tableau.


Let us drop the 0 label (corresponding to the first column) on $T_r$. We need to "pivot" the first column, so one of those non zero variables in that column will become 0. We identify this by choosing the row with the minimum positive ratio of $(T_r)_{i5} / (T_r)_{i1}$. This ensures that the resulting vertex is valid (and will have no negative variables). In our case the ratios in the first column are:

1. First row: $1/1$
2. Second row: $1/3$

Thus we pivot on the second row. We here take multiples of rows and carry out subtractions/additions of row so as to obtain a basic variable in the first column. In our case let us multiple the first row by 3 and subtract the second row from it:

$$
T_r =
\begin{pmatrix}
    0 & 8 & 3 & -1 & 2\\
    3 & 1 & 0 & 1 & 1
\end{pmatrix}
$$

We now (as in the example we carried out before) have non basic variables $x_2$ and $s_2$ in other words we have labels: $\{1, 3\}$. We have thus picked up the label $3$ which we need to drop from the other polytope.

In tableau form the column best response polytope is given by:

$$
T_c =
\begin{pmatrix}
    1 & 0 & 3 & 1 & 1\\
    0 & 1 & 1 & 3 & 1
\end{pmatrix}
$$

Note that this corresponds to:

$$
T_c = 
\begin{pmatrix}
I & A & 1\\
\end{pmatrix}
$$

we need to pivot the fourth column corresponding to label $3$ of $T_c$. First the minimum ratios: $1/1>1/3$, so we pivot on the second row. Let us multiply the first row by 3 and subtract the second row from it:

$$
T_c =
\begin{pmatrix}
    3 & -1 & 8 & 0 & 2\\
    0 & 1 & 1 & 3 & 1
\end{pmatrix}
$$

This has labels: $\{1, 2\}$ with $1$ being the newly picked up label that we now drop (by pivoting the second column) from $T_r$:

$$
T_r =
\begin{pmatrix}
    0 & 8 & 3 & -1 & 2\\
    24 & 0 & -3 & 9 & 6
\end{pmatrix}
$$

which has labels: $\{2, 3\}$ with $2$ being the newly picked up label so we now pivot the third column of $T_c$:

$$
T_c =
\begin{pmatrix}
    3 & -1 & 8 & 0 & 2\\
    -3 & 9 & 0 & 24 & 6
\end{pmatrix}
$$

which has labels: $\{0, 1\}$ so we have a fully labelled vertex pair. Setting the non basic variables to 0 in each tableau we obtain:

$$
\left((2/8, 8/24), (2/8, 6/24)\right) = \left((1/4, 1/4), (1/4, 1/4)\right)
$$

which, when normalised to have sum 1 gives:

$$
\left((1/2, 1/2), (1/2, 1/2)\right)
$$

---

A summary of integer pivoting:

1. Identify the row to pivot on using the minumum ratio test.
2. Carry out row operations to ensure that the pivot row is the only row with non zero variables in that column.
# Repeated games

---

## Definition of a repeated game

[Video](https://youtu.be/K4LKeO2rdgM?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Given a two player game $(A,B)\in{\mathbb{R}^{m\times n}}^2$, referred to as a **stage** game, a $T$-stage repeated game is a game in which players play that stage game for $T > 0$ periods. Players make decisions based on the full history of play over all the periods.

---

For example consider the game:

$$
A = 
\begin{pmatrix}
0 & 6 & 1\\
1 & 7 & 5
\end{pmatrix}
\qquad
B = 
\begin{pmatrix}
0 & 3 & 1\\
1 & 0 & 1
\end{pmatrix}
$$

by identifying the best responses:

$$
A = 
\begin{pmatrix}
0 & 6 & 1\\
\underline{1} & \underline{7} & \underline{5}
\end{pmatrix}
\qquad
B = 
\begin{pmatrix}
0 & \underline{3} & 1\\
\underline{1} & 0 & \underline{1}
\end{pmatrix}
$$

it is immediate to find two Nash equilibria:

$$((0,1), (1,0,0))\qquad((0,1), (0,0,1))$$


```python
import nashpy as nash
import numpy as np

A = np.array([[0, 6, 1],
              [1, 7, 5]])
B = np.array([[0, 3, 1],
              [1, 0, 1]])
game = nash.Game(A, B)
list(game.support_enumeration())
```




    [(array([0., 1.]), array([1., 0., 0.])),
     (array([0., 1.]), array([0., 0., 1.]))]



If we were to repeat this game twice ($T=2$) we obtain a new game. However to be able to think of this we need to define what a strategy in a repeated game is.

---

## Definition of a strategy in a repeated game

Given a two player stage game $(A,B)\in{\mathbb{R}^{m\times n}}^2$, repeated to give a $T$-stage repeated game. A strategy is a mapping from the entire history of play to an action of the stage game:

$$
\bigcup_{t=0}^{T-1}H(t)\to a
$$

where:

- $H(t)$ is the history of play of **both** players up until stage $t$ ($H(0)=(\emptyset, \emptyset)$)
- $a$ is an action (for either player) of the **stage** game

---

To help avoid confusion, whilst we have referred to pure strategies as choices made in stage games, here we will call those **actions**.

The actions for our example:

- for the row player: $\{r_1, r_2\}$ (corresponding to the rows)
- for the column player: $\{c_1, c_2, c_3\}$ (corresponding to the columns)

A strategy for the row/column player thus needs to map an element of the following set to an element of $\{r_1, r_2\}$/$\{c_1, c_2, c_3\}$:

$$\bigcup_{t=0}^{1}H(t)=\{(\emptyset, \emptyset), (r_1, c_1), (r_1, c_2), (r_1, c_3), (r_2, c_1), (r_2, c_2), (r_3, c_3)\}$$

In other words, in our example, a strategy answers both of the following questions:

- What should the player do in the first period?
- What should the player do in the second period **given** knowledge of what both players did in the first period?

The following theorem allows us to find **a** Nash equilibrium:


---

## Theorem of sequence of stage Nash equilibria

[Video](https://www.youtube.com/watch?v=wtl69v7Qz_s&list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb&index=30)

For any repeated game, any sequence of stage Nash profiles gives a Nash equilibrium.

### Proof 


Consider the following strategy:

> The row/column player should play action $a_{r/c}$ regardless of the play of any previous strategy profiles.

where $(a_{r}, a_{c})$ is a given stage Nash equilibrium.

Using backwards induction, this is a Nash equilibrium for the last stage game. Thus, at the last stage, no player has a reason to deviate. Similarly at the $T-1$th stage. The proof follows.

---

Thus, for our example we have the four Nash equilibria:

- $(r_2r_2, c_1c_1)$ with utility: (2, 2).
- $(r_2r_2, c_1c_3)$ with utility: (6, 2).
- $(r_2r_2, c_3c_1)$ with utility: (6, 2).
- $(r_2r_2, c_3c_3)$ with utility: (10, 2).

Note however that it is not the only equilibria for our repeated game.

## Reputation

[Video](https://youtu.be/VMYpSJMYQU0?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In a repeated game it is possible for players to encode reputation and trust in their strategies.

Consider the following two strategies:

1. For the row player:

   $$(\emptyset, \emptyset) \to r_1$$
   $$(r_1, c_1) \to r_2$$
   $$(r_1, c_2) \to r_2$$
   $$(r_1, c_3) \to r_2$$
   
2. For the column player:

   $$(\emptyset, \emptyset) \to c_2$$
   $$(r_1, c_2) \to c_3$$
   $$(r_2, c_2) \to c_1$$


Note that here we omit some of the histories which are not possible based on the first play by each player.

This strategy corresponds to the following scenario:

> Play $(r_1,c_2)$ in first stage and $(r_2,c_3)$ in second stage unless the row player does not cooperate in which case play $(r_2, c_1)$.

If both players play these strategies their utilities are: $(11, 4)$ which is better **for both players** then the utilities at any sequence of pure stage Nash equilibria. **But** is this a Nash equilibrium? To find out we investigate if either player has an incentive to deviate.

1. If the row player deviates, they would only be rational to do so in the first stage, if they did they would gain 1 in that stage but lose 4 in the second stage. Thus they have no incentive to deviate.
2. If the column player deviates, they would only do so in the first stage and gain no utility.

Thus this strategy pair **is a Nash equilibrium** and evidences how a reputation can be built and cooperation can emerge from complex dynamics.
# Prisoners Dilemma

[Video](https://youtu.be/DivraIWIwlQ?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

One big area of repeated games is specifically the Prisoner's Dilemma. We have previously defined this as the following game:

$$
A =
\begin{pmatrix}
    3 & 0\\
    5 & 1
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    3 & 5\\
    0 & 1
\end{pmatrix}
$$

The general form is:


$$
A =
\begin{pmatrix}
    R & S\\
    T & P
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    R & T\\
    S & P
\end{pmatrix}
$$

with the following constraints:

$$T > R > P > S$$
$$2R > T + S$$

- The first constraint ensures that the second action "Defect" dominates the first action "Cooperate".
- The second constraint ensures that a social dilemma arises: the sum of the utilities to both players is best when they both cooperate.

This game is a good model of agent (human, etc) interaction: a player can choose to take a slight loss of utility for the benefit of the other play **and** themselves.

As a single one shot game there is not much more to say about the Prisoner's dilemma. It becomes fascinating when studied as a repeated game.

---

## Axelrod's tournaments

[Video](https://youtu.be/Vfcv7k5PRvE?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)


In 1980, Robert Axelrod (a political scientist) invited submissions to a computer tournament version of an iterated prisoners dilemma. This was described in a 1980 paper titled ["Effective Choice in the Prisoner's Dilemma"](http://journals.sagepub.com/doi/abs/10.1177/002200278002400101).

### First tournament

- 15 strategies submitted. 
- Round robin tournament with 200 stages including a 16th player who played uniformly randomly.
- Some very complicated strategies, including for example a strategy that used a $\chi^2$ test to try and identify strategies that were acting randomly. You can read more about this tournament here: http://axelrod.readthedocs.io/en/stable/reference/overview_of_strategies.html#axelrod-s-first-tournament
- The winner (average score) was in fact a very simple strategy: Tit For Tat. This strategy starts by cooperating and then repeats the opponents previous move.

The fact that Tit For Tat won garnered a lot of research (still ongoing) as it showed a mathematical model of how cooperative behaviour can emerge in complex situations (why are we nice to each other?).

---

There is a Python library (`axelrod`) with over 200 strategies that can be used to reproduce this work. You can read the documentation for it here: http://axelrod.readthedocs.io.


```python
%matplotlib inline

import axelrod as axl

axl.seed(0)  # Make this reproducible
players = [
    axl.TitForTat(),
    axl.FirstByTidemanAndChieruzzi(),
    axl.FirstByNydegger(),
    axl.FirstByGrofman(),
    axl.FirstByShubik(),
    axl.FirstBySteinAndRapoport(),
    axl.Grudger(),
    axl.FirstByDavis(),
    axl.FirstByGraaskamp(),
    axl.FirstByDowning(),
    axl.FirstByFeld(),
    axl.FirstByJoss(),
    axl.FirstByTullock(),
    axl.FirstByAnonymous(),
    axl.Random(),
]
tournament = axl.Tournament(players, turns=200, repetitions=20)
results = tournament.play()
plot = axl.Plot(results)
plot.boxplot();
```

    Playing matches: 100%|██████████| 120/120 [00:26<00:00, 10.03it/s]
    Analysing: 100%|██████████| 25/25 [00:00<00:00, 35.71it/s]



![png](output_1_1.png)


We see that Tit For Tat does in fact **not** win this tournament (you can find a tutorial on reproducing the original work at https://axelrod.readthedocs.io/en/stable/tutorials/getting_started/running_axelrods_first_tournament.html). This highlights that there is no such thing as a best strategy but a best strategy for a particular environment.

Here is some of the source code for the strategies:


```python
axl.TitForTat.strategy??
```

Tit For Tat:

```python
Signature: axl.TitForTat.strategy(self, opponent:axelrod.player.Player) -> str
Source:   
    def strategy(self, opponent: Player) -> Action:
        """This is the actual strategy"""
        # First move
        if not self.history:
            return C
        # React to the opponent's last move
        if opponent.history[-1] == D:
            return D
        return C
File:      ~/anaconda3/envs/gt/lib/python3.6/site-packages/axelrod/strategies/titfortat.py
Type:      function
```


```python
axl.Grudger.strategy??
```

```python
Signature: axl.Grudger.strategy(opponent:axelrod.player.Player) -> str
Source:   
    @staticmethod
    def strategy(opponent: Player) -> Action:
        """Begins by playing C, then plays D for the remaining rounds if the
        opponent ever plays D."""
        if opponent.defections:
            return D
        return C
File:      ~/anaconda3/envs/gt/lib/python3.6/site-packages/axelrod/strategies/grudger.py
Type:      function
```

## Reactive strategies

[Video](https://youtu.be/Hbb2GcrbtVw?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

In 1989 a particular family of strategies was introduced by Martin Nowak. These strategies are defined by two parameters: $(p_1, p_1)$ where:

- $p_1$ is the probability of cooperating after an opponent cooperates;
- $p_2$ is the probability of cooperating after an opponent defects.


---

## Markov chain representation of a Match between two reactive strategies

Consider two reactive players:

$$
p=(p_1, p_2) \qquad q=(q_1, q_2)
$$


If we consider the order of possible states of a match to be:

$$S=\{CC, CD, DC, DD\}$$

then we can summarise a game with the following matrix:

$$
M = 
\begin{pmatrix}
    p_1q_1   & p_1(1-q_1) & (1-p_1)q_1 & (1-p_1)(1-q_1) \\
    p_2q_1   & p_2(1-q_1) & (1-p_2)q_1 & (1-p_2)(1-q_1) \\
    p_1q_2   & p_1(1-q_2) & (1-p_1)q_2 & (1-p_1)(1-q_2) \\
    p_2q_2   & p_2(1-q_2) & (1-p_2)q_2 & (1-p_2)(1-q_2) \\
\end{pmatrix}
$$

---

The matrix $M$ corresponds to a Markov chain. Given a probability vector $\pi$ representing the probability of being in a given state of $S$: the probabilities of being in the a given step in the next round are given by:

$$\pi M$$

If we consider:

$$
p=(1 / 4, 4 / 5) \qquad q=(2 / 5, 1 / 3)
$$

below is some code that calculates the probabilities over 20 turns starting with both strategies cooperating:


```python
import numpy as np
import matplotlib.pyplot as plt
v_1 = np.array([1 / 4, 4 / 5])
v_2 = np.array([2 / 5, 1 / 3])

M = np.array([[v_1[0] * v_2[0], v_1[0] * (1 - v_2[0]), (1 - v_1[0]) * v_2[0],  (1 - v_1[0]) * (1 - v_2[0])],
              [v_1[1] * v_2[0], v_1[1] * (1 - v_2[0]), (1 - v_1[1]) * v_2[0],  (1 - v_1[1]) * (1 - v_2[0])],
              [v_1[0] * v_2[1], v_1[0] * (1 - v_2[1]), (1 - v_1[0]) * v_2[1],  (1 - v_1[0]) * (1 - v_2[1])],
              [v_1[1] * v_2[1], v_1[1] * (1 - v_2[1]), (1 - v_1[1]) * v_2[1],  (1 - v_1[1]) * (1 - v_2[1])]])

pis = [np.array([1, 0, 0, 0])]
number_of_turns = 20
for _ in range(number_of_turns):
    pis.append(np.dot(pis[-1], M))

labels = ["CC", "CD", "DC", "DD"]
for state, label in zip(zip(*pis), labels):
    plt.plot(state, label=label)
plt.legend();
```


![png](output_8_0.png)


We see that over time these probabilities no longer change: this is referred to as steady state. A probability vector $\pi$ at steady state is a solution to the following matrix equation:

$$\pi M=\pi$$


---

## Theorem: steady state probabilities for match between reactive players

The steady state of a match between (non deterministic) reactive players is given by:

$$
\pi=(s_1s_2, s_1(1-s_2), (1-s_1)s_2, (1-s_1)(1-s_2))
$$

where:

$$
s_1 = \frac{q_2r_1+p_2}{1-r_1r_2}\qquad s_2 = \frac{p_2r_2+q_2}{1-r_1r_2}
$$

for:

$$r_1=p_1-p_2\qquad r_2=q_1-q_2$$

### Proof

The proof follow (after some heavy algebra) by carrying out the following multiplication:

$$
\pi M = 
(s_1s_2, s1(1-s_2), (1-s_1)s_2, (1-s_1)(1-s_2))
\begin{pmatrix}
    p_1q_1   & p_1(1-q_1) & (1-p_1)q_1 & (1-p_1)(1-q_1) \\
    p_2q_1   & p_2(1-q_1) & (1-p_2)q_1 & (1-p_2)(1-q_1) \\
    p_1q_2   & p_1(1-q_2) & (1-p_1)q_2 & (1-p_1)(1-q_2) \\
    p_2q_2   & p_2(1-q_2) & (1-p_2)q_2 & (1-p_2)(1-q_2) \\
\end{pmatrix}
$$

---

Using this we can obtain the expected utility of the first player:

$$s_1s_2\times R +  s1(1-s_2) \times S +  (1-s_1)s_2 \times T + (1-s_1)(1-s_2)\times P$$

The second player:

$$s_1s_2\times R +  s1(1-s_2) \times T +  (1-s_1)s_2 \times S + (1-s_1)(1-s_2)\times P$$


```python
def theoretic_steady_state(p, q):
    r_1 = p[0] - p[1]
    r_2 = q[0] - q[1]
    s_1 = (q[1] * r_1 + p[1]) / (1 - r_1 * r_2)
    s_2 = (p[1] * r_2 + q[1]) / (1 - r_1 * r_2)
    return np.array([s_1 * s_2, s_1 * (1 - s_2), (1 - s_1) * s_2, (1 - s_1) * (1 - s_2)])

def theoretic_utility(p, q, rstp=np.array([3, 0, 5, 1])):
    pi = theoretic_steady_state(p, q)
    return np.dot(pi, rstp)
```


```python
theoretic_utility(v_1, v_2), theoretic_utility(v_2, v_1)
```




    (1.675230818539924, 2.784555577382368)



We can confirm this using the Axelrod library:


```python
player_1 = axl.ReactivePlayer(probabilities=v_1)
player_2 = axl.ReactivePlayer(probabilities=v_2)
axl.seed(0)
match = axl.Match(players=(player_1, player_2), turns=5000)
interactions = match.play()
match.final_score_per_turn()
```




    (1.654, 2.799)



## Numerous variants of this tournament have since been carried out:

- Using a Probabilistic end (players don't know how many turns are going to be played). This was carried out in Axelrod's Second tournament, which had 64 strategies and Tit For Tat also won! (Described in a 1980 paper titled: ["More effective choice in the Prisoner's Dilemma"](http://journals.sagepub.com/doi/abs/10.1177/002200278002400301)).
- Playing the tournament on a Graph. This was carried out by Nowak in 1992 in a paper titled: ["Evolutionary games and Spatial chaos"](https://www.researchgate.net/profile/Martin_Nowak2/publication/216634494_Evolutionary_Games_and_Spatial_Chaos/links/54217b730cf274a67fea8e60/Evolutionary-Games-and-Spatial-Chaos.pdf).
- Understanding Evolutionary dynamics (we will understand what we mean by this in the later chapters as we start exploring evolutionary game theory).
- A specific type of strategy has recently garnered a lot of interest: Zero Determinant Strategies (in a 2012 paper titled: [Iterated Prisoner’s Dilemma contains strategies that dominate any evolutionary opponent](http://www.pnas.org/content/109/26/10409.short)). Claiming that memory does not matter. We will discuss this in further chapters.
# Evolutionary Dynamics

We will now consider how Game Theory can be used to study evolutionary processes. The main difference is that we now consider not two player games but game with an **infinite** population. The strategies will make up a dynamic population that changes over time.

## Reproduction

[Video](https://youtu.be/kBhoG3pjyG0?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Consider a simple model of population growth: let $x(t)$ denote the size of the population at time $t$ and let as assume that the rate of growth is $a$ per population size:

$$\frac{dx}{dt}=ax$$

Note that from here on we will refer to this rate as a **fitness**.

The solution of this differential equation is:

$$x(t)=x_0e^{at}\text{ where }x_0=x(0)$$


```python
import sympy as sym
sym.init_printing()
x = sym.Function('x')
t, a = sym.symbols('t, a')
sym.dsolve(sym.Derivative(x(t), t) - a * x(t), x(t))
```




$$x{\left (t \right )} = C_{1} e^{a t}$$



(This is exponential growth.)

We can also use scipy to solve this differential equation numerically (relevant for more complex dynamics):


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from scipy.integrate import odeint

t = np.linspace(0, 10, 100)  # Obtain 100 time points


def dx(x, t, a):
    """Define the derivate of x"""
    return a * x
```

If $a=10>0$:


```python
a = 10
xs = odeint(func=dx, y0=1, t=t, args=(a,))
plt.plot(xs);
```


![png](output_5_0.png)


If $a=-10<0$:


```python
a = -10
xs = odeint(func=dx, y0=1, t=t, args=(a,))
plt.plot(xs);
```


![png](output_7_0.png)


## Selection

[Video](https://youtu.be/ERbQGLLNGYo?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Reproduction alone is not enough to study evolutionary processes. Let us consider a population made up of two types of individuals:

- $x(t)$ denotes the first type;
- $y(t)$ denotes the second type.

Let us assume the same expressions for the as before:

$$\frac{dx}{dt}=ax\qquad\frac{dy}{dt}=by$$

both these population will increase or decrease independantly so there's not much of interest there **but** if we introduce the following:

$$
\rho(t) = \frac{x(t)}{y(t)}
$$

then $\lim_{t\to\infty}\rho(t)$ indicates which type takes over the population over time.

We have:

$$
\frac{d\rho}{dt} = \frac{\frac{dx}{dt}y -  \frac{dy}{dt}x}{y ^ 2} = \frac{xy(a - b)}{y^2} 
$$

which gives:

$$
\frac{d\rho}{dt} = (a-b)\rho
$$

which has solution (this is just the same differential equation as the previous section):

$$
\rho(t) = \rho_0e^{(a-b)t}\text{ where }\rho_0=\rho(0)
$$

note that even if both population grow, but one grows faster than the other (eg $a > b$) then the overall population will grow but one will take over:


```python
def drho(rho, t, a, b):
    """Define the derivate of x"""
    return (a - b) * rho

a, b = 10, 5
rhos = odeint(func=drho, y0=1, t=t, args=(a, b))
plt.plot(rhos);
```


![png](output_9_0.png)


## Selection with constant population size

[Video](https://youtu.be/_bsaV5sq6ZU?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Let us consider the case of $x(t) + y(t)=1$: so the case of a constant population size (choosing a constant of 1 is just a question of scale). For this to be possible, the rates need to reduced:

$$\frac{dx}{dt}=x(a - \phi)\qquad\frac{dy}{dt}=y(b - \phi)$$

because $x(t) + y(t)=1$:

$$\frac{dx}{dt} + \frac{dy}{dt} = 0$$

also:

$$\frac{dx}{dt} + \frac{dy}{dt} = ax + by - \phi(x + y)= ax + by - \phi$$

thus $\phi=ax+by$ (this corresponds to the average of the fitness).

Substituting $y=1-x$ we have:

$$\frac{dx}{dt}=x(a - ax-b(1-x))=x(a(1 - x)-b(1-x))$$

giving:

$$\frac{dx}{dt}=x(a-b)(1-x)$$

We do not need to solve this differential equation. There are two stable points:

- $x=0$: no population of first type: no change
- $x=1$: no population of second type: no change

Also:

- $a=b$: if both types have the same fitness: no change


```python
def dxy(xy, t, a, b):
    """
    Define the derivate of x and y. 
    It takes `xy` as a vector
    """
    x, y = xy
    phi = a * x + b * y
    return x * (a - phi), y * (b - phi)

a, b = 10, 5
xys = odeint(func=dxy, y0=[.5, .5], t=t, args=(a, b))
plt.plot(xys);
```


![png](output_11_0.png)



```python
a, b = 10, 5
xys = odeint(func=dxy, y0=[1, 0], t=t, args=(a, b))
plt.plot(xys);
```


![png](output_12_0.png)



```python
a, b = 10, 5
xys = odeint(func=dxy, y0=[0, 1], t=t, args=(a, b))
plt.plot(xys);
```


![png](output_13_0.png)



```python
a, b = 5, 5
xys = odeint(func=dxy, y0=[.5, .5], t=t, args=(a, b))
plt.plot(xys);
```


![png](output_14_0.png)

# Evolutionary Game Theory

In the previous chapter, we considered the case of fitness being independant of the distribution of the whole population (the rates of increase of 1 type just depended on the quantity of that type). That was a specific case of Evolutionary game theory which considers **frequency dependent selection**.


---

## Frequency dependent selection

[Video](https://youtu.be/PFtwwrcouXY?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Consider. Let $x=(x_1, x_2)$ correspond to the population sizes of both types. The fitness functions are given by:

$$f_1(x)\qquad f_2(x)$$

As before we ensure a constant population size: $x_1 + x_2 = 1$. We have:

$$
\frac{dx_1}{dt}=x_1(f_1(x)-\phi) \qquad \frac{dx_2}{dt}=x_2(f_2(x)-\phi)
$$

we again have:


$$
\frac{dx_1}{dt} + \frac{dx_2}{dt}=x_1(f_1(x)-\phi) + x_2(f_2(x)-\phi)=0
$$


So $\phi=x_1f_1(x)+x_2f_2(x)$ (the average fitness).

We can substitute: $x_2=1-x_1$ to obtain:

$$
\frac{dx_1}{dt}=x_1(f_1(x)-x_1f_1(x)-x_2f_2(x))=x_1((1-x_1)f_1(x)-(1-x_1)f_2(x))
$$

$$
\frac{dx_1}{dt}=x_1(1-x_1)(f_1(x)-f_2(x))
$$

We see that we have 3 equilibria:

- $x_1=0$
- $x_1=1$
- Whatever distribution of $x$ that ensures: $f_1(x)=f_2(x)$


---

## Evolutionary Game Theory

Now we will consider potential differences of these equilibria. First we will return to considering Normal form games:

$$
A = 
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
$$

Evolutionary Game theory assigns strategies as types in a population, and indivividuals randomly encounter other individuals and play their corresponding strategy. The matrix $A$ correspods to the utility of a row player in a game where the row player is a given individual and the column player is the population.

This gives:

$$f_1=ax_1+bx_2\qquad f_2=cx_1+dx_2$$

or equivalently:

$$f=Ax\qquad \phi=fx$$

thus we have the same equation as before but in matrix notation:

$$\frac{dx}{dt}=x(f-\phi)$$

---

In this case, the 3 stable distributions correspond to:

- An entire population playing the first strategy;
- An entire population playing the second strategy;
- A population playing a mixture of first and second (such that there is indifference between the fitness).

---

We now consider the utility of a stable population in a **mutated** population.


---

## Mutated population

Given a strategy vector $x=(x_1, x_2)$, some $\epsilon>0$ and another strategy $y=(y_1, y_2)$, the post entry population $x_{\epsilon}$ is given by:

$$
x_{\epsilon} = (x_1 + \epsilon(y_1 - x_1), x_2 + \epsilon(y_2 - x_2))
$$



---

## Evolutionary Stable Strategies

[Video](https://youtu.be/lbzcToUM9ic?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Given a stable population distribution, $x$ it represents an **Evolutionary Stable Strategy** (ESS) if and only if there exists $\bar\epsilon>0$:

$$u(x, x_{\epsilon})>u(y, x_{\epsilon})\text{ for all }0<\epsilon<\bar\epsilon, y$$


where $u(x, y)$ corresponds to the fitness of strategy $x$ in population $y$ which is given by:

$$xAy^T$$

---

For the first type to be an ESS this corresponds to:

$$a(1-\epsilon)+b\epsilon > c(1-\epsilon) + d\epsilon$$

For small values of $\epsilon$ this corresponds to:

$$a>c$$

However if $a=c$, this corresponds to:

$$b>d$$

Thus the first strategy is an ESS (ie resists invasion) iff one of the two hold:

1. $a > c$
2. $a=c$ and $b > d$


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from scipy.integrate import odeint

t = np.linspace(0, 10, 100)  # Obtain 100 time points

def dx(x, t, A):
    """
    Define the derivate of x.
    """
    f = np.dot(A, x)
    phi = np.dot(f, x)
    return x * (f - phi)
```

The case of $a>c$:


```python
A = np.array([[4, 3], [2, 1]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);
```


![png](output_3_0.png)


The case of $a=c$ and $b>d$:


```python
A = np.array([[4, 3], [4, 1]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);
```


![png](output_5_0.png)


$a=c$ and $b < d$:


```python
A = np.array([[4, 3], [4, 5]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);
```


![png](output_7_0.png)


$a < c$:


```python
A = np.array([[1, 3], [4, 1]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);
```


![png](output_9_0.png)


We see in the above case that the population seems to stabilise at a mixed strategy. This leads to the general definition of the fitness of a mixed strategy: $x=(x_1, x_2)$:

$$u(x,x) = x_1f_1(x)+x_2f_2(x)$$

---

## General condition for ESS

[Video](https://youtu.be/zkhInay5xQc?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

If $x$ is an ESS, then for all $y\ne x$, either:

1. $u(x,x)>u(y,x)$
2. $u(x,x)=u(y,x)$ and $u(x,y)>u(y,y)$
---


Conversely, if either (1) or (2) holds for all $y\ne x$ then $x$ is an ESS.

---

### Proof

---

If $x$ is an ESS, then by definition:

$$u(x,x_{\epsilon})>u(y,x_{\epsilon})$$

which corresponds to:

$$(1-\epsilon)u(x,x)+\epsilon u(x,y)>(1-\epsilon)u(y,x)+\epsilon u(y,y)$$

- If condition 1 of the theorem holds then the above inequality can be satisfied for \\(\epsilon\\) sufficiently small. If condition 2 holds then the inequality is satisfied.
- Conversely:

    - If $u(x,x) < u(y,x)$ then we can find $\epsilon$ sufficiently small such that the inequality is violated.

    - If $u(x, x) = u(y,x)$ and $u(x,y) \leq u(y,y)$ then the inequality is violated.

This result gives us an efficient way of computing ESS. The first condition is in fact almost a condition for Nash Equilibrium (with a strict inequality), the second is thus a stronger condition that removes certain Nash equilibria from consideration. This becomes particularly relevant when considering Nash equilibrium in mixed strategies.

To find ESS in a pairwise context population game we:

1. Write down the associated two-player game $(A, A^T)\in{\mathbb{R}^{m\times n}}^2$;
2. Identify all symmetric Nash equilibria of the game;
3. Test the Nash equilibrium against the two conditions of the above Theorem.

Let us apply it to the one example that seemed to stabilise at a mixed strategy:

$$
A =\begin{pmatrix}
1 & 3\\
4 & 1
\end{pmatrix}
$$


```python
import nashpy as nash
game = nash.Game(A, A.transpose())
list(game.support_enumeration())
```




    [(array([1., 0.]), array([0., 1.])),
     (array([0., 1.]), array([1., 0.])),
     (array([0.4, 0.6]), array([0.4, 0.6]))]



Looking at $x=(.4, .6)$ (which is the only symmetric nash equilibrium), we have

$$u(x, x)=u(y, x)$$

and (recall $y_1 + y_2 = 1$):

$$
u(x, y)=2.8y_1 + 1.8y_2=2.8y_1 + 1.8(1-y_1)=y_1+1.8
$$

\begin{align}
u(y, y)&=y_1^2+3y_1y_2+4y_1y_2+y_2^2\\
       &=y_1^2+7y_1-7y_1^2+1 - 2y_1 + y_1^2\\
       &=5y_1-5y_1^2+1
\end{align}

Thus:

$$u(x, y) - u(y, y) = -4y_1+5y_1^2+.8 = 5(y_1 - .4)^2$$

however $y_1\ne.4$ thus $x=(.4, .6)$ is an ESS.

Here is some code to verify the above calculations:


```python
import sympy as sym
sym.init_printing()
A = sym.Matrix(A)
y_1, y_2 = sym.symbols("y_1, y_2")
y = sym.Matrix([y_1, y_2])
A, y
```




$$\left ( \left[\begin{matrix}1.0 & 3.0\\4.0 & 1.0\end{matrix}\right], \quad \left[\begin{matrix}y_{1}\\y_{2}\end{matrix}\right]\right )$$




```python
rhs = sym.expand((y.transpose() * A * y)[0].subs({y_2: 1 - y_1}))
rhs
```




$$- 5.0 y_{1}^{2} + 5.0 y_{1} + 1.0$$




```python
lhs = sym.expand((sym.Matrix([[.4, .6]]) * A * y)[0].subs({y_2: 1-y_1}))
lhs
```




$$1.0 y_{1} + 1.8$$




```python
sym.factor(lhs - rhs)
```




$$1.0 \left(1.0 y_{1} - 0.4\right)^{2}$$


# Moran Processes

The evolutionary models discussed in the previous chapters assume an infinite population that can be divided in to infinitessimal parts. Finite populations can also be studied using a model called a Moran Process (first described in 1958).

---

## Moran process with neutral drift

[Video](https://youtu.be/OeMku85hwEc?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

Consider a population of two types of fixed size $N$. This can be represented as a vector of the form: $(i, N-i)$ where $i\geq 0$ represents the number of individuals of the first type.

The term **neutral** drift refers to the fact that the two types reproduce at the same rate.

The Moran process is as follows:

- At a given time step: select a random individual for reproduction and a random individual for elimination
- The eliminated individual is replaced by a new individual of the same type as the individual chosen for reproduction.
- Proceed to the next time step.
- The process terminates when there is only one type of individual in the population.

---

Here is some simple Python code that simulates such a Process assuming an initial population of $(3, 3)$:


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def neutral_moran(N, i=1, seed=0):
    """
    Return the population counts for the Moran process with neutral drift.
    """

    population = [0 for _ in range(i)] + [1 for _ in range(N - i)]
    counts = [(population.count(0), population.count(1))]
    np.random.seed(seed)
    while len(set(population)) == 2:
        reproduce_index = np.random.randint(N)
        eliminate_index = np.random.randint(N)
        population[eliminate_index] = population[reproduce_index]
        counts.append((population.count(0), population.count(1)))
    return counts
    
N = 6
plt.plot(neutral_moran(N=N, i=3, seed=6));
```


![png](output_1_0.png)


For different seeds we see we obtain different results. What becomes of interest is not the path but the end result: which strategy overcomes the presence of the other?


```python
def neutral_fixation(N, i=None, repetitions=10):
    """
    Repeat the neutral Moran process and calculate the fixation probability
    """
    fixation_count = 0
    for seed in range(repetitions):
        final_counts = neutral_moran(N=N, i=i, seed=seed)
        if final_counts[-1][0] > 0:
            fixation_count += 1 

    return  fixation_count / repetitions 
```

Let us take a look at probability of the first strategy taking over for different starting populations:


```python
probabilities = [neutral_fixation(N, i=i, repetitions=500) for i in range(1, N)]
plt.scatter(range(1, N), probabilities)
plt.xlabel("$i$")
plt.ylabel("$x_i$");
```


![png](output_5_0.png)


We see that as the initial population starts with more of a given type, the chance that that type "takes over" (becomes fixed) grows.

This Moran Process is a specific case of a Markov Process:

- A given state of the system can be described by a single integer $0\leq i\leq N$;
- The state to state transition probabilities are given by:

  $$
  \begin{aligned}
  p_{i, i-1}&=\frac{i(N - i)}{N^2}\\
  p_{i, i+1}&=\frac{i(N - i)}{N^2}\\
  p_{i, i}&=1 - p_{i, i-1} - p_{i, i+1}
  \end{aligned}
  $$
  
  We also have two absorbing states (when the Moran process ends):
  
  $$p_{00}=1\qquad p_{0i}=0\text{ for all }i>0$$
  
  $$
  p_{NN}=1\qquad p_{Ni}=0\text{ for all } N>i
  $$
  
  these transitions can be represented as a matrix. Here for example is the matrix for $N=6$:


```python
N = 6
p = np.zeros((N + 1, N + 1))
p[0, 0] = 1
p[N, N] = 1
for i in range(1, N):
    for j in [i - 1, i + 1]:
        p[i, j] = i * (N - i) / (N ** 2)
    p[i, i] = 1 - sum(p[i, :])
p.round(2)
```




    array([[1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
           [0.14, 0.72, 0.14, 0.  , 0.  , 0.  , 0.  ],
           [0.  , 0.22, 0.56, 0.22, 0.  , 0.  , 0.  ],
           [0.  , 0.  , 0.25, 0.5 , 0.25, 0.  , 0.  ],
           [0.  , 0.  , 0.  , 0.22, 0.56, 0.22, 0.  ],
           [0.  , 0.  , 0.  , 0.  , 0.14, 0.72, 0.14],
           [0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 1.  ]])



The above corresponds to a particular type of Markov process called a Birth-Death process

---

## Birth death process

[Video](https://youtu.be/zJQQF2tq9AA?list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

A birth death process is a Markov process with the following properties:

- $p_{i,i+1}+p_{i,i-1}\leq 1$
- $p_{ii}=1-p_{i,i+1}-p_{i,i-1}$
- $p_{00}=1$ and $p_{NN}=1$

---

Thus we have two absorbing states: $\{0, N\}$. Let us denote by $x_i$ the probability of being in $state$ $i$ and eventually reaching state $N$. 

We have the following linear system:

\begin{align}
    x_0&=0\\
    x_i&=p_{i,i-1}x_{i-1}+p_{ii}x_i+p_{i,i+1}x_{i+1}\text{ for all }0< i< N-1\\
    x_N&=1\\
\end{align}

---

## Theorem: Fixation probabilities for the birth death process

Given a birth death process as defined above, the fixation probability $x_i$ is given by:

$$x_i=\frac{1+\sum_{j=1}^{i-1}\prod_{k=1}^j\gamma_k}{1+\sum_{j=1}^{N-1}\prod_{k=1}^j\gamma_k}$$

where:

$$
\gamma_k = \frac{p_{k,k-1}}{p_{k,k+1}}
$$

### Proof

We have:

$$
\begin{aligned}
    p_{i,i+1}x_{i+1} & = -p_{i,i-1}x_{i-1} + x_i(1 - p_{ii}) \\ 
    p_{i,i+1}x_{i+1} & = p_{i,i-1}(x_{i} - x_{i-1}) + x_ip_{i,i+1} \\ 
    x_{i+1} - x_i    & = \frac{p_{i, i-1}}{p_{i, i+1}}(x_i-x_{i-1})=\gamma_i(x_i-x_{i-1})
\end{aligned}
$$

We observe that:

$$
\begin{aligned}
    x_2 - x_1 &= \gamma_1(x_1-x_{0})=\gamma_1x_1\\
    x_3 - x_2 &= \gamma_2(x_2-x_1)=\gamma_2\gamma_1x_1\\
    x_4 - x_3 &= \gamma_3(x_3-x_2)=\gamma_3\gamma_2\gamma_1x_1\\
              &\; \vdots & \\
    x_{i+1} - x_i &= \gamma_i(x_i-x_{i-1})=\prod_{k=1}^i\gamma_kx_1\\
               &\; \vdots & \\   
    x_{N} - x_{N-1} &= \gamma_{N-1}(x_{N-1}-x_{N-2})=\prod_{k=1}^{N-1}\gamma_kx_1\\
\end{aligned}
$$

thus we have:

$$x_i=\sum_{j=0}^{i-1}x_{j+1}-x_j=\left(1+\sum_{j=1}^{i-1}\prod_{k=1}^j\gamma_k\right)x_1$$

we complete the proof by solving the following equation to obtain $x_1$:

$$x_N=1=\left(1+\sum_{j=1}^{N-1}\prod_{k=1}^j\gamma_k\right)x_1$$

---

In the case of neutral drift (considered above) we have:

$$p_{i,i-1}=p_{i,i+1}$$

thus:

$$
\gamma_i=1
$$

so:

$$
x_i=\frac{1+\sum_{j=1}^{i-1}\prod_{k=1}^j\gamma_k}{1+\sum_{j=1}^{N-1}\prod_{k=1}^j\gamma_k}=\frac{1+i-1}{1+N-1}=\frac{i}{N}
$$


```python
probabilities = [neutral_fixation(N, i=i, repetitions=500) for i in range(1, N)]
plt.scatter(range(1, N), probabilities, label="Simulated")
plt.plot(range(1, N), [i / N for i in range(1, N)], label="Theoretic: $i/N$", linestyle="dashed")
plt.xlabel("$i$")
plt.ylabel("$x_i$")
plt.legend();
```


![png](output_9_0.png)


---

## Fixation probability

The fixation probability in a Moran process is the probability that a give type starting with $i=1$ individuals takes over an entire population. We denote the fixation probabilities of the first/second type as $\rho_1$ and $\rho_2$ respectively and we have:

$$
\rho_1=x_1
$$

$$
\rho_2=1-x_{N-1}
$$

---

We will now consider a Moran process on a game:

---

## Moran process on a game

[Video](https://www.youtube.com/watch?v=TpqVoF1fBF8&index=43&list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)


Consider a matrix $A\in\mathbb{R}^{m\times n}$ representing a game with two strategies. 

$$
A=
\begin{pmatrix}
    a & b\\
    c & d
\end{pmatrix}
$$

The Moran process is as follows:

- At a given time step: all individuals play all other individuals.
- Obtain their fitness as given by the game.
- Randomly select an individual proportional to their fitness as an individual to be reproduced
- Uniformly select an individual to be replaced
- Proceed to the next time step.
- The process terminates when there is only one type of individual in the population.


Assuming $i$ individuals of the first type, the fitness of both types is given respectively by:

$$f_{1i}=\frac{a(i-1)+b(N-i)}{N-1}$$
$$f_{2i}=\frac{c(i)+d(N-i-1)}{N-1}$$

The transition probabilities are then given by:

$$p_{i,i+1}=\frac{if_{1i}}{if_{1i} + (N-i)f_{2i}}\frac{N-i}{N}$$
$$p_{i,i-1}=\frac{(N-i)f_{2i}}{if_{1i} + (N-i)f_{2i}}\frac{i}{N}$$

which gives:

$$\gamma_i=\frac{f_{2i}}{f_{1i}}$$

thus:

$$
x_i=\frac{1+\sum_{j=1}^{i-1}\prod_{k=1}^j\gamma_k}{1+\sum_{j=1}^{N-1}\prod_{k=1}^j\gamma_k}
$$

---

Here is some code to carry out this calculation:


```python
def theoretic_fixation(N, game, i=1):
    """
    Calculate x_i as given by the above formula
    """
    f_ones = np.array([(game[0, 0] * (i - 1) + game[0, 1] * (N - i)) / (N - 1) for i in range(1, N)])
    f_twos = np.array([(game[1, 0] * i + game[1, 1] * (N - i - 1)) / (N - 1) for i in range(1, N)])
    gammas = f_twos / f_ones
    return (1 + np.sum(np.cumprod(gammas[:i-1]))) / (1 + np.sum(np.cumprod(gammas)))
```

Here is an example of calculating $x_1$ for the following game for $N=4$:

[Video](https://www.youtube.com/watch?v=3sBVrnQhemE&index=44&list=PLnC5h3PY-znxMsG0TRYGOyrnEO-QhVwLb)

$$
A = 
\begin{pmatrix}
    4 & 1\\
    1 & 4
\end{pmatrix}
$$


```python
A = np.array([[4, 1], 
              [1, 4]])
theoretic_fixation(N=4, i=1, game=A)
```




    0.125



Applying the theorem gives:

$$
\begin{aligned}
f_{1i}&=\frac{4(i - 1) + 4 - i}{3} = \frac{4i-4+4-i}{3}=i\\
f_{2i}&=\frac{i + 4(3 - i)}{3} = \frac{12-3i}{3}=4-i
\end{aligned}
$$

$$
\gamma_i = \frac{f_{2i}}{f_{1i}}=\frac{4-i}{i}=\frac{4}{i}-1
$$

Thus:

$$
\begin{aligned}
x_1 & =\frac{1 + \sum_{j=1}^{0}\prod_{k=1}^{j}\gamma_k}{1 + \sum_{j=1}^{4 - 1}\prod_{k=1}^{j}\gamma_k}\\  
    & =\frac{1}{1 + \sum_{j=1}^{3}\prod_{k=1}^{j}\gamma_k}\\ 
    & =\frac{1}{1 + \gamma_1 + \gamma_1\times \gamma_2 + \gamma_1 \times \gamma_2 \times \gamma_3}\\ 
    & =\frac{1}{1+3+3\times 1 + 3 \times 1\times \frac{1}{3}} = \frac{1}{1 + 3 + 3 + 1}=\frac{1}{8}\\
\end{aligned}
$$

Here is some code to simulate a Moran process.


```python
def moran(N, game, i=1, seed=0):
    """
    Return the population counts for 
    the Moran process on a 2 by 2 game
    """
    population = [0 for _ in range(i)] + [1 for _ in range(N - i)]
    counts = [(population.count(0), population.count(1))]
    
    np.random.seed(seed)
    
    while len(set(population)) == 2:
        
        scores = []
        
        for i, player in enumerate(population):
            total = 0
            for j, opponent in enumerate(population):
                if i != j:
                    total += game[player, opponent]
            scores.append(total)

        total_score = sum(scores)
        probabilities = [score / total_score for score in scores]
        reproduce_index = np.random.choice(range(N), p=probabilities)
        
        eliminate_index = np.random.randint(N)
        population[eliminate_index] = population[reproduce_index]
        
        counts.append((population.count(0), population.count(1)))
    return counts


def fixation(N, game, i=None, repetitions=10):
    """
    Repeat the Moran process and calculate the fixation probability
    """
    fixation_count = 0
    for seed in range(repetitions):
        final_counts = moran(N=N, i=i, game=game, seed=seed)
        if final_counts[-1][0] > 0:
            fixation_count += 1
    return  fixation_count / repetitions
```

Here is one specific simulated process for the game with initial population: $(1, 7)$ where the invader manages to become fixed.


```python
N = 8
plt.plot(moran(N=N, i=1, seed=44, game=A));
```


![png](output_19_0.png)


Here is how the fixation probabilities vary for different initial populations:


```python
probabilities = [fixation(N, i=i, game=A, repetitions=500) for i in range(1, N)]
plt.scatter(range(1, N), probabilities, label="Simulated")
plt.plot(range(1, N), [i / N for i in range(1, N)], label="Neutral: $i/N$", linestyle="dashed")
plt.plot(range(1, N), [theoretic_fixation(N=N, i=i, game=A) for i in range(1, N)], label="Theoretic")
plt.xlabel("$i$")
plt.ylabel("$x_i$")
plt.legend();
```


![png](output_21_0.png)

# Contemporary research topics

In this section of the course, we will look at a number of areas of recent (and ongoing!) mathematical research.

In particular 4 pieces of work will be reviewed:

- [Measuring the price of anarchy in critical care unit interactions](https://link.springer.com/article/10.1057/s41274-016-0100-8)
- [Iterated Prisoner’s Dilemma contains strategies that dominate any evolutionary opponent](http://www.pnas.org/content/109/26/10409.abstract)
- [Studying the emergence of invasiveness in tumours using game theory](https://link.springer.com/article/10.1140/epjb/e2008-00249-y)
- [Evolution Reinforces Cooperation with the Emergence of Self-Recognition Mechanisms: an empirical study of the Moran process for the iterated Prisoner's dilemma](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0204981)

These four papers offer insights in to modern game theoretic research across the topics studied in this course. As a class we will discuss the papers in turn (so you will need to have read them).

This will be examinable. Questions might include:

- What is the main area of game theory used in this paper?
- What are/is the main result of this paper?
- Give an overview of a/some specific proof/calculation/method used in this paper?
- Critique this paper: how could it be improved.
- How does this paper sit in comparison to the rest of the literature on the subject.

## [Measuring the price of anarchy in critical care unit interactions](https://link.springer.com/article/10.1057/s41274-016-0100-8)

This is a paper that looks at a 2 player game modelling hospital interactions.

## [Iterated Prisoner’s Dilemma contains strategies that dominate any evolutionary opponent](http://www.pnas.org/content/109/26/10409.abstract)

This is a paper that considers a particular type of strategy in the Iterated Prisoner's Dilemma

## [Studying the emergence of invasiveness in tumours using game theory](https://link.springer.com/article/10.1140/epjb/e2008-00249-y)

This is a paper that looks at cancer tumours using evolutionary game theory.

## [Evolution Reinforces Cooperation with the Emergence of Self-Recognition Mechanisms: an empirical study of the Moran process for the iterated Prisoner's dilemma](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0204981)

This is a paper that gives an in depth numerical study of Moran processes.
