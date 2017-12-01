import time
import random
import string

import numpy as np
from pyquil.gates import X, MEASURE, H, Y, CZ
from pyquil.latex_generation import to_latex
from pyquil.quil import Program
from subprocess import Popen
from grove.amplification.grover import Grover

WAIT_TIME = 3

p = Grover().oracle_grover(Program().inst(CZ(0, 1)).inst(CZ(1, 2)).inst(CZ(2, 3)), [0, 1, 2, 3], 5)



# for _ in range(40):
#     p.inst((random.choice(string.ascii_letters), np.random.randint(10)))
# p.inst(("X", 500))
print(p)
latex = to_latex(p)
filename = "circuit.tex"
Popen(["touch", filename])

with open(filename, 'w') as fh:
    fh.write(latex)

Popen(['pdflatex', filename])
time.sleep(WAIT_TIME)

Popen(['xdg-open', 'circuit.pdf'])
