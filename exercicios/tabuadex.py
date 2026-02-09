import random


print(80 * "_")
print("Bem-vindo ao Tabuadex")
print(80 * "_")
print("Esse é um jogo de matemática onde você ganha 10 pontos acertando cada conta\nE você tem 10 rodadas se não decidir sair")
totaldepontos = 0
numrodadas = 10

for rodada in range(numrodadas):
    numeros = random.randint(1, 50)
    numeros1 = random.randint(1, 50)
    operacao = '*'
    problema = f'{numeros1} {operacao} {numeros}'
    conta = int(input(f"Quanto é \n{problema} = "))

    if eval(problema) == float(conta):
        print("Acertou")
        totaldepontos += 10
        print(f"Pontos: {totaldepontos}")
    else:
        print(f"Errou, a resposta correta é {eval(problema)}")
        print(80 * "_")


    sair = input("Deseja:\n1) Continuar\n2) Sair\n>> ")

    if sair == '2':
        print('Obrigada por utilizar a Tabuadex, volte sempre!')
        break
    elif sair == '1':
        print('Boa escolha')
        print(80 * "_")
        continue
print(f"Jogo finalizado. Pontuação total: {totaldepontos}")
