# Method

The verifier constructs a two-expert Gaussian composition with exponents `[1, -0.5]`, evaluates the precision coefficient on 2,000 deterministic timesteps, and independently evaluates truncated normalizers with stable numerical quadrature. Endpoint positivity, intermediate negativity, and growth with the integration boundary are all required.

Negative control: the verifier tampers with the sign of the observed negative coefficient and requires the contract checker to reject it.
