from qiskit.circuit import Gate, QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import CCXGate, CXGate
from .utils import author


class PeresGate(Gate):
    """
    The Peres Gate (New Toffoli Gate).
    A 3-qubit reversible gate where:
    P = A
    Q = A ⊕ B
    R = (A . B) ⊕ C
    """

    def __init__(self, label=None):
        super().__init__(name="peres", num_qubits=3, params=[], label=label)

    def _define(self):
        """
        Defines the decomposition of the Peres gate.
        Peres = Toffoli(0,1,2) + CNOT(0,1)
        """
        qc = QuantumCircuit(3, name=self.name)

        # 1. Apply Toffoli (CCX)
        qc.append(CCXGate(), [0, 1, 2])

        # 2. Apply CNOT (CX)
        qc.append(CXGate(), [0, 1])

        self.definition = qc

    def inverse(self):
        """
        Returns the inverse Peres gate.
        Note: The Peres gate is NOT self-adjoint.
        Inverse Peres = CNOT(0,1) + Toffoli(0,1,2)
        """
        inv_qc = QuantumCircuit(3, name="peres_dg")
        inv_qc.append(CXGate(), [0, 1])
        inv_qc.append(CCXGate(), [0, 1, 2])
        return inv_qc.to_gate()


def peres(self, qubit_a, qubit_b, qubit_c):
    """
    Extension method to allow: circuit.peres(0, 1, 2)
    """
    return self.append(PeresGate(), [qubit_a, qubit_b, qubit_c])


# This allows users to call 'circuit.peres()' directly after importing your library
QuantumCircuit.peres = peres
