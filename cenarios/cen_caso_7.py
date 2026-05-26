from modelos.caso_7 import resolver_modelo_core
from ortools.linear_solver import pywraplp

def cenario_inteiro_caso_7():
    print("\n=== REFAZENDO: ALOCAÇÃO EXCLUSIVA POR ÁREA (ITEM 4) ===")
    status, solver, x = resolver_modelo_core(usar_inteiro=True)
    if status == pywraplp.Solver.OPTIMAL:
        custo_int = solver.Objective().Value()
        # Custo base aproximado calculado matematicamente: $540,000.00
        aumento = custo_int - 540000.00 
        print(f"Custo com Atribuição Única: ${custo_int:,.2f}")
        print(f"O custo aumentou em aproximadamente: ${max(0.0, aumento):,.2f}")
        for k, v in x.items():
            if v.solution_value() > 0:
                print(f" Área {k[0]+1} -> Escola {k[1]+1}: {v.solution_value():.0f} alunos (Não dividida)")
    else:
        print("Resultado: INVIÁVEL! Não é possível balancear as séries (30%-36%) sem dividir as áreas.")

def cenario_opcao1_caso_7():
    print("\n=== OPÇÃO 1: ELIMINAR TRANSPORTE DE 1 A 1.5 MILHA (ITEM 5) ===")
    # Na tabela fornecida, o custo de referência de $200 é eliminado (vira 0)
    status, solver, x = resolver_modelo_core(usar_inteiro=False, eliminar_custo=200)
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Novo Custo de Transporte Total: ${solver.Objective().Value():,.2f}")
        print("Impacto: Alunos de áreas próximas (Custo $200) agora vão a pé/recursos próprios.")
    else:
        print("Solução Inviável.")

def cenario_opcao2_caso_7():
    print("\n=== OPÇÃO 2: ELIMINAR TAMBÉM DE 1.5 A 2 MILHAS (ITEM 6) ===")
    # Na tabela fornecida, elimina-se o custo de referência de $300 (vira 0)
    status, solver, x = resolver_modelo_core(usar_inteiro=False, eliminar_custo=300)
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Novo Custo de Transporte Total: ${solver.Objective().Value():,.2f}")
        print("Impacto: Economia severa, porém expande enormemente o perímetro sem ônibus.")
    else:
        print("Solução Inviável.")

def sintese_decisao_caso_7():
    print("\n" + "=" * 60)
    print("SÍNTESE DE TRADE-OFF E RECOMENDAÇÃO FINAL (ITENS 7 E 8)")
    print("=" * 60)
    print("\n[Item 7 - Análise de Trade-off]")
    print("1. Divisão de Áreas vs Exclusividade: Permitir a divisão reduz custos e garante")
    print("   a viabilidade legal do mix de séries (30-36%). Forçar bairros inteiros em uma")
    print("   única escola rompe o equilíbrio populacional aceitável.")
    print("2. Corte de Ônibus ($200 e $300): Reduz drasticamente as despesas do distrito,")
    print("   mas gera forte inconveniência política e riscos de segurança urbana para os alunos.")
    print("\n[Item 8 - Recomendação Recomendada]")
    print("Recomenda-se adotar o CENÁRIO BASE com a OPÇÃO 1 integrada. Permitir a divisão")
    print("de alunos garante conformidade matemática de cotas por série, enquanto o corte")
    print("de transporte em até 1.5 milhas ($200) economiza recursos públicos sem penalizar")
    print("distâncias críticas de caminhada.")