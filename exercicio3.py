# Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# Conta o número de caracteres (incluindo espaços)
quantidade_caracteres = len(nome_completo)

# Exibe o nome em letras maiúsculas
nome_maiusculo = nome_completo.upper()

# Mostra os resultados
print(f"Seu nome possui {quantidade_caracteres} caracteres (incluindo espaços).")
print(f"Seu nome em letras maiúsculas: {nome_maiusculo}")