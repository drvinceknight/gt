---
layout: class-notes
title: "Matching Games"
tags:
  - matching-games
---

## Activity (20 minutes)

### Student Instruction Sheet

You have been given a character card. Each card describes the personality,  
strengths, and tendencies of a famous mathematician or physicist. A short  
sentence also gives a fact about their historical contributions.

Your task is to imagine how your character would rank the members of the  
opposite group.

1. Read your card carefully.
2. Think about which characters your own character would most like to work  
   with, and which they would not.
3. Write down a ranked list from most preferred to least preferred.
4. Keep your preferences private until the matching begins.

We will then run the **stable matching algorithm** together. Be ready to:

- Propose to other characters in the order you ranked them.
- Accept or reject proposals depending on your list.

After the activity, we will discuss:

- How the algorithm guarantees stability.
- How the outcome changes depending on who proposes.
- What this might mean in real-world applications of matching algorithms.

---

### Teacher Instruction Sheet

Below are **suggested preference orders** for each character. These are based  
on the biographies provided, but you can change them to keep the game fresh.  
(Students can also invent their own lists if you want more variety.)

#### Mathematicians vs Physicists

**Mathematicians**

- Gauss: Einstein > Curie > Newton > Feynman
- Noether: Curie > Feynman > Einstein > Newton
- Turing: Einstein > Feynman > Curie > Newton
- Euler: Newton > Curie > Einstein > Feynman

**Physicists**

- Einstein: Noether > Gauss > Turing > Euler
- Curie: Noether > Euler > Turing > Gauss
- Newton: Gauss > Euler > Noether > Turing
- Feynman: Turing > Noether > Gauss > Euler

---

#### Past vs Present Mathematicians

**Past Mathematicians**

- Euclid: Erdős > Lovelace > Turing > Noether
- Archimedes: Noether > Lovelace > Erdős > Turing
- Euler: Turing > Noether > Lovelace > Erdős
- Newton: Noether > Turing > Euler > Erdős

**Present Mathematicians**

- Noether: Archimedes > Euler > Newton > Euclid
- Lovelace: Newton > Euler > Euclid > Archimedes
- Turing: Euler > Newton > Noether > Euclid
- Erdős: Euclid > Newton > Noether > Archimedes

---

#### Teaching Notes

- Start with one group proposing (e.g., mathematicians to physicists).
- Record the matching.
- Reset, then swap proposers (e.g., physicists to mathematicians).
- Compare the two outcomes and highlight who benefits in each case.

Use the discussion to connect to fairness, power, inclusivity, and real-world  
matching systems like school admissions and residency matches.

---

### Character Bios

---

#### Mathematicians vs Physicists

**Carl Friedrich Gauss (1777–1855)**  
Gauss, often called the “Prince of Mathematics,” valued precision and elegance.  
He preferred collaborators who respected rigor and quiet focus. He was less  
interested in flashy ideas than in solid foundations.  
_Contribution:_ Gauss made fundamental contributions to number theory,  
statistics, analysis, differential geometry, and electromagnetism.

**Emmy Noether (1882–1935)**  
A pioneer of abstract algebra, Noether loved symmetry and generality. She  
thrived with creative, inclusive collaborators and dismissed narrow or rigid  
approaches.  
_Contribution:_ Noether’s theorem revealed the deep link between symmetries and  
conservation laws in physics.

**Alan Turing (1912–1954)**  
Visionary and analytical, Turing admired boundary-pushing ideas in logic and  
computation. He was impatient with old-fashioned approaches but enjoyed  
brilliance and playful creativity.  
_Contribution:_ Turing is considered a father of computer science and helped  
crack the Enigma code in World War II.

**Leonhard Euler (1707–1783)**  
Prolific and versatile, Euler thrived on solving many problems with boundless  
energy. He liked enthusiastic colleagues and disliked skeptics or show-offs.  
_Contribution:_ Euler made groundbreaking contributions across mathematics,  
including graph theory, analysis, and mechanics.

**Albert Einstein (1879–1955)**  
Einstein valued bold, imaginative ideas and admired eccentric creativity. He  
struggled with rigid, routine-based thinkers.  
_Contribution:_ Einstein developed the special and general theories of  
relativity, revolutionizing physics.

**Marie Curie (1867–1934)**  
Curie respected discipline, patience, and practicality. She admired  
collaborators who balanced creativity with hard work, but avoided drama.  
_Contribution:_ Curie discovered polonium and radium, and pioneered research in  
radioactivity.

**Isaac Newton (1642–1727)**  
Intense and ambitious, Newton respected power and clear reasoning. He liked  
determined collaborators but disliked rivals.  
_Contribution:_ Newton developed the laws of motion and universal gravitation,  
and co-invented calculus.

**Richard Feynman (1918–1988)**  
Playful and curious, Feynman thrived on excitement and fresh perspectives. He  
disliked rigidity and self-importance.  
_Contribution:_ Feynman contributed to quantum electrodynamics and became known  
as a brilliant physics communicator.

---

#### Past vs Present Mathematicians

**Euclid (c. 300 BCE)**  
Euclid loved order, clarity, and logical systems. He admired systematic  
thinkers and disliked chaotic approaches.  
_Contribution:_ Euclid wrote _Elements_, one of the most influential works in  
the history of mathematics.

**Archimedes (c. 287–212 BCE)**  
Archimedes was inventive and practical, preferring energy and cleverness. He  
grew frustrated with endless theorizing without application.  
_Contribution:_ Archimedes advanced geometry, mechanics, and invented ingenious  
machines such as war engines and pumps.

**Leonhard Euler (1707–1783)**  
(Prolific and versatile, as above.) Euler enjoyed enthusiastic collaborators  
and disliked obstruction or excessive skepticism.  
_Contribution:_ Euler bridged pure and applied mathematics, creating much of  
modern mathematical notation.

**Isaac Newton (1642–1727)**  
(Intense and ambitious, as above.) Newton demanded high standards and resisted  
undermining of his authority.  
_Contribution:_ Newton’s _Principia Mathematica_ laid the foundation for  
classical mechanics.

**Emmy Noether (1882–1935)**  
(Creative, symmetry-loving, as above.) She admired open collaboration and  
avoided rigid hierarchies.  
_Contribution:_ Noether’s algebraic insights transformed mathematics and  
physics alike.

**Ada Lovelace (1815–1852)**  
Visionary and imaginative, Lovelace embraced the link between art and  
mathematics. She admired forward-looking colleagues and disliked dismissive  
critics.  
_Contribution:_ Lovelace is regarded as the first computer programmer for her  
notes on Charles Babbage’s Analytical Engine.

**Alan Turing (1912–1954)**  
(Logical and boundary-pushing, as above.) He admired curiosity about machines  
and avoided conservative views.  
_Contribution:_ Turing formalized the concept of computation and proposed the  
universal Turing machine.

**Paul Erdős (1913–1996)**  
Restless and eccentric, Erdős loved endless collaboration and disliked  
territoriality.  
_Contribution:_ Erdős published more papers than any other mathematician and  
is celebrated for his collaborative spirit.

---

### Example Gale–Shapley Run (Mathematicians Propose)

**Round 1**

- Gauss proposes to Einstein (accepted).
- Noether proposes to Curie (accepted).
- Turing proposes to Einstein (Einstein prefers Noether to Gauss, but Gauss is  
  better than Turing → Einstein keeps Gauss, rejects Turing).
- Euler proposes to Newton (accepted).

**Round 2**

- Turing, rejected by Einstein, proposes to Feynman (accepted).

**Final Matching (Mathematicians propose)**

- Gauss ↔ Einstein
- Noether ↔ Curie
- Euler ↔ Newton
- Turing ↔ Feynman

This outcome is **mathematician-optimal**. Repeat with physicists proposing to  
see how the matches change.

---

## Discussion (20 minutes)
