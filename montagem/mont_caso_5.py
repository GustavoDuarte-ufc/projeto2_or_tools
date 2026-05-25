def montagem_caso_5():

    print("\n" + "=" * 60)
    print("MONTAGEM DO MODELO MATEMÁTICO — CASO 5")
    print("=" * 60)

    print("\nOBJETIVO:")
    print(
        "Determinar o mix ótimo de produção mensal (Camisetas, Calças "
        "e Jaquetas) para maximizar o lucro total, respeitando a "
        "disponibilidade de matéria-prima, mão de obra e demandas de mercado."
    )

    print("\n" + "-" * 60)
    print("VARIÁVEIS DE DECISÃO")
    print("-" * 60)

    print(
        """
x1 = Quantidade de Camisetas a produzir (unidades)
x2 = Quantidade de Calças a produzir (unidades)
x3 = Quantidade de Jaquetas a produzir (unidades)
"""
    )

    print("\n" + "-" * 60)
    print("FUNÇÃO OBJETIVO")
    print("-" * 60)

    print(
        """
Maximizar o Lucro Total (Z):

Z = 15.00 * x1 + 28.00 * x2 + 45.00 * x3
"""
    )

    print("\n" + "-" * 60)
    print("RESTRIÇÕES DO SISTEMA")
    print("-" * 60)

    print(
        """
1. Matéria-Prima (Disponibilidade de Tecido):
   1.5 * x1 + 2.5 * x2 + 4.0 * x3 <= 12.000 m²

2. Mão de Obra (Capacidade de Costura):
   0.5 * x1 + 1.2 * x2 + 2.0 * x3 <= 4.500 horas

3. Mercado (Contratos e Demandas Mínimas):
   x1 >= 1.000 (Camisetas)
   x2 >= 500   (Calças)
   x3 >= 200   (Jaquetas)

4. Não-Negatividade e Integralidade:
   x1, x2, x3 >= 0 e devem ser valores inteiros
"""
    )

    print("\n" + "-" * 60)
    print("ANÁLISE DE PRODUTIVIDADE (LUCRO POR HORA)")
    print("-" * 60)

    print(
        """
• Camisetas : US$ 15.00 / 0.5h = US$ 30.00 por hora
• Calças    : US$ 28.00 / 1.2h = US$ 23.33 por hora
• Jaquetas  : US$ 45.00 / 2.0h = US$ 22.50 por hora

Nota: Embora as Jaquetas deem o maior lucro absoluto por peça,
as Camisetas trazem o melhor retorno por hora de dedicação!
O Solver calibrará o balanço perfeito entre tecido e tempo.
"""
    )

    print("\nModelo matemático estruturado com sucesso.\n")