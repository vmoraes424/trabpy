import random
import os

times = [
    "Internacional x Bahia",
    "Grêmio x Caxias",
    "Vasco x Flamengo",
    "Fluminense x Ceará",
    "Brasil de Pelotas x Pelotas",
    "Corinthians x Gama",
]

nomes = []
apostas = []
valores = []

def salvaDados():
    arq = open("apostas.txt", "w")
    arq.write("Ola mundo!")

def carregaDados():
    # arq = open("apostas.txt", "r")
    pass

def cadastrar():
    nome = input("Digite seu nome: ")
    aposta = input("Seu palpite do jogo Ex.(2x1): ")
    valor = input("Digite o valor da aposta: ")

    nomes.append(nome)
    apostas.append(aposta)
    valores.append(valor)
    

def listarAposta():
    pass
def listarResultado():
    pass
def total():
    pass
def totalDeApostas():
    pass
def resultado():
    pass

carregaDados()
while True:
    print("")
    print("")
    print("BetPro - Controle de Apostas")
    print("")
    print("Jogo de hoje")
    timeEscolhido = print(random.choice(times))
    print("="*30)
    print("1 - Cadastrar Aposta")
    print("2 - Listar Aposta")
    print("3 - Listar Resultado")
    print("4 - Total de Apostas")
    print("5 - Apostas por Resultado")
    print("6 - Resultado e Premiação")
    print("7 - Finalizar")
    print()
    res = int(input("Selecione a opção: "))
    
    if res == 1:
        cadastrar()
    elif res == 2:
        listarAposta()
    elif res == 3:
        listarResultado()
    elif res == 4:
        total()
    elif res == 5:
        totalDeApostas()
    elif res == 6:
        resultado()
    elif res == 7:
        salvaDados()
            
    