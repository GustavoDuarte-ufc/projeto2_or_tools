# cenarios/cen_caso_4.py

from modelos.caso_4 import caso_4


# ======================================================
# CENÁRIO 2
# LIMITAÇÃO DE OPERADOR INGLÊS ÀS 13H
# ======================================================

def cenario_2_caso_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 2 — LIMITE DE OPERADOR INTEGRAL ÀS 13H")
    print("=" * 60)

    print(
        "\nA administração deseja limitar "
        "a quantidade de operadores integrais "
        "de inglês iniciando às 13h."
    )

    print(
        "\nObjetivo: avaliar o impacto "
        "operacional da restrição."
    )

    print(
        "\nNova regra operacional:"
    )

    print(
        "• Máximo de 1 operador integral "
        "de inglês iniciando às 13h."
    )

    print("\nAnálise operacional:\n")

    caso_4(
        limite_integral_13h=1
    )


# ======================================================
# CENÁRIO 3
# REDUÇÃO DE OPERADORES BILÍNGUES
# ======================================================

def cenario_3_caso_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 3 — REDUÇÃO DE BILÍNGUES")
    print("=" * 60)

    print(
        "\nA empresa avalia reduzir "
        "a dependência de operadores "
        "bilíngues para diminuir custos."
    )

    print(
        "\nNovo cenário:"
    )

    print(
        "• Apenas 10% das chamadas "
        "necessitam espanhol."
    )

    print("\nImpacto esperado:\n")

    print(
        "• Menor necessidade de operadores "
        "especializados."
    )

    print(
        "• Redução do custo operacional."
    )

    print("\nResultado do modelo:\n")

    caso_4(
        percentual_espanhol=0.10
    )


# ======================================================
# CENÁRIO 4
# CONTRATAÇÃO DE BILÍNGUES
# ======================================================

def cenario_4_caso_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 4 — OPERADORES BILÍNGUES")
    print("=" * 60)

    print(
        "\nA diretoria avalia contratar "
        "operadores bilíngues capazes "
        "de atender inglês e espanhol."
    )

    print(
        "\nObjetivo:"
    )

    print(
        "• Reduzir o número total "
        "de operadores necessários."
    )

    print(
        "• Melhorar flexibilidade operacional."
    )

    print(
        "\nHipótese operacional:"
    )

    print(
        "• Operadores bilíngues substituem "
        "parte dos operadores em espanhol."
    )

    print("\nResultado estimado:\n")

    caso_4(
        percentual_espanhol=0.15
    )


# ======================================================
# CENÁRIO 5
# AUMENTO DA DEMANDA
# ======================================================

def cenario_5_caso_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 5 — AUMENTO DA DEMANDA")
    print("=" * 60)

    print(
        "\nO hospital projeta aumento "
        "de chamadas durante horários "
        "de pico."
    )

    print(
        "\nNova condição:"
    )

    print(
        "• Crescimento de 20% "
        "na demanda operacional."
    )

    print("\nObjetivo da análise:\n")

    print(
        "• Avaliar necessidade "
        "de expansão da equipe."
    )

    print(
        "• Identificar gargalos "
        "operacionais."
    )

    nova_demanda = {
        '7-9': 40 * 2 * 1.2,
        '9-11': 85 * 2 * 1.2,
        '11-13': 70 * 2 * 1.2,
        '13-15': 95 * 2 * 1.2,
        '15-17': 80 * 2 * 1.2,
        '17-19': 35 * 2 * 1.2,
        '19-21': 10 * 2 * 1.2,
    }

    print("\nResultado do modelo:\n")

    caso_4(
        demanda_por_periodo=nova_demanda
    )


# ======================================================
# CENÁRIO 6
# REDUÇÃO DE CUSTOS
# ======================================================

def cenario_6_caso_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 6 — REDUÇÃO DE CUSTOS")
    print("=" * 60)

    print(
        "\nA empresa deseja avaliar "
        "o impacto de redução salarial "
        "nos turnos noturnos."
    )

    print(
        "\nNovo cenário salarial:"
    )

    print(
        "• Após 17h: US$ 11/h"
    )

    print(
        "• Antes das 17h: mantido em US$ 10/h"
    )

    novo_salario = {
        '7-9': 20,
        '9-11': 20,
        '11-13': 20,
        '13-15': 20,
        '15-17': 20,
        '17-19': 22,
        '19-21': 22
    }

    print("\nResultado do modelo:\n")

    caso_4(
        salario_por_periodo=novo_salario
    )


# ======================================================
# CENÁRIO 7
# OPERAÇÃO OTIMIZADA
# ======================================================

def cenario_7_caso_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 7 — OPERAÇÃO OTIMIZADA")
    print("=" * 60)

    print(
        "\nA administração deseja "
        "avaliar um cenário otimizado "
        "com múltiplas melhorias."
    )

    print("\nMudanças implementadas:\n")

    melhorias = [
        "• Redução das chamadas em espanhol",
        "• Melhor distribuição operacional",
        "• Crescimento moderado da demanda",
        "• Controle de custos noturnos",
    ]

    for melhoria in melhorias:
        print(melhoria)

    nova_demanda = {
        '7-9': 40 * 2 * 1.1,
        '9-11': 85 * 2 * 1.1,
        '11-13': 70 * 2 * 1.1,
        '13-15': 95 * 2 * 1.1,
        '15-17': 80 * 2 * 1.1,
        '17-19': 35 * 2 * 1.1,
        '19-21': 10 * 2 * 1.1,
    }

    print("\nResultado executivo:\n")

    caso_4(
        percentual_espanhol=0.10,
        demanda_por_periodo=nova_demanda
    )