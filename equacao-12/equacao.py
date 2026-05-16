'''
Docstring para equacao12

"Qual é o número cujo quádruplo subtraído de 5 dá o mesmo que seu dobro somado com 11?"
'''

print("Descubra o número:")
print('"O quádruplo de um número menos 5 é igual ao seu dobro mais 11."\n')

# Usuário digita o número
x = float(input("Digite o número que você acha correto: "))

# Calculando os dois lados da equação
lado_esquerdo = (4 * x) - 5
lado_direito = (2 * x) + 11

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