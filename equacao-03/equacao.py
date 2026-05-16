'''
Docstring para equacao03

Três amigos somaram suas idades.
João tem o dobro da idade de Pedro.
Carlos tem a mesma idade de Pedro.
A soma das idades é 60 anos.

Qual é a idade de cada um?
'''

print("Descubra as idades:")
print("João tem o dobro da idade de Pedro.")
print("Carlos tem a mesma idade de Pedro.")
print("A soma das idades é 60 anos.\n")

# Usuário digita a idade de Pedro
idade_pedro = int(input("Digite a idade de Pedro: "))

# Calculando as outras idades
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro

# Soma das idades
soma_idades = idade_pedro + idade_joao + idade_carlos

# Verificando se está correto
if soma_idades == 60:
    print("\nOK! Você acertou.")
    print(f"Pedro tem {idade_pedro} anos.")
    print(f"João tem {idade_joao} anos.")
    print(f"Carlos tem {idade_carlos} anos.")
    print(f"A soma das idades é {soma_idades} anos.")
else:
    print("\nErro! Resposta incorreta.")