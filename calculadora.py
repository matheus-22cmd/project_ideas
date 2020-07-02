def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicao(x,y):
    return x * y


def divisao(x,y):
    return x/y

print("Tela de seleção")
print( "1 - Adição\n", "2 - Subtração\n","3 - Multiplicação\n","4 - Divisão\n")

while True:
  
    escolha= input("Enter choice(1/2/3/4): ")

    
    if escolha in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicao(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))
        break
    else:
        print("Invalid Input")