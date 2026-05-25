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


def apresentar_caso_1():

    linha()

    escrever("CHILDFAIR LOGISTICS")
    escrever("Sistema Estratégico de Otimização de Transporte")

    linha()

    escrever("\n[1] Contexto do negócio\n")

    escrever(
        "A Childfair possui uma operação logística "
        "composta por 3 fábricas e 4 centros de distribuição."
    )

    escrever(
        "O objetivo estratégico da companhia é minimizar "
        "os custos mensais de transporte das remessas."
    )

    escrever(
        "O estudo considera simultaneamente restrições "
        "de capacidade produtiva e atendimento da demanda."
    )

    linha()

    escrever("\n[2] Capacidade produtiva das fábricas\n")

    fabricas = [
        ["Fábrica 1", "12 remessas/mês"],
        ["Fábrica 2", "17 remessas/mês"],
        ["Fábrica 3", "11 remessas/mês"],
    ]

    print(
        tabulate(
            fabricas,
            headers=["Fábrica", "Capacidade"],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[3] Demanda dos centros de distribuição\n")

    centros = [
        ["Centro 1", "10 remessas/mês"],
        ["Centro 2", "10 remessas/mês"],
        ["Centro 3", "10 remessas/mês"],
        ["Centro 4", "10 remessas/mês"],
    ]

    print(
        tabulate(
            centros,
            headers=["Centro", "Demanda"],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[4] Estrutura de custos logísticos\n")

    escrever("• Custo fixo por remessa: $100")
    escrever("• Custo variável: $0,50 por milha percorrida")

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

    escrever("\n[6] Objetivo estratégico\n")

    escrever(
        "O modelo matemático deverá determinar "
        "quantas remessas cada fábrica deve enviar "
        "para cada centro de distribuição."
    )

    escrever(
        "A solução deve minimizar o custo total "
        "de transporte sem violar as restrições "
        "operacionais do problema."
    )

    linha()

    escrever("\n[7] Processamento do modelo\n")

    time.sleep(0)

    escrever("Analisando variáveis logísticas...")
    time.sleep(0)

    escrever("Validando restrições de oferta e demanda...")
    time.sleep(0)

    escrever("Aplicando algoritmo de otimização linear...")
    time.sleep(0)

    escrever("Buscando solução de menor custo operacional...")
    time.sleep(0)

    linha()

    escrever(
        "\nSistema preparado para execução do modelo."
    )

    linha()
