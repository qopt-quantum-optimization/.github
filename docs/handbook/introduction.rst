Introduction
============

Quantum computing is a rapidly advancing field with promising applications across cryptography, quantum chemistry, optimization, and machine learning.  
A variety of quantum hardware platforms — including superconducting qubits, neutral atoms, trapped ions, and photonic systems — are actively being developed by leading companies.  
As these technologies continue to mature, real-world applications are becoming increasingly viable. For example, IBM’s 2026 technology roadmap envisions demonstrating quantum advantage by integrating quantum computing with high-performance computing (HPC).  

Among these applications, **quantum optimization** stands out as a particularly promising area :cite:`abbas2024challenges`, aiming to solve classical optimization problems more efficiently using quantum devices.
.. Common approaches to quantum optimization include variational quantum algorithms (VQAs) :cite:`cerezo2021variational` , quantum annealing :cite:`finnila1994quantum`, and Grover’s search algorithm :cite:`grover1997quantum`.
VQAs are the most widely used for quantum optimization. They are applicable to a broad range of problems, including quantum chemistry, machine learning, and combinatorial optimization. 
The workflow of VQAs typically involves the following steps:

1. **Problem Encoding**: Transform the classical optimization problem into a Hamiltonian.
2. **Ansatz Design**: Construct a parameterized quantum circuit (ansatz) that approximates the ground state of the Hamiltonian.
3. **Circuit Compilation**: Compile the ansatz circuit to the target quantum hardware.
4. **Classical Optimization**: Use classical optimization algorithms to update the ansatz parameters based on measurement outcomes.

The **Argonne Quantum Optimization Toolkit** offers a comprehensive and modular framework for solving optimization problems using these quantum algorithms.  
It supports all stages of the quantum optimization workflow. We also have application studies of quantum optimization.

All tools are publicly accessible through our platform: `<link>`_.

In the following sections, we provide a brief overview of each component and the tools available.