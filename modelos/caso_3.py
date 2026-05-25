# Problema de reducão de custos da cafeteria
from ortools.linear_solver import pywraplp

def caso_3(
        solver=pywraplp.Solver.CreateSolver('SCIP'), 
        ingredientes=['batata', 'vagem'], 
        tabela_nutricional={'batata': {'proteina': 1.5, 'ferro': 0.3, 'vitamina_c': 12}, 'vagem': {'proteina': 5.67, 'ferro': 3.402, 'vitamina_c': 28.35}}, 
        custo_por_ingrediente = {
            'batata': 0.4,
            'vagem': 1
        },
        proteina_minima=180,
        custo_vagem=1,
        ferro_minimo=80,
        vitamina_c_minima=1050,
        razao_batata=6,
        razao_vagem=5,
        producao_minima_kg=10,
        usar_feijao_lima=False,
        validar_nutricao=False,
        mostrar=True):
    
    # 1. Criar o solver
    if not solver:
        print("Could not create solver GLOP") 

    if usar_feijao_lima:

        ingredientes = ['batata', 'feijao_lima']

        tabela_nutricional['feijao_lima'] = {
            'proteina': 22.68,
            'ferro': 6.804,
            'vitamina_c': 0
        }

        custo_por_ingrediente['feijao_lima'] = 0.60

    else:

        custo_por_ingrediente['vagem'] = custo_vagem

    # 2. Variáveis de decisão
    quantidade_por_ingrediente = {}

    # Variáveis de decisão para cada ingrediente
    for ingrediente in ingredientes:

        quantidade_por_ingrediente[ingrediente] = solver.NumVar(0, solver.infinity(), f'quantidade_{ingrediente}')

    # 3. Tabela nutricional(Proteina, Ferro e Vitamina C)

    # Converter tabela nutricional para a mesma unidade de medida (g por 453.6g) para ambos os ingredientes
    
    tabela_convertida = {}

    for ingrediente in ingredientes:

        tabela_convertida[ingrediente] = {}

    # Batata -> por libra

    tabela_convertida['batata']['proteina'] = (
        tabela_nutricional['batata']['proteina'] * (453.6 / 100)
    )

    tabela_convertida['batata']['ferro'] = (
        tabela_nutricional['batata']['ferro'] * (453.6 / 100)
    )

    tabela_convertida['batata']['vitamina_c'] = (
        tabela_nutricional['batata']['vitamina_c'] * (453.6 / 100)
    )

    ingrediente_secundario = ingredientes[1]

    tabela_convertida[ingrediente_secundario]['proteina'] = (
        tabela_nutricional[ingrediente_secundario]['proteina'] / 0.625
    )

    tabela_convertida[ingrediente_secundario]['ferro'] = (
        tabela_nutricional[ingrediente_secundario]['ferro'] / 0.625
    )

    tabela_convertida[ingrediente_secundario]['vitamina_c'] = (
        tabela_nutricional[ingrediente_secundario]['vitamina_c'] / 0.625
    )
    

    # 4. Restrições
    solver.Add(

        solver.Sum(

            tabela_convertida[ingrediente]['proteina']
            * quantidade_por_ingrediente[ingrediente]

            for ingrediente in ingredientes

        ) >= proteina_minima
    )

    solver.Add(

        solver.Sum(

            tabela_convertida[ingrediente]['ferro']
            * quantidade_por_ingrediente[ingrediente]

            for ingrediente in ingredientes

        ) >= ferro_minimo
    )

    solver.Add(

        solver.Sum(

            tabela_convertida[ingrediente]['vitamina_c']
            * quantidade_por_ingrediente[ingrediente]

            for ingrediente in ingredientes

        ) >= vitamina_c_minima
    )

    # ======================================================
    # RESTRIÇÃO DE SABOR
    # ======================================================

    ingrediente_secundario = ingredientes[1]

    solver.Add(

        razao_vagem *
        quantidade_por_ingrediente['batata']

        >=

        razao_batata *
        quantidade_por_ingrediente[ingrediente_secundario]
    )

    producao_minima_lb = producao_minima_kg / 0.4536

    solver.Add(

        solver.Sum(

            quantidade_por_ingrediente[ingrediente]

            for ingrediente in ingredientes

        ) >= producao_minima_lb
    )

    solver.Minimize(solver.Sum(custo_por_ingrediente[ingrediente] * quantidade_por_ingrediente[ingrediente] for ingrediente in ingredientes))

    # 6. Resolver o problema
    status = solver.Solve()

    custo_total = 0

    if status == pywraplp.Solver.OPTIMAL:

        custo_total = solver.Objective().Value()

        if mostrar:

            print('\nSolução ótima encontrada:\n')

            for ingrediente in ingredientes:

                valor_lb = (
                    quantidade_por_ingrediente[ingrediente]
                    .solution_value()
                )

                valor_kg = valor_lb * 0.4536

                custo = (
                    custo_por_ingrediente[ingrediente]
                    * valor_lb
                )

                print(f'{ingrediente.upper()}')

                print(f' - Quantidade: {valor_lb:.2f} lb')

                print(f' - Quantidade: {valor_kg:.2f} kg')

                print(f' - Custo: R$ {custo:.2f}\n')

            print(f'Custo total: R$ {custo_total:.2f}')

            # ==============================================
            # VALIDAÇÃO NUTRICIONAL
            # ==============================================

            if validar_nutricao:

                print("\nVALIDAÇÃO NUTRICIONAL")
                print("-" * 50)

                for nutriente in [
                    'proteina',
                    'ferro',
                    'vitamina_c'
                ]:

                    total = sum(

                        tabela_convertida[ingrediente][nutriente]
                        * quantidade_por_ingrediente[ingrediente]
                        .solution_value()

                        for ingrediente in ingredientes
                    )

                    print(
                        f'{nutriente.capitalize()}: '
                        f'{total:.2f}'
                    )

    else:

        print('A solução ótima não foi encontrada.')

    return custo_total