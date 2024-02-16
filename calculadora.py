import time

def soma(valor1,valor2):
    return valor1 + valor2
  
def multiplica(valor1,valor2):
    return valor1 * valor2

def subtracao(valor1,valor2):
    return valor1 - valor2

def divisao(valor1,valor2):
    return valor1 / valor2

def leOperador():
    return input('''
    Qual operador deseja usar ? 
    + para soma
    - para subtração
    * para multiplicação
    / para divisão

    ''')
    
def main():  
    while True:
        operacao = leOperador()

        if operacao in ["+", "-", "*", "/"]:
            valor1 = float(input("Qual o Primeiro Valor: "))
            valor2 = float(input("Qual o Segundo Valor: "))

            if operacao == "+":
                resultado = soma(valor1, valor2)
                print(f'A soma é {resultado}')

            elif operacao == "-":
                resultado = subtracao(valor1, valor2)
                print(f'A Subtração é {resultado}')

            elif operacao == "*":
                resultado = multiplica(valor1, valor2)
                print(f'A Multiplicação é {resultado}')
        
            elif operacao == "/":
                resultado = divisao(valor1, valor2)
                print(f'A divisão é {resultado}')

            break

        else:
            print('Operação não encontrada, reiniciando calculadora')
            time.sleep(1)
            print("---------------------------------")
            continue
    
    
print("Bem Vindo a Calculadora Simples !")

while True:
    main()
    continuar = input("Deseja Realizar nova Operação? S/N: ").upper()
    if continuar != "S":
        print("Obrigado por usar a Calculadora!")
        break