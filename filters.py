def filtrar(lista, condicion):
    lista_filtrada = []
    for i in lista:
        if condicion(i):
            lista_filtrada.append(i)
    return lista_filtrada

def combinar_and(c1, c2):
    return lambda t: c1(t) and c2(t)

def combinar_or(c1, c2):
    return lambda t: c1(t) or c2(t)

def negar(c):
    return lambda t: not c(t)