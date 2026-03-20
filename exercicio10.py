# Solicita ao usuário 5 números e armazena em uma lista
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Calcula o maior, menor e a média
maior = numeros[0]
menor = numeros[0]
soma = 0

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero

media = soma / len(numeros)

# Exibe os resultados
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média aritmética: {media:.2f}")