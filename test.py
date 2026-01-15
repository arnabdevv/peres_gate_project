from qiskit import QuantumCircuit
import peres_gate  # Your library name

qc = QuantumCircuit(3)
# Because of the monkey-patching in __init__.py, this works:
qc.peres(0, 1, 2)

print("Circuit with Peres Gate:")
print(qc.draw())

print("\nDecomposed into basis gates:")
print(qc.decompose().draw())
