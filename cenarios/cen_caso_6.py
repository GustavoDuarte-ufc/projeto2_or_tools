# cenarios/cen_caso_6.py
from modelos.caso_6 import caso_6

# ======================================================
# ITEM 1 & 2 — CENÁRIO BASE E LANCE (BID)
# ======================================================
def cenario_1_e_2_caso_6():
    print("\n" + "=" * 60)
    print("ITEM 1 & 2 — MODELO BASE E CÁLCULO DE LANCE (BID)")
    print("=" * 60)
    print("Objetivo: Resolver o custo mínimo e aplicar margem de lucro de 15%.")
    caso_6()


# ======================================================
# ITEM 3 — EXIGÊNCIA ADICIONAL POR CÉLULA (MÍNIMO 50)
# ======================================================
def cenario_3_caso_6():
    print("\n" + "=" * 60)
    print("ITEM 3 — EXIGÊNCIA MÍNIMA GEOGRÁFICA/ETÁRIA")
    print("=" * 60)
    print("Nova Restrição: Ao menos 50 pessoas de cada faixa etária em cada região.")
    caso_6(minimo_por_celula=50)


# ======================================================
# ITEM 4 — RESTRIÇÕES DE TETO (MÁXIMOS CAP)
# ======================================================
def cenario_4_caso_6():
    print("\n" + "=" * 60)
    print("ITEM 4 — LIMITES MÁXIMOS DE COBERTA (CAPS)")
    print("=" * 60)
    print("Novas Restrições:")
    print(" • Máximo de 600 pessoas na faixa de 18-25 anos.")
    print(" • Máximo de 650 pessoas na região de alto uso (Silicon Valley).")
    caso_6(maximo_jovens=600, maximo_alto_uso=650)


# ======================================================
# ITEM 5 — ATUALIZAÇÃO DE CUSTOS POR REGIÃO
# ======================================================
def cenario_5_caso_6():
    print("\n" + "=" * 60)
    print("ITEM 5 — CUSTOS ATUALIZADOS POR GRUPO/REGIÃO")
    print("=" * 60)
    print("Mudança: Custos passam a ser fixados puramente por região geográfica:")
    print(" • Silicon Valley: $6.50/pessoa  • Big Cities: $6.75/pessoa  • Small Towns: $7.00/pessoa")
    caso_6(novos_custos_regionais=True)


# ======================================================
# ITEM 6 — REQUISITOS MAIS RÍGIDOS (PERCENTUAIS FIXOS)
# ======================================================
def cenario_6_caso_6():
    print("\n" + "=" * 60)
    print("ITEM 6 — REQUISITOS MAIS RÍGIDOS (PERCENTUAIS FIXOS)")
    print("=" * 60)
    print("Mudança: As cotas mínimas passam a ser tratadas como alocações FIXAS exatas:")
    print(" • Idades: 18-25 (25%), 26-40 (35%), 41-50 (20%), 51+ (20%)")
    print(" • Regiões: Silicon Valley (20%), Big Cities (50%), Small Towns (30%)")
    caso_6(percentuais_fixos=True)