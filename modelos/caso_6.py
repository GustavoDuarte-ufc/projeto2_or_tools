# modelos/caso_6.py
from ortools.linear_solver import pywraplp

def caso_6(
    solver=None,
    minimo_por_celula=0,
    maximo_jovens=None,
    maximo_alto_uso=None,
    novos_custos_regionais=False,
    percentuais_fixos=False,
    mostrar=True
):
    if solver is None:
        solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Não foi possível criar o solver.")
        return None

    regioes = ['vale silicio', 'grandes cidades', 'pequenas cidades']
    grupo_de_idades = ['18-25', '26-40', '41-50', '50+']
    entrevistados_totais = 2000

    # Variáveis de Decisão
    relacao_regiao_idade = {}
    for regiao in regioes:
        for idade in grupo_de_idades:
            relacao_regiao_idade[regiao, idade] = solver.IntVar(
                0, solver.infinity(), f'relacao_{regiao}_{idade}'
            )

    # ------------------------------------------------------
    # DEFINIÇÃO DE CUSTOS (Base vs Atualizações da Imagem)
    # ------------------------------------------------------
    if novos_custos_regionais:
        # Tabela 2 da imagem: "Region survey cost per person" (Custos fixos por região)
        custos = {
            ('vale silicio', idx): 6.50 for idx in grupo_de_idades
        }
        custos.update({('grandes cidades', idx): 6.75 for idx in grupo_de_idades})
        custos.update({('pequenas cidades', idx): 7.00 for idx in grupo_de_idades})
    else:
        # Tabela original do cenário base
        custos = {
            ('vale silicio', '18-25'): 4.75, ('vale silicio', '26-40'): 6.50,
            ('vale silicio', '41-50'): 6.50, ('vale silicio', '50+'): 5.00,
            ('grandes cidades', '18-25'): 5.25, ('grandes cidades', '26-40'): 5.75,
            ('grandes cidades', '41-50'): 6.25, ('grandes cidades', '50+'): 6.25,
            ('pequenas cidades', '18-25'): 6.50, ('pequenas cidades', '26-40'): 7.50,
            ('pequenas cidades', '41-50'): 7.50, ('pequenas cidades', '50+'): 7.25
        }

    # ------------------------------------------------------
    # RESTRIÇÕES
    # ------------------------------------------------------
    # Fechamento amostral total
    solver.Add(sum(relacao_regiao_idade[r, i] for r in regioes for i in grupo_de_idades) == entrevistados_totais)

    # Item 3: Exigência adicional de ao menos X pessoas em cada combinação
    if minimo_por_celula > 0:
        for r in regioes:
            for i in grupo_de_idades:
                solver.Add(relacao_regiao_idade[r, i] >= minimo_por_celula)

    # Regras de Cotas (Fixas para o Item 6 vs Mínimas para o Base)
    if percentuais_fixos:
        # Tabela 3 da imagem: "Population percentage of people surveyed"
        # Etárias Fixas
        solver.Add(sum(relacao_regiao_idade[r, '18-25'] for r in regioes) == 0.25 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade[r, '26-40'] for r in regioes) == 0.35 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade[r, '41-50'] for r in regioes) == 0.20 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade[r, '50+'] for r in regioes) == 0.20 * entrevistados_totais)
        # Regionais Fixas
        solver.Add(sum(relacao_regiao_idade['vale silicio', i] for i in grupo_de_idades) == 0.20 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade['grandes cidades', i] for i in grupo_de_idades) == 0.50 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade['pequenas cidades', i] for i in grupo_de_idades) == 0.30 * entrevistados_totais)
    else:
        # Mínimas padrão (Base)
        solver.Add(sum(relacao_regiao_idade[r, '18-25'] for r in regioes) >= 0.20 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade[r, '26-40'] for r in regioes) >= 0.275 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade[r, '41-50'] for r in regioes) >= 0.15 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade[r, '50+'] for r in regioes) >= 0.15 * entrevistados_totais)

        solver.Add(sum(relacao_regiao_idade['vale silicio', i] for i in grupo_de_idades) >= 0.15 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade['grandes cidades', i] for i in grupo_de_idades) >= 0.35 * entrevistados_totais)
        solver.Add(sum(relacao_regiao_idade['pequenas cidades', i] for i in grupo_de_idades) >= 0.20 * entrevistados_totais)

    # Item 4: Limites Máximos (Cap)
    if maximo_jovens is not None:
        solver.Add(sum(relacao_regiao_idade[r, '18-25'] for r in regioes) <= maximo_jovens)
    if maximo_alto_uso is not None:
        # Alto uso de internet = Vale do Silício
        solver.Add(sum(relacao_regiao_idade['vale silicio', i] for i in grupo_de_idades) <= maximo_alto_uso)

    # Função Objetivo: Minimizar Custos
    solver.Minimize(sum(custos[r, i] * relacao_regiao_idade[r, i] for r in regioes for i in grupo_de_idades))
    
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        custo_total = solver.Objective().Value()
        lance_bid = custo_total * 1.15  # Item 2: Margem de lucro de 15% sobre o custo
        
        if mostrar:
            print("\n" + "-" * 50)
            print(f" Custo Total Calculado : R$ {custo_total:,.2f}")
            print(f" Lance Sugerido (Bid)  : R$ {lance_bid:,.2f} (Lucro 15% incluso)")
            print("-" * 50)
        return custo_total
    else:
        if mostrar:
            print("\n❌ Nenhuma solução ótima encontrada para esta configuração.")
        return None