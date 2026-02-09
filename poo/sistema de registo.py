import random


class Aluno:

    quantidade_alunos = 0

    def __init__(self, nome, idade, curso, n_matricula):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.n_matricula = n_matricula
        Aluno.quantidade_alunos += 1

    def __str__(self):
        return f"Nome: {self.nome}| Idade: {self.idade}| Curso: {self.curso}| Número de Matrícula: {self.n_matricula}"


def adicionaraluno():

    nome = str(input("introduza o seu nome\n>>"))
    idade = int(input("introduza sua idade\n>>"))
    curso = str(input("qual curso você está realizando\n>>"))
    n_matricula = random.randint(1, 100)
    print(f"numero de matricula:{n_matricula}")
    return Aluno(nome, idade, curso, n_matricula)


def menu():
    print("Escolha uma opção digitando o numero (1, 2 e 3):")
    print("1)Criar novo aluno")
    print("2)Exibir informações de aluno")
    print("3)Sair")


def exibiraluno(aluno):
    print(aluno)
    print(80 * '_')


def main():
    alunos = []
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")
        if opcao == '1' and 'criar novo aluno':
            aluno = adicionaraluno()
            alunos.append(aluno)
            print("Aluno criado com sucesso!")
            print(80*'_')
        elif opcao == '2' and 'exibir infomarções de aluno':
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in alunos:
                    print("aluno:", end=' ')
                    exibiraluno(aluno)
        elif opcao == '3' and 'sair':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
