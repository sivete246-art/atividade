preco = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
desconto = preco * (percentual_desconto / 100)
novo_preco = preco - desconto
print(f"O novo preço com desconto é: R$ {novo_preco:.2f}")