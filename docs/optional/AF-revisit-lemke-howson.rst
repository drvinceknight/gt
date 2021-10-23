AF- Revisiting Lemke-Howson
===========================

Corresponding chapters
----------------------

- `Lemke Howson algorithm <https://vknight.org/gt/chapters/07/>`_

**Duration**: 50 minutes


Objectives
----------

- Re visit Lemke Howson Algorithm


Notes
-----


Consider the :math:`(A,B)\in{\mathbb{R}^{2\times 2}}^2` game:

.. math::

   A = \begin{pmatrix}
   1 & 4 \\
   -3 & 2
   \end{pmatrix}
   \qquad
   B = \begin{pmatrix}
   5 & 2 \\
   -1 & 9
   \end{pmatrix}

**Ask students in pairs to construct the column player best response polytope**

First we add :math:`4` to all elements to ensure they are positive:

.. math::

   A = \begin{pmatrix}
   5 & 8 \\
   1 & 6
   \end{pmatrix}
   \qquad
   B = \begin{pmatrix}
   9 & 6 \\
   3 & 13
   \end{pmatrix}

By definition
(https://vknight.org/gt/chapters/06/#Definition-of-best-response-polytopes), the
column player best response polytope :math:`\mathcal{Q}` is given by:

.. math::

   \mathcal{Q} = \{y\in\mathbb{R}^{n}\;|\;Ay\leq 1\;y\geq0\}

So the inequalities are:

.. math::

   \begin{align*}
   5y_1+8y_2&\leq 1&&\text{ label: }0\\
   y_1 + 6y_2&\leq 1&&\text{ label: }1\\
   y_1&\geq 0&&\text{ label: }2\\
   y_2&\geq 0&&\text{ label: }3
   \end{align*}

The first two inequalities come from :math:`Ay\leq 1`, however, :math:`Ay`
corresponds to the row players utility against **vertex** :math:`y`. 

Note that
everything is scaled so that the best response of the row player is :math:`1`
(the scaling takes place in the strategies/vertices).

**Thus** if a vertex has label :math:`0` or :math:`1` that implies that the
first/second row player strategy is a best response to :math:`y`.

**We will return to this idea** but first let us plot our :math:`Q`. We start by
rearranging our inequalities:

.. math::

   \begin{align*}
   y_2 &\leq 1/8 - 5/8y_1&&\text{ label: }0\\
   y_2 &\leq 1/6 - y_1/6&&\text{ label: }1\\
   y_1&\geq 0&&\text{ label: }2\\
   y_2&\geq 0&&\text{ label: }3
   \end{align*}

Now let us sketch these::

    import matplotlib.pyplot as plt
    %matplotlib inline
    y1s = [0, 1]
    first_line = [1 / 8 - 5 / 8 * y for y in y1s]
    second_line = [1 / 6 - y / 6 for y in y1s]
    plt.figure()
    plt.plot(first_line, label="$1/8-5/8y_1$ (label: 0)")
    plt.plot(second_line, label="$1/6-y_1/6$ (label: 1)")
    plt.legend();

This gives:

.. image:: ../assets/activities/AA-dominated-strategy-polytope.png
   :width: 500px

We can see that our polytope is a straightforward triangle and that no vertex
will ever have label :math:`1`.

**Discuss if this is OK?**

Returning to the game:

.. math::
   A = \begin{pmatrix}
   \underline{5} & \underline{8} \\
   1 & 6
   \end{pmatrix}

We see that the first strategy dominates the second: so the second strategy **is
never** a best response.

Our vertices with labels are:

.. math::

   \begin{align*}
   (0, 0)&\text{ labels }\{2, 3\}\\
   (0, 1/8)&\text{ labels }\{0, 2\}\\
   (1/5, 0)&\text{ labels }\{0, 3\}\\
   \end{align*}

**Exercise:**

Obtain the best response polytope for the row player:

By definition
(https://vknight.org/gt/chapters/06/#Definition-of-best-response-polytopes), the
row player best response polytope :math:`\mathcal{P}` is given by:

.. math::

   \mathcal{Q} = \{x\in\mathbb{R}^{m}\;|\;x\geq0\;xB\leq 1\}

So the inequalities are:

.. math::

   \begin{align*}
   x_1&\geq 0&&\text{ label: }0\\
   x_2&\geq 0&&\text{ label: }1\\
   9x_1+3x_2&\leq 1&&\text{ label: }2\\
   6x_1 + 13x_2&\leq 1&&\text{ label: }3
   \end{align*}

Rearranging:

.. math::

   \begin{align*}
   x_1&\geq 0&&\text{ label: }0\\
   x_2&\geq 0&&\text{ label: }1\\
   x_2&\leq 1/3 - 3 x_1&&\text{ label: }2\\
   x_2&\leq 1/13 - 6/13x_1&&\text{ label: }3
   \end{align*}

Now let us sketch these::

    x1s = [0, 1]
    first_line = [1 / 3 - 3 * x for x in x1s]
    second_line = [1 / 13 - 6 / 13 * x for x in x1s]
    plt.figure()
    plt.plot(first_line, label="$1/3-3x_1$ (label: 2)")
    plt.plot(second_line, label="$1/13-6/13x_1$ (label: 3)")
    plt.legend();

This gives:

.. image:: ../assets/activities/AA-row-player-strategy-polytope.png
   :width: 500px

We see that there our polytope has 4 vertices:

.. math::

   \begin{align*}
   (0, 0)&\text{ labels }\{0, 1\}\\
   (0, 1/6)&\text{ labels }\{0, 3\}\\
   (1/9, 0)&\text{ labels }\{1, 2\}\\
   (10/99, 1/33)&\text{ labels }\{2, 3\}\\
   \end{align*}

Here is some sympy code to verify the intersection of both boundaries::

   >>> import sympy as sym
   >>> x = sym.Symbol("x")
   >>> sym.solveset(sym.S(1) / 3-3 * x - sym.S(1) / 1/13 + sym.S(6) / 13 * x, x)
   {10/99}

We now carry out the Lemke-Howson algorithm.

- Start at :math:`((0, 0), (0, 0))`, have labels :math:`\{0, 1, 2, 3\}`. Drop 3 in
  :math:`\mathcal{Q}`: move to :math:`((0, 0), (0, 1/8))` and pick up 0.
- At :math:`((0, 0), (0, 1/8))`, have labels :math:`\{0, 1, 2\}`. Drop 0 in
  :math:`\mathcal{P}`: move to :math:`((1 / 9, 0), (0, 1/8))` and pick up 2.
- At :math:`((1/9, 0), (0, 1/8))`, have labels :math:`\{0, 1, 2\}`. Drop 2 in
  :math:`\mathcal{Q}`: move to :math:`((1 / 9, 0), (1/5, 0))` and pick up 3.
- At :math:`((1/9, 0), (1/5, 0))`, have labels :math:`\{0, 1, 2, 3\}`: stop.

Normalise to get:

.. math::

   ((1, 0), (1, 0))

Now, ask students to carry this out using tableaux:

Apply definitions to get:


.. math::

   T_r = \begin{pmatrix}
       9 &  3  &  1 & 0 & 1 \\
       6 &  13 &  0 & 1 & 1 \\
   \end{pmatrix}

and:

.. math::

   T_c = \begin{pmatrix}
       1 &  0  &  5 & 8 & 1 \\
       0 &  1  &  1 & 6 & 1 \\
   \end{pmatrix}


- :math:`T_r` has labels :math:`\{0, 1\}`.
- :math:`T_c` has labels :math:`\{2, 3\}`.


Now let us drop 3 from :math:`T_c`. The minimum ratio test: :math:`1/8<1/6` so
pivot on 1st row.

.. math::

   T_c = \begin{pmatrix}
       1 &  0  &  5  & 8 & 1 \\
      -6 &  8  & -22 & 0 & 2 \\
   \end{pmatrix}

which has labels :math:`\{0, 2\}` thus we need to drop 0 in :math:`\mathcal{P}`.
The minimum ratio test: :math:`1/9<1/6` so pivot on 1st row:

.. math::

   T_r = \begin{pmatrix}
       9 &  3  &  1 & 0 & 1 \\
       0 &  99 &  -6 & 9 & 3 \\
   \end{pmatrix}

which has labels :math:`\{1, 2\}` thus we need to drop 2 in :math:`\mathcal{Q}`.
The minimum ratio test: there is only 1 positive ratio so we pivot on 1st row.

.. math::

   T_c = \begin{pmatrix}
       1 &  0  &  5  & 8 & 1 \\
      -8 & 40  &  0  & 176 & 32 \\
   \end{pmatrix}

which has labels :math:`\{0, 3\}` thus we have a Nash equilibria.

Recall that the variable for :math:`T_r` in order are:

.. math::

   x_1, x_2, s_1, s_2


Recall that the variable for :math:`T_r` in order are:

.. math::

   s_1, s_2, y_1, y_2

Thus, :math:`5y_1=1` and :math:`9x_1=1` which gives:

.. math::

   x = (1/9, 0)\qquad y=(1/5, 0)

after normalising we get the required result:

.. math::

   \sigma_r = (1, 0)\qquad \sigma_c=(1, 0)
