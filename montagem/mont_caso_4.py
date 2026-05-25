# montagem/mont_caso_4.py

def montagem_caso_4():

    print("\n" + "=" * 60)
    print("MONTAGEM DO MODELO MATEMÁTICO — CASO 4")
    print("=" * 60)

    print("\nOBJETIVO:")
    print(
        "Determinar a quantidade ideal de operadores "
        "integrais e parciais para minimizar custos "
        "e atender toda a demanda telefônica."
    )

    print("\n" + "-" * 60)
    print("VARIÁVEIS DE DECISÃO")
    print("-" * 60)

    print(
        """
x_it = operadores integrais de inglês iniciando no telefone
x_ia = operadores integrais de inglês iniciando no administrativo

x_st = operadores integrais de espanhol iniciando no telefone
x_sa = operadores integrais de espanhol iniciando no administrativo

p_t = operadores parciais
"""
    )

    print("\n" + "-" * 60)
    print("FUNÇÃO OBJETIVO")
    print("-" * 60)

    print(
        """
Minimizar:

Custo Total =
Σ operadores integrais
+
Σ operadores parciais
"""
    )

    print("\n" + "-" * 60)
    print("RESTRIÇÕES")
    print("-" * 60)

    print(
        """
1. Atender demanda mínima de chamadas
2. Garantir 20% da operação em espanhol
3. Respeitar horários de trabalho
4. Funcionários integrais alternam:
   - 4h telefone
   - 4h administrativo
5. Funcionários parciais trabalham apenas telefone
6. Todos os valores devem ser inteiros
"""
    )

    print("\n" + "-" * 60)
    print("EXEMPLO DE RESTRIÇÃO")
    print("-" * 60)

    print(
        """
Período 7h–9h:

Operadores inglês >= '80%' da demanda
Operadores espanhol >= '20%' da demanda
"""
    )

    print("\nModelo matemático estruturado com sucesso.\n")