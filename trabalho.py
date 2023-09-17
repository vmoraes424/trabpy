time1 = "Vasco"
time2 = "Sorocaba"

nomes = []
apostas = []
valores = []

total_vasco = 0
total_sorocaba = 0
total_empate = 0

def salvaDados():
    with open("apostas.txt", "w") as arq:
        for i in range(len(nomes)):
            arq.write(f"{nomes[i]};{apostas[i]};{valores[i]}\n")

def carregaDados():
    pass

def cadastrar():
    global total_vasco
    global total_sorocaba
    global total_empate

    nome = input("Digite seu nome: ")
    palpite = input(f"Seu palpite do jogo Ex.(2x1): ")
    valor = input("Digite o valor da aposta: ")

    nomes.append(nome)
    apostas.append(palpite)
    valores.append(valor)

    gols_palpite = palpite.split('x')
    gols_vasco = int(gols_palpite[0].strip())
    gols_sorocaba = int(gols_palpite[1].strip())

    if gols_vasco > gols_sorocaba:
        total_vasco += 1
    elif gols_sorocaba > gols_vasco:
        total_sorocaba += 1
    else:
        total_empate += 1


def calcularResultado(palpite):
    gols_time1, gols_time2 = map(int, palpite.split('x'))
    if gols_time1 > gols_time2:
        return f"{time1} venceu"
    elif gols_time1 < gols_time2:
        return f"{time2} venceu"
    else:
        return "Empate"


def listarResultado():
    if len(nomes) == 0:
        print("Nenhuma aposta registrada.")
    else:
        print("Resultado das Apostas:")
        for i in range(len(nomes)):
            print("")
            print(f"{nomes[i]} apostou em '{apostas[i]}'. Resultado: {calcularResultado(apostas[i])}")
            print("")

def listarAposta():
    pass

def totalDeApostas():
    print("")
    print("")
    print(f"Total de apostas: {len(nomes)}")
    print(f"Total apostado: R${sum(valores)}")

def totalDeApostasPorResultado():
    print("")
    print("")
    print("Total de apostas por resultado:")
    print("")
    print(f"{time1}: {total_vasco} apostas")
    print(f"{time2}: {total_sorocaba} apostas")
    print(f"Empate: {total_empate} apostas")

def resultadoPremiacao(resultado):
    global total_vasco
    global total_sorocaba
    global total_empate

    gols_vasco, gols_sorocaba = map(int, resultado.split('x'))

    total_apostado = total_vasco + total_sorocaba + total_empate

    print("Resultado da partida:", resultado)

    print("Ganhadores:")
    if gols_vasco > gols_sorocaba:
        print(f"- Apostas em {time1} ganharam. Cada apostador receberá o dobro do valor apostado.")
        premio = 2 * total_vasco
    elif gols_sorocaba > gols_vasco:
        print(f"- Apostas em {time2} ganharam. Cada apostador receberá o dobro do valor apostado.")
        premio = 2 * total_sorocaba
    else:
        print("- Apostas em empate ganharam. Cada apostador receberá o dobro do valor apostado.")
        premio = 2 * total_empate

    print("Total apostado:", total_apostado)
    print("Total a ser distribuído em prêmios:", premio)

carregaDados()
while True:
    print("")
    print("BetPro - Controle de Apostas")
    print("")
    print(f"{time1} x {time2}")
    print("=" * 30)
    print("1 - Cadastrar Aposta")
    print("2 - Listar Apostas")
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
        totalDeApostas()
    elif res == 5:
        totalDeApostasPorResultado()
    elif res == 6:
        resultado = calcularResultado(f'{time1} x {time2}')
        print("Resultado do jogo:", resultado)
        resultadoPremiacao(resultado)
    elif res == 7:
        salvaDados()
        break