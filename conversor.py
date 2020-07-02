def menu_inicial():
    print("Bem vindo ao conversor de temperatura")
    print("Selecione as opções: \n","1 - Celsius-Fahrenheit\n","2 - Fahrenheit-Celsius\n","3 - Kelvin-Celsius \n")

def celsius_fahr():
    C = float(input("Digite o valor em Celsius: \n"))
    F = C * (9 / 5) + 32
    print("Valor em Fahrenheit: {0} °F".format(F))


def fahr_celsius():
    F = float(input("Digite o valor em Fahrenhei: \n"))
    C = (F-32) *(5/9)
    print("Valor em Celsius: {0} °C".format(C))

def celsius_kevin():
    C = float(input("Digite o valor em Celsius:"))
    K = (C + 273.5)
    print("Valor em kelvin: {0} K".format(K))


if __name__ == "__main__":
    menu_inicial()
    escolha = input("escolha o tipo de conversão que deseja fazer: ")
    if escolha == "1":
        celsius_fahr()
    if escolha == "2":
        fahr_celsius()
    if escolha == "3":
        celsius_kevin()