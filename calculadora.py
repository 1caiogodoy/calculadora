# fazer uma calcudora com as mesmas funções do calculadora do windows


def soma():
    print("Digite 0 para parar a soma dos numeros")
    somar = 0
    while True:
        numeros = float(input("Digite um dos numeros que deseja somar: "))
        if numeros == 0:
            return (f"Resultado: {somar}")
        somar += numeros


def subtracao():
    print("Digite 0 para parar subtração dos numeros")
    contador = 0
    menos = 0
    while True:
        contador += 1
        numeros = float(input("Digite um dos numeros que deseja subtrair: "))
        if numeros == 0:
            return (f"Resultado: {menos}")
        if contador == 1:
            menos = numeros
        else:
            menos -= numeros


def multiplicacao():
    print("Digite 0 para parar subtração dos numeros")
    vezes = 1
    while True:
        numeros = float(input("Digite um dos numeros que quer multiplicar: "))
        if numeros == 0:
            return (f"Resultado: {vezes}")
        vezes *= numeros


def divisao():
    print("Digite 0 para parar subtração dos numeros")
    divisaoo = 1
    contador = 0
    while True:
        contador += 1
        numeros = float(input("Digite um dos numeros que deseja dividir: "))
        if numeros == 0:
            return f"Resultado: {divisaoo}"
        if contador == 1:
            divisaoo = numeros
        else:
            divisaoo /= numeros


def raiz():
    raizQ = float(input(("Digite o numero que quer ver a raiz: "))) ** 0.5
    return f"resultado {raizQ}"


def potencia():
    base = float(input("Digite a base que deseja: "))
    expoente = float(input("Digite o exponte que deseja: "))
    return f"Resutado: {base ** expoente}"


def inverso():
    numero = 1 / float(input("Digite o numero que deseja ver o inverso: "))
    return f"Resultado: {numero}"


def calculadora():
    while True:
        escolha = str(input("Escolha o calculo que deseja fazer\n"
                            "(digite qualquer coisa para parar): "))
        if escolha in ["soma", "somar", "mais", "+", "adcionar"]:
            print(soma())
        elif escolha in ["diminuir", "subtrair", "subtração", "subtracao",
                         "subtraçao", "reduzir", "-"]:
            print(subtracao())
        elif escolha in ["vezes", "*", "x", "multiplicar", "multiplica",
                         "multiplicação", "multiplicacao", "multiplicaçao"]:
            print(multiplicacao())
        elif escolha in ["dividir", "divisao", "divisão"]:
            print(divisao())
        elif escolha in ["raiz", "raiz quadrada", "√"]:
            print(raiz())
        elif escolha in ["potencia", "expoente"]:
            print(potencia())
        elif escolha in ["inverso", "um dvidido pelo numero"]:
            print(inverso())
        else:
            return ("Obrigado por confiar nos nossos calculos")


print(calculadora())
