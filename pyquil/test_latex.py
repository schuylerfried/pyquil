import time
import random
import string

import numpy as np
from pyquil.gates import X, MEASURE, H
from pyquil.latex_generation import to_latex
from pyquil.quil import Program
from subprocess import Popen


WAIT_TIME = 3

p = Program()
p.inst(X(2))
# p.inst(X(2))
p.inst(("U", 0, 2))
p.inst(("U", 0, 1))
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
