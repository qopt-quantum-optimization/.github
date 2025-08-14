Circuit Compilation
===================

After designing the ansatz, the next step is to compile it for execution on a quantum device.  
Quantum devices are highly sensitive to noise, which increases with the number of qubits used and the overall circuit depth.  
Therefore, it is crucial to compile the ansatz into an equivalent form that is more hardware-efficient and less error-prone.

1. **QuClear**

   For logical ansatze, we have the **QuClear** framework :cite:`liu2025quclear`, which introduces two key techniques:

   - **Clifford Extraction**: This process identifies and extracts Clifford subcircuits from the original circuit, moving them toward the end of the circuit while simultaneously optimizing gate sequences.
   - **Clifford Absorption**: Since Clifford circuits are classically simulatable, this step absorbs the extracted Clifford subcircuits and processes them classically, reducing the quantum overhead.

   This approach significantly reduces the number of CNOT gates and the overall entangling depth, making the circuit more suitable for execution on NISQ (Noisy Intermediate-Scale Quantum) devices.

2. **HOPPS**

   We also support **HOPPS** (Hardware-Aware Optimal Phase Polynomial Synthesis), which focuses on optimally compiling QAOA ansatze under hardware constraints.  
   Using a SAT-based synthesis approach, HOPPS produces CNOT-optimal and depth-optimal circuits that respect the device's qubit connectivity.

   This method not only improves the physical realizability of QAOA circuits but also serves as a benchmark for evaluating mapping algorithms and guiding further circuit optimizations.
