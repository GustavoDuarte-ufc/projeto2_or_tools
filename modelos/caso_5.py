# modelos/caso_5.py
from ortools.linear_solver import pywraplp

def caso_5(
    solver=None,
    veludo_devolvivel=True,
    aumento_custo_lã_blazer=0.0,
    acetato_extra=0.0,
    venda_sobras_novembro=False,
    mostrar=True
):
    if solver is None:
        # SCIP é obrigatório aqui para processar variáveis inteiras e binárias (MIP)
        solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Erro: Solver não pôde ser inicializado.")
        return None

    # ======================================================
    # VARIÁVEIS DE DECISÃO (Seus produtos mantidos)
    # ======================================================
    calca_la = solver.IntVar(0, solver.infinity(), 'calca_la')
    sueter_cashmere = solver.IntVar(0, solver.infinity(), 'sueter_cashmere')
    blusa_seda = solver.IntVar(0, solver.infinity(), 'blusa_seda')
    camisole_seda = solver.IntVar(0, solver.infinity(), 'camisole_seda')
    saia_social = solver.IntVar(0, solver.infinity(), 'saia_social')
    blazer_la = solver.IntVar(0, solver.infinity(), 'blazer_la')
    calca_veludo = solver.IntVar(0, solver.infinity(), 'calca_veludo')
    sueter_algodao = solver.IntVar(0, solver.infinity(), 'sueter_algodao')
    minissaia_algodao = solver.IntVar(0, solver.infinity(), 'minissaia_algodao')
    blusa_botoes = solver.IntVar(0, solver.infinity(), 'blusa_botoes')

    # Camisa de Veludo + Variável Binária para o Custo Fixo (Item 1 & 2)
    camisa_veludo = solver.IntVar(0, solver.infinity(), 'camisa_veludo')
    produzir_veludo = solver.IntVar(0, 1, 'produzir_veludo')  # 1 se produzir, 0 se não

    # Lógica do Custo Fixo (Big-M): Se produzir_veludo for 0, camisa_veludo será 0
    M = 100000
    solver.Add(camisa_veludo <= M * produzir_veludo)

    # ======================================================
    # MATÉRIAS-PRIMAS (Com injeção do Item 6)
    # ======================================================
    disp = {
        'la': 45000.0,
        'acetato': 28000.0 + acetato_extra,
        'cashmere': 9000.0,
        'seda': 18000.0,
        'rayon': 30000.0,
        'veludo': 20000.0,
        'algodao': 30000.0
    }

    # ======================================================
    # RESTRIÇÕES ORIGINAIS
    # ======================================================
    solver.Add(3 * calca_la + 2.5 * blazer_la <= disp['la'])
    solver.Add(2 * calca_la + 1.5 * blazer_la <= disp['acetato'])
    solver.Add(1.5 * sueter_cashmere <= disp['cashmere'])
    solver.Add(1.5 * blusa_seda + 0.5 * camisole_seda <= disp['seda'])
    solver.Add(2 * saia_social + 1.5 * blusa_botoes <= disp['rayon'])
    solver.Add(3 * calca_veludo + 1.5 * camisa_veludo <= disp['veludo'])
    solver.Add(1.5 * sueter_algodao + 0.5 * minissaia_algodao <= disp['algodao'])
    
    # Sobras/Reaproveitamentos
    solver.Add(0.5 * camisole_seda <= 0.375 * blusa_seda)
    solver.Add(0.5 * minissaia_algodao <= 0.375 * sueter_algodao)

    # ======================================================
    # FUNÇÃO OBJETIVO DINÂMICA
    # ======================================================
    lucro_blazer = 154.75 - aumento_custo_lã_blazer  # Item 5: -$80 se ativado

    lucros_unitarios = {
        calca_la: 110.0,
        sueter_cashmere: 210.0,
        blusa_seda: 60.5,
        camisole_seda: 53.5,
        saia_social: 145.5,
        blazer_la: lucro_blazer,
        calca_veludo: 135.0,
        sueter_algodao: 66.25,
        minissaia_algodao: 33.75,
        blusa_botoes: 26.625
    }

    # Lucro Operacional Base (Somatório dos produtos comuns)
    objetivo = sum(lucro * var for var, lucro in lucros_unitarios.items())

    # Item 1 & 2: Lucro unitário de $22 e Custo Fixo de $500.000 se produzir_veludo for ativado
    objetivo += (22.0 * camisa_veludo) - (500000.0 * produzir_veludo)

    # Item 7: Venda de sobras de Lã por 60% do valor (Exemplo de aplicação prática da regra)
    if venda_sobras_novembro:
        la_restante = disp['la'] - (3 * calca_la + 2.5 * blazer_la)
        objetivo += 15.0 * la_restante  # Valor residual fictício parametrizado para o Item 7

    solver.Maximize(objetivo)
    status = solver.Solve()

    # ======================================================
    # EXIBIÇÃO RESULTADOS
    # ======================================================
    if status == pywraplp.Solver.OPTIMAL:
        if mostrar:
            custo_fixo_corporativo = 860000 + (3 * 2700000)
            lucro_operacional = solver.Objective().Value()
            
            # Ajuste de caixa para o Item 3 (Custo Afundado / Sunk Cost)
            # Se o veludo não é devolvível e NÃO produzimos, o prejuízo do tecido comprado deve ser abatido
            if not veludo_devolvivel and camisa_veludo.solution_value() == 0:
                lucro_operacional -= 50000.0  # Simulação do custo do veludo perdido

            lucro_final = lucro_operacional - custo_fixo_corporativo

            print('\n========== SOLUÇÃO ÓTIMA DETECTADA ==========')
            for var in lucros_unitarios.keys():
                if var.solution_value() > 0:
                    print(f' • {var.name():<18}: {int(var.solution_value())} unidades')
            
            # Print específico da camisa de veludo
            print(f' • camisa_veludo     : {int(camisa_veludo.solution_value())} unidades')
            print('---------------------------------------------')
            print(f' Decisão Camisa Veludo: {"PRODUZIR" if camisa_veludo.solution_value() > 0 else "NÃO PRODUZIR"}')
            print(f' Lucro Operacional    : ${lucro_operacional:,.2f}')
            print(f' Lucro Líquido Final  : ${lucro_final:,.2f}')
            print('=============================================\n')
        return solver.Objective().Value()
    else:
        print('Nenhuma solução ótima encontrada.')
        return None