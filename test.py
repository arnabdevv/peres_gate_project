from qiskit_peres_gate import author
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.peres(0, 1, 2)
print(qc.draw())
print(qc.decompose().draw())
author()
