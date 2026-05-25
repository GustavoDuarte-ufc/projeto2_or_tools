# Problema de Planejamento de Qualidade Automotiva
from ortools.linear_solver import pywraplp

def caso_2(
        solver=pywraplp.Solver.CreateSolver('SCIP'),
        modelos=['Family Thrillseeker', 'Classy Cruiser'],
        horas_por_unidade={
            'Family Thrillseeker': 6,
            'Classy Cruiser': 10.5
        },
        lucro_por_unidade={
            'Family Thrillseeker': 3600,
            'Classy Cruiser': 5400
        },
        marketing=0,
        demanda_cruiser=3500,
        horas_totais=48000,
        mostrar=True,
        demanda_obrigatoria=False):
    
    # 1. Criar o solver
    if not solver:
        print("Could not create solver GLOP")

    # 2. Variáveis de decisão
    modelos = ['Family Thrillseeker', 'Classy Cruiser']
    unidades_por_modelo = {}

    # Variáveis de decisão para cada modelo
    unidades_por_modelo['Classy Cruiser'] = solver.IntVar(0, solver.infinity(), 'unidades_classy_cruiser')
    unidades_por_modelo['Family Thrillseeker'] = solver.IntVar(0, solver.infinity(), 'unidades_family_thrillseeker')

    # 3. Restrições

    # Restrições de demanda
    if demanda_obrigatoria:

        solver.Add(
            unidades_por_modelo['Classy Cruiser']
            == demanda_cruiser
        )

    else:

        solver.Add(
            unidades_por_modelo['Classy Cruiser']
            <= demanda_cruiser
        )

    # Restrições de capacidade total
    solver.Add(4*unidades_por_modelo['Family Thrillseeker'] + 4*unidades_por_modelo['Classy Cruiser'] <= 20000)

    # Restrições de horas de trabalho
    horas_por_unidade = {
        'Family Thrillseeker': 6,
        'Classy Cruiser': 10.5
    }

    solver.Add(solver.Sum(horas_por_unidade[modelo] * unidades_por_modelo[modelo] for modelo in modelos) <= horas_totais)

    # 4. Função objetivo: maximizar o lucro
    lucro_por_unidade = {
        'Family Thrillseeker': 3600,
        'Classy Cruiser': 5400
    }

    solver.Maximize(solver.Sum(lucro_por_unidade[modelo] * unidades_por_modelo[modelo] for modelo in modelos) - marketing)

    # 5. Resolver o problema
    status = solver.Solve()

    lucro_total = 0

    # 6. Imprimir os resultados
    if status == pywraplp.Solver.OPTIMAL:

        if mostrar:
            print('Solução ótima encontrada:\n')

        for modelo in modelos:

            if mostrar:
                print(
                    f'Unidades produzidas do modelo {modelo}: '
                    f'{unidades_por_modelo[modelo].solution_value()}'
                )

                print(
                    f'Lucro total do modelo {modelo}: '
                    f'R$ {lucro_por_unidade[modelo] * unidades_por_modelo[modelo].solution_value():.2f}\n'
                )

        lucro_total = solver.Objective().Value()

        if mostrar:
            print(f'Lucro total: R$ {lucro_total:.2f}')

    else:

        if mostrar:
            print("Nenhuma solução ótima encontrada.")

    return lucro_total