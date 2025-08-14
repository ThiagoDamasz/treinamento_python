listaA = [2, 3, 4]
listaB = [10, 11, 12]

resultado = [a ** b for a, b in zip(listaA, listaB)]
print(resultado)