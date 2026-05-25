def montagem_caso_3():

    print("\n" + "=" * 60)
    print("MONTAGEM DO MODELO MATEMÁTICO")
    print("=" * 60)

    print("\nVARIÁVEIS DE DECISÃO")
    print("-" * 60)

    print(
        "\nx1 = quantidade de batata utilizada "
        "(em libras)"
    )

    print(
        "x2 = quantidade de vagem utilizada "
        "(em libras)"
    )

    print("\nFUNÇÃO OBJETIVO")
    print("-" * 60)

    print(
        "\nMinimizar o custo total semanal "
        "da produção."
    )

    print("\nMin Z = 0.40x1 + 1.00x2")

    print("\nRESTRIÇÕES NUTRICIONAIS")
    print("-" * 60)

    print("\nProteína mínima:")

    print(
        "1.5x1 + 5.67x2 >= 180"
    )

    print("\nFerro mínimo:")

    print(
        "0.3x1 + 3.402x2 >= 80"
    )

    print("\nVitamina C mínima:")

    print(
        "12x1 + 28.35x2 >= 1050"
    )

    print("\nRESTRIÇÕES OPERACIONAIS")
    print("-" * 60)

    print("\nRazão mínima batata:vagem = 6:5")

    print(
        "5x1 - 6x2 >= 0"
    )

    print("\nProdução mínima semanal:")

    print(
        "x1 + x2 >= 10"
    )

    print("\nNÃO NEGATIVIDADE")
    print("-" * 60)

    print("\nx1 >= 0")
    print("x2 >= 0")

    print("\nINTERPRETAÇÃO EXECUTIVA")
    print("-" * 60)

    print(
        "\nO modelo busca identificar a combinação "
        "de ingredientes com menor custo possível."
    )

    print(
        "As restrições garantem que os requisitos "
        "nutricionais e operacionais sejam atendidos."
    )

    print("\n" + "=" * 60)