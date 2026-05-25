def apresentar_caso_5():

    print("\n" + "=" * 60)
    print("CASO 5 — PLANEJAMENTO DE PRODUÇÃO TÊXTIL")
    print("=" * 60)

    print(
        "\nUma indústria têxtil precisa planejar sua estratégia "
        "de produção para o próximo mês, maximizando o lucro total "
        "da fábrica sob limites rígidos de recursos e demanda."
    )

    print(
        "\nO objetivo do projeto é determinar o mix ideal de produtos "
        "(camisetas, calças e jaquetas) a serem fabricados, "
        "respeitando a disponibilidade de matéria-prima e horas de mão de obra."
    )

    print("\nDADOS OPERACIONAIS (POR UNIDADE):\n")

    print("• Camisetas:")
    print("  - Tecido necessário: 1.5 m²")
    print("  - Tempo de costura/acabamento: 0.5 horas")
    print("  - Lucro unitário: US$ 15.00")
    
    print("\n• Calças:")
    print("  - Tecido necessário: 2.5 m²")
    print("  - Tempo de costura/acabamento: 1.2 horas")
    print("  - Lucro unitário: US$ 28.00")

    print("\n• Jaquetas:")
    print("  - Tecido necessário: 4.0 m²")
    print("  - Tempo de costura/acabamento: 2.0 horas")
    print("  - Lucro unitário: US$ 45.00")

    print("\nDISPONIBILIDADE DE RECURSOS (MENSAL):\n")

    print("• Estoque Máximo de Tecido: 12.000 m²")
    print("• Capacidade de Mão de Obra (Costura): 4.500 horas")

    print("\nRESTRIÇÕES DE MERCADO (DEMANDA MÍNIMA OBRIGATÓRIA):\n")

    tabela = [
        ("Camisetas", 1000, "Unidades"),
        ("Calças", 500, "Unidades"),
        ("Jaquetas", 200, "Unidades"),
    ]

    print(f"{'PRODUTO':<20}{'DEMANDA MÍNIMA':<20}{'UNIDADE'}")
    print("-" * 50)

    for produto, demanda, unidade in tabela:
        print(f"{produto:<20}{demanda:<20}{unidade}")

    print("\nOBJETIVO DE NEGÓCIO:\n")

    print(
        "Determinar a quantidade exata de cada produto "
        "que deve ser fabricada para:"
    )

    print("• Consumir eficientemente o estoque de tecido")
    print("• Otimizar o uso das horas de costura disponíveis")
    print("• Atender aos contratos mínimos de entrega de mercado")

    print(
        "\nGarantindo a máxima rentabilidade financeira "
        "para a operação têxtil."
    )

    