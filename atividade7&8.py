def max(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_valor = max(lista[1:])
        return lista[0] if lista[0] > max_valor else max_valor
    
def min(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        min_valor = min(lista[1:])
        return lista[0] if lista[0] < min_valor else min_valor



lista = [5, 0, 8, 9, 98, 100, 546]
min_valor = min(lista)
max_valor = max(lista)
print(f'maior valor: {max_valor}')
print(f'menor valor: {min_valor}')