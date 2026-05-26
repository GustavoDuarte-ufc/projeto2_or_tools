from ortools.linear_solver import pywraplp

def resolver_modelo_core(usar_inteiro=False, eliminar_custo=None):
    # Inicialização dos dados estáveis da imagem
    areas = [1, 2, 3, 4, 5, 6]
    escolas = [1, 2, 3]
    series = [0, 1, 2] # Representa 6º, 7º, 8º
    estudantes_por_area = [450, 600, 550, 350, 500, 450]
    
    proporcao = [
        [0.32, 0.38, 0.30],
        [0.37, 0.28, 0.35],
        [0.30, 0.32, 0.38],
        [0.28, 0.40, 0.32],
        [0.39, 0.34, 0.27],
        [0.34, 0.28, 0.38]
    ]
    
    custos_base = [
        [300, 0, 700],
        ['Inviavel', 400, 500],
        [600, 300, 200],
        [200, 500, 'Inviavel'],
        [0, 'Inviavel', 400],
        [500, 300, 0]
    ]
    
    capacidade = [900, 1100, 1000]

    # Aplicando alterações dinâmicas de remoção de custos (itens 5 e 6)
    for i in range(6):
        for j in range(3):
            if custos_base[i][j] == eliminar_custo:
                custos_base[i][j] = 0

    # Configuração de tipo de solver
    if usar_inteiro:
        solver = pywraplp.Solver.CreateSolver('SCIP')
    else:
        solver = pywraplp.Solver.CreateSolver('GLOP')

    x = {}
    for i in range(6):
        for j in range(3):
            if custos_base[i][j] == 'Inviavel':
                x[(i, j)] = solver.NumVar(0.0, 0.0, f'x_{i}_{j}')
            elif usar_inteiro:
                x[(i, j)] = solver.IntVar(0.0, float(estudantes_por_area[i]), f'x_{i}_{j}')
            else:
                x[(i, j)] = solver.NumVar(0.0, float(estudantes_por_area[i]), f'x_{i}_{j}')

    # Se for alocação exclusiva por área (MIP - Item 4)
    if usar_inteiro:
        y = {}
        for i in range(6):
            for j in range(3):
                y[(i, j)] = solver.IntVar(0, 1, f'y_{i}_{j}')
                solver.Add(x[(i, j)] <= estudantes_por_area[i] * y[(i, j)])
        for i in range(6):
            solver.Add(sum(y[(i, j)] for j in range(3)) == 1)

    # Restrições de Demanda
    for i in range(6):
        solver.Add(sum(x[(i, j)] for j in range(3)) == estudantes_por_area[i])

    # Restrições de Capacidade
    for j in range(3):
        solver.Add(sum(x[(i, j)] for i in range(6)) <= capacidade[j])

    # Restrições de Proporção por Série
    for j in range(3):
        for k in range(3):
            total_serie = sum(proporcao[i][k] * x[(i, j)] for i in range(6))
            total_escola = sum(x[(i, j)] for i in range(6))
            solver.Add(total_serie >= 0.30 * total_escola)
            solver.Add(total_serie <= 0.36 * total_escola)

    # Função Objetivo
    objetivo = []
    for i in range(6):
        for j in range(3):
            if custos_base[i][j] != 'Inviavel':
                objetivo.append(custos_base[i][j] * x[(i, j)])
    solver.Minimize(solver.Sum(objetivo))

    status = solver.Solve()
    return status, solver, x

# Função de execução direta do Cenário Base (Item 2 e 3)
def cenario_base_caso_7():
    status, solver, x = resolver_modelo_core(usar_inteiro=False)
    if status == pywraplp.Solver.OPTIMAL:
        print("\n=== CENÁRIO BASE OPTIMAL (ITENS 2 E 3) ===")
        print(f"Custo Mínimo de Transporte: ${solver.Objective().Value():,.2f}")
        for k, v in x.items():
            if v.solution_value() > 0:
                print(f" Área {k[0]+1} -> Escola {k[1]+1}: {v.solution_value():.1f} alunos")
    else:
        print("Inviável.")