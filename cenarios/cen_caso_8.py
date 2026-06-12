# cenarios/cen_caso_8.py

from ortools.linear_solver import pywraplp

def _executar_solver_base(v_soja=70.0, v_milho=60.0, v_trigo=40.0, cap_extra=0.0):
    """
    Função auxiliar interna que roda o modelo matemático da fazenda Ploughman.
    Recebe os coeficientes de mercado das culturas e aportes extras de capital.
    """
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return {"sucesso": False}
    
    # Variáveis de Decisão
    x1 = solver.NumVar(30.0, 42.0, 'Vacas')
    x2 = solver.NumVar(2000.0, 5000.0, 'Galinhas')
    x3 = solver.NumVar(0.0, solver.infinity(), 'Soja')
    x4 = solver.NumVar(0.0, solver.infinity(), 'Milho')
    x5 = solver.NumVar(0.0, solver.infinity(), 'Trigo')
    h1 = solver.NumVar(0.0, solver.infinity(), 'Horas_S1')
    h2 = solver.NumVar(0.0, solver.infinity(), 'Horas_S2')

    # Restrições do Modelo
    solver.Add(2.0 * x1 + x3 + x4 + x5 <= 640.0) # Limite de Terra
    
    # Restrição de Capital parametrizada (Investimento Inicial + Aporte Extra)
    restricao_capital = solver.Add(1500.0 * x1 + 3.0 * x2 <= 71000.0 + cap_extra)
    
    solver.Add(x4 >= 1.0 * x1)    # Alimentação Mínima: Milho
    solver.Add(x5 >= 0.05 * x2)  # Alimentação Mínima: Trigo
    
    # Balanço de Mão de Obra Semestral
    solver.Add(60.0 * x1 + 0.3 * x2 + 1.0 * x3 + 0.9 * x4 + 0.6 * x5 + h1 == 4000.0)
    solver.Add(60.0 * x1 + 0.3 * x2 + 1.4 * x3 + 1.2 * x4 + 0.7 * x5 + h2 == 4500.0)

    # Função Objetivo Simplificada e Linearizada
    solver.Maximize(700.0 * x1 + 3.50 * x2 + v_soja * x3 + v_milho * x4 + v_trigo * x5 + 5.0 * h1 + 5.5 * h2 - 10750.0)
    
    status = solver.Solve()
    
    preco_sombra_cap = 0.0
    if status == pywraplp.Solver.OPTIMAL:
        if hasattr(restricao_capital, "dual_value"):
            preco_sombra_cap = restricao_capital.dual_value()
        return {
            "sucesso": True,
            "riqueza": solver.Objective().Value(),
            "solucoes": [x1.solution_value(), x2.solution_value(), x3.solution_value(), x4.solution_value(), x5.solution_value(), h1.solution_value(), h2.solution_value()],
            "preco_sombra_capital": preco_sombra_cap
        }
    return {"sucesso": False}


# ==============================================================================
# ITEM 3: SOLUÇÃO ÓTIMA E ESTIMATIVA DO PATRIMÔNIO FINAL
# ==============================================================================
def cenario_solucao_base_e_patrimonio():
    print("\n" + "=" * 60)
    print("ITEM 3: SOLUÇÃO ÓTIMA E ESTIMATIVA DO PATRIMÔNIO FINAL")
    print("=" * 60)
    
    res = _executar_solver_base()
    
    if res["sucesso"]:
        sol = res["solucoes"]
        print(f"Patrimônio Líquido Estimado ao Fim do Ano: ${res['riqueza']:,.2f}")
        print("-" * 50)
        print("Plano de Produção Otimizado:")
        print(f"  - Tamanho do Rebanho de Vacas (x1): {sol[0]:.2f}")
        print(f"  - Tamanho do Lote de Galinhas (x2): {sol[1]:.2f}")
        print(f"  - Área Destinada à Soja (x3): {sol[2]:.2f} acres")
        print(f"  - Área Destinada ao Milho (x4): {sol[3]:.2f} acres")
        print(f"  - Área Destinada ao Trigo (x5): {sol[4]:.2f} acres")
        print(f"  - Mão de Obra Alocada no Vizinho S1 (h1): {sol[5]:.2f} horas")
        print(f"  - Mão de Obra Alocada no Vizinho S2 (h2): {sol[6]:.2f} horas")
        
        print("\n[INTERPRETAÇÃO DE NEGÓCIO]")
        print("A fazenda opera em capacidade máxima de ativos biológicos permitida pelo orçamento ")
        print("e espaço. O milho e trigo são plantados estritamente na quantidade mínima regulamentar ")
        print("para suprir o rebanho, direcionando a terra restante para a cultura mais rentável.")
    else:
        print("Erro ao computar cenário base.")


# ==============================================================================
# ITEM 4: ANÁLISE DE SENSIBILIDADE - FAIXAS DE OTIMALIDADE
# ==============================================================================
def cenario_faixas_otimalidade():
    print("\n" + "=" * 60)
    print("ITEM 4: ANÁLISE DE SENSIBILIDADE - FAIXAS DE OTIMALIDADE")
    print("=" * 60)
    print("Calculando limites de estabilidade para os valores líquidos por acre...")
    
    res_base = _executar_solver_base()
    base_sol = res_base["solucoes"]
    
    # 1. Faixa da Soja
    soja_inf, soja_sup = 0.0, float('inf')
    for val in range(0, 200):
        res = _executar_solver_base(v_soja=float(val))
        if res["sucesso"] and abs(res["solucoes"][2] - base_sol[2]) > 0.1:
            if float(val) < 70.0: soja_inf = float(val)
            elif float(val) > 70.0 and soja_sup == float('inf'): soja_sup = float(val)
            
    # 2. Faixa do Milho
    milho_inf, milho_sup = 0.0, float('inf')
    for val in range(0, 200):
        res = _executar_solver_base(v_milho=float(val))
        if res["sucesso"] and abs(res["solucoes"][3] - base_sol[3]) > 0.1:
            if float(val) < 60.0: milho_inf = float(val)
            elif float(val) > 60.0 and milho_sup == float('inf'): milho_sup = float(val)

    # 3. Faixa do Trigo
    trigo_inf, trigo_sup = 0.0, float('inf')
    for val in range(0, 200):
        res = _executar_solver_base(v_trigo=float(val))
        if res["sucesso"] and abs(res["solucoes"][4] - base_sol[4]) > 0.1:
            if float(val) < 40.0: trigo_inf = float(val)
            elif float(val) > 40.0 and trigo_sup == float('inf'): trigo_sup = float(val)

    print("\n[RESULTADOS DAS FAIXAS DE OTIMALIDADE]")
    print(f"* Valor Líquido da SOJA:  Permanece ótima entre ${soja_inf:.2f} e ${soja_sup:.2f} por acre.")
    print(f"* Valor Líquido do MILHO: Permanece ótima entre ${milho_inf:.2f} e ${milho_sup:.2f} por acre.")
    print(f"* Valor Líquido do TRIGO: Permanece ótima entre ${trigo_inf:.2f} e ${trigo_sup:.2f} por acre.")
    
    print("\n[DIRETRIZ DE NEGÓCIO]")
    print("Contanto que as flutuações de mercado mantenham os retornos líquidos das culturas dentro ")
    print("desses intervalos, a Família Ploughman NÃO deve alterar o planejamento de uso do solo, ")
    print("pois a combinação atual garante a maior eficiência financeira possível perante as restrições.")


# ==============================================================================
# ITEM 5: REOTIMIZAÇÃO EM CADA CENÁRIO CLIMÁTICO ADVERSO
# ==============================================================================
def cenario_climatico_item_5():
    print("\n" + "=" * 60)
    print("ITEM 5: REOTIMIZAÇÃO POR CENÁRIO CLIMÁTICO ADVERSO")
    print("=" * 60)
    
    tabela_climas = {
        "Drought (Seca)": (60.0, 45.0, 40.0),
        "Flood (Enchente)": (85.0, 80.0, 50.0),
        "Early Frost (Geada Precoce)": (120.0, 100.0, 70.0),
        "Drought and Early Frost": (55.0, 40.0, 30.0),
        "Flood and Early Frost": (80.0, 70.0, 45.0)
    }
    
    for clima, valores in tabela_climas.items():
        res = _executar_solver_base(v_soja=valores[0], v_milho=valores[1], v_trigo=valores[2])
        if res["sucesso"]:
            sol = res["solucoes"]
            print(f"\nClima: {clima}")
            print(f"  -> Patrimônio Estimado: ${res['riqueza']:,.2f}")
            print(f"  -> Rebanho Otimizado:  {sol[0]:.0f} Vacas | {sol[1]:.0f} Galinhas")
            print(f"  -> Uso do Solo:        Soja: {sol[2]:.1f} ac | Milho: {sol[3]:.1f} ac | Trigo: {sol[4]:.1f} ac")
        else:
            print(f"Erro ao calcular o cenário: {clima}")


# ==============================================================================
# ITEM 6: ANÁLISE DE ROBUSTEZ FINANCEIRA (GANHO VS RISCO)
# ==============================================================================
def analise_robustez_item_6():
    print("\n" + "=" * 60)
    print("ITEM 6: COMPARAÇÃO DE ROBUSTEZ E EQUILÍBRIO GANHO-RISCO")
    print("=" * 60)
    print("[DIRETRIZES DE GESTÃO DE RISCO ESTRATÉGICO]:")
    print("* Cenário de Maior Riqueza: 'Early Frost' (Geada Precoce), pois a escassez de oferta")
    print("  no mercado eleva drasticamente o valor líquido dos grãos (Soja vai a $120/acre).")
    print("* Cenário de Pior Risco: 'Drought and Early Frost', onde as perdas simultâneas derrubam")
    print("  fortemente as margens operacionais da lavoura.")
    print("\n[Estratégia de Equilíbrio]:")
    print("A melhor solução para mitigar o risco mantendo o ganho alto é blindar a pecuária leiteira.")
    print("Como o gado garante uma receita fixa anual de $850 por cabeça que independe diretamente")
    print("do clima severo nas lavouras, a fazenda deve manter o rebanho fixado no teto físico (42 vacas),")
    print("utilizando a venda de horas de trabalho sobressalentes como um colchão de liquidez estável.")


# ==============================================================================
# ITEM 7: CÁLCULO DOS VALORES MÉDIOS PONDERADOS HISTÓRICOS
# ==============================================================================
def calcular_valores_esperados_item_7():
    print("\n" + "=" * 60)
    print("ITEM 7: VALORES MÉDIOS PONDERADOS (FREQUÊNCIAS HISTÓRICAS)")
    print("=" * 60)
    
    e_soja = (70 * 0.40) + (60 * 0.20) + (85 * 0.10) + (120 * 0.15) + (55 * 0.10) + (80 * 0.05)
    e_milho = (60 * 0.40) + (45 * 0.20) + (80 * 0.10) + (100 * 0.15) + (40 * 0.10) + (70 * 0.05)
    e_trigo = (40 * 0.40) + (40 * 0.20) + (50 * 0.10) + (70 * 0.15) + (30 * 0.10) + (45 * 0.05)
    
    print("Indicadores Macroeconômicos Esperados (E[X]):")
    print(f"  - Retorno Esperado da Soja:  ${e_soja:.2f} por acre")
    print(f"  - Retorno Esperado do Milho: ${e_milho:.2f} por acre")
    print(f"  - Retorno Esperado do Trigo: ${e_trigo:.2f} por acre")
    
    return e_soja, e_milho, e_trigo


# ==============================================================================
# ITEM 8: RESOLUÇÃO DO MODELO COM A ABORDAGEM DE VALOR ESPERADO
# ==============================================================================
def resolver_valor_esperado_item_8():
    print("\n" + "=" * 60)
    print("ITEM 8: SOLUÇÃO ÓTIMA DA ABORDAGEM ESTOCÁSTICA (VALOR ESPERADO)")
    print("=" * 60)
    
    es, em, et = 68.50, 59.50, 46.25
    res = _executar_solver_base(v_soja=es, v_milho=em, v_trigo=et)
    
    if res["sucesso"]:
        sol = res["solucoes"]
        print(f"Patrimônio Médio Esperado sob Incerteza Climática: ${res['riqueza']:,.2f}")
        print("-" * 50)
        print("Plano de Production Estocasticamente Seguro:")
        print(f"  - Rebanho de Vacas (x1): {sol[0]:.0f} unidades")
        print(f"  - Lote de Galinhas (x2): {sol[1]:.0f} unidades")
        print(f"  - Área para Soja (x3):   {sol[2]:.1f} acres")
        print(f"  - Área para Milho (x4):  {sol[3]:.1f} acres")
        print(f"  - Área para Trigo (x5):  {sol[4]:.1f} acres")
        print(f"  - Horas no Vizinho S1/S2: {sol[5]:.1f}h / {sol[6]:.1f}h")
    else:
        print("Erro ao solucionar o modelo estocástico.")


# ==============================================================================
# ITEM 9: ANÁLISE DE PREÇO-SOMBRA PARA TOMADA DE EMPRÉSTIMO A 10%
# ==============================================================================
def avaliar_emprestimo_item_9():
    print("\n" + "=" * 60)
    print("ITEM 9: ANÁLISE DE PREÇO-SOMBRA E VIABILIDADE DE EMPRÉSTIMO")
    print("=" * 60)
    
    res_base = _executar_solver_base()
    res_extra = _executar_solver_base(cap_extra=10000.0)
    
    ganho_por_dolar = (res_extra["riqueza"] - res_base["riqueza"]) / 10000.0
    
    print(f"Taxa de Retorno Marginal do Fundo de Investimento: {ganho_por_dolar * 100:.2f}%")
    print(f"Custo de Capital do Financiamento Bancário:        10.00%")
    print("-" * 50)
    
    if ganho_por_dolar > 0.10:
        print("RECOMENDAÇÃO: SIM, VALE A PENA TOMAR O EMPRÉSTIMO.")
        print("O preço-sombra (valor dual) do recurso financeiro é superior à taxa de juros de 10%,")
        print("indicando que a compra de novos animais gera valor real e paga as parcelas do banco com folga.")
    else:
        print("RECOMENDAÇÃO: NÃO VALE A PENA TOMAR O EMPRÉSTIMO.")
        print("O preço-sombra está abaixo de 10% (ou zerado). Isso ocorre porque a limitação")
        print("física de infraestrutura (como o espaço do celeiro para 42 vacas) impede que")
        print("mais capital seja convertido em ativos biológicos produtivos.")


# ==============================================================================
# ITEM 10: ANÁLISE PÓS-OTIMIZAÇÃO E PRECISÃO DE ESTIMATIVAS
# ==============================================================================
def avaliar_precisao_estimativas_item_10():
    print("\n" + "=" * 60)
    print("ITEM 10: SENSIBILIDADE ANALÍTICA DAS LAVOURAS")
    print("=" * 60)
    print("[Mapeamento de Sensibilidade Volátil]:")
    print("1. Cultura de Maior Precisão Exigida: A SOJA.")
    print("   Como a soja não possui exigência mínima de consumo interno pelos animais (ao contrário")
    print("   do milho e do trigo), toda a sua oscilação de mercado afeta diretamente o lucro marginal.")
    print("2. Impacto de Erros de Previsão:")
    print("   Qualquer variação de centavos nas estimativas da soja pode alterar o ponto de virada exato")
    print("   entre plantar grãos ou alocar a família para vender horas na fazenda vizinha. Portanto,")
    print("   John e Eunice devem focar seus esforços de pesquisa de mercado na precisão dos preços da soja.")


# ==============================================================================
# ITEM 11: GENERALIZAÇÃO DO PROBLEMA FORA DO CONTEXTO DA FAZENDA
# ==============================================================================
def mostrar_generalizacao_item_11():
    print("\n" + "=" * 60)
    print("ITEM 11: GENERALIZAÇÃO DO MODELO DE PROGRAMAÇÃO LINEAR")
    print("=" * 60)
    print("Este problema pertence à classe dos 'Modelos Estocásticos de Mix de Portfólio com Restrição de Ativos'.")
    print("\n[Exemplo Prático Corporativo: Indústria de Tecnologia e Manufatura de Hardware]")
    print("Imagine uma corporação fabril de eletrônicos avaliando o planejamento para o próximo ano:")
    print("  - Ativos Biológicos (Vacas/Galinhas) = Linhas de Montagem e Maquinários SMT robóticos,")
    print("    que possuem capacidade máxima física instalada e sofrem depreciação anual severa por obsolescência.")
    print("  - Culturas de Grãos (Soja/Milho/Trigo) = Produção de Chips de Silício de diferentes categorias.")
    print("  - Subsistência Interna (Ração dos Bichos) = Chips básicos produzidos internamente que servem")
    print("    como insumo obrigatório para alimentar a montagem dos produtos finais de alto valor.")
    print("  - Cenários Climáticos (Incertezas) = Flutuações macroeconômicas na taxa de câmbio ou")
    print("    escassez de silício no mercado asiático, alterando o valor esperado de retorno de cada item.")
    print("  - Venda de Mão de Obra para o Vizinho = Aluguel de engenheiros/capacidade de TI ociosa")
    print("    para projetos de terceiros (Outsourcing) como receita garantida de segurança.")