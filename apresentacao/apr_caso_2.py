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


def apresentar_caso_2():

    linha()

    escrever("AUTOMOTIVE INDUSTRY SOLUTIONS")
    escrever("Planejamento Estratégico de Produção Automotiva")

    linha()

    escrever("\n[1] Contexto do negócio\n")

    escrever(
        "Uma montadora automobilística produz dois "
        "modelos de veículos em sua planta industrial."
    )

    escrever(
        "O desafio operacional consiste em definir "
        "o melhor plano mensal de produção."
    )

    escrever(
        "O objetivo estratégico da companhia é "
        "maximizar o lucro total da operação."
    )

    linha()

    escrever("\n[2] Modelos produzidos\n")

    modelos = [
        ["Family Thrillseeker", "$3.600"],
        ["Classy Cruiser", "$5.400"],
    ]

    print(
        tabulate(
            modelos,
            headers=["Modelo", "Lucro Unitário"],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[3] Recursos produtivos disponíveis\n")

    recursos = [
        ["Horas de trabalho", "48.000 horas/mês"],
        ["Portas disponíveis", "20.000 unidades"],
    ]

    print(
        tabulate(
            recursos,
            headers=["Recurso", "Disponibilidade"],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[4] Consumo de recursos por veículo\n")

    consumo = [
        ["Family Thrillseeker", "6 horas", "4 portas"],
        ["Classy Cruiser", "10,5 horas", "4 portas"],
    ]

    print(
        tabulate(
            consumo,
            headers=[
                "Modelo",
                "Horas por unidade",
                "Portas por unidade"
            ],
            tablefmt="fancy_grid"
        )
    )

    linha()

    escrever("\n[5] Limitações operacionais\n")

    escrever(
        "O modelo Classy Cruiser possui "
        "demanda máxima limitada em 3.500 unidades."
    )

    escrever(
        "O modelo Family Thrillseeker "
        "não possui limite adicional de demanda."
    )

    linha()

    escrever("\n[6] Objetivo estratégico\n")

    escrever(
        "O modelo matemático deverá determinar "
        "quantas unidades de cada veículo devem "
        "ser produzidas."
    )

    escrever(
        "A solução deve maximizar o lucro total "
        "sem ultrapassar os recursos disponíveis."
    )

    linha()

    escrever("\n[7] Processamento analítico\n")

    time.sleep(0)

    escrever("Analisando capacidade produtiva...")
    time.sleep(0)

    escrever("Validando consumo de recursos...")
    time.sleep(0)

    escrever("Aplicando otimização linear...")
    time.sleep(0)

    escrever("Buscando maior rentabilidade operacional...")
    time.sleep(0)

    linha()

    escrever(
        "\nSistema preparado para montagem do modelo matemático."
    )

    linha()