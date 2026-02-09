class Pagamento:
    def Proc_pagamento(self):
        print("seu pagamento está generico sendo processado")


class Cartaocredito(Pagamento):
    def Proc_pagamento(self):
        print("seu pagamento no Cartão de Crédito está sendo processado...")


class Paypal(Pagamento):
   def Proc_pagamento(self):
        print("seu pagamento no Paypal está sendo processado...")



def main():
    opcao = int(input("digite o numero(1 ou 2) para a forma de pagamento desejada:\n1)Cartão de Crédito\n2)PayPal\n>>"))
    if opcao == 1:
        print("você escolheu a forma de pagamento |Cartão de Crédito")
        formadepagamento = Cartaocredito()
    elif opcao == 2:
        print("você escolheu a forma de pagamento |PayPal")
        formadepagamento = Paypal()
    else:
        print("Opção invalida.tente novamente")
    formadepagamento.Proc_pagamento()

main()