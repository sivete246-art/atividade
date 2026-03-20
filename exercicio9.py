# Define a senha correta
senha_correta = "viadinho69"

# Solicita a senha ao usuário
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso Garantido")
        break
    else:
        print("Senha Incorreta")