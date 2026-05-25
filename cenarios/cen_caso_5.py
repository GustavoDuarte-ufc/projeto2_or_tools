# cenarios/cen_caso_5.py
from modelos.caso_5 import caso_5

def cenario_1_e_2_caso_5():
    print("\n" + "=" * 60)
    print("CENÁRIO 1 & 2 — AVALIAÇÃO DE PRODUÇÃO DE CAMISAS DE VELUDO")
    print("=" * 60)
    print("Análise: Margem unitária de $22 vs Custo Fixo de $500.000.")
    caso_5(veludo_devolvivel=True)

def cenario_3_caso_5():
    print("\n" + "=" * 60)
    print("CENÁRIO 3 — VELUDO NÃO DEVOLVÍVEL (SUNK COST)")
    print("=" * 60)
    print("Análise: Se o veludo não puder ser devolvido, o custo torna-se afundado.")
    caso_5(veludo_devolvivel=False)

def cenario_4_caso_5():
    print("\n" + "=" * 60)
    print("CENÁRIO 4 — EXPLICAÇÃO ECONÔMICA INTUITIVA")
    print("=" * 60)
    print("• Devolvível: Não produzir economiza o custo fixo e recupera o valor do tecido.")
    print("• Não Devolvível: O capital do tecido está perdido. Se a margem gerada pagar")
    print("  pelo menos uma parte do custo fixo, o modelo pode forçar a produção para mitigar perdas.")

def cenario_5_caso_5():
    print("\n" + "=" * 60)
    print("CENÁRIO 5 — INCREMENTO DE CUSTO NO BLAZER DE LÃ")
    print("=" * 60)
    print("Análise: Impacto do aumento de $80 em mão de obra e máquina do blazer_la.")
    caso_5(aumento_custo_lã_blazer=80.0)

def cenario_6_caso_5():
    print("\n" + "=" * 60)
    print("CENÁRIO 6 — DISPONIBILIDADE DE ACETATO EXTRA")
    print("=" * 60)
    print("Análise: Adição de 10.000 jardas extras de acetato ao estoque.")
    caso_5(acetato_extra=10000.0)

def cenario_7_caso_5():
    print("\n" + "=" * 60)
    print("CENÁRIO 7 — MONETIZAÇÃO DE SOBRAS EM NOVEMBRO")
    print("=" * 60)
    print("Análise: Venda de sobras de Setembro/Outubro por 60% do valor original.")
    caso_5(venda_sobras_novembro=True)