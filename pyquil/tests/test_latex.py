from pyquil.quil import Program
from pyquil.gates import X, CZ, SWAP, MEASURE, CNOT
from pyquil.latex_generation import to_latex


def test_to_latex():
    qubit0 = 0
    qubit1 = 1
    qubit2 = 2
    p = Program()
    p.inst(X(qubit0)).inst(('Y', qubit0)).inst(CZ(qubit0, qubit1)).inst(SWAP(qubit0, qubit1)).inst(("MEASURE", qubit0)).inst(CNOT(qubit2, qubit0))
    _ = to_latex(p)
