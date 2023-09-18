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
    global nomes, apostas, valores, total_vasco, total_sorocaba, total_empate
    with open("apostas.txt", "r") as arq:
        for linha in arq:
            nome, palpite, valor = linha.strip().split(";")
            nomes.append(nome)
            apostas.append(palpite)
            valores.append(float(valor))
            gols_palpite = palpite.split("x")
            gols_vasco = int(gols_palpite[0].strip())
            gols_sorocaba = int(gols_palpite[1].strip())
            if gols_vasco > gols_sorocaba:
                total_vasco += 1
            elif gols_sorocaba > gols_vasco:
                total_sorocaba += 1
            else:
                total_empate += 1


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

    gols_palpite = palpite.split("x")
    gols_vasco = int(gols_palpite[0].strip())
    gols_sorocaba = int(gols_palpite[1].strip())

    if gols_vasco > gols_sorocaba:
        total_vasco += 1
    elif gols_sorocaba > gols_vasco:
        total_sorocaba += 1
    else:
        total_empate += 1


def calcularResultado(palpite):
    gols_time1, gols_time2 = map(int, palpite.split("x"))
    if gols_time1 > gols_time2:
        return f"{time1}"
    elif gols_time1 < gols_time2:
        return f"{time2}"
    else:
        return "Empate"


def listarResultado():
    if len(nomes) == 0:
        print("Nenhuma aposta registrada.")
    else:
        print("Resultado das Apostas:")
        for i in range(len(nomes)):
            print("")
            print(
                f"{nomes[i]} apostou em '{apostas[i]}'. Palpite: {calcularResultado(apostas[i])}"
            )
            print("")


def listarAposta():
    for aposta in apostas:
        print(aposta, end=", ")


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
    global total_vasco, total_sorocaba, total_empate

    gols_vasco, gols_sorocaba = map(int, resultado.split("x"))

    total_apostado = sum(valores)

    print("")
    print("")
    print("Resultado da partida:", resultado)
    print("Total apostado:", total_apostado)

    apostadores_ganhadores = []

    if gols_vasco > gols_sorocaba:
        print(f"Ganhadores apostando em {time1}:")
        for i in range(len(nomes)):
            if apostas[i] == f"{gols_vasco}x{gols_sorocaba}":
                apostadores_ganhadores.append(nomes[i])
    elif gols_sorocaba > gols_vasco:
        print(f"Ganhadores apostando em {time2}:")
        for i in range(len(nomes)):
            if apostas[i] == f"{gols_vasco}x{gols_sorocaba}":
                apostadores_ganhadores.append(nomes[i])
    else:
        print("Ganhadores apostando em empate:")
        for i in range(len(nomes)):
            if apostas[i] == f"{gols_vasco}x{gols_sorocaba}":
                apostadores_ganhadores.append(nomes[i])

    if len(apostadores_ganhadores) == 0:
        print("Nenhum ganhador para este resultado.")
    else:
        premio_por_apostador = total_apostado / len(apostadores_ganhadores)
        for apostador in apostadores_ganhadores:
            print(f"- {apostador} ganhou R${premio_por_apostador:.2f}")


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
        resultadoPremiacao("1x2")
    elif res == 7:
        salvaDados()
        break
