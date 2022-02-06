import sys

def intro():
    print("*****************************************************************************")
    print('''
        Bem vindo à calculadora
    ''')

def calc():
    print("*****************************************************************************")
    opt = input('''
        Por favor, insira a operação desejada dentre as alternativas abaixo:
        Adição -> +
        Subtração -> -
        Multiplicação -> *
        Divisão -> /
        Potenciação -> **
        Módulo -> %
    ''')
    print("*****************************************************************************")

    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    if opt == "+":
        res = num1 + num2
        print("{} + {} = {}".format(num1, num2, res))

    elif opt == "-":
        res = num1 - num2
        print("{} - {} = {}".format(num1, num2, res))

    elif opt == "*":
        res = num1 * num2
        print("{} * {} = {}".format(num1, num2, res))

    elif opt =="/":
        res = num1 / num2
        print("{} / {} = {}".format(num1, num2, res))

    elif opt =="**":
        res = num1 ** num2
        print("{} ** {} = {}".format(num1, num2, res))
    
    elif opt =="%":
        res = num1 % num2
        print("{} % {} = {}".format(num1, num2, res))

    else:
        print("Operação inválida. Suspendendo o programa...")

    print("*****************************************************************************")
    newOperation()

def newOperation():
    again = input("Deseja realizar um segundo cálculo? ")
    print(again)

    if again == "Y" or again == "y":
        calc()

    elif again == "N" or again == "n":
        print("Finalizando a aplicação...")
        sys.exit()

    else:
        print("Opção inválida. Tente novamente")
        newOperation()

intro()
calc()