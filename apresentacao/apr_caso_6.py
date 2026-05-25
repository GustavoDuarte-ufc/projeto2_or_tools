def apresentar_caso_6():

    print("\n" + "=" * 60)
    print("CASO 6 — PESQUISA DE MERCADO PARA BANCO DIGITAL")
    print("=" * 60)

    print(
        "\nUm banco digital deseja contratar uma empresa para realizar "
        "uma pesquisa de mercado sobre serviços bancários pela internet."
    )

    print(
        "\nO objetivo do modelo é minimizar o custo total de coleta de dados, "
        "garantindo o cumprimento de cotas mínimas exigidas por faixas etárias "
        "e por regiões estratégicas."
    )

    print("\nDADOS PRINCIPAIS DO PROJETO:\n")

    print("• Total de entrevistados exigidos: 2.000 pessoas")
    print("• Cotas mínimas por Faixa Etária:")
    print("  - 18 a 25 anos: 20,0%")
    print("  - 26 a 40 anos: 27,5%")
    print("  - 41 a 50 anos: 15,0%")
    print("  - 51 anos ou mais: 15,0%")
    
    print("\n• Cotas mínimas por Região (Uso de Internet):")
    print("  - Silicon Valley (Alto uso): 15,0%")
    print("  - Big Cities (Médio uso): 35,0%")
    print("  - Small Towns (Baixo uso): 20,0%")

    print("\nMATRIZ DE CUSTOS POR ENTREVISTADO ($):\n")

    # Cabeçalho da tabela de custos
    print(f"{'REGIÃO (REGION)':<20}{'18-25':<10}{'26-40':<10}{'41-50':<10}{'51+'}")
    print("-" * 55)
    print(f"{'Silicon Valley':<20}{'$4.75':<10}{'$6.50':<10}{'$6.50':<10}{'$5.00'}")
    print(f"{'Big Cities':<20}{'$5.25':<10}{'$5.75':<10}{'$6.25':<10}{'$6.25'}")
    print(f"{'Small Towns':<20}{'$6.50':<10}{'$7.50':<10}{'$7.50':<10}{'$7.25'}")

    print("\nOBJETIVO DE NEGÓCIO:\n")

    print(
        "Determinar a combinação ótima de questionários que devem ser "
        "aplicados em cada região e faixa etária para:"
    )

    print("• Cumprir todas as metas demográficas da amostragem")
    print("• Respeitar a distribuição geográfica de amostragem")
    print("• Atingir exatamente o tamanho amostral de 2.000 respondentes")

    print(
        "\nGarantindo a validade estatística da pesquisa com o menor "
        "investimento financeiro possível."
    )