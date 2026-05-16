'''
“A diferença entre um número e sua terça parte é 20.”
Qual é esse número?
'''

print("Descubra o número:")
print('"A diferença entre um número e sua terça parte é 20."')

# Pedindo resposta do usuário
resposta = int(input("Digite o número que você acha correto: "))

# Calculando a terça parte
terca_parte = resposta / 3

# Calculando a diferença
resultado = resposta - terca_parte

# Verificando se a resposta está correta
if resultado == 20:
    print("\nOK! Você acertou.")
    print(f"O número é {resposta}.")
    print(f"Sua terça parte é {terca_parte}.")
    print(f"A diferença entre eles é {resultado}.")
else:
    print("\nErro! Resposta incorreta.")