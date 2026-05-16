'''
Docstring para equacao05

"O triplo de um número menos 5 é igual ao dobro do mesmo número mais 1."

Qual é esse número?
'''

print("Descubra o número:")
print('"O triplo de um número menos 5 é igual ao dobro do mesmo número mais 1."\n')

# Usuário digita o número
numero = float(input("Digite o número que você acha correto: "))

# Calculando os dois lados da equação
lado_esquerdo = (3 * numero) - 5
lado_direito = (2 * numero) + 1

# Verificando se está correto
if lado_esquerdo == lado_direito:
    print("\nOK! Você acertou.")
    print(f"O número é {numero}.")
    print(f"Verificação: {lado_esquerdo} = {lado_direito}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {numero}.")
    print(f"Lado esquerdo: {lado_esquerdo}")
    print(f"Lado direito: {lado_direito}")