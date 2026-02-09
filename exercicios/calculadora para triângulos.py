import math
import sys

print("bem vindo à calculadora de triângulos")
def calculolados():
    calculo = True
    while calculo:
        a = float(input("digite o ladoa>>"))
        b = float(input("digite o ladob>>"))
        c = float(input("digite o ladoc>>"))
        if a < b and b < a + c and c < a + b:
            print("os dados acima podem formar um triângulo ", end ='')
            if a==b==c:
                print("o triângulo é um Equilátero")
                calculoarea()
            elif a == b and b == c and a == c:
                print("o triângulo é um Isósceles")
                calculoarea()
            else:
                print("o triângulo é um Escaleno")
                calculoarea()
        else:
         print("os dados acima não podem forma um triângulo, tente outros dados!")
         calculolados()
def calculoarea():
        calculoarea = True
        while calculoarea:
            base = float(input("digite a base>> "))
            altura = float(input("digite a altura>> "))
            area = base * altura/ 2

            print("a area do triângulo é ",area,"cm²")

            sair = input("você deseja: \n1)fazer outro calculo \n2)sair\n>>")
            if sair == '1' or sair == 'fazer outro calculo':
                print('reiniciando...')
                calculolados()
            else:
                print("obrigada por ultilizar nossa calculadora, até breve!")
            sys.exit()


calculolados()


