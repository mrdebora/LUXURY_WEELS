from abc import ABC, abstractmethod

class Herois(ABC):

    @abstractmethod
    def atacar(self, oponente):
        pass

    @abstractmethod
    def defender(self, dano):
        pass

    @abstractmethod
    def obtervida(self):
        pass

class Superman(Herois):
    def __init__(self):
        self.vida = 100

    def atacar(self, oponente):
        print("Superman ataca com soco forte!")
        oponente.defender(20)

    def defender(self, dano):
        danoreduzido = max(0, dano - 5)
        self.vida -= danoreduzido
        print(f"Superman defende e reduz o dano para {danoreduzido}. Vida restante: {self.vida}")

    def obtervida(self):
        return self.vida

class Mulhermaravilha(Herois):
    def __init__(self):
        self.vida = 100

    def atacar(self, oponente):
        print("Mulhermaravilha ataca com soco forte!")
        oponente.defender(20)

    def defender(self, dano):
        danoreduzido = max(0, dano - 3)
        self.vida -= danoreduzido
        print(f"Mulhermaravilha defende e reduz o dano para {danoreduzido}. Vida restante: {self.vida}")

    def obtervida(self):
        return self.vida

def escolha(nome):
    if nome.lower() == "mulhermaravilha":
        return Mulhermaravilha()
    elif nome.lower() == "superman":
        return Superman()
    else:
        raise ValueError("Personagem indisponível")

def main():
    print("Escolha seu primeiro personagem (Mulhermaravilha, Superman):")
    nome1 = input("(é importante que esteja escrito corretamente)\n>>")
    personagem1 = escolha(nome1)

    print("Escolha seu segundo personagem (Mulhermaravilha, Superman):")
    nome2 = input("(é importante que esteja escrito corretamente)\n>>")
    personagem2 = escolha(nome2)

    rodadas = 1
    while personagem1.obtervida() > 0 and personagem2.obtervida() > 0:
        print(f"\nRodada: {rodadas}")
        if rodadas % 2 == 1:
            personagem1.atacar(personagem2)
        else:
            personagem2.atacar(personagem1)
        rodadas += 1

    if personagem1.obtervida() > 0:
        print(f"\n{nome1} venceu!")
    else:
        print(f"\n{nome2} venceu!")

main()
