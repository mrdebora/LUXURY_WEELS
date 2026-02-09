class Animal:
    def __init__(self, nome, som):
        self._nome = nome
        self.som = som

    def som_animal(self):
        return f"O Animal {self._nome} faz o som {self.som}"


def nome_gato():
    print(80*"_")
    recebergato = input("digite o nome que deseja colocar no seu Gato \n>>")
    gato1 = Animal(f"{recebergato}", "MIU MIU")
    print(f"O seu GATO {recebergato} emite o som {gato1.som}")
    print(f"O {recebergato} está miando.")
    return Animal.som_animal(gato1)


def nome_cachorro():
    print(80 * "_")
    recebercachorro = input("digite o nome que deseja colocar no seu cachorro\n>>")
    cachorro = Animal(f"{recebercachorro}", "AU AU")
    print(f"O seu CACHORRO {recebercachorro} emite o som {cachorro.som}")
    print(f"O {recebercachorro} está latindo.")
    return Animal.som_animal


def main():
    opcao = int(input("digite o numero (1 e 2) do animal que você deseja escolher\n1)Gato\n2)Cachorro\n>>"))
    if opcao == 1:
        print("você escolhe o gato!")
        nome_gato()
    elif opcao == 2:
        print("você escolheu o cachorro!")
        nome_cachorro()
    else:
        print("opção inválida!")
        return


main()
