'''
Docstring para equacao08

"Quatro vezes um número subtraído de 8 é igual a 28."

Qual é esse número?
'''

print("Descubra o número:")
print('"Quatro vezes um número subtraído de 8 é igual a 28."\n')

# Usuário digita o número
numero = float(input("Digite o número que você acha correto: "))

# Calculando a expressão
resultado = (4 * numero) - 8

# Verificação
if resultado == 28:
    print("\nOK! Você acertou.")
    print(f"O número é {numero}.")
    print(f"Verificação: (4 * {numero}) - 8 = {resultado}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {numero}.")
    print(f"O resultado foi {resultado}, não 28.")