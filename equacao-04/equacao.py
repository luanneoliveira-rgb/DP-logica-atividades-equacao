'''
Docstring para equacao04

“Multiplique um número por 3 e subtraia 9.
O resultado é igual ao próprio número.”

Qual é esse número?
'''

print("Descubra o número:")
print('"Multiplique um número por 3 e subtraia 9. O resultado é igual ao próprio número."\n')

# Usuário tenta adivinhar o número
numero = float(input("Digite o número que você acha correto: "))

# Calculando a expressão do problema
resultado = (3 * numero) - 9

# Verificando se está correto
if resultado == numero:
    print("\nOK! Você acertou.")
    print(f"O número é {numero}.")
    print(f"Verificação: (3 * {numero}) - 9 = {resultado}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {numero}, mas o resultado foi {resultado}.")