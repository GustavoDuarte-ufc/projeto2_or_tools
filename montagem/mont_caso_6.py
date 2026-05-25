def montagem_caso_6():

    print("\n" + "=" * 60)
    print("MONTAGEM DO MODELO MATEMÁTICO — CASO 6")
    print("=" * 60)

    print("\nOBJETIVO:")
    print(
        "Determinar a quantidade ideal de entrevistados por região "
        "e faixa etária, minimizando o custo total da coleta de dados "
        "e cumprindo todas as cotas exigidas."
    )

    print("\n" + "-" * 60)
    print("VARIÁVEIS DE DECISÃO")
    print("-" * 60)

    print(
        """
A matriz de decisão cruza 3 Regiões com 4 Faixas Etárias:

x_sv_18 = Entrevistados em Silicon Valley, de 18 a 25 anos
x_sv_26 = Entrevistados em Silicon Valley, de 26 a 40 anos
x_sv_41 = Entrevistados em Silicon Valley, de 41 a 50 anos
x_sv_51 = Entrevistados em Silicon Valley, com 51 anos ou mais

x_bc_18 = Entrevistados em Big Cities, de 18 a 25 anos
x_bc_26 = Entrevistados em Big Cities, de 26 a 40 anos
x_bc_41 = Entrevistados em Big Cities, de 41 a 50 anos
x_bc_51 = Entrevistados em Big Cities, com 51 anos ou mais

x_st_18 = Entrevistados em Small Towns, de 18 a 25 anos
x_st_26 = Entrevistados em Small Towns, de 26 a 40 anos
x_st_41 = Entrevistados em Small Towns, de 41 a 50 anos
x_st_51 = Entrevistados em Small Towns, com 51 anos ou mais
"""
    )

    print("\n" + "-" * 60)
    print("FUNÇÃO OBJETIVO")
    print("-" * 60)

    print(
        """
Minimizar Custo Total =
  4.75*x_sv_18 + 6.50*x_sv_26 + 6.50*x_sv_41 + 5.00*x_sv_51 +
  5.25*x_bc_18 + 5.75*x_bc_26 + 6.25*x_bc_41 + 6.25*x_bc_51 +
  6.50*x_st_18 + 7.50*x_st_26 + 7.50*x_st_41 + 7.25*x_st_51
"""
    )

    print("\n" + "-" * 60)
    print("RESTRIÇÕES DO MODELO")
    print("-" * 60)

    print(
        """
1. Total de Amostras Obrigatório:
   Soma de todas as variáveis = 2.000

2. Cotas Mínimas por Faixa Etária (Sobre o total de 2.000):
   • 18 a 25 anos: Soma(x_r_18) >= 400 (20%)
   • 26 a 40 anos: Soma(x_r_26) >= 550 (27,5%)
   • 41 a 50 anos: Soma(x_r_41) >= 300 (15%)
   • 51 ou mais:  Soma(x_r_51) >= 300 (15%)

3. Cotas Mínimas por Região (Sobre o total de 2.000):
   • Silicon Valley: Soma(x_sv_e) >= 300 (15%)
   • Big Cities:     Soma(x_bc_e) >= 700 (35%)
   • Small Towns:    Soma(x_st_e) >= 400 (20%)

4. Condições de Não-Negatividade e Integralidade:
   Todas as variáveis x >= 0 e devem ser valores inteiros.
"""
    )

    print("\n" + "-" * 60)
    print("EXEMPLO DE CÁLCULO DE COTA (MATRIZ)")
    print("-" * 60)

    print(
        """
Para a Região 'Big Cities', a soma de todas as idades entrevistadas
naquela região deve cobrir pelo menos 35% do projeto:

x_bc_18 + x_bc_26 + x_bc_41 + x_bc_51 >= 700
"""
    )

    print("\nModelo matemático estruturado com sucesso.\n")