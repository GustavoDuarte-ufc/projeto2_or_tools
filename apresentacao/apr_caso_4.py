# apresentacao/apr_caso_4.py

def apresentar_caso_4():

    print("\n" + "=" * 60)
    print("CASO 4 — ESCALA DE OPERADORES EM CENTRAL")
    print("=" * 60)

    print(
        "\nUm hospital deseja estruturar "
        "uma central de atendimento telefônico "
        "para agendamentos e registros."
    )

    print(
        "\nO objetivo do projeto é definir "
        "a escala ótima de operadores "
        "minimizando custo operacional "
        "e garantindo o nível de serviço."
    )

    print("\nDADOS OPERACIONAIS:\n")

    print("• Funcionamento: 7h às 21h")
    print("• Divisão em períodos de 2 horas")
    print("• Cada operador atende 6 chamadas por hora")
    print("• 20% das chamadas exigem espanhol")
    print("• Operadores integrais:")
    print("  - trabalham 8h")
    print("  - 4h no telefone")
    print("  - 4h em tarefas administrativas")

    print("\nHORÁRIOS DE ENTRADA:\n")

    print("• Integrais: 7h, 9h, 11h e 13h")
    print("• Parciais: 15h e 17h")

    print("\nDEMANDA DE CHAMADAS:\n")

    tabela = [
        ("7h - 9h", 40),
        ("9h - 11h", 85),
        ("11h - 13h", 70),
        ("13h - 15h", 95),
        ("15h - 17h", 80),
        ("17h - 19h", 35),
        ("19h - 21h", 10),
    ]

    print(f"{'PERÍODO':<20}{'CHAMADAS/HORA'}")
    print("-" * 40)

    for periodo, chamadas in tabela:

        print(f"{periodo:<20}{chamadas}")

    print("\nCUSTOS OPERACIONAIS:\n")

    print("• Até 17h: US$ 10/h")
    print("• Após 17h: US$ 12/h")

    print("\nOBJETIVO DE NEGÓCIO:\n")

    print(
        "Determinar automaticamente "
        "a melhor combinação entre:"
    )

    print("• Operadores integrais")
    print("• Operadores parciais")
    print("• Operadores inglês")
    print("• Operadores espanhol")

    print(
        "\nGarantindo o menor custo "
        "operacional possível."
    )

    