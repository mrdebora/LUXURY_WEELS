class Veiculo:
    def __init__(self, marca, ano):
        self._marca = marca
        self._ano = ano

    def info(self):
        print(f'|Marca:{self._marca}\n|Ano:{self._ano}')


class Veiculocarro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self._portas = portas

    def info(self):
        super().info()
        print(f"|nº de portas:{self._portas}")


class Veiculomoto(Veiculo):
    def __init__(self, marca, ano, tipo):
        super().__init__(marca, ano)
        self._tipo = tipo

    def info(self):
        super().info()
        print(f"|Tipo:{self._tipo}")


def carro():
    carro_marca = input("Digite a Marca do seu Carro\n>>")
    carro_ano = int(input("Digite o Ano do seu Carro\n>>"))
    carro_portas = int(input("Digite o numero de portas do seu Carro\n>>"))
    carro1 = Veiculocarro(carro_marca, carro_ano, carro_portas)
    carro1.info()


def moto():
    marca_moto = input("Digite a Marca da sua Moto\n>> ")
    ano_moto = int(input("Digite o Ano da sua Moto\n>> "))
    tipo_moto = input("Digite o Tipo da sua Moto\n>> ")
    moto1 = Veiculomoto(marca_moto, ano_moto, tipo_moto)
    moto1.info()


def main():
    opcao = int(input("Qual veiculo deseja adicionar (digite o numero 1 e 2)\n1)Carro\n2)Moto\n>>"))
    if opcao == 1:
        print("preciso de algumas informaçãos...")
        print(80 * "_")
        carro()
    elif opcao == 2:
        print("preciso de algumas informaçãos...")
        print(80 * "_")
        moto()
    else:
        print("opção invalida")


main()
