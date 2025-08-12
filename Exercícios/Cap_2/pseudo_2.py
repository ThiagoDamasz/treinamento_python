print("Bem vindo à Calculadora")
print("Digite o primeiro número:")
numero1 = float(input())
print("Digite o segundo número:")
numero2 = float(input())
print("Escolha a operação: (+, -, *, /)")
op = input() # ja retorna string

match op:
    case "+":
        resultado = numero1 + numero2
        print("Resultado: ", resultado)
    case "-":
        resultado = numero1 - numero2
        print("Resultado: ", resultado)
    case "*":    
        resultado = numero1 * numero2
        print("Resultado: ", resultado)
    case "/":
        if numero2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            resultado = None
        else:
            resultado = numero1 / numero2
            print("Resultado: ", resultado)        