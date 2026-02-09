class ContaBancaria:
    quantidadeconta = 0

    def __init__(self, saldo, titular, conta):
        self.__saldo = saldo
        self.__titular = titular
        self.__conta = conta
        ContaBancaria.quantidadeconta += 1
    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia
            print(f"Depósito de {quantia} euros realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def levantar(self, quantia):
        if quantia > 0 and self.__saldo >= quantia:
            self.__saldo -= quantia
            print(f"Levantamento de {quantia} euros realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para levantamento.")


    def Verificarsaldo(self):
        print(f"possui {self.__saldo}euros ")
        print(80 * "_")


def adicionarconta():
    conta = int(input("digite o numero da sua conta\n>>"))
    titular = str(input("digite o titular da conta\n>>"))
    saldo = float(input("digite o saldo da sua conta\n>>"))
    return ContaBancaria(saldo, titular, conta)

def menu():
    print("Escolha uma opção digitando o numero (1, 2, 3, 4 e 5):")
    print("1)Criar nova conta")
    print("2)Exibir saldo da conta")
    print("3)Fazer levantamento")
    print("4)Fazer deposito")
    print("5)Sair")


def main():
    contas = []
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            conta = adicionarconta()
            contas.append(conta)
            print("conta criada com sucesso")
            print(80*"_")
        elif opcao == "2":
            if not contas:
                print("você ainda não tem conta adicionada")
            else:
                for conta in contas:
                    print("saldo:", end=" ")
                    conta.Verificarsaldo()
        elif opcao == "3":
            if not contas:
                print("você ainda não tem conta adicionada")
            else:
                quantia = float(input("Digite a quantia que deseja levantar\n>> "))
                for conta in contas:
                    conta.levantar(quantia)
        elif opcao == "4":
            if not contas:
                print("você ainda não tem conta adicionada")
            else:
                quantia = float(input("Digite o valor do depósito\n>> "))
                for conta in contas:
                    conta.depositar(quantia)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



main()