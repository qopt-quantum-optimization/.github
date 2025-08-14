Ansatz Design
=============

Once the Hamiltonian for the optimization problem is defined, the next step is to design an appropriate **ansatz** — a parameterized quantum circuit tailored to the problem.

1. **Dynamic Quantum Variational Ansatz (DQVA)**

   For constrained quantum approximate optimization, we have the **Dynamic Quantum Variational Ansatz (DQVA)** :cite:`saleem2023approaches`, which is designed to maximize the utilization of a fixed allocation of available quantum resources.

2. **Quantum Logical Search Ansatz**
   
   We also have the **Quantum Logical Search Ansatz** and the algorithm, as described in :cite:`tomesh2022quantum`, which solving complex problems by decomposing them into smaller, local subproblems.  
   The Quantum Logical Search selects subgraphs (neighborhoods) whose sizes are compatible with the quantum hardware’s qubit limitations.  
   By iteratively solving these local subproblems and integrating their solutions, a global solution can be efficiently constructed.
