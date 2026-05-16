'''
Docstring para equacao06

"A soma de dois números consecutivos é 47."

Qual é o primeiro número?
'''

print("Descubra os números:")
print('"A soma de dois números consecutivos é 47."\n')

# Usuário digita o primeiro número
numero1 = int(input("Digite o primeiro número: "))

# Número consecutivo
numero2 = numero1 + 1

# Soma
soma = numero1 + numero2

# Verificação
if soma == 47:
    print("\nOK! Você acertou.")
    print(f"Os números são {numero1} e {numero2}.")
    print(f"A soma é {soma}.")
else:
    print("\nErro! Resposta incorreta.")
    print(f"Você testou {numero1} e {numero2}.")
    print(f"A soma deu {soma}, não 47.")