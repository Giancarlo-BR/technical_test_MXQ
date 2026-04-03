"""
Questão 1 — Listas e loops
Dado o código abaixo, o que será impresso no terminal? Explique o que cada linha faz.
"""

# Cria uma lista com os números de 1 a 6
numeros = [1, 2, 3, 4, 5, 6]

# Cria uma lista vazia que vai armazenar os resultados
resultado = []

for n in numeros:
    # Verifica se o número é par (resto da divisão por 2 igual a zero)
    if n % 2 == 0:
        # Se for par, multiplica por 2 e adiciona à lista 'resultado'
        resultado.append(n * 2)

# Exibe a lista resultado no terminal
print(resultado)

"""
RESPOSTA:

Será impresso: [4, 8, 12], a função apenas pega os números no loop que são pares e multiplicam por 2 na lista "resultado"

"""
