class Carro:
    vencedor = ""

    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade

    def correr(self, distancia):
        tempo_base = distancia / self.velocidade
        return tempo_base


def corrida(carros, distancia):
    tempos = {}
    for carro in carros:
        tempo = carro.correr(distancia)
        tempos[carro.nome] = tempo
        print(f"Carro {carro.nome} completou a corrida em {tempo:.2f} minutos")

    vencedor = min(tempos)
    Carro.vencedor = vencedor

    print(f"\nO vencedor da corrida é {Carro.vencedor} com um tempo de {tempos[Carro.vencedor]:.2f} minutos")


def main():

    carro1 = Carro("renault", 150)
    carro2 = Carro("porshe", 160)
    carro3 = Carro("brabux", 170)
    carros = [carro1, carro2, carro3]
    print("escolha seu carro de acordo com os numeros (1,2 e 3)")
    for i, carro in enumerate(carros):
        print(f"{i+1})carro:{carro.nome}|velocidade:{carro.velocidade}km")
    opcao = input('>>')
    if opcao in ["1", "2", "3"]:
        escolhido = carros[int(opcao) - 1]
        print(f"Você escolheu carro:{escolhido.nome}|velocidade:{escolhido.velocidade}km")
    else:
        print("Opção inválida")
        return

    distancia = 100

    corrida(carros, distancia)


main()
