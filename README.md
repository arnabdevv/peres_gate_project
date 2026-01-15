# Qiskit Peres Gate Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Qiskit Version](https://img.shields.io/badge/Qiskit-1.0+-blueviolet)](https://qiskit.org/)

A lightweight Python library to integrate the **Peres Gate** (also known as the New Toffoli Gate) into Qiskit circuits. This gate is a fundamental component in reversible logic synthesis and quantum arithmetic.

## What is a Peres Gate?

The Peres Gate is a 3-qubit reversible gate. It is highly valued in quantum computing because it functions as an efficient **Half-Adder** with a lower Quantum Cost (QC=4) compared to the standard Toffoli-based implementation.

### Logic Transformation:

- $P = A$
- $Q = A \oplus B$
- $R = (A \cdot B) \oplus C$

## Installation

You can install this library locally for development:

```bash
git clone [https://github.com/arnabdevv/peres_gate_project.git](https://github.com/arnabdevv/peres_gate_project.git)
cd qiskit-peres-gate
pip install .
```
