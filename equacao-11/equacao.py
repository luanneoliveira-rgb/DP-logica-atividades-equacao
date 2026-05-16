'''
Docstring para equacao11

"Um número somado ao triplo de seu sucessor resulta em 74."

Qual é esse número?
'''

print("Descubra o número:")
print('"Um número somado ao triplo de seu sucessor resulta em 74."\n')

# Usuário digita o número
x = float(input("Digite o número que você acha correto: "))

# Sucessor do número
sucessor = x + 1

# Calculando a expressão
resultado = x + (3 * sucessor)

# Verificação
if resultado == 74:
    print("\nOK! Você acertou.")
    print(f"O número é {x}.")
    print(f"Sucessor: {sucessor}")
    print(f"Resultado da expressão: {resultado}")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {x}.")
    print(f"Resultado da expressão foi {resultado}, não 74.")