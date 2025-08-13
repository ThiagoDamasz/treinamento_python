def recebe_lista(list):
    list.append(5)
    list.append(6)
    return list

lista = [1,2,3,4]
recebe_lista(lista)
print(lista)