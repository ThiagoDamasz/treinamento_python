print ("Cria uma lista com os números de 1 a 100 e imprime os números pares divisíveis por 4")
numeros = list(range(1,101))


for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)

#list comprehension
pares_divisiveis_por_4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
print(pares_divisiveis_por_4)        