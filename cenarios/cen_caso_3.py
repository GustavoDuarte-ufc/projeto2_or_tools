from modelos.caso_3 import caso_3


# ==========================================================
# CENÁRIO 2 — NOVA RAZÃO OPERACIONAL
# ==========================================================

def cenario_2_caso_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 2 — NOVA RAZÃO OPERACIONAL")
    print("=" * 60)

    print(
        "\nA razão mínima entre batata e vagem "
        "passa de 6:5 para 1:2."
    )

    caso_3(
        razao_batata=1,
        razao_vagem=2
    )


# ==========================================================
# CENÁRIO 3 — REDUÇÃO DA EXIGÊNCIA DE FERRO
# ==========================================================

def cenario_3_caso_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 3 — REDUÇÃO DA EXIGÊNCIA DE FERRO")
    print("=" * 60)

    print(
        "\nA exigência mínima de ferro "
        "cai para 65 mg."
    )

    caso_3(
        ferro_minimo=65
    )


# ==========================================================
# CENÁRIO 4 — REDUÇÃO DO PREÇO DA VAGEM
# ==========================================================

def cenario_4_caso_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 4 — REDUÇÃO DE PREÇO")
    print("=" * 60)

    print(
        "\nO preço da vagem cai "
        "de R$ 1,00 para R$ 0,50."
    )

    caso_3(
        custo_vagem=0.50
    )


# ==========================================================
# CENÁRIO 5 — SUBSTITUIÇÃO POR FEIJÃO-LIMA
# ==========================================================

def cenario_5_caso_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 5 — SUBSTITUIÇÃO DE INGREDIENTE")
    print("=" * 60)

    print(
        "\nA vagem será substituída "
        "por feijão-lima."
    )

    caso_3(
        usar_feijao_lima=True
    )


# ==========================================================
# CENÁRIO 6 — VALIDAÇÃO NUTRICIONAL
# ==========================================================

def cenario_6_caso_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 6 — VALIDAÇÃO NUTRICIONAL")
    print("=" * 60)

    print(
        "\nVerificação do atendimento "
        "dos requisitos nutricionais."
    )

    caso_3(
        usar_feijao_lima=True,
        validar_nutricao=True
    )


# ==========================================================
# CENÁRIO 7 — NOVAS EXIGÊNCIAS NUTRICIONAIS
# ==========================================================

def cenario_7_caso_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 7 — NOVOS REQUISITOS")
    print("=" * 60)

    print(
        "\nNovos requisitos nutricionais:"
    )

    print("• Ferro mínimo = 120 mg")
    print("• Vitamina C mínima = 500 mg")

    caso_3(
        usar_feijao_lima=True,
        ferro_minimo=120,
        vitamina_c_minima=500
    )