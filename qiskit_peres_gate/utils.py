"""Utility functions for creating and using the Peres gate."""

from __future__ import annotations

from qiskit.circuit import Gate, QuantumCircuit


def create_peres_gate() -> Gate:
    """
    Creates a Peres gate as a Qiskit Gate object.

    The Peres gate is a 3-qubit gate that performs the following transformation
    on the computational basis states:
    P|a,b,c> = |a, a XOR b, (a AND b) XOR c>

    This gate is notable for being a universal reversible classical gate.
    It is implemented by decomposing it into a Toffoli (CCX) gate and a
    subsequent CNOT (CX) gate.

    Returns:
        Gate: A Qiskit Gate object representing the 3-qubit Peres gate.
    """
    # A quantum circuit is created to define the Peres gate's internal operations.
    peres_circ = QuantumCircuit(3, name="Peres")

    # The decomposition of the Peres gate:
    # 1. A Toffoli gate (CCX) with qubits 0 and 1 as controls and qubit 2 as target.
    #    This implements the (a AND b) XOR c part for the third qubit.
    peres_circ.ccx(0, 1, 2)

    # 2. A CNOT gate (CX) with qubit 0 as control and qubit 1 as target.
    #    This implements the a XOR b part for the second qubit.
    peres_circ.cx(0, 1)

    # The circuit is converted into a reusable Gate object.
    peres_gate = peres_circ.to_gate()
    return peres_gate


def add_peres_gate(
    circuit: QuantumCircuit, control1: int, control2_target: int, target: int
):
    """
    Appends a Peres gate to an existing QuantumCircuit.

    This function provides a convenient way to add the Peres gate to a circuit,
    mapping it to the specified qubits.

    Args:
        circuit: The QuantumCircuit to which the gate will be added.
        control1: The index of the qubit corresponding to 'a' in the Peres
                  gate logic (P|a,b,c>).
        control2_target: The index of the qubit corresponding to 'b' in the
                         Peres gate logic.
        target: The index of the qubit corresponding to 'c' in the Peres
                gate logic.
    """
    peres_gate = create_peres_gate()
    circuit.append(peres_gate, [control1, control2_target, target])


def author():
    print("Arnab Dinda")
