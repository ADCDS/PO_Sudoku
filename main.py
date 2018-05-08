import read
from docplex.cp.model import CpoModel
from docplex.cp.config import context

context.solver.agent = 'local'
context.solver.local.execfile = '/home/a15001/cplex/cpoptimizer/bin/x86-64_linux/cpoptimizer'
from read import read_instance

matrix = read_instance()

mdl = CpoModel()

x = [[[0] * 9] * 9] * 9


for l in range(0, 8):
    for c in range(0, 8):
        for v in range(0, 8):
            x[l][c][v] = mdl.integer_var(0, 1)


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            mdl.add(x[i][j][matrix[i][j] - 1] == 1)


# Restrição de linha
for c in range(0, 8):
    for v in range(0, 8):
        expr = 0
        for l in range(0, 8):
            expr = expr + x[l][c][v]
        mdl.add(expr == 1)

# Restrição de coluna
for l in range(0, 8):
    for v in range(0, 8):
        expr = 0
        for c in range(0, 8):
            expr = expr + x[l][c][v]
        mdl.add(expr == 1)

# Restrição de coluna
for l in range(0, 8):
    for c in range(0, 8):
        expr = 0
        for v in range(0, 8):
            expr = expr + x[l][c][v]
        mdl.add(expr == 1)

# Restrição de quadrante
for aux_l in [0, 3, 6]:
    for aux_c in [0, 3, 6]:
        for v in range(0, 8):
            expr = 0
            for l in range(aux_l, aux_l + 2):
                for c in range(aux_c, aux_c + 2):
                    expr += x[l][c][v]
            mdl.add(expr == 1)

if mdl.solve():
    print("Solved")
else:
    print("Couldnt solve")
