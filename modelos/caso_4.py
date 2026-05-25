# Problema Escala de operadores em central de atendimento

from ortools.linear_solver import pywraplp
import math


def caso_4(

    solver=pywraplp.Solver.CreateSolver('SCIP'),

    percentual_ingles=0.80,
    percentual_espanhol=0.20,

    limite_integral_13h=None,

    demanda_por_periodo=None,

    salario_por_periodo=None,

    mostrar=True
):

    # ======================================================
    # 1. CRIAR SOLVER
    # ======================================================

    if not solver:
        print("Solver não criado.")

    # ======================================================
    # 2. DADOS DO PROBLEMA
    # ======================================================
    if salario_por_periodo is None:

        salario_por_periodo = {

            '7-9': 2 * 10,
            '9-11': 2 * 10,
            '11-13': 2 * 10,
            '13-15': 2 * 10,
            '15-17': 2 * 10,
            '17-19': 2 * 12,
            '19-21': 2 * 12
        }

    periodos = [
        '7-9',
        '9-11',
        '11-13',
        '13-15',
        '15-17',
        '17-19',
        '19-21',
    ]

    horarios_integral = [7, 9, 11, 13]

    horarios_parcial = [15, 17]

    # ======================================================
    # DEMANDA PADRÃO
    # ======================================================

    if demanda_por_periodo is None:

        demanda_por_periodo = {

            '7-9': 40 * 2,
            '9-11': 85 * 2,
            '11-13': 70 * 2,
            '13-15': 95 * 2,
            '15-17': 80 * 2,
            '17-19': 35 * 2,
            '19-21': 10 * 2
        }

    # ======================================================
    # 3. VARIÁVEIS
    # ======================================================

    funcionarios = {

        'integral_ingles_tel': {},
        'integral_espanhol_tel': {},
        'integral_ingles_adm': {},
        'integral_espanhol_adm': {},
        'parcial': {}
    }

    # Integrais

    for horario in horarios_integral:

        funcionarios['integral_ingles_tel'][horario] = (

            solver.IntVar(
                0,
                solver.infinity(),
                f'integral_ingles_tel_{horario}'
            )
        )

        funcionarios['integral_espanhol_tel'][horario] = (

            solver.IntVar(
                0,
                solver.infinity(),
                f'integral_espanhol_tel_{horario}'
            )
        )

        funcionarios['integral_ingles_adm'][horario] = (

            solver.IntVar(
                0,
                solver.infinity(),
                f'integral_ingles_adm_{horario}'
            )
        )

        funcionarios['integral_espanhol_adm'][horario] = (

            solver.IntVar(
                0,
                solver.infinity(),
                f'integral_espanhol_adm_{horario}'
            )
        )

    # Parciais

    for horario in horarios_parcial:

        funcionarios['parcial'][horario] = (

            solver.IntVar(
                0,
                solver.infinity(),
                f'parcial_{horario}'
            )
        )

    # ======================================================
    # 4. OPERADORES NECESSÁRIOS
    # ======================================================

    operadores_necessarios = {}

    for periodo in periodos:

        demanda = demanda_por_periodo[periodo]

        operadores_necessarios[periodo] = (

            math.ceil(demanda / 12)
        )

    # ======================================================
    # 5. RESTRIÇÕES
    # ======================================================

    # ======================================================
    # 7h - 9h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_tel'][7]

        >=

        math.ceil(
            operadores_necessarios['7-9']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_tel'][7]

        >=

        math.ceil(
            operadores_necessarios['7-9']
            * percentual_espanhol
        )
    )

    # ======================================================
    # 9h - 11h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_tel'][9]
        +
        funcionarios['integral_ingles_adm'][7]

        >=

        math.ceil(
            operadores_necessarios['9-11']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_tel'][9]
        +
        funcionarios['integral_espanhol_adm'][7]

        >=

        math.ceil(
            operadores_necessarios['9-11']
            * percentual_espanhol
        )
    )

    # ======================================================
    # 11h - 13h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_tel'][11]
        +
        funcionarios['integral_ingles_adm'][9]
        +
        funcionarios['integral_ingles_tel'][7]

        >=

        math.ceil(
            operadores_necessarios['11-13']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_tel'][11]
        +
        funcionarios['integral_espanhol_adm'][9]
        +
        funcionarios['integral_espanhol_tel'][7]

        >=

        math.ceil(
            operadores_necessarios['11-13']
            * percentual_espanhol
        )
    )

    # ======================================================
    # 13h - 15h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_tel'][13]
        +
        funcionarios['integral_ingles_adm'][11]
        +
        funcionarios['integral_ingles_tel'][9]
        +
        funcionarios['integral_ingles_adm'][7]

        >=

        math.ceil(
            operadores_necessarios['13-15']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_adm'][13]
        +
        funcionarios['integral_espanhol_adm'][11]
        +
        funcionarios['integral_espanhol_tel'][9]
        +
        funcionarios['integral_espanhol_adm'][7]

        >=

        math.ceil(
            operadores_necessarios['13-15']
            * percentual_espanhol
        )
    )

    # ======================================================
    # 15h - 17h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_adm'][13]
        +
        funcionarios['integral_ingles_tel'][11]
        +
        funcionarios['integral_ingles_adm'][9]
        +
        funcionarios['parcial'][15]

        >=

        math.ceil(
            operadores_necessarios['15-17']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_adm'][13]
        +
        funcionarios['integral_espanhol_tel'][11]
        +
        funcionarios['integral_espanhol_adm'][9]

        >=

        math.ceil(
            operadores_necessarios['15-17']
            * percentual_espanhol
        )
    )

    # ======================================================
    # 17h - 19h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_tel'][13]
        +
        funcionarios['integral_ingles_adm'][11]
        +
        funcionarios['parcial'][17]

        >=

        math.ceil(
            operadores_necessarios['17-19']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_tel'][13]
        +
        funcionarios['integral_espanhol_adm'][11]

        >=

        math.ceil(
            operadores_necessarios['17-19']
            * percentual_espanhol
        )
    )

    # ======================================================
    # 19h - 21h
    # ======================================================

    solver.Add(

        funcionarios['integral_ingles_adm'][13]
        +
        funcionarios['parcial'][15]
        +
        funcionarios['parcial'][17]

        >=

        math.ceil(
            operadores_necessarios['19-21']
            * percentual_ingles
        )
    )

    solver.Add(

        funcionarios['integral_espanhol_adm'][13]
        +
        funcionarios['parcial'][15]

        >=

        math.ceil(
            operadores_necessarios['19-21']
            * percentual_espanhol
        )
    )

    # ======================================================
    # RESTRIÇÃO EXTRA
    # ======================================================

    if limite_integral_13h is not None:

        solver.Add(

            funcionarios['integral_ingles_tel'][13]
            +
            funcionarios['integral_espanhol_tel'][13]
            +
            funcionarios['integral_ingles_adm'][13]
            +
            funcionarios['integral_espanhol_adm'][13]

            <= limite_integral_13h
        )

    # ======================================================
    # 6. FUNÇÃO OBJETIVO
    # ======================================================

    total_funcionarios = solver.Sum(

        funcionarios[tipo][horario]

        for tipo in funcionarios
        for horario in funcionarios[tipo]
    )

    solver.Minimize(total_funcionarios)

    # ======================================================
    # 7. RESOLVER
    # ======================================================

    status = solver.Solve()

    # ======================================================
    # 8. RESULTADOS
    # ======================================================

    if status == pywraplp.Solver.OPTIMAL:

        total = total_funcionarios.solution_value()

        if mostrar:

            print("\n" + "=" * 60)
            print("SOLUÇÃO ÓTIMA")
            print("=" * 60)

            print(f"\nTotal de funcionários: {total}\n")

            for tipo, horarios in funcionarios.items():

                for horario, var in horarios.items():

                    if var.solution_value() > 0:

                        print(
                            f"{tipo}"
                            f" | Entrada: {horario}h"
                            f" | Quantidade: {var.solution_value()}"
                        )

        return total

    else:

        print("\nNenhuma solução ótima encontrada.")

        return None