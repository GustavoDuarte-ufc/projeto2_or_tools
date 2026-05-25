# cenarios/cen_caso_2.py
from modelos.caso_2 import caso_2


# ==========================================================
# CENÁRIO 2 — CAMPANHA DE MARKETING
# ==========================================================

def cenario_2():

    print("\n" + "=" * 60)
    print("CENÁRIO 2 — CAMPANHA DE MARKETING")
    print("=" * 60)

    print(
        "\nUma campanha de marketing no valor "
        "de R$ 500.000 aumenta em 20% "
        "a demanda do modelo Classy Cruiser."
    )

    lucro_base = caso_2(
        mostrar=False
    )

    lucro_marketing = caso_2(
        mostrar=False,
        demanda_cruiser=3500 * 1.2
    )

    lucro_liquido = lucro_marketing - 500000

    print(f"\nLucro sem campanha: R$ {lucro_base:,.2f}")

    print(
        f"Lucro com aumento de demanda: "
        f"R$ {lucro_marketing:,.2f}"
    )

    print(
        f"Lucro líquido após custo "
        f"da campanha: R$ {lucro_liquido:,.2f}"
    )

    impacto = lucro_liquido - lucro_base

    print(
        f"\nImpacto econômico da campanha: "
        f"R$ {impacto:,.2f}"
    )

    print("\nAnálise executiva:\n")

    if impacto > 0:

        print(
            "A campanha apresenta retorno financeiro positivo "
            "e é economicamente recomendada."
        )

    else:

        print(
            "A campanha não gera ganho financeiro suficiente "
            "para compensar o investimento realizado."
        )


# ==========================================================
# CENÁRIO 3 — HORAS EXTRAS
# ==========================================================

def cenario_3():

    print("\n" + "=" * 60)
    print("CENÁRIO 3 — HORAS EXTRAS")
    print("=" * 60)

    print(
        "\nA empresa avalia a utilização "
        "de horas extras para ampliar "
        "a capacidade produtiva da planta."
    )

    nova_capacidade = 48000 * 1.25

    lucro_base = caso_2(
        mostrar=False
    )

    lucro_horas_extras = caso_2(
        mostrar=False,
        horas_totais=nova_capacidade
    )

    ganho = lucro_horas_extras - lucro_base

    print(f"\nLucro original: R$ {lucro_base:,.2f}")

    print(
        f"Lucro com horas extras: "
        f"R$ {lucro_horas_extras:,.2f}"
    )

    print(
        f"Ganho operacional: "
        f"R$ {ganho:,.2f}"
    )

    print("\nAnálise executiva:\n")

    if ganho > 0:

        print(
            "A ampliação da capacidade produtiva "
            "gera crescimento operacional."
        )

    else:

        print(
            "As horas extras não produzem "
            "ganhos financeiros relevantes."
        )


# ==========================================================
# CENÁRIO 4 — VALOR MÁXIMO DAS HORAS EXTRAS
# ==========================================================

def cenario_4():

    print("\n" + "=" * 60)
    print("CENÁRIO 4 — VALOR MÁXIMO DAS HORAS EXTRAS")
    print("=" * 60)

    lucro_base = caso_2(
        mostrar=False
    )

    lucro_horas_extras = caso_2(
        mostrar=False,
        horas_totais=48000 * 1.25
    )

    ganho = lucro_horas_extras - lucro_base

    print(
        f"\nLucro adicional obtido: "
        f"R$ {ganho:,.2f}"
    )

    print(
        "\nEsse representa o valor máximo "
        "que vale pagar pelas horas extras."
    )

    print("\nAnálise executiva:\n")

    print(
        "Qualquer custo acima desse valor "
        "elimina a viabilidade econômica "
        "da expansão operacional."
    )


# ==========================================================
# CENÁRIO 5 — MARKETING + HORAS EXTRAS
# ==========================================================

def cenario_5():

    print("\n" + "=" * 60)
    print("CENÁRIO 5 — COMBINAÇÃO DE CENÁRIOS")
    print("=" * 60)

    print(
        "\nA empresa avalia simultaneamente:"
    )

    print("• Campanha de marketing (+20% demanda)")
    print("• Horas extras (+25% capacidade)")

    lucro = caso_2(
        mostrar=True,
        demanda_cruiser=3500 * 1.2,
        horas_totais=48000 * 1.25
    )

    print(
        f"\nLucro total combinado: "
        f"R$ {lucro:,.2f}"
    )

    print("\nAnálise executiva:\n")

    print(
        "A combinação de expansão comercial "
        "e produtiva amplia o potencial "
        "de rentabilidade da operação."
    )


# ==========================================================
# CENÁRIO 6 — VIABILIDADE ECONÔMICA
# ==========================================================

def cenario_6():

    print("\n" + "=" * 60)
    print("CENÁRIO 6 — VIABILIDADE ECONÔMICA")
    print("=" * 60)

    lucro_base = caso_2(
        mostrar=False
    )

    lucro_cenario = caso_2(
        mostrar=False,
        demanda_cruiser=3500 * 1.2,
        horas_totais=48000 * 1.25
    )

    lucro_liquido = lucro_cenario - 500000 - 1600000

    impacto = lucro_liquido - lucro_base

    print(
        f"\nLucro líquido do cenário: "
        f"R$ {lucro_liquido:,.2f}"
    )

    print(
        f"Impacto frente ao cenário base: "
        f"R$ {impacto:,.2f}"
    )

    print("\nAnálise executiva:\n")

    if impacto > 0:

        print(
            "O investimento conjunto apresenta "
            "retorno econômico positivo."
        )

    else:

        print(
            "Os custos operacionais superam "
            "os ganhos financeiros obtidos."
        )


# ==========================================================
# CENÁRIO 7 — QUEDA DO LUCRO DO THRILLSEEKER
# ==========================================================

def cenario_7():

    print("\n" + "=" * 60)
    print("CENÁRIO 7 — REDUÇÃO DE MARGEM")
    print("=" * 60)

    print(
        "\nO lucro do modelo Family Thrillseeker "
        "cai para R$ 2.800 por unidade."
    )

    lucro = caso_2(
        mostrar=True,
        lucro_por_unidade={
            'Family Thrillseeker': 2800,
            'Classy Cruiser': 5400
        }
    )

    print(
        f"\nNovo lucro total: "
        f"R$ {lucro:,.2f}"
    )


# ==========================================================
# CENÁRIO 8 — AUMENTO DO TEMPO DE MONTAGEM
# ==========================================================

def cenario_8():

    print("\n" + "=" * 60)
    print("CENÁRIO 8 — INSPEÇÕES OPERACIONAIS")
    print("=" * 60)

    print(
        "\nO tempo de montagem do "
        "Family Thrillseeker sobe para 7,5 horas."
    )

    lucro = caso_2(
        mostrar=True,
        horas_por_unidade={
            'Family Thrillseeker': 7.5,
            'Classy Cruiser': 10.5
        }
    )

    print(
        f"\nNovo lucro operacional: "
        f"R$ {lucro:,.2f}"
    )


# ==========================================================
# CENÁRIO 9 — DEMANDA OBRIGATÓRIA DO CRUISER
# ==========================================================

def cenario_9():

    print("\n" + "=" * 60)
    print("CENÁRIO 9 — DEMANDA OBRIGATÓRIA")
    print("=" * 60)

    print(
        "\nA diretoria exige atendimento "
        "integral da demanda do Cruiser."
    )

    lucro_base = caso_2(
        mostrar=False
    )

    lucro_novo = caso_2(
        mostrar=False,
        demanda_obrigatoria=True
    )

    perda = lucro_base - lucro_novo

    print(
        f"\nQueda de lucro: "
        f"R$ {perda:,.2f}"
    )

    print("\nAnálise executiva:\n")

    if perda <= 2000000:

        print(
            "A exigência é financeiramente aceitável."
        )

    else:

        print(
            "A exigência compromete excessivamente "
            "a rentabilidade operacional."
        )


# ==========================================================
# CENÁRIO 10 — DECISÃO FINAL
# ==========================================================

def cenario_10():

    print("\n" + "=" * 60)
    print("CENÁRIO 10 — DECISÃO EXECUTIVA FINAL")
    print("=" * 60)

    print(
        "\nA análise consolidada considera:"
    )

    print("• Campanha de marketing")
    print("• Horas extras")
    print("• Queda de margem")
    print("• Aumento de inspeções")

    lucro = caso_2(
        mostrar=False,
        demanda_cruiser=3500 * 1.2,
        horas_totais=48000 * 1.25,
        lucro_por_unidade={
            'Family Thrillseeker': 2800,
            'Classy Cruiser': 5400
        },
        horas_por_unidade={
            'Family Thrillseeker': 7.5,
            'Classy Cruiser': 10.5
        }
    )

    lucro_liquido = lucro - 500000 - 1600000

    print(
        f"\nLucro líquido consolidado: "
        f"R$ {lucro_liquido:,.2f}"
    )

    print("\nDecisão executiva:\n")

    print(
        "A recomendação final deve considerar "
        "o equilíbrio entre crescimento operacional, "
        "capacidade produtiva e rentabilidade."
    )