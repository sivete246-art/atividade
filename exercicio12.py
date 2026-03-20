class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


# Método principal
if __name__ == "__main__":
    # Solicita os dados do aluno
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    notas = []

    for i in range(3):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)

    # Cria uma instância de Aluno
    aluno = Aluno(nome, idade, notas)

    # Calcula a média e verifica aprovação
    media = aluno.calcular_media()
    status = aluno.verificar_aprovacao()

    # Exibe os resultados
    print(f"\nAluno: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Média Final: {media:.2f}")
    print(f"Status: {status}")