'''
Docstring para equacao07

"Sua metade mais 7 é igual a 19."

Qual número atende a esse critério?
'''

print("Descubra o número:")
print('"Sua metade mais 7 é igual a 19."\n')

# Usuário digita o número
numero = float(input("Digite o número que você acha correto: "))

# Calculando a expressão
resultado = (numero / 2) + 7

# Verificação
if resultado == 19:
    print("\nOK! Você acertou.")
    print(f"O número é {numero}.")
    print(f"Verificação: ({numero}/2) + 7 = {resultado}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {numero}.")
    print(f"O resultado foi {resultado}, não 19.")