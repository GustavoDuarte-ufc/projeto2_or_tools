from tabulate import tabulate
import time
import sys


def escrever(texto, velocidade=0):

    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

    print()


def linha():

    print("=" * 70)


def montagem_caso_2():

    linha()

    escrever("AUTOMOTIVE INDUSTRY SOLUTIONS")
    escrever("Montagem do Modelo Matemático")

    linha()

    escrever("\n[1] Definição das variáveis de decisão\n")

    escrever(
        "Foram criadas variáveis para representar "
        "a quantidade produzida de cada modelo."
    )

    print()

    escrever("x1 = quantidade de Family Thrillseeker")
    escrever("x2 = quantidade de Classy Cruiser")

    linha()

    escrever("\n[2] Função objetivo\n")

    escrever(
        "O objetivo do modelo é maximizar "
        "o lucro total da montadora."
    )

    print()

    escrever(
        "Lucro Total = 3600(x1) + 5400(x2)"
    )

    linha()

    escrever("\n[3] Restrição de horas de trabalho\n")

    escrever(
        "A planta possui limite mensal "
        "de 48.000 horas produtivas."
    )

    print()

    escrever(
        "6(x1) + 10.5(x2) <= 48000"
    )

    linha()

    escrever("\n[4] Restrição de portas disponíveis\n")

    escrever(
        "A disponibilidade total de portas "
        "é limitada em 20.000 unidades."
    )

    print()

    escrever(
        "4(x1) + 4(x2) <= 20000"
    )

    linha()

    escrever("\n[5] Restrição de demanda do Cruiser\n")

    escrever(
        "O modelo Classy Cruiser possui "
        "demanda máxima de mercado."
    )

    print()

    escrever(
        "x2 <= 3500"
    )

    linha()

    escrever("\n[6] Restrição de não negatividade\n")

    escrever(
        "As variáveis não podem assumir "
        "valores negativos."
    )

    print()

    escrever(
        "x1 >= 0"
    )

    escrever(
        "x2 >= 0"
    )

    linha()

    escrever("\n[7] Estrutura geral do modelo\n")

    tabela = [
        ["Variáveis", "Quantidade produzida de veículos"],
        ["Objetivo", "Maximizar lucro"],
        ["Restrição 1", "Horas de trabalho"],
        ["Restrição 2", "Disponibilidade de portas"],
        ["Restrição 3", "Demanda máxima"],
    ]

    print(
        tabulate(
            tabela,
            headers=["Elemento", "Descrição"],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[8] Estratégia computacional\n")

    escrever(
        "O problema será resolvido utilizando "
        "Programação Linear."
    )

    escrever(
        "A otimização será realizada pelo solver SCIP "
        "através da biblioteca OR-Tools."
    )

    linha()

    escrever(
        "\nModelo matemático preparado para resolução."
    )

    linha()