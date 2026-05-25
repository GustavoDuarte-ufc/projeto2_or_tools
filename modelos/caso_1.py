# Problema de Transporte de Cadeiras Infantis
from ortools.linear_solver import pywraplp

def caso_1(
        solver=pywraplp.Solver.CreateSolver('SCIP'), 
        producao_maxima=[12, 17, 11], 
        distancia=[[800, 1300, 400, 700], [1100, 1400, 600, 1000], [600, 1200, 800, 900]]):
    
    # 1. Criar o solver
    if not solver:
        print("Could not create solver GLOP")

    # 2. Variáveis de decisão
    x = {}

    for i in range(3): # 3 Fábricas
        for j in range(4): # 4 Centros de Distribuição
            x[i, j] = solver.IntVar(0, solver.infinity(), f'x[{i},{j}]') # Conjunto de variáveis de transporte

    # Produção máxima de cada fábrica por mês
    producao_maxima = [12, 17, 11]

    # Distância em milhas entre as fábricas e os centros de distribuição
    distancia = [
        [800, 1300, 400, 700], # Distâncias da Fábrica 1 para os Centros de Distribuição
        [1100, 1400, 600, 1000], # Distâncias da Fábrica 2 para os Centros de Distribuição
        [600, 1200, 800, 900]  # Distâncias da Fábrica 3 para os Centros de Distribuição
    ]

    # Custos de transporte em milhas
    custo = {}

    for i in range(3):
        for j in range(4):
            custo[i, j] = 100 + distancia[i][j] * 0.5 # Custo de transporte é um valor fixo(100) mais 0.5 por milha

    # 3. Restrições

    # Restrições de oferta: limite de profução de cada fábrica
    for i in range(3):
        solver.Add(solver.Sum(x[i, j] for j in range(4)) <= producao_maxima[i])

    # Restrições de demanda: cada centro de distribuição deve receber exatamente 10 cadeiras
    for j in range(4):
        solver.Add(solver.Sum(x[i, j] for i in range(3)) == 10)

    # 4. Função objetivo
    solver.Minimize(solver.Sum(custo[i, j] * x[i, j] for i in range(3) for j in range(4)))

    # 5. Resolver o problema
    status = solver.Solve()

    # 6. Imprimir os resultados
    if status == pywraplp.Solver.OPTIMAL:
        print('Solução ótima encontrada:\n')
        for i in range(3):
            if any(x[i, j].solution_value() > 0 for j in range(4)):
                print(f'Fábrica {i + 1}:')
                for j in range(4):
                    if x[i, j].solution_value() > 0:
                        print(f'  Enviar {x[i, j].solution_value()} remessas para o Centro de Distribuição {j + 1}')
                        print(f'  - Custo de transporte: {custo[i, j] * x[i, j].solution_value()}\n')

        for i in range(3):
            print(f"Custo total de transporte da Fábrica {i + 1}: {sum(custo[i, j] * x[i, j].solution_value() for j in range(4))}")

        print(f'\nCusto total de transporte: {solver.Objective().Value()}')
    else:
        print('Nenhuma solução ótima encontrada.')