from ortools.linear_solver import pywraplp

def caso_8():
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Variáveis
    x_vaca = solver.NumVar(30.0, 42.0, 'Total_Vacas')
    x_galinha = solver.NumVar(2000.0, 5000.0, 'Total_Galinhas')
    x_soja = solver.NumVar(0.0, solver.infinity(), 'Acres_Soja')
    x_milho = solver.NumVar(0.0, solver.infinity(), 'Acres_Milho')
    x_trigo = solver.NumVar(0.0, solver.infinity(), 'Acres_Trigo')
    h1 = solver.NumVar(0.0, solver.infinity(), 'Horas_S1')
    h2 = solver.NumVar(0.0, solver.infinity(), 'Horas_S2')

    # Restrições
    solver.Add(2.0 * x_vaca + x_soja + x_milho + x_trigo <= 640.0)
    solver.Add(1500.0 * (x_vaca - 30) + 3.0 * (x_galinha - 2000) <= 20000.0)
    solver.Add(x_milho >= 1.0 * x_vaca)
    solver.Add(x_trigo >= 0.05 * x_galinha)
    solver.Add(60.0 * x_vaca + 0.3 * x_galinha + 1.0 * x_soja + 0.9 * x_milho + 0.6 * x_trigo + h1 == 4000.0)
    solver.Add(60.0 * x_vaca + 0.3 * x_galinha + 1.4 * x_soja + 1.2 * x_milho + 0.7 * x_trigo + h2 == 4500.0)

    solver.Maximize(700.0 * x_vaca + 3.50 * x_galinha + 70.0 * x_soja + 60.0 * x_milho + 40.0 * x_trigo + 5.0 * h1 + 5.5 * h2 - 10750.0)
    
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print("\n>>> SOLUÇÃO DO CENÁRIO BASE (NUMÉRICA) <<<")
        print(f"Resultado Patrimonial Otimizado: ${solver.Objective().Value():,.2f}")
        print(f"Rebanho: {x_vaca.solution_value():.0f} Vacas e {x_galinha.solution_value():.0f} Galinhas")
        print(f"Uso do Solo: Soja: {x_soja.solution_value():.1f} ac | Milho: {x_milho.solution_value():.1f} ac | Trigo: {x_trigo.solution_value():.1f} ac")
        print(f"Trabalho Externo: Semestre 1: {h1.solution_value():.1f}h | Semestre 2: {h2.solution_value():.1f}h")