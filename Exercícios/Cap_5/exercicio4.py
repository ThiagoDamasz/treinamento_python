numeros = [1, 2, 3, 4, 5]

def quadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

resutados = [(quadrado(n), cubo(n)) for n in numeros]

print(resutados)