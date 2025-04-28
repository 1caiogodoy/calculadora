"""
Calculadora para realizar calculos simples.
# Com as mesmas funções da calculadora do Windows
"""


def soma():
    """
    Objetivo da função soma():
        Realizar a soma de N numeros que a pessoa desejar,
        apertando 0 para parar a soma
    Sem atributos obrigatórios
    """
    print("Digite 0 para parar a soma dos numeros")
    somar = 0
    while True:
        numeros = float(input("Digite um dos numeros que deseja somar: "))
        if numeros == 0:
            return (f"Resultado: {somar}")
        somar += numeros


def subtracao():
    """
    Objetivo da função subtração():
        Realizar a subtração de N numeros que a pessoa desejar,
        apertando 0 para parar a subtração
    Sem atributos obrigatórios
    """
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
    """
    Objetivo da função multiplicação():
        Realizar a multiplicação de N numeros que a pessoa desejar,
        apertando 0 para parar a multiplicação
    Sem atributos obrigatórios
    """
    print("Digite 0 para parar subtração dos numeros")
    vezes = 1
    while True:
        numeros = float(input("Digite um dos numeros que quer multiplicar: "))
        if numeros == 0:
            return (f"Resultado: {vezes}")
        vezes *= numeros


def divisao():
    """
    Objetivo da função divisão():
        Realizar a divisão de N numeros que a pessoa desejar,
        apertando 0 para parar a divisão
    Sem atributos obrigatórios
    """
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
    """
    Objetivo da função raiz():
        Realizar a raiz quadrada do número que a pessoa desejar,
    Sem atributos obrigatórios
    """
    raizQ = float(input(("Digite o numero que quer ver a raiz: "))) ** 0.5
    return f"resultado {raizQ}"


def potencia():
    """
    Objetivo da função potencia():
        Realizar uma conta de potenciação,
        com a base e o expoente que a pessoa desejar,
    Sem atributos obrigatórios
    """
    base = float(input("Digite a base que deseja: "))
    expoente = float(input("Digite o exponte que deseja: "))
    return f"Resutado: {base ** expoente}"


def inverso():
    """
    Objetivo da função inverso():
        Mostrar o inverso do número que a pessoa digitou
    Sem atributos obrigatórios
    """
    numero = float(input("Digite o numero que deseja ver o inverso: "))
    inversoo = 1 / numero
    return f"Resultado: {inversoo}\nou: {1/numero}"


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
