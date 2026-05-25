# main.py

from modelos.caso_1 import caso_1
from apresentacao.apr_caso_1 import apresentar_caso_1

from modelos.caso_2 import caso_2
from apresentacao.apr_caso_2 import apresentar_caso_2

from modelos.caso_3 import caso_3
from apresentacao.apr_caso_3 import apresentar_caso_3

from modelos.caso_4 import caso_4
from apresentacao.apr_caso_4 import apresentar_caso_4

from modelos.caso_5 import caso_5
from apresentacao.apr_caso_5 import apresentar_caso_5

from modelos.caso_6 import caso_6

from montagem.mont_caso_1 import montagem_caso_1
from montagem.mont_caso_2 import montagem_caso_2
from montagem.mont_caso_3 import montagem_caso_3
from montagem.mont_caso_4 import montagem_caso_4
from montagem.mont_caso_5 import montagem_caso_5

from cenarios.cen_caso_2 import *
from cenarios.cen_caso_3 import *
from cenarios.cen_caso_4 import *
from cenarios.cen_caso_5 import *


while True:

    print("\n" + "=" * 60)
    print("SISTEMA DE OTIMIZAÇÃO E PESQUISA OPERACIONAL")
    print("=" * 60)

    print("\nEscolha um caso para resolver:\n")

    print("1. Transporte de Cadeiras Infantis")
    print("2. Planejamento de Produção Automotiva")
    print("3. Redução de Custos da Cafeteria")
    print("4. Escala de Operadores")
    print("5. Planejamento de Produção Têxtil")
    print("6. Pesquisa de Mercado para Banco Digital")
    print("0. Sair")

    escolha = input("\nDigite o número do caso desejado: ")

    # ======================================================
    # CASO 1
    # ======================================================

    if escolha == '1':

        apresentar_caso_1()

        while True:

            print("\nEscolha o próximo passo:\n")

            print("1. Apresentar montagem do modelo")
            print("2. Resolver modelo matemático")
            print("0. Retornar ao menu principal")

            passo = input("\nDigite sua opção: ")

            if passo == '1':
                montagem_caso_1()

            elif passo == '2':
                caso_1()

            elif passo == '0':

                print("\nRetornando ao menu principal...")
                break

            else:
                print("\nOpção inválida. Tente novamente.")

    # ======================================================
    # CASO 2
    # ======================================================

    elif escolha == '2':

        apresentar_caso_2()

        while True:

            print("\n" + "=" * 60)
            print("PLANEJAMENTO DE PRODUÇÃO AUTOMOTIVA")
            print("=" * 60)

            print("\nEscolha uma opção:\n")

            print("1. Montagem do modelo matemático")
            print("2. Resolver cenário base")
            print("3. Cenário 2 — Campanha de Marketing")
            print("4. Cenário 3 — Horas Extras")
            print("5. Cenário 4 — Valor Máximo das Horas Extras")
            print("6. Cenário 5 — Marketing + Horas Extras")
            print("7. Cenário 6 — Viabilidade Econômica")
            print("8. Cenário 7 — Queda do Lucro")
            print("9. Cenário 8 — Aumento do Tempo")
            print("10. Cenário 9 — Demanda Obrigatória")
            print("11. Cenário 10 — Decisão Final")
            print("0. Retornar ao menu principal")

            passo = input("\nDigite sua opção: ")

            if passo == '1':
                montagem_caso_2()

            elif passo == '2':
                caso_2()

            elif passo == '3':
                cenario_2()

            elif passo == '4':
                cenario_3()

            elif passo == '5':
                cenario_4()

            elif passo == '6':
                cenario_5()

            elif passo == '7':
                cenario_6()

            elif passo == '8':
                cenario_7()

            elif passo == '9':
                cenario_8()

            elif passo == '10':
                cenario_9()

            elif passo == '11':
                cenario_10()

            elif passo == '0':

                print("\nRetornando ao menu principal...")
                break

            else:
                print("\nOpção inválida. Tente novamente.")

    # ======================================================
    # CASO 3
    # ======================================================

    elif escolha == '3':

        apresentar_caso_3()

        while True:

            print("\n" + "=" * 60)
            print("REDUÇÃO DE CUSTOS DA CAFETERIA")
            print("=" * 60)

            print("\nEscolha uma opção:\n")

            print("1. Montagem do modelo matemático")
            print("2. Resolver cenário base")
            print("3. Cenário 4 — Redução de Preço")
            print("4. Cenário 5 — Substituição por Feijão-Lima")
            print("5. Cenário 6 — Validação Nutricional")
            print("6. Cenário 7 — Novas Exigências")
            print("0. Retornar ao menu principal")

            passo = input("\nDigite sua opção: ")

            if passo == '1':
                montagem_caso_3()

            elif passo == '2':
                caso_3()

            elif passo == '3':
                cenario_4_caso_3()

            elif passo == '4':
                cenario_5_caso_3()

            elif passo == '5':
                cenario_6_caso_3()

            elif passo == '6':
                cenario_7_caso_3()

            elif passo == '0':

                print("\nRetornando ao menu principal...")
                break

            else:
                print("\nOpção inválida. Tente novamente.")

    # ======================================================
    # CASO 4
    # ======================================================

    elif escolha == '4':

        apresentar_caso_4()

        while True:

            print("\n" + "=" * 60)
            print("ESCALA DE OPERADORES")
            print("=" * 60)

            print("\nEscolha uma opção:\n")

            print("1. Montagem do modelo matemático")
            print("2. Resolver cenário base")
            print("3. Cenário 2 — Limite às 13h")
            print("4. Cenário 3 — Redução de Bilíngues")
            print("5. Cenário 4 — Operadores Bilíngues")
            print("6. Cenário 5 — Aumento da Demanda")
            print("7. Cenário 6 — Redução de Custos")
            print("8. Cenário 7 — Operação Otimizada")
            print("0. Retornar ao menu principal")

            passo = input("\nDigite sua opção: ")

            if passo == '1':

                montagem_caso_4()

            elif passo == '2':

                caso_4()

            elif passo == '3':

                cenario_2_caso_4()

            elif passo == '4':

                cenario_3_caso_4()

            elif passo == '5':

                cenario_4_caso_4()

            elif passo == '6':

                cenario_5_caso_4()

            elif passo == '7':

                cenario_6_caso_4()

            elif passo == '8':

                cenario_7_caso_4()

            elif passo == '0':

                print("\nRetornando ao menu principal...")
                break

            else:

                print("\nOpção inválida. Tente novamente.")

   # ======================================================
    # CASO 5 - PRODUÇÃO DE MODA FEMININA
    # ======================================================
    elif escolha == '5':
        from apresentacao.apr_caso_5 import apresentar_caso_5
        apresentar_caso_5()

        while True:
            print("\n" + "=" * 60)
            print("MENU DE SELEÇÃO DE CENÁRIOS — CASO 5")
            print("=" * 60)
            print("1. Montagem do modelo matemático")
            print("2. Resolver Cenário Base (Itens 1 e 2 - Produção Veludo)")
            print("3. Resolver Item 3 (Veludo Não Devolvível)")
            print("4. Ver Item 4 (Explicação Econômica Intuitiva)")
            print("5. Resolver Item 5 (Aumento de Custo do Blazer_la)")
            print("6. Resolver Item 6 (10.000 Jardas Extras de Acetato)")
            print("7. Resolver Item 7 (Venda de Sobras por 60% em Novembro)")
            print("0. Retornar ao menu principal")

            passo = input("\nDigite sua opção: ")

            if passo == '1':
                from montagem.mont_caso_5 import montagem_caso_5
                montagem_caso_5()
            elif passo == '2':
                from cenarios.cen_caso_5 import cenario_1_e_2_caso_5
                cenario_1_e_2_caso_5()
            elif passo == '3':
                from cenarios.cen_caso_5 import cenario_3_caso_5
                cenario_3_caso_5()
            elif passo == '4':
                from cenarios.cen_caso_5 import cenario_4_caso_5
                cenario_4_caso_5()
            elif passo == '5':
                from cenarios.cen_caso_5 import cenario_5_caso_5
                cenario_5_caso_5()
            elif passo == '6':
                from cenarios.cen_caso_5 import cenario_6_caso_5
                cenario_6_caso_5()
            elif passo == '7':
                from cenarios.cen_caso_5 import cenario_7_caso_5
                cenario_7_caso_5()
            elif passo == '0':
                print("\nRetornando ao menu principal...")
                break
            else:
                print("\nOpção inválida. Tente novamente.")
            
    # ======================================================
    # CASO 6
    # ======================================================
    elif escolha == '6':
        from apresentacao.apr_caso_6 import apresentar_caso_6
        apresentar_caso_6()

        while True:
            print("\n" + "=" * 60)
            print("PESQUISA DE MERCADO — MENU DE CENÁRIOS")
            print("=" * 60)

            print("\nEscolha uma opção baseada nos Itens da Imagem:\n")
            print("1. Ver Montagem Teórica do Modelo")
            print("2. Resolver Item 1 & 2 (Cenário Base + Lance de 15%)")
            print("3. Resolver Item 3 (Mínimo de 50 pessoas por Célula)")
            print("4. Resolver Item 4 (Limites Máximos de Cap de Cobertura)")
            print("5. Resolver Item 5 (Tabela de Custos Fixados por Região)")
            print("6. Resolver Item 6 (Cotas com Percentuais Fixos por População)")
            print("0. Retornar ao menu principal")

            passo = input("\nDigite sua opção: ")

            if passo == '1':
                from montagem.mont_caso_6 import montagem_caso_6
                montagem_caso_6()
            elif passo == '2':
                from cenarios.cen_caso_6 import cenario_1_e_2_caso_6
                cenario_1_e_2_caso_6()
            elif passo == '3':
                from cenarios.cen_caso_6 import cenario_3_caso_6
                cenario_3_caso_6()
            elif passo == '4':
                from cenarios.cen_caso_6 import cenario_4_caso_6
                cenario_4_caso_6()
            elif passo == '5':
                from cenarios.cen_caso_6 import cenario_5_caso_6
                cenario_5_caso_6()
            elif passo == '6':
                from cenarios.cen_caso_6 import cenario_6_caso_6
                cenario_6_caso_6()
            elif passo == '0':
                print("\nRetornando ao menu principal...")
                break
            else:
                print("\nOpção inválida. Tente novamente.")

    # ======================================================
    # SAIR
    # ======================================================

    elif escolha == '0':

        print("\nEncerrando sistema...")
        break

    else:

        print("\nOpção inválida. Tente novamente.")