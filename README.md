# Game Theory

## Description

This is a course on Game theory. It covers 2 main topics:

1. Equilibrium computation and Repeated games;
2. Evolutionary game theory;
3. Current research topics

The course is taught in an active learning framework with class time being used
for activities and demonstrations whilst the content is made available to the
students at the start of the course.

Throughout this course concepts are illustrated/demonstrated using
Python. In particular the following libraries are used:

- [Nashpy](https://github.com/drvinceknight/Nashpy): computation of
  equilibria.
- [Axelrod](http://axelrod.readthedocs.io/en/stable/): study of the Iterated
  Prisoner's Dilemma.
- [Sympy](http://www.sympy.org/en/index.html): used to verify and carry out
  symbolic computations.

## Syllabus (WIP):

### Introduction to Games

#### Concepts

- Normal form games;
- Strategies (pure and mixed), utility computation;

#### Activities:

- Play the two thirds of the average game;
- Play pairwise Head or Tails game.

**Number of sessions: 2**

### Nash equilibrium

#### Concepts

- Dominated strategies: definitions and use to simplify games;
- Best response strategies: definitions and use to simplify games;
- Nash equilibria: definitions.

#### Activities:

- Play golden balls in class;
- Play against a mixed strategy;
- Rock Paper Scissors Lizard Spock tournament.

**Number of sessions: 3**

### Nash equilibria computation

#### Concepts

- Support enumeration in two by two games;
- Support enumeration in larger games
- Lemke Howson algorithm.

#### Activities

- In class calculations of support enumeration for larger games;
- Create a polytope (students as nodes), labels as post it notes and solve
  games.

**Number of sessions: 3**

### Repeated Games

#### Concepts

- What a strategy in a repeated game is.
- Equilibria of repeated games that is not sequence of stage nash
- The Iterated Prisoner's Dilemma
- Axelrod's tournament
- Infinitely repeated games

#### Activities

- Play an IPD tournament
- Play a probabilistic ending IPD tournament

**Number of sessions: 3**

### Evolutionary games in infinite populations

#### Concepts

- Population games
- Stable strategies

#### Activities

- Modelling using computer code

**Number of sessions: 2**

### Evolutionary games in finite populations

#### Concepts

- Moran processes;
- Obtaining expression for fixation in 2 strategy games;

#### Activities

- Use dice for N=2
- Pair wise Moran process in class (N>2)

### Contemporary research topic

#### Concepts

- IPD
- Game theoretic healthcare modelling

#### Activities

- Choosing a paper and working through it. Potentials:
    - Rhino paper
    - CCU Game paper with Jeff and Iza
    - Press and Dyson Paper
    - Moran paper

## Contents of this repository

```
|--- README.md
|--- environment.yml  # A conda environment file
|--- docs  # documentation (notes for the class leader)
|--- nbs  # nbs representing content for the site
```
