# preference-agent
Design and build a knowledge-based intelligent system
to solve a preference problem via collecting user preferences and reasoning about them.

The system should allow reading in these data
from files. The three components of a preference problem are the following:

1. Attributes: in this project all attributes are binary.

2. Hard constraints (H): represented as propositional formulas in the Conjunctional Normal
Form (CNF).

3. Preference theory (T): your program should support two preference logics of penalty
logic and qualitative choice logic. Formulas involved in the preference theories (i.e., the
φ’s and the ψ’s) are of CNF as well.

The system should support the following tasks:

1. Encoding: encode all objects using binary codes.

2. Feasibility Checking: decide whether there are feasible objects w.r.t H, that is, whether
there are models of H that are truth assignments making H true.

3. Show the Table: present the table to show all feasible objects w.r.t H and for each one
show the penalty or satisfaction degree values across all preference rules.

4. Exemplification: generate, if possible, two random feasible objects, and show the
preference between the two (strict preference, equivalence, or incomparison) w.r.t T

5. Omni-optimization: find all optimal feasible objects w.r.t T
