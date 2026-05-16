# Descubra o número:
# "Um número somado ao seu dobro resulta em 36."

print("Descubra o número:")
print('"Um número somado ao seu dobro resulta em 36."')

# Pedindo resposta do usuário
resposta = int(input("Digite o número que você acha correto: "))

# Verificando se a resposta está certa
if resposta + (2 * resposta) == 36:
    print("OK! Você acertou.")
    print(f"O número é {resposta}.")
else:
    print("Erro! Resposta incorreta.")