def montagem_caso_8():
    print("\n" + "-" * 60)
    print("ESTRUTURA MATEMÁTICA DO MODELO (CASO 8)")
    print("-" * 60)
    print("""
    [CONJUNTOS]
    - Culturas: {Soja, Milho, Trigo}
    - Períodos (Mão de Obra): {Semestre 1 (Inverno/Primavera), Semestre 2 (Verão/Outono)}

    [VARIÁVEIS DE DECISÃO]
    - x_vaca: Rebanho total de vacas (30 <= x_vaca <= 42)
    - x_galinha: Lote total de galinhas (2000 <= x_galinha <= 5000)
    - x_soja, x_milho, x_trigo: Acres destinados a cada cultura (>= 0)
    - h1, h2: Horas vendidas para a fazenda vizinha por período (>= 0)

    [FUNÇÃO OBJETIVO]
    Maximizar Z (Riqueza Final) = 700*x_vaca + 3.50*x_galinha + 70*x_soja 
                                  + 60*x_milho + 40*x_trigo + 5.0*h1 + 5.5*h2 - 10750

    [RESTRIÇÕES CRÍTICAS]
    - Limite de Espaço de Terra: 2*x_vaca + x_soja + x_milho + x_trigo <= 640 acres
    - Fundo de Investimento: 1500*(x_vaca - 30) + 3*(x_galinha - 2000) <= 20000
    - Subsistência Alimentar: x_milho >= x_vaca  |  x_trigo >= 0.05*x_galinha
    - Alocação de Horas S1: 60*x_vaca + 0.3*x_galinha + 1.0*x_soja + 0.9*x_milho + 0.6*x_trigo + h1 = 4000
    - Alocação de Horas S2: 60*x_vaca + 0.3*x_galinha + 1.4*x_soja + 1.2*x_milho + 0.7*x_trigo + h2 = 4500
    """)