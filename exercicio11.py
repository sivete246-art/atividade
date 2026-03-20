# Cria uma lista de produtos
produtos = ["po", "maconha", "coca", "skunk", "crack"]

# Solicita ao usuário o nome de um produto
produto_buscado = input("Digite o nome do produto que deseja buscar: ")

# Verifica se o produto está na lista
if produto_buscado in produtos:
    print(f"O produto '{produto_buscado}' está na lista.")
else:
    print(f"O produto '{produto_buscado}' não está na lista.")