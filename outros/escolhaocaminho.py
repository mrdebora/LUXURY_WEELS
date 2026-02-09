def caminho():
    print(80*"_")
    print("Bem-vindo à Escolha do Caminho!")
    print("Você tem três opções de caminho:")
    print("1)caminhoA")
    print("2)caminhoB")
    print("3)caminhoC")
    escolha = input("Por favor, escolha um dos caminhos digitando o nome,numero ou a letra correspondente (A, B, C)\n>>")

    if escolha == 'A' or escolha == 'caminhoA' or escolha == "1":
        print("Você escolheu o caminhoA: É um caminho seguro e tranquilo!")
    elif escolha == 'B' or escolha == 'caminhoB' or escolha == "2":
        print("Você escolheu o caminhoB: É um caminho misterioso e cheio de aventuras!")
    elif escolha == 'C' or escolha == 'caminhoC' or escolha == "3":
        print("Você escolheu o caminhoC: É um caminho desafiador e recompensador!")
    else:
        print("Escolha inválida. Por favor, tente novamente.")


caminho()
