# Quantum Password Generator

A password generator that uses quantum randomness via IBM's Qiskit framework to produce true-random passwords — replacing the pseudorandom number generators (PRNGs) used in classical approaches.

## How It Works

Classical password generators rely on PRNGs, which are deterministic algorithms seeded by system entropy. While practical, they are mathematically predictable given the seed.

This generator instead uses **quantum superposition and measurement collapse**:

1. A quantum circuit is constructed with one qubit per bit of randomness needed
2. A Hadamard gate places each qubit into superposition — equal probability of measuring 0 or 1
3. Upon measurement, each qubit collapses to a definite state, producing a truly random bitstring
4. The bitstring is mapped to characters from a pool of letters, digits, and symbols

Because the outcome is determined by quantum mechanics rather than a deterministic algorithm, the randomness is fundamentally non-reproducible.

## Stack

- Python
- [Qiskit](https://qiskit.org/) — quantum circuit construction
- [Qiskit Aer](https://github.com/Qiskit/qiskit-aer) — local quantum simulator
- Qiskit IBM Runtime — SamplerV2 for circuit execution

## Usage

```python
from password_gen import generate_password

print(generate_password(16))  # e.g. ZG.uACIPBeyD,z9h
```

## Notes

The generator runs on a **local Aer simulator**, which approximates ideal quantum behavior. For deployment-grade true randomness, the circuit could be submitted to a real IBM quantum device via IBM Quantum Platform.
