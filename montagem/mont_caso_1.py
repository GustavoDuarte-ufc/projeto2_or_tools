from tabulate import tabulate
import time
import sys


def escrever(texto, velocidade=0):
    """
    Exibe texto com efeito de digitação.
    """

    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

    print()


def linha():
    """
    Exibe linha separadora.
    """

    print("=" * 70)


def montagem_caso_1():

    linha()

    escrever("CHILDFAIR LOGISTICS")
    escrever("Modelagem Matemática do Problema de Transporte")

    linha()

    escrever("\n[1] Definição do cenário\n")

    escrever(
        "A Childfair deseja determinar o melhor plano "
        "de distribuição entre suas fábricas e centros "
        "de distribuição."
    )

    escrever(
        "O objetivo do modelo é minimizar os custos "
        "totais de transporte da operação logística."
    )

    linha()

    escrever("\n[2] Estrutura do problema\n")

    escrever("• 3 fábricas")
    escrever("• 4 centros de distribuição")
    escrever("• Transporte mensal de remessas")

    linha()

    escrever("\n[3] Variáveis de decisão\n")

    escrever(
        "Foi criada uma variável de decisão para cada "
        "rota possível entre fábricas e centros."
    )

    escrever(
        "Cada variável representa a quantidade de "
        "remessas enviadas em determinada rota."
    )

    escrever("\nExemplo:\n")

    escrever(
        "x[1,2] = quantidade enviada da "
        "Fábrica 1 para o Centro 2"
    )

    linha()

    escrever("\n[4] Capacidade produtiva das fábricas\n")

    producao = [
        ["Fábrica 1", "12 remessas"],
        ["Fábrica 2", "17 remessas"],
        ["Fábrica 3", "11 remessas"],
    ]

    print(
        tabulate(
            producao,
            headers=["Fábrica", "Capacidade Máxima"],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[5] Matriz de distâncias\n")

    distancias = [
        ["Fábrica 1", 800, 1300, 400, 700],
        ["Fábrica 2", 1100, 1400, 600, 1000],
        ["Fábrica 3", 600, 1200, 800, 900],
    ]

    print(
        tabulate(
            distancias,
            headers=[
                "Origem",
                "Centro 1",
                "Centro 2",
                "Centro 3",
                "Centro 4"
            ],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[6] Estrutura de custos\n")

    escrever(
        "O custo logístico de cada rota é composto por:"
    )

    escrever("• Valor fixo de $100 por remessa")
    escrever("• Valor variável de $0,50 por milha")

    escrever("\nExemplo de cálculo:\n")

    escrever(
        "Fábrica 1 → Centro 1"
    )

    escrever(
        "100 + (800 × 0.5) = $500"
    )

    linha()

    escrever("\n[7] Restrições do modelo\n")

    escrever(
        "Restrição 1 — Oferta:"
    )

    escrever(
        "Cada fábrica possui limite máximo "
        "de produção mensal."
    )

    escrever(
        "A soma das remessas enviadas não "
        "pode ultrapassar sua capacidade."
    )

    print()

    escrever(
        "Restrição 2 — Demanda:"
    )

    escrever(
        "Cada centro de distribuição deve "
        "receber exatamente 10 remessas."
    )

    linha()

    escrever("\n[8] Função objetivo\n")

    escrever(
        "O modelo busca minimizar o custo "
        "total de transporte da operação."
    )

    escrever(
        "A função objetivo soma os custos "
        "de todas as rotas utilizadas."
    )

    linha()

    escrever("\n[9] Estratégia computacional\n")

    escrever(
        "O problema foi modelado utilizando "
        "Programação Linear Inteira."
    )

    escrever(
        "A resolução será realizada pelo solver SCIP "
        "através da biblioteca OR-Tools."
    )

    linha()

    escrever(
        "\nModelo matemático preparado para execução."
    )

    linha()