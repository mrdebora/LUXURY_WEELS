class conta:
    quantidade_instancias = 0
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        conta.quantidade_instancias += 1
    def inf(self):
        print(f"titular:{self.titular}|saldo:{self.saldo}")

conta1 = conta("Débora","$13,045")
conta2 = conta("wellison","$9,123")

quantidade_comparacao = (conta.quantidade_instancias == 2)
comparar = conta1.saldo == conta2.saldo
print(f"Quantidade de instâncias criadas: {conta.quantidade_instancias}")
print(f"Os saldos das contas são iguais? {comparar}")
conta1.inf()
conta2.inf()
