import qiskit_peres_gate  # noqa: F401

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def expected_peres(a: int, b: int, c: int):
    """Classical Peres gate truth table."""
    P = a
    Q = a ^ b
    R = (a & b) ^ c
    return P, Q, R


def run_truth_table_test():
    sim = AerSimulator()

    print("a b c | P Q R | expected | status")
    print("----------------------------------")

    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):

                # Build circuit
                qc = QuantumCircuit(3, 3)

                # Prepare input |a b c>
                if a:
                    qc.x(0)
                if b:
                    qc.x(1)
                if c:
                    qc.x(2)

                # Apply Peres gate (from your library)
                qc.peres(0, 1, 2)

                # Measure
                qc.measure([0, 1, 2], [0, 1, 2])

                # Transpile for Aer (MANDATORY)
                tqc = transpile(qc, sim)

                # Execute
                result = sim.run(tqc, shots=1).result()
                bitstring = list(result.get_counts().keys())[0]

                # Qiskit returns bits MSB→LSB, reverse to match qubit order
                Pm, Qm, Rm = map(int, bitstring[::-1])

                Pe, Qe, Re = expected_peres(a, b, c)

                status = "OK" if (Pm, Qm, Rm) == (Pe, Qe, Re) else "FAIL"

                print(
                    f"{a} {b} {c} | "
                    f"{Pm} {Qm} {Rm} | "
                    f"{Pe} {Qe} {Re} | "
                    f"{status}"
                )

                # Hard failure for CI / correctness
                assert (Pm, Qm, Rm) == (
                    Pe,
                    Qe,
                    Re,
                ), f"Peres gate failed for input ({a}, {b}, {c})"


if __name__ == "__main__":
    run_truth_table_test()
