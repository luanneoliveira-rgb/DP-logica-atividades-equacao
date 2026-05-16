'''
Docstring para equacao09

"O quádruplo de um número mais 10 é igual ao triplo do mesmo número mais 22."

Qual é esse número?
'''

print("Descubra o número:")
print('"O quádruplo de um número mais 10 é igual ao triplo do mesmo número mais 22."\n')

# Usuário digita o número
numero = float(input("Digite o número que você acha correto: "))

# Calculando os dois lados da equação
lado_esquerdo = (4 * numero) + 10
lado_direito = (3 * numero) + 22

# Verificação
if lado_esquerdo == lado_direito:
    print("\nOK! Você acertou.")
    print(f"O número é {numero}.")
    print(f"Lado esquerdo: {lado_esquerdo}")
    print(f"Lado direito: {lado_direito}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {numero}.")
    print(f"Lado esquerdo: {lado_esquerdo}")
    print(f"Lado direito: {lado_direito}")