Classical Optimizer
===================

Running variational quantum algorithms (VQAs) requires a classical optimizer to update the parameters in the ansatz. 
These parameters are iteratively updated until convergence or until a predefined number of iterations is reached. 
The final solution is obtained from the ansatz under optimized parameters.

1. **ANATRAr**

   ANATRAr is a classical optimization algorithm specifically designed for VQAs on noisy quantum hardware.
   It employs minimum Frobenius norm models and preserves the geometry of the interpolation set to ensure robust convergence.

2. **SHOALS**

   SHOALS is a shot-adaptive stochastic optimization algorithm for VQAs that accounts for hardware-specific latencies, 
   such as shot acquisition times and circuit switching delays. 
   By emulating the dynamics of deterministic line-search optimization, SHOALS achieves improved worst-case iteration complexity.

