'''
Docstring para equacao10

"Cinco vezes um número somado com 2 é igual ao número multiplicado por 7."

Qual é esse número?
'''

print("Descubra o número:")
print('"Cinco vezes um número somado com 2 é igual ao número multiplicado por 7."\n')

# Usuário digita o número
x = float(input("Digite o número que você acha correto: "))

# Calculando os dois lados da equação
lado_esquerdo = (5 * x) + 2
lado_direito = 7 * x

# Verificação
if lado_esquerdo == lado_direito:
    print("\nOK! Você acertou.")
    print(f"O número é {x}.")
    print(f"Lado esquerdo: {lado_esquerdo}")
    print(f"Lado direito: {lado_direito}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {x}.")
    print(f"Lado esquerdo: {lado_esquerdo}")
    print(f"Lado direito: {lado_direito}")