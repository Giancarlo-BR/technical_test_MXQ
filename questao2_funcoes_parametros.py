"""
Questão 2 — Funções e parâmetros
Analise a função abaixo e responda: ela funciona corretamente?
Se sim, o que ela retorna para as chamadas indicadas?
Se houver algum problema, aponte e sugira uma correção.
"""


def somar(a, b=10):
    return a + b


# Chamada 1
print(somar(5))        # Saída: 15

# Chamada 2
print(somar(5, 3))     # Saída: 8

# Chamada 3
print(somar(b=2, a=4)) # Saída: 6


"""
RESPOSTA:

Sim, a função funciona corretamente. Não há nenhum problema.

A função 'somar' recebe dois parâmetros:
  - 'a': obrigatório (não tem valor padrão)
  - 'b': opcional, com valor padrão de 10

Resultado de cada chamada:
  - somar(5)        → a=5, b=10 (usa valor padrão) → retorna 15
  - somar(5, 3)     → a=5, b=3 (valor padrão sobrescrito) → retorna 8
  - somar(b=2, a=4) → a=4, b=2 (argumentos nomeados, ordem não importa) → retorna 6
"""
