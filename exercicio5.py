# Solicita o salário do funcionário
salario_antigo = float(input("Digite o salário do funcionário: R$ "))

# Calcula o novo salário com aumento de 15%
aumento = salario_antigo * 0.15
salario_novo = salario_antigo + aumento

# Exibe os resultados
print(f"Salário antigo: R$ {salario_antigo:.2f}")
print(f"Novo salário após o reajuste de 15%: R$ {salario_novo:.2f}")